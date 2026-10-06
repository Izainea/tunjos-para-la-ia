# Semana 1. La máquina que afirma

## Pregunta de la semana

Cuando un modelo de lenguaje responde, ¿afirma algo, y si afirma, quién afirma?

## Por qué esta semana

<p class="lede">El curso no empieza por la lógica sino por un problema que cualquiera que use modelos ha sentido. El output llega con la forma de una respuesta segura, bien escrita, con la estructura de un argumento, y a veces es falso. La reacción común es decir que el modelo alucinó. Esta semana muestra por qué esa palabra confunde y propone otra, tomada de Austin: el modelo comete un infortunio<sup class="mark">a</sup>. Produce un acto con la forma de una aserción fundamentada sin satisfacer las condiciones que la fundamentan. Nombrar bien el fallo decide dónde se busca la solución.</p>

<aside class="glosa"><span class="mark">a</span> En Austin, <i>infelicity</i> cubre los performativos que fallan por no cumplir sus condiciones convencionales: el juez sin jurisdicción, la promesa bajo coacción. No los enunciados falsos, que son errores ordinarios.</aside>

La semana abre también el hilo que recorre todo el curso. Un resultado puede validarse en tres sentidos distintos: porque es correcto, porque el proceso que lo produjo puede exhibirse, o porque alguien responde por él. A cada sentido le corresponde, como se verá entre las semanas 2 y 6, un tipo de inferencia donde se juega. Esta semana solo nombra los tres y muestra que un sistema con 95 % de acierto puede fallar en los dos últimos. Rendimiento no es validez<sup class="mark">b</sup>.

<aside class="glosa"><span class="mark">b</span> El 95 % correcto de un modelo se produce por las mismas razones estadísticas que el 5 % incorrecto. No hay una diferencia interna que el sistema pueda señalar entre uno y otro; esa es la tesis de <i>Agencia sin imputación</i> (Zainea, 2026) que el curso pone a prueba.</aside>

## Contenido de la sesión

1. Tres outputs reales de un modelo sobre un tema que el grupo conoce abren la sesión: uno correcto, uno falso y uno que nadie en la sala puede decidir sin verificar. Los tres tienen la misma forma, el mismo tono y la misma seguridad. La pregunta es qué los distingue desde adentro, y la respuesta es nada. Esa observación, y no una tesis sobre la mente de la máquina, es el punto de partida del curso.

2. La palabra alucinación migró de la psicopatología al discurso técnico cuando hizo falta una metáfora para audiencias no especializadas. Presupone una mente que construye representaciones del mundo y a veces las distorsiona. El modelo no construye representaciones en ningún sentido relevante: cuando genera un token falso sigue el mismo procedimiento que cuando genera uno verdadero. Hicks, Humphries y Slater (2024) prefieren hablar de *bullshit* en el sentido de Frankfurt, indiferencia a la verdad. La sesión discute por qué esa propuesta acierta en el diagnóstico y se queda corta en lo que permite diseñar.

3. Austin distingue en *Cómo hacer cosas con palabras* los enunciados que describen de los actos que hacen algo al decirse, y muestra que los segundos no son verdaderos o falsos sino afortunados o desafortunados. Un infortunio es un acto que tiene la forma de una promesa, un bautizo o una sentencia sin cumplir las condiciones que lo hacen valer. El curso extiende la categoría: el output de un modelo no es nunca puramente descriptivo, presenta *p* con la autoridad de quien procesó evidencia y llegó a una conclusión, y esa autoridad es lo que no puede respaldar. Eso es un infortunio de autoridad epistémica.

4. Las condiciones de un acto de habla epistémicamente válido son al menos cuatro: forma, referencia, sinceridad y capacidad de dar razones. El modelo satisface la primera con una perfección que oculta las otras tres. La referencia acierta y fabrica sin marca que distinga los casos. La sinceridad exige un sujeto que crea lo que dice, y no lo hay. Las razones, cuando se le piden, llegan como una nueva cadena de texto con la morfología de una justificación, que no es lo mismo que una justificación (Habermas, *Teoría de la acción comunicativa*, tomo I).

