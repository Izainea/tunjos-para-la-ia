# Semana 8. Del patrón a la hipótesis

## Pregunta de la semana

Después de agrupar, conectar, seguir en el tiempo y mostrar, ¿qué patrón del corpus propio merece que alguien se comprometa a perseguirlo, y quién es ese alguien?

## Por qué esta semana

<p class="lede">El curso termina donde empieza la investigación. Siete semanas de instrumentos han producido una colección de patrones con sus parámetros y sus pruebas de estabilidad, y ninguno de esos instrumentos ha dicho cuál de los patrones importa. No podía decirlo. Un grupo estable, un puente que sobrevive a tres umbrales, una ruptura que no se mueve con la ventana, un tema que aparece en cuatro corridas: todos son hechos del corpus en el sentido más modesto, regularidades que un procedimiento señala. Para que uno de ellos se convierta en hipótesis hace falta que sorprenda a alguien que esperaba otra cosa, y que ese alguien formule lo que lo explicaría, diga cómo lo probaría y se comprometa a pagar el costo. Esa es la abducción de Peirce, y es el único acto del curso que la máquina no puede hacer en lugar del estudiante, no porque le falte algo que la ingeniería podría añadirle, sino porque el acto consiste en responder ante otros. La sesión termina con presentaciones ante pares porque esa es la forma práctica de responder.</p>

La semana supone el tablero de la semana 7 y las fichas de patrón y lecturas de grafo de las entregas anteriores.

## Contenido de la sesión

1. La recapitulación cabe en una tabla: cuatro instrumentos, cuatro parámetros, una prueba y una pregunta. Embeddings y agrupamiento tienen el modelo, la semilla y k; las redes tienen la unidad y el umbral; las series tienen el periodo y la ventana; los temas tienen K y la semilla. A todos se les aplicó la misma prueba, mover el parámetro y ver si el patrón sobrevive, y a todos se les hizo la misma pregunta, qué afirma la vista y qué propone quien la lee. Lo que el estudiante entrega no es una lista de hallazgos sino una lista de candidatos con su historial de pruebas.

| Instrumento | Parámetro que cambia el patrón | Prueba de estabilidad | Lo que el instrumento no hace |
|---|---|---|---|
| Embeddings y agrupamiento | Modelo, semilla, k | Jaccard contra semillas, k±1, otra representación | Decidir cuántos grupos hay ni qué significan |
| Redes de coocurrencia | Unidad, umbral, algoritmo de comunidades | Tabla de tres umbrales, dos algoritmos | Decir qué relación afirma una arista |
| Series temporales | Periodo, normalización, ventana | Fecha de ruptura con tres ventanas y dos métodos | Configurar una trama |
| Modelado de temas | K, semilla, representación | Temas comunes a cuatro corridas | Nombrar un tema |
| *Consecuencia* | *Todo patrón se entrega con su parámetro* | *Sin prueba no hay candidato* | *La lectura es siempre del investigador* |

2. Un patrón sorprende contra un trasfondo, y sin trasfondo no hay hipótesis. Peirce (1903) formula la abducción así: se observa un hecho sorprendente C; si A fuera verdad, C sería natural; luego hay razón para sospechar A. La sorpresa no está en C sino en la distancia entre C y lo que se esperaba, y por eso la ficha de patrón pidió desde la semana 3 que el estudiante escribiera su expectativa antes de correr el algoritmo. Timmermans y Tavory (2012) añaden que el trasfondo es teórico: quien no conoce las teorías de su campo no puede sorprenderse de lo que las contradice. Un modelo de lenguaje puede proponer hipótesis para cualquier patrón con igual fluidez, y esa igualdad es el síntoma: nada le sorprende más que otra cosa.

3. La ficha de hipótesis sobre un patrón propio es la ficha de patrón con cuatro casillas más. A lo que ya tenía, patrón, parámetros, prueba de estabilidad y lectura, se añaden el trasfondo desde el que sorprende, la hipótesis que lo haría natural, la prueba que la confirmaría o la refutaría, y el costo de hacer esa prueba junto con lo que rendiría si acierta. Las cuatro casillas son los criterios de Peirce para elegir qué hipótesis perseguir<sup class="mark">a</sup>, que [*Las tres inferencias*](../../curso-1-tres-inferencias/README.md) presentó como filtro para decidir qué hipótesis pedidas a un modelo vale la pena perseguir, por sorpresa, plausibilidad, verificabilidad y economía; aquí se aplican a un hecho que salió de una máquina, y eso no cambia nada del filtro.

<aside class="glosa"><span class="mark">a</span> Peirce llamó economía de la investigación a la regla para elegir entre hipótesis: preferir la que es barata de probar, la que rinde más si acierta y la que no cierra otras vías. Es una regla de gestión del esfuerzo, no de verdad, y por eso supone a alguien que va a hacer el esfuerzo.</aside>

