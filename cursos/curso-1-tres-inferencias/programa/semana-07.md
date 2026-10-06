# Semana 7. Qué hace un modelo de lenguaje

## Pregunta de la semana

Con la teoría de la inferencia en la mano, ¿qué hace exactamente un modelo cuando razona, y qué criterio de validación tiene?

## Por qué esta semana

<p class="lede">Hasta aquí el curso ha hablado de la máquina de manera general. Esta semana la mira de cerca: cómo predice, qué es la cadena de pensamiento, qué son los modelos de recompensa por proceso que evalúan el razonamiento paso a paso. La conclusión es precisa y se puede refutar: los modelos actuales sí tienen un criterio de evaluación de pasos, pero es extrínseco, se ancla en una respuesta final conocida de antemano; local, funciona en dominios cerrados como matemáticas y código; y estadístico, mide la probabilidad de llegar a la respuesta, no la validez del paso.</p>

Un paso inválido puede recibir etiqueta positiva. Eso ya lo vio el estudiante en la semana 2 con sus propias manos, y la mini app vuelve esta semana con una lectura nueva. Lo que falta es un criterio intrínseco al paso, invariante entre dominios y normativo; por la semana 5 se sabe que ese criterio no puede ser interno al sistema<sup class="mark">a</sup>. La semana termina con el diagnóstico en los términos del curso, agencia sin imputación, y con la tercera entrega: el registro de frontera sobre una tarea real.

<aside class="glosa"><span class="mark">a</span> Semanas 5 y 6 en una frase: un sistema no certifica su propia consistencia desde adentro, y la abducción vale porque alguien se compromete a probarla ante una comunidad. Juntas dicen que el criterio que falta se construye afuera del modelo, no adentro.</aside>

## Contenido de la sesión

1. Un modelo de lenguaje es, en una frase honesta, un sistema que calcula la distribución de probabilidad del siguiente token dado el texto anterior y elige uno<sup class="mark">b</sup>. Todo lo demás, el diálogo, la síntesis, el razonamiento, es ese cálculo repetido. Por eso el output tiene la forma del género en que fue entrenado: como el corpus está hecho de texto humano donde afirmar con autoridad es constitutivo del género, el modelo afirma con autoridad. La forma de la aserción fundamentada no es un rasgo añadido; es el rasgo del material.

2. Wei et al. (2022) muestran que pedirle al modelo pasos intermedios antes de la respuesta mejora el desempeño en tareas de aritmética, sentido común y manipulación simbólica, y que la mejora aparece con la escala. La sesión precisa qué significa eso y qué no. Los pasos son texto generado con el mismo mecanismo que la respuesta, no un registro del proceso interno; mejoran el resultado porque dan al modelo más contexto sobre el que predecir, no porque lo obliguen a razonar.

3. Lightman et al. (2023) comparan dos maneras de entrenar un verificador: por resultado, premiar la cadena entera si la respuesta final es correcta, y por proceso, premiar cada paso. Los modelos de recompensa por proceso funcionan mejor. La pregunta del curso es cómo se obtienen las etiquetas de los pasos, y la respuesta es que las puso un anotador humano según si el paso lleva hacia la respuesta correcta conocida<sup class="mark">c</sup>. La etiqueta es la probabilidad de alcanzar la respuesta, no la validez formal del paso; un paso inválido que no estorba recibe etiqueta positiva.

4. Valmeekam, Stechly y Kambhampati (2024) miden los límites. Un modelo de razonamiento resuelve casi todos los problemas de planificación con solución de un conjunto de prueba y reconoce como irresolubles solo una fracción pequeña de los que no la tienen. Reconocer que un problema no tiene solución es un problema de decidibilidad, el de Turing en la semana 5, y la cifra muestra que el modelo no lo resuelve por mirar su propio proceso.

5. El diagnóstico en los términos del curso cabe en una frase larga. La máquina ejecuta pasos con forma deductiva que no verifica como tales, generaliza inductivamente con una potencia sin precedentes, y produce candidatos de hipótesis sin que nada en ella se sorprenda, se comprometa o pague el costo de probar. Hay agencia operativa, en el sentido de Floridi de la semana 1, y no hay agente al que imputar lo producido. Agencia sin imputación.

