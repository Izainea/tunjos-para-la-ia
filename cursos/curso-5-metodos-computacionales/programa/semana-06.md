# Semana 6. Modelado de temas y lectura distante

## Pregunta de la semana

Si un modelo de temas dice que el corpus habla de veinte cosas y muestra las palabras de cada una, ¿quién decidió que son veinte, y qué es un tema antes de que alguien lo nombre?

## Por qué esta semana

<p class="lede">El modelado de temas es el método computacional que más se parece a leer, y por eso es el que más fácilmente se confunde con leer. Produce listas de palabras que parecen asuntos y proporciones que parecen énfasis, y lo hace sobre miles de documentos que nadie va a leer completos. Moretti llamó lectura distante a ese modo de conocer un corpus por sus formas y no por sus páginas, y Arnold y Tilton lo extendieron a las imágenes. Esta semana presenta el modelo de temas por lo que es, una mezcla de distribuciones ajustada a un número de temas fijado de antemano, y presenta la lectura distante por lo que gana y por lo que pierde. La tesis del curso vuelve con otra cara: los temas son sugerencias, y el nombre que se les da es una abducción de quien los lee.</p>

La semana supone el corpus en una fila por documento y lo aprendido en la semana 3 sobre estabilidad: un tema, como un grupo, es un candidato hasta que sobrevive.

## Contenido de la sesión

1. Un modelo de temas describe cada documento como una mezcla de temas y cada tema como una distribución sobre palabras. En la asignación latente de Dirichlet (Blei, Ng y Jordan, 2003; Blei, 2012) el número de temas K es un dato de entrada, la representación es la bolsa de palabras y el ajuste busca las K distribuciones que mejor explican los conteos. El modelo no sabe qué es un tema: sabe que ciertas palabras tienden a aparecer juntas y agrupa esa tendencia. Lo que sale es, para cada tema, una lista de palabras ordenadas por probabilidad, y para cada documento, una proporción de cada tema<sup class="mark">a</sup>.

<aside class="glosa"><span class="mark">a</span> "Latente" quiere decir que los temas no se observan: se postulan como variables ocultas que explicarían las palabras observadas. "Dirichlet" es la distribución que gobierna cómo se reparten los temas en cada documento y las palabras en cada tema.</aside>

2. Nombrar un tema es una abducción. La lista "arriendo, desalojo, inmobiliaria, familias, cuadra" sugiere un nombre, y el nombre que se elija es una hipótesis sobre por qué esas palabras van juntas. DiMaggio, Nag y Blei (2013) proponen validar un tema de tres formas: que sea interpretable al leer sus palabras, que sea coherente al leer los documentos donde pesa más, y que se comporte como se espera frente a variables externas, por ejemplo el tiempo. Las tres pruebas las hace el investigador; el modelo solo produce las listas.

3. K y la semilla cambian los temas, y la prueba de estabilidad se aplica igual que en la semana 3. Con K igual a diez, "vivienda" es un tema; con K igual a treinta se parte en "arriendo", "desalojo" y "autoconstrucción"; con otra semilla las palabras se redistribuyen. El taller pide dos valores de K y dos semillas, y la tabla de qué temas aparecen en las cuatro corridas con las mismas palabras principales. Los que aparecen son candidatos; los demás se reportan como dependientes del parámetro. Un tema no es un código como los de [*Codificación cualitativa con IA en ciencias sociales*](../../curso-4-codificacion-asistida/README.md), donde el investigador y un modelo de lenguaje asignan códigos leyendo fragmentos y el libro de códigos resultante es una aserción de quien responde por él: el código lo asignó alguien leyendo; el tema lo produjo un ajuste contando. Los dos pueden dialogar, y el diálogo es más fecundo cuando no coinciden.

| Código (libro de códigos) | Tema (modelo de temas) |
|---|---|
| Lo asignó alguien leyendo el fragmento | Lo produjo un ajuste contando palabras |
| Tiene definición, reglas de inclusión y ejemplos | Tiene una lista de palabras ordenadas por probabilidad |
| Un fragmento lo tiene o no lo tiene | Un documento lo tiene en cierta proporción |
| Cambia cuando cambia el libro de códigos | Cambia cuando cambia K o la semilla |
| *Es una lectura con nombre* | *Es una sugerencia sin nombre* |

