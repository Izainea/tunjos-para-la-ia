# Semana 4. Abducción aplicada para elegir qué hipótesis perseguir

## Pregunta de la semana

Entre los patrones y códigos que el trabajo de configuración produjo, ¿cuál merece convertirse en hipótesis, con qué criterio se elige, y quién paga el costo de probarla?

## Por qué esta semana

<p class="lede">Las semanas 2 y 3 trabajaron el segundo sentido de validación: el proceso y sus criterios. Esta semana da el paso que ningún criterio de proceso da por sí solo: pasar del patrón a la hipótesis. Un modelo entrenado sobre un corpus produce patrones con facilidad, y un sistema de agentes produce candidatos de hipótesis en cantidad. Lo que ni el patrón ni el candidato traen es la decisión de perseguirlos. [*Validación del razonamiento con IA en ciencias sociales*](../../curso-1-tres-inferencias/programa/semana-04.md), el curso de fundamentos del programa, mostró con Peirce que la abducción, la inferencia que parte de un hecho sorprendente y propone la hipótesis que lo haría natural, no vale ni por forma ni por frecuencia: vale porque alguien se compromete a ponerla a prueba bajo criterios de economía, y por eso su validación no se delega. Esta semana aplica ese resultado al material propio. El estudiante llega con tres patrones que no sabe qué significan y sale con una hipótesis elegida, los cuatro criterios aplicados y una prueba diseñada. Es la semana en que el investigador empieza a refigurar, porque elegir qué perseguir ya es apropiarse de lo configurado.</p>

## Contenido de la sesión

1. Peirce describió la abducción como la inferencia que parte de un hecho sorprendente y propone la hipótesis que lo haría natural, y añadió que es la única operación lógica que introduce una idea nueva. En la séptima conferencia de Harvard (1903), formuló la pregunta que esta semana trabaja: puesto que hay infinitas hipótesis posibles, ¿con qué criterio se elige cuál perseguir? Su respuesta no es un criterio de verdad sino de economía de la investigación: la hipótesis debe explicar el hecho, ser verificable experimentalmente, ser económica en costo, rendimiento y en no cerrar otras vías, y ser plausible dado lo que ya se sabe.<sup class="mark">a</sup> Esos criterios se presentaron en [*Validación del razonamiento con IA en ciencias sociales*](../../curso-1-tres-inferencias/README.md), donde sirvieron de filtro sobre hipótesis pedidas a un modelo, evaluadas por sorpresa, plausibilidad, verificabilidad y economía; aquí se aplican a patrones que salieron de una máquina.

<aside class="glosa"><span class="mark">a</span> Peirce trató la economía de la investigación como un problema propio, en un texto de 1879 para el Coast Survey y en los <i>Collected Papers</i> (CP 7.220). La idea es que la investigación tiene costos y rendimientos, y que elegir qué hipótesis probar primero es una decisión económica antes que lógica. Es la razón por la que la validez de una abducción depende de quien decide.</aside>

2. Un patrón no es una hipótesis. Un patrón es una regularidad en lo configurado: estos códigos co-ocurren, estas imágenes se agrupan, esta palabra sube en este período. Una hipótesis es una proposición sobre por qué, que si fuera verdad haría natural el patrón. El paso del uno a la otra exige un hecho sorprendente, y la sorpresa supone un trasfondo: algo sorprende porque se esperaba otra cosa. Timmermans y Tavory (2012) hicieron de esto el centro de su análisis abductivo: la teoría fundamentada no es inductiva aunque lo diga, porque codificar es encontrar lo sorprendente, y nada sorprende sin conocimiento previo. Un modelo produce patrones sin que nada en él se sorprenda. Eso no es una tesis sobre lo que la máquina no puede; es la observación de que la sorpresa es del investigador, y por eso la hipótesis también.<sup class="mark">c</sup>

<aside class="glosa"><span class="mark">c</span> Stefan Timmermans e Iddo Tavory llamaron análisis abductivo a una revisión de la teoría fundamentada que exige al investigador familiaridad con muchas teorías, para que los datos puedan sorprenderlo, y trabajo sistemático con los casos que no encajan. Su libro de 2014, <i>Abductive Analysis</i>, desarrolla el artículo que el curso lee.</aside>

