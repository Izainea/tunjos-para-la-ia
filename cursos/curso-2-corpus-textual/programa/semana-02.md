# Semana 2. Python mínimo para humanidades

## Pregunta de la semana

¿Qué es lo menos que hay que saber de un lenguaje de programación para que un criterio escrito en prosa se convierta en un criterio que una máquina ejecuta igual cada vez?

## Por qué esta semana

<p class="lede">La semana anterior dejó una decisión escrita en prosa: qué entra al corpus y por qué. Esta semana empieza a escribirla en un lenguaje que una máquina ejecuta, y lo hace desde cero, para estudiantes que nunca han programado. El propósito no es formar programadores sino investigadores que puedan leer, modificar y defender el programa que construye su corpus. El cuaderno es la forma de registro que el curso adopta para todo: en él conviven la explicación en prosa, el código que la ejecuta y el resultado que produjo, en el orden en que ocurrieron. Un cuaderno bien llevado es a la vez el instrumento y la bitácora, y en la semana 6 se entrega como evidencia de que el catálogo se puede regenerar desde las fuentes.</p>

## Contenido de la sesión

1. El cuaderno es un documento que se ejecuta. Tiene celdas de texto, donde se explica lo que se va a hacer y por qué, y celdas de código, donde se hace. El orden importa: una celda usa lo que las anteriores definieron, y un cuaderno que solo funciona si se ejecutan las celdas en un orden que nadie anotó no es reproducible.<sup class="mark">a</sup> La primera regla del curso es reiniciar y ejecutar todo de arriba abajo antes de cerrar la sesión. Si algo falla, el cuaderno no está terminado.

<aside class="glosa"><span class="mark">a</span> El formato de cuaderno que usa el curso es el de Jupyter, un proyecto de software libre nacido en 2014 a partir de IPython. Se puede usar instalado en el propio computador o en servicios gratuitos en la nube; el curso no exige ninguno en particular.</aside>

2. Un texto, para Python, es una cadena de caracteres. Se escribe entre comillas, se guarda en una variable con un nombre que uno elige, y se le pueden hacer preguntas: cuántos caracteres tiene, si contiene cierta palabra, dónde empieza una secuencia, cómo queda en minúsculas. Esas preguntas son las mismas que un lector le hace a un documento, formuladas de modo que la máquina las responda sin interpretar. El estudiante empieza por ahí: con una nota del caso demostrativo guardada en una variable, y una docena de preguntas que la máquina contesta.

3. Una lista es una secuencia ordenada de cosas: de cadenas, de números, de otras listas. Un corpus en el cuaderno empieza siendo una lista de textos. El bucle `for` recorre la lista y hace lo mismo con cada elemento, y ahí está el primer sentido en que la máquina ejecuta un criterio: lo que el investigador haría con una pieza, el bucle lo hace con todas, igual, sin cansarse y sin fijarse en nada que el criterio no diga. Esa es su virtud y su límite, y las dos se ven en la misma sesión.

4. Un diccionario asocia nombres con valores: `{"id": "P-0001", "fuente": "El Tiempo", "fecha": "1910-03-02"}`. Es la forma natural del registro de una pieza, porque cada dato tiene nombre y el nombre dice qué es. Una lista de diccionarios es ya un catálogo rudimentario, y el salto a una tabla con pandas en la semana 4 es pequeño. Lo que el estudiante aprende esta semana es a pensar cada documento como un registro con campos, antes de pensar en la herramienta que lo guarda.

5. Leer un archivo es abrirlo, declarar cómo está codificado y cerrarlo. La codificación no es un detalle: un archivo guardado en una codificación y leído en otra convierte "año" en "aÃ±o", y el error se propaga en silencio a todo lo que venga después.<sup class="mark">b</sup> El curso adopta UTF-8 para todo y enseña a declararla siempre, en lectura y en escritura. La biblioteca `pathlib` permite recorrer una carpeta y obtener sus archivos como una lista, que es exactamente lo que hace falta para pasar de la carpeta al corpus.

