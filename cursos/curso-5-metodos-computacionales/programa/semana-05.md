# Semana 5. Tiempo: ventanas, tendencias, rupturas

## Pregunta de la semana

Cuando una serie del corpus muestra que un tema "emerge" en cierto mes, ¿qué afirma esa fecha, y cuánto se mueve si se cambia el ancho de la ventana?

## Por qué esta semana

<p class="lede">La frase "a partir de 2022 el tema aparece con fuerza" se escribe con facilidad y se sostiene con dificultad. Para escribirla hay que haber decidido qué se cuenta por periodo, cómo se normaliza ese conteo frente al tamaño del corpus en cada periodo, con qué ventana se suaviza la serie y con qué criterio se llama ruptura a un cambio. Cada una de esas decisiones mueve la fecha. Esta semana construye la serie temporal del corpus propio y muestra, con la mini app y con el cuaderno, que la emergencia de un fenómeno no es un dato de la serie sino una lectura de la serie bajo una ventana. Lo que el curso pide no es renunciar a la frase sino escribirla con sus condiciones. Además, es la semana de entrega del grafo con su lectura.</p>

La semana supone el corpus propio fechado y, de la semana 4, un grafo con su tabla de tres umbrales.

## Contenido de la sesión

1. Una serie del corpus es un conteo por periodo, y el periodo es una decisión. Contar documentos por mes o por trimestre, por año o por semana, cambia lo que se ve: una serie semanal es ruido, una anual pierde todo lo que dura menos de un año. Y el conteo crudo engaña cuando el corpus crece: si en 2023 hay el doble de documentos que en 2019, todo tema parece crecer. Por eso se cuenta la proporción de documentos del periodo que contienen el código, no el número<sup class="mark">a</sup>, y se reporta el tamaño del corpus por periodo junto a la serie.

| Conteo crudo por periodo | Proporción por periodo |
|---|---|
| "En 2023 hubo 310 documentos con el código" | "En 2023 el 14 % de los documentos tenía el código" |
| Sube cuando el corpus crece, aunque el tema no | Sube solo si el tema gana terreno dentro del corpus |
| Responde por la recolección | Responde por el fenómeno, con la recolección declarada al lado |
| Fácil de leer y fácil de confundir | Exige mostrar el tamaño del corpus por periodo |
| *Se reporta como control* | *Se lee como serie* |

<aside class="glosa"><span class="mark">a</span> Normalizar: dividir el conteo del código en el periodo por el total de documentos del periodo. Una serie normalizada responde "qué fracción del corpus habla de esto"; una cruda responde "cuántos documentos hay", que suele ser una pregunta sobre la recolección, no sobre el fenómeno.</aside>

2. Suavizar es decidir qué es ruido. El promedio móvil reemplaza cada valor por el promedio de una ventana alrededor; con ventana de un mes se ve todo, con ventana de doce se ve solo lo que dura un año. No hay ventana correcta: hay ventanas que corresponden a la escala temporal de la pregunta. Si la pregunta es sobre una campaña de dos meses, una ventana de doce la borra; si es sobre un cambio de década, una ventana de un mes la esconde entre picos.

3. Una ruptura es el output de un método de detección, con sus parámetros. El método más simple compara el promedio de los meses anteriores a un punto con el de los posteriores y marca el punto donde la diferencia es mayor; es el que usa la mini app. Los métodos de detección de puntos de cambio, como PELT (Killick, Fearnhead y Eckley, 2012), buscan varias rupturas a la vez con una penalización por cada una; el método de ráfagas de Kleinberg (2003) modela la serie como un autómata que entra y sale de estados de actividad. Los tres dan fechas distintas sobre la misma serie, y las tres fechas se mueven con la ventana<sup class="mark">b</sup>. La tabla de la mini app lo muestra: con ventanas cortas la ruptura cae en un pico de tres meses, con ventanas medias en un cambio de nivel, con ventanas largas en el inicio de una tendencia.

<aside class="glosa"><span class="mark">b</span> PELT: algoritmo que encuentra el conjunto de puntos de cambio que minimiza un costo de ajuste más una penalización por cada ruptura. Subir la penalización reduce el número de rupturas; es el equivalente, en este método, de agrandar la ventana. La biblioteca `ruptures` de Python lo implementa.</aside>

4. "Emerge" es una palabra que esconde una ventana. Un fenómeno emerge cuando su serie pasa de un nivel a otro de forma que el método usado, con la ventana usada, lo marca. Grimmer, Roberts y Stewart (2022, cap. 2) insisten en que la medida de un concepto en texto debe validarse contra la pregunta, y la fecha de emergencia es una medida como cualquier otra. La práctica de la semana pide la fecha con tres ventanas y, si se mueve más de lo que la pregunta tolera, reportar el rango y no un mes.

5. Las trampas de la serie son trampas del corpus. Un salto en 2016 puede ser el año en que el archivo empezó a digitalizar más; una caída en diciembre puede ser que el periódico no circula en vacaciones; un pico puede ser un solo documento largo que menciona el código cien veces. Antes de leer una ruptura hay que mirar la composición del corpus en los periodos que la rodean. Esa revisión no la hace el método y es, en el registro de frontera, un paso del investigador.

