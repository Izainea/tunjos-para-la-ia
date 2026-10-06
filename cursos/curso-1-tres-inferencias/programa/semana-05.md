# Semana 5. Los límites formales: Hilbert, Gödel, Turing

## Pregunta de la semana

¿Qué demostraron Gödel y Turing, y qué se les ha hecho decir sobre la inteligencia artificial que no demostraron?

## Por qué esta semana

<p class="lede">El argumento más popular contra la inteligencia artificial dice: por el teorema de incompletitud, hay verdades que la mente humana capta y ninguna máquina puede demostrar; luego la mente no es una máquina. Está en Lucas (1961), en Penrose (1989) y en casi toda la divulgación, incluido el video que el curso usa como punto de entrada. Y está entre los argumentos más refutados de la filosofía de la mente. Esta semana enseña los teoremas de verdad, para poder decir con precisión qué sí implican para el curso.</p>

Lo que implican es más modesto que la conclusión de Penrose y mucho más útil. Ningún sistema formal consistente puede certificar su propia consistencia desde adentro, y no existe un procedimiento general de decisión<sup class="mark">a</sup>. Dicho en los términos del curso: la validación en el segundo y el tercer sentido, la justificación del proceso y la imputación, es necesariamente externa al sistema que produce el resultado. El proyecto de la semana 2, identificar validación con corrección formal, no fue refutado desde afuera por sus críticos; encontró su límite desde adentro, por sus mejores practicantes. Esa es la lección que el curso conserva, y la que la semana 7 aplicará a los verificadores de los modelos.

<aside class="glosa"><span class="mark">a</span> El <i>Entscheidungsproblem</i> de Hilbert pedía un procedimiento que, dada cualquier fórmula de la lógica de primer orden, decidiera en un número finito de pasos si es válida. Church y Turing mostraron en 1936, por caminos distintos, que no existe.</aside>

## Contenido de la sesión

1. Hilbert formula hacia 1900 y precisa en 1928 el programa formalista: mostrar que la matemática es completa, toda verdad se demuestra; consistente, no se demuestra ninguna contradicción; y decidible, hay un procedimiento que resuelve cualquier pregunta. Después de Frege y Russell era un sueño razonable, y la sesión empieza por hacerlo verosímil: si la validez es forma, la forma debería bastarse a sí misma.

2. La paradoja de Russell reaparece aquí como aviso. El conjunto de todos los conjuntos que no se contienen a sí mismos se contiene si y solo si no se contiene. La autorreferencia es la grieta por la que entrará Gödel: un sistema capaz de hablar de sus propias fórmulas puede construir una que hable de sí misma.

3. Gödel demuestra en 1931 dos cosas. Primero, que todo sistema formal consistente capaz de expresar la aritmética contiene enunciados verdaderos que no demuestra. Segundo, que tal sistema no puede demostrar su propia consistencia<sup class="mark">b</sup>. La sesión dedica tanto tiempo a lo que los teoremas no dicen como a lo que dicen: no dicen que la matemática sea inconsistente, no dicen que haya contradicciones en matemáticas, no dicen nada sobre mentes ni sobre máquinas. Dicen algo sobre sistemas formales, y lo dicen con una demostración que cualquiera puede verificar.

4. Turing publica en 1936 el resultado que completa el cuadro: no hay procedimiento general que decida si un programa termina. La máquina de Turing, el modelo de todo computador posterior, nace de un resultado negativo, de la necesidad de definir con precisión qué es un procedimiento para poder demostrar que uno no existe. En 1950, en el artículo del juego de la imitación, Turing ya había respondido a la objeción matemática: también los humanos se equivocan, y nadie ha mostrado que una mente pueda certificar su propia consistencia.

5. El argumento de Lucas y Penrose se reconstruye con caridad y después se examina. Premisa uno: para todo sistema formal consistente hay una verdad gödeliana que el sistema no demuestra. Premisa dos: un matemático humano puede ver que esa verdad es verdadera. Conclusión: la mente no es un sistema formal. Las objeciones son conocidas. Si la mente es un sistema formal, también está sujeta al teorema y no puede ver su propia sentencia gödeliana; si no lo es, eso es lo que había que probar (Putnam, Benacerraf). Nadie puede saber que su propio sistema es consistente, y la premisa dos lo presupone (Feferman, Chalmers). Y los modelos actuales no son sistemas deductivos axiomáticos: aplicarles Gödel es un cambio de categoría.

