# Semana 3. Recolección legal y reproducible

## Pregunta de la semana

¿Cómo se recolecta un corpus de modo que otro pueda repetir la recolección y obtener lo mismo, sin tomar lo que no se puede tomar?

## Por qué esta semana

<p class="lede">Con un cuaderno que lee archivos y una delimitación escrita, el estudiante está listo para la operación que más se automatiza y que más se malentiende: traer los documentos desde la fuente. La automatización que el curso enseña no sirve para descargar más, sirve para descargar igual. Un programa de recolección es la forma ejecutable del protocolo: dice de dónde, con qué criterio, a qué ritmo y qué no. Otro investigador lo corre y obtiene el mismo corpus o una diferencia que el programa mismo detecta. Esta semana cierra el primer producto, el protocolo de corpus, porque solo ahora el estudiante sabe lo suficiente sobre sus fuentes para escribir cómo va a recolectarlas.</p>

## Contenido de la sesión

1. Las fuentes se distinguen por cómo entregan sus documentos, y esa distinción decide el programa. Los repositorios de acceso abierto y las bibliotecas digitales ofrecen descarga directa de archivos; las hemerotecas digitales, como la de la Biblioteca Nacional de Colombia, ofrecen visores y a veces descarga por número; los portales de datos abiertos como datos.gov.co ofrecen conjuntos de datos en CSV y una interfaz de programación; muchos sitios de entidades públicas ofrecen solo páginas web que hay que leer con un programa.<sup class="mark">a</sup> El protocolo de corpus registra, para cada fuente, cuál de estas formas usa, porque de ella dependen el método, el ritmo y los derechos.

<aside class="glosa"><span class="mark">a</span> Una interfaz de programación de aplicaciones, o API, es una dirección a la que un programa pide datos y recibe una respuesta estructurada, casi siempre en formato JSON. Es la forma de recolección más limpia porque la fuente misma la diseñó para eso; datos.gov.co la ofrece para todos sus conjuntos.</aside>

2. La descarga es un criterio escrito, no una aspiradora. El programa que recolecta recibe la lista de lo que el protocolo dice que entra (un rango de fechas, un periódico, una categoría de norma, una consulta en el buscador) y trae exactamente eso. Lo que se trae de más "por si acaso" no es corpus: es carpeta, y vuelve a plantear el problema de la semana 1. El curso enseña a escribir primero la lista de lo que se va a pedir, revisarla a mano, y solo después ejecutar la descarga.

3. Descargar de un sitio es entrar en una relación con quien lo mantiene, y esa relación tiene reglas escritas. El archivo `robots.txt` de cada sitio dice qué partes acepta que los programas visiten; el documento RFC 9309 de 2022 fija su formato. Los términos de uso dicen qué se puede hacer con lo descargado. Y la cortesía técnica tiene forma concreta: identificarse en cada petición con un nombre y un correo, esperar entre peticiones, no repetir lo que ya se tiene, y detenerse ante un error en lugar de insistir.<sup class="mark">b</sup> Un programa que ignora esto puede tumbar un servidor pequeño de un archivo regional, y ese es un daño que el investigador causa.

<aside class="glosa"><span class="mark">b</span> Un segundo de espera entre peticiones es un ritmo razonable para la mayoría de sitios públicos; mil documentos tardan diecisiete minutos. La prisa por descargar en menos no tiene justificación en investigación.</aside>

4. Hay cosas que no se descargan, y la lista se escribe en el protocolo. No se descargan documentos con datos personales de personas vivas cuando el proyecto no tiene cómo tratarlos conforme a la Ley 1581 de 2012; no se descarga lo que los términos del sitio prohíben reproducir; no se descarga lo que está detrás de una suscripción o una credencial de acceso ajena; no se descarga lo que el protocolo no incluyó. Para cada uno de estos casos el curso ofrece una alternativa legítima: pedir el conjunto por solicitud de acceso a la información bajo la Ley 1712 de 2014, recolectar a mano con registro, o trabajar con una muestra que sí se puede tomar.

