# Semana 5. Limpieza y normalización: lo que se pierde

## Pregunta de la semana

Cuando se limpia un texto para que la máquina lo lea, ¿qué se decide, quién lo decide y qué deja de poder verse?

## Por qué esta semana

<p class="lede">El catálogo está validado y los archivos crudos intactos. Antes de leerlos computacionalmente hay que convertirlos en texto que un programa procese igual en todas las piezas: una sola codificación, una sola forma de las tildes y las comillas, una segmentación en unidades comparables, sin encabezados ni números de página. Esa operación se llama limpieza y suele presentarse como trámite. El curso la trata como lo que es: una serie de decisiones sobre qué cuenta como texto y qué no, cada una de las cuales borra algo que podría haber sido evidencia. Rawson y Muñoz (2019) lo dicen sin rodeos: limpiar es hacer que los datos quepan en un modelo que alguien eligió. La semana enseña a limpiar bien y, sobre todo, a escribir lo que cada limpieza pierde, para que el análisis de la semana 6 sepa sobre qué está mirando.</p>

## Contenido de la sesión

1. Limpiar es decidir qué no es texto del documento. En una nota de prensa digitalizada hay texto de la nota, pero también el nombre del periódico en el encabezado, el número de página, la publicidad en la columna de al lado que el OCR mezcló, los guiones de corte de línea, y los caracteres que la digitalización inventó. Qué se quita y qué se conserva depende de la pregunta: para un estudio del léxico de las notas, el encabezado sobra; para un estudio de cómo se ubicaban las noticias en la página, el encabezado y la publicidad vecina son el dato. No hay una limpieza correcta; hay una limpieza coherente con el protocolo y escrita en el cuaderno.

2. La codificación es la primera capa y la más silenciosa. Un archivo es una secuencia de bytes; la codificación dice qué carácter representa cada secuencia. Si el archivo fue guardado en CP1252 y se lee como UTF-8, las vocales con tilde y la eñe se vuelven pares de signos sin sentido, y un programa que cuenta palabras contará "aÃ±o" como una palabra distinta de "año".<sup class="mark">a</sup> El curso enseña a detectar la codificación de origen, a convertir todo a UTF-8 una sola vez al pasar de `crudo` a `limpio`, y a verificar la conversión buscando las secuencias típicas del error.

<aside class="glosa"><span class="mark">a</span> A este fenómeno se le llama <i>mojibake</i>, palabra japonesa para los caracteres transformados. Es reconocible: donde debería haber una tilde aparece "Ã" seguida de otro signo. Una búsqueda de "Ã" en un corpus limpio debería devolver cero resultados.</aside>

3. El OCR es la segunda capa, y su error no es ruido aleatorio sino sistemático. El reconocimiento óptico de caracteres confunde lo que se parece en la tipografía de la época: la ese larga con la efe en impresos antiguos, la eñe con la ene cuando la tilde se perdió en el escaneo, la ele minúscula con el uno, las ligaduras con secuencias extrañas. Cordell (2017) muestra que el OCR sucio de los periódicos del siglo XIX es él mismo un objeto histórico: dice cómo se digitalizó, con qué prisa, con qué modelos. El curso enseña a medir cuánto error hay en una muestra leída a mano, a corregir solo lo sistemático y documentado, y a nunca corregir el crudo.

4. La normalización es la tercera capa y tiene reglas técnicas precisas. Unicode permite escribir la misma letra con tilde de dos maneras, como un carácter compuesto o como letra más tilde combinante, y un programa las cuenta como distintas si no se unifican; la forma NFC resuelve eso.<sup class="mark">b</sup> Los espacios múltiples, los saltos de línea dentro de un párrafo, las comillas tipográficas frente a las rectas, los guiones de distintas longitudes: todo eso se unifica para que las búsquedas de la semana 6 encuentren lo que buscan. Lo que no se unifica sin decisión explícita son las mayúsculas, porque distinguen nombres propios, ni las tildes, porque distinguen palabras.

<aside class="glosa"><span class="mark">b</span> La función <code>unicodedata.normalize("NFC", texto)</code> de la biblioteca estándar hace la unificación. NFC compone los caracteres; NFD los descompone. El curso usa NFC siempre y lo deja escrito en la celda de normalización.</aside>

