# Cuaderno de apoyo: los métodos del curso en Python

Este cuaderno acompaña las ocho semanas. Está escrito para que lo use alguien con nociones básicas de Python, copiando bloque a bloque; cada bloque viene precedido de lo que hace y de la decisión que exige. Los parámetros aparecen como variables con nombre al comienzo de cada bloque para que moverlos sea una línea y no una búsqueda. Todo lo que se calcula aquí se registra con su entorno y su semilla, porque la reproducibilidad es la mitad de la frontera.

## Preparación

Instale Python 3.10 o superior y, en una terminal, las bibliotecas del curso. La primera vez que se cargue un modelo de embeddings se descargará de internet; después queda en el computador.

```
pip install pandas numpy scipy scikit-learn sentence-transformers umap-learn networkx matplotlib plotly ruptures
```

El corpus se espera como una tabla `corpus.csv` con una fila por documento y las columnas `id`, `fecha` (en formato AAAA-MM-DD) y `texto`. Para imágenes, la columna `ruta` con la ubicación del archivo en vez de `texto`. Si tiene códigos por documento, una columna `codigos` con los códigos separados por punto y coma.

```python
import json, datetime, platform
import importlib.metadata as md
import numpy as np
import pandas as pd

corpus = pd.read_csv("corpus.csv")
textos = corpus["texto"].fillna("").astype(str).tolist()
print(len(textos), "documentos")
```

## Registro de entorno

Un resultado es reproducible si se sabe con qué se calculó. Este bloque escribe un archivo con la versión de Python, de cada biblioteca, el modelo usado y la semilla. Córralo cada vez que produzca un resultado que vaya a una entrega, y adjunte el archivo.

```python
def registrar_entorno(archivo="entorno.json", modelo=None, semilla=None, nota=""):
    paquetes = ["pandas", "numpy", "scipy", "scikit-learn", "sentence-transformers",
                "umap-learn", "networkx", "matplotlib", "plotly", "ruptures"]
    versiones = {}
    for p in paquetes:
        try:
            versiones[p] = md.version(p)
        except md.PackageNotFoundError:
            versiones[p] = "no instalado"
    info = {"fecha": datetime.datetime.now().isoformat(), "python": platform.python_version(),
            "paquetes": versiones, "modelo": modelo, "semilla": semilla, "nota": nota}
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(info, f, ensure_ascii=False, indent=2)
    return info

registrar_entorno(nota="prueba de instalación")
```

## Semana 1. Bolsa de palabras y coseno

La bolsa de palabras cuenta palabras y olvida el orden. TF-IDF es la misma bolsa con un peso que castiga las palabras que aparecen en casi todos los documentos. El coseno entre dos filas dice cuánto se parecen sus proporciones de palabras, y nada más. Este bloque calcula la matriz de similitud y muestra, para un par, qué palabras lo acercan.

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

STOP = ["el", "la", "los", "las", "de", "del", "en", "un", "una", "y", "o", "a", "que",
        "es", "por", "con", "para", "no", "se", "su", "sus", "al", "lo", "le", "más", "como"]

vec = TfidfVectorizer(lowercase=True, strip_accents="unicode", stop_words=STOP, min_df=1)
X = vec.fit_transform(textos)
S_bolsa = cosine_similarity(X)
palabras = np.array(vec.get_feature_names_out())

def explicar_par(i, j):
    a, b = X[i].toarray()[0], X[j].toarray()[0]
    comunes = palabras[(a > 0) & (b > 0)]
    print(f"coseno({i}, {j}) = {S_bolsa[i, j]:.2f}")
    print("palabras comunes:", ", ".join(comunes) if len(comunes) else "ninguna")

explicar_par(0, 1)
```

Para la ficha de la semana 1, busque un par con coseno alto que no le parezca parecido y uno con coseno bajo que sí. El bloque siguiente lista los pares extremos.

```python
n = len(textos)
pares = [(S_bolsa[i, j], i, j) for i in range(n) for j in range(i + 1, n)]
pares.sort(reverse=True)
print("cinco pares más parecidos para la medida:")
for s, i, j in pares[:5]:
    print(f"  {s:.2f}  [{i}] {textos[i][:60]}  |  [{j}] {textos[j][:60]}")