<aside class="glosa"><span class="mark">b</span> UTF-8 es la codificación que representa cualquier carácter de cualquier escritura y es hoy la norma en la web. Los archivos producidos en Windows con programas antiguos suelen venir en otra, llamada Latin-1 o CP1252. La semana 5 trata el problema en detalle.</aside>

6. Una función es un criterio escrito una vez y aplicado muchas. Si el investigador decide que una nota entra al corpus cuando tiene fecha legible y más de doscientos caracteres, esa decisión se escribe como una función que recibe un texto y devuelve verdadero o falso, con un nombre que dice qué decide. La función es el lugar del cuaderno donde la prosa del protocolo se vuelve código, y por eso cada función del curso lleva arriba una celda de texto que dice qué decisión encarna y de dónde viene.

<figure class="wide">
<svg viewBox="0 0 680 250" style="width:100%;max-width:42rem;height:auto;display:block" role="img" aria-label="Cadena de transformaciones: una carpeta con archivos pasa a una lista de rutas, cada ruta se abre como cadena de texto, de cada cadena se extraen campos a un diccionario, y los diccionarios se reúnen en un registro que se escribe como CSV. Debajo, la función de inclusión actúa entre la cadena y el diccionario.">
<style>.w2k{font-family:var(--mono);font-size:10px;letter-spacing:.05em;fill:var(--muted)} .w2t{font-family:var(--text);font-size:12px;fill:var(--ink)} .w2s{font-family:var(--text);font-size:11px;fill:var(--muted)} .w2f{fill:var(--surface);stroke:var(--rule);stroke-width:1} .w2a{fill:none;stroke:var(--muted);stroke-width:1.3} .w2c{font-family:var(--mono);font-size:11px;fill:var(--c-app)} .w2d{fill:none;stroke:var(--c-fil);stroke-width:1.4;stroke-dasharray:5 4}</style>
<rect x="16" y="40" width="118" height="70" rx="3" class="w2f"/><text x="24" y="58" class="w2k">CARPETA</text><text x="24" y="78" class="w2t">crudo/</text><text x="24" y="96" class="w2s">diez archivos .txt</text>
<path class="w2a" d="M134 75 L176 75"/><path class="w2a" d="M170 70 L177 75 L170 80"/>
<rect x="178" y="40" width="118" height="70" rx="3" class="w2f"/><text x="186" y="58" class="w2k">LISTA</text><text x="186" y="78" class="w2c">[ruta, ruta, …]</text><text x="186" y="96" class="w2s">pathlib.Path.glob</text>
<path class="w2a" d="M296 75 L338 75"/><path class="w2a" d="M332 70 L339 75 L332 80"/>
<rect x="340" y="40" width="118" height="70" rx="3" class="w2f"/><text x="348" y="58" class="w2k">CADENA</text><text x="348" y="78" class="w2c">"El día de ayer…"</text><text x="348" y="96" class="w2s">open(…, encoding="utf-8")</text>
<path class="w2a" d="M458 75 L500 75"/><path class="w2a" d="M494 70 L501 75 L494 80"/>
<rect x="502" y="40" width="160" height="70" rx="3" class="w2f"/><text x="510" y="58" class="w2k">DICCIONARIO</text><text x="510" y="78" class="w2c">{"id":…, "fecha":…}</text><text x="510" y="96" class="w2s">un registro por pieza</text>
<path class="w2d" d="M399 112 L399 150"/>
<rect x="300" y="150" width="200" height="44" rx="3" class="w2f" stroke="var(--c-fil)"/><text x="310" y="168" class="w2k" fill="var(--c-fil)">FUNCIÓN DE INCLUSIÓN</text><text x="310" y="186" class="w2c">entra(texto) → True / False</text>
<text x="40" y="168" class="w2s">La decisión del protocolo,</text><text x="40" y="184" class="w2s">escrita una vez, aplicada a todas.</text>
<path class="w2a" d="M582 112 L582 150"/><path class="w2a" d="M577 144 L582 151 L587 144"/>
<rect x="522" y="150" width="140" height="44" rx="3" class="w2f"/><text x="530" y="168" class="w2k">REGISTRO</text><text x="530" y="186" class="w2c">registro.csv</text>
<text x="16" y="230" class="w2t">Cada flecha es una celda del cuaderno con su explicación arriba. Lo que entra y lo que sale se puede inspeccionar.</text>
</svg>
<figcaption><b>Figura 2.</b> Del archivo al dato en cinco pasos. Lo que hay que ver es que la función de inclusión, que encarna la decisión del protocolo, está en un lugar visible del cuaderno y no escondida en la descarga.</figcaption>
</figure>

