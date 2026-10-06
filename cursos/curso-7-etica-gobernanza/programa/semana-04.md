# Semana 4. Exterioridad

## Pregunta de la semana

Cuando un modelo entrenado en otra parte lee un archivo producido aquí, ¿con qué precomprensión lo lee, y qué le pasa a lo que esa precomprensión no contiene?

## Por qué esta semana

<p class="lede">Es la semana central del curso y abre el segundo frente. Hasta aquí los daños eran daños a personas con derechos. Ahora el daño es a un sentido. Un modelo de lenguaje predice desde un corpus que sobrerrepresenta unas lenguas, unas regiones y unas formas de vida, y cuando lee material producido en otra parte lo hace con esa precomprensión. No se equivoca en los datos: aplana. Donde había una práctica local pone una categoría general; donde había una expresión con historia pone una paráfrasis neutra; donde había algo que no sabe nombrar, no pone nada y no avisa. Esta semana da nombre a ese fenómeno con tres fuentes: la injusticia hermenéutica de Fricker, la injusticia epistémica algorítmica de Kay, Kasirzadeh y Mohamed, y la matriz colonial de Muldoon y Wu. Y lo sitúa en el marco del programa: la prefiguración ajena como segunda especie de infortunio.</p>

En [*Validación del razonamiento con IA en ciencias sociales*, semana 8](../../curso-1-tres-inferencias/programa/semana-08.md), el curso de fundamentos del programa, se leyó el trabajo con modelos con la triple mímesis de *Tiempo y narración* (Ricœur, 1995): la prefiguración del mundo práctico, la configuración de la trama y la refiguración, cuando la obra vuelve al mundo del lector y lo transforma. Allí se sostuvo que el modelo habita la configuración sin refigurar, porque los otros dos momentos exigen un mundo y un sujeto, y se propuso la prótesis hermenéutica: un andamiaje en que la máquina configura, el investigador valida y la frontera entre ambos es auditable. Esta semana mira el otro extremo del arco, la prefiguración, y muestra que también ahí el arco se trunca.

## Contenido de la sesión

1. En *Tiempo y narración* (Ricœur, 1995) la prefiguración, Mímesis I, es la precomprensión del mundo práctico que toda configuración supone: la red de conceptos, símbolos y temporalidades con que una comunidad ya entiende su acción antes de narrarla. La tesis del docente es que la prefiguración de un modelo es su corpus de entrenamiento, y que ese corpus no coincide con el acervo de la comunidad cuyo material interpreta (Zainea, 2026). De ahí una segunda especie de infortunio, distinta del de autoridad: el acto se ejecuta sobre condiciones de fondo ajenas, y su resultado no es un error factual sino una imposición hermenéutica que ninguna validación por corrección detecta<sup class="mark">a</sup>. Conviene distinguir aquí lo que es exposición de Ricœur y lo que es tesis del programa: Ricœur no escribió sobre modelos; la lectura de la prefiguración como corpus es del docente, y el curso la propone como hipótesis de trabajo.

<aside class="glosa"><span class="mark">a</span> El anteproyecto doctoral del docente (Zainea, 2026) lo llama infortunio de prefiguración y lo enlaza con la injusticia hermenéutica: los recursos interpretativos colectivos de Fricker se leen como Mímesis I. Hasta donde el rastreo alcanza, nadie había articulado ambas nociones.</aside>

2. Fricker (2007) llama injusticia hermenéutica a la situación en que los recursos interpretativos colectivos carecen de los conceptos necesarios para que alguien dé sentido a una experiencia propia, y esa carencia no es casual: resulta de que el grupo afectado ha tenido menos parte en la producción de esos recursos<sup class="mark">b</sup>. Su ejemplo es el acoso sexual antes de que existiera la expresión: quien lo sufría no tenía con qué nombrarlo, y quien lo ejercía tampoco tenía con qué reconocerlo. Fricker expone una injusticia entre personas y grupos; el curso la extiende a un instrumento. La extensión es esta: cuando el archivo situado se lee con los recursos de otro acervo, los conceptos que faltan no faltan en la comunidad, que los tiene, sino en el lector, y la lectura resultante los borra.

<aside class="glosa"><span class="mark">b</span> Fricker, M. (2007). *Epistemic Injustice: Power and the Ethics of Knowing*. Oxford University Press. El capítulo 7, "Hermeneutical Injustice", desarrolla el concepto; los anteriores tratan la injusticia testimonial, que ocurre cuando se descuenta la credibilidad de alguien por prejuicio.</aside>

