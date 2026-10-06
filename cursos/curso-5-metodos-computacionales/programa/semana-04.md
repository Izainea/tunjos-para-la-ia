# Semana 4. Redes: el grafo como hipótesis relacional

## Pregunta de la semana

Cuando dos códigos aparecen juntos en muchos documentos y el grafo los dibuja unidos, ¿qué relación afirma esa arista, y quién la afirma?

## Por qué esta semana

<p class="lede">Un grafo parece el más objetivo de los instrumentos: puntos y líneas, nada que interpretar. Es lo contrario. Antes de que exista una sola arista alguien decidió qué cuenta como nodo, qué cuenta como relación y a partir de qué peso una relación merece dibujarse. Un grafo de coocurrencia de códigos es, por eso, una hipótesis relacional sobre el corpus: la hipótesis de que aparecer juntos en un documento significa algo. Las medidas que se calculan después, grado, centralidad, comunidades, son propiedades de esa hipótesis, no del corpus. Esta semana enseña a construir el grafo del corpus propio, a leer sus medidas por lo que miden, y a mostrar qué le pasa cuando se mueve el único parámetro que casi nadie declara: el umbral.</p>

La semana supone un corpus con unidades que puedan relacionarse: códigos de un libro de códigos, actores nombrados en documentos, etiquetas de imágenes. Quien no los tenga usa los grupos de la semana 3 como códigos.

## Contenido de la sesión

1. Un grafo es un conjunto de nodos y un conjunto de aristas, y elegir ambos ya es interpretar. En un grafo de coocurrencia los nodos son códigos y hay una arista entre dos códigos cuando aparecen en la misma unidad; pero la unidad puede ser el documento, el párrafo o una ventana de veinte palabras, y cada elección produce un grafo distinto. Lo mismo vale para actores que aparecen en la misma noticia o etiquetas que acompañan la misma imagen. Newman (2018, cap. 6) presenta el grafo como objeto matemático; el curso añade que ese objeto se construyó con decisiones que el informe debe declarar.

2. Las medidas de un grafo miden posiciones, no importancia. El grado de un nodo es cuántos vecinos tiene; la fuerza, la suma de los pesos de sus aristas; la intermediación (Freeman, 1978)<sup class="mark">a</sup>, cuántos caminos más cortos entre otros nodos pasan por él. Un código con alta intermediación y pocos vecinos está en una posición de puente que depende de pocas aristas y puede desaparecer al subir el umbral. Decir que un nodo es "central" sin decir en qué medida y con qué umbral es decir poco.

<aside class="glosa"><span class="mark">a</span> Intermediación: para cada par de nodos se cuentan los caminos más cortos y se mira qué fracción pasa por el nodo evaluado. Brandes (2001) dio el algoritmo que la hace calculable en grafos grandes. La mini app la calcula sobre el grafo filtrado por el umbral.</aside>

3. Las comunidades son particiones del método, como los grupos de la semana 3. La modularidad (Newman, 2006) mide cuánto más densas son las conexiones dentro de los grupos que lo esperado al azar, y los algoritmos que la maximizan, como el de Lovaina (Blondel et al., 2008), encuentran siempre alguna partición, también en grafos aleatorios. Fortunato (2010) revisa decenas de métodos y muestra que no coinciden entre sí. La prueba que el curso pide es la misma de la semana anterior: ¿la comunidad sobrevive a cambiar el algoritmo, la semilla y el umbral?

4. El umbral es el parámetro que cambia el grafo entero. Con umbral uno, casi todo está conectado con casi todo y las comunidades son una sola; con umbral alto, quedan unos pocos núcleos y muchos aislados. Entre los dos extremos hay una zona en que el grafo se parte<sup class="mark">b</sup>, y el umbral que se elige decide qué se ve. La práctica de la semana pide el grafo con tres umbrales y la tabla de qué comunidades y qué puentes se mantienen en los tres. Lo que aparece en uno solo se reporta como dependiente del umbral.

<aside class="glosa"><span class="mark">b</span> En física de redes, el punto en que un grafo pasa de muchos fragmentos a un componente gigante se llama transición de percolación (Barabási, 2016, cap. 3 en adelante). En un grafo de coocurrencia, subir el umbral recorre esa transición al revés.</aside>

5. Leer un grafo es proponer qué significa la estructura, y eso exige teoría. Granovetter (1973) leyó los lazos débiles como puentes por donde circula información nueva; la lectura no estaba en el grafo, estaba en la pregunta sociológica que él traía. Moretti (2015), en "Teoría de redes, análisis de la trama", dibuja el grafo de los personajes de *Hamlet* y descubre que al quitar a Horacio la corte pierde su conexión con el mundo exterior: la lectura vale porque Moretti conoce la obra. Un puente entre la comunidad de códigos de seguridad y la de cultura puede ser una categoría nueva, un error de codificación o un artefacto del umbral, y solo quien conoce el corpus puede decir cuál.

