# Semana 7. Lectura asistida y registro de frontera

## Pregunta de la semana

Si un modelo de lenguaje resume y etiqueta mil documentos en una tarde, ¿qué tiene que hacer el investigador para poder firmar una sola de esas etiquetas?

## Por qué esta semana

<p class="lede">Hasta aquí la máquina ha contado, buscado y comparado. Esta semana lee, o hace algo que tiene la forma de leer: recibe una unidad del corpus y devuelve un resumen, una etiqueta temática, una lista de entidades, una clasificación. Lo hace rápido, con consistencia y con la apariencia de una lectura fundamentada. <a href="../../curso-1-tres-inferencias/README.md"><em>Las tres inferencias</em></a>, el curso de fundamentos del programa, dio nombre a esa apariencia a partir de Austin: un infortunio de autoridad epistémica, un acto con forma de aserción fundamentada cuyas condiciones de validez no se satisfacen desde adentro, porque nadie detrás del output puede responder por él. Allí se concluyó que ese infortunio, y no una alucinación, es el error característico del modelo. Esta semana no renuncia a la lectura asistida, porque sobre un corpus grande es la única forma de llegar a todo. Lo que enseña es el procedimiento que la hace gobernable: una instrucción escrita y versionada, una muestra que el investigador lee a ciegas, una comparación que mide el desacuerdo, una decisión sobre qué se acepta, y un registro de frontera que deja todo eso escrito. Es la semana en que el método del programa se aplica al corpus pieza por pieza.</p>

## Contenido de la sesión

1. Lo que el modelo puede hacer con una unidad del corpus se reduce a cuatro operaciones con utilidad distinta. Resumir: devolver un texto más corto que conserva algo del original, útil para orientarse y peligroso para citar, porque el resumen no es la fuente. Etiquetar: asignar una o varias categorías de una lista que el investigador escribió. Extraer: listar nombres de lugares, instituciones, fechas o actores que el texto menciona. Clasificar: decidir si la unidad cumple un criterio binario. Las cuatro producen salidas con la forma de una lectura; ninguna produce una lectura de la que el modelo responda.<sup class="mark">a</sup>

<aside class="glosa"><span class="mark">a</span> Grimmer y Stewart (2013) formularon para el análisis automático de textos políticos cuatro principios que el curso adopta: todos los modelos cuantitativos del lenguaje están equivocados, pero algunos son útiles; los métodos aumentan la lectura, no la reemplazan; no hay un método mejor para todo; y hay que validar, validar y validar.</aside>

2. La instrucción que se le da al modelo es un criterio escrito, del mismo tipo que la función de inclusión de la semana 2. Dice qué categorías existen, qué significa cada una, qué hacer en caso de duda, y en qué formato responder. Se guarda en un archivo con número de versión y fecha, y cada salida del modelo registra con qué versión fue producida. Cambiar una palabra de la instrucción cambia las etiquetas de todo el corpus; por eso la instrucción se trata como código y no como conversación. El cuaderno de apoyo muestra cómo enviarla a un modelo por programa y cómo guardar cada respuesta con su fecha, su versión y el identificador de la unidad.

3. La auditoría es el procedimiento que convierte la salida del modelo en algo de lo que el investigador puede responder. Se toma una muestra aleatoria del corpus, de treinta a cien unidades según el tamaño, y el investigador las etiqueta a ciegas, sin ver lo que dijo el modelo, con la misma instrucción. Luego se comparan. La proporción de acuerdo es la primera cifra; el coeficiente kappa de Cohen, que descuenta el acuerdo esperable por azar, es la segunda.<sup class="mark">b</sup> Ninguna de las dos dice si las etiquetas son correctas: dicen cuánto coinciden dos lectores, uno de los cuales no responde. Qué cifra es aceptable depende de para qué se usan las etiquetas, y esa decisión se escribe.

<aside class="glosa"><span class="mark">b</span> Kappa vale 1 cuando el acuerdo es total y 0 cuando es el que daría el azar. Las convenciones que lo califican como "moderado" o "sustancial" son eso, convenciones; en un corpus con categorías muy desbalanceadas kappa puede ser bajo con un acuerdo alto. El cuaderno de apoyo lo calcula con una función de diez líneas.</aside>

4. Los desacuerdos son el dato de la semana, no el residuo. Cada unidad en que el modelo y el investigador no coinciden se lee de nuevo y se clasifica según por qué: el modelo generalizó desde su entrenamiento algo que en este corpus significa otra cosa; forzó una categoría de la lista cuando ninguna aplicaba; ignoró un contexto local que el investigador conoce, como el nombre de una institución de la época; leyó literalmente una ironía o una fórmula de cortesía; o el investigador se equivocó, lo que también ocurre y también se anota. La tipología de desacuerdos dice más sobre el corpus que la tasa de acuerdo, y suele mandar a corregir la instrucción o la lista de categorías.

