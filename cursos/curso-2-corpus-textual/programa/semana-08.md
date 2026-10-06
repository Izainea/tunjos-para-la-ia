# Semana 8. El corpus como aserción

## Pregunta de la semana

¿Qué tiene que contener la documentación de un corpus para que otro investigador lo reconstruya, lo cuestione y, si quiere, lo corrija?

## Por qué esta semana

<p class="lede">El curso termina donde empezó, con la tesis de que un corpus es una decisión documentada, y la lleva a su consecuencia: una decisión documentada es una aserción. Cuando el estudiante entrega su informe está afirmando algo ante una comunidad: que estos documentos, delimitados así, recolectados así, limpiados así y leídos así, son el material sobre el que va a sostener lo que diga después. Esa afirmación tiene los tres sentidos de validación que el programa distingue. Es correcta si el catálogo pasa sus reglas y los hash coinciden. Está justificada si el proceso se puede seguir paso a paso en el cuaderno. Y es imputable si alguien la firma y responde por la frontera que trazó. La máquina puede ayudar con los dos primeros sentidos; el tercero es del estudiante, y la presentación ante pares de esta sesión es su forma práctica.</p>

## Contenido de la sesión

1. Un corpus es una aserción con la forma "esto es lo que hay sobre X, delimitado así", y como toda aserción levanta pretensiones que alguien tiene que poder defender. Las tres preguntas que un par le hará al estudiante son las tres que el programa llama sentidos de validación. ¿Es correcto? Los hash coinciden, las fechas son válidas, no hay duplicados: eso lo verifica el cuaderno. ¿Está justificado? Cada decisión tiene su celda de explicación y su pérdida anotada: eso lo muestra el cuaderno. ¿Quién responde? De eso no hay celda posible; hay una persona que presenta y contesta.

2. Reconstruir quiere decir que otra persona, con la documentación y sin hablar con el autor, obtiene el mismo corpus o explica la diferencia. El curso fija una estructura de carpeta para eso: un `README` que dice la pregunta, la frontera y cómo ejecutar; el protocolo; el catálogo; los cuadernos de recolección, catálogo, limpieza y lectura; las carpetas `crudo` y `limpio` cuando los derechos lo permiten, o solo el catálogo y el cuaderno de recolección cuando no; el registro de frontera; y un archivo que lista las versiones de Python y de las bibliotecas usadas.<sup class="mark">a</sup> La estructura no es burocracia: es el orden en que un lector va a buscar las respuestas.

<aside class="glosa"><span class="mark">a</span> El archivo se llama por convención <code>requirements.txt</code> y lo produce el comando <code>pip freeze</code>. Sin él, un cuaderno que hoy corre puede dejar de correr en dos años porque una biblioteca cambió. Es la parte más barata de la reproducibilidad y la que más se olvida.</aside>

3. La declaración de datos es la forma que Bender y Friedman (2018) propusieron para documentar un conjunto de textos en procesamiento de lenguaje, y el curso la adapta al corpus de humanidades. Pide escribir la razón de la curaduría, es decir, por qué estos textos y no otros; la variedad de lengua, que en un corpus colombiano de prensa histórica no es un detalle; quiénes produjeron los textos y en qué situación; las características del texto, como género, extensión y periodo; y la procedencia, con sus derechos. Cada pregunta de la declaración tiene su respuesta en algún documento del curso: el protocolo, el catálogo o la tabla de pérdidas. La declaración las reúne en dos páginas al principio del informe.

4. Qué se publica lo decide el régimen de derechos de cada pieza, registrado en el catálogo desde la semana 4. El catálogo mismo se publica siempre, porque los metadatos de un documento no son el documento. Los textos de dominio público y las normas oficiales se publican con el corpus. Los textos bajo derechos de autor no se publican, pero el cuaderno de recolección sí, de modo que otro pueda volver a tomarlos de la fuente. Los textos con datos personales no se publican ni se conservan más allá de lo que el proyecto necesita, y el informe dice cómo se trataron.<sup class="mark">b</sup> La licencia del corpus publicado se declara en el `README`; el curso recomienda una licencia abierta para el catálogo y los cuadernos.