6. Cuando la relación tiene dirección, el grafo cuenta caminos. Quién cita a quién, quién contrata a quién y qué código precede a cuál en un relato son relaciones dirigidas, y en ellas importa no solo quién está conectado sino por dónde puede fluir algo. Los algebristas llaman carcaj, *quiver*, a un grafo dirigido mirado desde la composición de sus flechas, y el álgebra de caminos lleva la contabilidad exacta de cuántos caminos de cada longitud hay entre dos nodos (Zainea, 2026). Esa contabilidad es la que usan las redes neuronales de grafos cuando propagan información a lo largo de varias aristas, y es también lo que se pierde cuando demasiados caminos se comprimen en un solo vector. El curso no desarrolla el tema; lo señala como la frontera entre el grafo que se lee y el grafo con el que se calcula.

7. El dibujo de un grafo es un instrumento más, con parámetros propios. Los algoritmos de disposición por fuerzas ponen cerca lo conectado y lejos lo desconectado, con una semilla aleatoria; la posición de un nodo en el plano no es un dato, y dos dibujos del mismo grafo pueden sugerir estructuras distintas. El botón "reubicar" de la mini app existe para que el estudiante lo compruebe.

<figure class="wide">
  <svg viewBox="0 0 680 270" style="width:100%;max-width:42rem;height:auto;display:block" role="img" aria-label="Tres documentos con sus códigos a la izquierda; en el centro, el grafo de coocurrencia que resulta de unir códigos que comparten documento, con pesos; a la derecha, el mismo grafo con umbral dos, donde una arista desaparece y un código queda aislado. Un rótulo marca que cada paso es una decisión.">
    <style>.t4{font-family:var(--text);font-size:12.5px;fill:var(--ink)} .s4{font-family:var(--text);font-size:11px;fill:var(--muted)} .m4{font-family:var(--mono);font-size:10.5px;letter-spacing:.06em;fill:var(--muted)} .mf4{font-family:var(--mono);font-size:10.5px;letter-spacing:.06em;fill:var(--c-fil)} .bx{fill:var(--surface);stroke:var(--rule);stroke-width:1.2} .nd{fill:var(--c-app)} .ndg{fill:var(--surface);stroke:var(--muted);stroke-width:1.2} .e1{stroke:var(--muted);stroke-width:1.2} .e3{stroke:var(--muted);stroke-width:3.4} .ex{stroke:var(--c-fil);stroke-width:1.2;stroke-dasharray:4 3} .ar{stroke:var(--muted);stroke-width:1.3;fill:none} .ah{fill:var(--muted)}</style>
    <defs><marker id="s4-ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 1L9 5L0 9z" class="ah"/></marker></defs>
    <text x="10" y="18" class="m4">DOCUMENTOS Y CÓDIGOS</text>
    <rect x="10" y="30" width="180" height="46" rx="3" class="bx"/><text x="18" y="48" class="t4">doc 1</text><text x="18" y="66" class="s4">miedo · alumbrado · parque</text>
    <rect x="10" y="86" width="180" height="46" rx="3" class="bx"/><text x="18" y="104" class="t4">doc 2</text><text x="18" y="122" class="s4">miedo · alumbrado · rejas</text>
    <rect x="10" y="142" width="180" height="46" rx="3" class="bx"/><text x="18" y="160" class="t4">doc 3</text><text x="18" y="178" class="s4">miedo · alumbrado · fiesta</text>
    <path class="ar" d="M196 110 L228 110" marker-end="url(#s4-ah)"/>
    <text x="240" y="18" class="m4">GRAFO · UMBRAL 1</text>
    <g transform="translate(240 0)">
      <line x1="60" y1="60" x2="60" y2="160" class="e3"/>
      <line x1="60" y1="60" x2="150" y2="40" class="e1"/><line x1="60" y1="160" x2="150" y2="40" class="e1"/>
      <line x1="60" y1="60" x2="160" y2="110" class="e1"/><line x1="60" y1="160" x2="160" y2="110" class="e1"/>
      <line x1="60" y1="60" x2="150" y2="180" class="e1"/><line x1="60" y1="160" x2="150" y2="180" class="e1"/>
      <circle cx="60" cy="60" r="8" class="nd"/><text x="12" y="52" class="s4">miedo</text>
      <circle cx="60" cy="160" r="8" class="nd"/><text x="4" y="185" class="s4">alumbrado</text>
      <circle cx="150" cy="40" r="6" class="nd"/><text x="162" y="44" class="s4">parque</text>
      <circle cx="160" cy="110" r="6" class="nd"/><text x="172" y="114" class="s4">rejas</text>
      <circle cx="150" cy="180" r="6" class="nd"/><text x="162" y="196" class="s4">fiesta</text>
      <text x="66" y="116" class="m4">3</text>
    </g>
    <path class="ar" d="M446 110 L478 110" marker-end="url(#s4-ah)"/>
    <text x="490" y="18" class="m4">GRAFO · UMBRAL 2</text>
    <g transform="translate(490 0)">
      <line x1="60" y1="60" x2="60" y2="160" class="e3"/>
      <line x1="60" y1="60" x2="150" y2="40" class="ex"/><line x1="60" y1="160" x2="150" y2="40" class="ex"/>
      <line x1="60" y1="60" x2="160" y2="110" class="ex"/><line x1="60" y1="160" x2="160" y2="110" class="ex"/>
      <line x1="60" y1="60" x2="150" y2="180" class="ex"/><line x1="60" y1="160" x2="150" y2="180" class="ex"/>
      <circle cx="60" cy="60" r="8" class="nd"/><circle cx="60" cy="160" r="8" class="nd"/>
      <circle cx="150" cy="40" r="6" class="ndg"/><circle cx="160" cy="110" r="6" class="ndg"/><circle cx="150" cy="180" r="6" class="ndg"/>
      <text x="66" y="116" class="m4">3</text>
      <text x="100" y="230" class="mf4">TRES AISLADOS</text>
    </g>
    <text x="10" y="222" class="mf4">DECISIÓN 1: QUÉ ES UNA UNIDAD</text>
    <text x="240" y="222" class="mf4">DECISIÓN 2: QUÉ ES UNA ARISTA</text>
    <text x="10" y="256" class="s4">Cada paso es una decisión del investigador; el grafo que se lee al final es la suma de esas decisiones, y cambiar una cambia la lectura.</text>
  </svg>
  <figcaption><b>Figura 4.</b> El grafo como hipótesis relacional. De tres documentos codificados salen dos grafos distintos según el umbral; en el segundo, "parque", "rejas" y "fiesta" ya no se relacionan con nada. Ninguno de los dos es el corpus.</figcaption>
