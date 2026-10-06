# Syllabus

## Datos generales

| | |
|---|---|
| Nombre | Del archivo al corpus visual descrito |
| Programa | Tunjos para la IA, tercero de los siete cursos del programa. Capa Oficio |
| Duración | Ocho sesiones semanales de dos horas y trabajo autónomo guiado, unas 96 horas en total. Se adapta al formato de microcredencial o de curso de educación continua de cada institución |
| Modalidad | Híbrida: una sesión presencial de dos horas por semana, con participación remota sincrónica, y trabajo asincrónico guiado. La modalidad virtual es alternativa |
| Docente | Carlos Isaac Zainea Maya |
| Prerrequisitos | Ninguno. Se recomienda haber tomado [*Validación del razonamiento con IA en ciencias sociales*](../../curso-1-tres-inferencias/README.md), el curso de fundamentos del programa, donde se distinguen deducción, inducción y abducción por su régimen de validez y se concluye que un modelo configura sin poder validar ni responder por lo configurado; este curso usa esa distinción, pero la explica cuando la necesita. No requiere programación: las prácticas se pueden hacer con hojas de cálculo y con la interfaz web de un modelo; el cuaderno de apoyo en Python es opcional |
| Público | Egresados y estudiantes de posgrado en historia, estudios visuales, comunicación, antropología, sociología y artes; personal de museos, archivos y medios que trabaja con colecciones de imágenes |

## Problema que atiende

Quien investiga con imágenes casi nunca las recibe ordenadas. Las encuentra dispersas en catálogos de museo, en prensa digitalizada, en redes sociales, en carpetas heredadas de otro proyecto. Cada una llega con un fragmento de contexto distinto, o sin ninguno. Para que ese conjunto sea un corpus hay que hacer tres cosas que los cursos de método visual mencionan y rara vez enseñan a hacer: catalogar con procedencia, describir con una gramática compartida y decidir qué se puede mostrar. Los modelos multimodales añaden una cuarta: hoy es posible pedir una descripción de cada imagen a un modelo y obtenerla en segundos. El investigador que lo hace recibe textos fluidos, detallados y con la forma de una observación experta, que a veces describen lo que no hay y con frecuencia callan lo que un lector local vería primero. Este curso enseña a construir el corpus, a describirlo con la máquina y a auditar lo descrito con una gramática que permite decir, afirmación por afirmación, de dónde salió.

## Competencias

Al terminar el curso el estudiante puede:

1. **Construir un catálogo visual con procedencia**: recolectar imágenes de manera reproducible y respetuosa de las fuentes, deduplicarlas por hash perceptual, registrarlas en un esquema con identificador, periodo, fuente, derechos y escena, y validar su integridad.
2. **Describir imágenes con una gramática explícita**: aplicar las capas de Banks (narrativa interna, narrativa externa, materialidad) y los tres modos del signo de Peirce (ícono, índice, símbolo), con apoyo de la distinción denotación y connotación de Barthes.
3. **Delegar y auditar la descripción**: diseñar prompts por capas para un modelo multimodal, obtener descripciones densas a escala, y auditar una muestra clasificando cada afirmación del modelo en lo que está en la imagen, lo que no está y lo que requiere contexto local.
4. **Exhibir sin dañar y documentar la frontera**: decidir, imagen por imagen, bajo qué derechos y con qué resolución, recorte, anonimización o sustitución por descripción se muestra, y registrar qué describió la máquina y qué decidió el investigador.

## Resultados de aprendizaje y evidencias

| Competencia | Evidencia verificable | Semana |
|---|---|---|
| 1 | Catálogo visual con procedencia, deduplicado y validado | 3 |
| 2 y 3 | Descripciones por capas de todo el corpus y auditoría manual de una muestra | 6 |
| 2 y 4 | Ficha semiótica de imágenes representativas, registro de frontera visual y protocolo de exhibición | 8 |
| 1 a 4 | Presentación del corpus documentado ante pares | 8 |

## Programa por semanas

| Semana | Tema | Lectura central | Actividad |
|---|---|---|---|
| [1](semana-01.md) | La imagen como documento. Escenas (museo, prensa, plataforma), dispositivo (curaduría, editorial, algoritmo), materialidad. Ética de la imagen sensible y derechos | Banks (2010), caps. 1 y 2. Rose (2016), cap. 2 | Bitácora inicial: tres imágenes del proyecto leídas por escena y dispositivo |
| [2](semana-02.md) | Recolección y catálogo. Descarga reproducible, deduplicación por hash perceptual, esquema de catálogo, validación de integridad | Arnold y Tilton (2019). Guía de la práctica 1 | Práctica 1: primer catálogo de 20 imágenes, con duplicados detectados |
| [3](semana-03.md) | Semiótica para describir. Peirce: ícono, índice, símbolo. Barthes: denotación y connotación. Kress y van Leeuwen: gramática del diseño visual | Peirce (1894). Barthes (1964). Kress y van Leeuwen (2006), cap. 1 | Entrega: catálogo visual con procedencia |
| [4](semana-04.md) | Descripción densa con modelos multimodales. Prompts por capas, costos, límites | Smits y Wevers (2022). Guía de la práctica 2 | Práctica 2: descripciones por capas de 20 imágenes con dos prompts |
| [5](semana-05.md) | Auditoría de la descripción. Muestra de validación, sesgo cultural, lo intangible, qué no ve el modelo | Pouget et al. (2024). Schneider et al. (2025) | Auditoría de una muestra de 15 descripciones con la tabla de tres columnas |
| [6](semana-06.md) | De la descripción al código. Preclasificación asistida y primeras categorías | Rincón (2009). Banks (2010), cap. 4 | Entrega: descripciones por capas con auditoría de la muestra |
| [7](semana-07.md) | Exhibir sin dañar. Descripción densa en lugar de la imagen, resolución, anonimización, uso legítimo. Registro de frontera visual | Didi-Huberman (2004), parte I. Mitchell (2009), cap. 1 | Protocolo de exhibición y registro de frontera visual del corpus |
| [8](semana-08.md) | El corpus visual documentado. Presentación | Arnold y Tilton (2019), relectura. Zainea (2026) | Entrega final: ficha semiótica, registro de frontera y presentación |