<aside class="glosa"><span class="mark">b</span> El curso 7 del programa trata estos problemas con detalle, incluidos los corpus de relatos sensibles. Aquí basta con que el informe tenga una sección que diga, pieza por pieza o por grupo, qué se publica, qué no y por qué.</aside>

5. Lo que queda abierto se declara abierto, y eso distingue un informe de corpus de una nota de método. El informe dice qué fuentes no se pudieron recolectar y por qué; qué porcentaje de error de OCR tiene cada fuente y sobre qué muestra se estimó; qué pérdidas de la limpieza podrían importar para preguntas distintas de la del proyecto; qué tasa de acuerdo tuvo la lectura asistida y qué categorías fallaron; y qué parte del corpus no se leyó. Un informe que no tiene esta sección está afirmando más de lo que sabe, y un par lo va a notar.

<figure class="wide">
<svg viewBox="0 0 680 300" style="width:100%;max-width:42rem;height:auto;display:block" role="img" aria-label="Las capas de documentación de un corpus reconstruible, de arriba abajo: README con pregunta y frontera; protocolo; catálogo maestro; cuadernos de recolección, catálogo, limpieza y lectura; carpetas crudo y limpio según derechos; registro de frontera; requirements. A la derecha, otro investigador con tres preguntas: ¿es correcto?, ¿está justificado?, ¿quién responde? Cada pregunta apunta a las capas que la contestan; la tercera apunta a una persona.">
<style>.w8k{font-family:var(--mono);font-size:10px;letter-spacing:.05em;fill:var(--muted)} .w8t{font-family:var(--text);font-size:12px;fill:var(--ink)} .w8s{font-family:var(--text);font-size:11px;fill:var(--muted)} .w8f{fill:var(--surface);stroke:var(--rule);stroke-width:1} .w8a{fill:none;stroke:var(--muted);stroke-width:1.2} .w8q{font-family:var(--text);font-style:italic;font-size:12px;fill:var(--ink)} .w8p{fill:none;stroke:var(--c-fil);stroke-width:1.4} .w8g{stroke:var(--c-inv)}</style>
<text x="16" y="20" class="w8t">Carpeta del corpus entregado</text>
<rect x="16" y="32" width="300" height="24" rx="3" class="w8f"/><text x="24" y="48" class="w8k">README · pregunta, frontera, cómo ejecutar, licencia</text>
<rect x="16" y="60" width="300" height="24" rx="3" class="w8f"/><text x="24" y="76" class="w8k">protocolo-de-corpus.md</text>
<rect x="16" y="88" width="300" height="24" rx="3" class="w8f"/><text x="24" y="104" class="w8k">catalogo.csv · 14 campos, reglas de integridad</text>
<rect x="16" y="116" width="300" height="24" rx="3" class="w8f"/><text x="24" y="132" class="w8k">cuadernos/ · recoleccion, catalogo, limpieza, lectura</text>
<rect x="16" y="144" width="300" height="24" rx="3" class="w8f"/><text x="24" y="160" class="w8k">crudo/ · limpio/ · según derechos</text>
<rect x="16" y="172" width="300" height="24" rx="3" class="w8f"/><text x="24" y="188" class="w8k">registro-de-frontera.md · instruccion_v*.md</text>
<rect x="16" y="200" width="300" height="24" rx="3" class="w8f"/><text x="24" y="216" class="w8k">requirements.txt · versiones</text>
<rect x="16" y="228" width="300" height="24" rx="3" class="w8f"/><text x="24" y="244" class="w8k">informe-de-corpus.md · declaración de datos, lo abierto</text>
<text x="400" y="20" class="w8t">Otro investigador pregunta</text>
<text x="400" y="52" class="w8q">¿Es correcto?</text>
<path class="w8a" d="M396 48 L330 100"/><path class="w8a" d="M396 48 L330 212"/>
<text x="400" y="120" class="w8q">¿Está justificado?</text>
<path class="w8a" d="M396 116 L330 72"/><path class="w8a" d="M396 116 L330 128"/><path class="w8a" d="M396 116 L330 184"/><path class="w8a" d="M396 116 L330 240"/>
<text x="400" y="200" class="w8q">¿Quién responde?</text>
<path class="w8p" d="M396 196 L330 184"/>
<circle cx="560" cy="196" r="14" class="w8p"/><path class="w8p" d="M546 230 C 546 212 574 212 574 230"/>
<text x="560" y="256" text-anchor="middle" class="w8s">una persona,</text><text x="560" y="270" text-anchor="middle" class="w8s">no una celda</text>
<path class="w8p" d="M520 196 L544 196"/>
<text x="16" y="284" class="w8s">Las dos primeras preguntas se responden con archivos. La tercera, presentando.</text>
</svg>
<figcaption><b>Figura 8.</b> El corpus como aserción reconstruible. Lo que hay que ver es que cada pregunta de un par apunta a una capa de la documentación, y que la pregunta por quién responde no apunta a ninguna.</figcaption>
</figure>

