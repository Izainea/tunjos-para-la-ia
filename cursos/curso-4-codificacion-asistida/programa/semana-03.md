# Semana 3. Codificación abierta asistida

## Pregunta de la semana

Cuando el modelo propone un código para un fragmento, ¿qué tiene que ocurrir para que ese código pase a ser una decisión del investigador y no una aceptación?

## Por qué esta semana

<p class="lede">Esta semana se codifica. Hasta ahora el curso ha preparado el criterio; a partir de hoy el estudiante abre su corpus, le pide al modelo códigos para cada fragmento y decide, uno por uno, qué hace con ellos. La codificación abierta es la fase en la que la contribución del modelo es mayor y en la que la ilusión de validez es más fuerte: los códigos llegan con definiciones, con fragmentos citados y con una seguridad de superficie que ningún codificador humano muestra en su primera pasada. La semana enseña a tratar cada propuesta como lo que es, una configuración, y a convertirla en decisión mediante un registro de frontera por código.</p>

La semana se apoya en dos operaciones de la teoría fundamentada que son, al mismo tiempo, antídotos contra la aceptación acrítica: el microanálisis de Strauss y Corbin, que obliga a leer palabra por palabra antes de nombrar, y el código in vivo, que toma las palabras del hablante en lugar de las del analista. Las dos operaciones se le pueden pedir al modelo, y las dos dejan rastro verificable. Lo que no se le puede pedir es que decida.

## Contenido de la sesión

1. La codificación abierta, en Strauss y Corbin (2002), es el proceso analítico por el cual se identifican conceptos y se descubren en los datos sus propiedades y dimensiones. La regla de generación es fragmentar el material, nombrar cada fragmento con un concepto y comparar cada incidente con los anteriores para decidir si el nombre ya existe o hace falta uno nuevo. El criterio de validez es que el nombre esté anclado en el fragmento y no en una idea previa. La condición de terminación es provisional: se pasa a la siguiente fase cuando el material deja de producir nombres nuevos, y se vuelve cada vez que un fragmento posterior obliga a revisar. La condición de imputación queda en la firma del libro de códigos abierto, que es el primer producto del curso.

2. El microanálisis es la lectura detallada, línea por línea y a veces palabra por palabra, con la que Strauss y Corbin abren un texto antes de nombrarlo. Su función es impedir que el analista lea de corrido y vea lo que esperaba ver. Pedirle a un modelo que haga microanálisis es pedirle que, para cada frase, enumere los significados posibles de sus términos antes de proponer un código.<sup class="mark">a</sup> El modelo lo hace con una generosidad que cansa, y esa generosidad es útil: produce alternativas que el investigador descarta con razones, y las razones son el principio del registro.

<aside class="glosa"><span class="mark">a</span> El ejemplo de Strauss y Corbin es la frase "cuando oí el diagnóstico" en una entrevista sobre enfermedad: "oír" abre el sentido de recibir, de no poder no escuchar, de enterarse por otro; "diagnóstico" abre el de nombre médico, de sentencia, de principio de una etapa. Ninguna de esas aperturas es todavía un código. Son el material sobre el que se decide.</aside>

3. El código in vivo toma las palabras del participante como nombre del código. Saldaña (2021) lo presenta como uno de los métodos de primer ciclo más apropiados para estudios que privilegian la voz de los participantes, y Charmaz (2014) lo recomienda como protección contra la imposición de categorías. Para el curso tiene una ventaja adicional: un código in vivo es verificable con el registro, porque su anclaje es literal. Cuando el modelo propone "madrugar para alcanzar el bus" para un fragmento que dice "me toca madrugar a las tres para alcanzar el bus", el criterio de anclaje se satisface a simple vista. Cuando propone "precariedad laboral" para el mismo fragmento, el anclaje hay que buscarlo y no está.<sup class="mark">b</sup>

<aside class="glosa"><span class="mark">b</span> Saldaña recomienda escribir los códigos in vivo entre comillas, para que en el libro se distingan a simple vista de los que construyó el analista. En el registro del curso esa función la cumple la columna de origen, que además dice si el nombre lo propuso el modelo o el investigador.</aside>

