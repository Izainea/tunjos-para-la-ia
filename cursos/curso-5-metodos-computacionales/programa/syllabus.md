# Syllabus

## Datos generales

| | |
|---|---|
| Nombre | Métodos computacionales para el sentido |
| Programa | Tunjos para la IA, curso 5 de 7. Capa de Juicio |
| Duración | Ocho sesiones semanales de dos horas y trabajo autónomo guiado, unas 96 horas en total. Se adapta al formato de microcredencial o de curso de educación continua de cada institución |
| Modalidad | Híbrida: una sesión presencial de dos horas por semana, con participación remota sincrónica, y trabajo asincrónico guiado. La modalidad virtual es alternativa |
| Docente | Carlos Isaac Zainea Maya |
| Prerrequisitos | Recomendado: curso 2 o curso 3 del programa, o nociones básicas de Python. El curso provee un cuaderno de apoyo que se copia bloque a bloque y mini apps que no requieren programar |
| Público | Egresados y estudiantes de posgrado en ciencias sociales y humanidades que ya tienen un corpus, textual o visual, y quieren aplicarle métodos computacionales sin perder el criterio para leer lo que sale |

## Problema que atiende

Los métodos computacionales llegaron a las ciencias sociales y a las humanidades con una promesa y un riesgo. La promesa es la escala: miles de documentos o de imágenes representados como vectores, agrupados, conectados en redes y seguidos en el tiempo. El riesgo es que cada uno de esos instrumentos produce patrones con la misma facilidad con que un microscopio desenfocado produce formas. El número de grupos lo fija quien corre k-means; las comunidades de un grafo cambian con el umbral de peso; la fecha en que un tema "emerge" depende del ancho de la ventana. Quien no sabe esto presenta como hallazgo lo que es una decisión de parámetro. Quien lo sabe sin método se paraliza. El curso enseña lo que está en medio: cómo obtener el patrón, cómo probar si sobrevive a mover el parámetro, y cómo leerlo como lo que es, una hipótesis que alguien tiene que comprometerse a perseguir.

## Competencias

Al terminar el curso el estudiante puede:

1. **Representar** un corpus propio, textual o visual, como vectores, y explicar qué conserva y qué pierde cada representación, desde la bolsa de palabras hasta los embeddings de un modelo entrenado en otra parte.
2. **Aplicar** agrupamiento, redes de coocurrencia y series temporales al corpus propio, y someter cada patrón obtenido a una prueba de estabilidad frente a sus parámetros.
3. **Leer** un patrón como hipótesis abductiva: distinguir patrón de artefacto, decir desde qué trasfondo sorprende, formular la hipótesis con su prueba y su costo.
4. **Construir** un tablero analítico que declare lo que cada vista afirma y sus parámetros, y registrar la frontera entre lo que calculó la máquina y lo que interpretó el investigador.

## Resultados de aprendizaje y evidencias

| Competencia | Evidencia verificable | Semana |
|---|---|---|
| 1 y 2 | Representación y agrupamiento del corpus propio con prueba de estabilidad | 3 |
| 2 y 3 | Grafo de coocurrencia con lectura interpretativa | 5 |
| 3 y 4 | Tablero analítico con ficha de hipótesis y registro de frontera computacional, y presentación ante pares | 8 |
| 1 a 4 | Bitácora semanal | 1 a 8 |

## Programa por semanas