5. La decisión tiene tres salidas y el registro de frontera guarda cuál se tomó. Aceptar las etiquetas del modelo para el resto del corpus, con la tasa de acuerdo declarada y las categorías problemáticas marcadas. Corregir la instrucción y repetir la auditoría sobre una muestra nueva. O rechazar la lectura asistida para esta tarea, porque los desacuerdos tocan lo que la pregunta de investigación necesita. Las tres son decisiones legítimas; lo que no es legítimo es usar las etiquetas sin haber decidido. El registro de frontera del corpus, en `plantillas/registro-de-frontera-corpus.md`, tiene una fila por operación con la máquina, desde la propuesta de fuentes de la semana 1 hasta las etiquetas de hoy.

<figure class="wide">
<svg viewBox="0 0 680 300" style="width:100%;max-width:42rem;height:auto;display:block" role="img" aria-label="Flujo de la lectura asistida auditada: la instrucción versionada entra al modelo junto con todo el corpus; el modelo produce etiquetas para todas las unidades. Una muestra aleatoria va al investigador, que etiqueta a ciegas. Las dos etiquetas de la muestra se comparan: acuerdo y desacuerdos tipificados. De ahí sale la decisión: aceptar con tasa declarada, corregir la instrucción y repetir, o rechazar. Todo queda en el registro de frontera.">
<style>.w7k{font-family:var(--mono);font-size:10px;letter-spacing:.06em;fill:var(--muted)} .w7t{font-family:var(--text);font-size:12px;fill:var(--ink)} .w7s{font-family:var(--text);font-size:11px;fill:var(--muted)} .w7f{fill:var(--surface);stroke:var(--rule);stroke-width:1} .w7a{fill:none;stroke:var(--muted);stroke-width:1.3} .w7fr{fill:none;stroke:var(--c-fil);stroke-width:1.6;stroke-dasharray:6 5} .w7r{font-family:var(--mono);font-size:10px;letter-spacing:.06em;fill:var(--c-fil)} .w7g{fill:var(--surface);stroke:var(--c-inv);stroke-width:1.4}</style>
<rect x="16" y="24" width="130" height="50" rx="3" class="w7f"/><text x="24" y="42" class="w7k">INSTRUCCIÓN v1.2</text><text x="24" y="62" class="w7s">categorías, dudas, formato</text>
<rect x="16" y="90" width="130" height="50" rx="3" class="w7f"/><text x="24" y="108" class="w7k">CORPUS</text><text x="24" y="128" class="w7s">todas las unidades</text>
<path class="w7a" d="M146 49 L190 49 L190 82"/><path class="w7a" d="M146 115 L190 115 L190 96"/><path class="w7a" d="M190 90 L214 90"/><path class="w7a" d="M208 85 L215 90 L208 95"/>
<rect x="216" y="60" width="110" height="60" rx="3" class="w7f"/><text x="224" y="78" class="w7k">MODELO</text><text x="224" y="98" class="w7t">etiqueta todo</text><text x="224" y="112" class="w7s">rápido, consistente</text>
<path class="w7a" d="M326 90 L360 90"/><path class="w7a" d="M354 85 L361 90 L354 95"/>
<rect x="362" y="60" width="100" height="60" rx="3" class="w7f"/><text x="370" y="78" class="w7k">ETIQUETAS</text><text x="370" y="98" class="w7s">con versión,</text><text x="370" y="112" class="w7s">fecha e id</text>
<path class="w7fr" d="M16 160 L664 160"/><text x="664" y="154" text-anchor="end" class="w7r">FRONTERA</text>
<path class="w7a" d="M81 140 L81 200"/><path class="w7a" d="M76 194 L81 201 L86 194"/>
<rect x="16" y="202" width="130" height="50" rx="3" class="w7g"/><text x="24" y="220" class="w7k">MUESTRA ALEATORIA</text><text x="24" y="240" class="w7s">30 a 100 unidades</text>
<path class="w7a" d="M146 227 L180 227"/><path class="w7a" d="M174 222 L181 227 L174 232"/>
<rect x="182" y="202" width="120" height="50" rx="3" class="w7g"/><text x="190" y="220" class="w7k">INVESTIGADOR</text><text x="190" y="240" class="w7s">etiqueta a ciegas</text>
<path class="w7a" d="M302 227 L336 227"/><path class="w7a" d="M330 222 L337 227 L330 232"/>
<path class="w7a" d="M412 120 L412 200"/><path class="w7a" d="M407 194 L412 201 L417 194"/>
<rect x="338" y="202" width="150" height="50" rx="3" class="w7g"/><text x="346" y="220" class="w7k">COMPARACIÓN</text><text x="346" y="240" class="w7s">acuerdo · kappa · tipos de desacuerdo</text>
<path class="w7a" d="M488 227 L522 227"/><path class="w7a" d="M516 222 L523 227 L516 232"/>
<rect x="524" y="186" width="140" height="82" rx="3" class="w7g"/><text x="532" y="204" class="w7k">DECISIÓN</text><text x="532" y="222" class="w7t">aceptar con tasa</text><text x="532" y="238" class="w7t">corregir y repetir</text><text x="532" y="254" class="w7t">rechazar</text>
<path class="w7a" d="M594 186 L594 90 L462 90"/><path class="w7a" d="M468 85 L461 90 L468 95"/>
<text x="500" y="40" class="w7s">corregir la instrucción manda</text><text x="500" y="54" class="w7s">de vuelta arriba de la frontera</text>
<text x="16" y="288" class="w7s">Debajo de la frontera todo lo hace alguien que responde. Las tres decisiones van al registro de frontera.</text>
</svg>
<figcaption><b>Figura 7.</b> El registro de frontera en la lectura asistida. Lo que hay que ver es que el modelo etiqueta arriba de la frontera y la muestra, la comparación y la decisión ocurren debajo, donde alguien firma.</figcaption>
</figure>

