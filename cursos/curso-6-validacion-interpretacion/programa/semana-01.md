# Semana 1. Tres sentidos de validación

## Pregunta de la semana

Cuando alguien dice que un resultado está validado, ¿qué está diciendo exactamente: que es correcto, que el proceso fue correcto, o que alguien responde por él?

## Por qué esta semana

<p class="lede">En [*Validación del razonamiento con IA en ciencias sociales*](../../curso-1-tres-inferencias/README.md), el curso de fundamentos del programa, se distinguieron deducción, inducción y abducción por su régimen de validez: la deducción vale por su forma, la inducción por sus tasas de acierto, y la abducción, la inferencia que introduce hipótesis nuevas, solo porque alguien se compromete a perseguirla y a responder por ella. Aquel curso terminó con una conclusión de diseño: la máquina configura sin poder validar ni responder por lo configurado, y lo que le falta se construye desde afuera. Este curso empieza en ese afuera. El estudiante llega con material ya configurado, producido con o sin máquina: un corpus con procedencia documentada, como el que enseña a construir [*Corpus de textos con procedencia en ciencias sociales*](../../curso-2-corpus-textual/README.md); imágenes catalogadas y descritas por capas, como las de [*Descripción auditada de imágenes en investigación social*](../../curso-3-corpus-visual/README.md); un libro de códigos propuesto con un modelo y sostenido por el investigador, como el de [*Codificación cualitativa con IA en ciencias sociales*](../../curso-4-codificacion-asistida/README.md); grupos, redes y patrones con su prueba de estabilidad, como los de [*Patrones estables en datos de las ciencias sociales*](../../curso-5-metodos-computacionales/README.md); o lo que su propio proyecto haya producido sin ninguno de esos cursos. La pregunta ya no es qué inferencia hizo cada quien sino qué significa dar ese material por bueno. La primera semana desarma la palabra "validar", porque en ella conviven tres cosas distintas que la literatura sobre inteligencia artificial en investigación confunde de manera sistemática. Nombrarlas por separado es el primer instrumento del curso y la condición de todos los demás.</p>

## Contenido de la sesión

1. El caso de apertura es un informe real, anonimizado, que presenta como validada una categorización hecha con un modelo porque "el modelo coincidió con el codificador humano en el 92 % de los fragmentos". La sesión empieza por preguntar qué se validó ahí. La respuesta corta es que se midió algo, una tasa de coincidencia, y se dio por validado otra cosa, la categorización. El resto de la sesión explica por qué ese salto es el error típico del campo y no un descuido de un autor.

2. Validar tiene tres sentidos que no coinciden. En el primero, validar es comprobar la corrección del resultado: que lo afirmado sea verdadero, cosa que puede medirse sin atender al proceso, y que es lo que mide la ingeniería con sus tasas de acierto. En el segundo, validar es establecer que el proceso que condujo al resultado fue correcto, con independencia de que el resultado lo sea: es lo que exigen los criterios metodológicos. En el tercero, validar es que alguien pueda responder por lo afirmado, sostenerlo ante una comunidad y dar las razones que lo respaldan. El anteproyecto doctoral del docente (Zainea, 2026) sostiene que los cinco debates filosóficos sobre los modelos de lenguaje son variaciones de este tercer problema, y que el campo lo ha oscurecido al confundir los tres sentidos.<sup class="mark">a</sup>

<aside class="glosa"><span class="mark">a</span> El tercer sentido tiene tres nombres en la bibliografía del curso. Habermas lo llama redimir discursivamente una pretensión de validez; Floridi (2026), <i>answerability</i>, la posición de responder por lo que se afirma; en Ricœur remite a la imputabilidad. Son la misma exigencia vista desde la pragmática, la filosofía de la información y la hermenéutica.</aside>

3. Rendimiento no es validez. Un sistema puede acertar el 95 % de las veces y ser epistémicamente ingobernable, porque sus aciertos y sus errores proceden del mismo mecanismo y nada en su interior permite distinguirlos. La distinción no es de grado sino de categoría: el rendimiento mide aciertos; la validez, en su segundo y tercer sentido, mide la posibilidad de dar razones por un paso y de que alguien las sostenga. [*Validación del razonamiento con IA en ciencias sociales*](../../curso-1-tres-inferencias/programa/semana-01.md), el curso de fundamentos del programa, llamó a esto infortunio de autoridad epistémica, con la palabra que Austin (1982) usa para el acto de habla que falla no por ser falso sino por no cumplir las condiciones que lo hacen valer: el output tiene la forma de la aserción fundamentada sin que ningún agente pueda redimir sus pretensiones. Allí se propuso esa palabra en lugar de "alucinación", porque el problema no está en el contenido sino en la ausencia de quien responda. Esta semana lo vuelve criterio: cada vez que un informe presenta una cifra de rendimiento como validación, hay que preguntar en cuál de los tres sentidos.