5. El archivo crudo es intocable. Lo que llega de la fuente se guarda tal como llegó, en una carpeta `crudo` que no se edita nunca, con tres datos que lo acompañan desde ese instante: la dirección de donde vino, la fecha y hora de la descarga, y una huella criptográfica del contenido.<sup class="mark">c</sup> Todo lo que el curso hace después (limpiar, segmentar, normalizar) produce copias en otras carpetas. Si algo sale mal en cualquier paso, siempre se puede volver al crudo y repetir.

<aside class="glosa"><span class="mark">c</span> La huella, o hash, es una cadena corta calculada a partir del contenido completo del archivo. Dos archivos idénticos tienen la misma huella; un solo carácter distinto produce una huella distinta. El curso usa SHA-256, disponible en la biblioteca estándar de Python. La semana 4 la usa para detectar duplicados.</aside>

6. Reproducible quiere decir que el cuaderno de recolección, ejecutado por otra persona en otra máquina, produce el mismo corpus o explica la diferencia. Las fuentes cambian: una nota se corrige, un conjunto de datos se actualiza, una página desaparece. El hash detecta el cambio; la bitácora de descarga, que registra cada petición con su resultado, permite decir qué cambió y cuándo. Reproducible no es inmutable: es trazable.

<figure class="wide">
<svg viewBox="0 0 680 290" style="width:100%;max-width:42rem;height:auto;display:block" role="img" aria-label="Cadena de recolección: el protocolo produce una lista de lo que se pide; el programa hace peticiones identificadas y con pausa a la fuente, respetando robots.txt; cada respuesta se guarda intacta en la carpeta crudo con URL, fecha y hash, y cada petición se anota en la bitácora de descarga. Un cuadro aparte lista lo que no se descarga.">
<style>.w3k{font-family:var(--mono);font-size:10px;letter-spacing:.05em;fill:var(--muted)} .w3t{font-family:var(--text);font-size:12px;fill:var(--ink)} .w3s{font-family:var(--text);font-size:11px;fill:var(--muted)} .w3f{fill:var(--surface);stroke:var(--rule);stroke-width:1} .w3a{fill:none;stroke:var(--muted);stroke-width:1.3} .w3c{font-family:var(--mono);font-size:10.5px;fill:var(--c-app)} .w3n{fill:none;stroke:var(--c-fil);stroke-width:1.2;stroke-dasharray:5 4} .w3r{font-family:var(--mono);font-size:10px;fill:var(--c-fil)}</style>
<rect x="16" y="30" width="140" height="64" rx="3" class="w3f"/><text x="24" y="48" class="w3k">PROTOCOLO</text><text x="24" y="68" class="w3t">lista de lo que se pide</text><text x="24" y="84" class="w3s">revisada a mano</text>
<path class="w3a" d="M156 62 L196 62"/><path class="w3a" d="M190 57 L197 62 L190 67"/>
<rect x="198" y="30" width="150" height="64" rx="3" class="w3f"/><text x="206" y="48" class="w3k">PROGRAMA</text><text x="206" y="68" class="w3t">petición identificada</text><text x="206" y="84" class="w3s">pausa de 1 s · robots.txt</text>
<path class="w3a" d="M348 62 L388 62"/><path class="w3a" d="M382 57 L389 62 L382 67"/>
<rect x="390" y="30" width="110" height="64" rx="3" class="w3f"/><text x="398" y="48" class="w3k">FUENTE</text><text x="398" y="68" class="w3t">responde</text><text x="398" y="84" class="w3s">o rechaza</text>
<path class="w3a" d="M445 94 L445 130"/><path class="w3a" d="M440 124 L445 131 L450 124"/>
<rect x="340" y="132" width="220" height="80" rx="3" class="w3f"/><text x="348" y="150" class="w3k">CRUDO (no se edita)</text><text x="348" y="170" class="w3c">url · fecha_descarga · sha256</text><text x="348" y="188" class="w3t">el archivo tal como llegó</text><text x="348" y="204" class="w3s">todo lo demás es copia</text>
<path class="w3a" d="M273 94 L273 160 L338 160"/><path class="w3a" d="M332 155 L339 160 L332 165"/>
<rect x="110" y="132" width="150" height="80" rx="3" class="w3f"/><text x="118" y="150" class="w3k">BITÁCORA</text><text x="118" y="170" class="w3t">una fila por petición</text><text x="118" y="188" class="w3s">qué, cuándo, resultado,</text><text x="118" y="204" class="w3s">hash o error</text>
<path class="w3a" d="M273 94 L273 160 L262 160"/>
<rect x="16" y="226" width="544" height="50" rx="3" class="w3n"/>
<text x="26" y="246" class="w3r">NO SE DESCARGA</text>
<text x="26" y="264" class="w3s">datos personales sin tratamiento previsto · lo que los términos prohíben · lo que está tras una credencial ajena · lo que el protocolo no incluyó</text>
<text x="580" y="160" class="w3s" transform="rotate(90 580 160)">trazable</text>
</svg>
<figcaption><b>Figura 3.</b> La recolección reproducible. Lo que hay que ver es que el archivo crudo nace con su dirección, su fecha y su huella, y que la lista de lo que no se descarga es parte del programa, no una nota al margen.</figcaption>
</figure>

