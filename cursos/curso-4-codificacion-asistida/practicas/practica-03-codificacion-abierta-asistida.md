# Práctica 3. Codificación abierta asistida

Duración estimada: 4 horas, de las cuales 1 en la sesión sincrónica de la semana 3; se continúa en la semana 4.
Requisitos: el corpus propio en un archivo de texto plano, un fragmento por párrafo, numerado, sin datos personales de terceros; acceso a un modelo de lenguaje de uso gratuito en su versión web (cualquiera sirve; el curso no exige uno en particular); la plantilla `plantillas/registro-de-frontera-codificacion.md` y la lista de verificación de la semana 2.
No requiere programar. Para quien quiera, el cuaderno `cuaderno-apoyo.md` indica cómo hacer lo mismo por programa y cómo exportar el libro.

## Objetivo

Producir el libro de códigos abierto del corpus propio con un modelo como codificador auxiliar, de modo que cada código tenga origen, anclaje, decisión y criterio, y que el estudiante pueda distinguir lo que habría visto solo de lo que el modelo le mostró.

## Antes de la sesión

1. Numere los fragmentos. Un fragmento es una unidad con sentido propio: una respuesta de entrevista, un párrafo de prensa, una descripción de imagen. Entre veinte y sesenta es el tamaño del curso.
2. Revise que no haya nombres, direcciones ni datos que identifiquen a una persona. Si su material es sensible, trabaje con una muestra anonimizada o con material público; el curso 7 del programa trata estos problemas en detalle.
3. Tenga a mano la lista de verificación de la semana 2, en especial la regla de generación de su tradición. Lo que le va a pedir al modelo es esa regla.

## Ronda 0. Codificar a mano, antes

Codifique los fragmentos 1 a 5 sin el modelo. Para cada uno, haga microanálisis breve (qué sentidos abre cada término que le llame la atención) y proponga uno o dos códigos, con preferencia por códigos in vivo. Guarde esto en un archivo aparte y no lo mire durante la ronda 1. Este paso es el que permite, después, saber qué habría visto usted solo.

## Ronda 1. El modelo propone

Instrucción base para teoría fundamentada; adáptela si su tradición es otra, conservando las tres exigencias: anclaje literal, sin vocabulario de la literatura, alternativas descartables.

```
Voy a darte fragmentos numerados de [tipo de material] sobre [tema, en una
frase]. Para cada fragmento:
1. Haz microanálisis: enumera dos o tres sentidos posibles de los términos
   que más pesan en el fragmento, sin elegir todavía.
2. Propón uno o dos códigos. Usa las palabras del hablante cuando sea posible
   (código in vivo). No uses categorías de la literatura en ciencias sociales
   ni términos abstractos que no estén en el fragmento.
3. Para cada código, cita el fragmento literal que lo sostiene, entre
   comillas, y di qué término del fragmento da origen al nombre.
4. Si un código ya lo usaste en un fragmento anterior, dilo y explica en qué
   se parece el caso nuevo.
Trabaja fragmento por fragmento y numera cada decisión. No agrupes todavía.

Fragmentos:
[1] ...
[2] ...
```

Empiece con los fragmentos 1 a 5. Copie la salida completa a un anexo con fecha.

## Ronda 2. El investigador decide

Compare la salida del modelo con su codificación a mano, fragmento a fragmento, y llene el registro de frontera por código. Preguntas de apoyo:

- ¿El fragmento que el modelo cita está literalmente en el corpus? Verifíquelo con el archivo abierto; el modelo compone citas a veces.
- ¿El nombre sale de un término del fragmento o viene de fuera? Si viene de fuera, ¿la tradición declarada lo permite?
- Si acepto, ¿puedo decir por qué sin repetir lo que dijo el modelo?
- Si corrijo, ¿qué sé yo que el modelo no sabía: del tema, del contexto, de quien habla?
- Si rechazo, ¿es porque está mal o porque no puedo verificarlo? Anote cuál.
- ¿Hay un código que yo puse y el modelo no? Entra al libro con origen "yo".

Para cada código la decisión es una de cuatro: aceptar, corregir, rechazar, reformular como pregunta para un memo. "Dejar pasar" no existe en el registro.

## Ronda 3. Continuar con el corpus

Envíe al modelo los fragmentos siguientes en lotes de diez, con la misma instrucción y, al principio de cada lote, la lista de códigos ya aceptados con sus definiciones, para que el modelo compare contra ella. Observe si el modelo reutiliza los códigos aceptados o vuelve a proponer los que usted rechazó con otro nombre. Registre cada lote igual que el primero.

## Ronda 4. Primer memo

Al terminar, elija el código que más dudas le produjo y escriba un memo con `plantillas/memo-analitico.md`, con la sección de procedencia completa. Si el nombre vino del modelo, ejecute la prueba de anclaje: pídale el término del corpus del que sale y verifíquelo.

```
Para el código "[nombre]", que propusiste en los fragmentos [números], indica
qué término o expresión literal de esos fragmentos da origen al nombre. Si el
nombre no sale de ningún término literal, dilo así, sin inventar una cita.
```

## Después de la sesión

1. Complete el registro para todo el corpus.
2. Llene "los casos difíciles", "aceptaciones sin criterio" e "instrucciones que el modelo ignoró". No omita ninguna aceptación sin criterio: anotarlas es parte de la nota.
3. Llene el balance: qué vio el modelo que usted no, qué vio usted que el modelo no, qué forzó el modelo y con qué señal lo notó.
4. Arme el libro de códigos abierto con `plantillas/libro-de-codigos.md`, sección 2, y entréguelo en la semana 4 con el registro y el memo.

## Qué se evalúa

La precisión del registro, no la elegancia del libro. Un libro con doce códigos in vivo bien anclados, tres rechazos razonados y una aceptación sin criterio anotada vale más que uno con treinta categorías que nadie puso a prueba.

## Variante con material público

Quien no tenga corpus propio listo puede hacer la práctica con los doce fragmentos del simulador de la semana 3 (apps/simulador-codificacion.html), que son inventados y no tienen datos personales, y con textos de dominio público (cartas, crónicas, testimonios publicados antes de 1930). El registro se hace igual.

## Variante para grupos

Dos estudiantes codifican los mismos veinte fragmentos con el mismo modelo y la misma instrucción, y comparan registros. Las filas en que uno aceptó y el otro rechazó son el material de discusión de la sesión, y anticipan la matriz de acuerdo de la semana 6.
