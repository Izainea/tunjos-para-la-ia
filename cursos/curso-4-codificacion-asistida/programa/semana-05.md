# Semana 5. Codificación axial y consultas al corpus

## Pregunta de la semana

Cuando se relacionan categorías, ¿qué diferencia hay entre una consulta al corpus que devuelve fragmentos y una respuesta del modelo que describe lo que el corpus dice?

## Por qué esta semana

<p class="lede">La codificación abierta deja categorías sueltas; la axial las relaciona. Strauss y Corbin le dieron a esa fase un instrumento, el paradigma de codificación, y una representación, la matriz condicional y consecuencial, que ordena las condiciones en que un fenómeno ocurre, lo que la gente hace frente a él y lo que resulta. Es la fase en la que el analista empieza a afirmar relaciones, y por eso es la fase en la que una propuesta del modelo puede parecer un hallazgo. Esta semana enseña a construir la matriz sobre una categoría propia y, en paralelo, a distinguir dos operaciones que la interfaz de un modelo confunde: consultar el corpus, que devuelve fragmentos verificables, y preguntarle al modelo qué dice el corpus, que devuelve una configuración sin rastro.</p>

Los programas de análisis cualitativo asistido por computador, los CAQDAS, llevan treinta años haciendo consultas: recuperar todos los fragmentos de un código, cruzar dos códigos, contar en qué fuentes aparece cada uno. Gibbs (2012) las describe con precisión. Esas consultas son deductivas y mecánicas, y por eso una máquina las ejecuta y otra máquina las verifica. Una respuesta del modelo a "qué dice el corpus sobre la confianza" no es una consulta: es una síntesis que puede ser excelente y que no se puede auditar sin rehacerla.

## Contenido de la sesión

1. La codificación axial, en Strauss y Corbin (2002), es el proceso de relacionar categorías con subcategorías a lo largo de sus propiedades y dimensiones. La regla de generación es preguntar, para cada categoría, bajo qué condiciones ocurre lo que nombra, qué acciones e interacciones se dan frente a ello y con qué consecuencias. El criterio de validez es que cada relación propuesta tenga fragmentos que la sostengan. La condición de terminación es que las categorías principales tengan sus relaciones especificadas y que los fragmentos nuevos no las alteren. La condición de imputación es la misma de siempre, ahora sobre un objeto más comprometido: afirmar una relación es afirmar más que poner un nombre.

2. El paradigma de codificación es el esquema con el que Strauss y Corbin interrogan cada categoría: condiciones causales, contexto, condiciones intervinientes, estrategias de acción e interacción y consecuencias. Glaser lo consideró el ejemplo mayor de forzamiento, como vio la semana pasada. Corbin y Strauss (2008) lo suavizaron: el paradigma es una herramienta para pensar, no un molde que haya que llenar. El curso lo usa en ese sentido y con una condición adicional: cada celda del paradigma lleva los números de los fragmentos que la sostienen, y la celda sin fragmentos se deja vacía.<sup class="mark">a</sup>

<aside class="glosa"><span class="mark">a</span> La matriz condicional, en Strauss y Corbin (1990), es un diagrama de círculos concéntricos que va del nivel internacional al de la acción individual, para situar el fenómeno en sus condiciones. La versión de 1998, condicional y consecuencial, añade que las consecuencias de la acción vuelven a ser condiciones. La mini app de la semana dibuja una versión simplificada en la que los anillos son los bloques del paradigma.</aside>

3. Un modelo construye una matriz completa en segundos, y la construye bien en el sentido de que es coherente y plausible. El problema es el que la semana 4 enseñó a ver: las relaciones plausibles son las más frecuentes en la literatura, no necesariamente las del corpus. La prueba de anclaje se aplica aquí celda por celda. Para cada condición, acción o consecuencia que el modelo proponga, se le pide los fragmentos literales que la sostienen y se verifican contra el corpus. Lo que el curso encuentra en la práctica, y que el estudiante comprobará sobre su material, es que el modelo tiende a llenar todas las celdas, y que las celdas de condiciones causales son las que con más frecuencia quedan sin anclaje: el modelo sabe que un fenómeno tiene causas y las propone aunque el corpus no hable de ellas.

