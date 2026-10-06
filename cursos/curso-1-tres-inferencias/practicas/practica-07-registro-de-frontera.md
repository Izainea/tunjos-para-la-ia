# Práctica 7. Registro de frontera sobre una tarea real

Duración estimada: 3 horas, de las cuales 1 en la sesión sincrónica.
Requisitos: acceso a un modelo de lenguaje de uso gratuito en su versión web (cualquiera sirve; el curso no exige uno en particular) y la plantilla `plantillas/registro-de-frontera.md`.
No requiere programar. Para quien quiera, el cuaderno `cuaderno-apoyo.md` indica cómo hacer lo mismo por programa.

## Objetivo

Ejecutar con un modelo una tarea pequeña y real del propio proyecto, y producir el registro de frontera que distingue, paso a paso, lo que propuso la máquina de lo que decidió el investigador.

## Antes de la sesión

1. Elija una tarea real y acotada. Tres opciones probadas:
   - **Codificar.** Diez fragmentos de texto (entrevistas, prensa, documentos) o diez imágenes descritas, con el objetivo de proponer códigos iniciales.
   - **Sintetizar.** Tres fuentes de su bibliografía, con el objetivo de obtener un estado de la cuestión en una página.
   - **Categorizar.** Un listado de veinte a cuarenta elementos (títulos, hashtags, cartelas, titulares) con el objetivo de proponer categorías.
2. Prepare el material en un archivo de texto. No incluya datos personales de terceros.
3. Abra la plantilla del registro y llene el encabezado.

## Durante la sesión (tres rondas)

### Ronda 1. La máquina propone

Pídale al modelo que ejecute la tarea. Use un prompt que exija pasos explícitos. Ejemplo para codificar:

```
Tengo diez fragmentos de entrevistas sobre [tema]. Propón códigos iniciales
para cada fragmento. Para cada código, indica: el fragmento literal que lo
sustenta, por qué ese código y no otro más general, y qué otros fragmentos
del conjunto lo comparten. Trabaja paso a paso y numera cada decisión.
```

Copie el output completo a un anexo. Luego, en el registro, una fila por paso numerado del modelo. En la columna "qué propuso" sea fiel: no resuma de forma que mejore o empeore lo que dijo.

### Ronda 2. El investigador decide

Para cada fila, antes de seguir con el modelo, llene las columnas "tipo de inferencia", "qué decidí" y "criterio". Preguntas de apoyo:

- ¿Este paso se sigue por forma de los anteriores (deducción), generaliza sobre los fragmentos (inducción) o introduce una idea que no estaba en ellos (abducción)?
- Si acepto, ¿puedo decir por qué sin repetir lo que dijo el modelo?
- Si corrijo, ¿qué sé yo que el modelo no sabía? ¿Es conocimiento del tema, del contexto, de la comunidad?
- Si rechazo, ¿es porque está mal o porque no puedo verificarlo? Son cosas distintas; anote cuál.

### Ronda 3. Segunda vuelta con lo decidido

Devuélvale al modelo sus decisiones y pídale que continúe (por ejemplo, agrupar los códigos aceptados en categorías). Registre la nueva ronda igual. Observe si el modelo incorpora sus correcciones o vuelve a su propuesta inicial de otra forma.

## Después de la sesión

1. Llene "los casos difíciles" y "aceptaciones acríticas". No omita ninguna aceptación sin criterio: anotarlas es parte de la nota.
2. Llene el balance. Responda en especial si la frontera de esta tarea coincide con la de su mapa inferencial preliminar. Si no coincide, cuál de los dos documentos corrige al otro.
3. Entregue el registro con el anexo de prompts y outputs literales.

## Qué se evalúa

La precisión de la distinción, no el éxito de la tarea. Un registro en que el modelo hizo un trabajo mediocre y el estudiante lo detectó paso a paso vale más que uno en que el modelo hizo un trabajo brillante y el estudiante lo aceptó sin criterio.

## Variante para grupos

Dos estudiantes ejecutan la misma tarea con el mismo material y comparan registros. Las filas en que uno aceptó y el otro rechazó son el mejor material de discusión de la sesión.
