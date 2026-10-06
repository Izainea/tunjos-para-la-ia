# Semana 4. El catálogo maestro

## Pregunta de la semana

¿Qué tiene que saber una tabla de cada pieza para que el corpus se pueda reconstruir, citar y defender sin volver a la fuente?

## Por qué esta semana

<p class="lede">Hasta aquí el corpus es una carpeta <code>crudo</code> con una bitácora de descarga. Esta semana le da su columna vertebral: el catálogo maestro, una tabla con una fila por pieza y una columna por cada cosa que hay que saber de ella. El catálogo no es un inventario ni un adorno administrativo. Es el lugar donde la decisión de la semana 1 queda escrita pieza por pieza, donde la procedencia de la semana 3 se vuelve consultable, y donde el análisis de las semanas 6 y 7 va a buscar qué se puede decir de cada texto. Un corpus sin catálogo no se puede citar; un catálogo que no se valida no se puede creer. La semana enseña a construirlo con pandas, a limpiar sus duplicados con hash y a someterlo a reglas de integridad antes de usarlo.</p>

## Contenido de la sesión

1. El catálogo responde las preguntas que la cadena de procedencia dejó planteadas, y responde una por columna. De dónde salió la pieza: fuente y dirección. Cuándo fue producida y cuándo fue tomada: dos fechas distintas que se confunden con frecuencia. Quién la produjo y en qué situación: la escena, que en prensa es el periódico y la sección, y en normas es la entidad y el tipo de acto. Bajo qué régimen se puede usar: derechos. Por qué está en el corpus: el criterio de inclusión del protocolo que la hizo entrar. Y cómo se sabe que es la misma: el hash. Lo demás es útil; esto es obligatorio.

2. El esquema del curso tiene catorce campos y se adopta tal cual, para que los catálogos de todos los estudiantes se puedan comparar y para que los cursos 4 y 5 del programa los reciban sin traducción. Los campos obligatorios son `id`, `titulo`, `fuente`, `url`, `fecha_documento`, `fecha_descarga`, `escena`, `derechos`, `criterio_inclusion`, `hash_sha256` y `ruta_crudo`; los opcionales son `autor`, `ruta_limpio` y `notas`.<sup class="mark">a</sup> Un proyecto puede añadir columnas; no puede quitar las obligatorias. La plantilla `plantillas/catalogo-maestro.md` describe cada campo, su formato y un ejemplo.

<aside class="glosa"><span class="mark">a</span> El esquema sigue el espíritu de los principios FAIR de Wilkinson y coautores (2016): que los datos sean encontrables, accesibles, interoperables y reutilizables. Para un corpus de humanidades, encontrable quiere decir que cada pieza tiene identificador y descripción; reutilizable, que tiene derechos y procedencia declarados.</aside>

3. El identificador es propio, estable y opaco. Propio porque lo asigna el investigador y no la fuente: si la fuente renumera o desaparece, el corpus no cambia. Estable porque una vez asignado no se reutiliza: una pieza excluida conserva su identificador con la nota de exclusión, y la siguiente recibe uno nuevo. Opaco porque no codifica información que pueda cambiar: `P-0042` sirve; `ElTiempo-1910-marzo-nota3` deja de servir el día en que se descubre que la nota era de abril. Todo lo que el identificador quisiera decir se dice en las otras columnas.

4. Deduplicar es la primera limpieza del catálogo, y se hace con el hash antes que con los ojos. Dos piezas con el mismo SHA-256 son el mismo archivo byte a byte: una se conserva y la otra se anota como duplicado de la primera. Los casi duplicados, que difieren en espacios, en mayúsculas, en una tilde perdida por el OCR o en una línea de encabezado, no comparten hash, y para detectarlos hay que decidir qué diferencias se ignoran.<sup class="mark">b</sup> Esa decisión es del investigador, se escribe en el cuaderno, y la mini app muestra cómo cambia el resultado según qué se normaliza antes de comparar.

<aside class="glosa"><span class="mark">b</span> Una forma simple de medir cuánto se parecen dos textos es el índice de Jaccard: el número de palabras que comparten dividido por el número de palabras distintas que tienen entre los dos. Vale entre 0 y 1; dos textos idénticos dan 1. No reemplaza la lectura, pero señala dónde mirar.</aside>

<iframe class="app" src="apps/deduplicacion-hash.html" title="Deduplicación por hash: qué cuenta como el mismo texto según lo que se normaliza" loading="lazy"></iframe>

