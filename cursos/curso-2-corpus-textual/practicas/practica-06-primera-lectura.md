# Práctica 6. Primera lectura computacional del corpus propio

Duración estimada: 4 horas, de las cuales 1 en la sesión sincrónica.
Requisitos: el corpus propio en `limpio` con la tabla `unidades.csv` de la semana 5, el catálogo maestro validado, y la mini app `apps/concordancias.html` para ensayar antes de programar. Bloques de código en `practicas/cuaderno-apoyo.md`, sección "Semana 6".

## Objetivo

Aplicar los cuatro instrumentos de la semana (frecuencias, concordancia, colocaciones, dominios léxicos) al corpus propio, y producir para cada uno la tabla que lo documenta: qué produce, qué sugiere y qué líneas se leyeron para decirlo.

## Antes de la sesión

1. Elija desde el protocolo tres palabras nodo: palabras que su pregunta de investigación necesita entender en este corpus. No elija las más frecuentes; elija las que importan.
2. Abra la mini app de concordancias y ensaye con el corpus de demostración: cambie la ventana, mire cómo cambian las colocaciones, lea las líneas. Anote qué espera encontrar en su propio corpus para cada palabra nodo.
3. Escriba a mano una primera lista de palabras para dos dominios léxicos de su proyecto.

## Durante la sesión: cuatro instrumentos

### Frecuencias

Ejecute el bloque de frecuencias con y sin palabras funcionales. Anote en una celda de texto la lista de funcionales que quitó y por qué esas. Mire las veinte palabras de contenido más frecuentes y responda: ¿cuántas esperaba? ¿Cuáles no? Las que no esperaba son candidatas a palabra nodo para una segunda vuelta.

### Concordancia

Para cada palabra nodo, produzca la concordancia con ventana de cinco y lea veinte líneas, con su identificador y posición. Mientras lee, clasifique los usos: si "orden" aparece como "orden público" y como "orden del día", son dos palabras que el conteo fundió. Anote cuántos usos distintos encontró y cuál predomina.

### Colocaciones

Produzca las colocaciones de cada nodo con ventana de cuatro y mínimo de cinco apariciones. Si el mínimo deja la lista vacía, su corpus es pequeño para este instrumento y eso se anota; no baje el mínimo para que aparezca algo. Para la colocación más alta de cada nodo, vuelva a la concordancia y lea las líneas donde ocurre: ¿la asociación significa lo que parece?

### Dominios léxicos

Pida al modelo palabras para cada dominio dándole el nombre del dominio y diez líneas de concordancia. Acepte o rechace una por una; anote las rechazadas con la razón. Calcule el peso de cada dominio por fuente y por año como proporción por mil palabras. Mire la tabla y escriba una frase sobre lo que sugiere, y debajo, las líneas que leyó para escribirla.

## Después de la sesión

1. Llene la tabla de instrumentos:

| Instrumento | Qué produce | Qué sugiere | Qué líneas se leyeron |
|---|---|---|---|
| Frecuencias | | | |
| Concordancia de … | | | |
| Colocaciones de … | | | |
| Dominio … por fuente | | | |

2. Exporte a `salidas/` cada tabla con el nombre de la celda que la produjo.
3. Guarde el cuaderno como `cuadernos/04-lectura.ipynb`, reinicie y ejecute de arriba abajo.
4. Anote en el registro de frontera las palabras que propuso el modelo y la interpretación que propuso de las colocaciones, con su decisión.

## Qué se evalúa

La relación entre lo que el instrumento sugiere y lo que usted afirma. Una tabla de colocaciones seguida de "el corpus asocia orden con policía" sin líneas leídas no está en nivel Logrado. La misma tabla seguida de "en 14 de las 19 líneas la asociación es con la policía municipal; en las otras 5 'orden' es orden del día; se lee como X por Y" sí.

## Variante para grupos

Dos estudiantes con corpus distintos eligen la misma palabra nodo y comparan concordancias. Lo que la palabra hace en un corpus y no en el otro es la mejor demostración de que la frecuencia no es el sentido.