6. Lo que queda en pie es lo que el curso necesita. Un sistema no valida su propia consistencia desde adentro. Reconocer que un problema no tiene solución es un problema de decidibilidad, y los modelos de razonamiento actuales reconocen solo una fracción pequeña de los problemas sin solución (Valmeekam, Stechly y Kambhampati, 2024). Validar es externo. El debate de la segunda hora tiene un solo objetivo: que el grupo llegue por sí mismo a esa conclusión después de haber tumbado la de Lucas.

<figure class="wide">
  <svg viewBox="0 0 680 250" style="width:100%;max-width:42rem;height:auto;display:block" role="img" aria-label="Un sistema formal representado como una caja. Una flecha que sale de la caja e intenta volver a ella para certificar su consistencia está tachada. Otra flecha sale de la caja hacia una validación externa y llega.">
    <style>.w5-bx{fill:var(--surface);stroke:var(--rule);stroke-width:1.2} .w5-t{font-family:var(--text);font-size:13px;fill:var(--ink)} .w5-s{font-family:var(--text);font-size:11.5px;fill:var(--muted)} .w5-k{font-family:var(--mono);font-size:10px;letter-spacing:.08em;fill:var(--muted)} .w5-kf{font-family:var(--mono);font-size:10px;letter-spacing:.08em;fill:var(--c-fil)} .w5-ki{font-family:var(--mono);font-size:10px;letter-spacing:.08em;fill:var(--c-inv)} .w5-ar{fill:none;stroke:var(--muted);stroke-width:1.4} .w5-bad{fill:none;stroke:var(--c-fil);stroke-width:1.6;stroke-dasharray:6 4} .w5-ok{fill:none;stroke:var(--c-inv);stroke-width:1.8} .w5-x{stroke:var(--c-fil);stroke-width:2.4}</style>
    <defs><marker id="w5-ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 1L9 5L0 9z" fill="var(--muted)"/></marker><marker id="w5-ahok" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 1L9 5L0 9z" fill="var(--c-inv)"/></marker></defs>
    <rect x="40" y="60" width="300" height="130" rx="3" class="w5-bx"/>
    <text x="52" y="80" class="w5-k">SISTEMA FORMAL · modelo · verificador</text>
    <text x="52" y="106" class="w5-t">axiomas y reglas</text>
    <path class="w5-ar" d="M52 118 L52 136" marker-end="url(#w5-ah)"/>
    <text x="52" y="152" class="w5-t">teoremas · outputs · pasos etiquetados</text>
    <text x="52" y="176" class="w5-s">todo lo que produce vale por la forma de sus reglas</text>
    <path class="w5-bad" d="M280 60 C 280 14 190 14 190 58"/>
    <path class="w5-x" d="M180 20 L202 42"/><path class="w5-x" d="M202 20 L180 42"/>
    <text x="330" y="22" class="w5-kf">"SOY CONSISTENTE"</text>
    <text x="330" y="40" class="w5-s">no se demuestra desde adentro (Gödel II)</text>
    <path class="w5-ok" d="M340 125 L470 125" marker-end="url(#w5-ahok)"/>
    <rect x="476" y="60" width="180" height="130" rx="3" class="w5-bx"/>
    <text x="488" y="80" class="w5-ki">VALIDACIÓN EXTERNA</text>
    <text x="488" y="106" class="w5-t">otro sistema, o</text>
    <text x="488" y="124" class="w5-t">alguien que responde</text>
    <text x="488" y="152" class="w5-s">justificación del proceso</text>
    <text x="488" y="168" class="w5-s">e imputación (sentidos 2 y 3)</text>
    <text x="340" y="228" text-anchor="middle" class="w5-k">LA VALIDACIÓN EN EL SEGUNDO Y TERCER SENTIDO ES EXTERNA AL SISTEMA QUE PRODUCE EL RESULTADO</text>
  </svg>
  <figcaption><b>Figura 1.</b> El arco que no se cierra desde adentro. Un sistema formal no certifica su propia consistencia; la validación que importa al curso ocurre afuera.</figcaption>
