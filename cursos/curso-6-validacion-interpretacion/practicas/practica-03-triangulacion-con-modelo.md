# Práctica 3. Triangulación con un modelo como segundo codificador

Duración estimada: 3 horas, de las cuales 1 en la sesión sincrónica.
Requisitos: acceso a un modelo de lenguaje de uso gratuito en su versión web (cualquiera sirve) y, si es posible, a un segundo modelo de otra familia; diez fragmentos propios ya codificados; el libro de códigos con que se codificaron; la plantilla `plantillas/matriz-de-triangulacion.md`.
No requiere programar. El cuaderno `cuaderno-apoyo.md` indica cómo hacer lo mismo por programa y cómo calcular el acuerdo si se quiere reportar.

## Objetivo

Hacer codificar diez fragmentos propios por un modelo en dos condiciones, con y sin libro de códigos, declarar antes de correr qué se espera, comparar con la codificación propia, y llenar una fila de la matriz de triangulación por condición, diciendo cuál mide consistencia y cuál cuenta como pata.

## Antes de la sesión

1. Elija diez fragmentos de su material que ya tengan codificación suya o de su equipo. Que sean de distinta dificultad: tres claros, cuatro medios, tres en que usted dudó. Sin datos personales de terceros; si el material es sensible, use una muestra anonimizada.
2. Prepare dos archivos de texto. El primero, los diez fragmentos numerados, sin códigos. El segundo, el libro de códigos: nombre, definición en una o dos frases y un ejemplo por código.
3. Escriba, con fecha y hora, su expectativa para cada condición: en la condición con libro de códigos espero coincidencia alta porque aplica mi regla; en la condición sin libro de códigos espero divergencia en los fragmentos difíciles porque mis categorías vienen de un trasfondo que el modelo no tiene; o lo que usted espere. Esta expectativa se entrega con la matriz y no puede cambiarse después.
4. Llene el encabezado de la plantilla y las instancias que ya tiene, aparte del modelo.

## Tres rondas durante la sesión

### Ronda 1. Con libro de códigos

Dele al modelo el libro de códigos y los diez fragmentos. Use una instrucción que le exija citar y justificar. Ejemplo:

```
Aquí hay un libro de códigos con definiciones y ejemplos, y diez fragmentos
de entrevista numerados. Asigna a cada fragmento uno o más códigos del libro.
Para cada asignación: cita la frase exacta que la sustenta, di por qué ese
código y no el más cercano del libro, y marca si dudaste. No inventes códigos
nuevos; si ningún código aplica, escribe "ninguno" y explica por qué.
```

Copie el output completo al anexo. Compare fragmento por fragmento con su codificación: coincide, difiere, el modelo no asignó. Anote el conteo. Esta fila de la matriz se marca como consistencia: mide cuán bien el modelo aplica su regla, no si la regla es buena.

### Ronda 2. Sin libro de códigos

Abra una conversación nueva, en lo posible con un modelo de otra familia. Dele los diez fragmentos y la pregunta de investigación, nada más. Ejemplo:

```
Aquí hay diez fragmentos de entrevista numerados y la pregunta de investigación:
[pregunta]. Propón códigos para cada fragmento a partir de lo que dice. Para
cada código: nombre breve, definición en una frase, la frase exacta que lo
sustenta, y qué supuesto das por sentado al nombrarlo así.
```

Copie el output al anexo. Compare con su codificación por sentido y no por nombre: un código del modelo converge con uno suyo si recortan el mismo fragmento con la misma razón, aunque el nombre cambie. Anote convergencia, divergencia o silencio por hallazgo. Esta fila puede contar como pata si el modelo es de otra familia que cualquier otro usado en el proyecto y la expectativa se declaró antes.

### Ronda 3. Las divergencias

Tome cada divergencia de la ronda 2 y, antes de decidir si el modelo se equivocó, responda por escrito: qué trasfondo distinto produjo la divergencia. Tres preguntas de apoyo:

- ¿El modelo nombró con una categoría más general que la mía? Entonces lo que diverge es el nivel, y la pregunta es si mi nivel está justificado por el material o por mi marco.
- ¿El modelo nombró algo que yo no vi? Entonces hay que volver al fragmento y decidir si lo que vio está ahí o lo trajo de su corpus.
- ¿El modelo no nombró algo que para mí es obvio? Entonces lo obvio puede ser de mi pertenencia, y hay que decir si la categoría exige pertenecer para verse.

Las divergencias que se explican por prefiguración se registran en la matriz con esa explicación. Las que, después de volver al fragmento, resultan error del modelo, se registran como error, con la frase del fragmento que lo muestra.

## Después de la sesión

1. Complete la matriz con las demás instancias que tenga: otras fuentes, otro método, otra teoría, otro investigador si lo hubo. Marque convergencia, divergencia o silencio por hallazgo y escriba la nota de cada celda.
2. Lea la matriz por columnas y asigne estatuto a cada hallazgo. Los de una sola pata se marcan como conjetura.
3. Lea la matriz por filas y responda si alguna instancia nunca diverge, y por qué.
4. Entregue la matriz con el anexo de instrucciones, outputs literales y expectativas fechadas.

## Qué se evalúa

Que la condición de independencia de cada fila esté declarada y sea correcta, que la expectativa esté fechada antes de correr, que las divergencias tengan explicación por prefiguración y no solo por error, y que los hallazgos de una sola pata estén marcados. No se evalúa el acuerdo: una ronda con bajo acuerdo bien explicada vale más que una con acuerdo alto que se presenta como validación.

## Variante para grupos

Dos estudiantes intercambian fragmentos y libros de códigos y cada uno codifica el material del otro antes de ver la codificación original. Esa fila sí es de investigadores independientes. Compararla con la fila del modelo bajo la misma condición es el mejor material de discusión: suele mostrar que el par humano diverge donde el modelo converge, y al revés.
