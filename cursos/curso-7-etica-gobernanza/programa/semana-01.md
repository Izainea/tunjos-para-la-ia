# Semana 1. Tres frentes de la ética en investigación asistida

## Pregunta de la semana

Cuando un investigador usa un modelo sobre material que no es suyo, ¿a quién puede dañar, qué puede excluir y quién responde si algo sale mal?

## Por qué esta semana

<p class="lede">La ética del trabajo con modelos suele llegar al final, como un párrafo de "consideraciones éticas" que se redacta cuando el análisis ya está hecho. Este curso la pone al principio y la divide en tres frentes que exigen instrumentos distintos. El primero es el del material: textos con autor, relatos con nombres, imágenes con rostros. El segundo es el de la lectura: un modelo entrenado en otra parte lee ese material con una precomprensión que no es la de la comunidad que lo produjo. El tercero es el de la responsabilidad: cuando el resultado está mal, la palabra que se usa para nombrar el error decide si alguien responde o nadie. La semana presenta los tres frentes, los distingue y muestra que el tercero es la condición de los otros dos.</p>

Este curso cierra el programa. En [*Las tres inferencias*](../../curso-1-tres-inferencias/README.md), el curso de fundamentos del programa, se distinguieron deducción, inducción y abducción por su régimen de validez y se concluyó que la máquina configura sin poder validar ni responder por lo configurado. Allí se sostuvo también que el error típico del modelo no es una alucinación sino un infortunio de autoridad epistémica, en el sentido de Austin: un acto que tiene la forma de una aserción fundamentada, la de quien procesó evidencia y llegó a una conclusión, sin cumplir las condiciones que la fundamentan, porque no hay nadie detrás que crea lo que dice ni que pueda dar razones. Este curso parte de esas dos conclusiones y repite aquí lo necesario para seguir sin haber tomado aquel.

## Contenido de la sesión

1. El caso que abre el curso es real y es del docente. Un sistema de agentes con modelos de lenguaje procesó más de 136.000 registros de relatos sobre personas desaparecidas en Colombia para identificar y normalizar categorías temáticas<sup class="mark">a</sup>. Antes de la primera línea de código hubo que decidir tres cosas: qué podía salir de la entidad hacia un proveedor externo y qué no, qué categorías podía proponer el modelo y cuáles solo podían venir de quienes conocen el conflicto, y quién firmaba el informe en que esas categorías aparecían. Esas tres decisiones son los tres frentes del curso, y ninguna se resolvió con un principio general.

<aside class="glosa"><span class="mark">a</span> El trabajo se hizo para la Unidad de Búsqueda de Personas dadas por Desaparecidas entre 2024 y 2026. Los relatos contienen nombres, lugares, fechas y descripciones de violencia. Ninguno salió de la infraestructura de la entidad sin anonimización, y las categorías finales las validó un equipo de analistas que conocía los casos.</aside>

2. El primer frente es el de los derechos y el cuidado del material. Una pieza de un corpus tiene casi siempre un autor con derechos, una persona a la que se refiere, una comunidad que la produjo y una plataforma que fijó condiciones cuando se publicó. En Colombia esos vínculos tienen nombre legal: el derecho de autor de la Ley 23 de 1982, la protección de datos personales de la Ley estatutaria 1581 de 2012, y los términos de uso que cada plataforma impone como contrato<sup class="mark">c</sup>. La semana 2 los lee con detalle. Hoy basta con la pregunta que los une: ¿qué puedo hacer con esta pieza sin dañar a nadie y sin apropiarme de lo que no es mío?

<aside class="glosa"><span class="mark">c</span> La Ley 1581 de 2012 llama dato personal a cualquier información vinculada o que pueda asociarse a una persona natural determinada o determinable, y dato sensible al que afecta la intimidad o puede dar lugar a discriminación: origen étnico, opinión política, creencias, salud, vida sexual, datos biométricos. Un relato de violencia suele contener varios a la vez.</aside>