5. Validar la integridad es someter el catálogo a reglas antes de confiar en él, y escribir las reglas en el cuaderno para que se apliquen cada vez que el catálogo cambie. Las reglas del curso son cinco: ningún campo obligatorio vacío; las fechas con formato ISO y la de descarga posterior a la del documento; el hash de la columna igual al hash recalculado del archivo en `ruta_crudo`; ningún identificador repetido; y ningún criterio de inclusión que no exista en el protocolo. Un catálogo que no pasa las cinco no entra al análisis. La mini app aplica las tres primeras a diez registros y explica, para cada falla, qué dejaría de poder reconstruirse.

<iframe class="app" src="apps/validador-catalogo.html" title="Validador de catálogo: qué registros no podrían reconstruirse y por qué" loading="lazy"></iframe>

6. pandas entra esta semana con tres operaciones y no más: leer una tabla desde CSV, filtrar filas por una condición, y agrupar por una columna para contar. Con las tres, el estudiante responde las preguntas que un lector le hará a su corpus: cuántas piezas por fuente, cuántas por año, cuántas por criterio de inclusión, cuántas con derechos restringidos. Las respuestas son la primera descripción del corpus, y van al informe de la semana 8 tal como salen del cuaderno, con la celda que las produjo.

<figure class="wide">
<svg viewBox="0 0 680 320" style="width:100%;max-width:42rem;height:auto;display:block" role="img" aria-label="Esquema del catálogo maestro como una fila con catorce campos agrupados en cinco bloques: identidad (id, titulo, autor), procedencia (fuente, url, fecha_documento, fecha_descarga), escena, régimen (derechos, criterio_inclusion), integridad (hash_sha256, ruta_crudo, ruta_limpio, notas). Debajo de cada bloque, la pregunta que responde.">
<style>.w4k{font-family:var(--mono);font-size:10px;letter-spacing:.05em;fill:var(--muted)} .w4c{font-family:var(--mono);font-size:10.5px;fill:var(--ink)} .w4q{font-family:var(--text);font-style:italic;font-size:11px;fill:var(--muted)} .w4f{fill:var(--surface);stroke:var(--rule);stroke-width:1} .w4o{fill:var(--surface);stroke:var(--c-inv);stroke-width:1.4} .w4t{font-family:var(--text);font-size:12px;fill:var(--ink)}</style>
<text x="16" y="22" class="w4t">Una fila del catálogo maestro. Los campos con borde verde son obligatorios.</text>
<rect x="16" y="40" width="120" height="100" rx="3" class="w4f"/><text x="24" y="58" class="w4k">IDENTIDAD</text>
<rect x="24" y="66" width="104" height="18" rx="2" class="w4o"/><text x="30" y="79" class="w4c">id</text>
<rect x="24" y="88" width="104" height="18" rx="2" class="w4o"/><text x="30" y="101" class="w4c">titulo</text>
<rect x="24" y="110" width="104" height="18" rx="2" class="w4f"/><text x="30" y="123" class="w4c">autor</text>
<text x="16" y="160" class="w4q">¿Cuál pieza es,</text><text x="16" y="174" class="w4q">sin depender de la fuente?</text>
<rect x="148" y="40" width="150" height="144" rx="3" class="w4f"/><text x="156" y="58" class="w4k">PROCEDENCIA</text>
<rect x="156" y="66" width="134" height="18" rx="2" class="w4o"/><text x="162" y="79" class="w4c">fuente</text>
<rect x="156" y="88" width="134" height="18" rx="2" class="w4o"/><text x="162" y="101" class="w4c">url</text>
<rect x="156" y="110" width="134" height="18" rx="2" class="w4o"/><text x="162" y="123" class="w4c">fecha_documento</text>
<rect x="156" y="132" width="134" height="18" rx="2" class="w4o"/><text x="162" y="145" class="w4c">fecha_descarga</text>
<text x="148" y="204" class="w4q">¿De dónde salió,</text><text x="148" y="218" class="w4q">cuándo fue hecha y cuándo tomada?</text>
<rect x="310" y="40" width="110" height="78" rx="3" class="w4f"/><text x="318" y="58" class="w4k">ESCENA</text>
<rect x="318" y="66" width="94" height="18" rx="2" class="w4o"/><text x="324" y="79" class="w4c">escena</text>
<text x="318" y="100" class="w4q">productor, género,</text><text x="318" y="112" class="w4q">sección, situación</text>
<text x="310" y="138" class="w4q">¿Quién la produjo</text><text x="310" y="152" class="w4q">y en qué situación?</text>
<rect x="432" y="40" width="130" height="100" rx="3" class="w4f"/><text x="440" y="58" class="w4k">RÉGIMEN</text>
<rect x="440" y="66" width="114" height="18" rx="2" class="w4o"/><text x="446" y="79" class="w4c">derechos</text>
<rect x="440" y="88" width="114" height="18" rx="2" class="w4o"/><text x="446" y="101" class="w4c">criterio_inclusion</text>
<text x="432" y="160" class="w4q">¿Se puede usar,</text><text x="432" y="174" class="w4q">y por qué está aquí?</text>
<rect x="16" y="232" width="546" height="56" rx="3" class="w4f"/><text x="24" y="250" class="w4k">INTEGRIDAD</text>
<rect x="24" y="258" width="130" height="18" rx="2" class="w4o"/><text x="30" y="271" class="w4c">hash_sha256</text>
<rect x="162" y="258" width="110" height="18" rx="2" class="w4o"/><text x="168" y="271" class="w4c">ruta_crudo</text>
<rect x="280" y="258" width="110" height="18" rx="2" class="w4f"/><text x="286" y="271" class="w4c">ruta_limpio</text>
<rect x="398" y="258" width="80" height="18" rx="2" class="w4f"/><text x="404" y="271" class="w4c">notas</text>
<text x="16" y="308" class="w4q">¿Es el mismo archivo que se tomó, y dónde está?</text>
<text x="580" y="60" class="w4k">14 campos</text><text x="580" y="76" class="w4k">11 obligatorios</text>
</svg>
<figcaption><b>Figura 4.</b> El esquema del catálogo maestro. Lo que hay que ver es que cada bloque responde una pregunta de la cadena de procedencia, y que un campo obligatorio vacío deja una de esas preguntas sin respuesta.</figcaption>
</figure>