</figure>

<iframe class="app" src="apps/grafo-coocurrencia.html" title="Grafo de coocurrencia de códigos con umbral ajustable, comunidades y panel del nodo seleccionado" loading="lazy"></iframe>

## IA y exigencia

Se le pide a un modelo de lenguaje que escriba el código de construcción del grafo y de sus medidas a partir del cuaderno, y que proponga una lectura de las comunidades encontradas. El estudiante debe poder defender sin el modelo qué unidad de coocurrencia eligió y por qué, qué afirma cada medida que reporta, qué cambia en el grafo con los tres umbrales, y en qué se apoya la lectura de cada puente: en el corpus, en teoría, o en nada todavía. La lectura que proponga el modelo sobre las comunidades se registra como hipótesis del modelo, con la nota de que el modelo no ha leído los documentos.

## Lecturas

**Central**

- Newman, M. E. J. (2018). *Networks*. 2.ª ed. Oxford University Press. Caps. 6 y 7, sobre la matemática de las redes y sobre medidas y métricas. Leer por lo que mide cada medida, no por las fórmulas.
- Barabási, A.-L. (2016). *Network Science*. Cambridge University Press. Cap. 2, "Graph Theory". Libro completo de acceso abierto: http://networksciencebook.com/

**Complementaria**

- Freeman, L. C. (1978). "Centrality in Social Networks: Conceptual Clarification". *Social Networks* 1(3), 215-239. https://doi.org/10.1016/0378-8733(78)90021-7
- Newman, M. E. J. (2006). "Modularity and Community Structure in Networks". *PNAS* 103(23), 8577-8582. https://doi.org/10.1073/pnas.0601602103
- Blondel, V. D., Guillaume, J.-L., Lambiotte, R. y Lefebvre, E. (2008). "Fast Unfolding of Communities in Large Networks". *Journal of Statistical Mechanics: Theory and Experiment*, P10008. https://arxiv.org/abs/0803.0476
- Fortunato, S. (2010). "Community Detection in Graphs". *Physics Reports* 486(3-5), 75-174. https://arxiv.org/abs/0906.0612
- Granovetter, M. S. (1973). "The Strength of Weak Ties". *American Journal of Sociology* 78(6), 1360-1380. https://doi.org/10.1086/225469
- Moretti, F. (2015). *Lectura distante*. Fondo de Cultura Económica. "Teoría de redes, análisis de la trama".
- Zainea, C. I. (2026). "¿Qué es un quiver y por qué debería importarle a quien trabaja con datos?". https://izainea.github.io/blog/que-es-un-quiver/