4. Las consultas al corpus son la otra mitad de la semana. Gibbs (2012) describe lo que un CAQDAS hace: recuperación de todos los fragmentos de un código, búsqueda de texto, consultas de coocurrencia (fragmentos con dos códigos a la vez), de proximidad (un código cerca de otro) y matrices de código por atributo (qué códigos aparecen en qué fuentes). Todas son operaciones sobre el registro: dado el libro de códigos y las asignaciones, el resultado es único y cualquiera puede reproducirlo. En términos del curso 1 del programa, son deductivas, y por eso una máquina las verifica. El cuaderno de apoyo las implementa en unas líneas de Python sobre una tabla de fragmentos y códigos; no hace falta un programa comercial.

5. Preguntarle al modelo "qué dice el corpus sobre la confianza entre vendedores y compradores" parece la misma operación y no lo es. El modelo no recupera: configura. Lee los fragmentos que caben en su ventana, produce una síntesis con la forma de una respuesta fundamentada y, cuando cita, puede citar bien o puede componer una cita a partir de varias. Lo que devuelve puede ser mejor que lo que devolvería una consulta, porque incluye relaciones que ningún cruce de códigos mostraría. Y no se puede auditar sin rehacerla: no hay un procedimiento que, aplicado al registro, reproduzca la respuesta. Es la diferencia entre el segundo sentido de validación, la justificación del proceso, y su ausencia (Zainea, 2026).<sup class="mark">b</sup>

<aside class="glosa"><span class="mark">b</span> La diferencia no es de calidad sino de tipo. Una consulta mala es reproducible y se corrige; una síntesis buena no es reproducible y se acepta o se rechaza entera. El curso no prohíbe la segunda: exige que se registre como lo que es, una hipótesis sobre el corpus, y que se verifique con consultas antes de entrar al libro.</aside>

6. De ahí el protocolo de la semana para las consultas con modelo. Primero, la pregunta se formula como consulta y se ejecuta sobre el registro: qué fragmentos tienen tal código, cuáles tienen dos a la vez. Segundo, se le pide al modelo que lea solo esos fragmentos, numerados, y que proponga relaciones entre ellos citando el número de cada fragmento que usa. Tercero, cada relación propuesta se verifica leyendo los fragmentos citados, y la que no se sostiene se descarta con una línea en el memo. El orden importa: la consulta delimita lo que el modelo puede ver, y la cita numerada hace auditable lo que dice. Invertir el orden, es decir, preguntar primero al modelo y luego buscar fragmentos que confirmen, es la forma más común de forzamiento en la fase axial.

7. La matriz que el estudiante construye hoy sobre una categoría propia es una hipótesis de relaciones, no un resultado. Timmermans y Tavory (2012) dirían que es el momento abductivo del análisis: algo en el corpus sorprende, y la matriz propone lo que haría natural esa sorpresa. Lo que la convierte en aserción es la semana 8, cuando el estudiante la firme. Entre hoy y entonces, cada relación tiene que ganarse su lugar con fragmentos, y el modelo puede ayudar a buscarlos y no puede decidir si bastan.