7. El catálogo preliminar sale de la sesión con las piezas que el estudiante ya tiene en `crudo`, generado por el cuaderno y no a mano. Que lo genere el cuaderno es lo que lo hace reproducible: si entran veinte piezas más la semana siguiente, se ejecuta de nuevo y el catálogo crece sin que nadie copie celdas. Lo que no sale del cuaderno, como la escena o el criterio de inclusión, se completa en una tabla aparte que el cuaderno lee y une al catálogo, de modo que las decisiones a mano también queden en un archivo con fecha.

## IA y exigencia

Se le pide al modelo que proponga, a partir del protocolo del estudiante, valores de `escena` y `criterio_inclusion` para diez piezas, dándole el texto de cada una. El estudiante revisa las diez propuestas contra su lectura, acepta, corrige o rechaza cada una, y anota el resultado en una columna `propuesta_modelo` que el catálogo conserva al lado del valor decidido. Lo que debe poder defender sin la máquina es cada regla de integridad: por qué esa regla, qué falla detecta, y qué pasaría si no estuviera.

## Lecturas

**Central**

- Gibbs, G. (2012). *El análisis de datos cualitativos en investigación cualitativa*. Madrid: Morata. Cap. 3, "Preparación de los datos".
- Wilkinson, M. D. et al. (2016). "The FAIR Guiding Principles for scientific data management and stewardship". *Scientific Data* 3, 160018. https://doi.org/10.1038/sdata.2016.18

**Complementaria**

- pandas development team. *pandas: Getting started* y *10 minutes to pandas*. https://pandas.pydata.org/docs/user_guide/10min.html
- Python Software Foundation. Módulo `hashlib`. https://docs.python.org/es/3/library/hashlib.html
- Gebru, T., Morgenstern, J., Vecchione, B., Wortman Vaughan, J., Wallach, H., Daumé III, H. y Crawford, K. (2021). "Datasheets for Datasets". *Communications of the ACM* 64(12), 86-92. https://arxiv.org/abs/1803.09010
- Gitelman, L. (ed.) (2013). *"Raw Data" Is an Oxymoron*. Cambridge, MA: MIT Press. Introducción.

## Guía de lectura

