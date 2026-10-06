# Semana 4. Descripción densa con modelos multimodales

## Pregunta de la semana

¿Qué le pide un investigador a un modelo multimodal cuando le pide que describa una imagen, y qué recibe a cambio?

## Por qué esta semana

<p class="lede">Con el catálogo construido y la gramática en la mano, el curso entra en la delegación. Un modelo multimodal recibe una imagen y un texto y devuelve un texto; pedirle una descripción es la operación más simple que admite y la más útil para un corpus grande. Produce, en segundos y por cada imagen, un párrafo que enumera objetos, personas, colores, disposición y, si se le pide, atmósfera y posible contexto. Lo hace con una fluidez que parece observación experta. Esta semana enseña a pedir esa descripción por capas, para que cada frase caiga en una celda conocida de la plantilla, y a conocer los costos y los límites de la operación. Smits y Wevers (2022) dan el marco: los modelos de visión no son ventanas sino instrumentos ópticos con agencia propia, y lo que ven depende de los conjuntos de datos con que fueron construidos.</p>

## Contenido de la sesión

1. Un modelo multimodal es un modelo de lenguaje que acepta imágenes como parte de la entrada. La imagen se convierte en una secuencia de fragmentos que el modelo trata como si fueran palabras, y la salida es texto generado por el mismo mecanismo de predicción de cualquier modelo de lenguaje: cada fragmento es el más probable dado lo anterior, y ningún paso lleva consigo un criterio de corrección. [*Validación del razonamiento con IA en ciencias sociales*, semana 7](../../curso-1-tres-inferencias/programa/semana-07.md) describe ese mecanismo, con la cadena de pensamiento y los modelos de recompensa por proceso, y concluye que el criterio de validez es extrínseco, local y estadístico: no está en el modelo. Eso tiene una consecuencia directa: la descripción no es un registro de lo que el modelo "vio" sino el texto más probable dado la imagen y el prompt, en el género de las descripciones de imagen con que fue entrenado. Ese género incluye textos alternativos, pies de foto, cartelas de museo y leyendas de bancos de imágenes, en su mayoría en inglés y sobre objetos del norte global.<sup class="mark">a</sup>

<aside class="glosa"><span class="mark">a</span> Smits y Wevers (2022) analizan seis conjuntos de datos de referencia de visión por computador (Caltech 101 y 256, PASCAL VOC, ImageNet, MS COCO, Open Images) y muestran que las categorías con que un modelo aprende a ver son decisiones históricas de quien armó el conjunto. Un modelo entrenado con ellos "ve" esas categorías.</aside>

2. La descripción densa es la que cubre la imagen con afirmaciones localizadas, no un resumen. El término viene de la visión por computador (describir regiones, no la imagen entera) y el curso lo usa en un sentido cercano al de Geertz: una descripción que registra lo suficiente para que otro pueda interpretar. En la práctica, densa quiere decir que enumera, localiza y califica: qué hay, dónde en el cuadro, de qué tamaño relativo, en qué relación con lo demás. Un modelo produce esa densidad con facilidad; lo que no produce con facilidad es la distinción entre lo que ve y lo que supone.

3. El prompt por capas pide la descripción en el orden de la plantilla y prohíbe mezclar. Primero la denotación de la narrativa interna: personas, objetos, lugar, disposición, texto visible, sin interpretar. Segundo, los índices materiales visibles: tipo de imagen (fotografía, grabado, captura de pantalla), señales de época (grano, color, formato), marcas de agua o de recorte. Tercero, y por separado, lo que el modelo supone: época probable, lugar probable, género, función, con el grado de confianza y la razón. Cuarto, lo que el modelo declara no poder saber. La separación es lo que hace auditable el resultado: una frase de la tercera capa que aparezca en la primera es un infortunio detectable.

| Prompt plano ("describe esta imagen en detalle") | Prompt por capas |
|---|---|
| Un párrafo fluido que mezcla lo que ve con lo que supone. | Cuatro bloques en orden: denotación, índices, suposiciones, lo que no sabe. |
| La suposición llega con el tono de la observación. | La suposición llega etiquetada, con confianza y razón. |
| Más agradable de leer; imposible de auditar frase por frase. | Menos fluido; cada frase cae en una celda de la ficha. |
| El modelo elige qué contar. | El investigador fija qué debe contarse y en qué orden. |
| *Produce una descripción.* | *Produce una descripción auditable, que es otra cosa.* |