3. Cuando se le pide a un modelo que proponga hipótesis sobre un patrón, propone, y propone bien en un sentido preciso: sus candidatos tienden a ser los que un lector informado del corpus de entrenamiento daría primero. Eso los hace plausibles por defecto y poco sorprendentes por construcción. El filtro peirceano aplicado a candidatos de un modelo tiene por eso una forma típica: el candidato gana en plausibilidad, empata en verificabilidad, y pierde en economía, porque la hipótesis más común suele ser la que cierra otras vías. La ficha de hipótesis de esta semana pide al estudiante que diga, para cada candidato del modelo, qué trasfondo lo hace plausible, y si ese trasfondo es el suyo, el de su comunidad o el del corpus de entrenamiento.

4. Verificable no basta; hace falta saber qué tan fuerte sería la prueba. Van Evera (1997) ordenó las pruebas de una hipótesis en cuatro tipos según lo que pasar o no pasar implica.<sup class="mark">b</sup> Una prueba de aro es necesaria pero no suficiente: si la hipótesis no la pasa, cae; si la pasa, sigue en pie sin confirmarse. Una prueba de pistola humeante es suficiente pero no necesaria: pasarla confirma; no pasarla no refuta. Una prueba de paja al viento es ni necesaria ni suficiente; una doblemente decisiva, ambas. El anteproyecto del docente usa esta ordenación como criterio de registro, la fuerza probatoria: un sistema puede etiquetar qué tipo de prueba sostiene cada hallazgo, y una persona puede auditar la etiqueta. Lo que no puede hacer el sistema es decidir que vale la pena correr la prueba.

<aside class="glosa"><span class="mark">b</span> Stephen Van Evera formuló los cuatro tipos en <i>Guide to Methods for Students of Political Science</i> (1997) a partir de la lógica del rastreo de procesos. Los nombres, aro, pistola humeante, paja al viento y doblemente decisiva, se usan hoy en toda la metodología de estudios de caso para decir cuánto pesa una evidencia antes de recogerla.</aside>

5. La admisibilidad de una hipótesis es un criterio de registro; el compromiso con ella es una condición de imputación. La distinción importa porque los dos se confunden en la práctica: un informe dice que "el análisis sugiere" una hipótesis y nadie sabe si alguien la persigue. Una hipótesis es admisible si explica el hecho, es verificable y no contradice lo establecido sin decirlo; eso puede comprobarse con el registro. Una hipótesis está comprometida si alguien ha decidido perseguirla, ha diseñado la prueba y asume el costo si falla; eso solo lo puede hacer un agente que responda. La ficha de hipótesis separa las dos cosas en dos secciones, y la rúbrica evalúa la segunda en primera persona.

6. El resultado de la semana es una decisión documentada. De los tres patrones, uno se convierte en hipótesis con prueba diseñada, uno se guarda como conjetura admisible sin compromiso, y uno se descarta con razón. Las tres decisiones son del estudiante aunque los candidatos los haya escrito el modelo, y las tres entran en el informe final con su estatuto: hallazgo, conjetura o descarte. La matriz de triangulación de la semana 5 recibe la hipótesis elegida como columna nueva y pregunta sobre cuántas patas se sostiene.