4. El acuerdo entre codificadores es el ejemplo más limpio de la confusión. La tradición del análisis de contenido midió la fiabilidad de una codificación por la coincidencia entre codificadores independientes, con coeficientes como el kappa de Cohen o el alfa de Krippendorff.<sup class="mark">b</sup> McDonald, Schoenebeck y Forte (2019) revisaron cómo se usa esa medida en la investigación cualitativa y concluyeron que el acuerdo mide consistencia, no validez: dos codificadores pueden coincidir en una categoría equivocada, y en muchos diseños cualitativos el desacuerdo es un dato, no un ruido. Cuando el segundo codificador es un modelo, se añade un problema más, que el anteproyecto señala como vacío del campo: si las categorías emergieron del propio modelo, no hay contra qué medir el acuerdo. La cifra del 92 % del caso de apertura es un dato del primer sentido que se presentó como validación del segundo y se usó como si resolviera el tercero.

<aside class="glosa"><span class="mark">b</span> El kappa de Cohen (1960) corrige el acuerdo observado entre dos codificadores por el acuerdo esperado al azar. El alfa de Krippendorff generaliza la idea a más codificadores y a datos faltantes. Ninguno de los dos dice nada sobre si la categoría es la adecuada; solo sobre si se aplica igual.</aside>

5. Los tres sentidos se distribuyen de manera desigual entre máquina e investigador, y esa distribución es la tesis del curso. La ingeniería de los modelos ha progresado en el primer sentido; en el segundo, solo en dominios cerrados, donde un verificador externo conoce la respuesta de antemano; en el tercero no puede progresar por construcción, porque responder exige un agente que pueda ser tenido por autor de lo afirmado. El problema de este curso empieza donde no existe tal verificador: en la investigación social y humanística, donde no hay respuesta terminal contra la cual medir, y donde la validación del segundo sentido se articuló durante un siglo con la del tercero.<sup class="mark">c</sup> La tradición cualitativa contiene los recursos; las semanas 2 y 3 los extraen.

<aside class="glosa"><span class="mark">c</span> Un dominio es cerrado, en el sentido del curso, cuando existe un verificador externo al sistema que conoce la respuesta correcta: una demostración que un comprobador formal valida, un programa que pasa sus pruebas. En esos dominios los modelos de recompensa por proceso etiquetan cada paso por la probabilidad de alcanzar esa respuesta; [*Validación del razonamiento con IA en ciencias sociales*, semana 7](../../curso-1-tres-inferencias/programa/semana-07.md) los examinó a partir de Lightman et al. (2023) y concluyó que su criterio es extrínseco, local y estadístico: se ancla en una respuesta final conocida, funciona en matemáticas y código, y mide la probabilidad de llegar, no la validez del paso. Un corpus de entrevistas no tiene respuesta terminal; por eso el criterio no se transfiere.</aside>

6. Los tres sentidos organizan también los tres productos del curso. El protocolo de validación de la semana 3 dice, para cada fase del proyecto, qué sentido está en juego y qué criterio lo gobierna. La matriz de triangulación de la semana 5 trabaja el segundo sentido en su región más exigente, la de las instancias independientes. El informe analítico de la semana 8 es el lugar del tercero: cada hallazgo lleva su aserente, y la declaración de uso de IA dice qué fue de quién. Nada de eso se entiende sin la distinción de hoy.

7. La frase que organiza el curso es que el investigador refigura. En la triple mímesis de *Tiempo y narración* (Ricœur, 1995), configurar es organizar en trama lo disperso, y refigurar es devolver lo configurado a un mundo y a un lector que se lo apropia. La máquina configura con competencia; el investigador refigura, y refigurar incluye validar en los tres sentidos y responder. Esta semana solo nombra el mapa; la semana 6 lo recorre entero.

