# Cuaderno de apoyo en Python para construir el corpus

Este cuaderno acompaña las ocho semanas. Está escrito para alguien que nunca ha programado: cada bloque lleva antes una explicación de qué hace y por qué, y se puede copiar tal cual en una celda del cuaderno propio. Los bloques usan el caso demostrativo del curso; para el corpus propio basta cambiar las rutas y los nombres. Todo el software es libre.

Regla del curso: antes de cada bloque de código, una celda de texto con sus palabras que diga qué decisión encarna. Después de cada sesión, reiniciar el núcleo y ejecutar todo de arriba abajo.

## Preparación

Instale Python 3.11 o superior desde https://www.python.org/ y, en una terminal, las bibliotecas del curso:

```
pip install jupyterlab pandas requests beautifulsoup4
```

Abra el cuaderno con `jupyter lab`. Si la instalación no es posible, cualquier servicio gratuito de cuadernos en la nube sirve; suba la carpeta `crudo` y trabaje igual.

Estructura de carpetas del proyecto, que el cuaderno espera:

```
mi-corpus/
  crudo/          archivos tal como llegaron; no se editan
  limpio/         archivos en UTF-8, limpios
  cuadernos/      los cuadernos del curso
  decisiones.csv  decisiones a mano, con fecha
  catalogo.csv    generado por el cuaderno
```

## Semana 2. Leer archivos y escribir el primer registro

Una cadena es un texto en una variable. Se le pueden hacer preguntas que la máquina responde sin interpretar.

```python
texto = "El día de ayer se reunió la junta en el salón de sesiones del concejo."
print(len(texto))                 # cuántos caracteres
print(texto[:20])                 # los primeros veinte
print("junta" in texto)           # ¿contiene la palabra?
print(texto.lower())              # todo en minúsculas
print(texto.split()[:5])          # las primeras cinco palabras
```

Abrir un archivo exige declarar su codificación. El curso usa UTF-8 siempre.

```python
from pathlib import Path

ruta = Path("crudo") / "P-0001.txt"
texto = ruta.read_text(encoding="utf-8")
print(ruta.name, len(texto), "caracteres")
print(texto.splitlines()[0])      # la primera línea
```

`pathlib` recorre una carpeta y devuelve sus archivos como una lista. Esa lista es la primera forma del corpus.

```python
rutas = sorted(Path("crudo").glob("*.txt"))
print(len(rutas), "archivos")
for r in rutas[:3]:
    print(r.name)
```

Un diccionario es un registro con campos nombrados. Una lista de diccionarios es un catálogo rudimentario. El bucle hace con cada archivo lo que el investigador haría con uno.

```python
import datetime

registro = []
for r in rutas:
    t = r.read_text(encoding="utf-8")
    registro.append({
        "archivo": r.name,
        "bytes": r.stat().st_size,
        "caracteres": len(t),
        "primera_linea": t.splitlines()[0] if t.strip() else "",
        "fecha_lectura": datetime.datetime.now().isoformat(timespec="minutes"),
    })
registro[0]
```

Una función es un criterio escrito una vez. Esta encarna un criterio del protocolo preliminar: entra lo que tiene más de doscientos caracteres y contiene una fecha con cuatro dígitos. Cambie el criterio por el suyo y escriba arriba de dónde viene.

```python
import re

def entra(texto):
    """Criterio 1 del protocolo: longitud mínima y fecha legible."""
    tiene_fecha = re.search(r"\b1[89]\d\d\b|\b20\d\d\b", texto) is not None
    return len(texto) > 200 and tiene_fecha

for fila, r in zip(registro, rutas):
    fila["entra"] = entra(r.read_text(encoding="utf-8"))
```

El registro se escribe en un archivo CSV que cualquier hoja de cálculo abre. Es el primer producto del código.

```python
import csv

campos = list(registro[0].keys())
with open("registro.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=campos)
    w.writeheader()
    w.writerows(registro)
print("registro.csv escrito con", len(registro), "filas")
```

## Semana 3. Recolección reproducible

Antes de pedir nada, se lee lo que el sitio declara. Python trae un lector de `robots.txt` en la biblioteca estándar.

```python
from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
rp.set_url("https://www.datos.gov.co/robots.txt")
rp.read()
print(rp.can_fetch("corpus-curso2", "https://www.datos.gov.co/resource/"))
```

