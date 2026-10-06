# Syllabus

## Datos generales

| | |
|---|---|
| Nombre | Las tres inferencias: razonamiento humano y razonamiento artificial |
| Programa | Tunjos para la IA, curso 1 de 7 |
| Duración | Ocho sesiones semanales de dos horas y trabajo autónomo guiado, unas 96 horas en total. Se adapta al formato de microcredencial o de curso de educación continua de cada institución |
| Modalidad | Híbrida: una sesión presencial de dos horas por semana, con participación remota sincrónica, y trabajo asincrónico guiado. La modalidad virtual es alternativa |
| Docente | Carlos Isaac Zainea Maya |
| Prerrequisitos | Ninguno. No requiere programación ni formación filosófica previa |
| Público | Egresados y estudiantes de posgrado en ciencias sociales y humanidades, profesionales que investigan o producen informes con apoyo de modelos de lenguaje |

## Problema que atiende

Los modelos de lenguaje ya participan en la producción de conocimiento: sintetizan literatura, proponen categorías, codifican corpus y redactan informes. Quien los usa recibe outputs con la forma de una aserción fundamentada, y rara vez tiene criterio para decidir qué parte de ese output puede aceptar, qué parte debe verificar y qué parte le corresponde decidir a él. Los cursos de herramientas enseñan a pedirle cosas a la máquina. Los cursos de método ignoran la máquina. Este curso enseña lo que falta en medio: una teoría de la inferencia suficiente para saber qué razonamiento hace cada quien, y una práctica para marcar esa frontera en el propio trabajo.

## Competencias

Al terminar el curso el estudiante puede:

1. **Distinguir y nombrar** las tres formas de inferencia (deducción, inducción, abducción) y sus regímenes de validez, y reconocerlas en un flujo de investigación real.
2. **Caracterizar** lo que hace un modelo de lenguaje en términos inferenciales, y explicar por qué su output tiene forma de aserción fundamentada sin satisfacer sus condiciones.
3. **Evaluar hipótesis** generadas por un modelo con criterios explícitos de abducción (sorpresa, plausibilidad, verificabilidad, economía de la investigación), en lugar de aceptarlas o rechazarlas por intuición.
4. **Trazar la frontera** entre lo que una máquina puede validar y lo que exige un investigador que responda, y documentarla en un registro auditable sobre el propio proyecto.

## Resultados de aprendizaje y evidencias

| Competencia | Evidencia verificable | Semana |
|---|---|---|
| 1 | Mapa inferencial, versión preliminar | 4 |
| 2 y 3 | Ficha de hipótesis con filtro peirceano sobre tres hipótesis producidas por un modelo | 6 |
| 4 | Registro de frontera de un ejercicio real con un modelo | 7 |
| 1 a 4 | Mapa inferencial final y presentación ante pares | 8 |

## Programa por semanas