<figure class="wide">
<svg viewBox="0 0 680 230" style="width:100%;max-width:42rem;height:auto;display:block" role="img" aria-label="Tres sentidos de validación: corrección del resultado, justificación del proceso, imputación. La máquina progresa en el primero, en el segundo solo en dominios cerrados, en el tercero no puede por construcción. La flecha del informe típico salta del primero al tercero.">
<style>.v-h{font-family:var(--display);font-weight:700;font-size:15px;fill:var(--ink)} .v-d{font-family:var(--text);font-size:12px;fill:var(--muted)} .v-k{font-family:var(--mono);font-size:10px;letter-spacing:.08em;fill:var(--muted)} .v-kf{font-family:var(--mono);font-size:10px;letter-spacing:.08em;fill:var(--c-fil)} .v-bx{fill:var(--surface);stroke:var(--rule);stroke-width:1.2} .v-ok{fill:var(--c-inv)} .v-mid{fill:var(--accent)} .v-no{fill:var(--c-fil)} .v-ar{stroke:var(--c-fil);stroke-width:1.6;fill:none;stroke-dasharray:6 5}</style>
<rect x="10" y="40" width="200" height="120" rx="3" class="v-bx"/>
<text x="24" y="62" class="v-k">SENTIDO 1</text>
<text x="24" y="84" class="v-h">Corrección</text>
<text x="24" y="104" class="v-d">Lo afirmado es verdadero.</text>
<text x="24" y="120" class="v-d">Se mide: tasa de acierto, kappa.</text>
<circle cx="190" cy="58" r="5" class="v-ok"/>
<text x="24" y="148" class="v-d">La máquina progresa.</text>
<rect x="240" y="40" width="200" height="120" rx="3" class="v-bx"/>
<text x="254" y="62" class="v-k">SENTIDO 2</text>
<text x="254" y="84" class="v-h">Justificación</text>
<text x="254" y="104" class="v-d">Cada paso siguió un criterio</text>
<text x="254" y="120" class="v-d">que otro puede comprobar.</text>
<circle cx="420" cy="58" r="5" class="v-mid"/>
<text x="254" y="148" class="v-d">Solo en dominios cerrados.</text>
<rect x="470" y="40" width="200" height="120" rx="3" class="v-bx"/>
<text x="484" y="62" class="v-k">SENTIDO 3</text>
<text x="484" y="84" class="v-h">Imputación</text>
<text x="484" y="104" class="v-d">Alguien responde por lo</text>
<text x="484" y="120" class="v-d">afirmado ante una comunidad.</text>
<circle cx="650" cy="58" r="5" class="v-no"/>
<text x="484" y="148" class="v-d">No puede, por construcción.</text>
<path class="v-ar" d="M110 170 C 110 215 570 215 570 170"/>
<text x="340" y="222" text-anchor="middle" class="v-kf">EL SALTO DEL INFORME TÍPICO: "ACERTÓ EL 92 %", LUEGO "ESTÁ VALIDADO"</text>
<text x="340" y="24" text-anchor="middle" class="v-k">VALIDAR</text>
</svg>
<figcaption><b>Figura 1.</b> Los tres sentidos de validación y lo que la máquina puede en cada uno. Lo que hay que ver es el salto punteado: una cifra del primer sentido presentada como si cerrara el tercero.</figcaption>
</figure>

<iframe class="app" src="apps/sentidos-de-validacion.html" title="Clasificador de sentidos de validación: asigne cada afirmación a un sentido y lea por qué se confunden" loading="lazy"></iframe>

## IA y exigencia

Esta semana se le pide al modelo que produzca afirmaciones de validación sobre el material del estudiante: que diga por qué una categorización suya es buena, qué tan confiable es, qué la respalda. El estudiante debe poder clasificar cada afirmación del modelo en uno de los tres sentidos sin ayuda, y decir cuáles de ellas el modelo no está en posición de hacer. La exigencia no es desconfiar del modelo sino saber qué clase de cosa dijo.

## Lecturas

**Central**

- Zainea, C. I. (2026). *Agencia sin imputación. Hermenéutica, pragmática y la validación epistémica del discurso artificial*. Secciones sobre los tres sentidos de validación y sobre rendimiento y validez. https://izainea.github.io/escritos/agencia-sin-imputacion.pdf
- McDonald, N., Schoenebeck, S. y Forte, A. (2019). "Reliability and Inter-rater Reliability in Qualitative Research: Norms and Guidelines for CSCW and HCI Practice". *Proceedings of the ACM on Human-Computer Interaction* 3(CSCW), artículo 72. https://doi.org/10.1145/3359174

**Complementaria**

- Zainea, C. I. (2026). "Los modelos de lenguaje no alucinan: cometen infortunios". https://izainea.github.io/blog/alucinacion-o-infortunio/
- Floridi, L. (2023). "AI as Agency Without Intelligence: On ChatGPT, Large Language Models, and Other Generative Models". *Philosophy & Technology* 36, 15. https://doi.org/10.1007/s13347-023-00621-y
- Krippendorff, K. (2004). "Reliability in Content Analysis: Some Common Misconceptions and Recommendations". *Human Communication Research* 30(3), 411-433. https://doi.org/10.1111/j.1468-2958.2004.tb00738.x

## Guía de lectura