6. Lo que sigue de ahí es una decisión de diseño, no una tesis ontológica. Si el criterio no puede ser interno, hay que construirlo afuera: un andamiaje en que cada paso del modelo lleve su procedencia y sus límites, y en que alguien identificable responda por la frontera. Es la prótesis hermenéutica de la semana 8, y el registro de frontera de la segunda hora es su versión mínima: una tabla en que el estudiante escribe, paso a paso, qué propuso la máquina y qué decidió él.

<figure class="wide">
  <svg viewBox="0 0 680 230" style="width:100%;max-width:42rem;height:auto;display:block" role="img" aria-label="Dos columnas enfrentadas. Izquierda: el criterio que los modelos tienen, extrínseco, local, estadístico. Derecha: el criterio que haría falta, intrínseco, invariante, normativo. Una flecha de la izquierda a la derecha dice: no se obtiene con más escala; se construye afuera.">
    <style>.w7-col{fill:var(--surface);stroke:var(--rule);stroke-width:1.2} .w7-h{font-family:var(--display);font-weight:700;font-size:14px;fill:var(--ink)} .w7-t{font-family:var(--text);font-size:12.5px;fill:var(--ink)} .w7-s{font-family:var(--text);font-size:11px;fill:var(--muted)} .w7-k{font-family:var(--mono);font-size:10px;letter-spacing:.08em;fill:var(--muted)} .w7-kf{font-family:var(--mono);font-size:10px;letter-spacing:.08em;fill:var(--c-fil)} .w7-ki{font-family:var(--mono);font-size:10px;letter-spacing:.08em;fill:var(--c-inv)} .w7-ar{fill:none;stroke:var(--muted);stroke-width:1.4}</style>
    <defs><marker id="w7-ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 1L9 5L0 9z" fill="var(--muted)"/></marker></defs>
    <rect x="20" y="20" width="280" height="170" rx="3" class="w7-col"/>
    <text x="32" y="40" class="w7-kf">EL CRITERIO QUE HAY</text>
    <text x="32" y="68" class="w7-h">extrínseco</text><text x="32" y="84" class="w7-s">se ancla en una respuesta final conocida</text>
    <text x="32" y="112" class="w7-h">local</text><text x="32" y="128" class="w7-s">vale donde hay respuesta única: matemáticas, código</text>
    <text x="32" y="156" class="w7-h">estadístico</text><text x="32" y="172" class="w7-s">probabilidad de llegar, no validez del paso</text>
    <rect x="380" y="20" width="280" height="170" rx="3" class="w7-col"/>
    <text x="392" y="40" class="w7-ki">EL CRITERIO QUE HARÍA FALTA</text>
    <text x="392" y="68" class="w7-h">intrínseco</text><text x="392" y="84" class="w7-s">evalúa el paso por lo que el paso hace</text>
    <text x="392" y="112" class="w7-h">invariante</text><text x="392" y="128" class="w7-s">vale igual en un dominio abierto</text>
    <text x="392" y="156" class="w7-h">normativo</text><text x="392" y="172" class="w7-s">dice si el paso es válido, no si suele funcionar</text>
    <path class="w7-ar" d="M300 105 L372 105" marker-end="url(#w7-ah)"/>
    <text x="340" y="214" text-anchor="middle" class="w7-k">NO SE OBTIENE CON MÁS ESCALA · SE CONSTRUYE AFUERA DEL SISTEMA</text>
  </svg>
  <figcaption><b>Figura 1.</b> El criterio de validación que los modelos tienen y el que haría falta. La flecha no es una promesa de progreso: por la semana 5, el segundo no puede ser interno.</figcaption>
</figure>

<iframe class="app" src="apps/verificador-pasos.html" title="Verificador de pasos: la misma cadena de la semana 2, ahora leída como etiqueta por resultado frente a validez del paso" loading="lazy"></iframe>

<aside class="glosa"><span class="mark">b</span> Un token es la unidad en que el modelo parte el texto: una palabra corta, un trozo de palabra, un signo. El modelo no elige siempre el más probable; un parámetro de temperatura regula cuánto azar admite. Nada de eso cambia el mecanismo.</aside>