5. Validar un resultado puede significar tres cosas. Que el resultado es correcto. Que el proceso que lo produjo puede exhibirse y evaluarse. Que alguien se hace responsable de él ante otros. La ingeniería mide el primero con tasas de acierto. El segundo y el tercero son los que un sistema de 95 % de rendimiento puede no satisfacer, y los que la investigación necesita: una tesis no se defiende con una tasa.

6. El mapa del curso queda anunciado, no desarrollado. A la corrección del resultado le corresponde la deducción, que vale por su forma (semana 2). A la justificación del proceso le corresponde la inducción, que vale por sus tasas (semana 3). A la imputación le corresponde la abducción, que vale porque alguien se compromete a probarla (semanas 4 y 6). El modelo, como se verá en la semana 7, ejecuta las tres formas y solo puede ser validado en las dos primeras.

Los dos marcos que se enfrentan en la sesión pueden ponerse en una tabla de dos columnas. La última fila resume lo que cada uno permite hacer.

| Marco mentalista | Marco pragmático |
|---|---|
| El modelo alucina | El modelo comete infortunios |
| Tiene una mente que produce representaciones falsas del mundo | Produce un acto con la forma de una aserción sin cumplir sus condiciones de validez (Austin) |
| Solución: mejorar la mente, con más datos y más ajuste | Solución: construir desde afuera las condiciones de validez |
| *No hay mente; la metáfora es incoherente con su objeto* | *No presupone mente; permite diseñar* |

<figure class="wide">
  <svg viewBox="0 0 680 230" style="width:100%;max-width:42rem;height:auto;display:block" role="img" aria-label="Tres outputs con la misma forma: uno correcto, uno falso, uno indecidible. Desde adentro, nada los distingue. Debajo, los tres sentidos de validación: corrección, justificación, imputación.">
    <style>.w1-bx{fill:var(--surface);stroke:var(--rule);stroke-width:1.2} .w1-t{font-family:var(--text);font-size:13px;fill:var(--ink)} .w1-s{font-family:var(--text);font-size:11.5px;fill:var(--muted)} .w1-k{font-family:var(--mono);font-size:10px;letter-spacing:.08em;fill:var(--muted)} .w1-ok{fill:var(--c-inv)} .w1-no{fill:var(--c-fil)} .w1-q{fill:var(--c-doc)} .w1-ln{stroke:var(--rule);stroke-width:1.2} .w1-br{stroke:var(--c-fil);stroke-width:1.2;fill:none}</style>
    <g><rect x="20" y="20" width="200" height="70" rx="3" class="w1-bx"/><line x1="34" y1="40" x2="190" y2="40" class="w1-ln"/><line x1="34" y1="54" x2="206" y2="54" class="w1-ln"/><line x1="34" y1="68" x2="160" y2="68" class="w1-ln"/><circle cx="120" cy="104" r="5" class="w1-ok"/><text x="120" y="122" text-anchor="middle" class="w1-s">correcto</text></g>
    <g transform="translate(220 0)"><rect x="20" y="20" width="200" height="70" rx="3" class="w1-bx"/><line x1="34" y1="40" x2="190" y2="40" class="w1-ln"/><line x1="34" y1="54" x2="206" y2="54" class="w1-ln"/><line x1="34" y1="68" x2="160" y2="68" class="w1-ln"/><circle cx="120" cy="104" r="5" class="w1-no"/><text x="120" y="122" text-anchor="middle" class="w1-s">falso</text></g>
    <g transform="translate(440 0)"><rect x="20" y="20" width="200" height="70" rx="3" class="w1-bx"/><line x1="34" y1="40" x2="190" y2="40" class="w1-ln"/><line x1="34" y1="54" x2="206" y2="54" class="w1-ln"/><line x1="34" y1="68" x2="160" y2="68" class="w1-ln"/><circle cx="120" cy="104" r="5" class="w1-q"/><text x="120" y="122" text-anchor="middle" class="w1-s">indecidible sin verificar</text></g>
    <text x="340" y="146" text-anchor="middle" class="w1-k">DESDE ADENTRO: LA MISMA FORMA, EL MISMO TONO, LA MISMA SEGURIDAD</text>
    <path class="w1-br" d="M20 160 L20 170 L660 170 L660 160"/>
    <text x="120" y="196" text-anchor="middle" class="w1-t">¿Es correcto?</text><text x="120" y="212" text-anchor="middle" class="w1-k">CORRECCIÓN</text>
    <text x="340" y="196" text-anchor="middle" class="w1-t">¿Puede exhibirse el proceso?</text><text x="340" y="212" text-anchor="middle" class="w1-k">JUSTIFICACIÓN</text>
    <text x="560" y="196" text-anchor="middle" class="w1-t">¿Quién responde?</text><text x="560" y="212" text-anchor="middle" class="w1-k">IMPUTACIÓN</text>
  </svg>
  <figcaption><b>Figura 1.</b> Tres outputs de la misma forma y los tres sentidos en que podría validarse cada uno. La forma no decide ninguno de los tres.</figcaption>
