# Semana 2. Deducción: la historia de la validación formal

## Pregunta de la semana

¿Qué hace válida una deducción, y por qué eso es exactamente lo que una máquina puede verificar?

## Por qué esta semana

<p class="lede">La deducción es la inferencia mejor entendida y la menos útil para descubrir algo. Va de lo general a lo particular y no añade información: la conclusión ya estaba en las premisas. Tiene, en cambio, una propiedad que ninguna otra inferencia tiene. Su validez es formal, se comprueba paso a paso sin saber de qué hablan las premisas, y por eso es el primer sentido de validación de la semana anterior, la corrección, en su versión más pura. Esa propiedad hizo soñar con una ciencia por completo formalizada y es la que hoy hace que un verificador de pasos funcione en matemáticas y en código.</p>

La semana cuenta la historia de ese sueño, de Aristóteles al Círculo de Viena, porque es la historia de cómo la filosofía identificó validación con corrección formal<sup class="mark">a</sup>. La semana 5 mostrará dónde se rompió desde adentro y la semana 6 qué vino después. Aquí importa entender qué se ganó: un criterio que no depende de quién razona. Una máquina puede aplicarlo, y la segunda hora pone al estudiante a aplicarlo sobre una cadena producida por un modelo.

<aside class="glosa"><span class="mark">a</span> Semana 1 en una frase: validar un resultado puede significar que es correcto, que su proceso puede exhibirse o que alguien responde por él. La deducción es el caso en que los dos primeros sentidos coinciden: exhibir el proceso es demostrar la corrección.</aside>

## Contenido de la sesión

1. Aristóteles descubre en los *Analíticos primeros* que la validez de un argumento no depende de lo que dice sino de cómo está armado. Todos los hombres son mortales, Sócrates es hombre, luego Sócrates es mortal. Si se cambian los términos y se conserva la forma, la conclusión sigue siendo necesaria; si se cambia la forma, deja de serlo aunque los términos sean verdaderos. Ese descubrimiento es el que hace posible verificar sin comprender, y el curso volverá a él en la semana 4 cuando Peirce gire el mismo silogismo.

2. Frege, en la *Conceptografía* de 1879, construye un lenguaje en que el pensamiento se escribe sin ambigüedad y la inferencia se comprueba sobre la escritura<sup class="mark">b</sup>. La distinción entre sentido y referencia (1892) separa lo que una expresión significa de aquello que designa, y permite que dos expresiones con distinto sentido tengan el mismo valor de verdad. Con Frege la validez deja de ser una propiedad del razonamiento de alguien y pasa a ser una propiedad de las fórmulas.

3. Russell lleva ese programa a su forma más ambiciosa y encuentra su primera grieta. Con Whitehead intenta derivar la matemática de la lógica en los *Principia Mathematica*; antes, en 1901, descubre que el conjunto de todos los conjuntos que no se contienen a sí mismos no puede existir sin contradicción. El atomismo lógico, que el estudiante lee en el capítulo VII de *Los problemas de la filosofía*, da la imagen de fondo: el mundo como hechos y el lenguaje como su espejo, y los principios generales de la inferencia como algo que se conoce sin necesidad de experiencia.

4. El *Tractatus* lleva la imagen al límite. Las proposiciones son figuras de hechos, y entre ellas hay un caso extremo: la tautología, que es verdadera para cualquier estado del mundo y por eso no dice nada sobre él (4.46 a 4.4661). Toda deducción válida es una tautología. El precio de la validez formal queda a la vista: lo que es válido por su forma no informa, y lo que informa no es válido solo por su forma. De lo que no se puede hablar, hay que callar; el segundo Wittgenstein volverá en la semana 6 sobre todo lo que ese silencio dejó fuera.

5. El Círculo de Viena convierte el *Tractatus* en programa. Una proposición significa lo que la verificaría; la filosofía es análisis lógico del lenguaje de la ciencia; lo que no se verifica no es falso sino sin sentido. El proyecto es coherente y deja fuera exactamente lo que el curso necesitará: las prácticas, los compromisos y las comunidades que sostienen una afirmación cuando no hay forma que la valide.