La diferencia entre las dos formas de descargar no está en la herramienta sino en qué se escribe antes.

| Descargar como aspiradora | Descargar como criterio |
|---|---|
| Se trae todo lo que el sitio deja traer | Se trae lo que la lista revisada a mano dice |
| El criterio de inclusión se aplica después, sobre la carpeta | El criterio de inclusión está en la lista, antes de pedir |
| No hay bitácora: lo que hay es lo que hay | Cada petición tiene fila, fecha, resultado y hash |
| Lo que no se debía tomar ya está tomado | Lo que no se toma está escrito y tiene alternativa |
| *Otro no puede repetirlo ni saber qué falta* | *Otro lo repite y explica la diferencia* |

7. El protocolo de corpus se entrega esta semana porque reúne lo aprendido en las tres primeras: la delimitación y los criterios de Valles de la semana 1, el registro con campos de la semana 2, y las fuentes, el método y los límites de recolección de esta. Es un documento de dos a cuatro páginas, con la plantilla de `plantillas/protocolo-de-corpus.md`, que otro investigador podría leer y ejecutar. El cuaderno de recolección, que se escribe en el taller, es su anexo.

## IA y exigencia

El modelo puede escribir la primera versión de una función de descarga, y esta semana se le pide eso: a partir de la descripción de una fuente, proponer el código que pide un documento, espera, lo guarda en `crudo` y anota la bitácora. El estudiante lee ese código línea por línea antes de ejecutarlo, verifica que respeta la pausa, que se identifica y que no toca nada fuera de la lista, y anota en el cuaderno qué corrigió. Lo que debe poder defender sin la máquina es la lista de lo que pidió y la lista de lo que no: ninguna de las dos la puede escribir el modelo.

## Lecturas

**Central**

- Congreso de Colombia. Ley 1712 de 2014, Ley de Transparencia y del Derecho de Acceso a la Información Pública Nacional. Títulos I y II. http://www.secretariasenado.gov.co/senado/basedoc/ley_1712_2014.html
- Congreso de Colombia. Ley 1581 de 2012, protección de datos personales. Títulos I a III. http://www.secretariasenado.gov.co/senado/basedoc/ley_1581_2012.html
- Koster, M., Illyes, G., Zeller, H. y Sassman, L. (2022). *Robots Exclusion Protocol*. RFC 9309. Internet Engineering Task Force. Secciones 1 y 2. https://www.rfc-editor.org/rfc/rfc9309

**Complementaria**

- Congreso de Colombia. Ley 23 de 1982, sobre derechos de autor. Arts. 1 a 45. http://www.secretariasenado.gov.co/senado/basedoc/ley_0023_1982.html
- Reitz, K. y colaboradores. *Requests: HTTP for Humans*. Documentación. https://requests.readthedocs.io/
- Richardson, L. *Beautiful Soup Documentation*. https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- Gobierno de Colombia. Portal de datos abiertos. https://www.datos.gov.co/
- *The Programming Historian en español*. Lección "Descargar páginas web con Python". https://programminghistorian.org/es/

## Guía de lectura