3. El segundo frente es el de la exterioridad. Leído con la triple mímesis de *Tiempo y narración* (Ricœur, 1995), el modelo configura con competencia, pero su prefiguración es ajena: el corpus del que predice no es la precomprensión de la comunidad cuyo material interpreta (Zainea, 2026). El efecto no es un error factual que una verificación detecte, sino una imposición de categorías. Un modelo que describe una imagen de un altar con una figura de yeso, veladoras y una botella de aguardiente como "decoración rústica" no se equivocó en ningún dato. Dejó fuera lo que esa escena significa para quien la montó. La semana 4 le da a eso el nombre que Fricker (2007) acuñó, injusticia hermenéutica, y la semana 5 enseña a medirlo.

4. El tercer frente es el de la gobernanza, y su punto de partida es una palabra. Cuando el sistema produce algo falso o impone una categoría, el discurso corriente dice que "alucinó". La metáfora presupone una mente que representa y distorsiona, y esa mente no existe (Zainea, 2026). Pero tiene además un efecto político: deja el fallo dentro de la máquina y a nadie afuera<sup class="mark">b</sup>. Si en cambio el fallo se nombra como infortunio, en el sentido de Austin (1982), un acto que tiene la forma de la aserción fundamentada sin satisfacer sus condiciones, la pregunta siguiente es inevitable: ¿quién ejecutó el acto, con qué título y ante quién responde? Esa pregunta es la que un protocolo de gobernanza contesta por escrito.

<aside class="glosa"><span class="mark">b</span> Förster y Skop (2026) rastrean la historia de la metáfora en el discurso sobre IA y muestran cómo contribuye a desplazar la responsabilidad desde quien despliega el sistema hacia una supuesta patología del sistema mismo.</aside>

5. Los tres frentes no están al mismo nivel. El de los derechos y el de la exterioridad describen daños posibles; el de la gobernanza describe quién los evita y quién responde si ocurren. Sin el tercero, los otros dos son listas de buenas intenciones. Por eso el producto final del curso es un protocolo y no un informe ético: un documento que alguien distinto de su autor puede ejecutar, que dice qué se registra, quién revisa y en qué condiciones se rechaza un resultado.

<figure class="wide">
  <svg viewBox="0 0 680 300" style="width:100%;max-width:42rem;height:auto;display:block" role="img" aria-label="Tres frentes: derechos y cuidado del material, exterioridad de la lectura, gobernanza de la responsabilidad. Los dos primeros describen daños; el tercero sostiene a los otros dos y dice quién responde.">
    <style>.f1-h{font-family:var(--display);font-weight:700;font-size:15px;fill:var(--ink)} .f1-d{font-family:var(--text);font-size:12px;fill:var(--muted)} .f1-k{font-family:var(--mono);font-size:10px;letter-spacing:.08em;fill:var(--muted)} .f1-kf{font-family:var(--mono);font-size:10px;letter-spacing:.08em;fill:var(--c-fil)} .f1-bx{fill:var(--surface);stroke:var(--rule);stroke-width:1.2} .f1-base{fill:var(--surface);stroke:var(--c-fil);stroke-width:1.6} .f1-ar{stroke:var(--muted);stroke-width:1.3;fill:none}</style>
    <rect x="20" y="30" width="300" height="110" rx="3" class="f1-bx"/>
    <text x="34" y="50" class="f1-k">FRENTE 1 · MATERIAL</text>
    <text x="34" y="76" class="f1-h">Derechos y cuidado</text>
    <text x="34" y="98" class="f1-d">autor · datos personales · imágenes sensibles</text>
    <text x="34" y="116" class="f1-d">consentimiento en plataformas</text>
    <rect x="360" y="30" width="300" height="110" rx="3" class="f1-bx"/>
    <text x="374" y="50" class="f1-k">FRENTE 2 · LECTURA</text>
    <text x="374" y="76" class="f1-h">Exterioridad</text>
    <text x="374" y="98" class="f1-d">prefiguración ajena · categorías impuestas</text>
    <text x="374" y="116" class="f1-d">injusticia hermenéutica</text>
    <path class="f1-ar" d="M170 140 L170 185"/>
    <path class="f1-ar" d="M510 140 L510 185"/>
    <text x="340" y="170" text-anchor="middle" class="f1-k">DESCRIBEN DAÑOS POSIBLES</text>
    <rect x="20" y="190" width="640" height="90" rx="3" class="f1-base"/>
    <text x="34" y="210" class="f1-kf">FRENTE 3 · RESPONSABILIDAD</text>
    <text x="34" y="236" class="f1-h">Gobernanza</text>
    <text x="34" y="258" class="f1-d">quién decide · qué se registra · quién revisa · cuándo se rechaza · quién responde</text>
  </svg>
  <figcaption><b>Figura 1.</b> Los tres frentes. Los dos de arriba nombran daños; el de abajo nombra responsables. Sin el tercero, los otros dos quedan en lista de intenciones.</figcaption>
