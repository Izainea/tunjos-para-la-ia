# Semana 2. Embeddings de texto e imagen

## Pregunta de la semana

Si un vector aprendido por un modelo acerca "arriendo" a "renta" sin que nadie se lo haya dicho, ¿qué sabe ese vector del corpus propio, y qué sabe de otra cosa?

## Por qué esta semana

<p class="lede">La bolsa de palabras de la semana anterior pierde los sinónimos porque cuenta formas. Los embeddings resuelven ese problema con una idea de 1954 y una potencia de cálculo de este siglo: una palabra se conoce por la compañía que lleva, y un modelo puede aprender, de miles de millones de frases, un vector para cada palabra, cada oración o cada imagen, de modo que lo que aparece en contextos parecidos quede cerca. El resultado es un instrumento de alcance enorme y de origen ajeno. Los vectores no se calcularon sobre el corpus del estudiante sino sobre un corpus que otros reunieron en otra parte, con otros fines. Esta semana enseña a obtenerlos, a leer lo que codifican, y a tratar su origen como lo que es: una precomprensión que no es la de la comunidad cuyo material se interpreta.</p>

La semana supone lo visto en la primera: una representación conserva unas cosas y pierde otras, y el coseno afirma un parecido de proporciones y nada más.

## Contenido de la sesión

1. Un embedding es un vector aprendido, no contado. En la bolsa de palabras cada dimensión es una palabra y el número es un conteo; en un embedding las dimensiones no significan nada por separado<sup class="mark">a</sup> y el vector entero se ajustó para que una tarea de predicción saliera bien. En word2vec (Mikolov et al., 2013) la tarea es predecir las palabras vecinas de cada palabra; en Sentence-BERT (Reimers y Gurevych, 2019) la tarea es que oraciones parafraseadas queden cerca; en CLIP (Radford et al., 2021) la tarea es que una imagen y su descripción queden cerca en el mismo espacio. Lo que el vector codifica es lo que sirvió para esa tarea.

<aside class="glosa"><span class="mark">a</span> Un embedding de oración típico tiene 384 o 768 dimensiones. Ninguna es "el tema" o "el tono"; el parecido se lee entre vectores completos, por coseno, y nunca mirando una coordenada.</aside>

2. La hipótesis distribucional sostiene todo el edificio. Firth la formuló en 1957, "se conoce una palabra por la compañía que lleva", y Harris la había hecho operativa en 1954: dos palabras que aparecen en contextos parecidos tienen significados parecidos. Es una hipótesis sobre el lenguaje, no una verdad: funciona porque en un corpus muy grande "arriendo" y "renta" rodean las mismas palabras, y falla donde el corpus no tiene suficientes contextos o donde el contexto local del investigador usa una palabra de otro modo. Un modelo entrenado con texto de internet sabe cómo se usa "parche" en millones de páginas y no sabe cómo lo usa un barrio.

3. Lo que un embedding codifica se lee en sus vecinos. La primera prueba de sentido de cualquier modelo sobre el corpus propio es tomar diez documentos y mirar, para cada uno, los cinco más cercanos por coseno. Si los vecinos tienen sentido para quien conoce el corpus, el modelo conserva algo que importa; si los vecinos comparten solo longitud, género textual o una palabra frecuente, el modelo conserva otra cosa. Esa lectura no la hace el modelo y no la hace una métrica: la hace alguien que conoce el material.

4. El sesgo del entrenamiento es una precomprensión ajena. Bolukbasi et al. (2016) mostraron que en vectores entrenados con noticias la analogía "hombre es a programador como mujer es a..." se completaba con "ama de casa": el vector había aprendido la regularidad del corpus, y el corpus llevaba una historia. Leído con la triple mímesis de *Tiempo y narración* (Ricœur, 1995), el embedding es una prefiguración, una Mímesis I, que no viene del mundo práctico de la comunidad cuyo material se analiza sino de otro. Esto no invalida el instrumento. Obliga a declarar con qué modelo se calcularon los vectores, con qué corpus se entrenó ese modelo cuando se sabe, y a buscar activamente los lugares donde la precomprensión ajena y el corpus propio chocan.

