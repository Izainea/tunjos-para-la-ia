# Guía de autoría de un curso del programa

Esta guía fija la estructura, la voz y las restricciones de cada curso. Un curso escrito con esta guía se publica sin retoques en la página del programa y alimenta automáticamente las dos propuestas en formato de convocatoria. Las reglas de estilo provienen de las instrucciones que el docente mantiene en sus proyectos y de sus textos publicados; no son negociables.

## 1. El programa en tres frases

*Tunjos para la IA* es un programa de siete microcredenciales sobre razonamiento, validación e inteligencia artificial en ciencias sociales y humanidades. Su tesis: quien investiga con modelos de lenguaje necesita saber qué inferencia hace la máquina y cuál hace él, construir un flujo técnico con rastro auditable, y validar y responder por el resultado ante una comunidad. Su principio de diseño: cada curso se enseña con el método que enseña; el estudiante configura con la máquina, valida, registra la frontera entre ambos y entrega el registro.

Marco de fondo (tesis doctoral del docente, *Agencia sin imputación*): el modelo configura (Mímesis II de Ricœur) sin poder refigurar ni imputarse lo configurado; su error típico es un infortunio de autoridad epistémica (Austin), no una alucinación; hay tres sentidos de validación (corrección del resultado, justificación del proceso, imputación); la deducción vale por su forma, la inducción por sus tasas, la abducción porque alguien se compromete a probarla (Peirce); la prótesis hermenéutica es la arquitectura en que la máquina configura, el investigador valida y la frontera es auditable.

Horizonte que anima todo el programa sin decirse de forma explícita en cada página: privilegiar la pregunta epistemológica (cómo se valida) sobre la ontológica (qué es la máquina); distinguir configurar sentido de validarlo; pensar el error como infortunio pragmático y no como defecto de un sujeto; separar rendimiento de validez; preguntar qué significa usar un lenguaje sin participar en la forma de vida que lo sostiene; preguntar por el andamiaje procesal que hace gobernable una práctica; atender la dimensión política y situada del saber. Nunca afirmar que "la IA no puede abducir" ni ninguna tesis ontológica sobre lo que la máquina no puede hacer.

Los siete cursos:

| Nº | Curso | Capa |
|---|---|---|
| 1 | Las tres inferencias en el razonamiento humano y el artificial | Fundamentos |
| 2 | Del documento al corpus textual trazable | Oficio |
| 3 | Del archivo al corpus visual descrito | Oficio |
| 4 | Codificación asistida por una máquina que configura | Oficio |
| 5 | Métodos computacionales para el sentido | Juicio |
| 6 | Validación e interpretación como refiguración del investigador | Juicio |
| 7 | Ética, exterioridad y gobernanza | Juicio |

Rutas: Fundamentos (1, 6); Texto (1, 2, 4, 6); Imagen (1, 3, 4, 6); Computacional (2, 3, 5); Programa completo (1 a 7 más proyecto integrador).

## 2. Formato común de cada curso

- 2 créditos, 8 semanas, 96 horas del estudiante (16 sincrónicas en 8 sesiones de 2 horas, 80 autónomas).
- Modalidad híbrida: sesiones presenciales con participación remota sincrónica y trabajo asincrónico guiado. La modalidad virtual es solo alternativa. Decirlo así en todas partes.
- Sin prerrequisitos de programación salvo que el curso lo diga. Público: egresados y posgrado en ciencias sociales y humanidades, profesionales que investigan o producen informes con modelos.
- Tres productos acumulativos sobre el proyecto propio del estudiante y una bitácora semanal. Evaluación por rúbricas de cuatro niveles (Insuficiente, Básico, Logrado, Sobresaliente). Pesos típicos 40/25/20/15. Se aprueba con Logrado en los dos productos principales y 3,5 sobre 5,0.
- Política de uso de modelos: obligatorio y declarado; el uso no declarado es un infortunio de autoridad y se devuelve para escribir el registro que faltaba. El curso promueve la IA y exige comprender y defender todo el trabajo.

## 3. Estructura de carpetas (obligatoria)

```
cursos/curso-N-slug/
  README.md                  pregunta del curso, respuesta que construye, tabla de carpetas, productos
  programa/
    syllabus.md              datos generales, problema, competencias (4), evidencias, tabla de 8 semanas con enlaces, metodología, evaluación, articulación, política de IA
    semana-01.md … semana-08.md
    evaluacion.md            rúbricas de cada producto y de la bitácora, política de integridad, certificación
    bibliografia.md          por semana, centrales marcadas con ●, enlaces de acceso abierto cuando existan
  plantillas/                una plantilla .md por producto (tablas listas para llenar)
  practicas/                 guías paso a paso de las prácticas, y un cuaderno de apoyo en Python cuando aplique
  apps/                      mini apps HTML autocontenidas (ver §5)
  propuestas/                contenido.py con el texto para los formatos de convocatoria (ver §6). Esta carpeta NO se publica.
```

