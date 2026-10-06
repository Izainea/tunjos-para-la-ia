# Cuaderno de apoyo: hacer las prácticas por programa

Opcional. Todo el curso se puede hacer con la interfaz web de un modelo y con hojas de cálculo. Este cuaderno es para quien quiera dejar instrucciones, outputs, expectativas y decisiones en archivos, repetir la codificación con varios modelos, y calcular el acuerdo cuando quiera reportarlo. Está pensado para alguien sin experiencia previa en Python, copiando bloque a bloque. El cuaderno del curso 1 explica la preparación del entorno y la función base; aquí se repite lo mínimo.

## Preparación

Instale Python 3.11 o superior y, en una terminal:

```
pip install openai python-dotenv pandas
```

Cree un archivo `.env` con la clave del proveedor que use. La biblioteca `openai` sirve para cualquier proveedor compatible con su interfaz; cambie `base_url` según el caso. Para la triangulación entre familias conviene tener dos claves de proveedores distintos; varios ofrecen cuota gratuita.

```
API_KEY=su_clave
BASE_URL=https://api.openai.com/v1
MODEL=nombre_del_modelo
```

## Función base con registro

Cada llamada queda en un archivo con fecha, modelo e instrucción literal. Ese archivo es el anexo que piden las plantillas.

```python
import os, json, datetime
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("API_KEY"), base_url=os.getenv("BASE_URL"))
MODEL = os.getenv("MODEL")

def preguntar(prompt, etiqueta, registro="registro.jsonl"):
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
            "etiqueta": etiqueta,
            "prompt": prompt,
            "respuesta": texto,
        }, ensure_ascii=False) + "\n")
    return texto
```

## Semana 3. Declarar la expectativa antes de correr

La expectativa se escribe en un archivo con hora antes de la primera llamada. Lo que importa es que quede fechada.

```python
def declarar_expectativa(condicion, expectativa, archivo="expectativas.jsonl"):
    with open(archivo, "a", encoding="utf-8") as f:
        f.write(json.dumps({
            "fecha": datetime.datetime.now().isoformat(),
            "condicion": condicion,
            "expectativa": expectativa,
        }, ensure_ascii=False) + "\n")

declarar_expectativa("con libro de códigos",
    "coincidencia alta: el modelo aplica mi regla; mide consistencia, no es pata")
declarar_expectativa("sin libro de códigos, otra familia",
    "divergencia en los fragmentos 4, 7 y 9, donde la categoría exige contexto local")
```

## Semana 3. Las dos condiciones

```python
fragmentos = open("fragmentos.txt", encoding="utf-8").read()
libro = open("libro-de-codigos.txt", encoding="utf-8").read()
pregunta = "¿Cómo narran los entrevistados su relación con las instituciones locales?"

p_con = f"""Libro de códigos:\n{libro}\n\nFragmentos:\n{fragmentos}\n
Asigna a cada fragmento uno o más códigos del libro. Para cada asignación cita
la frase exacta, di por qué ese código y no el más cercano, y marca si dudaste.
No inventes códigos; si ninguno aplica escribe "ninguno" y explica."""
con_libro = preguntar(p_con, "semana3-con-libro")

p_sin = f"""Pregunta de investigación: {pregunta}\n\nFragmentos:\n{fragmentos}\n
Propón códigos para cada fragmento. Para cada código: nombre breve, definición
en una frase, la frase exacta que lo sustenta, y qué supuesto das por sentado."""
sin_libro = preguntar(p_sin, "semana3-sin-libro")
```

Para la segunda condición con otra familia, cambie `MODEL` y `BASE_URL` en `.env` o cree un segundo cliente.

## Semana 3. Calcular el acuerdo, y qué hacer con él

Si quiere reportar el acuerdo de la condición con libro de códigos, el curso pide que lo reporte como consistencia y no como validez. Con una tabla `codificacion.csv` de columnas `fragmento`, `codigo_mio`, `codigo_modelo`:

```python
import pandas as pd

df = pd.read_csv("codificacion.csv")
acuerdo = (df["codigo_mio"] == df["codigo_modelo"]).mean()
print(f"Acuerdo observado: {acuerdo:.1%}")
```

Para un kappa de Cohen, `pip install scikit-learn` y:

```python
from sklearn.metrics import cohen_kappa_score
print("Kappa:", round(cohen_kappa_score(df["codigo_mio"], df["codigo_modelo"]), 2))
```

Lo que se escribe en la matriz no es la cifra sino la frase: "el modelo aplica mi libro de códigos con un acuerdo de 0,81; mide consistencia; no cuenta como pata". Una cifra sin esa frase es el salto de la semana 1.

## Semana 4. Candidatos de hipótesis con supuesto explícito

```python
patron = "Los fragmentos que mencionan 'la alcaldía' nunca mencionan 'la policía', y al revés."
p = f"""Patrón observado: {patron}\n
Propón dos hipótesis distintas e incompatibles que lo explicarían. Para cada una:
(1) el hecho que explica, (2) una observación que la distinguiría de la otra,
(3) el supuesto que das por sentado al proponerla."""
print(preguntar(p, "semana4-candidatos"))
```

El punto 3 es el que llena la columna "desde qué trasfondo es plausible" de la ficha.

## Semana 7. Marcadores de autoridad

Un conteo sencillo sobre el propio borrador. La lista es la de la práctica; amplíela con los marcadores de su campo.

```python
import re

MARCADORES = [
    "los datos muestran", "el análisis revela", "es evidente que", "se observa que",
    "los resultados indican", "resulta claro", "como puede apreciarse",
    "la evidencia sugiere", "se concluye que", "queda demostrado",
]

texto = open("borrador.txt", encoding="utf-8").read().lower()
for m in MARCADORES:
    n = len(re.findall(re.escape(m), texto))
    if n:
        print(f"{m}: {n}")
```

El programa no reescribe nada. Marca dónde hay que ponerse a escribir.

## Nota sobre costos y privacidad

Use cuotas gratuitas y material sin datos personales de terceros. Si su proyecto incluye material sensible, haga las prácticas con una muestra anonimizada o con material público, y revise las condiciones de uso de datos del proveedor antes de enviar nada: la plantilla de declaración pregunta si las revisó. El curso 7 del programa trata estos problemas en detalle.