```

## Semana 2. Embeddings y vecinos

Un embedding es un vector aprendido por un modelo entrenado en otro corpus. El bloque usa un modelo multilingüe de Sentence-BERT de descarga libre; el nombre del modelo es la primera decisión que se registra. Los vectores se normalizan para que el producto punto sea el coseno.

```python
from sentence_transformers import SentenceTransformer

MODELO = "paraphrase-multilingual-MiniLM-L12-v2"   # decisión: qué modelo, y por tanto qué precomprensión
modelo = SentenceTransformer(MODELO)
E = modelo.encode(textos, normalize_embeddings=True, show_progress_bar=True)
np.save("embeddings.npy", E)
print(E.shape)   # (documentos, dimensiones)
registrar_entorno(modelo=MODELO, nota="embeddings de texto")
```

Para un corpus visual, el mismo procedimiento con CLIP sobre las imágenes. El modelo acerca imágenes a descripciones en inglés, y esa es su precomprensión.

```python
from PIL import Image

MODELO = "clip-ViT-B-32"
modelo = SentenceTransformer(MODELO)
imagenes = [Image.open(r).convert("RGB") for r in corpus["ruta"]]
E = modelo.encode(imagenes, normalize_embeddings=True, show_progress_bar=True, batch_size=16)
np.save("embeddings.npy", E)
registrar_entorno(modelo=MODELO, nota="embeddings de imagen")
```

La primera prueba de sentido es leer vecinos. Para cada documento que conozca, los cinco más cercanos por coseno. Si los vecinos tienen sentido, el espacio conserva algo que importa; si comparten solo longitud o género, conserva otra cosa.

```python
S = E @ E.T

def vecinos(i, n=5):
    orden = np.argsort(-S[i])
    return [(int(j), float(S[i, j])) for j in orden if j != i][:n]

for i in [0, 1, 2]:          # cambie por los índices de documentos que conozca bien
    print(f"\n[{i}] {textos[i][:90]}")
    for j, s in vecinos(i):
        print(f"   {s:.2f}  [{j}] {textos[j][:90]}")
```

Para ver el espacio hay que proyectarlo, y la proyección es otro instrumento con parámetros. PCA es lineal y conserva varianza; UMAP conserva vecindades locales y deforma las distancias grandes. Las dos se guardan con sus parámetros en el título.

```python
from sklearn.decomposition import PCA
import umap
import plotly.express as px

SEMILLA = 0
N_VECINOS, MIN_DIST = 15, 0.1    # decisiones de UMAP: cambiarlas cambia la figura

P2 = PCA(n_components=2, random_state=SEMILLA).fit_transform(E)
U2 = umap.UMAP(n_neighbors=N_VECINOS, min_dist=MIN_DIST, random_state=SEMILLA).fit_transform(E)

etiquetas = [t[:80] for t in textos]
px.scatter(x=P2[:, 0], y=P2[:, 1], hover_name=etiquetas,
           title="PCA, 2 componentes").write_html("nube_pca.html")
px.scatter(x=U2[:, 0], y=U2[:, 1], hover_name=etiquetas,
           title=f"UMAP · n_neighbors={N_VECINOS} · min_dist={MIN_DIST} · semilla {SEMILLA}").write_html("nube_umap.html")
```

## Semana 3. Agrupamiento y prueba de estabilidad

k-means produce la mejor partición en k grupos, para el k que se le pide y la semilla con que empieza. El bloque corre k de 2 a 10 con cinco semillas y guarda todo, porque la prueba de estabilidad necesita todas las corridas. La silueta y la inercia ayudan a descartar valores absurdos de k; no deciden entre dos razonables.

```python
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, adjusted_rand_score

E = np.load("embeddings.npy")
KS, SEMILLAS = range(2, 11), range(5)

