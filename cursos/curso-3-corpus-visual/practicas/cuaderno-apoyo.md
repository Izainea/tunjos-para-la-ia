# Cuaderno de apoyo para hacer las prácticas por programa

Opcional. Todo el curso se puede hacer con una hoja de cálculo, el navegador y la interfaz web de un modelo. Este cuaderno es para quien quiera que la recolección, el hash, el catálogo y las descripciones queden en archivos y se puedan repetir. Está pensado para alguien sin experiencia previa en Python, copiando bloque a bloque. Cada bloque se explica antes de mostrarse.

## Preparación

Instale Python 3.11 o superior y, en una terminal:

```
pip install requests pillow imagehash pandas python-dotenv openai
```

Cree una carpeta de trabajo con esta estructura:

```
mi-corpus/
  paginas.csv        lista de páginas fuente (la escribe usted antes de descargar)
  img/               imágenes descargadas
  descartadas/       lo que no es del tema
  catalogo.csv       el catálogo
  descripciones.jsonl
  .env               la clave del modelo; nunca va en el código ni en el repositorio
```

`paginas.csv` tiene cuatro columnas: `fuente`, `escena`, `url`, `periodo`. Una fila por página.

## Comprobar robots

Antes de descargar nada, el programa pregunta al sitio si permite visitar la ruta. La biblioteca estándar trae un lector de `robots.txt`. Si el archivo no existe, la función devuelve permitido; anótelo igual, porque "no dijo que no" no es "dijo que sí".

```python
from urllib import robotparser
from urllib.parse import urlparse

AGENTE = "corpus-visual-curso3 (contacto: su-correo@ejemplo.org)"

def permitido(url):
    """True si robots.txt del sitio permite que AGENTE visite la url."""
    base = "{0.scheme}://{0.netloc}".format(urlparse(url))
    rp = robotparser.RobotFileParser()
    rp.set_url(base + "/robots.txt")
    try:
        rp.read()
    except Exception:
        return True  # sin robots.txt: permitido, y se anota
    return rp.can_fetch(AGENTE, url)
```

## Descargar una página

Explicación. El bloque pide la página, busca todas las etiquetas de imagen, resuelve la URL de cada una, la descarga con una pausa entre peticiones, lee las dimensiones con Pillow y escribe una fila por imagen con la URL de la imagen, la URL de la página, el texto alternativo y las medidas. Se identifica con el agente y espera dos segundos entre imágenes. No filtra: el filtrado es un paso aparte y registrado.

```python
import csv, os, re, time
import requests
from io import BytesIO
from urllib.parse import urljoin
from PIL import Image

def descargar_pagina(url, fuente, escena, periodo, carpeta="img", catalogo="catalogo.csv", pausa=2.0):
    if not permitido(url):
        print("robots.txt no permite:", url)
        return
    os.makedirs(carpeta, exist_ok=True)
    html = requests.get(url, headers={"User-Agent": AGENTE}, timeout=30).text
    etiquetas = re.findall(r'<img[^>]+>', html, flags=re.I)
    nuevo = not os.path.exists(catalogo)
    with open(catalogo, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if nuevo:
            w.writerow(["id", "periodo", "fuente", "pagina_fuente", "url_imagen", "ancho", "alto",
                        "extension", "descripcion_heredada", "origen_descripcion", "derechos",
                        "escena", "ruta_local", "grupo_duplicados", "canonica", "sensible"])
        n = sum(1 for _ in open(catalogo, encoding="utf-8")) - 1
        for et in etiquetas:
            src = re.search(r'src="([^"]+)"', et)
            if not src:
                continue
            url_img = urljoin(url, src.group(1))
            alt = re.search(r'alt="([^"]*)"', et)
            alt = alt.group(1) if alt else ""
            try:
                r = requests.get(url_img, headers={"User-Agent": AGENTE}, timeout=30)
                im = Image.open(BytesIO(r.content))
            except Exception as e:
                print("no se pudo:", url_img, e)
                continue
            n += 1
            ext = (im.format or "jpg").lower()
            ruta = os.path.join(carpeta, f"{n:04d}.{ext}")
            with open(ruta, "wb") as g:
                g.write(r.content)
            w.writerow([n, periodo, fuente, url, url_img, im.width, im.height, "." + ext,
                        alt, "alt" if alt else "ninguna", "", escena, ruta, "", "", ""])
            time.sleep(pausa)
```