La función de descarga encarna la cortesía técnica: se identifica, espera, guarda lo que llegó sin tocarlo, calcula el hash y anota la bitácora. Cambie el correo por el suyo. Si el sitio responde con error, la función lo anota y no insiste.

```python
import requests, time, hashlib, json, datetime
from pathlib import Path

CABECERAS = {"User-Agent": "corpus-curso2 (investigacion; su-correo@ejemplo.org)"}
PAUSA = 1.0  # segundos entre peticiones

def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()

def descargar(url, destino, bitacora="bitacora_descarga.jsonl"):
    """Pide url, guarda la respuesta intacta en destino y anota la bitácora."""
    fila = {"url": url, "destino": str(destino),
            "fecha_descarga": datetime.datetime.now().isoformat(timespec="minutes")}
    try:
        r = requests.get(url, headers=CABECERAS, timeout=30)
        fila["estado"] = r.status_code
        if r.ok:
            Path(destino).write_bytes(r.content)
            fila["hash_sha256"] = sha256_bytes(r.content)
            fila["bytes"] = len(r.content)
    except requests.RequestException as e:
        fila["estado"] = "error"
        fila["detalle"] = str(e)
    with open(bitacora, "a", encoding="utf-8") as f:
        f.write(json.dumps(fila, ensure_ascii=False) + "\n")
    time.sleep(PAUSA)
    return fila
```

La lista de lo que se pide se escribe antes y se revisa a mano. Aquí, una norma de la Secretaría del Senado y un conjunto de datos abiertos por su interfaz de programación. El protocolo dice qué va en esta lista; el programa solo la recorre.

```python
Path("crudo").mkdir(exist_ok=True)

pedidos = [
    ("http://www.secretariasenado.gov.co/senado/basedoc/ley_0023_1982.html", "crudo/N-0001.html"),
    ("https://www.datos.gov.co/resource/XXXX-XXXX.csv?$limit=500", "crudo/D-0001.csv"),
]
for url, destino in pedidos:
    print(descargar(url, destino))
```

Reemplace `XXXX-XXXX` por el identificador del conjunto de datos que eligió en datos.gov.co; aparece en la dirección de cada conjunto. Para extraer el texto de una página HTML se usa Beautiful Soup, pero eso ocurre en la semana 5, sobre una copia: `crudo` no se toca.

Comparar dos ejecuciones es comparar hash. Este bloque lee la bitácora y señala las direcciones cuyo contenido cambió.

```python
import pandas as pd

b = pd.read_json("bitacora_descarga.jsonl", lines=True)
cambios = b.groupby("url")["hash_sha256"].nunique()
print(cambios[cambios > 1])   # vacío si nada cambió entre ejecuciones
```

## Semana 4. El catálogo maestro con pandas

El hash de cada archivo en `crudo` es la base del catálogo. Se calcula sobre los bytes, no sobre el texto, para que no dependa de la codificación.

```python
import hashlib
from pathlib import Path
import pandas as pd

def sha256_archivo(ruta):
    return hashlib.sha256(Path(ruta).read_bytes()).hexdigest()

filas = []
for r in sorted(Path("crudo").iterdir()):
    if r.is_file():
        filas.append({"ruta_crudo": str(r).replace("\\", "/"),
                      "hash_sha256": sha256_archivo(r)})
hashes = pd.DataFrame(filas)
hashes.head()
```

La bitácora de descarga aporta la dirección y la fecha de descarga; se une por la ruta. Los identificadores se asignan en orden de descarga y no se reutilizan.

```python
b = pd.read_json("bitacora_descarga.jsonl", lines=True)
b = b[b["estado"] == 200].rename(columns={"destino": "ruta_crudo"})
cat = hashes.merge(b[["ruta_crudo", "url", "fecha_descarga"]], on="ruta_crudo", how="left")
cat = cat.sort_values("fecha_descarga").reset_index(drop=True)
cat["id"] = ["P-%04d" % (i + 1) for i in range(len(cat))]
```

Los duplicados exactos comparten hash. El primero se conserva; los demás se anotan y se excluyen con el criterio `E1`, sin perder su identificador.