</figure>

| Si el error se llama alucinación | Si el error se llama infortunio |
|---|---|
| El fallo está dentro del sistema | El fallo está en un acto ejecutado sin título |
| La solución es técnica: mejor modelo, más datos | La solución es procesal: reglas sobre quién ejecuta y quién revisa |
| Quien desplegó el sistema queda fuera de la escena | Quien desplegó el sistema reclamó una autoridad y debe responder por ella |
| El informe dice "la herramienta se equivocó" | El informe dice "aceptamos esto sin verificarlo" |
| *Nadie responde* | *Alguien responde, y el protocolo dice quién* |

6. Hay una distinción que recorre el curso y conviene fijarla desde hoy. Una cosa es lo que el modelo produce y otra lo que el investigador afirma. En el momento en que una categoría propuesta por el modelo entra en un informe con el nombre del investigador, deja de ser output y pasa a ser aserción, y las aserciones tienen autor. En [*Las tres inferencias*](../../curso-1-tres-inferencias/README.md) se llamó frontera a ese límite, el lugar donde termina lo que la máquina configura y empieza lo que el investigador afirma y por lo que responde, y se enseñó a dejarlo por escrito en un registro de frontera: una tabla con lo que propuso la máquina en cada paso, lo que decidió el investigador y con qué criterio. Este curso pregunta qué reglas hacen que cruzarla sea defendible, y ante quién: ante las personas y comunidades a las que el material se refiere, y ante quienes leerán el resultado.

## IA y exigencia

Esta semana se le pide al modelo que describa tres piezas del material del estudiante y que proponga, para cada una, qué riesgos ve en usarla. El estudiante debe poder decir, sin el modelo, qué riesgo pasó por alto el modelo y por qué: casi siempre será uno que exige conocer el contexto de la pieza, y ese es el primer indicio de exterioridad que el curso registra.

## Lecturas

**Central**

- Zainea, C. I. (2026). *Agencia sin imputación. Hermenéutica, pragmática y la validación epistémica del discurso artificial*. Secciones sobre el infortunio de autoridad epistémica y sobre la prefiguración ajena. https://izainea.github.io/escritos/agencia-sin-imputacion.pdf
- Floridi, L. (2023). *The Ethics of Artificial Intelligence: Principles, Challenges, and Opportunities*. Oxford University Press. Parte 2, capítulo sobre el marco unificado de principios.

**Complementaria**

- Zainea, C. I. (2026). "Los modelos de lenguaje no alucinan: cometen infortunios". https://izainea.github.io/blog/alucinacion-o-infortunio/
- Förster, S. y Skop, Y. (2026). "Between fact and fairy: Tracing the hallucination metaphor in AI discourse". *AI & Society* 41(3), 1685-1698. https://doi.org/10.1007/s00146-025-02392-w
- Austin, J. L. (1982). *Cómo hacer cosas con palabras*. Conferencias I y II. Barcelona: Paidós.