5. Segmentar es decidir cuál es la unidad de análisis, y la decisión se hereda del protocolo. Un corpus de prensa puede analizarse por nota, por párrafo o por oración; un corpus normativo por norma, por artículo o por inciso. Cada unidad produce conteos distintos y responde preguntas distintas. El curso segmenta con expresiones regulares sencillas y guarda la segmentación como una columna más: cada unidad sabe a qué pieza del catálogo pertenece y en qué posición está. Así una concordancia de la semana 6 puede devolver no solo la línea sino el identificador y el lugar exacto, que es lo que una cita necesita.

6. Lo que se pierde se escribe. Esta es la regla que distingue el curso de un tutorial de limpieza. Cada operación del cuaderno de limpieza lleva arriba una celda que dice qué quita, por qué, y qué pregunta ya no se podrá responder con el texto limpio. Quitar los encabezados pierde la página; unificar comillas pierde la distinción entre cita y énfasis que algunos impresos marcaban con ellas; segmentar por oración pierde la frontera del párrafo; corregir el OCR pierde la huella de la digitalización. Nada de eso es un error, siempre que el crudo exista y la pérdida esté anotada.

<figure class="wide">
<svg viewBox="0 0 680 330" style="width:100%;max-width:42rem;height:auto;display:block" role="img" aria-label="Cuatro capas de limpieza de arriba abajo: crudo con mojibake y encabezados; codificación corregida; sin encabezados ni números de página; normalizado y segmentado. A la derecha de cada capa, lo que se pierde: en la primera nada; en la segunda la evidencia de cómo se guardó; en la tercera la posición en la página; en la cuarta la frontera del párrafo y la forma original de comillas y guiones.">
<style>.w5k{font-family:var(--mono);font-size:10px;letter-spacing:.05em;fill:var(--muted)} .w5c{font-family:var(--mono);font-size:10.5px;fill:var(--ink)} .w5s{font-family:var(--text);font-size:11px;fill:var(--muted)} .w5l{font-family:var(--text);font-style:italic;font-size:11px;fill:var(--c-fil)} .w5f{fill:var(--surface);stroke:var(--rule);stroke-width:1} .w5a{fill:none;stroke:var(--muted);stroke-width:1.2} .w5t{font-family:var(--text);font-size:12px;fill:var(--ink)}</style>
<text x="16" y="20" class="w5t">La misma nota en cuatro capas</text><text x="430" y="20" class="w5t">Lo que ya no se puede ver</text>
<rect x="16" y="32" width="390" height="56" rx="3" class="w5f"/><text x="24" y="48" class="w5k">CRUDO</text>
<text x="24" y="64" class="w5c">EL TIEMPO  pÃ¡g. 3   El dÃ­a de ayer se reuniÃ³ la</text><text x="24" y="80" class="w5c">junta en el saÃ³n de-   [anuncio]  sesiones del</text>
<text x="430" y="64" class="w5s">nada: todo está, aunque ilegible</text>
<path class="w5a" d="M210 88 L210 102"/><path class="w5a" d="M205 97 L210 103 L215 97"/>
<rect x="16" y="104" width="390" height="56" rx="3" class="w5f"/><text x="24" y="120" class="w5k">CODIFICACIÓN CORREGIDA (UTF-8)</text>
<text x="24" y="136" class="w5c">EL TIEMPO  pág. 3   El día de ayer se reunió la</text><text x="24" y="152" class="w5c">junta en el salón de-   [anuncio]  sesiones del</text>
<text x="430" y="136" class="w5l">cómo se guardó el archivo</text>
<path class="w5a" d="M210 160 L210 174"/><path class="w5a" d="M205 169 L210 175 L215 169"/>
<rect x="16" y="176" width="390" height="56" rx="3" class="w5f"/><text x="24" y="192" class="w5k">SIN ENCABEZADO, PAGINACIÓN NI ANUNCIO</text>
<text x="24" y="208" class="w5c">El día de ayer se reunió la junta en el salón de-</text><text x="24" y="224" class="w5c">sesiones del</text>
<text x="430" y="208" class="w5l">la página, la columna vecina,</text><text x="430" y="224" class="w5l">lo que rodeaba a la nota</text>
<path class="w5a" d="M210 232 L210 246"/><path class="w5a" d="M205 241 L210 247 L215 241"/>
<rect x="16" y="248" width="390" height="56" rx="3" class="w5f"/><text x="24" y="264" class="w5k">NORMALIZADO Y SEGMENTADO</text>
<text x="24" y="280" class="w5c">[P-0003 · oración 1] El día de ayer se reunió la</text><text x="24" y="296" class="w5c">junta en el salón de sesiones del</text>
<text x="430" y="280" class="w5l">el guion de corte, la frontera</text><text x="430" y="296" class="w5l">del párrafo, la forma original</text>
<text x="16" y="324" class="w5s">Cada flecha es una celda con su explicación y su pérdida anotada. El crudo nunca cambia.</text>
</svg>
<figcaption><b>Figura 5.</b> Qué pierde la limpieza. Lo que hay que ver es que cada capa deja el texto más legible para la máquina y menos capaz de responder una pregunta que el crudo sí respondía.</figcaption>
</figure>