4. El caso demostrativo usó un prompt estructurado por las tres capas de Banks sobre lotes de imágenes elegidos por muestreo teórico, como entrada de un pipeline de teoría fundamentada (microanálisis, codificación abierta, axial, evaluación de saturación). Las salidas se convirtieron en la materia prima del descubrimiento de categorías que la semana 6 retoma. En la sesión el docente muestra salidas reales de ese pipeline y lo que se espera encontrar en cualquier corpus local: detalle abundante en lo que el género de las leyendas nombra bien (vestuario, vehículos, objetos) y poco o ninguno en lo que solo un lector situado reconoce (una fachada de barrio, una estética que una telenovela hizo legible, un gesto de duelo popular). Eso no se corrige con un prompt más largo: es el límite de la precomprensión del modelo, y es el tema de la semana 5.

5. Los costos son de tres tipos y hay que presupuestarlos antes de empezar. El costo monetario depende del proveedor, del tamaño de la imagen y de la longitud de la salida; con cuotas gratuitas, 20 imágenes se describen sin pagar y 1.800 exigen un plan o varios días. El costo de tiempo es el de revisar: una descripción de 200 palabras por imagen son 360.000 palabras para el corpus del caso, que nadie lee enteras, y por eso la auditoría es por muestra. El costo ético es el envío de la imagen a un servidor ajeno: el curso lo evita con material sensible hasta tener el protocolo de la semana 7, y recomienda modelos locales cuando el corpus lo exige.<sup class="mark">b</sup>

<aside class="glosa"><span class="mark">b</span> Un modelo local corre en el computador del investigador sin enviar nada a un servidor. Los hay de visión de uso gratuito, con menor calidad de descripción y mayor control. La decisión entre calidad y control es del investigador y debe quedar en el registro de frontera.</aside>

6. Los límites conocidos conviene listarlos antes de verlos. El modelo tiende a completar: si ve tres figuras parcialmente ocultas, describe cuatro. Tiende a nombrar: si ve un uniforme, le asigna un cuerpo armado aunque no pueda saberlo. Tiende a la escena típica: una mesa con botellas se vuelve "celebración". Lee el texto visible con buena tasa y lo interpreta con mala. Y no ve lo que no está en su género: una foto de un cadáver cubierto puede describirse como "una persona descansando". Ninguno de estos límites es una alucinación; cada uno es el texto más probable para quien no participa de la forma de vida que produjo la imagen.