3. Kay, Kasirzadeh y Mohamed (2024) llevan la noción a la IA generativa y la llaman injusticia epistémica algorítmica generativa. Distinguen cuatro dimensiones: injusticia testimonial amplificada, cuando el sistema reproduce a escala el descuento de credibilidad; injusticia testimonial manipulativa, cuando produce contenido que degrada la confianza en fuentes legítimas; ignorancia hermenéutica, cuando sus recursos interpretativos no cubren la experiencia de ciertos grupos; e injusticia de acceso, cuando el beneficio del sistema se distribuye de forma desigual. Para un investigador la tercera es la que opera en su flujo: el modelo no tiene con qué entender una parte del material y produce de todos modos una lectura con forma de lectura completa.

4. Muldoon y Wu (2023) sitúan el fenómeno en una escala mayor con la matriz colonial del poder de Quijano: la IA como ensamblaje sociotécnico que extrae datos y trabajo del sur global, concentra el diseño en el norte y devuelve categorías que presentan como universales las de quien diseñó<sup class="mark">c</sup>. El curso toma de ahí una pregunta y no una conclusión. La pregunta es qué excluye un andamiaje diseñado desde una tradición y operado por modelos entrenados sobre otra. Dussel (1974) le da un nombre a esa pregunta: pensar desde la exterioridad, desde lo que queda fuera de una totalidad, y por eso el curso llama exterioridad a este frente.

<aside class="glosa"><span class="mark">c</span> Muldoon, J. y Wu, B. A. (2023). "Artificial Intelligence in the Colonial Matrix of Power". *Philosophy & Technology* 36(4), artículo 80. El artículo discute además la decolonialidad como programa para la IA y sus límites; el curso no lo sigue hasta ahí.</aside>

5. La evidencia empírica muestra dónde falla la lectura. Schneider, Holtermann, Biemann y Lauscher (2025) evaluaron modelos multimodales sobre conocimiento cultural de 144 países y encontraron que aciertan el origen regional amplio de una imagen o un texto y fallan en la comprensión matizada, sobre todo de la cultura intangible: rituales, prácticas, significados locales. Pouget et al. (2024) mostraron que la brecha es invisible para las métricas habituales porque esas métricas se construyen sobre datos del mismo origen que los modelos. Lo que la semana 1 ilustró con el altar y la botella de aguardiente tiene detrás una medida: el modelo describe bien el objeto y mal lo que el objeto hace en la vida de quien lo puso ahí.

<figure class="wide">
  <svg viewBox="0 0 680 270" style="width:100%;max-width:42rem;height:auto;display:block" role="img" aria-label="Arco de la triple mímesis aplicado a un modelo. Mímesis I, prefiguración: en el modelo es su corpus de entrenamiento, ajeno al archivo; marcado como ajena. Mímesis II, configuración: el modelo la ejecuta con competencia. Mímesis III, refiguración: no hay mundo al cual retornar; marcada como ausente. Debajo, el archivo situado con su propia prefiguración, que el modelo no comparte.">
    <style>.f4-h{font-family:var(--display);font-weight:700;font-size:14px;fill:var(--ink)} .f4-d{font-family:var(--text);font-size:11.5px;fill:var(--muted)} .f4-k{font-family:var(--mono);font-size:10px;letter-spacing:.08em;fill:var(--muted)} .f4-kf{font-family:var(--mono);font-size:10px;letter-spacing:.08em;fill:var(--c-fil)} .f4-ki{font-family:var(--mono);font-size:10px;letter-spacing:.08em;fill:var(--c-inv)} .f4-bx{fill:var(--surface);stroke:var(--rule);stroke-width:1.2} .f4-bf{fill:var(--surface);stroke:var(--c-fil);stroke-width:1.6;stroke-dasharray:6 4} .f4-arc{stroke:var(--muted);stroke-width:1.3;fill:none} .f4-x{stroke:var(--c-fil);stroke-width:2}</style>
    <path class="f4-arc" d="M110 70 C 250 10 430 10 570 70"/>
    <rect x="20" y="70" width="190" height="80" rx="3" class="f4-bf"/>
    <text x="32" y="90" class="f4-kf">MÍMESIS I · AJENA</text>
    <text x="32" y="112" class="f4-h">Prefiguración</text>
    <text x="32" y="130" class="f4-d">el corpus de entrenamiento</text>
    <text x="32" y="144" class="f4-d">no es el acervo del archivo</text>
    <rect x="245" y="70" width="190" height="80" rx="3" class="f4-bx"/>
    <text x="257" y="90" class="f4-ki">MÍMESIS II · COMPETENTE</text>
    <text x="257" y="112" class="f4-h">Configuración</text>
    <text x="257" y="130" class="f4-d">describe, categoriza, resume</text>
    <text x="257" y="144" class="f4-d">con forma de lectura completa</text>
    <rect x="470" y="70" width="190" height="80" rx="3" class="f4-bf"/>
    <text x="482" y="90" class="f4-kf">MÍMESIS III · AUSENTE</text>
    <text x="482" y="112" class="f4-h">Refiguración</text>
    <text x="482" y="130" class="f4-d">no hay mundo al cual volver</text>
    <text x="482" y="144" class="f4-d">ni sujeto que responda</text>
    <path class="f4-x" d="M95 160 L125 190"/>
    <path class="f4-x" d="M125 160 L95 190"/>
    <rect x="20" y="200" width="640" height="55" rx="3" class="f4-bx"/>
    <text x="32" y="220" class="f4-k">EL ARCHIVO SITUADO Y SU PROPIA PREFIGURACIÓN</text>
    <text x="32" y="242" class="f4-d">expresiones, objetos, escenas con historia local · lo que el modelo lee con otra precomprensión y aplana sin avisar</text>
  </svg>
  <figcaption><b>Figura 4.</b> La prefiguración ajena en el arco de la mímesis. El modelo configura con competencia entre dos extremos truncados; el de la izquierda es el que esta semana examina.</figcaption>