</figure>

## IA y exigencia

Esta semana se le pide al modelo que haga lo que mejor hace: responder con seguridad a tres preguntas sobre un tema que el estudiante domina. La exigencia está del otro lado. El estudiante debe poder decir, sin el modelo y para cada output, si tiene forma de aserción, si puede verificarlo ahora, quién respondería si fuera falso y cuál de los tres sentidos de validación está en juego. Si no puede responder a la tercera pregunta, ya tiene el primer dato del curso: nadie responde, y eso no lo arregla un modelo mejor<sup class="mark">c</sup>.

<aside class="glosa"><span class="mark">c</span> Floridi (2023) caracteriza los modelos como agentes en sentido propio, interactivos, autónomos y adaptables, sin que por ello les corresponda intencionalidad ni responsabilidad. Hay agencia operativa; falta un agente al que imputar lo producido.</aside>

## Lecturas

**Central**

- Austin, J. L. (1982). *Cómo hacer cosas con palabras*. Conferencias I y II. Barcelona: Paidós. Edición original: *How to Do Things with Words*, Oxford, 1962.
- Floridi, L. (2023). "AI as Agency Without Intelligence: On ChatGPT, Large Language Models, and Other Generative Models". *Philosophy & Technology*, 36, 15. https://doi.org/10.1007/s13347-023-00621-y

**Complementaria**

- Hicks, M. T., Humphries, J. y Slater, J. (2024). "ChatGPT is bullshit". *Ethics and Information Technology*, 26, 38. https://doi.org/10.1007/s10676-024-09775-5
- Zainea, C. I. (2026). "Los modelos de lenguaje no alucinan: cometen infortunios". https://izainea.github.io/blog/alucinacion-o-infortunio/
- Frankfurt, H. G. (2006). *On Bullshit. Sobre la manipulación de la verdad*. Barcelona: Paidós.

## Guía de lectura

- Austin enumera seis condiciones de felicidad (A.1, A.2, B.1, B.2, Γ.1, Γ.2) y las dos últimas no exigen un procedimiento sino un hablante con ciertos pensamientos e intenciones. Un modelo puede cumplir las cuatro primeras por construcción, si el procedimiento existe y se ejecuta. *¿Cuáles de las seis podría cumplir un modelo de lenguaje y cuáles no, y qué cambia en el diagnóstico si la falla está en Γ y no en A o B?*

- Floridi separa agencia de inteligencia: un sistema puede actuar con consecuencias reales sin comprender nada. La separación evita la discusión ontológica y abre la epistemológica. *¿Qué pierde y qué gana esa distinción frente a decir, sin más, que el modelo no comprende?*

- Hicks, Humphries y Slater prefieren *bullshit* a alucinación porque el modelo es indiferente a la verdad, no porque se equivoque. El curso acepta el diagnóstico y lo reformula como infortunio. *¿Qué permite diseñar la segunda palabra que la primera no permite?*