6. Un modelo de lenguaje que resuelve un problema paso a paso produce una cadena de enunciados con forma deductiva. Cada paso parece seguirse del anterior. La pregunta de la segunda hora es si se sigue, y la única manera de responderla es verificar cada paso sin mirar la conclusión. El estudiante descubrirá que un paso inválido puede convivir con una respuesta correcta, y esa observación, hecha con las propias manos, es la que la semana 7 explicará.

<figure class="wide">
  <svg viewBox="0 0 680 150" style="width:100%;max-width:42rem;height:auto;display:block" role="img" aria-label="Cadena de cinco pasos de un modelo. El paso 3 está tachado como inválido, pero la flecha llega igual a una respuesta correcta porque los pasos 4 y 5 no dependen de él.">
    <style>.w2-bx{fill:var(--surface);stroke:var(--rule);stroke-width:1.2} .w2-bad{stroke:var(--c-fil);stroke-width:1.6} .w2-t{font-family:var(--mono);font-size:11px;fill:var(--ink)} .w2-s{font-family:var(--text);font-size:11.5px;fill:var(--muted)} .w2-k{font-family:var(--mono);font-size:10px;letter-spacing:.08em;fill:var(--muted)} .w2-ar{stroke:var(--muted);stroke-width:1.3;fill:none} .w2-x{stroke:var(--c-fil);stroke-width:2.2} .w2-ok{font-family:var(--text);font-size:13px;fill:var(--c-inv)}</style>
    <defs><marker id="w2-ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 1L9 5L0 9z" fill="var(--muted)"/></marker></defs>
    <g><rect x="10" y="30" width="90" height="44" rx="3" class="w2-bx"/><text x="55" y="56" text-anchor="middle" class="w2-t">paso 1</text></g>
    <path class="w2-ar" d="M100 52 L124 52" marker-end="url(#w2-ah)"/>
    <g><rect x="128" y="30" width="90" height="44" rx="3" class="w2-bx"/><text x="173" y="56" text-anchor="middle" class="w2-t">paso 2</text></g>
    <path class="w2-ar" d="M218 52 L242 52" marker-end="url(#w2-ah)"/>
    <g><rect x="246" y="30" width="90" height="44" rx="3" class="w2-bx w2-bad"/><text x="291" y="56" text-anchor="middle" class="w2-t">paso 3</text><path class="w2-x" d="M256 36 L326 68"/><path class="w2-x" d="M326 36 L256 68"/></g>
    <path class="w2-ar" d="M218 44 C 290 6 350 6 362 44" marker-end="url(#w2-ah)"/>
    <g><rect x="364" y="30" width="90" height="44" rx="3" class="w2-bx"/><text x="409" y="56" text-anchor="middle" class="w2-t">paso 4</text></g>
    <path class="w2-ar" d="M454 52 L478 52" marker-end="url(#w2-ah)"/>
    <g><rect x="482" y="30" width="90" height="44" rx="3" class="w2-bx"/><text x="527" y="56" text-anchor="middle" class="w2-t">paso 5</text></g>
    <path class="w2-ar" d="M572 52 L596 52" marker-end="url(#w2-ah)"/>
    <text x="604" y="56" class="w2-ok">respuesta ✓</text>
    <text x="291" y="98" text-anchor="middle" class="w2-s">inválido y no usado</text>
    <text x="340" y="130" text-anchor="middle" class="w2-k">LA RESPUESTA ES CORRECTA; LA CADENA NO ES VÁLIDA</text>
  </svg>
  <figcaption><b>Figura 1.</b> Un paso inválido dentro de una cadena que llega a la respuesta correcta. Verificar la respuesta no verifica la cadena.</figcaption>
</figure>