</figure>

6. Lo culturalmente codificado es el caso límite y por eso es el caso de prueba. Una expresión regional, un objeto de devoción popular, un gesto en una fotografía, una escena cuya violencia se lee por lo que falta y no por lo que se ve, son piezas en las que el sentido depende de participar en la forma de vida que las produjo. En [*Validación del razonamiento con IA en ciencias sociales*, semana 6](../../curso-1-tres-inferencias/programa/semana-06.md) se leyó al segundo Wittgenstein, para quien el significado es un uso dentro de un juego de lenguaje y los juegos de lenguaje viven en formas de vida, y se concluyó que la validez de una hipótesis no está en su forma ni en su frecuencia sino en que alguien se compromete con ella ante una comunidad. De ahí sale la pregunta de fondo de esta semana: qué significa usar un lenguaje sin participar en la forma de vida que lo sostiene. Esta semana la vuelve operativa. Si el modelo aplana justo ahí, entonces ahí es donde hay que medir, y la semana 5 enseña cómo.

| Error factual | Imposición hermenéutica |
|---|---|
| El modelo afirma algo falso sobre la pieza | El modelo afirma algo verdadero en sus términos y falso en los de la comunidad |
| Se detecta comparando con la pieza | Se detecta comparando con un lector que conoce el contexto |
| Lo mide una tasa de acierto | Ninguna tasa de acierto lo ve, porque la referencia se construyó con el mismo acervo |
| Se corrige con más datos del mismo tipo | Se corrige cambiando quién lee y con qué categorías |
| *Validación en el primer sentido* | *Validación en el segundo y el tercer sentido: proceso e imputación* |

7. La distinción entre exposición y tesis importa aquí más que en ninguna otra semana. Fricker, Kay y sus coautores, Muldoon y Wu describen injusticias; ninguno de ellos propone el instrumento de la semana 5. La articulación entre injusticia hermenéutica y mímesis es del docente, y la auditoría de exterioridad es una propuesta del curso que el estudiante debe poder criticar, no solo aplicar.

## IA y exigencia

Esta semana se le pide al modelo que lea las tres piezas cargadas de sentido local que el estudiante trajo y que diga qué significan. El estudiante debe poder, sin el modelo, decir para cada pieza qué entendió mal, qué aplanó y qué ignoró, y explicar por qué esa diferencia no es un error factual sino una lectura desde otra precomprensión. Esa triple pregunta es el núcleo de la auditoría de la próxima semana.

## Lecturas

**Central**

- Fricker, M. (2007). *Epistemic Injustice: Power and the Ethics of Knowing*. Oxford University Press. Capítulo 7.
- Kay, J., Kasirzadeh, A. y Mohamed, S. (2024). "Epistemic Injustice in Generative AI". *Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society* 7(1), 684-697. https://doi.org/10.1609/aies.v7i1.31671 (versión abierta: https://arxiv.org/abs/2408.11441)
- Muldoon, J. y Wu, B. A. (2023). "Artificial Intelligence in the Colonial Matrix of Power". *Philosophy & Technology* 36(4), 80. https://doi.org/10.1007/s13347-023-00687-8

