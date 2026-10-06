# Semana 3. La inducción y la máquina que generaliza

## Pregunta de la semana

Si un modelo aprende regularidades de millones de ejemplos, ¿qué puede y qué no puede concluir de ellas?

## Por qué esta semana

<p class="lede">La inducción sí añade conocimiento: de muchos casos sale una regla. Es el método de la ciencia empírica y es, en su núcleo, lo que hace un modelo entrenado por aprendizaje estadístico. Pero la inducción tiene dos límites que la filosofía conoce desde hace tres siglos. El primero, de Hume: nada en los casos pasados garantiza los futuros, y cualquier justificación de la inducción usa la inducción. El segundo, de Goodman: infinitas hipótesis son compatibles con los mismos datos, y los datos no eligen entre ellas. Ambos límites son hoy límites de los modelos, y entenderlos es la mitad del criterio que el curso busca.</p>

La semana anterior dejó claro que la deducción vale por su forma y no informa. Esta semana muestra la inferencia que informa y que, por eso mismo, no vale por su forma sino por sus tasas de acierto a largo plazo: el segundo sentido de validación, la justificación del proceso, en su versión estadística<sup class="mark">a</sup>. Lo que la inducción no hace, elegir entre hipótesis que los datos no distinguen, es el hueco que la semana 4 llena con la abducción.

<aside class="glosa"><span class="mark">a</span> Una inducción no se verifica paso a paso como una deducción. Se evalúa por su historial: cuántas veces una regla inferida así acertó. Es el régimen de validez de la estadística y del aprendizaje automático, y es tan legítimo como el formal, mientras no se confunda con él.</aside>

## Contenido de la sesión

1. Hume separa en la sección IV de la *Investigación* las relaciones de ideas, que se conocen por puro pensamiento, de las cuestiones de hecho, que solo se conocen por experiencia. Que el sol saldrá mañana es una cuestión de hecho, y de que haya salido siempre no se sigue lógicamente que vuelva a salir. La única respuesta que Hume encuentra es el hábito: inferimos porque estamos hechos así. Lo que esa respuesta concede es que la inducción no tiene fundamento racional, solo práctico, y el curso tomará esa concesión en serio en la semana 6.

2. El pavo de Russell hace visible el argumento<sup class="mark">b</sup>. Alimentado todos los días a las nueve de la mañana, con lluvia y con sol, en invierno y en verano, infiere la regla de que siempre lo alimentan a las nueve. Llega la víspera de Navidad y la regla falla del modo más completo. La inducción es sintética, añade algo que no estaba en los casos, y por eso ninguna cantidad de casos la convierte en necesaria.

3. Goodman muestra en *Hecho, ficción y pronóstico* que el problema no es solo que el futuro pueda cambiar: es que ni siquiera el presente fija qué regla se infirió. Defina "verdul" como verde si se examinó antes de hoy y azul si no. Todas las esmeraldas observadas confirman por igual que las esmeraldas son verdes y que son verdules. Los datos no eligen. Lo que elige es la proyectabilidad del predicado, su arraigo en una práctica de uso, y eso no está en los datos sino en quienes los usan.

4. Popper ofrece una salida que el curso examina sin adoptar del todo: la ciencia no confirma, corrobora; avanza por conjeturas que se intentan refutar. Ninguna cantidad de cisnes blancos prueba que todos lo sean, y un cisne negro basta para refutarlo. Lo que Popper deja sin explicar es de dónde salen las conjeturas, y ese silencio es la puerta de la semana 4.

5. Chollet (2019) traduce el problema al vocabulario de la inteligencia artificial. La inteligencia no es una habilidad sino la eficiencia con que se adquieren habilidades nuevas; un sistema que interpola sobre datos masivos puede parecer inteligente en todo lo que se parece a su distribución y fallar en cuanto sale de ella. Los modelos actuales son máquinas inductivas de una potencia sin precedentes, y esa potencia no cambia el régimen de validez de lo que producen<sup class="mark">c</sup>.

6. Lo que la inducción no hace queda enunciado para la próxima semana. Confirma, no inventa. Pesa hipótesis que ya existen, no las propone. Cuando un modelo responde con la explicación más probable de unos datos, hace exactamente eso: elige la que más se parece a lo que vio, y la pregunta de la segunda hora es si esa elección es un criterio.