Las dos actitudes ante la limpieza producen archivos parecidos y corpus distintos.

| La limpieza como trámite | La limpieza como decisión |
|---|---|
| Un patrón largo quita todo de una vez | Un patrón por operación, con antes y después |
| Se quitan tildes y mayúsculas para que las búsquedas funcionen | Las tildes y las mayúsculas se conservan salvo decisión escrita |
| El OCR se corrige donde se ve | El error de OCR se mide en una muestra y se anota por fuente |
| El crudo se edita cuando algo estorba | El crudo no se toca; el hash lo vigila |
| *El texto limpio parece el documento* | *El texto limpio sabe en qué deja de parecerse* |

7. El corpus queda en tres versiones y el catálogo sabe dónde está cada una. La carpeta `crudo` no se toca; la carpeta `limpio` tiene un archivo por pieza en UTF-8, sin lo que el protocolo declaró ajeno al texto; y una tabla de unidades, generada por el cuaderno, tiene una fila por segmento con su identificador de pieza y su posición. La columna `ruta_limpio` del catálogo apunta a la segunda; el cuaderno de limpieza es el puente entre las dos y documenta, operación por operación, lo que separa a una de otra.

## IA y exigencia

El modelo es bueno para proponer expresiones regulares y para explicar por qué una no funciona, y esta semana se usa para eso: el estudiante describe en palabras lo que quiere quitar o separar, el modelo propone el patrón, y el estudiante lo prueba sobre diez piezas y mira lo que el patrón quitó de más y de menos. También se le puede pedir que corrija OCR en un fragmento, con una condición: la corrección se compara con el crudo y se registra como propuesta, nunca se escribe sobre `limpio` sin revisión. Lo que debe poder defender sin la máquina es la lista de pérdidas: qué quitó cada operación y qué pregunta se cerró con ella.

## Lecturas

**Central**

- Rawson, K. y Muñoz, T. (2019). "Against Cleaning". En M. K. Gold y L. F. Klein (eds.), *Debates in the Digital Humanities 2019*. Minneapolis: University of Minnesota Press. Acceso abierto: https://dhdebates.gc.cuny.edu/
- Cordell, R. (2017). "'Q i-jtb the Raven': Taking Dirty OCR Seriously". *Book History* 20, 188-225. https://doi.org/10.1353/bh.2017.0006

**Complementaria**

- Python Software Foundation. Módulos `unicodedata` y `re`. https://docs.python.org/es/3/library/unicodedata.html y https://docs.python.org/es/3/library/re.html
- Python Software Foundation. *Unicode HOWTO*. https://docs.python.org/es/3/howto/unicode.html
- Drucker, J. (2011). "Humanities Approaches to Graphical Display". *Digital Humanities Quarterly* 5(1). http://www.digitalhumanities.org/dhq/vol/5/1/000091/000091.html
- *The Programming Historian en español*. Lección "Limpieza de datos con OpenRefine" y lección "Normalizar datos textuales con Python". https://programminghistorian.org/es/

## Guía de lectura

