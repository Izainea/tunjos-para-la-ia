# Cuaderno de apoyo con kappa, alfa, consultas y exportación del libro

Opcional. Todo el curso se puede hacer con la interfaz web de un modelo y una hoja de cálculo. Este cuaderno es para quien quiera calcular el acuerdo con exactitud, ejecutar consultas al corpus como las de un programa de análisis cualitativo, exportar el libro de códigos y, si lo desea, llamar a un modelo por programa dejando registro. Está pensado para que lo use alguien sin experiencia previa en Python, copiando bloque a bloque. Cada bloque dice antes qué hace y por qué.

## Preparación

Instale Python 3.11 o superior. En una terminal:

```
pip install pandas
```

Solo el último bloque, la llamada opcional a un modelo, necesita además:

```
pip install openai python-dotenv
```

## El formato de trabajo

Todo el cuaderno trabaja sobre dos archivos de texto separados por comas, que se pueden crear y editar en cualquier hoja de cálculo.

`fragmentos.csv`, un fragmento por fila:

```
id,fuente,texto
1,entrevista-03,"Yo le compro a la misma señora desde hace años."
2,entrevista-03,"Los sábados vengo más por ver gente que por comprar."
```

`codificacion.csv`, una fila por asignación de código, con quién lo asignó:

```
id,codigo,codificador
1,confianza en el vendedor,yo
1,confianza en el vendedor,modelo
2,encuentro vecinal,yo
2,encuentro vecinal,modelo
```

Un fragmento puede tener varias filas por codificador si la codificación es múltiple. Para la matriz de acuerdo de la semana 6 se usa un código por fragmento y codificador.

## Semana 6. Kappa de Cohen

Kappa compara el acuerdo observado entre dos codificadores con el que se esperaría por azar dadas las distribuciones de cada uno. El bloque lee las asignaciones de dos codificadores, alinea los fragmentos que ambos codificaron, y calcula po, pe y kappa. Un código fuera del libro cuenta como categoría aparte, como pide la práctica.

```python
import pandas as pd

cod = pd.read_csv("codificacion.csv")

def tabla_dos(cod, a="yo", b="modelo"):
    """Devuelve un DataFrame con una fila por fragmento y una columna por codificador."""
    t = cod.pivot_table(index="id", columns="codificador", values="codigo", aggfunc="first")
    t = t.dropna(subset=[a, b])
    return t[[a, b]]

def kappa_cohen(t):
    a, b = t.columns
    n = len(t)
    po = (t[a] == t[b]).mean()
    cats = sorted(set(t[a]) | set(t[b]))
    pe = sum((t[a] == c).sum() * (t[b] == c).sum() for c in cats) / (n * n)
    k = (po - pe) / (1 - pe) if pe != 1 else float("nan")
    return {"n": n, "categorias": len(cats), "po": round(po, 3), "pe": round(pe, 3), "kappa": round(k, 3)}

t = tabla_dos(cod)
print(kappa_cohen(t))
```

Para reportar con coma decimal, como pide el curso:

```python
r = kappa_cohen(t)
print(f"Acuerdo simple: {r['po']*100:.1f} %".replace(".", ","))
print(f"kappa = ({r['po']} - {r['pe']}) / (1 - {r['pe']}) = {r['kappa']}".replace(".", ","))
```

## Semana 6. Alfa nominal de Krippendorff

Alfa generaliza la idea a cualquier número de codificadores y admite fragmentos que no todos codificaron. Para datos nominales, el bloque calcula el desacuerdo observado y el esperado a partir de la matriz de coincidencias, siguiendo la definición de Krippendorff (2018, capítulo sobre fiabilidad). Con dos codificadores y datos completos, el valor suele quedar cerca de kappa.

