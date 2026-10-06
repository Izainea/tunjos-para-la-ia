# Semana 3. El número de grupos como decisión del agrupamiento

## Pregunta de la semana

Si k-means con k igual a cuatro encuentra cuatro grupos y con k igual a cinco encuentra cinco, ¿cuántos grupos hay en el corpus?

## Por qué esta semana

<p class="lede">La respuesta honesta a la pregunta de la semana es que la pregunta está mal hecha. Un algoritmo de agrupamiento no descubre cuántos grupos hay: produce la mejor partición en el número de grupos que se le pidió, y la produce siempre, incluso sobre ruido. Es un inductor de enorme alcance que no elige entre hipótesis. Por eso la semana no enseña a "encontrar el k correcto" sino algo más útil y más exigente: a tratar cada grupo como un candidato, a someterlo a pruebas que el método no hace solo, y a decidir, con razones que se puedan escribir, cuáles de esos candidatos merecen el nombre de categoría. Es la primera entrega del curso y el primer lugar donde el estudiante firma una lectura.</p>

La semana supone los vectores del corpus propio calculados en la semana 2, con el modelo o la representación declarados.

## Contenido de la sesión

1. Agrupar es inducir una partición a partir de distancias. k-means<sup class="mark">a</sup> elige k centros, asigna cada punto al centro más cercano, mueve cada centro al promedio de sus puntos y repite hasta que nada cambia. El resultado depende de k, que es un dato de entrada, y de los centros iniciales, que son aleatorios. Dos corridas con distinta semilla pueden dar particiones distintas sobre los mismos vectores. Nada de esto es un defecto del algoritmo: es lo que el algoritmo es.

<aside class="glosa"><span class="mark">a</span> k-means minimiza la suma de distancias al cuadrado entre cada punto y el centro de su grupo. Encuentra un mínimo local, no el global; por eso se corre varias veces con semillas distintas y se conserva la mejor. Fue formulado por Lloyd en 1957 y publicado en 1982.</aside>

2. El agrupamiento jerárquico hace visible que el número de grupos es una altura de corte. En vez de fijar k, une los dos puntos más cercanos, luego los dos grupos más cercanos, y así hasta que todo es un solo grupo; el resultado es un árbol, el dendrograma, y cortar el árbol a distintas alturas da distintos números de grupos. Mirar el dendrograma del corpus propio enseña más que cualquier criterio numérico: se ve si hay alturas en que el árbol se parte con claridad o si las ramas se separan de forma continua, sin ningún corte que se imponga.

3. Los criterios para elegir k son criterios del método, no de la pregunta. El coeficiente de silueta (Rousseeuw, 1987) mide cuánto más cerca está cada punto de su grupo que del grupo vecino; el método del codo mira dónde deja de bajar la inercia. Ambos sirven para descartar valores absurdos de k y ninguno decide entre un k de cuatro y uno de cinco cuando los dos son razonables. Grimmer, Roberts y Stewart (2022, cap. 12) lo dicen sin rodeos: el agrupamiento es una herramienta de descubrimiento, y la elección final la hace quien va a usar los grupos, con la pregunta en mente.

| Criterio del método | Criterio de la pregunta |
|---|---|
| "La silueta es máxima en k = 2" | "Mi pregunta distingue cuatro tipos de discurso" |
| Mide la geometría de la partición | Mide si los grupos sirven para lo que se van a usar |
| Descarta valores absurdos de k | Elige entre los razonables |
| Lo calcula cualquiera | Lo sostiene quien conoce el corpus |
| *Necesario y no suficiente* | *Decide, y se escribe en la ficha con su razón* |

4. La prueba de estabilidad es lo que el curso añade al procedimiento habitual. Un grupo es un candidato a categoría si sobrevive a tres movimientos: cambiar la semilla, mover k uno arriba y uno abajo, y cambiar la representación, de embeddings a TF-IDF o entre dos modelos. Para medir la supervivencia se compara cada grupo con los grupos de la otra corrida por el índice de Jaccard<sup class="mark">b</sup>, y la partición entera por el índice de Rand ajustado (Hubert y Arabie, 1985). Un grupo con Jaccard alto en los tres movimientos describe algo del corpus; un grupo que se disuelve al cambiar la semilla describe la semilla.