## Metodología

El curso se enseña con el método que enseña. Cada semana tiene tres momentos.

- **Lectura guiada** (asincrónica, 4 a 5 horas). Un texto central con guía de lectura y una lectura complementaria opcional.
- **Sesión sincrónica** (2 horas). La primera hora discute la lectura a partir del caso demostrativo, un corpus de unas 1.800 imágenes de cultura visual colombiana construido por el docente. La segunda es taller sobre el corpus propio del estudiante.
- **Bitácora** (asincrónica, 3 a 4 horas). El estudiante registra el trabajo de la semana sobre su corpus, lo que describió el modelo cuando lo hubo, lo que decidió él y con qué criterio. Las bitácoras alimentan los tres productos.

Las prácticas con modelos multimodales usan modelos de acceso gratuito en su versión web. El cuaderno de apoyo en Python permite hacer lo mismo por programa, con la clave de acceso en un archivo `.env` y nunca en el código; es opcional.

## Evaluación

| Producto | Peso | Criterio principal |
|---|---|---|
| Ficha semiótica y registro de frontera visual, con protocolo de exhibición y presentación | 40 % | Cada afirmación sobre una imagen tiene origen declarado (cartela, modelo o investigador) y la decisión de exhibición está argumentada |
| Descripciones por capas con auditoría de una muestra | 25 % | La auditoría distingue con precisión lo que está, lo que no está y lo que requiere contexto local, y resume el sesgo del modelo |
| Catálogo visual con procedencia | 20 % | Cada fila tiene fuente, página fuente y derechos; los duplicados se detectaron y se explicó por qué lo son |
| Bitácora semanal | 15 % | Continuidad y honestidad en el registro, incluidas las imágenes que no se supo describir |

La rúbrica detallada está en [evaluacion.md](evaluacion.md).

## Articulación

Este curso pertenece a dos rutas del programa Tunjos para la IA. En la ruta Imagen lo precede [*Validación del razonamiento con IA en ciencias sociales*](../../curso-1-tres-inferencias/README.md), que distingue deducción, inducción y abducción por su régimen de validez y concluye que la máquina configura sin poder validar, y lo siguen [*Codificación cualitativa con IA en ciencias sociales*](../../curso-4-codificacion-asistida/README.md), donde un modelo propone códigos y categorías sobre material cualitativo y el investigador responde por el libro de códigos, y [*Validar y defender investigación social asistida por IA*](../../curso-6-validacion-interpretacion/README.md), donde lo ya configurado se valida en tres sentidos y se escribe como hallazgo propio. En la ruta Computacional lo precede [*Corpus de textos con procedencia en ciencias sociales*](../../curso-2-corpus-textual/README.md), que construye con Python un corpus de documentos con procedencia, y lo sigue [*Patrones estables en datos de las ciencias sociales*](../../curso-5-metodos-computacionales/README.md), donde embeddings, agrupamiento y redes se tratan como instrumentos inductivos que no eligen entre hipótesis. A *Codificación cualitativa con IA en ciencias sociales* este curso entrega un corpus descrito y auditado sobre el que la codificación puede empezar; a *Patrones estables en datos de las ciencias sociales*, un catálogo tabular con descripciones listas para representar y agrupar. Ninguno de esos cursos es prerrequisito de este. Se articula con cursos de metodologías visuales, historia del arte, estudios de medios, archivística y museología de programas de posgrado en ciencias sociales y humanidades, a los que aporta lo que no suelen cubrir: la construcción técnica del corpus y la auditoría de descripciones producidas por modelos.

## Política de uso de modelos multimodales

Se usan desde la semana 4, de forma declarada. Cada entrega incluye qué modelo se usó, con qué prompt, sobre qué imágenes y qué parte del resultado es decisión del estudiante. Un uso no declarado se trata como infortunio de autoridad: el estudiante presenta como observación propia algo por lo que no puede responder. Se devuelve para que escriba el registro de frontera que faltaba. El material sensible del corpus propio no se envía a un modelo sin haber pasado por el protocolo de exhibición de la semana 7; hasta entonces, las prácticas usan imágenes públicas o una muestra sin personas identificables.