Para recorrer la lista:

```python
import pandas as pd
paginas = pd.read_csv("paginas.csv")
for _, p in paginas.iterrows():
    descargar_pagina(p["url"], p["fuente"], p["escena"], p["periodo"])
```

## Filtrar lo que no es del tema

Explicación. El filtrado se hace mirando, pero el programa ayuda a encontrar candidatos: dimensiones muy pequeñas, dimensiones repetidas muchas veces en la misma página, nombres de archivo con "logo", "icon" o "banner". El bloque solo lista candidatos; usted decide y mueve.

```python
cat = pd.read_csv("catalogo.csv")
cat["dims"] = cat["ancho"].astype(str) + "x" + cat["alto"].astype(str)
repetidas = cat.groupby(["pagina_fuente", "dims"]).size()
candidatas = cat[(cat["ancho"] < 150) | (cat["alto"] < 150) |
                 cat["url_imagen"].str.contains("logo|icon|banner|sprite", case=False, na=False)]
print(repetidas[repetidas > 5])
print(candidatas[["id", "url_imagen", "dims"]])
```

## Hash perceptual

Explicación. `imagehash.dhash` reduce cada imagen a 9 por 8 píxeles en gris y anota si cada píxel es más claro que el siguiente de su fila: 64 bits. La distancia entre dos hashes es el número de bits distintos. El bloque calcula el hash de cada imagen del catálogo, compara todos los pares y lista los que quedan bajo el umbral. Mire con cuidado los pares entre 8 y 14: ahí se decide.

```python
import imagehash
from itertools import combinations

UMBRAL = 10
cat = pd.read_csv("catalogo.csv")
hashes = {}
for _, fila in cat.iterrows():
    try:
        hashes[fila["id"]] = imagehash.dhash(Image.open(fila["ruta_local"]))
    except Exception as e:
        print("sin hash:", fila["id"], e)

pares = []
for a, b in combinations(hashes, 2):
    d = hashes[a] - hashes[b]
    if d <= UMBRAL + 4:
        pares.append((a, b, d, "bajo umbral" if d <= UMBRAL else "en el límite"))
pares.sort(key=lambda t: t[2])
for p in pares:
    print(p)
```

Para asignar grupos, una pasada simple: cada par bajo el umbral une a los dos ids en el mismo grupo.

```python
grupo = {}
siguiente = 1
for a, b, d, _ in pares:
    if d > UMBRAL:
        continue
    ga, gb = grupo.get(a), grupo.get(b)
    if ga and gb:
        for k, v in grupo.items():
            if v == gb:
                grupo[k] = ga
    elif ga:
        grupo[b] = ga
    elif gb:
        grupo[a] = gb
    else:
        grupo[a] = grupo[b] = f"G{siguiente}"
        siguiente += 1
cat["grupo_duplicados"] = cat["id"].map(grupo).fillna("")
cat.to_csv("catalogo.csv", index=False)
```

El ejemplar canónico lo elige usted en la columna `canonica`, con la razón en la plantilla.

## Validar

Explicación. Dos comprobaciones: cada fila tiene archivo, cada archivo tiene fila. El bloque imprime las discrepancias y no corrige nada solo.

```python
import glob
cat = pd.read_csv("catalogo.csv")
en_disco = set(glob.glob("img/*"))
en_catalogo = set(cat["ruta_local"].astype(str))
print("filas sin archivo:", sorted(en_catalogo - en_disco))
print("archivos sin fila:", sorted(en_disco - en_catalogo))
print("filas:", len(cat), "archivos:", len(en_disco))
```

## Describir con un modelo multimodal (bloque opcional)

Explicación. El bloque envía una imagen y el prompt por capas a un modelo compatible con la interfaz de `openai`, y guarda prompt, salida y metadatos en `descripciones.jsonl`. La clave está en `.env` y se lee con `python-dotenv`; nunca se escribe en el código ni se sube a un repositorio. Antes de correrlo sobre una imagen, compruebe en el catálogo que no está marcada como sensible. Varios proveedores ofrecen cuota gratuita; cambie `BASE_URL` y `MODEL` según el suyo.

Contenido de `.env`:

```
API_KEY=su_clave
BASE_URL=https://api.openai.com/v1
MODEL=nombre_del_modelo_con_vision
```