5. Para ver un espacio de 384 dimensiones hay que proyectarlo, y la proyección es otro instrumento con parámetros. PCA conserva las direcciones de mayor varianza y es lineal; UMAP (McInnes, Healy y Melville, 2018) y t-SNE (van der Maaten y Hinton, 2008) conservan vecindades locales y deforman las distancias grandes. Wattenberg, Viégas y Johnson (2016) muestran con ejemplos que t-SNE produce grupos donde no los hay y tamaños de grupo que no significan nada<sup class="mark">b</sup>. La nube de puntos que el estudiante verá en la mini app es una proyección de ese tipo: sirve para explorar y no para medir.

<aside class="glosa"><span class="mark">b</span> En t-SNE y UMAP la distancia entre dos grupos lejanos en el plano no se corresponde con su distancia en el espacio original, y cambiar la perplejidad o el número de vecinos cambia la figura entera. Toda nube de puntos debe decir con qué método y con qué parámetros se proyectó.</aside>

6. El trabajo de la semana sobre el corpus propio es elegir un modelo, registrar su nombre y versión, calcular los vectores, mirar vecinos y anotar los choques. Para texto en español el cuaderno de apoyo usa un modelo multilingüe de Sentence-BERT de descarga libre; para imágenes, CLIP. Quien no pueda correr modelos usa la bolsa de palabras con pesos TF-IDF<sup class="mark">c</sup>, que es más pobre y perfectamente defendible si se declara. En ambos casos la bitácora registra lo mismo: modelo, parámetros, diez documentos con sus vecinos, y una lectura de qué conserva el espacio y qué no.

| Bolsa de palabras | Embedding |
|---|---|
| Cada dimensión es una palabra; el número es un conteo | Ninguna dimensión significa nada sola; el vector entero se aprendió |
| Se calcula sobre el corpus propio y solo sobre él | Se calcula con lo aprendido en otro corpus |
| Pierde sinónimos y contexto | Recupera parte de ambos, con la precomprensión del corpus ajeno |
| Transparente: se puede ver qué palabra acerca dos documentos | Opaco: se ve que están cerca, no por qué |
| *Afirma menos y se explica entera* | *Afirma más y exige declarar de dónde viene* |

<aside class="glosa"><span class="mark">c</span> TF-IDF: el conteo de cada palabra en el documento, multiplicado por un factor que baja el peso de las palabras que aparecen en casi todos los documentos. Es la bolsa de palabras con una corrección que castiga lo común.</aside>

<figure class="wide">
  <svg viewBox="0 0 680 250" style="width:100%;max-width:42rem;height:auto;display:block" role="img" aria-label="Dos regiones: una grande, el corpus de entrenamiento del modelo, de origen ajeno, y una pequeña, el corpus propio, parcialmente dentro de la grande. Flechas indican que los vectores del corpus propio se calculan con la precomprensión aprendida en el corpus ajeno. La zona del corpus propio que queda fuera de la grande está marcada como lo que el modelo no vio.">
    <style>.t2{font-family:var(--text);font-size:13px;fill:var(--ink)} .s2{font-family:var(--text);font-size:11.5px;fill:var(--muted)} .m2{font-family:var(--mono);font-size:10.5px;letter-spacing:.06em;fill:var(--muted)} .mf{font-family:var(--mono);font-size:10.5px;letter-spacing:.06em;fill:var(--c-fil)} .g{fill:var(--surface);stroke:var(--rule);stroke-width:1.4} .p{fill:none;stroke:var(--accent);stroke-width:1.8} .ar{stroke:var(--muted);stroke-width:1.3;fill:none} .ah{fill:var(--muted)} .fr{stroke:var(--c-fil);stroke-width:1.6;stroke-dasharray:6 5;fill:none}</style>
    <defs><marker id="s2-ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 1L9 5L0 9z" class="ah"/></marker></defs>
    <ellipse cx="270" cy="125" rx="250" ry="100" class="g"/>
    <text x="60" y="60" class="m2">CORPUS DE ENTRENAMIENTO DEL MODELO</text>
    <text x="60" y="78" class="s2">miles de millones de frases, reunidas en otra parte, con otros fines</text>
    <ellipse cx="455" cy="150" rx="105" ry="55" class="p"/>
    <text x="400" y="118" class="m2">CORPUS PROPIO</text>
    <text x="392" y="160" class="s2">lo que el modelo "ya conoce"</text>
    <path class="fr" d="M520 95 L520 205"/>
    <text x="528" y="150" class="mf">LO QUE EL MODELO</text>
    <text x="528" y="166" class="mf">NO VIO</text>
    <path class="ar" d="M200 150 C 300 190 360 190 420 160" marker-end="url(#s2-ah)"/>
    <text x="235" y="205" class="s2">los vectores del corpus propio se calculan con</text>
    <text x="235" y="221" class="s2">la precomprensión aprendida aquí</text>
    <text x="20" y="243" class="m2">MÍMESIS I AJENA: EL MODELO PREFIGURA CON UN MUNDO QUE NO ES EL DEL CORPUS</text>
  </svg>
  <figcaption><b>Figura 2.</b> El espacio ajeno. El embedding del corpus propio se calcula con lo que el modelo aprendió en otro corpus; la parte del corpus propio que ese corpus no cubre es donde los vecinos dejan de tener sentido.</figcaption>