## Guía de lectura

- Newman define varias centralidades y muestra que ordenan los nodos de forma distinta. *Elija dos nodos de su grafo: ¿cuál es más central por grado y cuál por intermediación? ¿Qué pregunta de su investigación respondería cada una?*
- Barabási presenta la matriz de adyacencia y los grafos ponderados y dirigidos como variantes de un mismo objeto. *¿Su relación tiene dirección? Si "A aparece con B" es simétrico pero "A precede a B" no, ¿cuál de las dos le importa?*
- Granovetter lee los lazos débiles con una teoría sobre la circulación de información. *¿Qué teoría traería usted para leer un puente entre dos comunidades de su grafo? Si no tiene ninguna, ¿qué diría del puente?*
- Moretti quita un personaje del grafo y observa qué pasa con el resto. *¿Qué nodo quitaría de su grafo para ver si la estructura depende de él?*

## Taller de la segunda hora

Sobre el corpus propio, con el bloque de la semana 4 del cuaderno de apoyo:

1. Defina la unidad de coocurrencia y constrúyala: una tabla con una fila por unidad y la lista de códigos, actores o etiquetas que contiene.
2. Construya el grafo ponderado. Calcule grado, fuerza e intermediación de cada nodo, y las comunidades con el algoritmo de Lovaina y con uno más.
3. Repita con tres umbrales: el mínimo, uno medio y uno alto. Llene la tabla:

| Umbral | Aristas | Componentes | Comunidades | Puentes (nodos con alta intermediación) | Aislados |
|---|---|---|---|---|---|

4. Marque las comunidades y los puentes que aparecen en los tres umbrales. Son los candidatos a lectura.
5. Dibuje el grafo dos veces con semillas distintas y guarde ambas imágenes: en la entrega se declara cuál se usó y por qué.

## Guion de la sesión

| Minuto | Momento | Docente | Estudiante | Material |
|---|---|---|---|---|
| 0 a 10 | Apertura | Muestra el grafo de la mini app con umbral uno y con umbral ocho y pregunta cuál es "el" grafo | Anota qué unidad de coocurrencia tiene su corpus | App de grafo |
| 10 a 30 | Lectura | Explica grado, fuerza, intermediación y modularidad por lo que miden; discute la guía | Responde con nodos de su propio corpus | Lecturas centrales |
| 30 a 55 | Mecanismo | Sube el umbral paso a paso en la mini app; selecciona un puente y lee su panel; pulsa "reubicar" | Predice qué nodo quedará aislado primero | App de grafo |
| 55 a 65 | Pausa | | | |
| 65 a 105 | Taller | Acompaña la construcción del grafo propio y la tabla de tres umbrales | Construye y llena la tabla | Cuaderno, semana 4 |
| 105 a 120 | Cierre | Recoge los puentes estables y pregunta qué teoría los leería | Nombra un puente y su posible lectura | Bitácora |

Notas para el docente. Lo que suele fallar: el estudiante construye el grafo con umbral uno y lo encuentra ilegible, o con umbral alto y lo encuentra vacío, y concluye en ambos casos que el grafo "no sirve"; insistir en la zona intermedia y en la tabla de tres umbrales. Segundo fallo: la posición en el dibujo se lee como dato ("este código está en el centro"); usar "reubicar" hasta que la idea se desgaste. Tercero: las comunidades coinciden con las categorías del libro de códigos y el estudiante lo toma como confirmación; preguntar si podría ser de otra forma, dado que los códigos se asignaron con esas categorías en mente.

## Bitácora

Registre la unidad de coocurrencia, la tabla de tres umbrales, las dos imágenes del grafo y los candidatos a lectura. Añada una línea sobre qué puente le sorprendió y qué teoría, si alguna, lo leería. Esta bitácora es el borrador del producto de la semana 5.

## Para la próxima semana

Leer Kleinberg (2003), secciones 1 y 2, y Grimmer, Roberts y Stewart (2022), capítulo 2. Llegar con el corpus propio fechado: cada documento o imagen con una fecha o un periodo. La semana 5 construye la serie temporal del corpus y entrega el grafo con su lectura, sobre la plantilla `plantillas/lectura-de-grafo.md`.