Tomar como modelo `cursos/curso-1-tres-inferencias/`. Leerlo entero antes de escribir.

## 4. Cada semana (semana-NN.md)

Secciones en este orden, con estos títulos:

1. `# Semana N. Título` (título sobrio, sin gancho)
2. `## Pregunta de la semana` (una pregunta)
3. `## Por qué esta semana` (primer párrafo con `<p class="lede">`; sitúa la semana en el arco del curso)
4. `## Contenido de la sesión` (entre cinco y siete párrafos numerados en prosa corrida, cada uno abre con la afirmación; nada de rótulos en negrita seguidos de dos puntos)
5. Al menos una figura y, en las semanas que lo pidan, una mini app embebida, en el punto donde ayude a ver el mecanismo
6. `## IA y exigencia` (un párrafo: qué se le pide a la máquina esta semana y qué debe poder defender el estudiante sin ella)
7. `## Lecturas` con `**Central**` y `**Complementaria**`, referencias completas con enlace cuando exista
8. `## Guía de lectura` (tres o cuatro entradas; cada una es una reflexión breve seguida de la pregunta en cursiva, como en los seminarios del docente)
9. `## Taller de la segunda hora` (instrucciones ejecutables; si hay tabla, ponerla)
10. `## Guion de la sesión` (tabla minuto a minuto: momento, qué hace el docente, qué hace el estudiante, material; y "Notas para el docente" con dos o tres advertencias de lo que suele fallar)
11. `## Bitácora` o `## Entrega` según corresponda
12. `## Para la próxima semana`

Extensión: 120 a 180 líneas de markdown por semana. Cada semana debe poder leerse sola, sin el resto del curso, y por eso repite en una frase lo que necesita de semanas anteriores.

## 5. Didáctica: mini apps, diagramas, grafos

Cada curso tiene al menos tres mini apps y al menos cuatro figuras repartidas en las semanas. Son parte del contenido, no adorno: cada una hace visible un mecanismo que el texto solo describe. El estándar es el de las reseñas gráficas que el docente construye para sus seminarios: instrumentos distintos según lo que el texto pide (grafo conceptual, matriz de predicados, línea de tiempo, simulación), con interacción mínima y lectura clara.

Mini apps. Archivos HTML autocontenidos en `apps/`, un archivo por app, copiados de `herramientas/app-base.html` (conserva los tokens de color, las fuentes y el script de tema). Sin dependencias externas salvo d3 o cytoscape desde cdnjs.cloudflare.com cuando un grafo lo justifique. Sin llamadas a ningún modelo ni a ninguna API: todo corre en el navegador con datos incluidos en el archivo. Deben funcionar en claro y en oscuro y a 360 px de ancho. Tipos esperados: un clasificador donde el estudiante marca y recibe retroalimentación razonada; un simulador que muestra cómo cambia un resultado al mover un parámetro; un grafo interactivo con panel que explique el nodo seleccionado; una línea de tiempo navegable; un verificador que deja ver por qué un paso válido y uno inválido llevan a la misma respuesta; una matriz de contraste clicable. Se embeben en la semana con:

```html
<iframe class="app" src="apps/nombre.html" title="Qué hace" loading="lazy"></iframe>
```

Figuras. SVG inline dentro de `<figure class="wide">…<figcaption><b>Figura N.</b> …</figcaption></figure>`, con `viewBox`, `role="img"` y `aria-label`, y colores solo con variables: `var(--ink)`, `var(--muted)`, `var(--rule)`, `var(--surface)`, `var(--accent)`, `var(--c-fil)`, `var(--c-inv)`, `var(--c-app)`. Fuente `var(--mono)` para etiquetas y `var(--text)` para texto. Modelo de estilo: los SVG de las entradas de blog en `izainea.github.io/src/content/blog/*.mdx`.

Verificación obligatoria antes de entregar: sintaxis de cada app con `esprima` desde Python (`pip install esprima`; extraer el bloque `<script>` y llamar `esprima.parseScript`), y captura de cada app con Edge sin interfaz: `"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --headless=new --screenshot=<png> --window-size=1000,800 "file:///<ruta codificada con %20 y %C3%AD>"`. Mirar la captura. Si algo no se ve, no está hecho.

## 6. Propuestas en formato de convocatoria (propuestas/contenido.py)

Copiar `cursos/curso-1-tres-inferencias/propuestas/contenido.py` y rellenar todas las variables con el mismo nombre y tipo. Reglas:

- Modalidad híbrida en todos los campos de modalidad; en el formato que pide justificar la presencialidad, justificarla (talleres sobre material propio, presentaciones ante pares, trabajo en grupos).
- `PROFESOR` y `hv_resumen` se construyen a partir de `docente.md` (raíz del repositorio) con la fila de experiencia directa del curso.
- Los nombres de universidades destinatarias solo pueden aparecer dentro de `propuestas/`. En todo lo demás está prohibido nombrar la universidad a la que se enviaría la propuesta o la palabra "convocatoria".
- Para el formato de 10 sesiones de 3 horas (30 horas), redistribuir las 8 semanas en 10 sesiones: una por semana, más la semana central y el taller práctico desdoblados.