| Semana | Tema | Lectura central | Actividad |
|---|---|---|---|
| [1](semana-01.md) | Qué es un patrón. De la frecuencia al vector; distancia y similitud; lo que se pierde al representar | Grimmer, Roberts y Stewart (2022), caps. 1 a 3 | Medir la similitud entre fragmentos del corpus propio y anotar qué no captura la medida |
| [2](semana-02.md) | Embeddings de texto e imagen. Qué codifican y qué no; el sesgo del entrenamiento como precomprensión ajena | Mikolov et al. (2013). Reimers y Gurevych (2019) | Calcular embeddings del corpus propio y leer los vecinos más cercanos |
| [3](semana-03.md) | Agrupamiento. k-means y jerárquico; el número de grupos como decisión; estabilidad; cuándo un grupo es una categoría | Grimmer, Roberts y Stewart (2022), cap. 12 | Entrega: representación y agrupamiento con prueba de estabilidad |
| [4](semana-04.md) | Redes. Coocurrencia de códigos, actores y etiquetas; grado, centralidad, comunidades; el grafo como hipótesis relacional | Newman (2018), caps. 6 y 7. Barabási (2016), cap. 2 | Construir el grafo del corpus propio y leerlo con tres umbrales |
| [5](semana-05.md) | Tiempo. Series del corpus por periodo; ventanas, tendencias, rupturas; cuándo emerge algo | Kleinberg (2003). Grimmer, Roberts y Stewart (2022), cap. 2 | Entrega: grafo de coocurrencia con lectura interpretativa |
| [6](semana-06.md) | Modelado de temas y lectura distante. Temas como sugerencias | Blei (2012). Moretti (2015), "Conjeturas sobre la literatura mundial". Arnold y Tilton (2019) | Modelar temas del corpus propio con dos valores de K y comparar |
| [7](semana-07.md) | Visualización que no engaña. Escalas, colores, lo que una vista afirma; tableros para investigar, no para vender | Tufte (2001), caps. 2 y 4. Drucker (2011) | Montar el tablero: cada vista con su pregunta y sus parámetros |
| [8](semana-08.md) | Del patrón a la hipótesis. Ficha de hipótesis sobre un patrón propio; registro de frontera; presentación | Peirce (1903). Timmermans y Tavory (2012) | Entrega final y presentación ante pares |

## Metodología

El curso se enseña con el método que enseña. Cada semana el estudiante obtiene un patrón de su corpus con un instrumento, mueve el parámetro del instrumento, registra qué cambia, y escribe la lectura que el instrumento no escribe. Tres momentos:

- **Lectura guiada** (asincrónica, 4 a 5 horas). Un texto central con guía de lectura y una lectura complementaria opcional. Las lecturas técnicas se leen por lo que miden, no por sus fórmulas.
- **Sesión sincrónica** (2 horas). La primera hora discute la lectura sobre una mini app que muestra el mecanismo de la semana. La segunda es taller sobre el corpus propio, con el cuaderno de apoyo o con las apps.
- **Bitácora** (asincrónica, 3 a 4 horas). El estudiante registra el patrón obtenido, los parámetros usados, el resultado de moverlos y su lectura. Las bitácoras alimentan los tres productos.

Las prácticas usan bibliotecas abiertas de Python y modelos de embeddings de descarga libre. Quien no programe puede hacer todo el curso con las mini apps y con una hoja de cálculo, salvo el cálculo de embeddings del corpus propio, para el que el cuaderno trae bloques que se copian sin modificar.

## Evaluación

| Producto | Peso | Criterio principal |
|---|---|---|
| Tablero analítico con ficha de hipótesis y registro de frontera | 40 % | Cada vista declara lo que afirma y sus parámetros; la hipótesis está formulada con su prueba; la frontera entre cálculo y lectura es precisa |
| Representación y agrupamiento con prueba de estabilidad | 25 % | La representación está justificada y los grupos que se presentan como categorías sobrevivieron a cambiar semilla, k y representación |
| Grafo de coocurrencia con lectura interpretativa | 20 % | La lectura distingue lo que la red muestra de lo que el investigador propone, y declara qué cambia con el umbral |
| Bitácora semanal | 15 % | Continuidad y honestidad en el registro de parámetros, pruebas y dudas |

La rúbrica detallada está en [evaluacion.md](evaluacion.md).

## Articulación

El curso cierra la ruta Computacional del programa (cursos 2, 3 y 5) y pertenece a la capa de Juicio junto con los cursos 6 y 7. Recibe el corpus catalogado del curso 2 o 3 y, cuando lo hay, el libro de códigos del curso 4. Entrega al curso 6 un conjunto de patrones con su lectura y su prueba de estabilidad, que es el material sobre el que allí se valida y se escribe. Se articula con cursos de métodos cuantitativos, análisis de redes sociales y humanidades digitales de programas de posgrado, a los que aporta lo que no suelen cubrir: la prueba de estabilidad como condición de la lectura.

## Política de uso de modelos de lenguaje

Los modelos de lenguaje se usan de forma declarada para escribir y depurar código, para proponer etiquetas de grupos y temas, y para redactar lecturas preliminares que el estudiante corrige. Cada entrega declara qué modelo se usó, para qué, y qué parte del resultado es decisión del estudiante. Las etiquetas que un modelo propone para un grupo o un tema son hipótesis del modelo, no del estudiante, hasta que él las lee contra los miembros del grupo y las adopta o las rechaza con razones. Un uso no declarado se trata como infortunio de autoridad: el estudiante presenta como propio algo por lo que no puede responder, y la entrega se devuelve para que escriba el registro que faltaba.