4. La codificación asistida que el curso enseña tiene una forma fija: el modelo propone, el investigador decide, y la decisión se registra con su criterio. Decidir admite cuatro resultados: aceptar el código tal como vino, corregirlo (cambiar el nombre, estrechar o ampliar la definición), rechazarlo, o reformularlo como pregunta para un memo. Lo que no admite es la quinta opción, que es la más frecuente cuando no hay registro: dejar pasar. Un código que pasó sin decisión es un output que se presenta como aserción, y el curso lo trata como infortunio de autoridad epistémica (Zainea, 2026): no porque el código esté mal, sino porque nadie responde por él.

5. El registro de frontera por código es la herramienta de la semana y la columna vertebral del primer producto. Para cada código: su nombre, su definición operativa, los fragmentos que lo anclan, su origen (propuesto por el modelo, propuesto por el investigador, propuesto por el modelo y corregido), la decisión tomada, el criterio de la decisión, y quién responde. La plantilla está en `plantillas/registro-de-frontera-codificacion.md`. No es un informe de uso de inteligencia artificial: es la evidencia de que el estudiante sabe, código por código, dónde terminó la máquina y dónde empezó él.

6. La contribución del modelo es real y hay que decirlo con precisión para no caer en la imagen del instrumento pasivo. El modelo aplica la regla de generación con consistencia, no se cansa en el fragmento cuarenta, no olvida que ya usó un nombre y produce, para cada fragmento, más alternativas de las que un analista considera. Es, en los términos de *Agencia sin imputación*, un agente de configuración competente. Lo que no aporta es la comparación constante en sentido propio, porque no recuerda qué comparó de una sesión a otra, ni la sensibilidad teórica de Glaser (1978), que es la capacidad de ver en los datos lo que el trasfondo del investigador permite ver. Su trasfondo es otro. La semana 4 muestra cómo se nota.

7. Queda una advertencia metodológica sobre el acuerdo. Es tentador, al terminar la primera ronda, contar en cuántos fragmentos el estudiante y el modelo pusieron el mismo código y leer esa cifra como una medida de calidad. El simulador de la semana calcula esa cifra y muestra por qué no mide lo que parece: dos codificadores pueden coincidir en un código mal puesto, y pueden discrepar porque uno de los dos vio algo que el libro de códigos aún no sabe nombrar. McDonald, Schoenebeck y Forte (2019) lo dicen para codificadores humanos; el curso lo extiende al modelo en la semana 6. Por ahora basta con ver los desacuerdos uno por uno.