6. Hay dos cosas que no se le piden al modelo sobre el corpus, y la razón es la misma en ambas. No se le pide que decida qué unidades entran al corpus, porque la inclusión es el criterio del protocolo y delegarla deja sin autor la frontera que el curso entero construye. Y no se le pide un texto que luego se cite como si fuera una fuente: un resumen del modelo puede orientar la lectura, pero la cita del informe sale de la unidad del corpus, con su identificador y su posición, nunca del resumen. Las dos prohibiciones son la forma práctica de la tesis con que concluye [*Las tres inferencias*](../../curso-1-tres-inferencias/README.md): la máquina configura, el investigador valida, y la validación no se delega, porque la inferencia que introduce hipótesis solo vale cuando alguien se compromete a responder por ella.

La diferencia que esta semana enseña se deja escribir en dos columnas.

| El modelo como lector | El modelo como etiquetador auxiliar |
|---|---|
| Sus etiquetas van al informe | Sus etiquetas van a una tabla que alguien audita |
| La instrucción se improvisa en cada conversación | La instrucción está en un archivo con versión y fecha |
| Se le pregunta si está seguro | Se le compara con una muestra etiquetada a ciegas |
| Un resumen suyo se cita | La cita sale de la unidad del corpus, con identificador y posición |
| *Nadie responde por la lectura* | *Responde quien decidió con la tasa de acuerdo en la mano* |

7. La práctica de la semana ejecuta todo esto sobre el corpus propio con una muestra de treinta unidades, en tres rondas: el modelo etiqueta, el estudiante etiqueta a ciegas, los dos resultados se comparan y se decide. La guía está en `practicas/practica-07-auditoria-lectura-asistida.md`. El resultado va al informe de la semana 8 como una sección propia: tasa de acuerdo, tipología de desacuerdos, decisión y lo que cambiaría de la instrucción.

## IA y exigencia

Esta semana el modelo hace la tarea entera, por diseño: etiqueta la muestra con la instrucción versionada del estudiante. Lo que se le exige al estudiante es haber etiquetado la misma muestra sin mirar, haber calculado el acuerdo, haber leído cada desacuerdo y haberlo tipificado, y haber tomado una de las tres decisiones con una razón. Lo que debe poder defender sin la máquina es cada etiqueta de la muestra que firmó como suya, y la decisión sobre el resto del corpus.

## Lecturas

**Central**

- Grimmer, J. y Stewart, B. M. (2013). "Text as Data: The Promise and Pitfalls of Automatic Content Analysis Methods for Political Texts". *Political Analysis* 21(3), 267-297. https://doi.org/10.1093/pan/mps028
- Ziems, C., Held, W., Shaikh, O., Chen, J., Zhang, Z. y Yang, D. (2024). "Can Large Language Models Transform Computational Social Science?". *Computational Linguistics* 50(1), 237-291. https://doi.org/10.1162/coli_a_00502

**Complementaria**

- Gilardi, F., Alizadeh, M. y Kubli, M. (2023). "ChatGPT outperforms crowd workers for text-annotation tasks". *Proceedings of the National Academy of Sciences* 120(30). https://doi.org/10.1073/pnas.2305016120
- Pangakis, N., Wolken, S. y Fasching, N. (2023). "Automated Annotation with Generative AI Requires Validation". https://arxiv.org/abs/2306.00176
- Krippendorff, K. (1990). *Metodología de análisis de contenido. Teoría y práctica*. Barcelona: Paidós. Cap. sobre fiabilidad.
- Zainea, C. I. (2026). "Los modelos de lenguaje no alucinan: cometen infortunios". https://izainea.github.io/blog/alucinacion-o-infortunio/
- Zainea, C. I. (2026). "La prótesis hermenéutica". https://izainea.github.io/blog/protesis-hermeneutica/