- Gibbs trata la preparación de datos como una serie de decisiones sobre qué conservar del contexto de producción: quién habló, dónde, en qué condiciones. Lea su lista pensando en la columna `escena`. *¿Qué datos de la situación de producción de sus documentos se perderían si solo guardara el texto?*
- Los principios FAIR fueron escritos para datos científicos y hablan de metadatos legibles por máquinas. Traduzca cada principio al catálogo. *¿Cuál de los cuatro principios cumple hoy su carpeta `crudo` y cuál no?*
- Gitelman sostiene que no hay datos crudos: todo dato fue tomado por alguien con un criterio. El curso llama `crudo` a una carpeta sabiendo eso. *¿En qué sentido el archivo que usted descargó ya no es crudo, y dónde queda registrado ese sentido?*
- Gebru y sus coautores proponen una ficha para cada conjunto de datos con preguntas sobre motivación, composición y recolección. *¿Qué pregunta de esa ficha no puede responder hoy sobre su corpus?*

## Taller de la segunda hora

Construcción del catálogo preliminar con el cuaderno. Bloques en `practicas/cuaderno-apoyo.md`, sección "Semana 4".

1. Recorrer `crudo` y calcular el SHA-256 de cada archivo; unir el resultado a la bitácora de descarga por la ruta.
2. Asignar identificadores propios en orden de descarga.
3. Detectar duplicados exactos por hash; anotar en `notas` cuál conserva y cuál se excluye.
4. Leer la tabla de decisiones a mano (escena, criterio, derechos) y unirla al catálogo por `id`.
5. Aplicar las cinco reglas de integridad y listar las filas que fallan.
6. Guardar `catalogo.csv` y producir tres conteos: por fuente, por año, por criterio.

| Regla | Qué comprueba | Qué se rompe si falla |
|---|---|---|
| 1 | Ningún campo obligatorio vacío | Una pregunta de la cadena sin respuesta |
| 2 | Fechas en formato ISO; descarga posterior al documento | La pieza no se puede situar |
| 3 | Hash de la columna igual al recalculado | No se sabe si el archivo es el que se tomó |
| 4 | Ningún id repetido | Dos piezas se citan igual |
| 5 | Criterio de inclusión existe en el protocolo | La pieza entró sin razón escrita |

## Guion de la sesión

| Momento | Docente | Estudiante | Material |
|---|---|---|---|
| 0 a 10 min | Abre el catálogo del caso demostrativo y hace preguntas que solo él puede responder | Anota qué preguntas no responde su registro de la semana 2 | catalogo.csv del caso |
| 10 a 30 min | Expone el esquema campo por campo con la figura 4 | Marca en su registro qué campos ya tiene y cuáles faltan | Figura 4, plantilla del catálogo |
| 30 a 45 min | Deduplicación con la mini app: cambia normalizaciones en vivo | Prueba con dos textos propios casi iguales | apps/deduplicacion-hash.html |
| 45 a 60 min | Validación con la mini app: rompe registros y lee la explicación | Corrige los diez registros hasta que todos pasen | apps/validador-catalogo.html |
| 60 a 70 min | Pausa | | |
| 70 a 110 min | Acompaña la construcción del catálogo propio | Ejecuta los seis pasos del taller | cuaderno-apoyo.md, sección 4 |
| 110 a 120 min | Pide los tres conteos y los proyecta de dos estudiantes | Compara sus conteos con su protocolo | |

Notas para el docente. Lo que suele fallar: el estudiante quiere identificadores con significado y se resiste a los opacos; el ejemplo de la nota mal fechada suele convencer. El segundo fallo es la unión de tablas por `id` en pandas, donde un espacio de más deja filas sin pareja; mostrar el error y la función `strip`. El tercero es el hash que no coincide porque el archivo se abrió y guardó con un editor que cambió los finales de línea: es la mejor demostración de por qué `crudo` no se toca.

## Bitácora

El cuaderno de la sesión con el catálogo preliminar, la lista de filas que fallan las reglas y lo que piensa hacer con ellas. Las propuestas del modelo para escena y criterio, con su decisión pieza por pieza. Una pregunta abierta sobre un campo que no sabe cómo llenar para alguna fuente.

## Para la próxima semana

Leer Rawson y Muñoz (2019), "Against Cleaning", y Cordell (2017) sobre el OCR sucio. Abrir tres archivos de `crudo` y anotar todo lo que no es texto del documento: encabezados, números de página, saltos, caracteres extraños. La semana 5 decide qué hacer con eso y qué se pierde al hacerlo.