<figure class="wide">
<svg viewBox="0 0 680 260" style="width:100%;max-width:42rem;height:auto;display:block" role="img" aria-label="De izquierda a derecha: patrones producidos por la máquina entran a un embudo con cuatro filtros, explica el hecho, es verificable, es económica, es plausible, que son criterios de registro; a la salida, una sola hipótesis cruza la frontera hacia el compromiso, donde alguien diseña la prueba y asume el costo. Eso es imputación.">
<style>.a-h{font-family:var(--display);font-weight:700;font-size:13px;fill:var(--ink)} .a-d{font-family:var(--text);font-size:11.5px;fill:var(--muted)} .a-k{font-family:var(--mono);font-size:10px;letter-spacing:.08em;fill:var(--muted)} .a-kf{font-family:var(--mono);font-size:10px;letter-spacing:.08em;fill:var(--c-fil)} .a-bx{fill:var(--surface);stroke:var(--rule);stroke-width:1.2} .a-ln{stroke:var(--muted);stroke-width:1.3;fill:none} .a-fr{stroke:var(--c-fil);stroke-width:1.8;stroke-dasharray:6 5;fill:none} .a-pt{fill:var(--c-app)} .a-ok{fill:var(--c-inv)} .a-ah{fill:var(--muted)}</style>
<defs><marker id="a-ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 1L9 5L0 9z" class="a-ah"/></marker></defs>
<text x="60" y="22" text-anchor="middle" class="a-k">PATRONES</text>
<circle cx="40" cy="60" r="6" class="a-pt"/><text x="54" y="64" class="a-d">co-ocurrencia</text>
<circle cx="40" cy="100" r="6" class="a-pt"/><text x="54" y="104" class="a-d">agrupamiento</text>
<circle cx="40" cy="140" r="6" class="a-pt"/><text x="54" y="144" class="a-d">serie temporal</text>
<circle cx="40" cy="180" r="6" class="a-pt"/><text x="54" y="184" class="a-d">candidato del modelo</text>
<text x="60" y="222" text-anchor="middle" class="a-k">LA MÁQUINA LOS PRODUCE</text>
<path class="a-ln" d="M160 120 L190 120" marker-end="url(#a-ah)"/>
<rect x="200" y="36" width="250" height="180" rx="3" class="a-bx"/>
<text x="325" y="22" text-anchor="middle" class="a-k">FILTRO DE PEIRCE · REGISTRO</text>
<text x="214" y="66" class="a-h">¿Explica el hecho sorprendente?</text>
<text x="214" y="104" class="a-h">¿Es verificable, y con qué prueba?</text>
<text x="214" y="122" class="a-d">aro, pistola humeante, paja al viento</text>
<text x="214" y="156" class="a-h">¿Es económica?</text>
<text x="214" y="174" class="a-d">costo, rendimiento, no cierra vías</text>
<text x="214" y="204" class="a-h">¿Es plausible, y desde qué trasfondo?</text>
<path class="a-fr" d="M480 30 L480 230"/>
<text x="480" y="246" text-anchor="middle" class="a-kf">FRONTERA</text>
<path class="a-ln" d="M450 120 L500 120" marker-end="url(#a-ah)"/>
<rect x="510" y="70" width="160" height="100" rx="3" class="a-bx"/>
<text x="590" y="22" text-anchor="middle" class="a-k">COMPROMISO · POSICIÓN</text>
<circle cx="530" cy="96" r="6" class="a-ok"/>
<text x="544" y="100" class="a-h">la persigo</text>
<text x="524" y="124" class="a-d">diseño la prueba</text>
<text x="524" y="142" class="a-d">asumo el costo si falla</text>
<text x="524" y="160" class="a-d">respondo ante pares</text>
</svg>
<figcaption><b>Figura 4.</b> Del patrón a la hipótesis comprometida. Lo que hay que ver es que los cuatro criterios pueden aplicarse sobre el registro, y que la decisión de perseguir una hipótesis está del otro lado de la frontera.</figcaption>
</figure>

## IA y exigencia

Esta semana se le pide al modelo que proponga, para cada uno de los tres patrones del estudiante, dos hipótesis que los explicarían y una observación que las distinguiría. El estudiante debe poder aplicar los cuatro criterios a cada candidato sin ayuda, decir desde qué trasfondo es plausible cada uno, clasificar la prueba propuesta según Van Evera, y tomar una decisión que pueda sostener aunque la hipótesis elegida la haya escrito el modelo.

## Lecturas

**Central**

- Peirce, C. S. (1903). "El pragmatismo como lógica de la abducción". Séptima conferencia de Harvard. Traducción del Grupo de Estudios Peirceanos, Universidad de Navarra. https://www.unav.es/gep/PragmatismoLogicaAbduccion.html
- Timmermans, S. y Tavory, I. (2012). "Theory Construction in Qualitative Research: From Grounded Theory to Abductive Analysis". *Sociological Theory* 30(3), 167-186. https://doi.org/10.1177/0735275112457914

**Complementaria**

- Peirce, C. S. (1878). "Deducción, inducción e hipótesis". Traducción del Grupo de Estudios Peirceanos. https://www.unav.es/gep/DeducInducHipotesis.html
- Van Evera, S. (1997). *Guide to Methods for Students of Political Science*. Ithaca: Cornell University Press. Capítulo 1, sobre las pruebas de una hipótesis.
- Lipton, P. (2004). *Inference to the Best Explanation*. 2.ª ed. Londres: Routledge. Capítulo 4.
- Reichertz, J. (2007). "Abduction: The Logic of Discovery of Grounded Theory". En A. Bryant y K. Charmaz (eds.), *The SAGE Handbook of Grounded Theory*, 214-228. Londres: Sage.
- Charmaz, K. (2014). *Constructing Grounded Theory*. 2.ª ed. Londres: Sage. Capítulo sobre codificación.

## Guía de lectura