```python
dup = cat.duplicated("hash_sha256", keep="first")
primero = cat.drop_duplicates("hash_sha256").set_index("hash_sha256")["id"]
cat["notas"] = ""
cat.loc[dup, "notas"] = "Duplicado exacto de " + cat.loc[dup, "hash_sha256"].map(primero) + "; excluido"
cat["criterio_inclusion"] = ""
cat.loc[dup, "criterio_inclusion"] = "E1"
print(dup.sum(), "duplicados exactos")
```

Las decisiones a mano viven en `decisiones.csv`, con fecha. El cuaderno las lee y las une por `id`. Así el catálogo sigue siendo regenerable aunque contenga decisiones que ningún programa toma.

```python
dec = pd.read_csv("decisiones.csv", dtype=str).fillna("")
cat = cat.merge(dec, on="id", how="left", suffixes=("", "_dec"))
for col in ["titulo", "autor", "fuente", "fecha_documento", "escena", "derechos", "ruta_limpio"]:
    if col not in cat.columns:
        cat[col] = ""
# una decisión a mano sobre criterio o notas tiene prioridad sobre lo automático
for col in ["criterio_inclusion", "notas"]:
    if col + "_dec" in cat.columns:
        cat[col] = cat[col + "_dec"].where(cat[col + "_dec"] != "", cat[col])
        cat = cat.drop(columns=[col + "_dec"])
```

Las cinco reglas de integridad en una función. Se ejecuta cada vez que el catálogo cambia; devuelve las filas que fallan y por qué.

```python
import re

OBLIGATORIOS = ["id", "titulo", "fuente", "url", "fecha_documento", "fecha_descarga",
                "escena", "derechos", "criterio_inclusion", "hash_sha256", "ruta_crudo"]
CRITERIOS = {"1", "2", "3", "4", "E1", "E2"}   # los del protocolo

def validar(cat):
    fallas = []
    for i, f in cat.iterrows():
        vacios = [c for c in OBLIGATORIOS if str(f.get(c, "")).strip() == ""]
        if vacios:
            fallas.append((f["id"], "regla 1: vacíos " + ", ".join(vacios)))
        fd, fc = str(f["fecha_documento"]), str(f["fecha_descarga"])
        if not re.fullmatch(r"\d{4}(-\d{2}(-\d{2})?)?", fd) or fc[:10] < fd[:10]:
            fallas.append((f["id"], "regla 2: fechas"))
        if Path(f["ruta_crudo"]).exists() and sha256_archivo(f["ruta_crudo"]) != f["hash_sha256"]:
            fallas.append((f["id"], "regla 3: hash no coincide"))
        if str(f["criterio_inclusion"]) not in CRITERIOS:
            fallas.append((f["id"], "regla 5: criterio no está en el protocolo"))
    repetidos = cat["id"][cat["id"].duplicated()].tolist()
    for r in repetidos:
        fallas.append((r, "regla 4: id repetido"))
    return pd.DataFrame(fallas, columns=["id", "falla"])

fallas = validar(cat)
print(len(fallas), "fallas")
fallas
```

El catálogo se guarda con las columnas en el orden del esquema, y se producen los tres conteos que describen el corpus.

```python
ORDEN = ["id", "titulo", "autor", "fuente", "url", "fecha_documento", "fecha_descarga", "escena",
         "derechos", "criterio_inclusion", "hash_sha256", "ruta_crudo", "ruta_limpio", "notas"]
cat = cat.reindex(columns=ORDEN).fillna("")
cat.to_csv("catalogo.csv", index=False, encoding="utf-8")

print(cat.groupby("fuente").size())
print(cat.groupby(cat["fecha_documento"].str[:4]).size())
print(cat.groupby("criterio_inclusion").size())
```

## Semana 5. Limpieza y normalización

La codificación se detecta probando: si UTF-8 falla, se intenta CP1252. Lo que se escribe en `limpio` es UTF-8 siempre. Después se busca el rastro del error.

```python
from pathlib import Path
import unicodedata, re

def leer_con_deteccion(ruta):
    b = Path(ruta).read_bytes()
    for enc in ("utf-8", "cp1252", "latin-1"):
        try:
            return b.decode(enc), enc
        except UnicodeDecodeError:
            continue
    raise ValueError("no se pudo decodificar " + str(ruta))

texto, enc = leer_con_deteccion("crudo/P-0001.txt")
print(enc, "|", texto.count("Ã"), "apariciones de Ã")
```

Si el archivo es HTML, el texto se extrae con Beautiful Soup sobre la copia leída, nunca sobre `crudo`.