Dos maneras de entender el cuaderno conviven en la práctica y conviene separarlas desde el principio.

| El cuaderno como borrador | El cuaderno como registro |
|---|---|
| Las celdas se ejecutan en el orden en que se le ocurrieron a uno | Las celdas se ejecutan de arriba abajo y el orden es el del argumento |
| El código está solo; lo que hace se recuerda | Cada celda de código lleva arriba la decisión que encarna |
| Si corre hoy, basta | Si no corre de nuevo desde cero, no está terminado |
| Las decisiones a mano se hacen y se olvidan | Las decisiones a mano quedan en una tabla con fecha que el cuaderno lee |
| *Produce un resultado* | *Produce un resultado y la posibilidad de reproducirlo* |

7. El registro de procedencia es el primer producto del código. Al final de la sesión, el cuaderno del estudiante recorre su carpeta `crudo`, abre cada archivo, anota su nombre, su tamaño, su número de caracteres, su primera línea y la fecha en que fue leído, y escribe todo en un archivo CSV. No es todavía el catálogo maestro, pero ya tiene su forma: una fila por pieza, una columna por dato, y un programa que lo produce de nuevo si la carpeta cambia.

## IA y exigencia

El modelo se usa esta semana como lo que mejor hace para un principiante: explicar un mensaje de error en palabras y proponer una corrección. Cada vez que el estudiante pega un error, anota en el cuaderno qué dijo el modelo y si la corrección funcionó. Lo que debe poder defender sin la máquina es cada línea del cuaderno que entregue: leerla en voz alta y decir qué hace. Una línea que no se puede explicar se borra o se aprende, pero no se entrega.

## Lecturas

**Central**

- Python Software Foundation. *El tutorial de Python*. Caps. 3 ("Una introducción informal a Python") y 7 ("Entrada y salida"). https://docs.python.org/es/3/tutorial/
- Rockwell, G. y Sinclair, S. (2016). *Hermeneutica: Computer-Assisted Interpretation in the Humanities*. Cambridge, MA: MIT Press. Cap. 1.

**Complementaria**

- Karsdorp, F., Kestemont, M. y Riddell, A. (2021). *Humanities Data Analysis: Case Studies with Python*. Princeton University Press. Cap. 1. Acceso abierto: https://www.humanitiesdataanalysis.org/
- *The Programming Historian en español*. Lecciones "Introducción a Python" y "Trabajar con archivos de texto en Python". https://programminghistorian.org/es/
- Project Jupyter. Documentación de JupyterLab. https://jupyterlab.readthedocs.io/

## Guía de lectura

- El tutorial de Python enseña con ejemplos numéricos porque fue escrito para todos los públicos. Léalo traduciendo cada ejemplo a un texto: donde dice lista de números, piense lista de notas de prensa. *¿Qué operación del capítulo 3 corresponde a algo que usted hace a mano cuando lee documentos?*
- Rockwell y Sinclair defienden que las herramientas de texto son instrumentos hermenéuticos, es decir, que participan en la interpretación en lugar de precederla. Esa tesis vale para el cuaderno. *Si el cuaderno interpreta, ¿en qué celda ocurre eso en el suyo?*
- Karsdorp y sus coautores empiezan por los formatos de datos antes que por el análisis. Note cuánto espacio le dan a la pregunta de cómo está guardado el texto. *¿En qué formato están hoy los documentos de su corpus, y quién decidió ese formato?*