- Rawson y Muñoz escriben desde un proyecto concreto, los menús históricos de la biblioteca pública de Nueva York, y muestran que "limpiar" los nombres de los platos borraba la variación que era el objeto de estudio. *¿Qué variación de su corpus desaparecería si unificara ortografía, mayúsculas o nombres?*
- Cordell trata el error del OCR como un rastro de las condiciones de digitalización y no como basura. La actitud vale para cualquier corpus heredado. *¿Qué sabe usted de cómo fueron digitalizados sus documentos, y dónde lo va a anotar?*
- Drucker distingue datos, lo dado, de lo que ella llama capta, lo tomado. Un texto limpio es capta dos veces: tomado de la fuente y tomado del crudo. *¿Qué decisiones de toma quedan invisibles cuando alguien lee solo el texto limpio?*

## Taller de la segunda hora

Cuaderno de limpieza sobre tres piezas del caso demostrativo y luego sobre las propias. Bloques en `practicas/cuaderno-apoyo.md`, sección "Semana 5".

1. Detectar la codificación de cada archivo de `crudo` y convertir a UTF-8 en `limpio`. Buscar "Ã" en el resultado y anotar cuántas apariciones quedan.
2. Leer a mano cien palabras de una pieza con OCR y contar los errores: ese es el porcentaje de error estimado de la fuente, y va al catálogo en `notas`.
3. Quitar encabezados, paginación y restos con expresiones regulares, mostrando antes y después de cada patrón sobre una pieza.
4. Normalizar con NFC, unificar espacios, comillas y guiones. Decidir por escrito si se tocan mayúsculas y tildes, y por qué no.
5. Segmentar según la unidad del protocolo y guardar la tabla de unidades con `id`, posición y texto.
6. Escribir la tabla de pérdidas.

| Operación | Qué quita o cambia | Qué pregunta ya no se puede responder | Dónde queda el original |
|---|---|---|---|
| Conversión a UTF-8 | | | crudo |
| Encabezados y paginación | | | crudo |
| Normalización NFC y espacios | | | crudo |
| Segmentación | | | limpio |

## Guion de la sesión

| Momento | Docente | Estudiante | Material |
|---|---|---|---|
| 0 a 10 min | Proyecta una nota del caso en crudo y pregunta qué es texto de la nota | Marca en una copia impresa lo que quitaría | Nota del caso en crudo |
| 10 a 25 min | Codificación: muestra el mojibake, lo detecta y lo convierte en vivo | Repite con un archivo propio | Archivo en CP1252 |
| 25 a 40 min | OCR: lee cien palabras con el grupo y cuentan errores juntos | Anota el porcentaje | Página escaneada del caso |
| 40 a 60 min | Normalización y segmentación con la figura 5; la tabla de pérdidas | Llena la primera fila de la tabla | Figura 5 |
| 60 a 70 min | Pausa | | |
| 70 a 110 min | Acompaña el cuaderno de limpieza propio | Ejecuta los seis pasos del taller | cuaderno-apoyo.md, sección 5 |
| 110 a 120 min | Lee dos tablas de pérdidas en voz alta | Compara con la suya | |

Notas para el docente. Lo que suele fallar: el estudiante quiere limpiar todo de una vez con un patrón largo que el modelo escribió y no puede explicar; pedir un patrón por operación, con su antes y después. El segundo fallo es quitar tildes "para que las búsquedas funcionen", lo que fusiona palabras distintas; mostrar un par mínimo del propio corpus. El tercero es editar un archivo de `crudo` para corregir un error evidente; recordar que el hash del catálogo dejará de coincidir y que la regla 3 lo detectará.

## Bitácora

El cuaderno de limpieza con la tabla de pérdidas completa y el porcentaje de error de OCR por fuente. Las expresiones regulares que propuso el modelo, cuáles funcionaron y qué quitaron de más. Una pregunta abierta sobre una decisión de limpieza que no sabe si fue correcta.

## Para la próxima semana

Leer Sinclair (1991), capítulos 1 y 8, y el capítulo 1 de Moretti (2015), "Conjeturas sobre la literatura mundial". Tener el corpus propio en `limpio` con la tabla de unidades. Terminar el catálogo maestro y el cuaderno que lo regenera: se entregan en la semana 6.
