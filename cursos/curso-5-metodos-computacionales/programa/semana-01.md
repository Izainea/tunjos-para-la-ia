# Semana 1. El patrón como vector de frecuencias

## Pregunta de la semana

Cuando un programa dice que dos textos o dos imágenes se parecen, ¿qué está afirmando exactamente, y qué parte del parecido queda fuera de la afirmación?

## Por qué esta semana

<p class="lede">Todo método computacional empieza por una sustitución: el texto o la imagen se reemplazan por un vector, y desde ese momento el método ya no ve el texto sino el vector. Lo que el método encuentre después, un grupo, una red, una tendencia, es una propiedad de los vectores, y solo vale para el corpus en la medida en que la sustitución haya conservado lo que importa. Esta semana mira esa sustitución de frente, con el instrumento más simple que existe, la bolsa de palabras, porque en él se ve con claridad lo que después los embeddings harán de forma más opaca: una representación conserva unas cosas y pierde otras, y una medida de similitud afirma algo muy preciso y nada más. El curso entero es una variación sobre esa frase.</p>

El curso supone que el estudiante tiene un corpus propio, textual o visual, catalogado como se hace en [*Corpus de textos con procedencia en ciencias sociales*](../../curso-2-corpus-textual/README.md) o en [*Descripción auditada de imágenes en investigación social*](../../curso-3-corpus-visual/README.md), o uno equivalente. En esos dos cursos el corpus se define como una decisión documentada y no como una carpeta de archivos: cada documento o imagen lleva su procedencia, sus derechos y el criterio por el que entró, en un catálogo que un cuaderno produce desde las fuentes. Aquí basta con una tabla con una fila por documento, con identificador, fecha y texto, o la ruta de la imagen. Quien no lo tenga trabaja con el conjunto de ejercicio del cuaderno de apoyo hasta conseguirlo.

## Contenido de la sesión

1. Un patrón es una regularidad que un procedimiento puede señalar sin entenderla. La concordancia de un texto bíblico, el índice de un libro y la tabla de frecuencias de un periódico ya eran patrones antes de cualquier computador: alguien contó y ordenó. Lo que cambia con los métodos computacionales no es la naturaleza del patrón sino su escala y su forma de existencia. El patrón vive ahora en un espacio de vectores donde "parecerse" es una distancia, y una distancia es un número que no sabe de qué habla.

2. Representar es decidir qué cuenta como lo mismo. La bolsa de palabras<sup class="mark">a</sup> toma un documento, cuenta cuántas veces aparece cada palabra del vocabulario y olvida el orden. Dos frases con las mismas palabras en distinto orden son, para esa representación, idénticas. La decisión no es un defecto sino una elección: la bolsa de palabras apuesta a que el tema de un documento está en qué palabras usa y no en cómo las encadena, y para muchas preguntas esa apuesta rinde (Grimmer, Roberts y Stewart, 2022, cap. 5). Para otras preguntas, las de la ironía, la negación o el argumento, rinde poco. Lo mismo ocurre con una imagen reducida a su histograma de colores: conserva la paleta y pierde la composición.

<aside class="glosa"><span class="mark">a</span> Bolsa de palabras: representación de un documento como vector de conteos sobre un vocabulario fijo. Si el vocabulario tiene diez mil palabras, cada documento es un punto en un espacio de diez mil dimensiones, casi todas en cero.</aside>

3. Una medida de similitud es una afirmación dentro de una representación. El coseno<sup class="mark">b</sup> entre dos vectores de conteo dice cuánto se parecen las proporciones de palabras de dos documentos, sin importar su longitud; la distancia euclidiana dice algo distinto, sensible a la longitud. Ninguna de las dos es "la" similitud. Cuando un informe dice que dos documentos son "muy similares" está diciendo que cierta función, aplicada a cierta representación, dio un número alto. El investigador que firma el informe tiene que poder desplegar esa frase completa.