<figure class="wide">
  <svg viewBox="0 0 680 230" style="width:100%;max-width:42rem;height:auto;display:block" role="img" aria-label="Diagrama de puntos observados hasta hoy, todos sobre la misma línea. Después de hoy la línea se bifurca en dos hipótesis, verde y verdul, igual de compatibles con los puntos.">
    <style>.w3-ax{stroke:var(--rule);stroke-width:1.2} .w3-pt{fill:var(--ink)} .w3-a{stroke:var(--c-inv);stroke-width:2;fill:none} .w3-b{stroke:var(--c-app);stroke-width:2;fill:none;stroke-dasharray:6 4} .w3-hoy{stroke:var(--c-fil);stroke-width:1.4;stroke-dasharray:3 4} .w3-t{font-family:var(--text);font-size:12.5px;fill:var(--ink)} .w3-k{font-family:var(--mono);font-size:10px;letter-spacing:.08em;fill:var(--muted)} .w3-s{font-family:var(--text);font-size:11.5px;fill:var(--muted)}</style>
    <line x1="40" y1="190" x2="650" y2="190" class="w3-ax"/><line x1="40" y1="30" x2="40" y2="190" class="w3-ax"/>
    <text x="650" y="208" text-anchor="end" class="w3-k">TIEMPO</text><text x="46" y="26" class="w3-k">LO OBSERVADO</text>
    <line x1="380" y1="30" x2="380" y2="190" class="w3-hoy"/><text x="380" y="214" text-anchor="middle" class="w3-k" style="fill:var(--c-fil)">HOY</text>
    <path class="w3-a" d="M60 120 L650 120"/><path class="w3-b" d="M380 120 L650 48"/>
    <circle cx="80" cy="120" r="4" class="w3-pt"/><circle cx="125" cy="120" r="4" class="w3-pt"/><circle cx="170" cy="120" r="4" class="w3-pt"/><circle cx="215" cy="120" r="4" class="w3-pt"/><circle cx="260" cy="120" r="4" class="w3-pt"/><circle cx="305" cy="120" r="4" class="w3-pt"/><circle cx="350" cy="120" r="4" class="w3-pt"/>
    <text x="210" y="148" text-anchor="middle" class="w3-s">todas las esmeraldas examinadas, verdes</text>
    <text x="560" y="140" text-anchor="middle" class="w3-t" style="fill:var(--c-inv)">verde</text>
    <text x="560" y="54" text-anchor="middle" class="w3-t" style="fill:var(--c-app)">verdul</text>
    <text x="520" y="178" text-anchor="middle" class="w3-s">los mismos datos confirman las dos</text>
  </svg>
  <figcaption><b>Figura 1.</b> El nuevo enigma de Goodman. Hasta hoy, verde y verdul coinciden en cada observación; lo que las separa no es un dato sino una práctica.</figcaption>
</figure>

<aside class="glosa"><span class="mark">b</span> Russell usa un pollo en <i>Los problemas de la filosofía</i>, capítulo VI; el pavo es la versión que popularizó Alan Chalmers en <i>¿Qué es esa cosa llamada ciencia?</i>. El curso conserva el pavo porque la fecha de la cena hace más clara la ruptura.</aside>

<aside class="glosa"><span class="mark">c</span> Chollet propone medir la inteligencia con tareas que no se parezcan a nada del entrenamiento, el <i>Abstraction and Reasoning Corpus</i>. En 2019 los mejores sistemas resolvían una fracción pequeña; la cifra ha subido desde entonces y la discusión sobre qué mide sigue abierta.</aside>

Los dos límites de la inducción que la sesión presenta no son el mismo, y conviene separarlos en dos columnas antes del taller.

| Límite de Hume | Límite de Goodman |
|---|---|
| Los casos pasados no garantizan los futuros | Los casos pasados no fijan siquiera qué regla se infirió |
| Toda justificación de la inducción usa la inducción | Infinitas hipótesis son compatibles con los mismos datos |
| Respuesta disponible: el hábito, una práctica | Respuesta disponible: la proyectabilidad, también una práctica |
| *Un modelo generaliza sin garantía, como cualquiera* | *Un modelo elige entre hipótesis por lo que más vio, y eso no es un criterio lógico* |

## IA y exigencia

Esta semana el modelo hace lo que hace un inductor: dado un conjunto de datos, propone la regla que mejor los explica, y luego otra. La exigencia es que el estudiante produzca por su cuenta una segunda hipótesis compatible con los mismos datos antes de pedirle la tercera al modelo, y que identifique el dato nuevo que las distinguiría. Sin la máquina, el estudiante debe poder decir con qué criterio eligió el modelo la primera hipótesis y con qué criterio elegiría él. Si los dos criterios resultan ser "la más común", la semana cumplió su objetivo: ese criterio es inductivo y no es el único.

## Lecturas

**Central**

- Hume, D. (2004). *Investigación sobre el entendimiento humano*. Sección IV, "Dudas escépticas sobre las operaciones del entendimiento". Madrid: Alianza. Original de dominio público: https://www.gutenberg.org/ebooks/9662
- Goodman, N. (2004). *Hecho, ficción y pronóstico*. Capítulo III, "El nuevo enigma de la inducción". Madrid: Síntesis.
- Chollet, F. (2019). "On the Measure of Intelligence". Secciones I y II. https://arxiv.org/abs/1911.01547

**Complementaria**

- Russell, B. (1970). *Los problemas de la filosofía*. Capítulo VI, "Sobre la inducción". https://www.gutenberg.org/ebooks/5827
- Popper, K. (1980). *La lógica de la investigación científica*. Capítulo I. Madrid: Tecnos.
- Chalmers, A. F. (2000). *¿Qué es esa cosa llamada ciencia?* Capítulos 1 y 2. Madrid: Siglo XXI.