<figure class="wide">
  <svg viewBox="0 0 680 310" style="width:100%;max-width:42rem;height:auto;display:block" role="img" aria-label="Dos columnas. Izquierda, consulta al corpus: libro de códigos y asignaciones entran a un procedimiento de recuperación que devuelve los fragmentos 4, 12, 19 y 33; el resultado es único, reproducible y verificable por otra máquina. Derecha, pregunta al modelo: el corpus entra a un modelo que devuelve una síntesis con forma de respuesta fundamentada; el resultado no es reproducible y se audita solo rehaciéndolo. Abajo, el protocolo del curso: consultar primero, pasar al modelo los fragmentos numerados, exigir citas por número, verificar cada relación.">
    <style>.t{font-family:var(--text);font-size:12px;fill:var(--ink)} .s{font-family:var(--text);font-size:10.5px;fill:var(--muted)} .k{font-family:var(--mono);font-size:9.5px;letter-spacing:.08em;fill:var(--muted)} .bx{fill:var(--surface);stroke:var(--rule);stroke-width:1.2} .ok{fill:var(--surface);stroke:var(--c-inv);stroke-width:1.4} .wn{fill:var(--surface);stroke:var(--accent);stroke-width:1.4} .ar{stroke:var(--muted);stroke-width:1.3;fill:none} .ah{fill:var(--muted)} .h{font-family:var(--display);font-weight:700;font-size:13px;fill:var(--ink)}</style>
    <defs><marker id="s5-ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 1L9 5L0 9z" class="ah"/></marker></defs>
    <text x="20" y="20" class="h">Consulta al corpus</text>
    <rect x="20" y="30" width="300" height="34" rx="3" class="bx"/>
    <text x="30" y="52" class="t">libro de códigos + asignaciones (registro)</text>
    <path class="ar" d="M170 64 L170 84" marker-end="url(#s5-ah)"/>
    <rect x="20" y="88" width="300" height="34" rx="3" class="bx"/>
    <text x="30" y="110" class="t">recuperar: código A ∧ código B</text>
    <path class="ar" d="M170 122 L170 142" marker-end="url(#s5-ah)"/>
    <rect x="20" y="146" width="300" height="48" rx="3" class="ok"/>
    <text x="30" y="164" class="t">fragmentos 4, 12, 19, 33</text>
    <text x="30" y="182" class="s">resultado único · reproducible · otra máquina lo verifica</text>
    <text x="360" y="20" class="h">Pregunta al modelo</text>
    <rect x="360" y="30" width="300" height="34" rx="3" class="bx"/>
    <text x="370" y="52" class="t">corpus entero (lo que cabe en la ventana)</text>
    <path class="ar" d="M510 64 L510 84" marker-end="url(#s5-ah)"/>
    <rect x="360" y="88" width="300" height="34" rx="3" class="bx"/>
    <text x="370" y="110" class="t">"¿qué dice el corpus sobre A y B?"</text>
    <path class="ar" d="M510 122 L510 142" marker-end="url(#s5-ah)"/>
    <rect x="360" y="146" width="300" height="48" rx="3" class="wn"/>
    <text x="370" y="164" class="t">síntesis con forma de respuesta fundamentada</text>
    <text x="370" y="182" class="s">no reproducible · se audita solo rehaciéndola</text>
    <path class="ar" d="M20 214 L660 214" stroke-dasharray="4 4"/>
    <text x="20" y="236" class="k">PROTOCOLO DEL CURSO</text>
    <text x="20" y="256" class="t">1. consultar primero   2. pasar al modelo solo los fragmentos recuperados, numerados</text>
    <text x="20" y="276" class="t">3. exigir que cada relación cite números   4. verificar cada cita contra el corpus</text>
    <text x="20" y="298" class="s">La consulta delimita lo que el modelo ve; la cita numerada hace auditable lo que dice.</text>
  </svg>
  <figcaption><b>Figura 5.</b> Consulta al corpus frente a pregunta al modelo. Lo que hay que ver: la primera es una operación sobre el registro y la segunda una configuración; el protocolo convierte la segunda en algo que se puede verificar con la primera.</figcaption>
</figure>

<iframe class="app" src="apps/matriz-condicional.html" title="Constructor de matriz condicional y consecuencial" loading="lazy"></iframe>

## IA y exigencia

Esta semana se le pide al modelo dos cosas separadas. Primero, que proponga el paradigma de codificación para la categoría principal del estudiante, celda por celda, citando fragmentos por número. Segundo, que lea los fragmentos devueltos por una consulta de coocurrencia y proponga relaciones entre ellos, también con citas numeradas. El estudiante debe poder, sin el modelo, ejecutar la consulta (a mano o con el cuaderno), verificar cada cita, señalar al menos una celda que el modelo llenó sin anclaje, y explicar por qué una consulta se verifica y una síntesis no.

## Lecturas

**Central**

- Strauss, A. y Corbin, J. (2002). *Bases de la investigación cualitativa*. Medellín: Universidad de Antioquia. Cap. 9, sobre la codificación axial, y cap. 12, sobre la matriz condicional y consecuencial.
- Gibbs, G. (2012). *El análisis de datos cualitativos en investigación cualitativa*. Madrid: Morata. Cap. 4, sobre codificación y categorización; caps. 8 y 9, sobre el análisis asistido por computador y las búsquedas.

**Complementaria**

- Corbin, J. y Strauss, A. (2008). *Basics of Qualitative Research*. 3.ª ed. Thousand Oaks: Sage. Cap. 5, sobre contexto y matriz condicional.
- Glaser, B. G. (1992). *Basics of Grounded Theory Analysis: Emergence vs Forcing*. Mill Valley: Sociology Press. Capítulo sobre el paradigma de codificación.
- Saldaña, J. (2021). *The Coding Manual for Qualitative Researchers*. 4.ª ed. Londres: Sage. Capítulo sobre métodos de segundo ciclo, en particular la codificación axial.
- Timmermans, S. y Tavory, I. (2012). "Theory Construction in Qualitative Research: From Grounded Theory to Abductive Analysis". *Sociological Theory* 30(3), 167-186. https://doi.org/10.1177/0735275112457914