<aside class="glosa"><span class="mark">b</span> Coseno: el producto punto de dos vectores dividido por el producto de sus longitudes. Vale 1 cuando apuntan en la misma dirección, 0 cuando no comparten ninguna componente. Es la medida más usada con texto porque ignora la longitud del documento.</aside>

4. Lo que se pierde al representar no desaparece del corpus; desaparece del método. El orden de las palabras, la negación, los sinónimos, el sentido de una palabra en su contexto, la referencia a un hecho local: todo eso sigue en el texto y lo lee quien lo lee. La mini app de la semana lo muestra con pares preparados: "la junta presionó a la alcaldía" y "la alcaldía presionó a la junta" tienen coseno 1; "el subsidio alcanza" y "el subsidio no alcanza" tienen coseno cercano a 1; "el arriendo subió" y "la renta se duplicó" tienen coseno 0. Los embeddings de la semana 2 corrigen parte de esto, y tienen a su vez su propio "nada más".

5. El patrón es el output de un instrumento, y la lectura es un acto de quien lo usa. Un telescopio no comprende las estrellas y nadie le reprocha eso: su valor depende de los protocolos que gobiernan su uso. La similitud por coseno es un instrumento del mismo tipo, con una diferencia que [*Validación del razonamiento con IA en ciencias sociales*](../../curso-1-tres-inferencias/README.md), el curso de fundamentos del programa, ya marcó al separar lo que verifica la máquina de lo que responde el investigador: su salida tiene forma de afirmación ("estos dos se parecen") y por eso tienta a tomarla como un juicio. Allí se distinguieron tres inferencias por su régimen de validez: la deducción vale por su forma, la inducción por sus tasas de acierto a largo plazo, y la abducción, que introduce hipótesis nuevas, porque alguien se compromete a responder por ella. En esos términos, calcular la distancia es una operación que cualquiera puede verificar; agrupar por distancia es una inducción sobre el corpus; decir que el grupo es una categoría es una abducción que alguien debe sostener. Esta semana se queda en la primera.

6. La pregunta del curso se deja planteada y no se responde. Cuando un método encuentra un patrón, ¿es una hipótesis o un artefacto? El criterio provisional, que las semanas siguientes refinan, es doble: un patrón que desaparece al cambiar la representación o al mover el parámetro es, hasta prueba en contrario, del método; un patrón que sobrevive merece una lectura, y la lectura exige un trasfondo desde el cual el patrón sorprenda. Grimmer, Roberts y Stewart (2022) abren su libro con un principio que el curso adopta como propio: los métodos de texto como dato no reemplazan la lectura sino que la amplifican, y la validación de cualquier resultado depende de la tarea para la que se obtuvo.

| Lo que afirma la medida | Lo que afirma quien la lee |
|---|---|
| "El coseno entre A y B es 0,40" | "A y B tratan del mismo problema" |
| Vale dentro de una representación y de una función declaradas | Vale si alguien conoce A y B y responde por la frase |
| Cualquiera la reproduce con el mismo código | Nadie la reproduce; se discute |
| No cambia si A y B cambian de sentido sin cambiar de palabras | Cambia con el sentido, aunque las palabras sigan |
| *Es un dato del instrumento* | *Es una hipótesis del investigador* |