```python
from bs4 import BeautifulSoup

html, enc = leer_con_deteccion("crudo/N-0001.html")
soup = BeautifulSoup(html, "html.parser")
for etiqueta in soup(["script", "style", "nav", "header", "footer"]):
    etiqueta.decompose()
texto = soup.get_text("\n")
print(texto[:300])
```

Cada operación de limpieza es un patrón con su antes y después. Este quita un encabezado de periódico y números de página; cambie el patrón por el que su fuente necesite y muestre siempre lo que quitó.

```python
def quitar_encabezados(t):
    antes = len(t)
    t = re.sub(r"^\s*EL TIEMPO.*$", "", t, flags=re.MULTILINE)      # encabezado
    t = re.sub(r"^\s*p[áa]g\.?\s*\d+\s*$", "", t, flags=re.MULTILINE) # paginación
    return t, antes - len(t)

limpio, quitados = quitar_encabezados(texto)
print(quitados, "caracteres quitados")
```

La normalización unifica la forma Unicode, los espacios, las comillas y los guiones. No toca mayúsculas ni tildes: esa es una decisión del curso, escrita aquí.

```python
def normalizar(t):
    t = unicodedata.normalize("NFC", t)
    t = t.replace("“", '"').replace("”", '"').replace("«", '"').replace("»", '"')
    t = t.replace("‘", "'").replace("’", "'")
    t = re.sub(r"[‐-―]", "-", t)        # guiones de distintas longitudes
    t = re.sub(r"(\w)-\n(\w)", r"\1\2", t)         # palabra cortada al final de línea
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()

limpio = normalizar(limpio)
Path("limpio").mkdir(exist_ok=True)
Path("limpio/P-0001.txt").write_text(limpio, encoding="utf-8")
```

La segmentación produce la tabla de unidades: una fila por unidad con el `id` de la pieza y la posición. Aquí por oración, con un patrón simple que el estudiante puede ajustar; por párrafo bastaría dividir por línea en blanco.

```python
import pandas as pd

def segmentar_oraciones(t):
    partes = re.split(r"(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚÑ¿¡\"'])", t)
    return [p.strip() for p in partes if p.strip()]

unidades = []
for ruta in sorted(Path("limpio").glob("*.txt")):
    pid = ruta.stem
    for i, s in enumerate(segmentar_oraciones(ruta.read_text(encoding="utf-8")), start=1):
        unidades.append({"id": pid, "posicion": i, "texto": s})
U = pd.DataFrame(unidades)
U.to_csv("unidades.csv", index=False, encoding="utf-8")
print(len(U), "unidades")
```

Estimar el error de OCR es leer cien palabras y contar. El programa solo ayuda a elegirlas al azar y a registrar el resultado en `decisiones.csv` o en `notas`.

```python
import random
palabras = re.findall(r"\w+", Path("limpio/P-0001.txt").read_text(encoding="utf-8"))
random.seed(7)
inicio = random.randint(0, max(0, len(palabras) - 100))
print(" ".join(palabras[inicio:inicio + 100]))
# cuente a mano los errores y anote: error_ocr = errores / 100
```

## Semana 6. Primera lectura computacional

Contar palabras exige decidir qué es una palabra. Aquí: secuencias de letras, en minúsculas, con tildes conservadas. La lista de palabras funcionales que se quita está escrita y se puede cambiar.

```python
from collections import Counter
import pandas as pd, re

U = pd.read_csv("unidades.csv", dtype=str)
FUNCIONALES = set("""de la el y a en los las que del se por con su sus o al un una es no lo para
como más ni ante sin sobre son le les ha han e u cual entre todo toda todos todas esta este esto
estos estas ser será serán hay sea sean tiene tienen""".split())

def tokens(t):
    return re.findall(r"[a-záéíóúüñ]+", t.lower())

todos = [w for t in U["texto"] for w in tokens(t)]
frec = Counter(todos)
print(len(todos), "palabras;", len(frec), "distintas")
print(frec.most_common(10))
contenido = Counter({w: c for w, c in frec.items() if w not in FUNCIONALES})
print(contenido.most_common(20))
```

La concordancia muestra la palabra nodo con su compañía, y devuelve el `id` y la posición para que la línea se pueda citar. La ventana se mide en palabras.