## Taller de la segunda hora

Primer cuaderno, celda por celda, con el docente proyectando el suyo sobre el caso demostrativo y el estudiante escribiendo el propio sobre su carpeta `crudo`. Bloques en `practicas/cuaderno-apoyo.md`, sección "Semana 2".

1. Una celda de texto con el título del cuaderno, la fecha y la pregunta de investigación en una frase.
2. Una celda que abre un archivo con `encoding="utf-8"` y lo guarda en una variable. Preguntas a la cadena: longitud, primera línea, si contiene una palabra del tema.
3. Una celda que recorre la carpeta con `pathlib` y produce la lista de rutas.
4. Un bucle que abre cada archivo y construye un diccionario por pieza con nombre, tamaño, número de caracteres, primera línea y fecha de lectura.
5. Una función `entra(texto)` que devuelve verdadero o falso según un criterio del protocolo preliminar de la semana 1, con su celda de explicación arriba.
6. La escritura de la lista de diccionarios en `registro.csv` con el módulo `csv`.
7. Reiniciar el núcleo y ejecutar todo de arriba abajo.

| Celda | Qué explica el texto de arriba | Qué produce |
|---|---|---|
| 2 | Qué archivo es y de dónde salió | Una cadena |
| 4 | Qué campos se anotan y por qué esos | Una lista de diccionarios |
| 5 | Qué criterio del protocolo encarna | Una función |
| 6 | Dónde queda el registro | registro.csv |

## Guion de la sesión

| Momento | Docente | Estudiante | Material |
|---|---|---|---|
| 0 a 10 min | Verifica que todos tienen un cuaderno abierto; resuelve instalaciones pendientes en paralelo con un monitor | Abre el cuaderno y ejecuta `print("listo")` | Guía de instalación |
| 10 a 30 min | Cadenas: una nota del caso en una variable y doce preguntas | Repite con una nota propia | Nota del caso demostrativo |
| 30 a 45 min | Listas, bucles y diccionarios, con la figura 2 | Construye un diccionario de una pieza a mano | Figura 2 |
| 45 a 60 min | Archivos y codificación; muestra "aÃ±o" en vivo | Abre un archivo propio con dos codificaciones y compara | Archivo en CP1252 preparado |
| 60 a 70 min | Pausa | | |
| 70 a 110 min | Acompaña el primer cuaderno mesa por mesa | Escribe las siete celdas del taller | cuaderno-apoyo.md, sección 2 |
| 110 a 120 min | Pide reiniciar y ejecutar todo; muestra un registro.csv abierto | Verifica que el suyo corre de arriba abajo | |

Notas para el docente. Lo que suele fallar: la instalación. Tener listo un servicio de cuadernos en la nube para quien no logró instalar, y resolver las instalaciones después de la sesión. El segundo fallo es el estudiante que copia los bloques sin leer la celda de explicación; pedirle que la escriba con sus palabras antes de ejecutar. El tercero es la codificación: alguien tendrá archivos que no abren en UTF-8, y es la mejor ocasión para mostrar el error y anunciar la semana 5.

## Bitácora

El cuaderno de la sesión, ejecutado de arriba abajo, con las celdas de explicación completas y el `registro.csv` adjunto. Anote los errores que pegó al modelo, qué respondió y si la corrección funcionó. Añada una pregunta abierta: qué quisiera que el cuaderno hiciera y aún no sabe cómo.

## Para la próxima semana

Leer la Ley 1712 de 2014 (títulos I y II) y el documento RFC 9309 sobre el protocolo de exclusión de robots, al menos sus secciones 1 y 2. Explorar las fuentes de su corpus y anotar, para cada una, si ofrece descarga, interfaz de programación, buscador o solo navegación. Traer la ficha de delimitación de la semana 1 revisada: es la base del protocolo de corpus que se entrega.