<aside class="glosa"><span class="mark">c</span> El conjunto PRM800K de Lightman et al. contiene cerca de 800.000 etiquetas humanas sobre pasos de soluciones a problemas de matemáticas de competencia. Las instrucciones a los anotadores pedían marcar cada paso como positivo, negativo o neutro según su corrección y utilidad para llegar a la solución.</aside>

La diferencia entre las dos columnas de la mini app es la diferencia entre dos cosas que suelen llamarse igual.

| Etiqueta por resultado | Validez del paso |
|---|---|
| Positiva si el paso lleva hacia la respuesta correcta conocida | Positiva si el paso se sigue de los anteriores por su forma |
| Exige conocer la respuesta de antemano | No exige conocer la respuesta |
| Funciona donde hay respuesta única: matemáticas, código | Funciona en cualquier dominio donde haya reglas de inferencia |
| Es una probabilidad aprendida de anotaciones humanas | Es una norma que alguien puede exhibir y defender |
| *Mide rendimiento* | *Mide validez, y es lo que el estudiante hizo en la semana 2* |

## IA y exigencia

Esta semana el modelo ejecuta una tarea real del proyecto del estudiante, codificar diez fragmentos, sintetizar tres fuentes o categorizar un listado, y lo hace en tres rondas: propone, recibe las decisiones del estudiante, continúa. La exigencia es el registro de frontera: para cada paso del modelo, qué propuso, qué inferencia es, qué decidió el estudiante, con qué criterio, quién responde si está mal. Sin el modelo, el estudiante debe poder explicar qué es la cadena de pensamiento y por qué no es un registro del proceso, cómo se etiquetan los pasos en un modelo de recompensa por proceso y por qué esa etiqueta no es validez, y en qué consiste el diagnóstico de agencia sin imputación. Lo que no debe hacer es concluir que el modelo no comprende: el curso no lo afirma y no lo necesita.

## Lecturas

**Central**

- Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E., Le, Q. y Zhou, D. (2022). "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models". *Advances in Neural Information Processing Systems*, 35. https://arxiv.org/abs/2201.11903
- Lightman, H., Kosaraju, V., Burda, Y., Edwards, H., Baker, B., Lee, T., Leike, J., Schulman, J., Sutskever, I. y Cobbe, K. (2023). "Let's Verify Step by Step". https://arxiv.org/abs/2305.20050
- Valmeekam, K., Stechly, K. y Kambhampati, S. (2024). "LLMs Still Can't Plan; Can LRMs? A Preliminary Evaluation of OpenAI's o1 on PlanBench". https://arxiv.org/abs/2409.13373
- Zainea, C. I. (2026). *Agencia sin imputación. Hermenéutica, pragmática y la validación epistémica del discurso artificial*. Secciones 1 a 3. https://izainea.github.io/escritos/agencia-sin-imputacion.pdf

**Complementaria**

- Kambhampati, S. (2024). "Can Large Language Models Reason and Plan?". *Annals of the New York Academy of Sciences*, 1534(1), 15-18. https://doi.org/10.1111/nyas.15125
- Bender, E. M. y Koller, A. (2020). "Climbing towards NLU: On Meaning, Form, and Understanding in the Age of Data". *Proceedings of ACL 2020*. https://aclanthology.org/2020.acl-main.463/
- Floridi, L. y Sanders, J. W. (2004). "On the Morality of Artificial Agents". *Minds and Machines*, 14, 349-379. https://doi.org/10.1023/B:MIND.0000035461.63578.9d
- Zainea, C. I. (2026). "Agencia sin imputación: por qué «la máquina no comprende» no cierra la discusión". https://izainea.github.io/blog/agencia-sin-imputacion/

## Guía de lectura

- Wei et al. informan mejoras grandes en aritmética y manipulación simbólica y mejoras menores o nulas en otras tareas. Las que mejoran tienen respuesta única y pasos verificables. *¿Qué tienen en común las tareas que mejoran, y qué dice eso sobre dónde funciona la cadena de pensamiento y dónde no?*

- Lightman et al. describen cómo se construyó el conjunto de etiquetas de pasos. Alguien decidió que un paso era bueno, y ese alguien tenía la respuesta. *¿Quién decide que un paso es bueno, con qué criterio, y qué pasaría con el verificador en una tarea sin respuesta conocida?*