<figure class="wide">
  <svg viewBox="0 0 680 290" style="width:100%;max-width:42rem;height:auto;display:block" role="img" aria-label="Diagrama de la frontera en la codificación asistida. Arriba, la máquina: recibe un fragmento, hace microanálisis, propone códigos con anclaje literal y alternativas. Una línea discontinua roja marca la frontera. Abajo, el investigador: decide aceptar, corregir, rechazar o reformular, escribe el criterio y firma el registro. A la derecha, el registro de frontera por código reúne nombre, anclaje, origen, decisión, criterio y quién responde. Una flecha de retroalimentación devuelve las decisiones a la máquina para la siguiente ronda.">
    <style>.bx{fill:var(--surface);stroke:var(--rule);stroke-width:1.2} .t{font-family:var(--text);font-size:12.5px;fill:var(--ink)} .s{font-family:var(--text);font-size:11px;fill:var(--muted)} .k{font-family:var(--mono);font-size:9.5px;letter-spacing:.08em;fill:var(--muted)} .kf{font-family:var(--mono);font-size:9.5px;letter-spacing:.08em;fill:var(--c-fil)} .ar{stroke:var(--muted);stroke-width:1.3;fill:none} .fr{stroke:var(--c-fil);stroke-width:1.6;stroke-dasharray:6 5;fill:none} .ah{fill:var(--muted)} .reg{fill:var(--surface);stroke:var(--accent);stroke-width:1.2}</style>
    <defs><marker id="s3-ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 1L9 5L0 9z" class="ah"/></marker></defs>
    <text x="20" y="16" class="k">FRAGMENTO n</text>
    <path class="ar" d="M60 22 L60 40" marker-end="url(#s3-ah)"/>
    <rect x="20" y="44" width="420" height="78" rx="3" class="bx"/>
    <text x="32" y="62" class="k">MÁQUINA · configura</text>
    <text x="32" y="84" class="t">microanálisis: abre los sentidos de cada término</text>
    <text x="32" y="102" class="t">propone códigos con anclaje literal y alternativas descartables</text>
    <text x="32" y="116" class="s">consistente en el fragmento 40 · no recuerda qué comparó · trasfondo ajeno</text>
    <path class="fr" d="M10 140 L450 140"/>
    <text x="450" y="136" text-anchor="end" class="kf">FRONTERA</text>
    <path class="ar" d="M60 124 L60 160" marker-end="url(#s3-ah)"/>
    <rect x="20" y="164" width="420" height="78" rx="3" class="bx"/>
    <text x="32" y="182" class="k">INVESTIGADOR · decide</text>
    <text x="32" y="204" class="t">acepta · corrige · rechaza · reformula como memo</text>
    <text x="32" y="222" class="t">escribe el criterio en una frase y firma</text>
    <text x="32" y="236" class="s">la quinta opción, dejar pasar, no existe en el registro</text>
    <rect x="470" y="44" width="200" height="198" rx="3" class="reg"/>
    <text x="482" y="62" class="k">REGISTRO POR CÓDIGO</text>
    <text x="482" y="86" class="t">nombre y definición</text>
    <text x="482" y="106" class="t">fragmentos de anclaje</text>
    <text x="482" y="126" class="t">origen: modelo / yo / mixto</text>
    <text x="482" y="146" class="t">decisión</text>
    <text x="482" y="166" class="t">criterio</text>
    <text x="482" y="186" class="t">quién responde</text>
    <text x="482" y="216" class="s">lo que el modelo escribió</text>
    <text x="482" y="230" class="s">queda arriba; lo decidido, abajo</text>
    <path class="ar" d="M440 90 L470 90" marker-end="url(#s3-ah)"/>
    <path class="ar" d="M440 210 L470 210" marker-end="url(#s3-ah)"/>
    <path class="ar" d="M230 242 C 230 270 8 270 8 150 C 8 60 14 48 20 48" marker-end="url(#s3-ah)"/>
    <text x="120" y="272" class="s">las decisiones vuelven al modelo en la siguiente ronda</text>
  </svg>
  <figcaption><b>Figura 3.</b> La frontera en la codificación asistida. Lo que hay que ver: el registro tiene dos partes separadas por la frontera, y la decisión con su criterio es lo único que convierte una propuesta en código.</figcaption>
</figure>

<iframe class="app" src="apps/simulador-codificacion.html" title="Simulador de codificación: el modelo propone, usted decide" loading="lazy"></iframe>

## IA y exigencia

Esta semana se le pide al modelo que haga microanálisis y proponga códigos, con anclaje literal, para cada fragmento del corpus propio, en una o dos rondas según la guía de la práctica 3. El estudiante debe poder, sin el modelo, justificar cada decisión del registro con un criterio que no sea "sonaba bien", señalar al menos un código que rechazó y decir por qué, y distinguir entre un código que aceptó porque lo verificó y uno que aceptó porque no supo qué más hacer. Los segundos no se borran: se anotan como aceptaciones sin criterio.

## Lecturas

**Central**

- Strauss, A. y Corbin, J. (2002). *Bases de la investigación cualitativa. Técnicas y procedimientos para desarrollar la teoría fundamentada*. Medellín: Universidad de Antioquia. Cap. 5, sobre el microanálisis, y cap. 8, sobre la codificación abierta. Original: *Basics of Qualitative Research*, 2.ª ed., Sage, 1998.
- Saldaña, J. (2021). *The Coding Manual for Qualitative Researchers*. 4.ª ed. Londres: Sage. Cap. 1, "An introduction to codes and coding".

**Complementaria**

- Charmaz, K. (2014). *Constructing Grounded Theory*. 2.ª ed. Londres: Sage. Cap. 5, sobre la codificación inicial y focalizada.
- Gibbs, G. (2012). *El análisis de datos cualitativos en investigación cualitativa*. Madrid: Morata. Cap. 4, sobre codificación temática y categorización.
- Glaser, B. G. (1978). *Theoretical Sensitivity: Advances in the Methodology of Grounded Theory*. Mill Valley: Sociology Press.
- Zainea, C. I. (2026). "Los modelos de lenguaje no alucinan: cometen infortunios". https://izainea.github.io/blog/alucinacion-o-infortunio/