```python
def kwic(U, nodo, ventana=5):
    filas = []
    patron = re.compile(r"\b" + re.escape(nodo) + r"\b", re.IGNORECASE)
    for _, u in U.iterrows():
        ws = u["texto"].split()
        for i, w in enumerate(ws):
            if patron.fullmatch(re.sub(r"^\W+|\W+$", "", w)):
                izq = " ".join(ws[max(0, i - ventana):i])
                der = " ".join(ws[i + 1:i + 1 + ventana])
                filas.append({"id": u["id"], "posicion": u["posicion"], "izquierda": izq, "nodo": w, "derecha": der})
    return pd.DataFrame(filas)

K = kwic(U, "orden", ventana=5)
print(len(K), "líneas")
for _, k in K.head(20).iterrows():
    print("%-40s  %-10s  %s   (%s, %s)" % (k["izquierda"][-40:], k["nodo"], k["derecha"][:40], k["id"], k["posicion"]))
```

Las colocaciones cuentan las palabras en la ventana y las comparan con su frecuencia total. Se descartan las que aparecen pocas veces en ventana, porque una razón alta con tres apariciones no vale nada.

```python
def colocaciones(U, nodo, ventana=4, minimo=5):
    en_ventana = Counter()
    for _, k in kwic(U, nodo, ventana).iterrows():
        for w in tokens(k["izquierda"]) + tokens(k["derecha"]):
            if w not in FUNCIONALES:
                en_ventana[w] += 1
    filas = [{"palabra": w, "en_ventana": c, "total": frec[w], "razon": round(c / frec[w], 3)}
             for w, c in en_ventana.items() if c >= minimo]
    return pd.DataFrame(filas).sort_values(["en_ventana", "razon"], ascending=False)

colocaciones(U, "orden")
```

Un dominio léxico es una lista escrita por el investigador. Se cuenta por pieza y se compara por las columnas del catálogo como proporción por mil palabras.

```python
DOMINIOS = {
    "orden":   ["orden", "policía", "autoridad", "ley", "decreto", "tribunal"],
    "trabajo": ["trabajo", "obreros", "jornal", "salario", "huelga", "fábrica"],
}
cat = pd.read_csv("catalogo.csv", dtype=str)

def peso_dominios(texto):
    ws = tokens(texto)
    n = max(1, len(ws))
    return {d: 1000 * sum(ws.count(p) for p in lista) / n for d, lista in DOMINIOS.items()}

por_pieza = U.groupby("id")["texto"].apply(" ".join).apply(peso_dominios).apply(pd.Series)
por_pieza = por_pieza.merge(cat[["id", "fuente", "fecha_documento"]], left_index=True, right_on="id")
por_pieza["anio"] = por_pieza["fecha_documento"].str[:4]
print(por_pieza.groupby("fuente")[list(DOMINIOS)].mean().round(2))
print(por_pieza.groupby("anio")[list(DOMINIOS)].mean().round(2))
```

Exportar a CSV lo que va al informe, con el nombre de la celda que lo produjo en el nombre del archivo.

```python
Path("salidas").mkdir(exist_ok=True)
K.to_csv("salidas/kwic_orden_v5.csv", index=False, encoding="utf-8")
colocaciones(U, "orden").to_csv("salidas/colocaciones_orden.csv", index=False, encoding="utf-8")
```

## Semana 7. Lectura asistida auditada

La instrucción se guarda como archivo con versión. El programa la lee, la envía con cada unidad y registra cada respuesta con fecha, modelo, versión e identificador. La biblioteca `openai` sirve para cualquier proveedor compatible con su interfaz; varios ofrecen cuota gratuita. Las credenciales van en un archivo `.env` que no se entrega.

```
pip install openai python-dotenv
```

```python
import os, json, datetime, random
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
import pandas as pd

load_dotenv()
client = OpenAI(api_key=os.getenv("API_KEY"), base_url=os.getenv("BASE_URL"))
MODEL = os.getenv("MODEL")
VERSION = "instruccion_v1"
INSTRUCCION = Path(VERSION + ".md").read_text(encoding="utf-8")

def etiquetar(unidad_id, texto, registro="llamadas.jsonl"):
    r = client.chat.completions.create(
        model=MODEL, temperature=0,
        messages=[{"role": "system", "content": INSTRUCCION},
                  {"role": "user", "content": texto}])
    salida = r.choices[0].message.content.strip()
    with open(registro, "a", encoding="utf-8") as f:
        f.write(json.dumps({"fecha": datetime.datetime.now().isoformat(timespec="minutes"),
                            "modelo": MODEL, "version": VERSION, "id": unidad_id,
                            "respuesta": salida}, ensure_ascii=False) + "\n")
    return salida
```