- Frankfurt define el *bullshit* por la indiferencia a la verdad, distinta de la mentira, que la presupone. Un modelo no miente, porque no cree nada; tampoco es indiferente, porque no tiene una actitud. *¿Sirve una categoría pensada para hablantes humanos para describir un sistema sin actitudes, o hace falta una que no presuponga ninguna?*

## Taller de la segunda hora

Cada estudiante le pide a un modelo tres cosas sobre un tema que domina: un dato, una síntesis y una recomendación. Usa cualquier modelo de acceso gratuito en su versión web y guarda el prompt y el output literales<sup class="mark">d</sup>. Luego llena, para cada output, la ficha de la semana:

<aside class="glosa"><span class="mark">d</span> Literal quiere decir copiado, no resumido. Un resumen mejora o empeora lo que el modelo dijo, y la ficha pierde su objeto. El cuaderno de apoyo muestra cómo guardar cada llamada con fecha en un archivo.</aside>

| Output | ¿Tiene forma de aserción? | ¿Es verificable por mí ahora? | ¿Quién respondería si fuera falso? | Sentido de validación en juego |
|---|---|---|---|---|
| Dato | | | | |
| Síntesis | | | | |
| Recomendación | | | | |

La columna que más cuesta llenar es la cuarta. Si la respuesta es "el modelo", el estudiante debe preguntarse ante quién respondería el modelo y cómo. Si la respuesta es "yo", debe preguntarse con qué base. Las dos preguntas son el material de la bitácora.

En los últimos quince minutos, tres estudiantes leen en voz alta un output y el grupo intenta adivinar, sin verificar, cuál de los tres es. El ejercicio suele terminar en empate, y ese empate es el resultado de la semana.

## Guion de la sesión

| Momento | Docente | Estudiante | Material |
|---|---|---|---|
| 0 a 10 min | Presenta los tres outputs sin decir cuál es cuál | Vota cuál es falso y anota por qué | Tres outputs impresos o proyectados |
| 10 a 35 min | Expone alucinación e infortunio a partir de los votos | Interviene con casos propios | Austin, conferencias I y II; Figura 1 |
| 35 a 55 min | Presenta los tres sentidos de validación y el mapa del curso | Pregunta y toma nota del mapa | Tabla de los tres sentidos |
| 55 a 60 min | Pausa | | |
| 60 a 100 min | Acompaña el taller mesa por mesa | Produce los tres outputs y llena la ficha | Modelo en versión web, ficha de la semana |
| 100 a 115 min | Modera la lectura en voz alta | Tres estudiantes leen; el grupo adivina | Outputs del taller |
| 115 a 120 min | Cierra con la pregunta abierta y la bitácora | Anota su pregunta abierta | Bitácora |

**Notas para el docente.** Los outputs iniciales deben ser sobre un tema que el grupo conozca de verdad; si el docente los trae de su propio campo, el ejercicio se convierte en clase magistral. Conviene tenerlos verificados de antemano, con la fuente a mano. En el taller suele pasar que el modelo acierta los tres pedidos y el estudiante concluye que el problema no existe; la pregunta de salida es qué habría pasado si no hubiera podido verificar, y esa es la situación normal en investigación. No discutir todavía si el modelo comprende: la pregunta se declara aparcada hasta la semana 7, y el curso no la responde en términos ontológicos.

## Bitácora

Registre los tres outputs con sus prompts literales y la ficha completa. Añada una pregunta que le haya quedado abierta y una frase sobre qué diría ahora de un output que antes habría llamado alucinación. La bitácora de esta semana es la primera página del registro de frontera que se entrega en la semana 7.

## Para la próxima semana

Leer Russell, *Los problemas de la filosofía*, capítulo VII, y *Tractatus* 4 a 4.5. Traer un ejemplo de razonamiento que considere perfectamente válido y otro que considere válido pero inútil. La semana 2 cuenta la historia del primer sentido de validación, la corrección formal, y pone a verificar una cadena de pasos de un modelo con una mini app.