</figure>

<iframe class="app" src="apps/embeddings-y-k.html" title="Nube de puntos de embeddings con agrupamiento k-means y deslizador de k" loading="lazy"></iframe>

Esta semana la app se usa para explorar: pasar el cursor por los puntos, leer qué fragmentos quedaron cerca y marcar "mostrar tema de origen" para comparar la cercanía con la etiqueta con que se escribió cada fragmento. El deslizador de k es el tema de la semana 3.

## IA y exigencia

Se le pide a un modelo de lenguaje que escriba el código para calcular los embeddings del corpus propio y la lista de vecinos, a partir de los bloques del cuaderno de apoyo, y que proponga una lectura de por qué ciertos documentos quedaron cerca. El estudiante debe poder defender sin el modelo qué modelo de embeddings usó y por qué, qué tarea de entrenamiento define lo que ese modelo acerca, y al menos dos casos de su corpus en que los vecinos no tienen sentido para quien conoce el material. La lectura que el modelo de lenguaje proponga sobre los vecinos es una hipótesis del modelo, y como tal se registra.

## Lecturas

**Central**

- Mikolov, T., Chen, K., Corrado, G. y Dean, J. (2013). "Efficient Estimation of Word Representations in Vector Space". Secciones 1 a 3. https://arxiv.org/abs/1301.3781
- Reimers, N. y Gurevych, I. (2019). "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks". *EMNLP-IJCNLP 2019*. Secciones 1 a 3. https://arxiv.org/abs/1908.10084

**Complementaria**

- Grimmer, J., Roberts, M. E. y Stewart, B. M. (2022). *Text as Data*. Princeton University Press. Cap. 8, sobre representaciones distribuidas de palabras.
- Bolukbasi, T., Chang, K.-W., Zou, J., Saligrama, V. y Kalai, A. (2016). "Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings". *NeurIPS 2016*. https://arxiv.org/abs/1607.06520
- Radford, A. et al. (2021). "Learning Transferable Visual Models From Natural Language Supervision". https://arxiv.org/abs/2103.00020
- Wattenberg, M., Viégas, F. y Johnson, I. (2016). "How to Use t-SNE Effectively". *Distill*. https://distill.pub/2016/misread-tsne/
- McInnes, L., Healy, J. y Melville, J. (2018). "UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction". https://arxiv.org/abs/1802.03426
- Firth, J. R. (1957). "A Synopsis of Linguistic Theory 1930-1955". En *Studies in Linguistic Analysis*. Blackwell.

## Guía de lectura