corridas = {}
for k in KS:
    for s in SEMILLAS:
        km = KMeans(n_clusters=k, n_init=10, random_state=s).fit(E)
        corridas[(k, s)] = (km.labels_, km.inertia_)

resumen = pd.DataFrame({
    "k": list(KS),
    "silueta": [silhouette_score(E, corridas[(k, 0)][0]) for k in KS],
    "inercia": [corridas[(k, 0)][1] for k in KS],
})
print(resumen.round(3))
```

El dendrograma del agrupamiento jerárquico muestra que el número de grupos es una altura de corte. Mírelo antes de elegir k.

```python
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

Z = linkage(E, method="ward")
plt.figure(figsize=(10, 4))
dendrogram(Z, no_labels=True)
plt.title("Agrupamiento jerárquico (Ward) sobre embeddings")
plt.savefig("dendrograma.png", dpi=150, bbox_inches="tight")
```

La prueba de estabilidad compara cada grupo de la corrida de referencia con la mejor coincidencia en otra corrida, por el índice de Jaccard. Se hace contra las otras semillas, contra k menos uno y k más uno, y contra otra representación. El índice de Rand ajustado compara particiones completas.

```python
K_ELEGIDO = 4                 # decisión: anótela con su razón en la ficha
ref = corridas[(K_ELEGIDO, 0)][0]

def grupos(labels):
    return [set(np.where(labels == g)[0]) for g in np.unique(labels)]

def jaccard(a, b):
    return len(a & b) / len(a | b)

def supervivencia(labels_ref, labels_otro):
    H = grupos(labels_otro)
    return [max(jaccard(g, h) for h in H) for g in grupos(labels_ref)]

por_semilla = np.mean([supervivencia(ref, corridas[(K_ELEGIDO, s)][0]) for s in range(1, 5)], axis=0)
k_menos = supervivencia(ref, corridas[(K_ELEGIDO - 1, 0)][0])
k_mas = supervivencia(ref, corridas[(K_ELEGIDO + 1, 0)][0])

# otra representación: TF-IDF sobre los mismos documentos
X_tfidf = TfidfVectorizer(strip_accents="unicode", stop_words=STOP, min_df=2).fit_transform(textos)
otra = KMeans(n_clusters=K_ELEGIDO, n_init=10, random_state=0).fit(X_tfidf).labels_
otra_rep = supervivencia(ref, otra)

tabla = pd.DataFrame({
    "grupo": range(K_ELEGIDO), "tamaño": np.bincount(ref),
    "jaccard_semilla": por_semilla, "jaccard_k_menos": k_menos,
    "jaccard_k_mas": k_mas, "jaccard_otra_rep": otra_rep,
})
print(tabla.round(2))
print("Rand ajustado, semilla 0 frente a 1:", round(adjusted_rand_score(ref, corridas[(K_ELEGIDO, 1)][0]), 3))
print("Rand ajustado, embeddings frente a TF-IDF:", round(adjusted_rand_score(ref, otra), 3))
registrar_entorno(semilla=0, nota=f"k-means k={K_ELEGIDO}")
```

Leer un grupo es mirar sus miembros más cercanos al centro y los más lejanos. Esos ocho textos son el material para proponer un nombre y para pedirle uno a un modelo de lenguaje.

```python
for g in range(K_ELEGIDO):
    idx = np.where(ref == g)[0]
    centro = E[idx].mean(axis=0)
    orden = np.argsort(-(E[idx] @ centro))
    print(f"\n=== grupo {g} · {len(idx)} miembros ===")
    print("más cerca del centro:")
    for i in idx[orden[:5]]:
        print("   ", textos[i][:100])
    print("más lejos del centro (candidatos a contraejemplo):")
    for i in idx[orden[-3:]]:
        print("   ", textos[i][:100])
```

## Semana 4. Grafo de coocurrencia

El grafo se construye desde una tabla de unidades con sus códigos. La unidad es la primera decisión; el umbral de peso, la segunda. El bloque cuenta cuántas unidades comparte cada par de códigos y construye el grafo para un umbral dado.

```python
import networkx as nx
from itertools import combinations
from collections import Counter