4. Los artefactos tienen una tipología, y nombrarlos ayuda a no confundirlos con hechos. Hay artefactos del método, un grupo que depende de k, una comunidad que depende del umbral, una ruptura que depende de la ventana; artefactos de la representación, un parecido que la bolsa de palabras ve y el embedding no, o al revés; artefactos del corpus, una emergencia que coincide con un cambio en la recolección; y artefactos de la vista, una tendencia que el eje recortado produce. La ficha pide, para el patrón elegido, decir de cuál de los cuatro tipos se descartó que fuera y con qué prueba. Un patrón que no se ha podido descartar como artefacto de algún tipo no es todavía un hecho sorprendente: es una pregunta sobre el método.

5. El registro de frontera computacional separa lo que calculó la máquina de lo que leyó el investigador, paso a paso. Lo que calculó la máquina es reproducible<sup class="mark">b</sup>: con los mismos datos, el mismo código y la misma semilla, cualquiera obtiene el mismo patrón, y ese es el segundo de los tres sentidos de validación que distingue [*Las tres inferencias*, semana 1](../../curso-1-tres-inferencias/programa/semana-01.md): un resultado se valida porque es correcto, porque el proceso que lo produjo puede exhibirse, o porque alguien responde por él.

<aside class="glosa"><span class="mark">b</span> Reproducible exige fijar la semilla de todo lo aleatorio, guardar la versión de cada biblioteca y del modelo de embeddings, y conservar el corpus en el estado en que se calculó. El cuaderno de apoyo trae un bloque que registra las tres cosas en un archivo junto a cada resultado.</aside> Lo que leyó el investigador es imputable: lleva su nombre y responde ante quien lo discuta, y ese es el tercer sentido. El registro tiene una fila por paso y, en cada fila, quién hizo qué y quién responde. Las filas difíciles, donde el modelo de lenguaje propuso un nombre y el estudiante lo adoptó sin saber bien por qué, son las que más valen, siempre que estén escritas.

6. Las presentaciones son la forma práctica de la imputación. Cada estudiante presenta en ocho minutos el tablero, el patrón elegido, la hipótesis y la frontera, y recibe dos preguntas de pares. La pregunta obligatoria es la misma para todos: "¿qué pasaría con tu patrón si movieras el parámetro un poco más?". Si la respuesta es "ya lo probé y esto es lo que pasa", el curso cumplió su propósito. Si la respuesta es "no sé", también, siempre que la frase siguiente sea "y lo voy a probar antes de escribirlo".

