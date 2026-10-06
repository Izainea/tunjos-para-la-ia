# Syllabus

## Datos generales

| | |
|---|---|
| Nombre | Del documento al corpus textual trazable |
| Programa | Tunjos para la IA, segundo de los siete cursos del programa. Capa de Oficio |
| Duración | Ocho sesiones semanales de dos horas y trabajo autónomo guiado, unas 96 horas en total. Se adapta al formato de microcredencial o de curso de educación continua de cada institución |
| Modalidad | Híbrida: una sesión presencial de dos horas por semana, con participación remota sincrónica, y trabajo asincrónico guiado. La modalidad virtual es alternativa |
| Docente | Carlos Isaac Zainea Maya |
| Prerrequisitos | Ninguno. No requiere programación previa: el curso enseña Python desde cero. Se recomienda haber cursado [*Validación del razonamiento con IA en ciencias sociales*](../../curso-1-tres-inferencias/README.md), el curso de fundamentos del programa, donde se distinguen deducción, inducción y abducción por su régimen de validez y se concluye que la máquina configura sin poder validar ni responder por lo configurado; no es obligatorio, porque lo que este curso toma de allí se explica donde se usa |
| Público | Egresados y estudiantes de posgrado en ciencias sociales y humanidades, profesionales que investigan o producen informes a partir de documentos, prensa, archivos o textos en línea |
| Equipo | Un computador con Python 3.11 o superior y un cuaderno (JupyterLab o un servicio gratuito de cuadernos en la nube). Todo el software del curso es libre |

## Problema que atiende

Buena parte de la investigación en humanidades y ciencias sociales empieza con una carpeta de archivos: notas de prensa descargadas, documentos escaneados, entrevistas transcritas, publicaciones copiadas de un sitio. La carpeta crece, se mezcla con versiones, pierde el rastro de dónde salió cada cosa, y cuando llega el momento de analizarla nadie puede decir con certeza qué hay dentro, por qué está, ni si se podría volver a reunir. Los modelos de lenguaje agravan el problema: ofrecen resumir, etiquetar y filtrar miles de documentos en minutos, y es tentador dejarles también la decisión de qué entra. El resultado es un corpus que nadie delimitó y del que nadie puede responder. Este curso enseña a hacer lo contrario: a tomar la decisión de qué es el corpus, a escribirla en forma de programa para que sea repetible, a documentar cada pieza con su procedencia y sus derechos, y a usar la primera lectura computacional y la lectura asistida por modelos como instrumentos que sugieren, bajo auditoría del investigador.

## Competencias

Al terminar el curso el estudiante puede:

1. **Delimitar y justificar** un corpus textual con criterios explícitos de inclusión y exclusión, evaluando cada fuente por autenticidad, credibilidad, representatividad e interpretabilidad, y con atención a derechos de autor, datos personales y acceso a la información.
2. **Recolectar de forma legal y reproducible** documentos de fuentes abiertas, hemerotecas digitales, portales de datos y sitios web, con un cuaderno de Python que otro puede ejecutar y que registra fecha, origen y huella de cada descarga.
3. **Construir y validar** un catálogo maestro de metadatos con procedencia, deduplicación por hash y verificación de integridad, y limpiar y normalizar los textos documentando lo que la limpieza pierde.
4. **Leer computacionalmente** el corpus con frecuencias, concordancias, colocaciones y dominios léxicos, usar un modelo de lenguaje para una lectura asistida auditada sobre una muestra, y documentar el corpus como una aserción por la que responde.

## Resultados de aprendizaje y evidencias

| Competencia | Evidencia verificable | Semana |
|---|---|---|
| 1 | Protocolo de corpus del proyecto propio | 3 |
| 2 y 3 | Catálogo maestro con procedencia y cuaderno reproducible que lo genera | 6 |
| 4 | Informe de corpus con primera lectura computacional, auditoría de la lectura asistida y registro de frontera | 8 |
| 1 a 4 | Bitácora semanal del cuaderno y de las decisiones | 1 a 8 |

## Programa por semanas