6. Leer una serie es configurar una trama, y la trama no viene en la serie. Con la triple mímesis de *Tiempo y narración* (Ricœur, 1995), la serie es material prefigurado; el investigador que dice "primero fue así, luego ocurrió esto y desde entonces aquello" está configurando, Mímesis II, y la configuración exige un relato que la serie no contiene. Un modelo de lenguaje puede proponer ese relato con una fluidez que tienta; el curso pide que el relato se escriba con la ventana declarada y con la lista de lo que la serie no puede decir.

<figure class="wide">
  <svg viewBox="0 0 680 240" style="width:100%;max-width:42rem;height:auto;display:block" role="img" aria-label="La misma serie mensual dibujada dos veces. Arriba, suavizada con ventana de dos meses: el marcador de ruptura cae en un pico breve. Abajo, suavizada con ventana de nueve meses: el pico desaparece y el marcador cae en un cambio de nivel posterior. Un rótulo dice que la fecha de emergencia depende de la ventana.">
    <style>.m5{font-family:var(--mono);font-size:10.5px;letter-spacing:.06em;fill:var(--muted)} .mf5{font-family:var(--mono);font-size:10.5px;letter-spacing:.06em;fill:var(--c-fil)} .bx{fill:var(--surface);stroke:var(--rule);stroke-width:1.2} .ln{fill:none;stroke:var(--accent);stroke-width:2.2} .raw{fill:none;stroke:var(--muted);stroke-width:1;stroke-opacity:.5} .rp{stroke:var(--c-fil);stroke-width:1.8;stroke-dasharray:5 4} .ax{stroke:var(--rule);stroke-width:1}</style>
    <rect x="10" y="22" width="660" height="92" rx="3" class="bx"/>
    <text x="18" y="16" class="m5">VENTANA 2 MESES</text>
    <line x1="30" y1="100" x2="660" y2="100" class="ax"/>
    <path class="raw" d="M30 80 L55 84 L80 78 L105 86 L130 82 L155 88 L180 84 L205 90 L230 60 L245 40 L260 44 L275 70 L300 88 L325 92 L350 86 L375 70 L400 62 L425 66 L450 60 L475 64 L500 58 L525 62 L550 56 L575 60 L600 54 L625 58 L650 52"/>
    <path class="ln" d="M30 82 L80 82 L130 84 L180 86 L210 80 L235 52 L255 42 L280 62 L310 88 L350 88 L390 66 L450 62 L520 60 L590 57 L650 54"/>
    <line x1="238" y1="30" x2="238" y2="100" class="rp"/>
    <text x="244" y="40" class="mf5">RUPTURA: DIC 2020</text>
    <rect x="10" y="134" width="660" height="92" rx="3" class="bx"/>
    <text x="18" y="128" class="m5">VENTANA 9 MESES</text>
    <line x1="30" y1="212" x2="660" y2="212" class="ax"/>
    <path class="raw" d="M30 192 L55 196 L80 190 L105 198 L130 194 L155 200 L180 196 L205 202 L230 172 L245 152 L260 156 L275 182 L300 200 L325 204 L350 198 L375 182 L400 174 L425 178 L450 172 L475 176 L500 170 L525 174 L550 168 L575 172 L600 166 L625 170 L650 164"/>
    <path class="ln" d="M30 194 L100 195 L170 194 L230 186 L280 184 L330 188 L380 180 L430 174 L490 172 L550 169 L610 167 L650 165"/>
    <line x1="392" y1="142" x2="392" y2="212" class="rp"/>
    <text x="398" y="152" class="mf5">RUPTURA: MAY 2022</text>
    <text x="30" y="238" class="m5">MISMA SERIE · DOS VENTANAS · DOS FECHAS DE EMERGENCIA</text>
  </svg>
  <figcaption><b>Figura 5.</b> La misma serie con dos ventanas. Con ventana corta el método marca un pico de tres meses; con ventana larga el pico desaparece y el método marca un cambio de nivel año y medio después. Ninguna de las dos fechas es falsa; ninguna es "la" fecha.</figcaption>
</figure>

<iframe class="app" src="apps/serie-ventana.html" title="Serie temporal del corpus con ventana móvil y marcador de ruptura" loading="lazy"></iframe>

## IA y exigencia

Se le pide a un modelo de lenguaje el código para construir la serie normalizada y para correr dos métodos de detección de rupturas a partir del cuaderno, y después se le pide un relato de la serie en un párrafo. El estudiante debe poder defender sin el modelo el periodo y la normalización elegidos, la fecha de ruptura con tres ventanas y su rango, y qué de la composición del corpus revisó antes de aceptar la ruptura. El relato del modelo se registra como configuración propuesta por la máquina, y el estudiante marca en él cada frase que la serie no sostiene.

## Lecturas

**Central**

- Kleinberg, J. (2003). "Bursty and Hierarchical Structure in Streams". *Data Mining and Knowledge Discovery* 7(4), 373-397. Secciones 1 y 2. https://doi.org/10.1023/A:1024940629314
- Grimmer, J., Roberts, M. E. y Stewart, B. M. (2022). *Text as Data*. Princeton University Press. Cap. 2, sobre investigación social y análisis de texto.

