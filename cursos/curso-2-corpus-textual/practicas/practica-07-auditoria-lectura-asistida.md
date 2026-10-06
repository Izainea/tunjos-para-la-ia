# Práctica 7. Auditoría de la lectura asistida

Duración estimada: 4 horas, de las cuales 1 en la sesión sincrónica.
Requisitos: la tabla `unidades.csv` del corpus propio, acceso a un modelo de lenguaje (versión web gratuita o interfaz de programación con cuota gratuita), la plantilla `plantillas/registro-de-frontera-corpus.md`. Bloques de código en `practicas/cuaderno-apoyo.md`, sección "Semana 7". La práctica se puede hacer sin programar, con la versión web del modelo y dos hojas de cálculo; el cuaderno solo la hace repetible.

## Objetivo

Hacer que un modelo etiquete una muestra del corpus con una instrucción escrita y versionada, etiquetar la misma muestra a ciegas, medir el desacuerdo, tipificarlo, decidir qué se hace con las etiquetas del resto del corpus, y dejar todo en el registro de frontera.

## Antes de la sesión

1. Escriba la lista de categorías con que quiere etiquetar las unidades de su corpus. Entre tres y siete. Para cada una, una definición de dos líneas y un ejemplo de su corpus.
2. Escriba la regla para la duda: qué debe hacer el etiquetador cuando ninguna categoría aplica o cuando aplican dos.
3. Reúna todo en `instruccion_v1.md`, con el formato de salida al final: una sola palabra, la categoría, sin explicación.
4. Elija la muestra con el bloque del cuaderno (treinta unidades al azar con semilla fija) o, sin programar, numerando las unidades y tomando treinta números de una tabla de azar. Anote cómo la eligió.

## Tres rondas durante la sesión

### Ronda 1. La máquina etiqueta

Envíe cada unidad de la muestra al modelo con la instrucción, por programa o pegando en la versión web la instrucción seguida de la unidad. Guarde cada respuesta con la fecha, el modelo y la versión de la instrucción. Cierre el archivo y no lo vuelva a abrir hasta la ronda 3.

### Ronda 2. Usted etiqueta a ciegas

En una tabla aparte, con la misma instrucción delante, etiquete las treinta unidades. No mire lo que dijo el modelo. Si una unidad le hace dudar, aplique la regla para la duda y anote que dudó: esas unidades van a ser las interesantes.

### Ronda 3. Comparar y tipificar

Una las dos tablas. Calcule la proporción de acuerdo y kappa con el bloque del cuaderno o a mano. Para cada desacuerdo, vuelva a leer la unidad y clasifíquelo:

| Tipo | Qué pasó |
|---|---|
| Generalización ajena | El modelo leyó algo como se lee en su entrenamiento, no como se lee en este corpus |
| Categoría forzada | Ninguna categoría aplicaba y el modelo eligió una en lugar de usar la regla para la duda |
| Contexto local | El modelo no sabía algo del periodo, del lugar o de la institución que usted sí sabe |
| Lectura literal | Ironía, fórmula de cortesía o cita que el modelo tomó al pie de la letra |
| Error propio | Usted se equivocó, y lo nota al releer |
| Lista defectuosa | Dos categorías se solapan y el desacuerdo mide la lista, no la lectura |

Cuente cuántos de cada tipo. Si predomina "lista defectuosa" o "categoría forzada", el problema está en la instrucción. Si predomina "contexto local", el problema está en lo que el modelo no puede saber. Si predomina "error propio", hay que revisar la lectura propia antes de culpar a nadie.

## La decisión

Elija una de las tres y escriba la razón:

1. Aceptar las etiquetas del modelo para el resto del corpus, con la tasa de acuerdo declarada en el informe y las categorías problemáticas marcadas.
2. Corregir la instrucción (`instruccion_v2.md`), etiquetar una muestra nueva y repetir la auditoría.
3. Rechazar la lectura asistida para esta tarea, porque los desacuerdos tocan lo que la pregunta de investigación necesita.

Ninguna es la respuesta correcta en general. La que elija tiene que seguirse de la tipología.

## Después de la sesión

1. Llene la sección de auditoría del registro de frontera y actualice las filas de las semanas anteriores.
2. Si eligió corregir, haga la segunda vuelta antes de la semana 8 y reporte las dos auditorías.
3. Escriba la sección 13 del informe de corpus con la plantilla.

## Qué se evalúa

La precisión de la auditoría, no la tasa de acuerdo. Una auditoría con 60 % de acuerdo, desacuerdos bien tipificados y la decisión de corregir vale más que una con 95 % de acuerdo y la decisión de aceptar sin haber leído los desacuerdos.

## Variante para grupos

Dos estudiantes etiquetan la misma muestra de uno de los dos corpus, a ciegas, con la misma instrucción. Ahora hay tres etiquetadores: el modelo y dos personas. El acuerdo entre las dos personas es la cifra de referencia contra la que se lee el acuerdo con el modelo.