- La Ley 1712 parte del principio de que la información pública es pública por defecto y que la reserva es la excepción que la entidad debe justificar. Eso cambia la posición del investigador: puede pedir. *¿Qué conjunto de documentos de su proyecto podría pedir por solicitud de acceso en lugar de descargarlo pieza por pieza?*
- La Ley 1581 define dato personal, dato sensible y tratamiento, y hace responsable a quien recolecta. Léala pensando en el archivo `crudo`: guardar ya es tratar. *¿Qué piezas de su corpus contienen datos personales, y tiene el proyecto una base para tratarlos?*
- El RFC 9309 es corto y técnico. Lo que interesa es su lógica: el sitio declara, el programa obedece, y lo que no está declarado no está permitido por omisión sino sujeto a juicio. *Abra el `robots.txt` de una de sus fuentes. ¿Qué dice sobre lo que usted quiere descargar?*

## Taller de la segunda hora

Primera recolección reproducible sobre el caso demostrativo y luego sobre una fuente propia. Guía completa en `practicas/practica-03-recoleccion-reproducible.md`; bloques en `practicas/cuaderno-apoyo.md`, sección "Semana 3".

1. Leer el `robots.txt` de datos.gov.co y de la Secretaría del Senado y anotar qué permiten.
2. Pedir un conjunto de datos de datos.gov.co por su interfaz de programación, guardarlo en `crudo` con su dirección, fecha y hash, y anotar la bitácora.
3. Pedir una norma de la Secretaría del Senado como página web, con identificación y pausa, y guardarla intacta.
4. Repetir con una fuente propia, sobre una lista de no más de diez piezas revisada a mano.
5. Cerrar el cuaderno, reiniciar y ejecutar todo. Comparar los hash de la segunda ejecución con los de la primera.

| Fuente | Forma de entrega | robots.txt permite | Ritmo | Qué no se toma |
|---|---|---|---|---|
| datos.gov.co | Interfaz de programación y CSV | | | |
| Secretaría del Senado | Páginas web | | | |
| Fuente propia 1 | | | | |

## Guion de la sesión

| Momento | Docente | Estudiante | Material |
|---|---|---|---|
| 0 a 10 min | Retoma tres fichas de delimitación y pregunta cómo entregan sus fuentes | Clasifica sus fuentes por forma de entrega | Fichas de la semana 1 |
| 10 a 30 min | Expone las formas de entrega y la descarga como criterio escrito | Escribe la lista de lo que pediría a una fuente | |
| 30 a 45 min | Lee en vivo dos `robots.txt` y los términos de un sitio; expone la cortesía técnica | Abre el `robots.txt` de una fuente propia | Navegador |
| 45 a 60 min | Expone lo que no se descarga y las alternativas; el crudo intocable y el hash | Marca en su ficha lo que no puede tomar | Figura 3 |
| 60 a 70 min | Pausa | | |
| 70 a 110 min | Ejecuta la recolección del caso y acompaña la propia | Escribe y corre el cuaderno de recolección | practica-03 |
| 110 a 120 min | Cierra con la comparación de hash entre dos ejecuciones | Anota diferencias si las hubo | |

Notas para el docente. Lo que suele fallar: la red del aula bloquea peticiones o el sitio responde con error; tener los archivos del caso descargados de antemano en una carpeta compartida para que el taller continúe. El segundo fallo es el estudiante que quiere descargar todo un sitio "ya que está"; devolverlo a la lista revisada a mano. El tercero es el código propuesto por el modelo sin pausa ni identificación: pedir que se lea en voz alta antes de ejecutar, siempre.

## Entrega

Protocolo de corpus, con la plantilla de `plantillas/protocolo-de-corpus.md` y el cuaderno de recolección como anexo. Se evalúa que la delimitación esté argumentada con los cuatro criterios, que las exclusiones estén escritas, que cada fuente tenga forma de entrega, régimen de derechos y método de recolección, y que la lista de lo que no se descarga exista. Un protocolo que dice "se descargará todo lo disponible" no está en nivel Básico.

## Para la próxima semana

Leer el capítulo 3 de Gibbs (2012) sobre preparación de datos y el artículo de Wilkinson y coautores (2016) sobre los principios FAIR. Tener en `crudo` al menos veinte piezas del corpus propio, con bitácora de descarga. Revisar el esquema de campos del registro de la semana 2: la semana 4 lo convierte en el catálogo maestro.
