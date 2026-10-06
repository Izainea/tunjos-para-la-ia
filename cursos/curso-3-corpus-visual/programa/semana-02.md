# Semana 2. Recolección y catálogo

## Pregunta de la semana

¿Qué tiene que registrar un catálogo para que otra persona pueda reconstruir de dónde salió cada imagen, y cómo se sabe que dos archivos distintos son la misma imagen?

## Por qué esta semana

<p class="lede">La semana anterior separó la imagen de su dispositivo. Esta semana construye el instrumento que conserva esa separación: el catálogo. Un corpus visual sin catálogo es una carpeta; con catálogo es un conjunto de filas en las que cada imagen tiene identificador, periodo, fuente, página fuente, dimensiones, descripción heredada, derechos y escena, y en las que la pregunta "¿de dónde salió esto?" tiene respuesta sin abrir el navegador. Arnold y Tilton (2019) llaman distant viewing al estudio de grandes colecciones de imágenes con métodos computacionales y advierten que el paso previo, construir y documentar la colección, es el que decide todo lo demás. La semana enseña ese paso con el caso demostrativo, incluidos sus errores.</p>

## Contenido de la sesión

1. La descarga reproducible es la que otra persona puede repetir y obtener lo mismo. Eso exige tres cosas: una lista de páginas fuente escrita antes de descargar, un programa o un procedimiento manual que registre para cada imagen la URL del archivo y la URL de la página, y respeto por lo que el sitio permite. El archivo `robots.txt` de un sitio declara qué rutas acepta que un programa visite; un descargador que lo ignora puede estar violando los términos del sitio y, en todo caso, está tomando sin preguntar.<sup class="mark">a</sup> El curso no enseña a evadir nada: enseña a descargar despacio, identificándose, y a anotar lo que no se pudo descargar.

<aside class="glosa"><span class="mark">a</span> El protocolo de exclusión de robots está documentado en el RFC 9309 (2022). No es una ley sino una convención; que sea una convención no la hace opcional para quien quiere que su recolección sea defendible ante pares.</aside>

2. El caso demostrativo se construyó con un pipeline que, para cada página fuente de una lista por periodo, descargaba todas las imágenes y las guardaba en carpetas por subperiodo con nombres numerados, y producía un catálogo parcial por periodo. Ocho catálogos parciales, del siglo XIX a 2025, se consolidaron luego en un catálogo maestro de unas 1.800 filas con un esquema unificado. El resultado tiene virtudes y defectos que conviene ver juntos: conservó la URL de imagen y de página de casi todas las filas, pero también bajó banderas de navegación, logotipos y miniaturas que no eran del tema, porque el programa no distinguía la imagen del dispositivo.

3. El esquema del catálogo es una decisión metodológica, no técnica. El curso propone diez campos mínimos: identificador único, periodo, fuente (institución o sitio), página fuente (URL), URL de la imagen, ancho y alto en píxeles, descripción heredada (con indicación de su origen), derechos (lo que se sabe y lo que no), escena (museo, prensa, plataforma, archivo) y ruta local. A esos campos el caso añade el catálogo de origen y una marca de existencia en disco. Cada campo responde a una capa de Banks: la materialidad se mide, la narrativa externa se registra, la interna se describirá después.

4. Dos archivos pueden ser la misma imagen sin ser el mismo archivo. En el caso, una imagen de prensa de 1989 aparece cuatro veces: en el sitio del periódico, en un blog que la copió con un recorte, en una red social con el brillo subido y en una galería que la redujo a miniatura. Los cuatro archivos tienen bytes distintos y el mismo contenido. Un hash criptográfico como SHA-256 los distingue a todos; un hash perceptual los agrupa, porque resume la estructura visual de la imagen en una huella corta que cambia poco cuando la imagen cambia poco.<sup class="mark">b</sup>

<aside class="glosa"><span class="mark">b</span> El hash de diferencia (dHash) reduce la imagen a escala de grises de 9 por 8 píxeles y anota, para cada fila, si cada píxel es más claro que el siguiente: 64 bits. Dos imágenes se comparan por distancia de Hamming, el número de bits distintos. Con umbral 10 o menos, recortes leves y cambios de brillo suelen caer dentro; una imagen distinta queda muy por fuera. La biblioteca <code>imagehash</code> de Python implementa este y otros.</aside>