6. La presentación es la forma práctica de la imputación, y por eso tiene un formato fijo de ocho minutos. El proyecto en una frase. La frontera del corpus: qué entra, qué queda afuera y por qué. Los números del catálogo: piezas por fuente, por periodo, por régimen. Una pérdida de la limpieza que podría importar. Una lectura computacional con las líneas que la respaldan. La decisión de la auditoría con su tasa y su razón. Y lo que queda abierto. Los pares hacen dos preguntas, y una de ellas es obligatoria: "¿Qué documento que quedó afuera cambiaría más su corpus si entrara?"

Un informe de corpus no es una nota de método, y la diferencia se ve en lo que cada uno permite hacer a un lector.

| Nota de método | Informe de corpus |
|---|---|
| Dice qué fuentes se consultaron | Dice qué entra, qué queda afuera y por qué, pieza por pieza |
| Describe el proceso en pasado | Entrega el cuaderno que lo ejecuta de nuevo |
| Menciona que se usó IA | Reporta la tasa de acuerdo, los desacuerdos y la decisión |
| Omite los límites o los deja para la discusión | Declara lo abierto como sección propia |
| *Se lee* | *Se ejecuta, se cuestiona y se corrige* |

7. Lo que sigue del curso es el uso del corpus. El catálogo y el cuaderno son el documento de entrada del curso 4 del programa, donde el corpus se codifica con el modelo como codificador auxiliar bajo el mismo procedimiento de auditoría, y del curso 5, donde se le aplican métodos computacionales que exigen un corpus con procedencia para que sus patrones puedan interpretarse. El corpus que se entrega hoy no es un resultado: es la condición para que los resultados de después puedan defenderse.

## IA y exigencia

El modelo puede redactar el borrador de la declaración de datos a partir del protocolo y del catálogo, y se le pide eso: una primera versión que el estudiante corrige frase por frase contra sus documentos, marcando lo que el modelo afirmó sin base. También puede revisar el `README` como si fuera un lector que intenta ejecutar el cuaderno, y señalar qué instrucción falta. Lo que debe poder defender sin la máquina es todo el informe, porque lo va a presentar, y en particular la sección de lo que queda abierto: ahí no hay nada que un modelo pueda saber por él.

## Lecturas

**Central**

- Bender, E. M. y Friedman, B. (2018). "Data Statements for Natural Language Processing: Toward Mitigating System Bias and Enabling Better Science". *Transactions of the Association for Computational Linguistics* 6, 587-604. https://aclanthology.org/Q18-1041/
- Zainea, C. I. (2026). *Agencia sin imputación. Hermenéutica, pragmática y la validación epistémica del discurso artificial*. Sección sobre la prótesis hermenéutica. https://izainea.github.io/escritos/agencia-sin-imputacion.pdf

**Complementaria**