**Complementaria**

- Killick, R., Fearnhead, P. y Eckley, I. A. (2012). "Optimal Detection of Changepoints With a Linear Computational Cost". *Journal of the American Statistical Association* 107(500), 1590-1598. https://doi.org/10.1080/01621459.2012.737745
- Truong, C., Oudre, L. y Vayatis, N. (2020). "Selective Review of Offline Change Point Detection Methods". *Signal Processing* 167, 107299. https://doi.org/10.1016/j.sigpro.2019.107299
- Ricœur, P. (1995). *Tiempo y narración I*. Siglo XXI. Cap. 3, "Tiempo y narración: la triple mímesis".

## Guía de lectura

- Kleinberg modela una ráfaga como un cambio de estado en un autómata, con un parámetro que controla cuánto cuesta cambiar de estado. *¿Qué pasa con las ráfagas detectadas si ese costo sube? ¿Cuál es el equivalente de ese parámetro en el promedio móvil?*
- Grimmer, Roberts y Stewart distinguen descubrir, medir e inferir como tareas con validaciones distintas. *La fecha de emergencia de un tema, ¿es un descubrimiento, una medida o una inferencia? ¿Qué validación le corresponde?*
- Ricœur describe la configuración como el acto de hacer de una sucesión una trama. *Tome la serie de su corpus y escriba su trama en tres frases. Luego subraye lo que la serie no puede sostener por sí sola.*

## Taller de la segunda hora

Primera parte, sobre la serie del corpus propio, con el bloque de la semana 5 del cuaderno de apoyo:

1. Construya la serie mensual o trimestral de un código o de un grupo de la semana 3, normalizada por el tamaño del corpus en el periodo. Grafique la serie y, debajo, el tamaño del corpus por periodo.
2. Suavice con tres ventanas y detecte la ruptura con el método de diferencia de medias y con PELT. Llene la tabla:

| Ventana | Ruptura (diferencia de medias) | Ruptura (PELT) | ¿La composición del corpus cambia alrededor? |
|---|---|---|---|

3. Escriba la fecha o el rango de emergencia con sus condiciones, en una frase que pueda ir en un informe.

Segunda parte: terminar la lectura del grafo sobre la plantilla `plantillas/lectura-de-grafo.md` con la tabla de tres umbrales de la semana anterior.

## Guion de la sesión

| Minuto | Momento | Docente | Estudiante | Material |
|---|---|---|---|---|
| 0 a 10 | Apertura | Lee en voz alta una frase de informe con "emerge" y pregunta qué ventana la sostiene | Anota la escala temporal de su pregunta | Tablero |
| 10 a 30 | Lectura | Explica ráfagas y puntos de cambio por lo que detectan; discute la guía | Responde con su serie en mente | Lecturas centrales |
| 30 a 50 | Mecanismo | Mueve la ventana de la mini app de 1 a 12 y lee la tabla de rupturas | Predice dónde caerá la ruptura con ventana 9 | App de serie |
| 50 a 60 | Pausa | | | |
| 60 a 95 | Taller | Acompaña la serie normalizada y las tres ventanas sobre corpus propios | Llena la tabla y escribe la frase de emergencia | Cuaderno, semana 5 |
| 95 a 115 | Entrega | Revisa lecturas de grafo en parejas: cada uno lee la del otro y marca una afirmación que el grafo no sostiene | Corrige la lectura de grafo | Plantilla de lectura de grafo |
| 115 a 120 | Cierre | Recoge rangos de emergencia | Nombra su rango | Bitácora |

Notas para el docente. Lo que suele fallar: el corpus tiene fechas incompletas o en formatos mezclados y la mitad del taller se va en limpiarlas; pedir las fechas limpias desde la semana anterior. Segundo fallo: la serie cruda y la normalizada cuentan historias opuestas y el estudiante elige la que le conviene; exigir las dos en la bitácora. Tercero: la revisión en parejas de la lectura de grafo se vuelve cortesía; dar la instrucción de que cada revisor debe encontrar al menos una afirmación sin sostén, y que no encontrarla es la excepción.

## Entrega

Grafo de coocurrencia con lectura interpretativa, sobre la plantilla `plantillas/lectura-de-grafo.md`, con la tabla de tres umbrales, las dos imágenes del grafo y el código o los pasos en anexo. Se evalúa que la lectura distinga lo que la red muestra de lo que el investigador propone, que declare qué cambia con el umbral, y que cada puente leído tenga su apoyo nombrado: corpus, teoría o ninguno todavía. Rúbrica en `evaluacion.md`.

## Para la próxima semana

Leer Blei (2012) completo, Moretti (2015), "Conjeturas sobre la literatura mundial", y Arnold y Tilton (2019). Llegar con el corpus en la forma de la semana 1, una fila por documento, para modelar temas. Quien trabaja con imágenes llega con las descripciones densas del curso 3 o con las etiquetas de CLIP del cuaderno.