<iframe class="app" src="apps/verificador-pasos.html" title="Verificador de pasos: marcar válido o inválido cada paso de una cadena de un modelo y compararlo con la etiqueta por resultado" loading="lazy"></iframe>

<aside class="glosa"><span class="mark">b</span> <i>Begriffsschrift</i>, "escritura conceptual". Frege la presenta como un lenguaje de fórmulas para el pensamiento puro, modelado sobre el de la aritmética. Es la primera lógica de predicados con cuantificadores.</aside>

La diferencia que la sesión persigue cabe en dos columnas. Lo que se gana con la validez formal se paga en información, y la tabla deja a la vista el precio.

| Validez formal | Validez material |
|---|---|
| Se comprueba por la forma, sin saber de qué hablan las premisas | Depende de que las premisas sean verdaderas y de que la regla aplique al caso |
| Cualquiera puede verificarla, incluida una máquina | Exige conocimiento del tema, del contexto o de la práctica |
| No añade información: la conclusión estaba en las premisas | Añade información y por eso puede fallar |
| *Es el primer sentido de validación en estado puro* | *Es donde empieza lo que el curso llamará frontera* |

## IA y exigencia

Esta semana el modelo hace el trabajo que parece más propio de él: razonar paso a paso. Se le pide un problema con varias etapas y una cadena numerada. La exigencia para el estudiante es verificar cada paso por su forma, sin mirar la conclusión y sin volver a preguntarle al modelo, y decir al final qué parte de esa verificación habría podido hacer una máquina y qué parte necesitó que él supiera del tema<sup class="mark">c</sup>. El estudiante debe poder explicar sin la máquina por qué un paso es válido o no lo es; si solo puede decir que la respuesta es correcta, no ha verificado nada todavía.

<aside class="glosa"><span class="mark">c</span> Verificar que 8 menos 5 es 3 no exige saber de entrevistas. Verificar que "mencionó policía sin mencionar miedo" es un conjunto distinto de "mencionó solo miedo" exige leer el enunciado con cuidado, y eso ya no es forma pura.</aside>

## Lecturas

**Central**

- Russell, B. (1970). *Los problemas de la filosofía*. Capítulo VII, "Sobre nuestro conocimiento de los principios generales". Barcelona: Labor. Original en inglés de dominio público: https://www.gutenberg.org/ebooks/5827
- Wittgenstein, L. (2012). *Tractatus logico-philosophicus*. Proposiciones 4 a 4.5. Madrid: Alianza. Original en alemán e inglés de dominio público: https://www.gutenberg.org/ebooks/5740

**Complementaria**

- Frege, G. (1984). "Sobre sentido y referencia" (1892). En *Estudios sobre semántica*. Barcelona: Ariel.
- Aristóteles (1988). *Analíticos primeros*, libro I, capítulos 1 a 7. En *Tratados de lógica (Órganon) II*. Madrid: Gredos.
- Santaolalla, J. (2026). "¿Las máquinas pueden sentir?". Date un Vlog, minutos 8 a 28 (Comte, Frege, Russell, Wittgenstein, Círculo de Viena). https://www.youtube.com/watch?v=MC2DubQU32g. Introducción narrativa; el curso corrige varias de sus afirmaciones en la semana 5.

## Guía de lectura

- Russell distingue el conocimiento de principios generales del conocimiento de hechos particulares, y sostiene que la certeza de que si *p* implica *q* y *p*, entonces *q*, no viene de la experiencia. Es la misma certeza que un verificador mecánico aplica. *¿De dónde viene, según Russell, esa certeza, y qué pasaría con el verificador si Russell estuviera equivocado?*

- El *Tractatus* dice en 4.461 que la tautología no dice nada, y en 4.4661 que sin embargo no carece de sentido, porque es parte del simbolismo. Toda deducción válida es una tautología. *¿Por qué es válida una proposición que no dice nada sobre el mundo, y qué nos dice eso sobre el precio de la validez formal?*