<aside class="glosa"><span class="mark">b</span> Jaccard entre dos conjuntos: el tamaño de la intersección dividido por el tamaño de la unión. Vale 1 si son el mismo conjunto y 0 si no comparten nada. La mini app lo calcula para cada grupo contra la mejor coincidencia de la otra corrida.</aside>

5. Un grupo se convierte en categoría cuando alguien lo lee y se compromete con la lectura. Leer un grupo es mirar sus miembros, sus bordes y sus miembros mal ubicados, y proponer un nombre que los explique; ese nombre es una hipótesis. Timmermans y Tavory (2012) describen el análisis cualitativo como abducción: lo sorprendente exige una explicación, y la explicación la propone quien tiene trasfondo para sorprenderse. Un grupo estable es un hecho sorprendente solo para quien esperaba otra cosa. Sin esa expectativa, todos los grupos son igual de interesantes, es decir, ninguno lo es. La ficha de patrón de la plantilla pide, por eso, qué esperaba el estudiante antes de agrupar.

6. El producto de la semana es la representación y el agrupamiento del corpus propio con prueba de estabilidad. No se evalúa que los grupos sean "correctos", porque no hay con qué compararlos. Se evalúa que la representación esté justificada, que los grupos presentados como categorías hayan sobrevivido a los tres movimientos, que los que no sobrevivieron estén reportados y no escondidos, y que la lectura de cada categoría diga qué miembros la contradicen. Un informe que presenta cinco grupos limpios sin mencionar la semilla ni k es, en los términos de [*Validación del razonamiento con IA en ciencias sociales*](../../curso-1-tres-inferencias/README.md), un infortunio. Allí se sostuvo que el error característico del modelo no es una alucinación sino un infortunio de autoridad epistémica: un acto que tiene la forma de un hallazgo sin las condiciones que lo sostienen ni alguien que responda por él.

<figure class="wide">
  <svg viewBox="0 0 680 260" style="width:100%;max-width:42rem;height:auto;display:block" role="img" aria-label="Los mismos veinte puntos agrupados dos veces: a la izquierda con k igual a 3, a la derecha con k igual a 4. Dos de los grupos coinciden en ambos; el tercero de la izquierda se parte en dos a la derecha. Un rótulo marca los grupos que sobreviven y el que no.">
    <style>.m3{font-family:var(--mono);font-size:10.5px;letter-spacing:.06em;fill:var(--muted)} .mk{font-family:var(--mono);font-size:10.5px;letter-spacing:.06em;fill:var(--c-inv)} .mf3{font-family:var(--mono);font-size:10.5px;letter-spacing:.06em;fill:var(--c-fil)} .bx{fill:var(--surface);stroke:var(--rule);stroke-width:1.2} .A{fill:var(--c-app)} .B{fill:var(--c-doc)} .C{fill:var(--c-blog)} .D{fill:var(--c-fil)}</style>
    <rect x="10" y="26" width="320" height="200" rx="3" class="bx"/>
    <text x="20" y="18" class="m3">k = 3 · semilla 1</text>
    <rect x="350" y="26" width="320" height="200" rx="3" class="bx"/>
    <text x="360" y="18" class="m3">k = 4 · semilla 1</text>
    <g>
      <circle cx="60" cy="70" r="5" class="A"/><circle cx="80" cy="90" r="5" class="A"/><circle cx="50" cy="105" r="5" class="A"/><circle cx="95" cy="65" r="5" class="A"/><circle cx="72" cy="120" r="5" class="A"/><circle cx="105" cy="100" r="5" class="A"/>
      <circle cx="250" cy="70" r="5" class="B"/><circle cx="275" cy="85" r="5" class="B"/><circle cx="240" cy="100" r="5" class="B"/><circle cx="290" cy="60" r="5" class="B"/><circle cx="265" cy="115" r="5" class="B"/>
      <circle cx="120" cy="180" r="5" class="C"/><circle cx="145" cy="195" r="5" class="C"/><circle cx="110" cy="205" r="5" class="C"/><circle cx="160" cy="170" r="5" class="C"/><circle cx="200" cy="185" r="5" class="C"/><circle cx="225" cy="200" r="5" class="C"/><circle cx="215" cy="165" r="5" class="C"/><circle cx="240" cy="180" r="5" class="C"/><circle cx="180" cy="205" r="5" class="C"/>
    </g>
    <g transform="translate(340 0)">
      <circle cx="60" cy="70" r="5" class="A"/><circle cx="80" cy="90" r="5" class="A"/><circle cx="50" cy="105" r="5" class="A"/><circle cx="95" cy="65" r="5" class="A"/><circle cx="72" cy="120" r="5" class="A"/><circle cx="105" cy="100" r="5" class="A"/>
      <circle cx="250" cy="70" r="5" class="B"/><circle cx="275" cy="85" r="5" class="B"/><circle cx="240" cy="100" r="5" class="B"/><circle cx="290" cy="60" r="5" class="B"/><circle cx="265" cy="115" r="5" class="B"/>
      <circle cx="120" cy="180" r="5" class="C"/><circle cx="145" cy="195" r="5" class="C"/><circle cx="110" cy="205" r="5" class="C"/><circle cx="160" cy="170" r="5" class="C"/>
      <circle cx="200" cy="185" r="5" class="D"/><circle cx="225" cy="200" r="5" class="D"/><circle cx="215" cy="165" r="5" class="D"/><circle cx="240" cy="180" r="5" class="D"/><circle cx="180" cy="205" r="5" class="D"/>
    </g>
    <text x="20" y="246" class="mk">AZUL Y OCRE SOBREVIVEN: JACCARD 1,0 ENTRE LAS DOS CORRIDAS</text>
    <text x="360" y="246" class="mf3">EL GRUPO INFERIOR SE PARTE: ¿DOS CATEGORÍAS O UN CORTE DE K?</text>
  </svg>
  <figcaption><b>Figura 3.</b> El mismo dato con dos k. Dos grupos son los mismos en ambas corridas; el tercero se divide al pasar de tres a cuatro. La división no es un hallazgo ni un error: es una pregunta que solo la lectura de sus miembros puede responder.</figcaption>