## Guía de lectura

- Zainea distingue tres sentidos de validación: corrección del resultado, justificación del proceso e imputación. Los daños del primer frente, los del segundo y los del tercero se detectan en sentidos distintos. *¿En cuál de los tres sentidos se detecta una categoría impuesta por un modelo sobre material situado, y por qué una tasa de acierto no la ve?*
- Floridi reúne los principios que las guías de ética de la IA repiten (beneficencia, no maleficencia, autonomía, justicia, explicabilidad) y sostiene que el quinto es el que la IA añade. Las guías de principios son abundantes y las instrucciones escasas. *¿Qué le falta a un principio como "explicabilidad" para convertirse en una regla que un equipo pueda ejecutar el lunes?*
- La metáfora de la alucinación tiene un efecto de exención. Piense en un informe de su campo con un error producido por un modelo. *Si el error se llama alucinación, ¿quién queda exculpado? Si se llama infortunio, ¿quién queda señalado?*
- El caso de los relatos de personas desaparecidas tuvo tres decisiones previas al código. *¿Cuáles serían las tres decisiones previas de su propio proyecto, y cuál de ellas no ha tomado todavía?*

## Taller de la segunda hora

Cada estudiante trae tres piezas de su material, de tipos distintos si es posible (un texto, una imagen, un registro de plataforma). Para cada pieza llena la ficha de la semana, primero sin el modelo y luego con él.

| Pieza | Quién tiene derechos sobre ella | A quién se refiere o expone | Qué sabe de ella quien la produjo que un modelo no sabría | Quién responde si un análisis la usa mal | Frente dominante (1, 2 o 3) |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

Después, pídale al modelo que llene las mismas columnas y compare. Marque las celdas en que el modelo dijo menos que usted y las que dijo algo que usted no había visto. La comparación va a la bitácora.

## Guion de la sesión

| Momento | Docente | Estudiante | Material |
|---|---|---|---|
| 0 a 15 min | Presenta el caso de los relatos y las tres decisiones previas | Anota qué decisión le resulta menos obvia | Caso del docente |
| 15 a 40 min | Expone los tres frentes y la Figura 1 | Ubica su propio proyecto en la figura | Figura 1 |
| 40 a 60 min | Discute la metáfora de la alucinación y el efecto de exención | Propone un ejemplo de su campo | Lecturas |
| 60 a 100 min | Acompaña el taller mesa por mesa | Llena la ficha sin modelo y luego con modelo | Ficha de la semana |
| 100 a 115 min | Recoge dos casos en que el modelo dijo menos | Expone un caso | Bitácora |
| 115 a 120 min | Anuncia las lecturas normativas de la semana 2 | Anota qué material va a traer | Lecturas |

Notas para el docente. Suele fallar que los estudiantes traigan material sin problemas visibles (un libro publicado, un dato estadístico) para evitar la incomodidad; pedir con una semana de anticipación al menos una pieza con personas. Suele fallar también que la discusión sobre la alucinación se vuelva ontológica (si la máquina entiende o no); devolverla a la pregunta por quién responde. Y conviene no cerrar el frente 2 hoy: basta con que vean un ejemplo de categoría impuesta.

## Bitácora

Registre las tres fichas, la comparación con el modelo y una pregunta que le haya quedado abierta. Anote además qué modelo usó y con qué instrucción. Esta bitácora es la primera página de la matriz de riesgos y derechos de la semana 3.

## Para la próxima semana

Leer los artículos 31 y 32 de la Ley 23 de 1982 y los artículos 3 a 6 de la Ley 1581 de 2012 en el gestor normativo de Función Pública, y el capítulo 7 de Banks (2010). Traer diez piezas del propio material en una lista con origen, fecha y tipo. Si el material incluye imágenes de personas o de violencia, traer la descripción y no la imagen.