unidades = pd.read_csv("unidades.csv")     # columnas: id, fecha, codigos (separados por ;)
pesos = Counter()
for cods in unidades["codigos"].fillna("").astype(str):
    lista = sorted({c.strip() for c in cods.split(";") if c.strip()})
    for a, b in combinations(lista, 2):
        pesos[(a, b)] += 1
todos = {c for par in pesos for c in par}

def grafo(umbral):
    G = nx.Graph()
    G.add_nodes_from(todos)
    for (a, b), w in pesos.items():
        if w >= umbral:
            G.add_edge(a, b, weight=w)
    return G
```

Las medidas se calculan sobre el grafo filtrado, y por eso cada número lleva su umbral. Las comunidades se calculan con dos algoritmos para ver dónde coinciden.

```python
UMBRALES = [1, 3, 6]     # decisión: el mínimo, uno medio, uno alto; ajuste a su corpus

for u in UMBRALES:
    G = grafo(u)
    conectados = [n for n in G if G.degree(n) > 0]
    H = G.subgraph(conectados)
    fuerza = dict(H.degree(weight="weight"))
    inter = nx.betweenness_centrality(H)
    louvain = nx.community.louvain_communities(H, weight="weight", seed=0)
    voraz = nx.community.greedy_modularity_communities(H, weight="weight")
    puentes = sorted(inter, key=inter.get, reverse=True)[:5]
    print(f"\numbral ≥ {u}: {H.number_of_edges()} aristas · {nx.number_connected_components(H)} componentes · "
          f"{len(louvain)} comunidades (Lovaina) · {len(voraz)} (voraz) · {len(todos) - len(conectados)} aislados")
    print("  puentes por intermediación:", puentes)
    print("  nodos más fuertes:", sorted(fuerza, key=fuerza.get, reverse=True)[:5])
    for i, c in enumerate(louvain):
        print(f"  comunidad {i + 1}:", sorted(c))
```

El dibujo es un instrumento más. Dos semillas del algoritmo de disposición dan dos imágenes del mismo grafo; se guardan ambas y se declara cuál se usa.

```python
U = 3
G = grafo(U).subgraph([n for n in grafo(U) if grafo(U).degree(n) > 0])
fuerza = dict(G.degree(weight="weight"))
for semilla in [0, 1]:
    pos = nx.spring_layout(G, weight="weight", seed=semilla)
    plt.figure(figsize=(9, 7))
    nx.draw(G, pos, with_labels=True, font_size=8,
            node_size=[30 * fuerza[n] for n in G],
            width=[0.4 * G[a][b]["weight"] for a, b in G.edges()])
    plt.title(f"umbral ≥ {U} · disposición por fuerzas · semilla {semilla}")
    plt.savefig(f"grafo_u{U}_s{semilla}.png", dpi=150, bbox_inches="tight")
```

Quitar un nodo y recalcular muestra si la estructura depende de él.

```python
QUITAR = "escriba aquí el código que sospecha"
if QUITAR in G:
    G2 = G.copy(); G2.remove_node(QUITAR)
    print("sin", QUITAR, "->", nx.number_connected_components(G2), "componentes,",
          len(nx.community.louvain_communities(G2, weight="weight", seed=0)), "comunidades")
```

## Semana 5. Serie del corpus, ventanas y rupturas

La serie cuenta, por periodo, la proporción de documentos que contienen un código. Se normaliza por el tamaño del corpus en el periodo porque el conteo crudo cuenta la recolección, no el fenómeno. El periodo es la primera decisión; la ventana de suavizado, la segunda.

```python
CODIGO = "desalojo"            # decisión: qué se cuenta
PERIODO = "MS"                 # decisión: "MS" mensual, "QS" trimestral, "YS" anual