- Mikolov et al. presentan dos arquitecturas que aprenden vectores prediciendo palabras vecinas, y muestran que los vectores resuelven analogías por aritmética. *¿Qué tendría que haber en el corpus de entrenamiento para que "rey menos hombre más mujer" dé "reina"? ¿Qué analogía de su campo no daría?*
- Reimers y Gurevych entrenan el modelo para que oraciones parafraseadas queden cerca, y miden el resultado en conjuntos de pares etiquetados por personas. *¿Quién decidió qué pares son parecidos, y se parecería su criterio al de esos anotadores?*
- Bolukbasi et al. muestran un sesgo y proponen corregirlo por geometría. *¿La corrección elimina la precomprensión ajena o la reemplaza por otra, la de quien corrige?*
- Wattenberg, Viégas y Johnson muestran nubes de t-SNE que inventan grupos. *¿Qué prueba haría usted antes de decir que un grupo visible en una proyección existe en el espacio original?*

## Taller de la segunda hora

Sobre el corpus propio, con el bloque de la semana 2 del cuaderno de apoyo (o con TF-IDF si no se pueden correr modelos):

1. Calcule los vectores de todos los documentos con un modelo declarado. Registre nombre, versión y dimensión.
2. Elija diez documentos que conozca bien. Para cada uno, liste los cinco vecinos más cercanos por coseno.
3. Llene la tabla:

| Documento | Vecinos con sentido para mí | Vecinos sin sentido | Qué parece conservar el espacio | Qué parece no ver |
|---|---|---|---|---|

4. Proyecte el corpus a dos dimensiones con PCA y con UMAP. Compare: ¿los vecinos de la tabla siguen cerca en las dos proyecciones?
5. Anote un choque entre la precomprensión del modelo y su corpus: una palabra o un tipo de imagen que el modelo acerca a cosas que en su material no van juntas.

## Guion de la sesión

| Minuto | Momento | Docente | Estudiante | Material |
|---|---|---|---|---|
| 0 a 10 | Apertura | Retoma los pares de la semana 1 donde la bolsa de palabras falló y anuncia qué corrigen los embeddings | Recuerda su par de coseno bajo con parecido real | Bitácora 1 |
| 10 a 35 | Lectura | Explica la tarea de entrenamiento de word2vec y de Sentence-BERT sobre la pizarra; discute la guía | Responde qué codifica cada tarea | Lecturas centrales |
| 35 a 55 | Mecanismo | Explora la nube de la mini app; muestra un vecino con sentido y uno sin sentido; activa el anillo de origen | Predice qué puntos quedarán cerca | App de embeddings |
| 55 a 65 | Pausa | | | |
| 65 a 105 | Taller | Acompaña el cálculo de vectores y vecinos sobre corpus propios; resuelve instalaciones | Llena la tabla de vecinos y busca el choque | Cuaderno, semana 2 |
| 105 a 120 | Cierre | Recoge los choques encontrados | Nombra su choque y el modelo que usó | Bitácora |

Notas para el docente. Lo que suele fallar: la instalación del modelo de embeddings consume la mitad del taller; pedir que se haga antes de la sesión y tener un archivo de vectores precalculados del conjunto de ejercicio para quien no lo logre. Segundo fallo: el estudiante lee la nube de puntos como si las distancias en el plano fueran distancias reales; volver a Wattenberg y mostrar la misma nube con otra proyección. Tercero: la discusión sobre sesgo se vuelve una discusión sobre si "la IA es sexista"; devolverla a la pregunta del curso, que es qué precomprensión trae el instrumento y cómo se declara.

## Bitácora

Registre el modelo, la tabla de vecinos, las dos proyecciones y el choque encontrado. Añada una línea sobre qué representación va a usar en el producto de la semana 3 y por qué: embeddings, TF-IDF o ambas.

## Para la próxima semana

Leer Grimmer, Roberts y Stewart (2022), capítulo 12, sobre agrupamiento. Llegar con los vectores del corpus calculados y guardados en un archivo: la semana 3 agrupa, prueba la estabilidad y entrega el primer producto. Leer la plantilla `plantillas/ficha-de-patron.md`.