4. La lectura distante es un programa, no un método. Moretti (2015) propuso en "Conjeturas sobre la literatura mundial" que para conocer la literatura del mundo hay que renunciar a leerla y estudiar en cambio sus formas a gran escala: gráficos de producción, mapas de circulación, árboles de géneros. Lo que se gana es un objeto que la lectura cercana no puede ver, la forma de un sistema; lo que se pierde es el texto. Da (2019) revisó decenas de estudios de literatura computacional y encontró resultados que no sobrevivían a reanalizar los datos. La crítica no invalida el programa: muestra que la lectura distante necesita, más que ninguna otra, la prueba de estabilidad que el curso enseña.

5. La visión distante hace con imágenes lo que la lectura distante con textos, y encuentra un problema propio. Arnold y Tilton (2019) señalan que un texto ya viene codificado en palabras y una imagen no: para contarla hay que anotarla primero, y la anotación, hecha por una red neuronal o por una persona, es una interpretación. Un modelo que etiqueta "multitud", "bandera", "noche" en mil fotografías ya decidió qué hay que ver<sup class="mark">b</sup>. El estudiante que trabaja con imágenes modela temas sobre esas etiquetas o sobre las descripciones densas de [*Descripción auditada de imágenes en investigación social*](../../curso-3-corpus-visual/README.md), producidas allí por un modelo multimodal con un prompt por capas y auditadas sobre una muestra, y declara en el registro que su corpus de entrada es una anotación.

<aside class="glosa"><span class="mark">b</span> Arnold y Tilton usan "distant viewing" en paralelo deliberado con Moretti. Su punto es que el "código" de la imagen, lo que la convierte en dato, no está en la imagen sino en el sistema de anotación, y que ese sistema debe ser explícito.</aside>

6. Los temas se entregan como sugerencias, con sus condiciones. Un informe que dice "el corpus se organiza en doce temas" afirma más de lo que el método sostiene. Uno que dice "con K igual a doce y esta representación, estos siete temas aparecen de forma estable con estas palabras, y los leemos así por estas razones; los otros cinco dependen del parámetro" afirma lo que puede sostener. La diferencia entre las dos frases es la diferencia entre un infortunio y una aserción.

<figure class="wide">
  <svg viewBox="0 0 680 250" style="width:100%;max-width:42rem;height:auto;display:block" role="img" aria-label="A la izquierda, cuatro documentos como barras apiladas de tres temas en proporciones distintas. A la derecha, los tres temas como listas de palabras ordenadas por probabilidad, sin nombre; un rótulo indica que el nombre lo pone quien lee. Debajo, la nota de que K igual a tres fue una decisión.">
    <style>.t6{font-family:var(--text);font-size:12px;fill:var(--ink)} .s6{font-family:var(--text);font-size:11px;fill:var(--muted)} .m6{font-family:var(--mono);font-size:10.5px;letter-spacing:.06em;fill:var(--muted)} .mf6{font-family:var(--mono);font-size:10.5px;letter-spacing:.06em;fill:var(--c-fil)} .bx{fill:var(--surface);stroke:var(--rule);stroke-width:1.2} .A{fill:var(--c-app)} .B{fill:var(--c-doc)} .C{fill:var(--c-blog)}</style>
    <text x="10" y="18" class="m6">DOCUMENTOS COMO MEZCLAS</text>
    <g transform="translate(10 30)">
      <text x="0" y="22" class="s6">doc 1</text><rect x="46" y="10" width="120" height="16" class="A"/><rect x="166" y="10" width="40" height="16" class="B"/><rect x="206" y="10" width="24" height="16" class="C"/>
      <text x="0" y="52" class="s6">doc 2</text><rect x="46" y="40" width="30" height="16" class="A"/><rect x="76" y="40" width="130" height="16" class="B"/><rect x="206" y="40" width="24" height="16" class="C"/>
      <text x="0" y="82" class="s6">doc 3</text><rect x="46" y="70" width="60" height="16" class="A"/><rect x="106" y="70" width="50" height="16" class="B"/><rect x="156" y="70" width="74" height="16" class="C"/>
      <text x="0" y="112" class="s6">doc 4</text><rect x="46" y="100" width="20" height="16" class="A"/><rect x="66" y="100" width="20" height="16" class="B"/><rect x="86" y="100" width="144" height="16" class="C"/>
      <text x="46" y="140" class="s6">0 %</text><text x="214" y="140" class="s6">100 %</text>
    </g>
    <text x="290" y="18" class="m6">TEMAS COMO LISTAS DE PALABRAS</text>
    <rect x="290" y="30" width="120" height="120" rx="3" class="bx"/><rect x="290" y="30" width="120" height="6" class="A"/>
    <text x="298" y="54" class="t6">arriendo</text><text x="298" y="70" class="t6">desalojo</text><text x="298" y="86" class="t6">inmobiliaria</text><text x="298" y="102" class="t6">familias</text><text x="298" y="118" class="s6">cuadra · depósito …</text>
    <rect x="420" y="30" width="120" height="120" rx="3" class="bx"/><rect x="420" y="30" width="120" height="6" class="B"/>
    <text x="428" y="54" class="t6">bus</text><text x="428" y="70" class="t6">estación</text><text x="428" y="86" class="t6">trancón</text><text x="428" y="102" class="t6">pasaje</text><text x="428" y="118" class="s6">ciclorruta · andén …</text>
    <rect x="550" y="30" width="120" height="120" rx="3" class="bx"/><rect x="550" y="30" width="120" height="6" class="C"/>
    <text x="558" y="54" class="t6">fiesta</text><text x="558" y="70" class="t6">parque</text><text x="558" y="86" class="t6">calle</text><text x="558" y="102" class="t6">vecinos</text><text x="558" y="118" class="s6">música · reja …</text>
    <text x="290" y="172" class="mf6">SIN NOMBRE: EL NOMBRE LO PONE QUIEN LEE, Y ES UNA HIPÓTESIS</text>
    <text x="290" y="192" class="s6">¿"fiesta, parque, calle, vecinos, reja" es cultura barrial, conflicto por el espacio, o dos temas que K = 3 obligó a fundir?</text>
    <text x="10" y="232" class="m6">K = 3 FUE UNA DECISIÓN DE ENTRADA · CON K = 5 LA TERCERA LISTA SE PARTE</text>
  </svg>
  <figcaption><b>Figura 6.</b> Documentos como mezclas y temas como listas. El modelo entrega proporciones y palabras; el nombre de cada tema, y la decisión de si la tercera lista es uno o dos asuntos, son del lector.</figcaption>