| Hash criptográfico (SHA-256) | Hash perceptual (dHash, pHash) |
|---|---|
| Resume los bytes del archivo. | Resume la estructura visual de la imagen. |
| Un píxel distinto cambia todo el hash. | Un recorte leve o un cambio de brillo cambian pocos bits. |
| Sirve para saber si dos archivos son idénticos. | Sirve para saber si dos archivos son la misma imagen. |
| No tiene umbral: igual o distinto. | Tiene umbral, y el umbral es una decisión del investigador. |
| *Responde "¿es el mismo archivo?"* | *Responde "¿es la misma imagen?", que es la pregunta del catálogo.* |

5. La deduplicación no borra: agrupa y decide. Que dos archivos sean la misma imagen no significa que uno sobre. El de mayor resolución es mejor materialidad; el de la red social tiene una narrativa externa que el del periódico no tiene. El catálogo conserva los dos con un campo que indique el grupo de duplicados y cuál es el ejemplar canónico. En el caso, la consolidación eliminó duplicados solo por nombre de archivo, que es la deduplicación más débil posible, y por eso el curso enseña la perceptual.

6. Validar la integridad es confrontar el catálogo con el disco en las dos direcciones. Cada fila debe tener su archivo; cada archivo debe tener su fila. El caso encontró imágenes huérfanas, presentes en disco y ausentes del catálogo, y las incorporó con los campos que se pudieron inferir de la ruta. Un catálogo que no pasó esa validación tiene un número de imágenes que nadie puede afirmar. El número es la primera cifra del informe y debe poder defenderse.

<figure class="wide">
  <svg viewBox="0 0 680 250" style="width:100%;max-width:42rem;height:auto;display:block" role="img" aria-label="Pipeline en cinco pasos del archivo al catálogo: lista de páginas fuente, descarga respetando robots con registro de URL de imagen y de página, hash perceptual y agrupación de duplicados, catálogo con diez campos, validación de integridad contra el disco en ambas direcciones. Debajo, lo que el caso demostrativo hizo mal en cada paso.">
    <style>.bx{fill:var(--surface);stroke:var(--rule);stroke-width:1.2} .t{font-family:var(--text);font-size:12.5px;fill:var(--ink)} .s{font-family:var(--text);font-size:11px;fill:var(--muted)} .k{font-family:var(--mono);font-size:9.5px;letter-spacing:.08em;fill:var(--muted)} .kf{font-family:var(--mono);font-size:9.5px;letter-spacing:.06em;fill:var(--c-fil)} .ar{stroke:var(--muted);stroke-width:1.3;fill:none} .ah{fill:var(--muted)}</style>
    <defs><marker id="s2-ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 1L9 5L0 9z" class="ah"/></marker></defs>
    <g transform="translate(10 30)"><rect width="118" height="70" rx="3" class="bx"/><text x="8" y="16" class="k">1 · LISTA</text><text x="8" y="36" class="t">Páginas fuente</text><text x="8" y="52" class="s">por periodo y escena</text></g>
    <path class="ar" d="M128 65 L146 65" marker-end="url(#s2-ah)"/>
    <g transform="translate(146 30)"><rect width="118" height="70" rx="3" class="bx"/><text x="8" y="16" class="k">2 · DESCARGA</text><text x="8" y="36" class="t">Con robots.txt</text><text x="8" y="52" class="s">URL imagen + URL página</text></g>
    <path class="ar" d="M264 65 L282 65" marker-end="url(#s2-ah)"/>
    <g transform="translate(282 30)"><rect width="118" height="70" rx="3" class="bx"/><text x="8" y="16" class="k">3 · HASH</text><text x="8" y="36" class="t">Perceptual</text><text x="8" y="52" class="s">grupos de duplicados</text></g>
    <path class="ar" d="M400 65 L418 65" marker-end="url(#s2-ah)"/>
    <g transform="translate(418 30)"><rect width="118" height="70" rx="3" class="bx"/><text x="8" y="16" class="k">4 · CATÁLOGO</text><text x="8" y="36" class="t">Diez campos</text><text x="8" y="52" class="s">una fila por imagen</text></g>
    <path class="ar" d="M536 65 L554 65" marker-end="url(#s2-ah)"/>
    <g transform="translate(554 30)"><rect width="118" height="70" rx="3" class="bx"/><text x="8" y="16" class="k">5 · VALIDAR</text><text x="8" y="36" class="t">Disco ↔ catálogo</text><text x="8" y="52" class="s">huérfanas y faltantes</text></g>
    <path class="ar" d="M69 100 L69 126"/><path class="ar" d="M205 100 L205 126"/><path class="ar" d="M341 100 L341 126"/><path class="ar" d="M477 100 L477 126"/><path class="ar" d="M613 100 L613 126"/>
    <text x="10" y="140" class="kf">EN EL CASO</text>
    <text x="10" y="156" class="s">Lista por periodo,</text><text x="10" y="170" class="s">sin escena.</text>
    <text x="146" y="156" class="s">Bajó logotipos y</text><text x="146" y="170" class="s">banderas del sitio.</text>
    <text x="282" y="156" class="s">Solo por nombre</text><text x="282" y="170" class="s">de archivo.</text>
    <text x="418" y="156" class="s">Sin derechos</text><text x="418" y="170" class="s">ni escena.</text>
    <text x="554" y="156" class="s">Halló huérfanas</text><text x="554" y="170" class="s">y las incorporó.</text>
    <text x="10" y="210" class="k">LO QUE EL CURSO AÑADE</text>
    <text x="10" y="228" class="s">escena desde la lista · filtro por dimensiones y por página · dHash con umbral · columnas de derechos y escena · validación en ambas direcciones</text>
  </svg>
  <figcaption><b>Figura 2.</b> Del archivo al catálogo en cinco pasos. Hay que ver que cada paso del caso tuvo un defecto corregible, y que el defecto del paso 3 (deduplicar solo por nombre) es el que la mini app de esta semana hace visible.</figcaption>