</figure>

<aside class="glosa"><span class="mark">b</span> El segundo teorema no dice que el sistema sea inconsistente. Dice que, si es consistente, la fórmula que expresa esa consistencia no es demostrable en él. Puede demostrarse en un sistema más fuerte, que a su vez no demuestra la propia.</aside>

## IA y exigencia

Esta semana el modelo participa como objeto, no como herramienta: la pregunta es qué le aplica de los teoremas y qué no. Se le puede pedir que reconstruya el argumento de Lucas y que lo refute, y suele hacer ambas cosas con soltura; el estudiante debe notar que esa soltura no decide nada, porque es el mismo punto de la semana 1. La exigencia es poder explicar sin el modelo la diferencia entre verdadero y demostrable en el sistema, reconstruir el argumento gödeliano en tres premisas y decir cuál ataca Feferman, y formular con sus propias palabras la conclusión sobre validación que sobrevive cuando el argumento contra la IA no sobrevive<sup class="mark">c</sup>.

<aside class="glosa"><span class="mark">c</span> Valmeekam, Stechly y Kambhampati (2024) informan que un modelo de razonamiento resolvió casi todos los problemas de planificación con solución del conjunto PlanBench y reconocía como irresolubles solo una parte pequeña de los que no la tenían. El curso usa la cifra como ilustración de decidibilidad, no como medida definitiva; cambia con cada modelo.</aside>

## Lecturas

**Central**

- Nagel, E. y Newman, J. R. (1994). *El teorema de Gödel*. Capítulos 1 a 3 y 7. Madrid: Tecnos.
- Turing, A. M. (1950). "Computing Machinery and Intelligence". *Mind*, 59(236), 433-460. https://doi.org/10.1093/mind/LIX.236.433. Hay traducción: "Maquinaria computadora e inteligencia", en *Mentes y máquinas*, Tecnos, 1985.
- Lucas, J. R. (1961). "Minds, Machines and Gödel". *Philosophy*, 36(137), 112-127. Texto del autor: https://users.ox.ac.uk/~jrlucas/Godel/mmg.html
- Feferman, S. (2009). "Gödel, Nagel, Minds, and Machines". *The Journal of Philosophy*, 106(4), 201-219. Preprint: https://math.stanford.edu/~feferman/papers/godelnagel.pdf

**Complementaria**

- Turing, A. M. (1936). "On Computable Numbers, with an Application to the Entscheidungsproblem". *Proceedings of the London Mathematical Society*, s2-42, 230-265. https://doi.org/10.1112/plms/s2-42.1.230
- Penrose, R. (1991). *La nueva mente del emperador*. Capítulos 2 y 4. Barcelona: Grijalbo Mondadori.
- Putnam, H. (1960). "Minds and Machines". En S. Hook (ed.), *Dimensions of Mind*. Nueva York: NYU Press. Reimpreso en *Mind, Language and Reality*, Cambridge University Press, 1975.
- Chalmers, D. (1995). "Minds, Machines, and Mathematics". *Psyche*, 2(9). https://consc.net/papers/penrose.html
- Valmeekam, K., Stechly, K. y Kambhampati, S. (2024). "LLMs Still Can't Plan; Can LRMs? A Preliminary Evaluation of OpenAI's o1 on PlanBench". https://arxiv.org/abs/2409.13373
- Santaolalla, J. (2026). "¿Las máquinas pueden sentir?", minutos 41 a 55. https://www.youtube.com/watch?v=MC2DubQU32g. El video afirma que Gödel mostró que "las matemáticas no son coherentes" y que "hay contradicciones en matemáticas". Ambas afirmaciones son falsas; identificar por qué.

## Guía de lectura

- Nagel y Newman construyen todo el libro sobre la diferencia entre "verdadero" y "demostrable en el sistema". Si esa diferencia no existiera, el teorema sería una contradicción y no un resultado. *¿Puede explicar con un ejemplo propio por qué una proposición puede ser verdadera y no demostrable dentro de un sistema dado?*