</figure>

## IA y exigencia

Se le pide a un modelo de lenguaje que proponga un nombre para cada tema a partir de sus veinte palabras principales y de tres documentos representativos, y que escriba el código de las corridas con dos K y dos semillas. El estudiante debe poder defender sin el modelo qué temas sobrevivieron a las cuatro corridas, qué nombre adoptó para cada uno y qué documentos de alto peso contradicen ese nombre, y qué diferencia hay entre esos temas y los códigos que él asignó leyendo, en el libro de códigos de [*Codificación cualitativa con IA en ciencias sociales*](../../curso-4-codificacion-asistida/README.md) si lo tiene. Los nombres propuestos por el modelo son hipótesis del modelo, y el registro dice cuáles se adoptaron y por qué.

## Lecturas

**Central**

- Blei, D. M. (2012). "Probabilistic Topic Models". *Communications of the ACM* 55(4), 77-84. https://doi.org/10.1145/2133806.2133826
- Moretti, F. (2015). *Lectura distante*. Fondo de Cultura Económica. "Conjeturas sobre la literatura mundial". Edición original: *Distant Reading*, Verso, 2013.
- Arnold, T. y Tilton, L. (2019). "Distant Viewing: Analyzing Large Visual Corpora". *Digital Scholarship in the Humanities* 34(Supplement 1), i3-i16. https://doi.org/10.1093/llc/fqz013

**Complementaria**

- Blei, D. M., Ng, A. Y. y Jordan, M. I. (2003). "Latent Dirichlet Allocation". *Journal of Machine Learning Research* 3, 993-1022. https://jmlr.org/papers/v3/blei03a.html
- DiMaggio, P., Nag, M. y Blei, D. (2013). "Exploiting Affinities between Topic Modeling and the Sociological Perspective on Culture". *Poetics* 41(6), 570-606. https://doi.org/10.1016/j.poetic.2013.08.004
- Grimmer, J., Roberts, M. E. y Stewart, B. M. (2022). *Text as Data*. Princeton University Press. Cap. 13, sobre modelos de temas.
- Da, N. Z. (2019). "The Computational Case against Computational Literary Studies". *Critical Inquiry* 45(3), 601-639. https://doi.org/10.1086/702594
- Underwood, T. (2019). *Distant Horizons: Digital Evidence and Literary Change*. University of Chicago Press.

## Guía de lectura