corpus["fecha"] = pd.to_datetime(corpus["fecha"], errors="coerce")
corpus["tiene"] = corpus["texto"].str.contains(CODIGO, case=False, na=False)
# si tiene columna de códigos, use en cambio:
# corpus["tiene"] = corpus["codigos"].fillna("").str.split(";").apply(lambda l: CODIGO in [c.strip() for c in l])

serie = (corpus.dropna(subset=["fecha"]).set_index("fecha")
         .resample(PERIODO).agg(total=("tiene", "size"), con_codigo=("tiene", "sum")))
serie["proporcion"] = (serie["con_codigo"] / serie["total"]).fillna(0)

VENTANAS = [1, 3, 9]
for w in VENTANAS:
    serie[f"suave_{w}"] = serie["proporcion"].rolling(w, center=True, min_periods=1).mean()
print(serie.tail())
```

La ruptura por diferencia de medias marca el periodo donde más cambia el promedio entre los `w` periodos anteriores y los `w` siguientes. Es el método de la mini app. PELT busca varias rupturas con una penalización por cada una; la penalización cumple el papel de la ventana.

```python
import ruptures as rpt

def ruptura(valores, w):
    v = np.asarray(valores, dtype=float)
    mejor, donde = -1.0, None
    for t in range(w, len(v) - w + 1):
        d = abs(v[t:t + w].mean() - v[t - w:t].mean())
        if d > mejor:
            mejor, donde = d, t
    return donde, mejor

for w in VENTANAS:
    t, salto = ruptura(serie["proporcion"], w)
    print(f"ventana {w}: ruptura en {serie.index[t].date()} (salto {salto:.3f})")

senal = serie["proporcion"].to_numpy()
senal = (senal - senal.mean()) / (senal.std() or 1)       # estandarizada para que la penalización tenga escala
algo = rpt.Pelt(model="l2").fit(senal)
for pen in [1, 3, 10]:
    puntos = algo.predict(pen=pen)[:-1]
    print(f"PELT pen={pen}:", [str(serie.index[p].date()) for p in puntos])
```

La gráfica lleva la serie y, debajo, el tamaño del corpus por periodo, porque un lector debe poder ver si la ruptura coincide con un cambio en la recolección.

```python
fig, (a1, a2) = plt.subplots(2, 1, figsize=(10, 6), sharex=True, height_ratios=[3, 1])
a1.plot(serie.index, serie["proporcion"], color="gray", lw=0.8, label="cruda")
for w in VENTANAS:
    a1.plot(serie.index, serie[f"suave_{w}"], lw=1.6, label=f"ventana {w}")
a1.set_ylabel(f"proporción con «{CODIGO}»"); a1.legend()
a2.bar(serie.index, serie["total"], width=20, color="gray"); a2.set_ylabel("documentos")
plt.savefig("serie.png", dpi=150, bbox_inches="tight")
```

## Semana 6. Modelado de temas

La asignación latente de Dirichlet describe cada documento como mezcla de K temas y cada tema como distribución sobre palabras. K es una decisión de entrada y la semilla cambia el resultado. El bloque corre dos K y dos semillas y guarda las veinte palabras principales de cada tema.

```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

KS_TEMAS, SEMILLAS_TEMAS = [8, 20], [0, 1]       # decisiones: un K bajo y uno alto para su corpus

cv = CountVectorizer(strip_accents="unicode", stop_words=STOP, min_df=3, max_df=0.9)
C = cv.fit_transform(textos)
vocab = cv.get_feature_names_out()

temas = {}
for K in KS_TEMAS:
    for s in SEMILLAS_TEMAS:
        lda = LatentDirichletAllocation(n_components=K, random_state=s, learning_method="batch").fit(C)
        theta = lda.transform(C)                      # proporción de cada tema en cada documento
        listas = [list(vocab[np.argsort(-fila)[:20]]) for fila in lda.components_]
        temas[(K, s)] = {"listas": listas, "theta": theta}
        print(f"\n=== K={K} · semilla {s} ===")
        for i, l in enumerate(listas):
            print(f"  tema {i}:", ", ".join(l[:10]))
