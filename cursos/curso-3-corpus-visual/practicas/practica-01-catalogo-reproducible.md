# Práctica 1. Catálogo reproducible con deduplicación perceptual

Duración estimada: 4 horas, de las cuales 1 en la sesión sincrónica de la semana 2.
Requisitos: una lista de páginas fuente del proyecto propio, una carpeta de trabajo y la plantilla `plantillas/catalogo-visual.md`. Para la vía por programa, Python 3.11 o superior con `requests`, `Pillow`, `imagehash` y `pandas` (ver `cuaderno-apoyo.md`). Para la vía manual, una hoja de cálculo y la mini app de deduplicación.
No requiere programar: cada paso tiene una vía manual.

## Objetivo

Construir el primer catálogo de 20 imágenes del corpus propio con las diez columnas de procedencia, detectar duplicados por hash perceptual con un umbral declarado, y validar la integridad entre catálogo y disco en ambas direcciones.

## Antes de la sesión

1. Escriba la pregunta con la que reúne el corpus. Una frase. Va en la cabecera de la plantilla y se escribe antes de descargar, porque después ya no es la misma.
2. Haga la lista de páginas fuente: al menos cinco páginas de al menos dos escenas distintas (museo o archivo, prensa, plataforma). Una fila por página en la primera tabla de la plantilla.
3. Para cada sitio, abra `https://<sitio>/robots.txt` en el navegador y anote si la ruta que va a visitar está permitida. Si el archivo no existe, anótelo. Si está prohibida, no la use y anote por qué.
4. Si va por programa, instale las bibliotecas y pruebe que el bloque "comprobar robots" del cuaderno corre.

## Durante la sesión (cuatro pasos)

### Paso 1. Descargar con registro

Vía manual. Para cada imagen que quiera incorporar, guarde el archivo con un nombre numerado (`0001.jpg`, `0002.jpg`) y anote en la hoja de cálculo la URL de la imagen (clic derecho, copiar dirección de la imagen), la URL de la página, la fecha y el texto alternativo o pie si lo hay. Las dimensiones se obtienen de las propiedades del archivo.

Vía por programa. Use el bloque "descargar una página" del cuaderno. Descarga las imágenes de una página respetando `robots.txt`, con pausa entre peticiones y un agente identificado, y escribe una fila por imagen con URL, página, dimensiones y texto alternativo.

En las dos vías, no filtre todavía: descargue todo lo que la página ofrezca como imagen. El filtrado es el paso siguiente y debe quedar registrado.

### Paso 2. Filtrar lo que no es del tema

Mire las imágenes descargadas y marque las que no pertenecen al corpus: logotipos, banderas de navegación, íconos, miniaturas de otras secciones. En el caso demostrativo, una fracción visible de lo descargado era de ese tipo, con dimensiones repetidas (236 por 350 píxeles) que las delataban antes de abrirlas. Anote el criterio de descarte en la plantilla. No borre los archivos: muévalos a una carpeta `descartadas/`.

### Paso 3. Deduplicar por hash perceptual

Vía por programa. El bloque "hash perceptual" del cuaderno calcula el dHash de cada imagen y la distancia de Hamming entre todos los pares. Fije el umbral en 10 para empezar y mire los pares con distancia entre 8 y 14: ahí está la decisión.

Vía manual. Con la mini app `apps/dedup-perceptual.html` vea cómo se calcula el hash y qué hace el umbral. Luego, en su carpeta, busque a ojo los pares sospechosos (misma escena, distinto recorte o brillo) y anótelos como grupo. Es menos preciso y se declara así.

Para cada grupo, elija el ejemplar canónico y diga por qué: mayor resolución, procedencia más clara, sin recorte. Los demás se conservan con el campo `canonica = no`.

### Paso 4. Validar la integridad

Confronte el catálogo con la carpeta en ambas direcciones. Vía por programa: bloque "validar". Vía manual: cuente los archivos de la carpeta, cuente las filas, y compare nombre por nombre. Anote cada discrepancia y qué hizo con ella. Dé la cifra del corpus con su historia: cuántas bajó, cuántas descartó, cuántos grupos, cuántas quedan.

## Después de la sesión

1. Amplíe el catálogo a 40 imágenes como mínimo siguiendo los mismos cuatro pasos. Es la entrega de la semana 3.
2. Consulte la página fuente de al menos la mitad de las imágenes para llenar la columna de derechos. "Desconocido" solo vale después de mirar.
3. Marque en la columna `sensible` todas las imágenes con personas identificables, menores o muerte. Es la entrada del protocolo de la semana 7.
4. Escriba la declaración: qué hizo un programa, qué hizo un asistente de código si lo usó, qué hizo usted, qué no pudo descargar.

## Qué se evalúa

La trazabilidad, no el tamaño. Un catálogo de 40 imágenes en que cada fila tiene fuente, página, derechos consultados y grupo de duplicados vale más que uno de 400 con columnas vacías. La cifra del corpus debe poder defenderse con la validación.

## Variante para grupos

Dos estudiantes descargan desde la misma lista de páginas con procedimientos distintos (uno manual, uno por programa) y comparan catálogos. Las filas que uno tiene y el otro no son el mejor material de discusión sobre reproducibilidad.