<figure class="wide">
  <svg viewBox="0 0 680 300" style="width:100%;max-width:42rem;height:auto;display:block" role="img" aria-label="Arriba de una línea punteada roja, la zona de la máquina: datos entran a los instrumentos (embeddings, grafo, serie, temas), que producen un patrón con sus parámetros, y la prueba de estabilidad lo marca como candidato o como artefacto. Debajo de la línea, la zona del investigador: el candidato se encuentra con un trasfondo de expectativas, produce sorpresa, y de la sorpresa sale una hipótesis con su prueba y su costo. Una flecha vuelve del investigador a los instrumentos con la nota de que la prueba de la hipótesis puede exigir otro cálculo.">
    <style>.t8{font-family:var(--text);font-size:12.5px;fill:var(--ink)} .s8{font-family:var(--text);font-size:11px;fill:var(--muted)} .m8{font-family:var(--mono);font-size:10.5px;letter-spacing:.06em;fill:var(--muted)} .mf8{font-family:var(--mono);font-size:10.5px;letter-spacing:.06em;fill:var(--c-fil)} .mk8{font-family:var(--mono);font-size:10.5px;letter-spacing:.06em;fill:var(--c-inv)} .bx{fill:var(--surface);stroke:var(--rule);stroke-width:1.2} .ar{stroke:var(--muted);stroke-width:1.3;fill:none} .ah{fill:var(--muted)} .fr{stroke:var(--c-fil);stroke-width:1.6;stroke-dasharray:6 5;fill:none}</style>
    <defs><marker id="s8-ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 1L9 5L0 9z" class="ah"/></marker></defs>
    <text x="12" y="16" class="m8">MÁQUINA · CALCULA · REPRODUCIBLE</text>
    <rect x="12" y="26" width="150" height="52" rx="3" class="bx"/><text x="22" y="46" class="t8">Corpus</text><text x="22" y="64" class="s8">vectores, códigos, fechas</text>
    <path class="ar" d="M162 52 L196 52" marker-end="url(#s8-ah)"/>
    <rect x="200" y="26" width="200" height="52" rx="3" class="bx"/><text x="210" y="46" class="t8">Instrumento</text><text x="210" y="64" class="s8">k · umbral · ventana · K · semilla</text>
    <path class="ar" d="M400 52 L434 52" marker-end="url(#s8-ah)"/>
    <rect x="438" y="26" width="230" height="52" rx="3" class="bx"/><text x="448" y="46" class="t8">Patrón con sus parámetros</text><text x="448" y="64" class="s8">grupo, puente, ruptura, tema</text>
    <path class="ar" d="M553 78 L553 98" marker-end="url(#s8-ah)"/>
    <rect x="438" y="102" width="230" height="40" rx="3" class="bx"/><text x="448" y="120" class="t8">Prueba de estabilidad</text><text x="448" y="136" class="s8">¿sobrevive a mover el parámetro?</text>
    <text x="300" y="126" class="mf8">NO → ARTEFACTO DEL MÉTODO</text>
    <text x="300" y="142" class="mk8">SÍ → CANDIDATO</text>
    <path class="fr" d="M12 160 L668 160"/>
    <text x="668" y="154" text-anchor="end" class="mf8">FRONTERA</text>
    <text x="12" y="182" class="m8">INVESTIGADOR · LEE · IMPUTABLE</text>
    <path class="ar" d="M553 142 L553 192" marker-end="url(#s8-ah)"/>
    <rect x="438" y="196" width="230" height="40" rx="3" class="bx"/><text x="448" y="214" class="t8">Hecho sorprendente</text><text x="448" y="230" class="s8">sorprende contra lo que yo esperaba</text>
    <rect x="200" y="196" width="200" height="40" rx="3" class="bx"/><text x="210" y="214" class="t8">Trasfondo</text><text x="210" y="230" class="s8">teoría, campo, lo escrito antes</text>
    <path class="ar" d="M400 216 L434 216" marker-end="url(#s8-ah)"/>
    <path class="ar" d="M553 236 L553 254" marker-end="url(#s8-ah)"/>
    <rect x="200" y="256" width="468" height="36" rx="3" class="bx"/><text x="210" y="279" class="t8">Hipótesis: si A fuera verdad, el patrón sería natural · prueba · costo · quien responde: yo</text>
    <path class="ar" d="M196 274 C 120 274 100 110 196 60" marker-end="url(#s8-ah)"/>
    <text x="20" y="250" class="s8">la prueba de la hipótesis</text><text x="20" y="266" class="s8">suele exigir otro cálculo</text>
  </svg>
  <figcaption><b>Figura 8.</b> El patrón como abducción con la frontera marcada. Arriba de la línea, lo que se calcula y se puede reproducir; debajo, lo que se lee y se imputa. El candidato cruza la frontera solo cuando alguien, con un trasfondo, se sorprende y formula qué lo explicaría.</figcaption>
</figure>

## IA y exigencia

Se le pide a un modelo de lenguaje que proponga tres hipótesis para el patrón elegido y una prueba para cada una, y que revise el registro de frontera buscando filas incompletas. El estudiante debe poder defender sin el modelo desde qué trasfondo le sorprende el patrón, por qué elige la hipótesis que elige aunque la haya escrito el modelo, qué prueba haría y qué costaría, y de qué tipos de artefacto descartó el patrón. En la presentación no se puede decir "el modelo sugirió"; se dice "propongo", y después, si hace falta, "la formulación salió de un modelo y la adopté por estas razones".

## Lecturas

**Central**

- Peirce, C. S. (1903). "El pragmatismo como lógica de la abducción" (séptima conferencia de Harvard). Traducción del Grupo de Estudios Peirceanos, Universidad de Navarra. https://www.unav.es/gep/PragmatismoLogicaAbduccion.html
- Timmermans, S. y Tavory, I. (2012). "Theory Construction in Qualitative Research: From Grounded Theory to Abductive Analysis". *Sociological Theory* 30(3), 167-186. https://doi.org/10.1177/0735275112457914

**Complementaria**

- Grimmer, J., Roberts, M. E. y Stewart, B. M. (2022). *Text as Data*. Princeton University Press. Cap. 10, sobre principios del descubrimiento, y el capítulo final sobre inferencia.
- Zainea, C. I. (2026). "La prótesis hermenéutica". https://izainea.github.io/blog/protesis-hermeneutica/
- Zainea, C. I. (2026). *Agencia sin imputación. Hermenéutica, pragmática y la validación epistémica del discurso artificial*. https://izainea.github.io/escritos/agencia-sin-imputacion.pdf

## Guía de lectura

