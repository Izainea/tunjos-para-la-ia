# Práctica 6. Matriz de acuerdo y análisis de desacuerdos

Duración estimada: 3 horas, de las cuales 1 en la sesión sincrónica de la semana 6.
Requisitos: el libro de códigos abierto fijado en la semana 4 (no se modifica durante la práctica); treinta fragmentos del corpus, numerados; acceso a un modelo de lenguaje en su versión web; la plantilla `plantillas/matriz-de-acuerdo.md`.
Para el cálculo: la mini app de la semana 3 calcula kappa para sus doce fragmentos fijos; para los treinta propios, el cuaderno `cuaderno-apoyo.md` calcula kappa y alfa con dos bloques copiables, o se calcula a mano con la tabla de la sección 3.

## Objetivo

Medir el acuerdo entre el investigador y el modelo al aplicar un mismo libro de códigos a los mismos fragmentos, interpretarlo como consistencia y no como validez, y convertir cada desacuerdo en una decisión sobre el libro.

## Antes de la sesión, codificar a ciegas

1. Elija treinta fragmentos que no haya codificado con el modelo en la práctica 3, o, si todo el corpus pasó ya por el modelo, treinta fragmentos elegidos al azar con un intervalo (cada segundo o tercer fragmento).
2. Codifique los treinta a mano con el libro fijo, un código por fragmento (el que predomina). Si el fragmento no cabe en ningún código, anote "ninguno" y la razón. Guarde el resultado con fecha.
3. No le pida nada al modelo antes de terminar este paso. La matriz mide acuerdo solo si usted codificó sin haber visto la salida del modelo.

## En la sesión

### Paso 1. El modelo aplica el libro

```
Este es un libro de códigos con [n] códigos. Para cada uno, nombre,
definición, qué incluye y qué excluye:
[pegue el libro completo]

Codifica los siguientes fragmentos numerados aplicando exactamente este libro.
Asigna a cada fragmento un solo código, el que predomina. No propongas
códigos nuevos: si ningún código cabe, escribe "ninguno" y explica por qué.
Responde con una tabla: número de fragmento, código, frase del fragmento que
justifica la elección.

Fragmentos:
[1] ...
```

Copie la salida al anexo con fecha. Si el modelo propuso un código nuevo a pesar de la instrucción, anótelo: cuenta como categoría aparte en el cálculo y como señal de forzamiento en el análisis.

### Paso 2. La matriz y el cálculo

Llene la sección 1 de la plantilla con los dos códigos por fragmento. Calcule:

- Acuerdo simple: fragmentos en acuerdo dividido por treinta.
- Kappa de Cohen: con el cuaderno, o a mano con la tabla de abajo.
- Alfa de Krippendorff nominal: con el cuaderno.

Cálculo a mano de kappa para quien no use el cuaderno. Construya la tabla de marginales:

| Código | Veces que lo usé yo (a) | Veces que lo usó el modelo (b) | a × b |
|---|---|---|---|
| … | | | |
| Suma | 30 | 30 | S |

El acuerdo esperado por azar es pe = S / (30 × 30). El acuerdo observado po es el acuerdo simple. Kappa = (po - pe) / (1 - pe). Reporte po, pe y kappa con dos decimales y coma decimal.

### Paso 3. La explicación del modelo

Para cada desacuerdo, pídale al modelo que explique su elección, sin decirle cuál fue la suya:

```
En el fragmento [n] asignaste el código "[X]". Explica, citando el fragmento,
por qué ese y no "[Y]" según las definiciones del libro.
```

Copie la explicación literal a la columna correspondiente. Léala con cuidado: a veces la explicación muestra que la definición de Y es estrecha; a veces muestra que el modelo aplicó la palabra y no el sentido.

### Paso 4. Leer los desacuerdos uno a uno

Clasifique cada desacuerdo con los tipos de la plantilla (A a G), decida quién tiene razón y con qué criterio, y derive una decisión sobre el libro: nueva regla, definición ampliada, fusión, ejemplo negativo, anotación de forzamiento, corrección propia. La decisión no se aplica al libro durante la práctica; se aplica después, y queda en la sección 5.

### Paso 5. Acuerdos sospechosos

Repase los fragmentos en acuerdo y busque al menos uno en que la coincidencia pueda deberse a que usted y el modelo comparten la literatura y no a lo que el fragmento dice. Si no encuentra ninguno, dígalo y diga por qué lo cree.

## Después de la sesión

1. Complete las secciones 5, 6 y 7 de la plantilla.
2. Escriba la frase final con los valores obtenidos: qué mide el acuerdo y qué no mide.
3. Aplique al libro de códigos los cambios de la sección 5 y anótelos en el registro de frontera con origen "matriz de acuerdo".
4. Entregue la matriz con el anexo de prompts y salidas literales.

## Qué se evalúa

El orden del procedimiento (a ciegas, libro fijo, misma instrucción), el cálculo con su interpretación, y sobre todo el análisis de desacuerdos: que cada uno produzca una decisión. Un kappa de 0,45 bien leído vale más que uno de 0,85 reportado como prueba de validez.

## Variante con un tercer codificador

Si dos estudiantes comparten corpus, o si un colega que conoce el campo acepta codificar los treinta fragmentos, la matriz se hace a tres: investigador, modelo y tercero. El cuaderno calcula alfa para cualquier número de codificadores. Los fragmentos en que el modelo coincide con uno de los dos humanos y no con el otro son el mejor material para discutir qué es triangulación y qué no.