</figure>

7. La mini app muestra el mecanismo del hash perceptual sobre seis imágenes sintéticas. Tres son la misma escena (original, con recorte, con más brillo); dos son otra escena, con y sin marca de agua; una no tiene relación con las demás. La app calcula el hash en el navegador, muestra la distancia entre cada par y marca cuáles quedan bajo el umbral. Mueva el umbral y observe cuándo un par deja de ser duplicado: ese es el parámetro que usted tendrá que fijar y declarar en su catálogo.

<iframe class="app" src="apps/dedup-perceptual.html" title="Deduplicación perceptual: seis imágenes sintéticas, su hash y las distancias entre pares" loading="lazy"></iframe>

## IA y exigencia

Esta semana la máquina que se usa no es un modelo de lenguaje sino un programa de descarga y un algoritmo de hash, y la exigencia es la misma que con cualquier máquina: el estudiante debe poder explicar qué hace el hash, por qué dos imágenes con distancia 6 se consideran la misma y qué umbral eligió, sin ejecutar el programa. Si usa un asistente de código para escribir el descargador, declara qué partes escribió el asistente y verifica que respeta `robots.txt` leyendo el código, no confiando en que lo hace.

## Lecturas

**Central**

- Arnold, T. y Tilton, L. (2019). "Distant viewing: analyzing large visual corpora". *Digital Scholarship in the Humanities*, 34(Supplement 1), i3-i16. https://doi.org/10.1093/llc/fqz013
- Guía de la práctica 1: `practicas/practica-01-catalogo-reproducible.md`.

**Complementaria**

- Wevers, M. y Smits, T. (2020). "The visual digital turn: Using neural networks to study historical images". *Digital Scholarship in the Humanities*, 35(1), 194-207. https://doi.org/10.1093/llc/fqy085
- Koster, M., Illyes, G., Zeller, H. y Sassman, L. (2022). *Robots Exclusion Protocol*. RFC 9309. https://www.rfc-editor.org/rfc/rfc9309
- Buchner, J. *imagehash*. Biblioteca de Python para hashes perceptuales. https://github.com/JohannesBuchner/imagehash

