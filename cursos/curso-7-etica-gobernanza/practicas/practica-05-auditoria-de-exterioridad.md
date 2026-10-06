# Práctica 5. Auditoría de exterioridad sobre una muestra propia

Duración estimada: 5 horas, de las cuales 1 en la sesión sincrónica y al menos 1 con el lector situado.
Requisitos: una muestra de entre diez y veinte piezas del propio corpus que cumpla la matriz de riesgos de la semana 3, al menos un lector situado que haya aceptado participar, acceso a un modelo de uso gratuito en su versión web, y la plantilla `plantillas/auditoria-de-exterioridad.md`.
No requiere programar.

## Objetivo

Medir qué excluye un modelo al leer material situado del propio corpus, clasificando las diferencias entre su lectura y la de un lector que participa en la forma de vida que produjo el material, y derivar de ahí una regla para el protocolo de gobernanza.

## Antes de la sesión

1. Elija la muestra por carga cultural. Pregúntese, pieza por pieza, si alguien de fuera la entendería sin explicación. Las que no, entran. Escriba el criterio en la sección 1 de la plantilla, con una frase sobre qué exagera la muestra por construcción: una muestra elegida así encuentra más exclusiones que el corpus completo, y eso es lo que se quiere, pero no puede presentarse como medida del modelo en general.
2. Verifique cada pieza contra la matriz de riesgos. Ninguna clasificada como "no usar". Las que tienen datos personales salen anonimizadas o como descripción densa. Si la descripción la hace usted, la pieza que el modelo lee es la descripción y la plantilla lo dice.
3. Consiga el lector situado. Explíquele qué va a leer, cuánto tiempo toma, que puede retirarse de cualquier pieza y que decide cómo se le reconoce en el informe. Registre su consentimiento con fecha en la sección 2. Si el lector situado es usted mismo porque pertenece a la comunidad, declárelo; se admite, pero la auditoría pierde la mirada externa y la sección 8 debe decirlo.
4. Pídale al lector situado que escriba, para cada pieza, una o dos frases: qué es, qué hace en la vida de quien la produjo o la usa, qué palabra local la nombra. Esto se hace antes de cualquier consulta al modelo y la fecha queda en la sección 3. El orden no se puede invertir: si el lector ve primero la lectura del modelo, su propia lectura se contamina por adhesión o por reacción.

## Durante la sesión: pasos 3 a 5

### Paso 3. La lectura del modelo

Fije con el grupo una instrucción única que pida descripción y significado sin sugerir categorías. Un punto de partida:

```
Describe esta pieza y explica qué significa para las personas que la produjeron
o la usan. Si hay algo que no puedes interpretar con seguridad, dilo. No uses
categorías generales si puedes usar el nombre específico de lo que ves.
```

Copie la instrucción literal en la sección 4. Consulte las piezas una por una, con la misma instrucción, y copie cada salida literal en la columna correspondiente de la sección 5. Registre modelo, versión y fecha. Si quiere comparar variantes (la misma instrucción en inglés, o con una frase de contexto sobre el lugar y la época), cada variante es una ronda y se registra aparte; no mezcle rondas en la misma tabla.

### Paso 4. El contraste

Para cada pieza ponga frente a frente la categoría local y la lectura del modelo, y decida el tipo de exclusión:

- Entendió mal: el modelo dijo algo que el lector situado considera falso en los términos de la comunidad. No cuenta un error factual sobre la pieza (una fecha, un nombre), que se anota aparte; cuenta una lectura que la comunidad rechazaría.
- Aplanó: el modelo sustituyó un sentido específico por una categoría general, correcta pero vacía. "Decoración" por un altar; "costumbre local" por una práctica con nombre; "una reunión" por una escena cuyo sentido está en quién falta.
- Ignoró: el modelo no dijo nada sobre algo que el lector situado considera central. La pregunta de apoyo es qué diría el lector situado que el modelo no dijo.

La clasificación la hace usted con el lector situado, nunca el modelo. En la columna siguiente copie lo que el lector situado dijo de la diferencia, con sus palabras. En la última, decida si la exclusión sería corregible con contexto en la instrucción, con categorías locales en el andamiaje, o si es un límite que hay que declarar.

### Paso 5. El perfil

Cuente las piezas por tipo de exclusión en la sección 6 y escriba qué tienen en común las piezas de cada tipo. Ahí está el resultado: no la cifra sino el patrón. Un modelo que aplana lo religioso y entiende bien lo político le dice dónde puede delegar y dónde no. Formule una hipótesis sobre la precomprensión del modelo que ese patrón sugiere, y escriba la regla que se deriva para el protocolo en la sección 7: en qué tipo de piezas la lectura del modelo no se acepta sin lector situado.

## Después de la sesión

1. Vuelva con el lector situado sobre las piezas en que la clasificación fue dudosa. Registre al menos una en la sección 6. Si hubo dos lectores y discreparon, registre ambas lecturas sin promediar.
2. Escriba la sección 8, lo que no se pudo medir. Es una sección evaluada: una auditoría sin límites declarados es menos creíble que una con ellos.
3. Confirme con el lector situado la forma de reconocimiento que eligió y que ninguna pieza de la que se retiró aparece en la entrega.
4. Entregue la plantilla completa con las salidas literales del modelo como anexo.

## Qué se evalúa

El criterio de la muestra, el orden entre lector situado y modelo, la clasificación con cita del lector situado, el perfil con su regla, y la declaración de límites. No se evalúa cuánto acertó el modelo: una auditoría en que el modelo leyó bien casi todo y el estudiante lo mostró con el mismo rigor vale lo mismo que una en que aplanó todo.

## Variante con dos lectores situados

Dos lectores escriben las categorías locales por separado y sin verse. La auditoría registra tres lecturas por pieza y clasifica dos diferencias: entre lectores, y entre cada lector y el modelo. Las piezas en que los lectores discrepan entre sí son las que mejor muestran que la referencia es una posición y no una verdad, y la sección 8 debe discutirlo.

## Variante por programa

Quien quiera repetir la auditoría con varios modelos o con varias rondas puede usar el [cuaderno de apoyo](../../curso-1-tres-inferencias/practicas/cuaderno-apoyo.md) de [*Las tres inferencias*](../../curso-1-tres-inferencias/README.md), un conjunto de bloques de Python pensado para quien no programa, que envía cada consulta a un modelo y guarda en un archivo la fecha, el modelo, la instrucción y la respuesta, de modo que el archivo sirve de anexo literal. La clasificación sigue siendo manual y con el lector situado.