```python
import pandas as pd
from collections import Counter

def alfa_krippendorff_nominal(cod):
    """cod: DataFrame con columnas id, codigo, codificador. Un código por fragmento y codificador."""
    t = cod.pivot_table(index="id", columns="codificador", values="codigo", aggfunc="first")
    # matriz de coincidencias: pares ordenados de valores dentro de cada unidad
    coinc = Counter()
    n_total = 0
    for _, fila in t.iterrows():
        vals = [v for v in fila.tolist() if pd.notna(v)]
        m = len(vals)
        if m < 2:
            continue
        n_total += m
        for i in range(m):
            for j in range(m):
                if i != j:
                    coinc[(vals[i], vals[j])] += 1 / (m - 1)
    if n_total == 0:
        return float("nan")
    n_c = Counter()
    for (c, k), v in coinc.items():
        n_c[c] += v
    do = sum(v for (c, k), v in coinc.items() if c != k) / n_total
    de = sum(n_c[c] * n_c[k] for c in n_c for k in n_c if c != k) / (n_total * (n_total - 1))
    return round(1 - do / de, 3) if de else float("nan")

cod = pd.read_csv("codificacion.csv")
print("alfa =", alfa_krippendorff_nominal(cod))
```

Prueba del bloque sobre el caso de doce fragmentos del simulador de la semana 3: con los códigos del modelo y una codificación de referencia (fragmentos 3, 4, 8, 9 y 12 en desacuerdo), kappa da 0,54 y alfa queda en el mismo orden. Si su resultado difiere mucho entre las dos medidas con datos completos, revise que no haya fragmentos duplicados en el archivo.

Para un tercer codificador basta añadir sus filas a `codificacion.csv` con otro valor en la columna `codificador`; alfa lo incorpora sin cambios, y kappa se calcula por pares.

## Semana 5. Consultas al corpus como las de un CAQDAS

Las consultas de recuperación, coocurrencia y matriz por fuente son operaciones sobre el registro: dado el libro y las asignaciones, el resultado es único. Estos bloques las ejecutan sobre los dos archivos. Lo que devuelven es lo que se le pasa al modelo, numerado, en el protocolo de la semana 5.

```python
import pandas as pd

frag = pd.read_csv("fragmentos.csv")
cod = pd.read_csv("codificacion.csv")
mias = cod[cod["codificador"] == "yo"]

def recuperar(codigo):
    """Todos los fragmentos con un código, con su texto."""
    ids = mias.loc[mias["codigo"] == codigo, "id"].unique()
    return frag[frag["id"].isin(ids)]

def coocurrencia(c1, c2):
    """Fragmentos que tienen los dos códigos a la vez."""
    a = set(mias.loc[mias["codigo"] == c1, "id"])
    b = set(mias.loc[mias["codigo"] == c2, "id"])
    return frag[frag["id"].isin(a & b)]

def matriz_por_fuente():
    """Cuántos fragmentos de cada fuente llevan cada código."""
    m = mias.merge(frag[["id", "fuente"]], on="id")
    return pd.crosstab(m["codigo"], m["fuente"])

print(recuperar("confianza en el vendedor"))
print(coocurrencia("confianza en el vendedor", "encuentro vecinal"))
print(matriz_por_fuente())
```

Para pasarle al modelo solo los fragmentos recuperados, numerados:

```python
def para_el_modelo(df):
    return "\n".join(f"[{r.id}] {r.texto}" for r in df.itertuples())

print(para_el_modelo(coocurrencia("confianza en el vendedor", "encuentro vecinal")))
```

## Semana 7. Curva de códigos nuevos por lote

La curva cuenta, para lotes sucesivos de fragmentos, cuántos códigos aparecen por primera vez. Es un instrumento de registro: cuenta códigos, no mide la saturación de propiedades. El bloque la calcula con lotes de diez.

```python
import pandas as pd

cod = pd.read_csv("codificacion.csv")
mias = cod[cod["codificador"] == "yo"].sort_values("id")
vistos, curva = set(), []
for inicio in range(mias["id"].min(), mias["id"].max() + 1, 10):
    lote = mias[(mias["id"] >= inicio) & (mias["id"] < inicio + 10)]
    nuevos = sorted(set(lote["codigo"]) - vistos)
    vistos |= set(nuevos)
    curva.append({"lote": f"{inicio}-{inicio+9}", "nuevos": len(nuevos), "acumulados": len(vistos), "nombres": "; ".join(nuevos)})
print(pd.DataFrame(curva).to_string(index=False))
```

## Semana 8. Exportar el libro de códigos

El libro se mantiene en `libro.csv` con las columnas de la plantilla, y el bloque lo convierte en la tabla markdown de `plantillas/libro-de-codigos.md`, con los fragmentos de anclaje tomados del archivo de codificación.