## Guía de lectura

- Strauss y Corbin describen el paradigma como un conjunto de preguntas y advierten que no toda categoría tiene todas las respuestas. *En la matriz que el modelo propuso para su categoría, ¿quedó alguna celda vacía? Si no, ¿qué dice eso del modelo y qué del corpus?*
- En el capítulo sobre la matriz condicional y consecuencial, fíjese en la idea de que las consecuencias de hoy son condiciones de mañana. *¿Puede un modelo que no conserva memoria entre sesiones seguir esa circularidad en un corpus largo? ¿Qué registro necesitaría usted para seguirla por él?*
- Gibbs describe las consultas de los CAQDAS como operaciones que dan siempre el mismo resultado para el mismo registro. *¿Cuál de las consultas que Gibbs describe es la más útil para su categoría principal, y qué le pediría luego al modelo sobre su resultado?*
- Timmermans y Tavory sostienen que la abducción exige sorpresa. *¿Qué la sorprendió a usted en la matriz de esta semana, y qué le hizo ver que el modelo no había notado?*

## Taller de la segunda hora

Sobre la categoría propia con más fragmentos:

1. Ejecute una consulta de recuperación (todos los fragmentos de la categoría) y una de coocurrencia (la categoría con otra que sospeche relacionada). Anote los números de fragmento.
2. Pásele al modelo solo esos fragmentos, numerados, y pídale el paradigma de codificación con citas por número.
3. Verifique cada celda contra el corpus y llene la tabla.
4. Dibuje la matriz con la mini app y exporte el markdown al memo.

| Celda del paradigma | Propuesta del modelo | Fragmentos citados | ¿Se sostienen? | Decisión (acepto / corrijo / vacío) | Criterio |
|---|---|---|---|---|---|
| Condiciones causales | | | | | |
| Contexto | | | | | |
| Condiciones intervinientes | | | | | |
| Acciones e interacciones | | | | | |
| Consecuencias | | | | | |

## Guion de la sesión

| Momento | Qué hace el docente | Qué hace el estudiante | Material |
|---|---|---|---|
| 0 a 15 min | Ejecuta en vivo una consulta de coocurrencia sobre un corpus de ejemplo y luego le pregunta lo mismo al modelo; compara los dos resultados | Anota qué devolvió cada uno y qué se puede verificar | Cuaderno de apoyo, modelo en versión web |
| 15 a 40 min | Expone la codificación axial, el paradigma y la matriz (figura 5), con la prueba de anclaje celda por celda | Elige su categoría y su consulta | Figura 5 |
| 40 a 55 min | Mini app de matriz con el ejemplo cargado; discute qué celda carece de anclaje | Prueba la app con su categoría | Mini app |
| 55 a 110 min | Taller sobre la categoría propia, mesa por mesa | Consulta, pide, verifica, decide, dibuja | Tabla del taller, cuaderno |
| 110 a 120 min | Cierra con una matriz leída en voz alta y anuncia la medición de acuerdo de la semana 6 | Guarda la matriz en el memo | Bitácora |

Notas para el docente. Suele fallar que el estudiante le pasa al modelo el corpus entero en lugar de los fragmentos recuperados, y entonces no puede verificar las citas; insistir en el orden del protocolo. Suele fallar que el modelo cita números de fragmento que no corresponden al texto citado; mostrar un caso y pedir que se verifique siempre el texto, no el número. Y suele ocurrir que un estudiante sin categoría clara se bloquea en la consulta: ofrecer la consulta más simple, la recuperación de un solo código, y dejar la coocurrencia para después.

## Bitácora

La tabla del taller completa, la matriz exportada, las consultas ejecutadas con sus resultados, y una nota sobre la celda que el modelo llenó sin anclaje. Prompts literales en anexo.

## Para la próxima semana

Leer McDonald, Schoenebeck y Forte (2019) y Krippendorff (2004). Leer la guía de la práctica 6 e instalar, para quien lo quiera, el cuaderno de apoyo. Preparar treinta fragmentos del corpus con el libro de códigos preliminar: la semana 6 los codifican el estudiante y el modelo por separado y se mide el acuerdo.
