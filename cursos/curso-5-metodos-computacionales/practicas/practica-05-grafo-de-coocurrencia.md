# Práctica 5. Grafo de coocurrencia con lectura interpretativa

Duración estimada: 4 horas, de las cuales 1 en la sesión sincrónica de la semana 4 y media en la de la semana 5.
Requisitos: una tabla de unidades del corpus propio con una columna de códigos, actores o etiquetas separados por punto y coma (columnas `id`, `fecha`, `codigos`), el cuaderno `cuaderno-apoyo.md` y la plantilla `plantillas/lectura-de-grafo.md`.
Quien no programe puede hacer la práctica con la mini app de grafo sobre el conjunto de ejercicio y con una hoja de cálculo para la tabla de umbrales; la lectura, en ese caso, se hace sobre el grafo de ejercicio y la plantilla lo declara.

## Objetivo

Construir el grafo de coocurrencia del corpus propio con una unidad declarada, calcular sus medidas por lo que miden, mostrar qué cambia con tres umbrales y dos algoritmos de comunidades, y escribir una lectura que distinga lo que la red muestra de lo que el investigador propone, con el apoyo de cada propuesta nombrado.

## Antes de la sesión de la semana 4

1. Decida la unidad de coocurrencia. Si tiene el libro de códigos de [*Codificación asistida*](../../curso-4-codificacion-asistida/README.md), los códigos del propio corpus con su definición y sus fragmentos de anclaje, construidos allí con ayuda de un modelo y bajo la responsabilidad del investigador, la unidad es el documento o el segmento codificado. Si tiene actores en noticias, la unidad es la noticia. Si tiene etiquetas de imágenes, la unidad es la imagen. Si no tiene nada de esto, use los grupos de la semana 3 como códigos y los documentos como unidades. Escriba la decisión y su razón en la sección 1 de la plantilla.
2. Construya la tabla de unidades. Cada fila, una unidad; en la columna `codigos`, los códigos presentes separados por punto y coma. Sin datos personales de terceros.

## Durante la sesión de la semana 4 (tres rondas)

### Ronda 1. Construir y medir

Con el bloque de la semana 4 del cuaderno, construya el grafo ponderado con umbral uno: una arista entre dos códigos por cada unidad que comparten, con peso igual al número de unidades. Calcule grado, fuerza e intermediación. Antes de mirar los números, escriba en la sección 2 qué mide cada una en una frase suya. Luego anote los cinco nodos más altos en cada medida y encuentre dos medidas que ordenen los nodos de forma distinta.

### Ronda 2. Mover el umbral

Repita con un umbral medio y uno alto. Los valores dependen del corpus: el medio suele estar donde el grafo deja de ser una maraña, y el alto donde empiezan a aparecer aislados. Para cada umbral, calcule comunidades con el algoritmo de Lovaina y con el de modularidad voraz, cuente componentes y aislados, y liste los puentes. Llene la sección 3. Marque lo que se mantiene en los tres umbrales y en los dos algoritmos.

### Ronda 3. Dibujar dos veces

Dibuje el grafo del umbral medio con dos semillas distintas del algoritmo de disposición. Guarde ambas imágenes. Mire qué nodo "parece central" en cada una y compruebe si lo es por alguna medida. Llene la sección 5 con la advertencia al lector.

## Entre las dos sesiones

1. Lea los candidatos: cada comunidad y cada puente que se mantuvo. Para cada uno, escriba en la sección 4 lo que la red muestra, sin interpretar, y luego lo que usted propone que significa.
2. Nombre el apoyo de cada propuesta: qué documentos del corpus la sostienen, qué teoría de su campo la leería, o ninguno todavía. "Ninguno todavía" es una respuesta válida y se escribe.
3. Pídale a un modelo de lenguaje una lectura alternativa de un puente, con el prompt registrado, y escríbala en la columna correspondiente con lo que decidiría entre las dos.
4. Quite un nodo del grafo, el que más sospeche que sostiene la estructura, y vuelva a calcular comunidades. Anote qué pasó.

## Durante la sesión de la semana 5, revisión en parejas

Cada estudiante lee la lectura de grafo de otro durante quince minutos con una sola instrucción: encontrar al menos una afirmación de la sección 4 que la red no sostiene, o un apoyo que no es tal. El autor corrige o defiende por escrito. No encontrar nada es la excepción, no la cortesía.

## Después de la sesión

Llene la sección 6, la frontera: qué calculó la máquina y cualquiera puede reproducir, qué leyó usted, qué propuso el modelo de lenguaje y qué hizo con ello. Adjunte el archivo de entorno y el código o los pasos. Entregue.

## Qué se evalúa

La construcción declarada, las medidas con lo que miden, la tabla de tres umbrales, la lectura con su apoyo nombrado y el dibujo con su advertencia. Una lectura que dice "ninguno todavía" en tres de cinco apoyos y lo discute vale más que una que inventa un apoyo para cada puente.

## Variante para grupos

Dos estudiantes construyen el grafo del mismo corpus con unidades distintas, el documento y el párrafo, y comparan comunidades y puentes. Lo que cambia con la unidad es la mejor demostración de que el grafo es una hipótesis relacional.