- Turing responde en 1950 a la objeción matemática (sección 6.3) con un argumento que Lucas no cita diez años después. *¿Qué dice Turing, y por qué Lucas pudo creer que su argumento era nuevo?*

- Lucas presenta su argumento en pocas páginas y con mucha confianza. Reconstrúyalo en tres premisas. *¿Cuál de las tres ataca Feferman, y qué le reprocha a Nagel y Newman de paso?*

- El video de Santaolalla afirma que Gödel mostró contradicciones en las matemáticas. Es un error común y preciso. *¿Qué confunde exactamente, y qué parte del teorema habría que leer para no cometerlo?*

## Taller de la segunda hora

Debate estructurado. El grupo se divide en dos. Un equipo defiende la tesis "el teorema de Gödel muestra que la mente humana no es una máquina"; el otro la ataca. Reglas:

1. Cada intervención debe citar una premisa concreta del argumento, numerada en el tablero.
2. No vale apelar a Penrose ni a Gödel como autoridades; vale citar lo que demostraron.
3. El docente anota en el tablero qué premisas quedaron en pie y cuáles cayeron, y con qué objeción.
4. Nadie puede decir "la máquina no comprende"; la pregunta ontológica está aparcada hasta la semana 7.

| Premisa | Quién la defendió | Objeción | ¿Queda en pie? |
|---|---|---|---|
| P1. Todo sistema formal consistente tiene una verdad gödeliana que no demuestra | | | |
| P2. Un matemático humano puede ver que esa verdad es verdadera | | | |
| P3. Luego la mente no es un sistema formal | | | |

Al final, el grupo entero responde una sola pregunta: ¿qué conclusión sobre validación sobrevive, aunque el argumento contra la IA no sobreviva? La respuesta esperada es la de la Figura 1, y es mejor que el grupo la formule antes de que el docente la muestre.

## Guion de la sesión

| Momento | Docente | Estudiante | Material |
|---|---|---|---|
| 0 a 10 min | Proyecta el fragmento del video (minutos 41 a 55) y pide errores | Anota lo que cree que está mal | Video de Santaolalla |
| 10 a 35 min | Hilbert, Russell, Gödel: qué dicen y qué no dicen los teoremas | Pregunta; reconstruye la diferencia entre verdadero y demostrable | Nagel y Newman |
| 35 a 50 min | Turing 1936 y 1950 | Localiza la objeción matemática en el texto | Turing (1950), sección 6.3 |
| 50 a 55 min | Presenta las reglas del debate y asigna equipos | Se reúne con su equipo | Tabla de premisas |
| 55 a 60 min | Pausa | | |
| 60 a 75 min | Preparación por equipos | Prepara dos intervenciones con premisa citada | Lucas; Feferman |
| 75 a 105 min | Modera el debate y anota en el tablero | Interviene citando premisas | Tablero |
| 105 a 120 min | Pide la conclusión que sobrevive y muestra la Figura 1 | Formula la conclusión con sus palabras; bitácora | Figura 1; bitácora |

**Notas para el docente.** El equipo que defiende a Lucas suele rendirse demasiado pronto; conviene asignar a ese equipo los estudiantes con más formación, para que la premisa dos reciba su mejor defensa. El tablero con las premisas es lo que evita que el debate derive en opiniones sobre la conciencia. Si el grupo llega a la conclusión sobre validación externa antes de ver la Figura 1, mostrarla como confirmación y no como respuesta. No permitir que la sesión cierre con "entonces Gödel no sirve para nada": sirve exactamente para lo que la figura muestra.

## Bitácora

Las premisas que quedaron en pie y las que cayeron, con la objeción que las tumbó. La conclusión sobre validación con sus propias palabras. Una nota sobre qué afirmaba usted antes de esta semana que ahora formularía distinto, con la frase anterior y la nueva.

## Para la próxima semana

Wittgenstein, *Investigaciones filosóficas*, §§ 1 a 43 y 201 a 243. Habermas, *Conocimiento e interés*, capítulos 5 y 6 sobre Peirce. Preparar la ficha de hipótesis sobre la bitácora de la semana 3, que es la segunda entrega. La semana 6 cuenta lo que la filosofía hizo con la validación después de que el proyecto formal encontró sus límites, y cierra el argumento del curso con un grafo de doce autores.