<figure class="wide">
  <svg viewBox="0 0 680 210" style="width:100%;max-width:42rem;height:auto;display:block" role="img" aria-label="Del texto al vector en tres pasos: el texto 'el arriendo subió el doble' se convierte en una lista de tokens sin orden, luego en un vector de conteos sobre un vocabulario, y por último en un punto en un espacio donde la distancia a otro documento es un número. Debajo, lo que se pierde en cada paso: orden, negación, sinónimos.">
    <style>.t1{font-family:var(--text);font-size:13px;fill:var(--ink)} .m1{font-family:var(--mono);font-size:10.5px;letter-spacing:.06em;fill:var(--muted)} .m2{font-family:var(--mono);font-size:10.5px;fill:var(--c-fil)} .bx{fill:var(--surface);stroke:var(--rule);stroke-width:1.2} .ar{stroke:var(--muted);stroke-width:1.3;fill:none} .ah{fill:var(--muted)}</style>
    <defs><marker id="s1-ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 1L9 5L0 9z" class="ah"/></marker></defs>
    <rect x="8" y="30" width="190" height="78" rx="3" class="bx"/>
    <text x="18" y="48" class="m1">TEXTO</text>
    <text x="18" y="72" class="t1">«El arriendo subió</text><text x="18" y="90" class="t1">el doble en tres años»</text>
    <path class="ar" d="M198 69 L236 69" marker-end="url(#s1-ah)"/>
    <rect x="240" y="30" width="190" height="78" rx="3" class="bx"/>
    <text x="250" y="48" class="m1">BOLSA DE PALABRAS</text>
    <text x="250" y="72" class="t1">arriendo 1 · subió 1</text><text x="250" y="90" class="t1">doble 1 · tres 1 · años 1</text>
    <path class="ar" d="M430 69 L468 69" marker-end="url(#s1-ah)"/>
    <rect x="472" y="30" width="200" height="78" rx="3" class="bx"/>
    <text x="482" y="48" class="m1">VECTOR Y DISTANCIA</text>
    <text x="482" y="72" class="t1">(0, 1, 0, 1, 1, 0, 1, 1, 0 …)</text>
    <text x="482" y="90" class="t1">cos(A, B) = 0,40</text>
    <text x="103" y="140" text-anchor="middle" class="m2">se pierde: nada aún</text>
    <text x="335" y="140" text-anchor="middle" class="m2">se pierde: orden, negación</text>
    <text x="572" y="140" text-anchor="middle" class="m2">se pierde: sinónimos, contexto</text>
    <path class="ar" d="M20 165 L660 165" />
    <text x="20" y="190" class="m1">LO QUE EL MÉTODO VE A PARTIR DE AQUÍ ES EL VECTOR, NO EL TEXTO</text>
  </svg>
  <figcaption><b>Figura 1.</b> Del texto al vector. Cada paso conserva algo y pierde algo; lo que se pierde sigue en el texto, pero ya no está disponible para el método.</figcaption>
</figure>

<iframe class="app" src="apps/distancia-coseno.html" title="Distancia y similitud entre dos frases con bolsa de palabras y coseno" loading="lazy"></iframe>

## IA y exigencia

Esta semana se le pide a un modelo de lenguaje que explique, con sus palabras, por qué dos fragmentos del corpus propio se parecen o no, y que proponga una medida alternativa al coseno. El estudiante debe poder defender sin el modelo tres cosas: qué representación se usó, qué afirma exactamente el número obtenido y qué del parecido real entre los fragmentos quedó fuera de la medida. Si el modelo propone una medida, el estudiante la aplica en la app o en el cuaderno y comprueba si el número cambia lo que él diría.

## Lecturas

**Central**

- Grimmer, J., Roberts, M. E. y Stewart, B. M. (2022). *Text as Data: A New Framework for Machine Learning and the Social Sciences*. Princeton University Press. Caps. 1 a 3 (principios) y 5 (bolsa de palabras).

**Complementaria**

- Grimmer, J., Roberts, M. E. y Stewart, B. M. (2022). *Text as Data*. Cap. 7, sobre el modelo de espacio vectorial y las medidas de similitud.
- Harris, Z. S. (1954). "Distributional Structure". *Word* 10(2-3), 146-162. https://doi.org/10.1080/00437956.1954.11659520
- Moretti, F. (2015). *Lectura distante*. Fondo de Cultura Económica. "Conjeturas sobre la literatura mundial", como anticipo de la semana 6.

## Guía de lectura