```python
import os, json, base64, datetime
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("API_KEY"), base_url=os.getenv("BASE_URL"))
MODEL = os.getenv("MODEL")

PROMPT_CAPAS = open("prompt_capas.txt", encoding="utf-8").read()  # el de la práctica 2

def describir(id_imagen, ruta, prompt=PROMPT_CAPAS, registro="descripciones.jsonl"):
    """Envía la imagen y el prompt; guarda todo con fecha. Devuelve el texto."""
    with open(ruta, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    ext = ruta.rsplit(".", 1)[-1].lower().replace("jpg", "jpeg")
    r = client.chat.completions.create(
        model=MODEL,
        temperature=0.2,
        messages=[{"role": "user", "content": [
            {"type": "text", "text": prompt},
            {"type": "image_url", "image_url": {"url": f"data:image/{ext};base64,{b64}"}},
        ]}],
    )
    texto = r.choices[0].message.content
    uso = getattr(r, "usage", None)
    with open(registro, "a", encoding="utf-8") as f:
        f.write(json.dumps({
            "id": id_imagen, "ruta": ruta, "fecha": datetime.datetime.now().isoformat(),
            "modelo": MODEL, "prompt": prompt, "respuesta": texto,
            "tokens": getattr(uso, "total_tokens", None),
        }, ensure_ascii=False) + "\n")
    return texto
```

Para la muestra de 20:

```python
cat = pd.read_csv("catalogo.csv")
muestra = cat[(cat["sensible"] != "sí")].head(20)
for _, fila in muestra.iterrows():
    print(fila["id"]); print(describir(fila["id"], fila["ruta_local"])); print("=====")
```

## Separar las capas de la salida

Explicación. Si el modelo respetó los títulos del prompt, el bloque corta la salida en cuatro columnas para la tabla de la semana 6.

```python
import re
TITULOS = [("denotacion", "DENOTACIÓN"), ("indices", "ÍNDICES MATERIALES"),
           ("suposiciones", "SUPOSICIONES"), ("no_sabe", "LO QUE NO PUEDES SABER")]

def capas(texto):
    """Corta la salida en cuatro capas por sus títulos; vacío si falta un título."""
    out = {}
    for i, (clave, titulo) in enumerate(TITULOS):
        inicio = texto.find(titulo)
        if inicio < 0:
            out[clave] = ""
            continue
        fin = len(texto)
        for _, t2 in TITULOS[i + 1:]:
            j = texto.find(t2, inicio + len(titulo))
            if j >= 0:
                fin = min(fin, j)
        out[clave] = texto[inicio + len(titulo):fin].strip(" .:\n")
    return out

desc = pd.read_json("descripciones.jsonl", lines=True)
tabla = pd.DataFrame([{"id": d["id"], **capas(d["respuesta"])} for _, d in desc.iterrows()])
tabla.to_csv("descripciones_por_capas.csv", index=False)
```

Si el modelo no respetó los títulos, la separación falla y se anota: es un dato sobre el modelo.

## Registro de frontera por programa

Mantenga un archivo con sus decisiones, una por afirmación, código o grupo de exhibición:

```python
def decidir(tipo, id_imagen, propuesta, decision, criterio, responde, archivo="frontera.jsonl"):
    with open(archivo, "a", encoding="utf-8") as f:
        f.write(json.dumps({"tipo": tipo, "id": id_imagen, "propuso_el_modelo": propuesta,
                            "decidi": decision, "criterio": criterio, "responde": responde},
                           ensure_ascii=False) + "\n")

decidir("descripcion", 17, "cuatro personas de pie frente a un muro",
        "corregir: son tres; la cuarta es una sombra",
        "miré la imagen a tamaño completo", "yo")
```

Al final, `frontera.jsonl` se convierte en las tablas de la plantilla:

```python
pd.read_json("frontera.jsonl", lines=True).to_csv("registro-de-frontera-visual.csv", index=False)
```

## Nota sobre costos y privacidad

Use cuotas gratuitas y, hasta la semana 7, solo imágenes sin personas identificables. Si su corpus es sensible, considere un modelo local de visión: menor calidad, control total, y la decisión queda en el registro. [*Ética, exterioridad y gobernanza*](../../curso-7-etica-gobernanza/README.md) trata estos problemas en detalle: derechos sobre el material, datos personales e imágenes sensibles, consentimiento en plataformas y la opción de describir en lugar de exhibir; concluye que esas decisiones se escriben en un protocolo de gobernanza que dice quién responde por cada una.