## 7. Voz y estilo: el del docente

Los materiales se escriben en el estilo del docente. Modelos obligatorios, leer antes de escribir:

- `izainea.github.io/src/content/blog/agencia-sin-imputacion.mdx`
- `izainea.github.io/src/content/blog/alucinacion-o-infortunio.mdx`
- `izainea.github.io/src/content/blog/protesis-hermeneutica.mdx`
- `Doctorado Filosofía/Coloquio/scripts/contenido_proyecto.md` (anteproyecto doctoral)

Rasgos que deben reproducirse:

- El párrafo abre con la afirmación y después la sostiene. No se anuncia lo que se va a decir: se dice. "La crítica ontológica es irrefutable, y este trabajo la acepta en su totalidad. Lo que discute es la inferencia que suele derivarse de ella."
- Cada tesis lleva su autor y su obra, en línea: "Leída con la triple mímesis de *Tiempo y narración* (Ricœur, 1995)…". Se distingue siempre entre exposición de un autor y tesis propia del curso.
- Glosas al margen para lo que precisa sin interrumpir: definiciones, ejemplos, datos biográficos, alcances. Se escriben como `<aside class="glosa"><span class="mark">a</span> texto</aside>` justo después del párrafo que las llama, y el párrafo lleva `<sup class="mark">a</sup>` en el punto exacto. Dos a cuatro por semana.
- Tablas de contraste de dos columnas cuando hay dos marcos enfrentados (pregunta ontológica frente a pregunta epistemológica; marco mentalista frente a marco pragmático). La última fila, en cursiva, resume la consecuencia.
- Figuras que muestran el mecanismo: un silogismo que falla, una frontera marcada, un arco que se trunca. Pie con `<b>Figura N.</b>` y una frase que diga qué hay que ver.
- Ejemplos concretos y físicos para ideas abstractas: el telescopio que no comprende las estrellas, el bastón del ciego en Merleau-Ponty, el pavo de Russell, la escena del crimen.
- Registro reflexivo de artículo de humanidades. Nunca tono de vendedor, nunca exclamaciones, nunca elogios al lector.
- Títulos sobrios y planos. Prohibidos los títulos con dos puntos de gancho ("Título: subtítulo llamativo"), las preguntas y las metáforas como gancho. Un título puede llevar dos puntos solo si la segunda parte precisa el alcance ("La deducción y la historia de la validación formal").
- Prosa corrida. No abrir ítems con un rótulo en negrita seguido de explicación. Las listas, cuando hagan falta, de siete elementos como máximo.
- Palabras prohibidas: fundamental, crucial, esencial, clave como adjetivo, robusto como relleno, poderoso, fascinante.
- Sin rayas ni guiones largos en la prosa. Sin paréntesis explicativos largos. Frases cortas; cada frase aporta algo distinto, y si se puede quitar sin perder información, se quita.
- Cifras con punto de miles y coma decimal (1.800 imágenes; 78,3 %).
- Cuando una afirmación viene de una verificación, decir sobre qué base se verificó y con qué resultado. Cuando algo no se verificó, decirlo. Lo que queda abierto se declara abierto.
- Explicación antes del código, nunca al revés.
- Referencias verificables: autor, año, título, revista o editorial, y enlace de acceso abierto si existe (arXiv, Gutenberg, Universidad de Navarra para Peirce, ACL Anthology, DOI). No inventar referencias: si no se está seguro de una, no incluirla. Formato APA 7.
- Español de Colombia. Segunda persona formal ("usted") en instrucciones al estudiante, tercera persona en descripciones.
- Lo que el curso enseña se aplica al proyecto propio del estudiante; nunca a casos ficticios cuando puede ser real. No mencionar herramientas de pago como requisito.

## 8. Cada curso es autocontenido

Un lector puede tomar un solo curso. Por eso está prohibido referirse a otro curso por su número o por su posición ("el curso 1", "el curso anterior", "los cursos siguientes", "la semana 7 del curso 1"). Toda referencia a otro curso lleva tres cosas: el nombre del curso en cursiva, un enlace a su README o a la semana concreta (`[*Corpus textual*](../../curso-2-corpus-textual/README.md)` desde `programa/`; `../curso-2-corpus-textual/README.md` desde el README del curso), y una o dos frases que digan de qué se habló allí y qué se concluyó, de modo que quien no lo tomó entienda igual. Si un párrafo da por supuesto algo que solo se explicó en otro curso, se añade aquí la explicación mínima. El verificador señala como error cualquier "curso N" suelto fuera de un enlace con nombre.