La muestra se elige al azar con semilla fija, para que la selección sea reproducible. El modelo etiqueta la muestra; el estudiante la etiqueta a ciegas en otro archivo, sin abrir el primero.

```python
U = pd.read_csv("unidades.csv", dtype=str)
random.seed(2027)
muestra = U.sample(n=30, random_state=2027).copy()
muestra["etiqueta_modelo"] = [etiquetar(i, t) for i, t in zip(muestra["id"] + "-" + muestra["posicion"], muestra["texto"])]
muestra[["id", "posicion", "texto", "etiqueta_modelo"]].to_csv("muestra_modelo.csv", index=False, encoding="utf-8")
muestra[["id", "posicion", "texto"]].assign(mi_etiqueta="").to_csv("muestra_a_ciegas.csv", index=False, encoding="utf-8")
```

Cuando `muestra_a_ciegas.csv` esté llena, se comparan las dos tablas: proporción de acuerdo y kappa de Cohen, calculado en diez líneas sin bibliotecas.

```python
m = pd.read_csv("muestra_modelo.csv", dtype=str)
h = pd.read_csv("muestra_a_ciegas.csv", dtype=str)
c = m.merge(h, on=["id", "posicion", "texto"])
a, b = c["etiqueta_modelo"].str.strip().str.lower(), c["mi_etiqueta"].str.strip().str.lower()

def kappa(a, b):
    n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    cats = set(a) | set(b)
    pe = sum((list(a).count(k) / n) * (list(b).count(k) / n) for k in cats)
    return (po - pe) / (1 - pe) if pe < 1 else 1.0

print("acuerdo:", round((a == b).mean(), 3), " kappa:", round(kappa(a, b), 3))
desacuerdos = c[a != b][["id", "posicion", "texto", "etiqueta_modelo", "mi_etiqueta"]]
desacuerdos.assign(tipo="", quien_tenia_razon="").to_csv("desacuerdos.csv", index=False, encoding="utf-8")
print(len(desacuerdos), "desacuerdos para tipificar a mano")
```

El registro de frontera por programa: una fila por operación, que al final se convierte en la tabla de la plantilla.

```python
def decidir(semana, operacion, propuesta, inferencia, decision, criterio, responde, archivo="frontera.jsonl"):
    with open(archivo, "a", encoding="utf-8") as f:
        f.write(json.dumps({"semana": semana, "operacion": operacion, "propuso_el_modelo": propuesta,
                            "inferencia": inferencia, "decidi": decision, "criterio": criterio,
                            "responde": responde}, ensure_ascii=False) + "\n")

decidir(7, "Etiquetas sobre la muestra", "30 etiquetas con instruccion_v1", "I",
        "corregir la instrucción y repetir", "8 de 9 desacuerdos fuerzan la categoría 'conflicto' donde no aplica", "yo")
pd.read_json("frontera.jsonl", lines=True).to_csv("registro-de-frontera.csv", index=False)
```

## Semana 8. Documentar para reconstruir

El archivo de versiones se produce desde el cuaderno. Sin él, el cuaderno que hoy corre puede dejar de correr.

```python
import subprocess, sys
req = subprocess.run([sys.executable, "-m", "pip", "freeze"], capture_output=True, text=True).stdout
Path("requirements.txt").write_text(req, encoding="utf-8")
print(req[:300])
```

La comprobación final: el hash del catálogo. Quien reconstruya el corpus debe obtener el mismo.

```python
print("catalogo.csv:", sha256_archivo("catalogo.csv"))
```

## Nota sobre costos y privacidad

Use cuotas gratuitas y material sin datos personales de terceros. Si su proyecto incluye material sensible, haga la práctica de la semana 7 con una muestra anonimizada o con material público. No entregue el archivo `.env`. [*Ética, exterioridad y gobernanza*](../../curso-7-etica-gobernanza/README.md) trata estos problemas en detalle: derechos sobre el material, datos personales y consentimiento, con una matriz de riesgos y derechos por tipo de pieza del corpus.