## Guía de lectura

- Strauss y Corbin presentan el microanálisis como una lectura que se hace al comienzo y cada vez que el análisis se estanca. Su función es generar posibilidades, no elegir entre ellas. *Si un modelo genera esas posibilidades en segundos, ¿qué queda del valor del microanálisis, y dónde se traslada el trabajo?*
- En el capítulo sobre codificación abierta, fíjese en la diferencia entre conceptualizar (poner un nombre) y categorizar (agrupar nombres bajo uno más abstracto). *¿En cuál de las dos operaciones es más probable que un modelo importe categorías de su entrenamiento?*
- Saldaña enumera decenas de métodos de codificación y advierte que elegir uno es una decisión de método, no de gusto. *¿Qué método eligió usted para su corpus, y cómo se lo dijo al modelo?*
- La entrada sobre infortunios sostiene que el error del modelo no es decir algo falso sino decirlo con una autoridad que no puede respaldar. *Un código bien puesto que el estudiante aceptó sin criterio, ¿es un infortunio? ¿De quién?*

## Taller de la segunda hora

Guía completa en `practicas/practica-03-codificacion-abierta-asistida.md`. En resumen: el estudiante trabaja sobre los primeros quince a veinte fragmentos de su corpus.

1. Antes de pedirle nada al modelo, codifica cinco fragmentos a mano, con microanálisis, y guarda sus códigos sin mostrarlos.
2. Le pide al modelo microanálisis y códigos para los mismos cinco fragmentos con la instrucción de la práctica, que exige anclaje literal y prohíbe vocabulario de la literatura.
3. Compara, fragmento a fragmento, y llena el registro de frontera por código: origen, decisión, criterio.
4. Continúa con los fragmentos siguientes ya con el modelo, decidiendo cada código.

| Código | Definición operativa | Fragmentos de anclaje | Origen (modelo / yo / mixto) | Decisión | Criterio | Quién responde |
|---|---|---|---|---|---|---|

## Guion de la sesión

| Momento | Qué hace el docente | Qué hace el estudiante | Material |
|---|---|---|---|
| 0 a 15 min | Hace microanálisis en vivo de una frase traída por un estudiante y luego muestra el del modelo sobre la misma frase | Compara las dos aperturas de sentido | Tablero, modelo en versión web |
| 15 a 35 min | Expone la codificación abierta con los cuatro enunciados y el registro de frontera por código (figura 3) | Revisa su lista de verificación de la semana 2 contra la figura | Figura 3, plantilla del registro |
| 35 a 50 min | Simulador de codificación: el grupo codifica los doce fragmentos y discute dos desacuerdos | Codifica, compara, decide quién tiene razón | Mini app |
| 50 a 110 min | Práctica 3 sobre el corpus propio, acompañando mesa por mesa | Codifica a mano cinco fragmentos, luego con el modelo, llena el registro | Práctica 3, corpus propio |
| 110 a 120 min | Cierra con dos registros leídos en voz alta y anuncia el memo de la semana 4 | Anota sus aceptaciones sin criterio | Bitácora |

Notas para el docente. Suele fallar que el estudiante pide los códigos al modelo antes de codificar a mano y luego no puede distinguir qué habría visto solo; insistir en el orden. Suele fallar que el modelo, a pesar de la instrucción, propone códigos abstractos ("precariedad", "resiliencia") y el estudiante los acepta porque suenan a ciencia social; es el material de la semana 4, pero conviene señalar uno en vivo. Y suele ocurrir que un estudiante con corpus sensible se bloquea: tener a mano la variante con material público de la práctica.

## Bitácora

El registro de frontera de los fragmentos codificados esta semana, con los prompts literales en anexo. Marque las aceptaciones sin criterio. Añada una nota sobre el simulador: en qué desacuerdo le costó más decidir y por qué.

## Para la próxima semana

Leer Glaser (1992), capítulos 1 a 3, Kelle (2005) y Strauss y Corbin (2002), capítulo 14, sobre memos. Terminar la codificación abierta del corpus completo con el registro. Escribir un primer memo sobre el código que más dudas le produjo, con la plantilla `plantillas/memo-analitico.md`. La semana 4 recibe el primer producto.
