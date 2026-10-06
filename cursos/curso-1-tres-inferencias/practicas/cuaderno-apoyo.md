# Cuaderno de apoyo para hacer las prácticas por programa

Opcional. Todo el curso se puede hacer con la interfaz web de un modelo. Este cuaderno es para quien quiera dejar los prompts, outputs y decisiones en archivos y repetir el ejercicio con varios modelos. Está pensado para que lo use alguien sin experiencia previa en Python, copiando bloque a bloque.

## Preparación

Instale Python 3.11 o superior y, en una terminal:

```
pip install openai python-dotenv
```

Cree un archivo `.env` en la carpeta de trabajo con la clave del proveedor que use. La biblioteca `openai` sirve para cualquier proveedor compatible con su interfaz; cambie `base_url` según el caso. El curso no exige un proveedor y varios ofrecen cuota gratuita.

```
API_KEY=su_clave
BASE_URL=https://api.openai.com/v1
MODEL=nombre_del_modelo
```

## Función base

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

Cada llamada queda en `registro.jsonl`. Ese archivo es el anexo literal que piden las plantillas.

## Semana 2. Verificar una cadena de pasos

```python
problema = """Un investigador entrevistó a 12 personas. 8 mencionaron la palabra
'miedo'. De esas 8, 5 también mencionaron 'policía'. 2 personas mencionaron
'policía' sin mencionar 'miedo'. ¿Cuántas personas no mencionaron ninguna de las dos?
Resuelve paso a paso y numera cada paso."""

print(preguntar(problema))
```

Numere los pasos en su bitácora, marque cuáles son deductivos y verifíquelos sin mirar la conclusión.

## Semana 3. Hipótesis rivales sobre los mismos datos

```python
datos = open("datos.txt", encoding="utf-8").read()

p1 = f"Estos son los datos:\n{datos}\n\nFormula la hipótesis que mejor los explica, en una frase, y di qué la sustenta."
h1 = preguntar(p1)

p2 = f"Estos son los datos:\n{datos}\n\nYa se propuso esta hipótesis: {h1}\n\nFormula una hipótesis distinta, incompatible con la anterior, que también sea compatible con todos los datos. Di qué dato nuevo permitiría decidir entre las dos."
h2 = preguntar(p2)
print(h1, "\n---\n", h2)
```

## Semana 6. Filtro peirceano asistido

El modelo puede ayudar a aplicar los criterios, pero la decisión es suya. Pídale que argumente los cuatro criterios a favor y en contra de cada hipótesis, y luego decida usted.

```python
hipotesis = [h1, h2, "mi hipótesis propia"]
for h in hipotesis:
    p = f"""Evalúa esta hipótesis con cuatro criterios, dando un argumento a favor
y uno en contra para cada uno: (1) explica el hecho sorprendente, (2) es
verificable y cómo, (3) es económica de probar y qué rinde, (4) es plausible
dado lo que se sabe del tema. Hipótesis: {h}"""
    print(preguntar(p), "\n=====\n")
```

## Semana 7. Registro de frontera por programa

Mantenga un segundo archivo con sus decisiones, una por paso del modelo:

```python
def decidir(paso, propuesta, inferencia, decision, criterio, responde, archivo="frontera.jsonl"):
    with open(archivo, "a", encoding="utf-8") as f:
        f.write(json.dumps({
            "paso": paso, "propuso_el_modelo": propuesta,
            "inferencia": inferencia, "decidi": decision,
            "criterio": criterio, "responde": responde,
        }, ensure_ascii=False) + "\n")

decidir(1, "Código 'desconfianza institucional' para fragmentos 2, 5, 7",
        "A", "corregir: separar 'desconfianza' de 'miedo', que el modelo fundió",
        "los fragmentos 5 y 7 hablan de temor físico, no de desconfianza",
        "yo")
```

Al final, `frontera.jsonl` se convierte en la tabla de la plantilla con cualquier hoja de cálculo o con:

```python
import pandas as pd
pd.read_json("frontera.jsonl", lines=True).to_csv("registro-de-frontera.csv", index=False)
```

## Nota sobre costos y privacidad

Use cuotas gratuitas y material sin datos personales de terceros. Si su proyecto incluye material sensible, haga la práctica con una muestra anonimizada o con material público. [*Exterioridad y gobernanza de la IA en ciencias sociales*](../../curso-7-etica-gobernanza/README.md), el curso del programa dedicado a la ética del trabajo con modelos, trata estos problemas en detalle: los derechos de autor y la protección de datos personales del material, el consentimiento en plataformas y la pregunta de si el proveedor del modelo conserva y usa para entrenar lo que recibe. La regla que allí se fija es concreta: el material con datos personales no sale hacia un servicio sin anonimización previa.