</figure>

<iframe class="app" src="apps/embeddings-y-k.html" title="Nube de puntos de embeddings con agrupamiento k-means y deslizador de k" loading="lazy"></iframe>

## IA y exigencia

Se le pide a un modelo de lenguaje que proponga un nombre para cada grupo a partir de diez miembros, y que escriba el código de la prueba de estabilidad a partir del cuaderno. El estudiante debe poder defender sin el modelo por qué eligió el k que presenta, qué grupos sobrevivieron a los tres movimientos y cuáles no, y por qué adopta o rechaza cada nombre propuesto, citando miembros del grupo que el nombre explica y miembros que no. Un nombre adoptado sin leer los miembros es una aserción sin fundamento, y el registro de frontera debe decirlo.

## Lecturas

**Central**

- Grimmer, J., Roberts, M. E. y Stewart, B. M. (2022). *Text as Data: A New Framework for Machine Learning and the Social Sciences*. Princeton University Press. Cap. 12, sobre agrupamiento, y cap. 10, sobre principios del descubrimiento.

**Complementaria**

- Rousseeuw, P. J. (1987). "Silhouettes: A Graphical Aid to the Interpretation and Validation of Cluster Analysis". *Journal of Computational and Applied Mathematics* 20, 53-65. https://doi.org/10.1016/0377-0427(87)90125-7
- Hubert, L. y Arabie, P. (1985). "Comparing Partitions". *Journal of Classification* 2, 193-218. https://doi.org/10.1007/BF01908075
- Timmermans, S. y Tavory, I. (2012). "Theory Construction in Qualitative Research: From Grounded Theory to Abductive Analysis". *Sociological Theory* 30(3), 167-186. https://doi.org/10.1177/0735275112457914
- Peirce, C. S. (1903). "El pragmatismo como lógica de la abducción". Traducción del Grupo de Estudios Peirceanos, Universidad de Navarra. https://www.unav.es/gep/PragmatismoLogicaAbduccion.html

## Guía de lectura

- Grimmer, Roberts y Stewart insisten en que los métodos de descubrimiento no producen conclusiones sino conceptos que después hay que medir y validar por separado. *¿En qué momento de su proyecto un grupo dejaría de ser un descubrimiento y pasaría a ser una medida? ¿Qué tendría que haber hecho entre los dos momentos?*
- Rousseeuw propone la silueta como ayuda gráfica, no como veredicto. *Si la silueta prefiere k igual a dos y su lectura prefiere k igual a cinco, ¿quién tiene razón, y qué significa aquí "tener razón"?*
- Timmermans y Tavory sostienen que el investigador necesita trasfondo teórico para que algo lo sorprenda. *¿Qué esperaba encontrar en su corpus antes de agrupar? Escríbalo antes de correr el algoritmo; después ya no podrá.*