- Peirce dice que la abducción "sugiere meramente que algo puede ser" y que su justificación es que sin ella no hay investigación. *Si un instrumento sugiere miles de patrones, ¿qué le falta a cada sugerencia para ser una abducción en el sentido de Peirce?*
- Timmermans y Tavory piden familiaridad con muchas teorías para poder sorprenderse. *Nombre dos teorías de su campo que su patrón elegido confirma o contradice. Si no puede nombrar ninguna, ¿de qué se sorprende?*
- En "La prótesis hermenéutica" la máquina configura y el investigador valida, con la frontera marcada. *Dibuje el flujo de su propio proyecto después de este curso. ¿Dónde está la frontera y por qué ahí?*

## Taller sobre presentaciones y cierre

Formato de presentación, ocho minutos y dos preguntas de pares:

1. El corpus y la pregunta en una frase.
2. El tablero: cinco paneles, cada uno con lo que afirma.
3. El patrón elegido, con su parámetro y su prueba de estabilidad.
4. La sorpresa: qué esperaba y qué salió.
5. La hipótesis, su prueba y su costo.
6. Un caso del registro de frontera en que rechazó una propuesta del modelo de lenguaje, y uno en que la adoptó.
7. Qué cambia de su proyecto después del curso.

La pregunta obligatoria de los pares: "¿qué pasaría con tu patrón si movieras el parámetro un poco más?".

## Guion de la sesión

| Minuto | Momento | Docente | Estudiante | Material |
|---|---|---|---|---|
| 0 a 10 | Apertura | Presenta la tabla de recapitulación y la figura 8; recuerda la pregunta obligatoria | Revisa su ficha de hipótesis | Tablero |
| 10 a 100 | Presentaciones | Modera, cronometra, anota en el tablero qué patrones fueron descartados como artefactos y de qué tipo | Presenta en ocho minutos y hace preguntas a dos pares | Tableros de los estudiantes |
| 100 a 115 | Cierre | Lee la lista de artefactos descartados y la de hipótesis que quedan en pie; conecta con [*Validación e interpretación*](../../curso-6-validacion-interpretacion/README.md), donde esos candidatos se validan y se escriben | Anota una hipótesis ajena que le interesó | Tablero |
| 115 a 120 | Entrega | Recibe los productos finales | Entrega | Plantillas |

Con más de doce estudiantes, las presentaciones se hacen en dos grupos paralelos con un relator por grupo, y la última media hora se dedica a que cada relator presente las hipótesis que quedaron en pie en su grupo.

Notas para el docente. Lo que suele fallar: las presentaciones se vuelven demostraciones del tablero y la hipótesis llega en el último minuto; pedir que el patrón y la sorpresa se digan en los primeros tres. Segundo fallo: la pregunta obligatoria recibe una respuesta de cortesía ("probablemente cambiaría un poco"); el docente repregunta con el parámetro concreto. Tercero: algún estudiante llega sin patrón que lo sorprenda y lo vive como fracaso; un tablero honesto que muestre que ningún patrón sobrevivió a las pruebas es un resultado que vale, y la hipótesis en ese caso es sobre la representación o sobre el corpus.

## Entrega final

Tablero analítico con ficha de hipótesis y registro de frontera computacional, sobre las plantillas `plantillas/ficha-de-patron.md` y `plantillas/registro-de-frontera-computacional.md`. Se entrega con la bitácora completa y los dos productos anteriores como anexos. Se evalúa que cada panel del tablero declare lo que afirma y sus parámetros, que la hipótesis tenga trasfondo, prueba y costo, que los artefactos descartados estén nombrados por tipo, y que el registro de frontera distinga en cada paso lo que calculó la máquina de lo que leyó el investigador. Rúbrica en `evaluacion.md`.

## Después del curso

La ruta Computacional del programa termina aquí. Quien siga a [*Validación e interpretación*](../../curso-6-validacion-interpretacion/README.md) lleva sus candidatos con su historial de pruebas: allí se distinguen tres sentidos de validar, comprobar la corrección del resultado, justificar el proceso y responder por lo afirmado, se releen los criterios de rigor de la tradición cualitativa para gobernar lo que un modelo produjo, y los hallazgos se escriben como aserciones propias con una declaración de uso de IA. Quien siga a [*Ética, exterioridad y gobernanza*](../../curso-7-etica-gobernanza/README.md) lleva la pregunta que esta semana dejó abierta: qué pasa con la precomprensión ajena de los instrumentos cuando el corpus es sensible o cuando quien lee no es de la comunidad que produjo el material. Allí esa pregunta se trata como un problema de exterioridad, el de un modelo entrenado en otra parte que impone sus categorías a un archivo situado, junto con los derechos sobre el material y la gobernanza de quién responde por cada aserción, y el producto es un protocolo de gobernanza epistémica para el propio proyecto.