<figure class="wide">
  <svg viewBox="0 0 680 270" style="width:100%;max-width:42rem;height:auto;display:block" role="img" aria-label="Esquema del prompt por capas. A la izquierda la imagen entra al modelo con cuatro instrucciones en orden: denotación de la narrativa interna, índices materiales visibles, suposiciones con confianza y razón, y lo que no puede saber. A la derecha, las cuatro salidas caen en cuatro celdas separadas de la ficha; una flecha roja marca el infortunio típico: una suposición que aparece en la capa de denotación.">
    <style>.bx{fill:var(--surface);stroke:var(--rule);stroke-width:1.2} .t{font-family:var(--text);font-size:12.5px;fill:var(--ink)} .s{font-family:var(--text);font-size:11px;fill:var(--muted)} .k{font-family:var(--mono);font-size:9.5px;letter-spacing:.08em;fill:var(--muted)} .kf{font-family:var(--mono);font-size:9.5px;letter-spacing:.06em;fill:var(--c-fil)} .ar{stroke:var(--muted);stroke-width:1.3;fill:none} .ah{fill:var(--muted)} .bad{stroke:var(--c-fil);stroke-width:1.6;fill:none;stroke-dasharray:5 4} .bh{fill:var(--c-fil)}</style>
    <defs><marker id="s4-ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 1L9 5L0 9z" class="ah"/></marker><marker id="s4-bh" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 1L9 5L0 9z" class="bh"/></marker></defs>
    <rect x="10" y="30" width="110" height="80" rx="3" class="bx"/><text x="20" y="48" class="k">ENTRADA</text><text x="20" y="70" class="t">imagen</text><text x="20" y="88" class="t">+ prompt</text>
    <path class="ar" d="M120 70 L150 70" marker-end="url(#s4-ah)"/>
    <rect x="150" y="10" width="230" height="250" rx="3" class="bx"/><text x="160" y="28" class="k">PROMPT POR CAPAS · en este orden</text>
    <text x="160" y="58" class="t">1. Denotación interna</text><text x="160" y="74" class="s">qué hay, dónde, texto visible; sin interpretar</text>
    <text x="160" y="104" class="t">2. Índices materiales</text><text x="160" y="120" class="s">tipo de imagen, grano, color, marcas, recorte</text>
    <text x="160" y="150" class="t">3. Suposiciones</text><text x="160" y="166" class="s">época, lugar, género; confianza y razón</text>
    <text x="160" y="196" class="t">4. Lo que no puede saber</text><text x="160" y="212" class="s">declarado, no omitido</text>
    <text x="160" y="244" class="s">Separar capas es lo que hace auditable la salida.</text>
    <path class="ar" d="M380 54 L440 54" marker-end="url(#s4-ah)"/><path class="ar" d="M380 100 L440 100" marker-end="url(#s4-ah)"/><path class="ar" d="M380 146 L440 146" marker-end="url(#s4-ah)"/><path class="ar" d="M380 192 L440 192" marker-end="url(#s4-ah)"/>
    <rect x="440" y="36" width="230" height="36" rx="3" class="bx"/><text x="450" y="58" class="t">Celda: narrativa interna · denotación</text>
    <rect x="440" y="82" width="230" height="36" rx="3" class="bx"/><text x="450" y="104" class="t">Celda: materialidad · índices</text>
    <rect x="440" y="128" width="230" height="36" rx="3" class="bx"/><text x="450" y="150" class="t">Celda: connotación · hipótesis del modelo</text>
    <rect x="440" y="174" width="230" height="36" rx="3" class="bx"/><text x="450" y="196" class="t">Celda: pendiente para el investigador</text>
    <path class="bad" d="M560 128 C 600 110 600 90 560 72" marker-end="url(#s4-bh)"/>
    <text x="450" y="238" class="kf">INFORTUNIO TÍPICO</text><text x="450" y="254" class="s">una suposición aparece como denotación</text>
  </svg>
  <figcaption><b>Figura 4.</b> El prompt por capas y las celdas en que cae cada salida. Hay que ver la flecha punteada: el error que la auditoría de la semana 5 busca es una afirmación de la capa 3 escrita en el tono de la capa 1.</figcaption>
</figure>

7. La práctica de esta semana compara dos prompts sobre las mismas 20 imágenes. El primero pide "describe esta imagen en detalle"; el segundo es el prompt por capas de la guía. El estudiante guarda las dos salidas por imagen con fecha, modelo y prompt literal, y en la bitácora anota qué cambió. Lo que suele cambiar no es la cantidad de detalle sino su clasificación: el prompt plano mezcla; el prompt por capas obliga al modelo a declarar sus suposiciones, y declararlas es lo que permite rechazarlas.

## IA y exigencia

Se le pide al modelo que describa 20 imágenes con dos prompts y que, en el segundo, separe lo que ve de lo que supone. Se le exige al estudiante que pueda explicar, sin el modelo, por qué el orden de las capas importa, qué género de texto está imitando el modelo cuando describe, y cuánto costó, en dinero, tiempo y exposición de material, describir sus 20 imágenes, extrapolado a su corpus completo.

## Lecturas

**Central**

- Smits, T. y Wevers, M. (2022). "The agency of computer vision models as optical instruments". *Visual Communication*, 21(2), 329-349. https://doi.org/10.1177/1470357221992097
- Guía de la práctica 2: `practicas/practica-02-descripcion-y-auditoria.md`.

**Complementaria**

- Arnold, T. y Tilton, L. (2023). *Distant Viewing: Computational Exploration of Digital Images*. Cambridge, MA: MIT Press. Cap. 1. Acceso abierto: https://doi.org/10.7551/mitpress/14046.001.0001
- Manovich, L. (2020). *Cultural Analytics*. Cambridge, MA: MIT Press. Cap. 1.
- Zainea, C. I. (2026). "Los modelos de lenguaje no alucinan: cometen infortunios". https://izainea.github.io/blog/alucinacion-o-infortunio/

## Guía de lectura