- Zainea distingue los tres sentidos y afirma que la ingeniería progresa en el primero, en el segundo solo en dominios cerrados y en el tercero no puede. La afirmación sobre el segundo sentido es la más discutible, porque un registro de proceso parece algo que una máquina puede producir. *¿Qué añade "dominio cerrado" a la idea de justificar un proceso, y qué pasa con esa justificación cuando no hay respuesta terminal conocida?*
- McDonald, Schoenebeck y Forte muestran que en muchos diseños cualitativos no se calcula acuerdo entre codificadores, y que eso no es una carencia sino una decisión coherente con el método. *¿En qué diseños el desacuerdo es un dato y no un ruido, y qué ocurre con ese dato cuando el segundo codificador es un modelo que no puede explicar por qué discrepó?*
- Krippendorff insiste en que la fiabilidad es condición necesaria y no suficiente de la validez. *Si eso ya se sabía en 2004 para codificadores humanos, ¿por qué la llegada de los modelos volvió a confundir las dos cosas?*
- En la entrada sobre infortunios, el docente sostiene que el 95 % correcto se produce por las mismas razones estadísticas que el 5 % incorrecto. *¿Es esa una afirmación sobre el modelo o sobre lo que el modelo puede decir de sí mismo? ¿Cambia algo para la validación?*

## Taller de la segunda hora

Cada estudiante trae tres afirmaciones de validación tomadas de su propio material: una escrita por él en un informe o bitácora anterior, una producida por un modelo cuando se le pidió evaluar su propio trabajo, y una tomada de un artículo de su campo que use modelos de lenguaje. Llena para cada una la ficha de la semana.

| Afirmación (literal) | Quién la hace | Sentido que invoca (1, 2, 3) | Sentido que en realidad satisface | Qué haría falta para satisfacer el sentido que invoca |
|---|---|---|---|---|

Tres ejemplos de afirmaciones que suelen aparecer, para calibrar: "la categoría 'desconfianza institucional' fue consistente en el 88 % de los fragmentos" invoca el sentido 2 y satisface el 1; "el modelo siguió el protocolo de codificación abierta, axial y selectiva" invoca el 2 y lo satisface solo si existe el registro de cada paso; "sostengo que la desconfianza institucional organiza el corpus" invoca el 3 y lo satisface si quien lo escribe puede dar razones ante quien se lo pregunte.

Después, en parejas, cada uno clasifica las afirmaciones del otro sin ver su columna. Las discrepancias son el material de la discusión final. La mini app de la semana sirve para calibrar antes de empezar: tiene afirmaciones reales del tipo "el modelo acertó el 92 %", "el proceso siguió el protocolo", "yo respondo por esta categoría", y explica las confusiones típicas.

## Guion de la sesión

| Momento | Docente | Estudiante | Material |
|---|---|---|---|
| 0 a 15 min | Presenta el caso de apertura y pregunta qué se validó | Responde por escrito en una frase antes de discutir | Informe anonimizado |
| 15 a 40 min | Expone los tres sentidos y la distinción entre rendimiento y validez | Toma nota de un ejemplo propio por cada sentido | Figura 1 |
| 40 a 60 min | Discute McDonald, Schoenebeck y Forte a partir de la guía de lectura | Defiende en qué diseños el desacuerdo es un dato | Lectura central |
| 60 a 70 min | Pausa | | |
| 70 a 85 min | Presenta la mini app y hace dos ejemplos con el grupo | Clasifica cinco afirmaciones en la app | apps/sentidos-de-validacion.html |
| 85 a 110 min | Acompaña el taller por parejas | Llena la ficha y cruza clasificaciones | Ficha de la semana |
| 110 a 120 min | Cierra con las discrepancias más frecuentes y anuncia la semana 2 | Anota la pregunta que le quedó abierta | Bitácora |

Notas para el docente. Lo que suele fallar: los estudiantes clasifican por quién habla y no por qué se afirma, de modo que todo lo que dice el investigador queda en el sentido 3 y todo lo que dice el modelo en el sentido 1; conviene mostrar una afirmación del investigador que es puro rendimiento ("codifiqué 300 fragmentos") y una del modelo con forma de imputación ("confío en esta categoría") que no puede satisfacer. Segundo fallo: tomar la distinción como jerarquía, como si el sentido 3 fuera el único serio; el sentido 1 es imprescindible donde hay respuesta contra la cual medir, y el curso no lo desprecia. Tercero: la discusión sobre el kappa se va a la fórmula; no importa la fórmula sino qué mide.

## Bitácora

Registre las tres afirmaciones con su ficha, la clasificación de su pareja y las discrepancias. Añada una pregunta que le haya quedado abierta. Esta bitácora es la primera página del protocolo de validación que entregará en la semana 3.

## Para la próxima semana

Leer Lincoln y Guba (1985), capítulo 11, "Establishing Trustworthiness", y la entrada del docente sobre la prótesis hermenéutica. Traer la lista de fases de su propio proyecto, de la recolección a la escritura, con una línea por fase que diga si en esa fase intervino un modelo y para qué.