```
codigo,definicion,incluye,excluye,origen,decision,criterio,responde
confianza en el vendedor,"Relación sostenida ...","compras repetidas ...","confianza del vendedor al comprador ...",modelo,corregí,"la definición era unidireccional",yo
```

```python
import pandas as pd

libro = pd.read_csv("libro.csv")
cod = pd.read_csv("codificacion.csv")
mias = cod[cod["codificador"] == "yo"]
anclaje = mias.groupby("codigo")["id"].apply(lambda s: ", ".join(str(i) for i in sorted(s)))
libro["fragmentos de anclaje"] = libro["codigo"].map(anclaje).fillna("")
cols = ["codigo", "definicion", "incluye", "excluye", "fragmentos de anclaje", "origen", "decision", "criterio", "responde"]
with open("libro-de-codigos.md", "w", encoding="utf-8") as f:
    f.write("| " + " | ".join(cols) + " |\n|" + "---|" * len(cols) + "\n")
    for r in libro[cols].itertuples(index=False):
        f.write("| " + " | ".join(str(x).replace("|", "/") for x in r) + " |\n")
print("libro-de-codigos.md escrito")
```

Las cifras de la sección 4 de la plantilla salen de:

```python
print(libro.groupby(["origen", "decision"]).size())
```

## Opcional. Llamar a un modelo por programa con registro

Para quien prefiera no usar la interfaz web. La biblioteca `openai` sirve para cualquier proveedor compatible con su interfaz; cambie `base_url` según el caso. El curso no exige un proveedor y varios ofrecen cuota gratuita. La clave se guarda en un archivo `.env` que no se comparte ni se entrega.

```
API_KEY=su_clave
BASE_URL=https://api.openai.com/v1
MODEL=nombre_del_modelo
```

```python
import os, json, datetime
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("API_KEY"), base_url=os.getenv("BASE_URL"))
MODEL = os.getenv("MODEL")

def preguntar(prompt, registro="registro.jsonl"):
    """Envía un prompt, devuelve la respuesta y guarda ambos con fecha."""
    r = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    texto = r.choices[0].message.content
    with open(registro, "a", encoding="utf-8") as f:
        f.write(json.dumps({
            "fecha": datetime.datetime.now().isoformat(),
            "modelo": MODEL,
            "prompt": prompt,
            "respuesta": texto,
        }, ensure_ascii=False) + "\n")
    return texto
```

Aplicar el libro fijo a treinta fragmentos (práctica 6) y guardar la salida en el formato de `codificacion.csv`:

```python
import pandas as pd

frag = pd.read_csv("fragmentos.csv")
libro_txt = open("libro.md", encoding="utf-8").read()
lote = frag[frag["id"].between(1, 30)]
prompt = f"""Este es un libro de códigos:
{libro_txt}

Codifica los siguientes fragmentos aplicando exactamente este libro. Un solo
código por fragmento. No propongas códigos nuevos: si ninguno cabe, escribe
"ninguno". Responde solo con líneas de la forma: id;codigo

{chr(10).join(f'[{r.id}] {r.texto}' for r in lote.itertuples())}"""
salida = preguntar(prompt)
filas = [l.split(";") for l in salida.strip().splitlines() if ";" in l]
pd.DataFrame([{"id": int(i.strip("[] ")), "codigo": c.strip(), "codificador": "modelo"} for i, c in filas]) \
  .to_csv("codificacion-modelo.csv", index=False)
```

Luego se concatena con las filas propias y se corre el bloque de kappa. Cada llamada queda en `registro.jsonl`, que es el anexo literal que piden las plantillas.

## Nota sobre costos y privacidad

Use cuotas gratuitas y material sin datos personales de terceros. Si su proyecto incluye material sensible, haga las prácticas con una muestra anonimizada o con material público, y procese el material solo con servicios cuyas condiciones excluyan el uso de los datos para entrenamiento. [*Exterioridad y gobernanza de la IA en ciencias sociales*](../../curso-7-etica-gobernanza/README.md) trata estos problemas en detalle: qué derechos pesan sobre cada pieza del material (autoría, datos personales, material sensible, condiciones de las plataformas), qué uso es defendible y hasta dónde llega la anonimización; su primer producto es una matriz de riesgos y derechos del propio material.