**Complementaria**

- Zainea, C. I. (2026). *Agencia sin imputación*. Sección sobre la triple mímesis. https://izainea.github.io/escritos/agencia-sin-imputacion.pdf
- Milano, S. y Prunkl, C. (2024). "Algorithmic profiling as a source of hermeneutical injustice". *Philosophical Studies* 182(1), 185-203. https://doi.org/10.1007/s11098-023-02095-2
- Schneider, F., Holtermann, C., Biemann, C. y Lauscher, A. (2025). "GIMMICK: Globally Inclusive Multimodal Multitask Cultural Knowledge Benchmarking". https://arxiv.org/abs/2502.13766
- Dussel, E. (1974). *Método para una filosofía de la liberación*. Salamanca: Sígueme.

## Guía de lectura

- Fricker exige que la carencia de conceptos sea estructural, no accidental: resulta de una desigualdad en la participación en los recursos interpretativos. *¿Es estructural la carencia de un modelo respecto de su archivo? ¿Quién participó en el corpus de entrenamiento y quién no?*
- Kay, Kasirzadeh y Mohamed llaman ignorancia hermenéutica a la tercera dimensión y le dan ejemplos. *¿Cuál de sus cuatro dimensiones opera en su flujo de investigación y cuál no? Argumente con una pieza propia.*
- Muldoon y Wu usan una categoría, la matriz colonial, que viene de la sociología latinoamericana. *¿Qué gana y qué pierde el curso al tomar de ahí una pregunta y no una conclusión? ¿Qué conclusión de ellos no aceptaría usted para su proyecto?*
- Milano y Prunkl muestran que un sistema de recomendación puede fragmentar los recursos interpretativos de sus usuarios. *¿Hay algo parecido en un flujo donde cada investigador consulta al modelo por separado y nadie compara las lecturas?*

## Taller de la segunda hora

Cada estudiante trae tres piezas cargadas de sentido local. Para cada una escribe primero, sin el modelo, qué sabe de ella alguien de la comunidad que la produjo. Luego pide al modelo una lectura y compara.

| Pieza | Lo que sabe un lector situado | Lectura del modelo | Qué entendió mal | Qué aplanó | Qué ignoró |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

Al final de la tabla, una frase: cuál de las tres columnas de exclusión se repite más en su material, y qué dice eso de la precomprensión del modelo.

## Guion de la sesión

| Momento | Docente | Estudiante | Material |
|---|---|---|---|
| 0 a 20 min | Expone la prefiguración ajena con la Figura 4 y distingue exposición de tesis | Ubica una pieza propia en la figura | Figura 4 |
| 20 a 40 min | Presenta a Fricker con el ejemplo del acoso y la extensión al instrumento | Discute si la extensión es legítima | Lectura central |
| 40 a 55 min | Recorre las cuatro dimensiones de Kay et al. y la pregunta de Muldoon y Wu | Elige la dimensión que opera en su flujo | Lecturas |
| 55 a 60 min | Presenta la tabla de contraste | Anota un caso de imposición | Tabla |
| 60 a 100 min | Acompaña el taller | Escribe la lectura situada, consulta al modelo, compara | Tabla del taller |
| 100 a 115 min | Recoge una pieza por estudiante | Expone la exclusión más repetida | Bitácora |
| 115 a 120 min | Anuncia la práctica de la semana 5 | Anota qué muestra va a usar | Guía de la práctica |

Notas para el docente. Suele fallar que el estudiante escriba la lectura situada después de ver la del modelo, y entonces la copia o la contradice por reacción; exigir el orden. Suele fallar que la columna "qué ignoró" quede vacía porque lo ignorado es por definición lo que no aparece; la pregunta de apoyo es qué diría un lector situado que el modelo no dijo. Y hay que cuidar que la discusión sobre colonialidad no sustituya al ejercicio: la pregunta se mide en la semana 5, no se zanja hoy.

## Bitácora

Registre la tabla de tres piezas, la frase final y el modelo usado con sus instrucciones. Anote una pieza en la que no esté seguro de si la diferencia es error factual o imposición: esos casos son los que la auditoría debe resolver.

## Para la próxima semana

Leer la guía `practicas/practica-05-auditoria-de-exterioridad.md` y la plantilla `plantillas/auditoria-de-exterioridad.md`. Seleccionar una muestra de entre diez y veinte piezas del propio corpus con el criterio de la guía, y conseguir al menos un lector situado que acepte leerla. Sin lector situado no hay auditoría.