- Blei describe el modelo como una historia generativa: primero se eligen proporciones de temas, luego palabras de cada tema. *¿Qué supone esa historia sobre cómo se escribió un documento de su corpus? ¿Es un supuesto razonable para entrevistas, para noticias, para descripciones de imágenes?*
- Moretti dice que la lectura distante es una condición de conocimiento y que la distancia "no es un obstáculo sino una forma específica de conocimiento". *¿Qué sabe usted de su corpus solo porque no lo ha leído entero? ¿Qué deja de saber?*
- Arnold y Tilton sostienen que las imágenes necesitan un código explícito antes de poder contarse. *Si su corpus es visual, ¿cuál es ese código en su caso, y quién lo escribió? Si es textual, ¿hay alguna anotación previa que esté haciendo el mismo trabajo sin declararse?*
- Da encuentra que muchos resultados de la literatura computacional no sobreviven a cambiar los parámetros. *Lea sus críticas como una lista de pruebas de estabilidad. ¿Cuáles ya hace el curso y cuál le falta?*

## Taller de la segunda hora

Sobre el corpus propio, con el bloque de la semana 6 del cuaderno de apoyo:

1. Ajuste un modelo de temas con dos valores de K, uno bajo y uno alto para el tamaño del corpus, y dos semillas cada uno. Guarde las veinte palabras principales de cada tema y los cinco documentos de mayor peso.
2. Empareje los temas entre las cuatro corridas por las palabras que comparten. Llene la tabla:

| Tema estable (palabras principales) | Aparece en las 4 corridas | Nombre propuesto por mí | Nombre propuesto por el modelo de lenguaje | Documentos de alto peso que contradicen el nombre | Código del libro de códigos más cercano, si lo hay |
|---|---|---|---|---|---|

3. Grafique la proporción de un tema estable a lo largo del tiempo, con la serie de la semana 5. ¿Se comporta como esperaba? Esa es la tercera prueba de DiMaggio, Nag y Blei.
4. Escriba dos frases sobre los temas de su corpus: una que afirme más de lo que el método sostiene y otra que afirme lo que puede sostener. Guarde las dos.

## Guion de la sesión

| Minuto | Momento | Docente | Estudiante | Material |
|---|---|---|---|---|
| 0 a 10 | Apertura | Muestra tres listas de palabras de un tema y pide nombres; anota la variedad | Propone un nombre y lo defiende en una frase | Tablero |
| 10 a 35 | Lectura | Explica la historia generativa de Blei sobre la pizarra; discute Moretti y Arnold y Tilton | Responde la guía | Lecturas centrales |
| 35 a 55 | Mecanismo | Corre el bloque del cuaderno sobre el conjunto de ejercicio con K igual a 3 y a 6 y compara en vivo | Empareja temas entre las dos corridas | Cuaderno, semana 6 |
| 55 a 65 | Pausa | | | |
| 65 a 105 | Taller | Acompaña las cuatro corridas sobre corpus propios | Llena la tabla de temas estables | Cuaderno, semana 6 |
| 105 a 120 | Cierre | Pide las dos frases, la que afirma de más y la que afirma lo que puede | Lee sus dos frases | Bitácora |

Notas para el docente. Lo que suele fallar: el ajuste de temas sobre un corpus pequeño produce listas de palabras sin sentido y el estudiante culpa al método; explicar que el modelo necesita cientos de documentos y que con menos la bolsa de palabras y el agrupamiento de la semana 3 son más honestos. Segundo fallo: los nombres del modelo de lenguaje son tan convincentes que la tabla se llena sin leer documentos; exigir la columna de documentos que contradicen el nombre antes que la del nombre. Tercero: la discusión sobre Moretti se vuelve un debate sobre si "hay que leer"; devolverla a qué sabe el estudiante de su corpus a cada distancia.

## Bitácora

Registre las cuatro corridas, la tabla de temas estables, la serie del tema elegido y las dos frases. Añada una línea sobre qué tema le sorprendió y por qué: ese tema es candidato a hecho sorprendente para la ficha de hipótesis de la semana 8.

## Para la próxima semana

Leer Tufte (2001), capítulos 2 y 4, y Drucker (2011). Reunir en una carpeta todas las vistas producidas hasta ahora: la nube de puntos, los grupos, el grafo con sus tres umbrales, la serie con sus ventanas, los temas. La semana 7 las convierte en un tablero, y para eso cada una necesita saber qué afirma.