- Gebru, T. et al. (2021). "Datasheets for Datasets". *Communications of the ACM* 64(12), 86-92. https://arxiv.org/abs/1803.09010
- Wilkinson, M. D. et al. (2016). "The FAIR Guiding Principles for scientific data management and stewardship". *Scientific Data* 3, 160018. https://doi.org/10.1038/sdata.2016.18
- Nguyen, D. et al. (2020). "How We Do Things With Words: Analyzing Text as Social and Cultural Data". *Frontiers in Artificial Intelligence* 3, 62. Sección sobre validación y reporte. https://doi.org/10.3389/frai.2020.00062
- Zainea, C. I. (2026). "La prótesis hermenéutica". https://izainea.github.io/blog/protesis-hermeneutica/
- Python Packaging Authority. *pip freeze*. https://pip.pypa.io/en/stable/cli/pip_freeze/

## Guía de lectura

- Bender y Friedman escriben para quienes entrenan sistemas, y su preocupación es el sesgo que un conjunto de textos transmite a un modelo. La misma ficha, leída por un historiador, describe la posición desde la que se tomó el corpus. *¿Qué respuesta de su declaración de datos cambiaría más la lectura que otro haría de sus resultados?*
- La sección sobre la prótesis hermenéutica dice que con andamiaje cada salida incluye su procedencia, sus límites declarados y las condiciones bajo las cuales debería rechazarse. Léala como una descripción de su carpeta. *¿Dónde están, en su entrega, las condiciones bajo las cuales su corpus debería rechazarse?*
- Nguyen y sus coautores cierran con recomendaciones para reportar análisis de texto. Compárelas con la plantilla del informe. *¿Qué recomendación de ellos no está en su informe, y por qué?*

## Taller: presentaciones y cierre

Formato de presentación, ocho minutos y dos preguntas de pares:

1. El proyecto en una frase.
2. La frontera del corpus: qué entra, qué queda afuera, por qué.
3. Los números del catálogo.
4. Una pérdida de la limpieza que podría importar.
5. Una lectura computacional con sus líneas.
6. La decisión de la auditoría, con tasa y razón.
7. Lo que queda abierto.

Pregunta obligatoria de los pares: ¿qué documento que quedó afuera cambiaría más su corpus si entrara?

## Guion de la sesión

| Momento | Docente | Estudiante | Material |
|---|---|---|---|
| 0 a 10 min | Recapitula el curso en una página: decisión, programa, catálogo, pérdida, instrumento, auditoría, aserción | Anota qué semana le cambió más el corpus | |
| 10 a 25 min | Expone los tres sentidos de validación aplicados al corpus y la figura 8 | Marca en su carpeta qué archivo responde cada pregunta | Figura 8 |
| 25 a 60 min | Modera cuatro presentaciones | Presenta o pregunta | Informes |
| 60 a 70 min | Pausa | | |
| 70 a 110 min | Modera cuatro presentaciones más | Presenta o pregunta | Informes |
| 110 a 120 min | Cierra: qué reciben los cursos 4 y 5 de lo que se entregó hoy | Anota una tarea pendiente de su corpus | |

Notas para el docente. Lo que suele fallar: el estudiante presenta resultados de lectura en lugar del corpus, y hay que devolverlo a la frontera y a los números. El segundo fallo es saltarse la sección de lo abierto por pudor; la pregunta obligatoria de los pares la fuerza. El tercero es el tiempo: con más de doce estudiantes hacen falta dos sesiones o presentaciones en paralelo con el docente rotando.

## Entrega final

Informe de corpus, con la plantilla de la sección correspondiente de `plantillas/protocolo-de-corpus.md` y la declaración de datos, acompañado de la carpeta completa del corpus: protocolo, catálogo, cuadernos, `crudo` y `limpio` según derechos, registro de frontera, `requirements.txt`. Se entrega con la bitácora completa. Rúbrica en `evaluacion.md`.

## Después del curso

La ruta Texto del programa continúa con el curso 4, codificación asistida, y la ruta Computacional con el curso 5, métodos computacionales para el sentido. Los dos reciben el catálogo maestro y el cuaderno como documento de entrada. El curso 6 vuelve sobre la validación de lo que se diga a partir de este corpus, y el curso 7 sobre los derechos y la exterioridad que aquí solo se registraron.