- Valmeekam et al. dan una cifra de problemas irresolubles reconocidos. La cifra es pequeña y cambiará con cada modelo nuevo. *¿Qué relación tiene esa cifra con el problema de la parada, y por qué la relación no desaparece si la cifra sube?*

- Zainea distingue tres sentidos de validación y tres adjetivos del criterio actual, extrínseco, local y estadístico. Pueden leerse como tres defectos independientes o como uno solo visto de tres lados. *¿Está de acuerdo con que sean tres y no uno, y cuál de los tres le parece más difícil de corregir desde afuera?*

## Taller de la segunda hora

Práctica guiada. Guía completa en [practicas/practica-07-registro-de-frontera.md](../practicas/practica-07-registro-de-frontera.md). En resumen: el estudiante usa un modelo para una tarea real de su proyecto, codificar diez fragmentos, resumir tres fuentes o proponer categorías para un listado, en tres rondas: la máquina propone, el investigador decide, segunda vuelta con lo decidido. Durante la tarea mantiene el registro de frontera:

| Paso | Qué propuso el modelo | Tipo de inferencia | Qué decidí yo | Criterio de mi decisión | ¿Quién responde si está mal? |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |

El registro no es un informe de uso: es la evidencia de que el estudiante sabe dónde termina la máquina y dónde empieza él. Las filas más valiosas son las difíciles, donde la distinción entre lo propuesto y lo decidido no es clara, y las aceptaciones acríticas, donde el estudiante aceptó sin un criterio que pueda nombrar. No se borran: se anotan. Plantilla en [plantillas/registro-de-frontera.md](../plantillas/registro-de-frontera.md).

## Guion de la sesión

| Momento | Docente | Estudiante | Material |
|---|---|---|---|
| 0 a 15 min | Predicción del siguiente token y la forma de la aserción | Relee un output de la semana 1 con esa clave | Bitácora de la semana 1 |
| 15 a 30 min | Cadena de pensamiento y modelos de recompensa por proceso | Vuelve a la mini app y lee la columna de etiquetas | Mini app verificador; Lightman et al. |
| 30 a 45 min | Valmeekam et al. y la decidibilidad; Figura 1 | Discute si la flecha de la figura es una promesa | Figura 1 |
| 45 a 55 min | El diagnóstico: agencia sin imputación | Formula el diagnóstico con sus palabras | Zainea, secciones 1 a 3 |
| 55 a 60 min | Pausa | | |
| 60 a 75 min | Ronda 1: la máquina propone | Ejecuta la tarea y copia el output literal | Guía de la práctica 7 |
| 75 a 95 min | Ronda 2: el investigador decide | Llena las columnas de inferencia, decisión y criterio | Plantilla del registro |
| 95 a 110 min | Ronda 3: segunda vuelta | Devuelve sus decisiones al modelo y registra | Modelo en versión web |
| 110 a 120 min | Recoge un caso difícil y una aceptación acrítica | Expone el suyo; anota la bitácora | Registros |

**Notas para el docente.** La sesión tiene demasiado contenido para una hora si se intenta explicar la arquitectura de los modelos; la frase honesta del punto 1 basta, y el detalle técnico va al cuaderno de apoyo. En la práctica, la ronda 2 debe hacerse antes de volver al modelo; si el estudiante pide la segunda vuelta sin haber decidido, el registro queda vacío de criterio. La columna "quién responde" se llena casi siempre con "yo" sin pensar; pedir, al menos en dos filas, ante quién y con qué base. Un registro en que el modelo lo hizo mal y el estudiante lo detectó vale más que uno en que el modelo lo hizo bien y el estudiante lo aceptó.

## Entrega

Registro de frontera completo sobre una tarea real, con el anexo de prompts y outputs literales. Se evalúa la precisión de la distinción, no el éxito de la tarea. La rúbrica está en [evaluacion.md](evaluacion.md).

## Para la próxima semana

Zainea (2026), sección sobre la prótesis hermenéutica, y la entrada del blog correspondiente. Vallor (2024), capítulo 4. Terminar el mapa inferencial final con las correcciones a la versión preliminar y preparar una presentación de ocho minutos. La semana 8 convierte el diagnóstico en un diseño y pone el mapa a prueba ante pares.