| Semana | Tema | Lectura central | Actividad |
|---|---|---|---|
| [1](semana-01.md) | La máquina que afirma. Alucinación o infortunio. Tres sentidos de validación | Austin, conferencias I y II. Floridi (2023) | Bitácora inicial: tres outputs de un modelo clasificados por lo que afirman |
| [2](semana-02.md) | Deducción. La historia de la validación formal: Aristóteles, Frege, Russell, el Tractatus, el Círculo de Viena | Russell, *Los problemas de la filosofía*, cap. VII. Wittgenstein, *Tractatus* 4 a 4.5 | Reconstruir una cadena de razonamiento de un modelo y verificar cada paso |
| [3](semana-03.md) | Inducción. Hume, el pavo de Russell, Goodman, Popper. La IA como máquina inductiva | Hume, *Investigación*, sección IV. Goodman, cap. III. Chollet (2019) | Encontrar dos hipótesis compatibles con los mismos datos |
| [4](semana-04.md) | Abducción. Peirce y la lógica del descubrimiento. Inferencia a la mejor explicación. Análisis abductivo en investigación cualitativa | Peirce (1878, 1903). Harman (1965). Timmermans y Tavory (2012) | Entrega: mapa inferencial preliminar |
| [5](semana-05.md) | Los límites formales. Hilbert, Gödel, Turing. Qué dicen y qué no dicen sobre la inteligencia artificial | Nagel y Newman. Turing (1950). Lucas (1961) y Feferman (2009) | Debate estructurado: el argumento gödeliano a favor y en contra |
| [6](semana-06.md) | El giro pragmático. Segundo Wittgenstein, Austin, Habermas, la comunidad de investigación de Peirce. Validez abductiva e imputación | Wittgenstein, *Investigaciones* §§ 1 a 43 y 201 a 243. Habermas, *Conocimiento e interés*, caps. 5 y 6 | Entrega: ficha de hipótesis con filtro peirceano |
| [7](semana-07.md) | Qué hace un modelo de lenguaje. Predicción, cadena de pensamiento, modelos de recompensa por proceso. Un criterio extrínseco, local y estadístico | Wei et al. (2022). Lightman et al. (2023). Valmeekam et al. (2024). Zainea (2026) | Práctica guiada con modelo y entrega del registro de frontera |
| [8](semana-08.md) | La prótesis hermenéutica. Mapa inferencial del propio proyecto y presentación | Zainea (2026), prótesis hermenéutica. Vallor (2024) | Entrega final y presentación ante pares |

## Metodología

El curso se enseña con el método que enseña. Cada semana tiene tres momentos.

- **Lectura guiada** (asincrónica, 4 a 5 horas). Un texto central con guía de lectura y preguntas, y una lectura complementaria opcional.
- **Sesión presencial con participación remota sincrónica** (2 horas). La primera hora discute la lectura a partir de un caso. La segunda es taller: el estudiante aplica la distinción de la semana a un output real de un modelo o a su propio proyecto. Cada semana tiene un guion minuto a minuto, al menos una figura y, cuando ayuda a ver el mecanismo, una mini app interactiva.
- **Bitácora** (asincrónica, 3 a 4 horas). El estudiante registra en una bitácora semanal el ejercicio, lo que propuso la máquina cuando la hubo, lo que decidió él y con qué criterio. Las bitácoras alimentan los tres productos.

Las prácticas con modelos de lenguaje usan modelos de acceso gratuito. El curso provee las guías de prompts, un cuaderno de apoyo que no requiere programar y cinco mini apps en [apps/](../apps/): verificador de pasos (semanas 2 y 7), silogismos de Peirce y clasificador de inferencias (semana 4), genealogía de la validación y filtro peirceano (semana 6).

## Evaluación

| Producto | Peso | Criterio principal |
|---|---|---|
| Mapa inferencial final | 40 % | Cada paso del flujo está clasificado con justificación, y la frontera está argumentada, no postulada |
| Ficha de hipótesis con filtro peirceano | 25 % | Cada hipótesis se evalúa con los cuatro criterios y la decisión queda explicada |
| Registro de frontera | 20 % | Distingue con precisión lo que propuso la máquina de lo que decidió el investigador |
| Bitácora semanal | 15 % | Continuidad y honestidad en el registro, incluidas las dudas |

La rúbrica detallada está en [evaluacion.md](evaluacion.md).

## Articulación

Este curso es el fundamento de las rutas Texto, Imagen y Programa completo del programa Tunjos para la IA. Se articula con cursos de metodología cualitativa, epistemología, lógica informal y ética de la inteligencia artificial de programas de posgrado en ciencias sociales y humanidades, a los que aporta lo que ellos no suelen cubrir: la clasificación inferencial del trabajo asistido por modelos.

## Política de uso de modelos de lenguaje

Se usan en todas las semanas, de forma declarada. Cada entrega incluye qué modelo se usó, para qué, y qué parte del resultado es decisión del estudiante. Un uso no declarado se trata como infortunio de autoridad: el estudiante presenta como propio algo por lo que no puede responder. Esa es, de hecho, la lección del curso.