## Guía de lectura

- Hume sostiene que toda justificación de la inducción presupone que la naturaleza es uniforme, y que solo la inducción apoya esa presuposición. El argumento es circular, no falso. *¿Es un argumento contra la inducción, o contra cierta idea de lo que sería justificarla?*

- Goodman pregunta qué hace que "verde" sea mejor hipótesis que "verdul" si los datos las confirman igual. Si la respuesta es que siempre hemos usado verde, la validez de la inducción descansa en una práctica. *¿Es eso un criterio lógico o una costumbre, y qué cambiaría si fuera lo segundo?* Guarde la respuesta para la semana 6.

- Chollet distingue habilidad de generalización y critica medir la inteligencia por el desempeño en tareas conocidas. Los modelos de lenguaje se evalúan casi siempre por desempeño en tareas conocidas. *¿Qué mide entonces una tasa de acierto, y qué no mide?*

- Popper afirma que la ciencia no confirma sino corrobora, y que una conjetura vale mientras resiste intentos de refutación. *¿Puede un modelo proponer una conjetura refutable, y puede querer refutarla?* Son dos preguntas distintas; responda las dos.

## Taller de la segunda hora

Se le da al grupo un conjunto pequeño de datos reales: una tabla de veinte filas de un tema social o veinte fragmentos de texto, de preferencia tomados del proyecto de uno de los estudiantes. Se le pide a un modelo que formule la hipótesis que mejor los explica. Luego cada estudiante:

1. Formula por su cuenta una segunda hipótesis distinta, compatible con los mismos datos. Debe escribirla antes de volver al modelo.
2. Le pide al modelo una tercera, con la instrucción de que sea incompatible con la primera y compatible con todos los datos. El cuaderno de apoyo trae el prompt.
3. Identifica qué dato nuevo distinguiría entre las tres. Si no existe tal dato, las hipótesis no son distintas.
4. Responde por escrito: ¿con qué criterio eligió el modelo la primera? ¿Con qué criterio elegiría usted?

| | Hipótesis | Origen | Dato que la refutaría |
|---|---|---|---|
| H1 | | modelo | |
| H2 | | propia | |
| H3 | | modelo | |

Las tres hipótesis y el dato discriminante son el borrador de la ficha de hipótesis de la semana 6, cuando se les aplique el filtro de Peirce.

## Guion de la sesión

| Momento | Docente | Estudiante | Material |
|---|---|---|---|
| 0 a 10 min | Recoge las regularidades traídas de casa y pregunta cómo se justifican | Expone la suya y descubre la circularidad | Ejemplos de los estudiantes |
| 10 a 30 min | Hume y el pavo de Russell | Discute si el hábito es una respuesta | Hume, sección IV |
| 30 a 45 min | Goodman con la Figura 1 | Propone otro predicado del tipo verdul sobre sus propios datos | Figura 1 |
| 45 a 55 min | Popper y Chollet en contraste: corroborar y generalizar | Anota la pregunta que Popper deja abierta | Chollet, secciones I y II |
| 55 a 60 min | Pausa | | |
| 60 a 75 min | Presenta los datos y obtiene la primera hipótesis del modelo ante el grupo | Lee los datos; anota la H1 | Datos del taller; modelo en versión web |
| 75 a 100 min | Acompaña la formulación de H2 y la obtención de H3 | Escribe H2 sin el modelo; pide H3 | Cuaderno de apoyo, semana 3 |
| 100 a 115 min | Recoge los datos discriminantes propuestos | Defiende su dato | Tabla del taller |
| 115 a 120 min | Cierra con la pregunta del criterio | Responde la pregunta 4 en la bitácora | Bitácora |

**Notas para el docente.** La H2 propia debe escribirse antes de ver la H3 del modelo; si se invierte el orden, el estudiante produce una variante de lo que el modelo dijo y el ejercicio se pierde. Los datos del taller tienen que ser de verdad ambiguos: veinte filas que solo admiten una lectura dejan sin material la hora. Es frecuente que el modelo entregue como primera hipótesis la explicación más común en la literatura sobre el tema, no la que mejor se ajusta a esos datos; conviene señalarlo cuando ocurre, sin llamarlo error, porque es exactamente lo que un inductor hace.

## Bitácora

Las tres hipótesis con su origen, el dato discriminante y la respuesta a la pregunta del criterio. Anote además si la H1 del modelo le pareció la mejor y por qué: la semana 6 le pedirá revisar esa impresión con criterios explícitos.

## Para la próxima semana

Peirce (1878) completo y las secciones indicadas de las conferencias de 1903. Harman (1965). Timmermans y Tavory (2012). Es la semana central del curso y la primera entrega evaluable; reservar tiempo. Traer el flujo del propio proyecto dividido en pasos, aunque sea en borrador.