## Taller de la segunda hora

Sobre los vectores del corpus propio, con el bloque de la semana 3 del cuaderno de apoyo o con la mini app si el corpus es pequeño:

1. Escriba en una línea qué grupos espera encontrar. Guárdela.
2. Corra k-means para k de 2 a 10 con cinco semillas cada uno. Grafique la silueta y la inercia por k. Dibuje el dendrograma del agrupamiento jerárquico.
3. Elija dos valores de k razonables. Para cada grupo de cada uno, calcule el Jaccard contra la mejor coincidencia con las otras semillas, con k más uno y k menos uno, y con la otra representación.
4. Llene la tabla de la ficha de patrón:

| Grupo | Tamaño | Jaccard semilla | Jaccard k±1 | Jaccard otra representación | Miembros que lo contradicen | Nombre propuesto | ¿Categoría o corte? |
|---|---|---|---|---|---|---|---|

5. Compare lo que esperaba con lo que sobrevivió. La diferencia es el hecho sorprendente de la semana 8.

## Guion de la sesión

| Minuto | Momento | Docente | Estudiante | Material |
|---|---|---|---|---|
| 0 a 10 | Apertura | Muestra dos informes con distinto número de grupos sobre el mismo corpus y pregunta cuál está bien | Escribe su expectativa de grupos antes de agrupar | Tablero |
| 10 a 30 | Lectura | Discute el capítulo de agrupamiento y la idea de descubrimiento frente a medida | Responde la guía | Lectura central |
| 30 a 55 | Mecanismo | Mueve k y la semilla en la mini app; lee la tabla de supervivencia; muestra un grupo que se disuelve | Predice qué grupo sobrevivirá antes de mover k | App de embeddings |
| 55 a 65 | Pausa | | | |
| 65 a 105 | Taller | Acompaña la corrida con varias semillas y la prueba de estabilidad sobre corpus propios | Llena la tabla de la ficha de patrón | Cuaderno, semana 3 |
| 105 a 120 | Cierre | Pide a tres estudiantes el grupo que más le sorprendió y por qué | Nombra un grupo estable y uno que no lo fue | Bitácora |

Notas para el docente. Lo que suele fallar: el estudiante corre k-means una vez, obtiene grupos bonitos y no quiere volver a correrlo; exigir las cinco semillas antes de cualquier lectura. Segundo fallo: la prueba de estabilidad sale mal en todos los grupos y el estudiante concluye que el corpus "no tiene estructura"; discutir que eso también es un resultado, y uno que se puede reportar y que a menudo señala un problema de representación. Tercero: los nombres propuestos por el modelo de lenguaje son tan plausibles que nadie lee los miembros; pedir, para cada nombre, los tres miembros que peor encajan.

## Entrega

Representación y agrupamiento del corpus propio con prueba de estabilidad, sobre la plantilla `plantillas/ficha-de-patron.md`, con el código o los pasos usados en anexo. Se evalúa la justificación de la representación, la prueba de estabilidad completa, el reporte honesto de los grupos que no sobrevivieron y la lectura de cada categoría con sus contraejemplos. Rúbrica en `evaluacion.md`.

## Para la próxima semana

Leer Newman (2018), capítulos 6 y 7, por lo que miden las medidas y no por sus fórmulas, y Barabási (2016), capítulo 2, de acceso abierto. Llegar con una lista de pares del corpus propio que puedan ser aristas: códigos que coinciden en un documento, actores que aparecen en la misma noticia, etiquetas que acompañan la misma imagen. Quien hizo [*Codificación cualitativa con IA en ciencias sociales*](../../curso-4-codificacion-asistida/README.md) trae su libro de códigos: la lista de códigos del propio corpus, cada uno con su definición, sus fragmentos de anclaje y su origen, modelo o investigador, que allí se construye con ayuda de un modelo de lenguaje y se concluye que es una aserción del investigador y no un output.