- Grimmer, Roberts y Stewart enumeran al comienzo del libro los principios de su enfoque, entre ellos que el texto como dato amplifica al lector en vez de reemplazarlo y que la validación depende de la tarea. *¿Cuál de esos principios le parece más difícil de cumplir en su propio proyecto, y por qué?*
- En el capítulo sobre bolsa de palabras, los autores defienden una representación que descarta el orden. *¿Qué pregunta de su investigación sobrevive a esa pérdida y cuál no?*
- Harris formula en 1954 la hipótesis distribucional: el significado de una palabra se refleja en los contextos en que aparece. Esa hipótesis sostiene los embeddings de la semana 2. *¿Qué tendría que ser cierto del corpus para que la hipótesis funcione en él?*
- La similitud por coseno se presenta en el capítulo 7 como una medida entre muchas. *Si tuviera que explicarle a un colega qué afirma un coseno de 0,40 entre dos entrevistas, ¿qué frase usaría y qué frase evitaría?*

## Taller de la segunda hora

Cada estudiante trae diez fragmentos de su corpus (párrafos, descripciones de imágenes, titulares) en un archivo de texto. Con la mini app, o con el bloque de la semana 1 del cuaderno de apoyo:

1. Elija cinco pares de fragmentos: dos que considere parecidos, dos que considere distintos y uno del que no esté seguro. Anote su juicio antes de calcular.
2. Calcule el coseno de cada par con palabras vacías y sin ellas. Anote si el número cambia lo que usted diría.
3. Para cada par, liste las palabras que lo acercan y lo que del parecido, o de la diferencia, no está en esa lista.

Luego llene la ficha:

| Par | Coseno | Palabras que los acercan | Qué los hace parecidos para mí | Qué de ese parecido no está en la medida | ¿La medida acertó? |
|---|---|---|---|---|---|

Se buscan dos casos obligatorios: un par con coseno alto que el estudiante no considera parecido, y un par con coseno bajo que sí lo considera. Esos dos casos son la primera entrada del registro de frontera computacional.

## Guion de la sesión

| Minuto | Momento | Docente | Estudiante | Material |
|---|---|---|---|---|
| 0 a 10 | Apertura | Plantea la pregunta del curso con un ejemplo: dos informes que llegaron a conclusiones opuestas sobre el mismo corpus | Escribe en una línea qué espera encontrar en su corpus | Tablero |
| 10 a 35 | Lectura | Discute los principios de Grimmer, Roberts y Stewart sobre casos del grupo | Responde la guía de lectura en voz alta | Lectura central |
| 35 a 55 | Mecanismo | Corre la mini app con los pares preparados; muestra qué pierde la bolsa de palabras | Predice el coseno antes de verlo | App de distancia |
| 55 a 65 | Pausa | | | |
| 65 a 105 | Taller | Acompaña el cálculo sobre fragmentos propios | Llena la ficha de pares | App o cuaderno, semana 1 |
| 105 a 120 | Cierre | Recoge los pares donde la medida y el juicio no coinciden | Nombra uno de sus dos casos obligatorios | Bitácora |

Notas para el docente. Lo que suele fallar: el estudiante toma el coseno como veredicto y, si es alto, deja de leer los fragmentos; obligar a que llene la columna "qué de ese parecido no está en la medida" antes que las otras. Segundo fallo: fragmentos demasiado largos hacen que todo tenga coseno medio y nada se vea; pedir fragmentos de dos o tres frases. Tercero: quien no programa se desanima en el primer bloque del cuaderno; recordar que las apps bastan para la semana y que el cuaderno se copia sin modificar.

## Bitácora

Registre los diez fragmentos, la tabla de pares y los dos casos obligatorios. Añada una línea sobre qué representación de su corpus le parece más adecuada para su pregunta y por qué. Esta bitácora es la primera página del registro de frontera computacional.

## Para la próxima semana

Leer Mikolov et al. (2013), secciones 1 a 3, y Reimers y Gurevych (2019), secciones 1 a 3. Instalar el entorno del cuaderno de apoyo siguiendo la sección "Preparación" y comprobar que el bloque de prueba corre. Traer el corpus completo en un archivo por documento o en una tabla con una fila por documento.