- Frege separa el sentido de la referencia con el ejemplo del lucero de la mañana y el lucero de la tarde. Un modelo de lenguaje opera sobre sentidos, es decir, sobre cómo se dicen las cosas, no sobre referencias. *¿Qué implicaría para la verificación de un paso que la máquina trabaje solo con sentidos?*

## Taller de la segunda hora

Se le pide a un modelo que resuelva un problema con razonamiento paso a paso. Puede ser un problema lógico, un cálculo con varias etapas o una inferencia jurídica sencilla; el cuaderno de apoyo trae uno de conteo listo. El estudiante:

1. Numera cada paso de la cadena tal como el modelo la escribió, sin corregirla.
2. Marca si el paso es deductivo, es decir, si se sigue de los anteriores por su forma, o si introduce algo que no estaba.
3. Verifica cada paso deductivo sin mirar la conclusión. Tapa la última línea si hace falta.
4. Registra si la conclusión es correcta y si algún paso incorrecto condujo a una conclusión correcta.
5. Repite el ejercicio con la mini app de la semana sobre una cadena preparada, y compara la columna de validez con la columna de etiqueta por resultado.

| Paso | Texto del modelo | ¿Deductivo? | ¿Válido? | ¿Se usa después? |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |

El último punto es el que importa. Un paso inválido puede llevar a una respuesta correcta, sea porque no se usa, sea porque otro error lo compensa. Eso anticipa la semana 7: los verificadores de proceso de los modelos etiquetan los pasos por la probabilidad de llegar a la respuesta, no por su validez.

## Guion de la sesión

| Momento | Docente | Estudiante | Material |
|---|---|---|---|
| 0 a 10 min | Recoge los ejemplos de razonamiento válido e inútil traídos de casa | Lee uno en voz alta | Ejemplos de los estudiantes |
| 10 a 40 min | Recorre Aristóteles, Frege, Russell, Tractatus y Círculo de Viena con un solo silogismo como hilo | Sigue el silogismo en el tablero y propone cambios de términos | Tablero; Tractatus 4.46 a 4.4661 |
| 40 a 55 min | Presenta la Figura 1 y plantea la pregunta de la segunda hora | Discute si verificar la respuesta verifica la cadena | Figura 1 |
| 55 a 60 min | Pausa | | |
| 60 a 85 min | Acompaña la obtención de la cadena y su numeración | Pide la cadena al modelo y la numera | Modelo en versión web; tabla del taller |
| 85 a 105 min | Acompaña la verificación paso a paso | Verifica sin mirar la conclusión; usa la mini app | Mini app verificador de pasos |
| 105 a 120 min | Recoge los casos de paso inválido con respuesta correcta | Cuenta su caso; anota la bitácora | Bitácora |

**Notas para el docente.** El riesgo de la primera hora es convertirla en historia de la filosofía; cada autor debe entrar por lo que aporta a un solo problema, qué hace válida una deducción, y salir en cuanto lo aportó. En el taller, la mitad de los estudiantes verifica mirando la conclusión y luego racionaliza los pasos; pedirles que tapen la última línea del output antes de empezar. Si el modelo produce una cadena sin ningún paso inválido, lo que ocurre con problemas fáciles, la mini app garantiza que todos vean al menos un caso.

## Bitácora

La cadena numerada con sus marcas y la tabla completa. Una reflexión de un párrafo: qué parte de la verificación habría podido hacer una máquina y qué parte necesitó que usted supiera del tema. Si encontró un paso inválido con respuesta correcta, descríbalo; si no, diga por qué cree que no apareció.

## Para la próxima semana

Hume, *Investigación sobre el entendimiento humano*, sección IV; Goodman, *Hecho, ficción y pronóstico*, capítulo III; Chollet (2019), secciones I y II. Traer un ejemplo de una regularidad en la que confía y que no puede justificar sin circularidad. La semana 3 trata la inducción, que sí añade conocimiento y por eso no puede verificarse por su forma.