| Semana | Tema | Lectura central | Actividad |
|---|---|---|---|
| [1](semana-01.md) | Qué es un corpus y qué lo hace válido. Delimitación, muestreo teórico, los cuatro criterios de Valles, derechos y ética | Valles (1997), cap. 4. Nguyen et al. (2020) | Primera delimitación del corpus propio y cadena de procedencia de un documento |
| [2](semana-02.md) | Python mínimo para humanidades. El cuaderno, el texto, las listas, los archivos, el registro de procedencia | Tutorial oficial de Python, caps. 3 y 7. Rockwell y Sinclair (2016), cap. 1 | Primer cuaderno: leer diez archivos y escribir su registro |
| [3](semana-03.md) | Recolección legal y reproducible. Fuentes abiertas, hemerotecas, portales de datos, interfaces de programación, descarga responsable | Ley 1712 de 2014 y Ley 1581 de 2012. RFC 9309 | Entrega: protocolo de corpus |
| [4](semana-04.md) | El catálogo maestro. Esquema de metadatos, deduplicación por hash, validación de integridad | Gibbs (2012), cap. 3. Wilkinson et al. (2016) | Catálogo preliminar validado con la mini app |
| [5](semana-05.md) | Limpieza y normalización. Codificación, OCR y su error, segmentación, lo que se pierde al limpiar | Rawson y Muñoz (2019). Cordell (2017) | Bitácora de limpieza: antes, después y lo perdido |
| [6](semana-06.md) | Primera lectura computacional. Frecuencias, concordancias, colocaciones, dominios léxicos | Sinclair (1991), caps. 1 y 8. Moretti (2015), cap. 1 | Entrega: catálogo maestro y cuaderno reproducible |
| [7](semana-07.md) | Lectura asistida. El modelo resume y etiqueta, el investigador audita sobre una muestra. Registro de frontera aplicado al corpus | Grimmer y Stewart (2013). Ziems et al. (2024) | Práctica guiada: auditoría de etiquetas sobre una muestra |
| [8](semana-08.md) | El corpus como aserción. Documentar el corpus para que otro lo reconstruya. Presentación | Bender y Friedman (2018). Zainea (2026) | Entrega final del informe de corpus y presentación ante pares |

## Metodología

El curso se enseña con el método que enseña. Cada semana tiene tres momentos.

- **Lectura y ejercicio guiado** (asincrónico, 4 a 5 horas). Un texto central con guía de lectura, y un bloque de Python del cuaderno de apoyo que el estudiante ejecuta y adapta a su material.
- **Sesión sincrónica** (2 horas). La primera hora discute la lectura sobre el caso demostrativo, un corpus de documentos públicos colombianos de acceso abierto. La segunda es taller: el estudiante aplica lo visto a su propio corpus, con el docente y los pares al lado.
- **Bitácora** (asincrónica, 3 a 4 horas). El estudiante registra en su cuaderno el ejercicio de la semana, las decisiones que tomó sobre su corpus, lo que propuso el modelo cuando lo hubo, y con qué criterio decidió. El cuaderno es la bitácora: no hay dos documentos.

Python se enseña a medida que hace falta, con explicación antes del código. Todo el software es libre. Las prácticas con modelos de lenguaje usan modelos de acceso gratuito.

## Evaluación

| Producto | Peso | Criterio principal |
|---|---|---|
| Informe de corpus | 40 % | Otro investigador podría reconstruir el corpus y repetir la lectura con lo que el informe dice; la auditoría de la lectura asistida distingue lo que propuso el modelo de lo que responde el estudiante |
| Catálogo maestro y cuaderno reproducible | 25 % | Cada pieza tiene procedencia, derechos y criterio; el cuaderno corre de principio a fin y produce el catálogo |
| Protocolo de corpus | 20 % | La delimitación está argumentada con los cuatro criterios y las exclusiones están escritas |
| Bitácora semanal | 15 % | Continuidad y honestidad del registro, incluidas las decisiones que se revirtieron |

La rúbrica detallada está en [evaluacion.md](evaluacion.md).

## Articulación

Este curso abre la capa de Oficio del programa y pertenece a las rutas Texto, Computacional y Programa completo. Su producto, el catálogo maestro con el cuaderno que lo genera, es el documento de entrada de [*Codificación cualitativa con IA en ciencias sociales*](../../curso-4-codificacion-asistida/README.md), donde el corpus se codifica con el modelo como codificador auxiliar y el libro de códigos resultante se trata como aserción del investigador y no como output, y de [*Patrones estables en datos de las ciencias sociales*](../../curso-5-metodos-computacionales/README.md), donde se le aplican embeddings, agrupamientos y redes de coocurrencia, instrumentos cuyos patrones solo pueden interpretarse si el corpus tiene procedencia. Se articula con cursos de metodología cualitativa, análisis de contenido, archivística y humanidades digitales de posgrados en ciencias sociales y humanidades, a los que aporta lo que ellos no suelen cubrir: la construcción programada y documentada del corpus antes del análisis.

## Política de uso de modelos de lenguaje

Se usan de forma declarada: para explicar errores de Python, para proponer esquemas de metadatos, y en la semana 7 para resumir y etiquetar documentos bajo auditoría. Cada entrega incluye qué modelo se usó, para qué, y qué parte del resultado es decisión del estudiante. Lo que no se admite es que el modelo decida qué entra al corpus ni que su etiqueta se presente como lectura del investigador sin auditoría. Un uso no declarado se trata como infortunio de autoridad: el estudiante presenta como propio algo por lo que no puede responder, y la entrega se devuelve para escribir el registro que faltaba.