## Guía de lectura

- Grimmer y Stewart escribieron antes de los modelos de lenguaje actuales y sus cuatro principios no han envejecido. Lea la sección sobre validación como si hablara de su práctica de esta semana. *¿Cuál de los cuatro principios es el que su proyecto está más tentado de saltarse?*
- Ziems y sus coautores evalúan modelos de lenguaje en decenas de tareas de ciencias sociales computacionales y concluyen que sirven como anotadores auxiliares, no como reemplazo. Note cómo definen "auxiliar". *¿Qué tendría que pasar en su auditoría para que usted dijera que el modelo no sirve ni como auxiliar en su corpus?*
- Pangakis, Wolken y Fasching muestran que el rendimiento de la anotación automática varía mucho entre tareas y que no se puede saber sin validar en cada caso. *¿Qué tasa de acuerdo le parece suficiente para su uso, y por qué esa y no otra?*
- Las dos entradas del docente dan el vocabulario de la decisión: infortunio y prótesis. *Cuando acepta una etiqueta del modelo con una tasa de acuerdo declarada, ¿quién responde por esa etiqueta y en qué documento consta?*

## Taller de la segunda hora

Auditoría de la lectura asistida sobre la muestra de treinta unidades del corpus propio. Guía completa en `practicas/practica-07-auditoria-lectura-asistida.md`; bloques en `practicas/cuaderno-apoyo.md`, sección "Semana 7".

1. Escribir la instrucción con las categorías, su definición, la regla para la duda y el formato de salida; guardarla como `instruccion_v1.md`.
2. Enviar las treinta unidades al modelo con esa instrucción y guardar cada respuesta con fecha, versión e identificador.
3. Etiquetar las treinta a ciegas en una tabla aparte.
4. Comparar: proporción de acuerdo, kappa, lista de desacuerdos.
5. Tipificar cada desacuerdo y decidir.
6. Llenar el registro de frontera del corpus con esta operación y las anteriores.

| Unidad | Etiqueta del modelo | Mi etiqueta | ¿Coinciden? | Tipo de desacuerdo | Quién tenía razón y por qué |
|---|---|---|---|---|---|

## Guion de la sesión

| Momento | Docente | Estudiante | Material |
|---|---|---|---|
| 0 a 10 min | Muestra tres resúmenes del modelo sobre notas del caso, uno fiel, uno que inventa un detalle, uno que omite lo central | Adivina cuál es cuál y luego lee las notas | Tres notas y tres resúmenes |
| 10 a 30 min | Las cuatro operaciones y la instrucción como criterio versionado | Escribe la primera versión de su instrucción | Plantilla de instrucción |
| 30 a 50 min | Auditoría sobre el caso: etiqueta diez unidades con el grupo a ciegas y compara con el modelo | Participa y cuenta acuerdos | Diez unidades del caso |
| 50 a 60 min | Tipología de desacuerdos y las tres decisiones; figura 7 | Clasifica los desacuerdos del caso | Figura 7 |
| 60 a 70 min | Pausa | | |
| 70 a 110 min | Acompaña la auditoría propia | Ejecuta los seis pasos del taller | practica-07 |
| 110 a 120 min | Pide dos decisiones en voz alta con su razón | Anota la suya | Registro de frontera |

Notas para el docente. Lo que suele fallar: el estudiante mira las etiquetas del modelo antes de etiquetar y el acuerdo se infla; separar las dos tablas en archivos distintos y pedir que la del modelo no se abra hasta terminar. El segundo fallo es una lista de categorías que se solapan, con lo que el desacuerdo mide la lista y no la lectura; revisarla en la primera media hora. El tercero es tomar una tasa de acuerdo alta como prueba de corrección; recordar que dos lectores pueden coincidir en un error, y que el que firma es uno solo.

## Bitácora

La instrucción versionada, las dos tablas de etiquetas, la comparación con su cifra y la tipología de desacuerdos, la decisión con su razón, y el registro de frontera actualizado con todas las operaciones del curso. Una pregunta abierta sobre el desacuerdo que más le costó resolver.

## Para la próxima semana

Leer Bender y Friedman (2018) sobre las declaraciones de datos y la sección sobre la prótesis hermenéutica de Zainea (2026). Redactar el borrador del informe de corpus con la plantilla, y preparar una presentación de ocho minutos que empiece por la frontera del corpus y termine por la decisión de la auditoría.