- Peirce dice en 1903 que la abducción "sugiere meramente que algo puede ser", y que su justificación es que sin ella no hay investigación. *Si la justificación de la abducción es que hace posible investigar, ¿qué le pasa a una hipótesis que nadie va a investigar, por bien formulada que esté?*
- Timmermans y Tavory insisten en que el investigador necesita un trasfondo teórico amplio para que algo le sorprenda. *Cuando un modelo propone una hipótesis plausible, ¿de quién es el trasfondo que la hace plausible, y qué pasa si ese trasfondo no coincide con el de la comunidad cuyo material se analiza?*
- Van Evera ordena las pruebas por lo que implica pasarlas o no. *Para la hipótesis que usted va a elegir, ¿qué prueba está a su alcance, de qué tipo es, y qué se compromete a aceptar si no la pasa?*
- Reichertz distingue la abducción de la mera adivinanza por el compromiso posterior con la verificación. *¿Es esa distinción lógica o práctica? ¿Qué cambia para un informe que presenta hipótesis sin prueba diseñada?*
- En el texto de 1878, Peirce presenta la hipótesis como el silogismo girado: de la regla y el resultado al caso. *Tome un patrón suyo y escríbalo como resultado; ¿cuál sería la regla que, si valiera, haría de su material un caso? ¿Es esa regla suya o del corpus del modelo?*

Sobre los candidatos del modelo. Conviene pedirlos con una instrucción que exija, para cada hipótesis, el hecho que explica, la observación que la distinguiría de la otra y el supuesto que da por sentado. La tercera parte es la que más sirve para la columna del trasfondo, porque el modelo suele hacer explícito ahí lo que trajo de su corpus.

## Taller de la segunda hora

Ficha de hipótesis sobre material propio. Cada estudiante trae tres patrones y, con un modelo, obtiene dos candidatos de hipótesis por patrón. Luego llena la ficha, que está en la segunda parte de `plantillas/matriz-de-triangulacion.md`.

| Patrón | Hecho sorprendente y desde qué trasfondo | Hipótesis (propia o del modelo) | Explica | Verificable, con qué prueba y de qué tipo | Económica | Plausible, desde qué trasfondo | Decisión |
|---|---|---|---|---|---|---|---|

La columna decisiva es la última, y tiene tres valores posibles: persigo, guardo como conjetura, descarto. Para "persigo" hay que escribir la prueba y el costo. Para "guardo" hay que decir qué haría falta para perseguirla. Para "descarto" hay que decir qué criterio la hundió.

## Guion de la sesión

| Momento | Docente | Estudiante | Material |
|---|---|---|---|
| 0 a 10 min | Devuelve comentarios generales sobre los protocolos entregados | Anota qué debe corregir | Protocolos |
| 10 a 35 min | Expone los cuatro criterios de Peirce con un patrón propio del prototipo visual como ejemplo | Aplica los criterios en voz alta a un patrón del grupo | Figura 4 |
| 35 a 55 min | Introduce las pruebas de Van Evera y la distinción entre admisibilidad y compromiso | Clasifica una prueba propuesta por el docente | Van Evera, cap. 1 |
| 55 a 65 min | Pausa | | |
| 65 a 105 min | Acompaña la ficha: pide candidatos al modelo, aplica criterios, decide | Llena la ficha para sus tres patrones | Plantilla |
| 105 a 120 min | Recoge las decisiones y pregunta a dos estudiantes por qué la decisión es suya | Defiende una decisión en dos minutos | Bitácora |

Notas para el docente. Lo que suele fallar: el estudiante elige la hipótesis más plausible y no la más económica, y después no sabe qué prueba diseñar; conviene pedir la prueba antes de la decisión. Segundo fallo: el hecho sorprendente no se formula, y sin él la ficha es una lista de ideas; devolver la ficha hasta que diga qué se esperaba y por qué. Tercero: la frontera entre admisibilidad y compromiso se borra cuando el estudiante escribe "se podría investigar"; exigir sujeto y verbo en primera persona.

## Bitácora

Registre los candidatos literales del modelo, la ficha completa y la decisión. Anote si la hipótesis elegida la escribió el modelo y por qué, aun así, la decisión es suya y qué costo asume.

## Para la próxima semana

Leer Entman (1993) y el capítulo 1 de Kress y van Leeuwen (2006). Si su material es visual, leer además Barthes, "Retórica de la imagen". Traer una imagen o un fragmento de texto de su corpus con la descripción o codificación que un modelo produjo sobre él, y la matriz de triangulación avanzada: se entrega en la semana 5 junto con la ficha de hoy.