- Smits y Wevers leen los conjuntos de datos de referencia como instrumentos ópticos con agencia, siguiendo a Latour y a Crary. *¿Qué categorías del conjunto con que se entrenó el modelo que usted usa coinciden con las de su corpus, y cuáles de las suyas no existen allí?*
- Los autores muestran que la categoría "persona" en esos conjuntos está desigualmente poblada por región y por género. *¿Qué espera que haga el modelo con las personas de su corpus que no se parecen a las del conjunto?*
- Arnold y Tilton (2023) insisten en que toda anotación automática es una interpretación codificada en el modelo, no una medición. *¿Cuál de las cuatro capas de su prompt se parece más a una medición, y por qué incluso esa no lo es?*
- En la entrada sobre infortunios, el error del modelo se describe como un acto con la forma de una aserción fundamentada sin sus condiciones. *¿Qué forma tiene una descripción de imagen "fundamentada", y cuál de sus condiciones no puede cumplir el modelo por construcción?*

## Taller de la segunda hora

Práctica 2, primera parte. Guía completa en `practicas/practica-02-descripcion-y-auditoria.md`. En resumen:

1. Para cada una de las 20 imágenes, obtener la descripción con el prompt plano y con el prompt por capas. Guardar modelo, fecha, prompt literal y salida.
2. Elegir tres imágenes y, en la tabla, anotar para cada capa de la salida estructurada cuántas afirmaciones contiene y cuántas de ellas usted habría escrito igual.
3. Anotar el costo: tokens o llamadas usadas, tiempo de ejecución, tiempo de lectura de las 40 salidas.

| Imagen | Afirmaciones en capa 1 | De ellas, escritas igual por mí | Suposiciones en capa 3 | De ellas, que yo rechazaría | Algo que el modelo declaró no saber |
|---|---|---|---|---|---|

Variante para grupos. Dos estudiantes describen las mismas cinco imágenes con el mismo prompt por capas en dos modelos distintos y comparan la capa de suposiciones. Las suposiciones en que los modelos coinciden no son por eso más ciertas; son más probables en el género, y conviene anotar la diferencia.

## Guion de la sesión

| Minuto | Momento | Qué hace el docente | Qué hace el estudiante | Material |
|---|---|---|---|---|
| 0 a 15 | Apertura | Muestra dos descripciones del caso (sin la imagen) y pide adivinar cuál usó el prompt por capas | Distingue por la estructura, no por el contenido | Dos salidas del caso |
| 15 a 35 | Mecanismo | Expone qué es un modelo multimodal y qué género imita, con Smits y Wevers | Nombra qué textos de su campo se parecen a las salidas | Pizarra |
| 35 a 50 | Prompt | Recorre la figura 4 y el prompt de la guía | Adapta el prompt a su corpus en dos frases | Figura 4, guía |
| 50 a 60 | Costos | Presupuesta en vivo el corpus del caso | Presupuesta el suyo | Calculadora |
| 60 a 105 | Práctica 2 | Acompaña; resuelve acceso al modelo | Describe 20 imágenes con dos prompts | Guía, cuaderno o interfaz web |
| 105 a 115 | Puesta en común | Pide un caso de suposición escrita como denotación | Lee el suyo | Salidas |
| 115 a 120 | Cierre | Anuncia la auditoría de la semana 5 | Elige 15 descripciones para auditar | Syllabus |

Notas para el docente. Suele fallar que los estudiantes envíen imágenes con personas identificables; revisar la selección antes de empezar. Suele fallar que la cuota gratuita se agote en la sesión; tener dos proveedores alternativos y la opción local probada. Y suele fallar que la comparación de prompts se lea como "el segundo es mejor"; insistir en que el segundo es más auditable, que es otra cosa.

## Bitácora

Registre las 40 salidas con sus metadatos, en el formato que después usará para todo el corpus, la tabla de las tres imágenes, el presupuesto extrapolado al corpus completo y una lista de las suposiciones del modelo que usted no habría hecho. Añada una pregunta abierta sobre lo que el modelo no vio.

## Para la próxima semana

Leer Pouget et al. (2024), al menos las secciones 1, 3 y 6, y Schneider et al. (2025), secciones 1 y 5. Tener elegidas 15 descripciones por capas de la práctica para auditarlas con la tabla de tres columnas de la semana 5.