```

Un tema es candidato si aparece, con las mismas palabras principales, en las cuatro corridas. El bloque empareja cada tema de la corrida de referencia con el más parecido de cada otra corrida por Jaccard sobre las veinte palabras.

```python
REF = (KS_TEMAS[0], 0)
for otra in [c for c in temas if c != REF]:
    print(f"\nreferencia {REF} frente a {otra}:")
    for i, la in enumerate(temas[REF]["listas"]):
        js = [jaccard(set(la), set(lb)) for lb in temas[otra]["listas"]]
        j = int(np.argmax(js))
        print(f"  tema {i} ~ tema {j} (Jaccard {js[j]:.2f}): {', '.join(la[:6])}")
```

Para leer un tema se miran sus documentos de mayor peso, no solo sus palabras. Esos documentos son también los contraejemplos posibles del nombre que se proponga.

```python
TEMA = 0
theta = temas[REF]["theta"]
for i in np.argsort(-theta[:, TEMA])[:5]:
    print(f"{theta[i, TEMA]:.2f}  {textos[i][:120]}")
```

## Semana 7. Un panel honesto

Un panel declara la pregunta, la escala, los parámetros, la prueba de estabilidad, lo que afirma y, separada, la lectura. El bloque construye un panel con Plotly a partir de la serie anual; el eje empieza en cero y el pie lleva las seis casillas. Repita el patrón para cada vista del tablero.

```python
import plotly.graph_objects as go

anual = (corpus.dropna(subset=["fecha"]).set_index("fecha")
         .resample("YS").agg(total=("tiene", "size"), con_codigo=("tiene", "sum")))
anual["pct"] = 100 * anual["con_codigo"] / anual["total"]

PREGUNTA = f"¿Crece la proporción de documentos que mencionan «{CODIGO}»?"
PARAMETROS = "agregación anual · sin suavizado · la tendencia se mantiene con agregación trimestral"
AFIRMA = f"la proporción pasa de {anual['pct'].iloc[0]:.0f} % a {anual['pct'].iloc[-1]:.0f} %"
LECTURA = "escriba aquí su lectura, separada de lo que la vista afirma"

fig = go.Figure(go.Bar(x=anual.index.year, y=anual["pct"], marker_color="#2B55B8",
                       text=anual["total"], textposition="outside"))
fig.update_layout(
    title=PREGUNTA, yaxis=dict(range=[0, max(20, anual["pct"].max() * 1.2)], title="% de documentos del año"),
    xaxis=dict(title="año (n de documentos sobre cada barra)"), margin=dict(b=160),
    annotations=[dict(xref="paper", yref="paper", x=0, y=-0.32, showarrow=False, align="left",
                      text=f"<b>Parámetros y estabilidad:</b> {PARAMETROS}<br>"
                           f"<b>Lo que la vista afirma:</b> {AFIRMA}<br>"
                           f"<b>Lectura del investigador:</b> {LECTURA}")])
fig.write_html("panel_serie.html")
```

El tablero reúne los paneles en una sola página. Este bloque escribe un archivo que incrusta los paneles guardados; no necesita servidor.

```python
PANELES = ["nube_umap.html", "grafo_u3_s0.png", "panel_serie.html"]   # añada los suyos

partes = []
for p in PANELES:
    if p.endswith(".html"):
        partes.append(f'<iframe src="{p}" style="width:100%;height:560px;border:0"></iframe>')
    else:
        partes.append(f'<img src="{p}" style="max-width:100%">')
html = "<!doctype html><meta charset='utf-8'><title>Tablero</title>" + "\n".join(partes)
with open("tablero.html", "w", encoding="utf-8") as f:
    f.write(html)
```

## Nota sobre costos y privacidad

Todas las bibliotecas del cuaderno son abiertas y corren en el computador propio; los modelos de embeddings se descargan una vez. No suba a ningún servicio material con datos personales de terceros. Si su corpus es sensible, haga la práctica con una muestra anonimizada. El curso 7 del programa trata estos problemas en detalle.