## Guía de lectura

- Arnold y Tilton distinguen el código visual, lo que hay que saber para ver una imagen, de la anotación, lo que un algoritmo extrae de ella. Tome su corpus. *¿Qué parte del código visual de sus imágenes daría usted por obvia y no se le ocurriría anotar?*
- Los autores insisten en que el corpus debe construirse con una pregunta y documentarse antes del análisis. *¿Con qué pregunta reunió usted sus imágenes, y en qué momento la escribió: antes o después de descargar?*
- Wevers y Smits muestran que las redes neuronales reconocen tipos de imagen (fotografía, grabado, mapa) en prensa histórica con buena tasa. *¿Qué tipo de imagen de su corpus un clasificador confundiría, y por qué eso importa para su catálogo?*

## Taller de la segunda hora

Práctica 1, parte sincrónica. Guía completa en `practicas/practica-01-catalogo-reproducible.md`. En resumen:

1. Con la lista de páginas fuente del estudiante, descargar 20 imágenes registrando URL de imagen, URL de página, dimensiones y extensión. Quien no programe lo hace a mano con la hoja de cálculo de la plantilla.
2. Calcular el hash perceptual de las 20 con el cuaderno o, sin programar, con la mini app sobre pares sospechosos elegidos a ojo.
3. Llenar las diez columnas de la plantilla `plantillas/catalogo-visual.md` para las 20 imágenes.
4. Confrontar catálogo y carpeta en ambas direcciones y anotar discrepancias.

| Grupo de duplicados | Archivos | Distancia | Ejemplar canónico y por qué |
|---|---|---|---|

## Guion de la sesión

| Minuto | Momento | Qué hace el docente | Qué hace el estudiante | Material |
|---|---|---|---|---|
| 0 a 15 | Apertura | Muestra el catálogo maestro del caso, sus campos y sus filas defectuosas (logotipos, miniaturas) | Identifica qué campo habría permitido filtrar cada defecto | Esquema del catálogo del caso |
| 15 a 35 | Descarga | Expone la descarga reproducible y `robots.txt` con la figura 2 | Revisa el `robots.txt` de una de sus fuentes | Figura 2, navegador |
| 35 a 55 | Hash | Explica dHash con la mini app; cambia el umbral en vivo | Predice qué pares caerán bajo el umbral antes de verlo | Mini app |
| 55 a 60 | Pausa | | | |
| 60 a 105 | Práctica 1 | Acompaña por mesas; resuelve instalación | Descarga, calcula hash, llena el catálogo de 20 imágenes | Guía de la práctica 1, plantilla |
| 105 a 115 | Validación | Pide la cifra de cada estudiante: cuántas imágenes tiene | Confronta catálogo y carpeta y corrige la cifra | Hoja de cálculo o cuaderno |
| 115 a 120 | Cierre | Fija el alcance de la entrega de la semana 3 | Anota qué le falta para 40 imágenes | Syllabus |

Notas para el docente. Suele fallar la instalación de Pillow o `imagehash` en la sesión; pedirla la semana anterior y tener la vía manual lista. Suele fallar que los estudiantes borren duplicados en lugar de agruparlos; insistir en que el catálogo conserva ejemplares y marca el canónico. Y suele fallar que la cifra del corpus se dé antes de validar; no aceptar ninguna cifra sin la confrontación en ambas direcciones.

## Bitácora

Registre el catálogo de 20 imágenes, los grupos de duplicados con sus distancias y el umbral que eligió, las discrepancias de la validación y las imágenes que no pudo descargar y por qué. Anote qué partes del procedimiento hizo un programa y cuáles usted.

## Para la próxima semana

Leer Peirce (1894), Barthes (1964) y el capítulo 1 de Kress y van Leeuwen (2006). Ampliar el catálogo a 40 imágenes como mínimo con las diez columnas llenas: es la primera entrega. Elegir tres imágenes del catálogo en las que algo señale hacia fuera de la imagen (una huella, una firma, un gesto).
