# Práctica 3. Representación y agrupamiento con prueba de estabilidad

Duración estimada: 5 horas, de las cuales 1 en la sesión sincrónica de la semana 3 y el resto repartido entre las semanas 2 y 3.
Requisitos: el corpus propio en una tabla con una fila por documento (columnas `id`, `fecha`, `texto`; para imágenes, `ruta` en vez de `texto`), el cuaderno `cuaderno-apoyo.md` con el entorno instalado, y la plantilla `plantillas/ficha-de-patron.md`.
Quien no programe puede hacer la práctica con la mini app de embeddings sobre el conjunto de ejercicio y con una hoja de cálculo para la tabla de estabilidad; en ese caso la representación no es la del corpus propio y la ficha lo declara.

## Objetivo

Representar el corpus propio como vectores con una representación declarada, agruparlo con k-means y con agrupamiento jerárquico, someter cada grupo a tres pruebas de estabilidad y leer los que sobreviven como candidatos a categoría, con sus contraejemplos.

## Antes de la sesión

1. Escriba en la sección 0 de la ficha lo que espera encontrar. Hágalo antes de calcular nada; es la parte de la práctica que no se puede repetir.
2. Calcule los vectores del corpus con el bloque de la semana 2 del cuaderno. Registre el modelo, la versión y la dimensión en la sección 1 de la ficha. Si el corpus es visual, use el bloque de CLIP; si no puede correr modelos, use TF-IDF y declárelo.
3. Lea los vecinos de diez documentos que conozca bien y llene la tabla de vecinos. Busque al menos un choque entre lo que el modelo acerca y lo que su corpus junta.
4. Calcule una segunda representación (TF-IDF si la primera fue embeddings, o un segundo modelo de embeddings). Guárdela: es la tercera prueba de estabilidad.

## Durante la sesión (tres rondas)

### Ronda 1. Agrupar varias veces

Corra k-means para k de 2 a 10 con cinco semillas cada uno, con el bloque de la semana 3 del cuaderno. Grafique la silueta y la inercia por k, y dibuje el dendrograma del agrupamiento jerárquico. Mire las tres cosas y elija dos valores de k razonables. Anote por qué los eligió; "porque la silueta es máxima" es una razón del método, y "porque mi pregunta distingue entre cuatro tipos de discurso" es una razón de la pregunta. Las dos valen, y la ficha pide cuál fue.

### Ronda 2. Probar la estabilidad

Para cada uno de los dos valores de k, con la semilla 0 como referencia, calcule para cada grupo:

- el Jaccard medio contra la mejor coincidencia en las otras cuatro semillas;
- el Jaccard contra la mejor coincidencia con k menos uno y con k más uno;
- el Jaccard contra la mejor coincidencia en la segunda representación.

Calcule también el índice de Rand ajustado entre particiones completas. Llene la sección 3 de la ficha. Un grupo es candidato si pasa las tres pruebas con los umbrales que el grupo fije en la sesión; el curso sugiere 0,8 para la semilla y 0,6 para las otras dos, y acepta otros umbrales si se declaran.

### Ronda 3. Leer los candidatos

Para cada candidato, liste los cinco miembros más cercanos al centro y los tres más lejanos. Léalos. Proponga un nombre. Pídale a un modelo de lenguaje que proponga otro a partir de los mismos ocho miembros, y registre el prompt. Llene la sección 4 de la ficha con los miembros que el nombre explica y los que no. Decida: adopta, corrige o rechaza cada nombre, con razones que no repitan lo que dijo el modelo.

## Después de la sesión

1. Compare la sección 0 con lo que sobrevivió. Escriba qué coincidió, qué no y qué le sorprendió.
2. Escriba lo que dicen los grupos que no sobrevivieron: ¿dependen de la semilla, de k o de la representación? ¿Qué le enseña eso sobre su corpus o sobre el instrumento?
3. Corra el bloque de registro de entorno del cuaderno y adjunte el archivo que produce. Entregue la ficha con el código o los pasos en anexo.

## Qué se evalúa

La justificación de la representación, la prueba de estabilidad completa, el reporte honesto de lo que no sobrevivió, y la lectura de cada candidato con sus contraejemplos. Una ficha con dos candidatos bien probados y tres grupos reportados como inestables vale más que una con cinco grupos limpios y una sola corrida.

## Variante para grupos

Dos estudiantes con corpus parecidos intercambian vectores y corren la prueba de estabilidad sobre el corpus del otro. Las diferencias en los candidatos que cada uno declara son el mejor material de discusión: muestran cuánto de la lectura viene del corpus y cuánto de quien lee.
