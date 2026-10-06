# Semana 7. Visualización que no engaña

## Pregunta de la semana

Una gráfica muestra el mismo dato de dos maneras y una de ellas convence más. ¿Qué afirmó la gráfica que el dato no afirma, y cómo se construye una vista que declare lo que afirma?

## Por qué esta semana

<p class="lede">Hasta aquí el curso ha producido patrones y los ha sometido a prueba. Falta el momento en que los patrones se muestran a otros, y ese momento tiene sus propios instrumentos y sus propios artefactos. Una escala recortada convierte un crecimiento modesto en un salto; una suma acumulada borra los años que bajaron; un color rojo señala una alerta que nadie midió; dos ejes ajustados hacen coincidir lo que no coincide. Nada de eso es mentir con los datos: es afirmar con la vista algo que el dato no sostiene, y en el vocabulario de [*Las tres inferencias*](../../curso-1-tres-inferencias/README.md), donde se propuso llamar infortunio y no alucinación al error característico del modelo, es exactamente eso: un acto con la forma de un hallazgo sin sus condiciones. Esta semana enseña a construir vistas que declaren lo que afirman y a reunirlas en un tablero para investigar, que es lo contrario de un tablero para vender.</p>

La semana supone las vistas producidas en las semanas 2 a 6, reunidas en una carpeta, y las plantillas de ficha de patrón y de lectura de grafo ya usadas.

## Contenido de la sesión

1. Toda vista afirma algo, y la integridad gráfica consiste en que afirme lo que el dato sostiene. Tufte (2001, cap. 2) propone medir la distorsión con un factor de mentira<sup class="mark">a</sup>, la razón entre el efecto que la gráfica muestra y el efecto que hay en el dato, y da ejemplos de prensa donde ese factor pasa de diez. La regla que el curso adopta es más simple que cualquier factor: debajo de cada vista va una frase que dice qué afirma, y la frase debe poder sostenerse con el dato y con los parámetros declarados.

<aside class="glosa"><span class="mark">a</span> Factor de mentira: tamaño del efecto en la gráfica dividido por tamaño del efecto en los datos. Una barra que crece un 300 % para representar un dato que creció un 35 % tiene un factor cercano a 9. Tufte propone que una gráfica honesta se mantenga entre 0,95 y 1,05.</aside>

2. La escala es la primera decisión y la que más se esconde. Un eje de barras que no empieza en cero exagera las diferencias; un eje logarítmico comprime los grandes y expande los pequeños, útil para órdenes de magnitud y engañoso si no se declara; dos ejes verticales en la misma gráfica permiten hacer coincidir cualquier par de series. La mini app muestra las cuatro trampas con la misma cifra y, al lado, la misma cifra con la decisión declarada. El punto no es que la vista honesta sea aburrida: es que afirma lo que puede.

3. El color afirma orden, agrupación o alerta, y cada una de esas afirmaciones debe venir del dato. Una escala secuencial, de claro a oscuro, dice "esto va de menos a más"; una divergente dice "hay un centro y dos extremos"; una categórica dice "estas cosas son de distinta clase". Pintar de rojo los tres últimos años de una serie dice "aquí hay una alerta", y si nadie midió la alerta, la vista la inventó. Healy (2018) y Munzner (2014) dan reglas para elegir la escala según el tipo de variable<sup class="mark">b</sup>; el curso añade que la elección se declara al pie.

<aside class="glosa"><span class="mark">b</span> Regla mínima: variable ordenada, escala secuencial; variable con un centro significativo, escala divergente; variable nominal, colores categóricos y no más de siete. Y en todos los casos, que la diferencia se vea también sin color, porque una parte de los lectores no distingue el rojo del verde.</aside>

4. Las proyecciones y los dibujos de grafos afirman más de lo que parece, y eso ya lo sabe el estudiante. La nube de puntos de la semana 2 afirma vecindades locales y no distancias; el dibujo por fuerzas de la semana 4 afirma conexión y no posición; la serie suavizada de la semana 5 afirma lo que la ventana deja ver. En el tablero, cada una de esas vistas lleva su proyección, su semilla, su umbral o su ventana escritos en el pie, y lleva, cuando lo hay, el resultado de la prueba de estabilidad: "los grupos marcados sobreviven a cinco semillas y a k más y menos uno".

5. Un tablero para investigar es distinto de un tablero para vender, y Drucker (2011) dice por qué. Las convenciones gráficas de las ciencias naturales presentan el dato como algo dado, *data*, cuando en humanidades el dato es algo tomado, *capta*, construido por una interpretación que la gráfica debería mostrar y no borrar. Un tablero para vender muestra cifras limpias y tendencias claras y esconde los parámetros; uno para investigar muestra la cifra con su incertidumbre, la tendencia con su ventana, el grupo con su estabilidad, y deja al lector la posibilidad de no estar de acuerdo. El producto final del curso es un tablero del segundo tipo.

| Tablero para vender | Tablero para investigar |
|---|---|
| Cifras limpias, tendencias claras | Cifras con su incertidumbre, tendencias con su ventana |
| Los parámetros no se ven | Los parámetros están al pie de cada panel |
| El título es la conclusión | El título es la pregunta; la conclusión va aparte y firmada |
| El lector debe convencerse | El lector puede no estar de acuerdo, y sabe con qué |
| *Afirma lo que conviene* | *Afirma lo que puede* |

6. La anatomía de una vista honesta es la misma para todas las vistas del curso. Arriba, la pregunta a la que la vista responde. En el centro, el dato con la escala declarada. Al pie, los parámetros, el resultado de la prueba de estabilidad, la frase de lo que afirma y, separada con claridad, la lectura del investigador. Esa separación entre lo que afirma la vista y lo que propone quien la lee es la frontera que [*Las tres inferencias*](../../curso-1-tres-inferencias/README.md) traza entre lo que verifica la máquina y lo que responde el investigador, dibujada en cada panel del tablero. Una vista que mezcla las dos cosas, por ejemplo un título que ya es una conclusión, ha cruzado la frontera sin decirlo.

<figure class="wide">
  <svg viewBox="0 0 680 280" style="width:100%;max-width:42rem;height:auto;display:block" role="img" aria-label="Anatomía de un panel honesto: un rectángulo con cinco zonas rotuladas. Arriba, la pregunta. En el centro, la vista con su escala. Debajo, tres franjas: parámetros y prueba de estabilidad, lo que la vista afirma, y, separada por una línea punteada roja, la lectura del investigador.">
    <style>.t7{font-family:var(--text);font-size:12.5px;fill:var(--ink)} .s7{font-family:var(--text);font-size:11px;fill:var(--muted)} .m7{font-family:var(--mono);font-size:10.5px;letter-spacing:.06em;fill:var(--muted)} .mf7{font-family:var(--mono);font-size:10.5px;letter-spacing:.06em;fill:var(--c-fil)} .bx{fill:var(--surface);stroke:var(--rule);stroke-width:1.2} .bar{fill:var(--c-app)} .fr{stroke:var(--c-fil);stroke-width:1.6;stroke-dasharray:6 5;fill:none} .ax{stroke:var(--muted);stroke-width:1}</style>
    <rect x="10" y="10" width="660" height="260" rx="3" class="bx"/>
    <text x="22" y="30" class="m7">PREGUNTA</text>
    <text x="110" y="30" class="t7">¿Crece la proporción de documentos que hablan de desalojo entre 2019 y 2024?</text>
    <g transform="translate(22 44)">
      <line x1="30" y1="90" x2="300" y2="90" class="ax"/><line x1="30" y1="10" x2="30" y2="90" class="ax"/>
      <text x="6" y="94" class="s7">0</text><text x="0" y="16" class="s7">20 %</text>
      <rect x="45" y="62" width="30" height="28" class="bar"/><rect x="85" y="58" width="30" height="32" class="bar"/><rect x="125" y="60" width="30" height="30" class="bar"/><rect x="165" y="50" width="30" height="40" class="bar"/><rect x="205" y="46" width="30" height="44" class="bar"/><rect x="245" y="42" width="30" height="48" class="bar"/>
      <text x="48" y="106" class="s7">2019</text><text x="248" y="106" class="s7">2024</text>
      <text x="330" y="30" class="s7">eje desde cero · proporción, no conteo</text>
      <text x="330" y="48" class="s7">n por año debajo: 212, 240, 251, 298, 310, 322</text>
      <text x="330" y="66" class="s7">un color porque es una variable</text>
    </g>
    <text x="22" y="178" class="m7">PARÁMETROS Y ESTABILIDAD</text>
    <text x="230" y="178" class="s7">código "desalojo" del libro de códigos v3 · agregación anual · sin suavizado · la tendencia se mantiene con agregación trimestral</text>
    <text x="22" y="204" class="m7">LO QUE LA VISTA AFIRMA</text>
    <text x="230" y="204" class="t7">La proporción pasa de 7 % a 14 % en seis años, con un retroceso en 2021.</text>
    <path class="fr" d="M22 220 L658 220"/>
    <text x="22" y="246" class="mf7">LECTURA DEL INVESTIGADOR</text>
    <text x="230" y="246" class="t7">Propongo que el aumento sigue a la llegada de las torres nuevas; la prueba</text>
    <text x="230" y="262" class="t7">sería cruzar con fechas de licencias. Quien responde por esta frase soy yo.</text>
  </svg>
  <figcaption><b>Figura 7.</b> Anatomía de un panel honesto. Pregunta, vista con escala declarada, parámetros y estabilidad, lo que la vista afirma y, del otro lado de la línea, lo que el investigador propone. La línea es la frontera.</figcaption>
</figure>

<iframe class="app" src="apps/vista-que-engana.html" title="La misma cifra en una vista que exagera y en una que declara lo que afirma" loading="lazy"></iframe>

## IA y exigencia

Se le pide a un modelo de lenguaje el código del tablero, en Plotly o en la biblioteca que el estudiante prefiera, a partir de los bloques del cuaderno, y después se le pide que escriba el pie de cada panel. El estudiante debe poder defender sin el modelo cada decisión de escala y color de cada panel, la frase de lo que afirma cada vista, y la separación entre esa frase y su lectura. Los pies que escriba el modelo se revisan uno por uno: cualquier frase del pie que afirme más de lo que el panel sostiene se corrige y se anota en el registro de frontera como propuesta del modelo rechazada.

## Lecturas

**Central**

- Tufte, E. R. (2001). *The Visual Display of Quantitative Information*. 2.ª ed. Graphics Press. Cap. 2, "Graphical Integrity", y cap. 4, "Data-Ink and Graphical Redesign". Edición original de 1983.
- Drucker, J. (2011). "Humanities Approaches to Graphical Display". *Digital Humanities Quarterly* 5(1). http://www.digitalhumanities.org/dhq/vol/5/1/000091/000091.html

**Complementaria**

- Healy, K. (2018). *Data Visualization: A Practical Introduction*. Princeton University Press. Versión abierta: https://socviz.co/
- Munzner, T. (2014). *Visualization Analysis and Design*. CRC Press. Caps. 5 y 10, sobre marcas, canales y color.
- Cairo, A. (2019). *How Charts Lie: Getting Smarter about Visual Information*. W. W. Norton.
- Wattenberg, M., Viégas, F. y Johnson, I. (2016). "How to Use t-SNE Effectively". *Distill*. https://distill.pub/2016/misread-tsne/

## Guía de lectura

- Tufte propone que la representación de los números sea directamente proporcional a los números. *Tome una gráfica de su carpeta y calcule su factor de mentira. Si es mayor que 1,05, ¿qué decisión lo produjo?*
- Tufte también propone quitar toda tinta que no sea dato. *¿Qué hay en sus gráficas que no es dato? ¿Y hay algo que no es dato pero debería estar, como los parámetros?*
- Drucker distingue *data* de *capta*. *Elija una vista de su tablero y escriba en una frase cómo fue tomado el dato que muestra. ¿Cabría esa frase en el pie?*
- Healy insiste en que la gráfica que se ve bien no es la que mejor muestra el dato. *¿Cuál de sus vistas le gusta más? ¿Es la que mejor afirma lo que puede?*

## Taller de la segunda hora

Sobre las vistas del corpus propio, con el bloque de la semana 7 del cuaderno de apoyo:

1. Elija cinco vistas de la carpeta: una nube de puntos con grupos, el grafo, la serie, los temas y una libre.
2. Para cada una, llene el panel de la figura 7:

| Vista | Pregunta | Escala y color declarados | Parámetros y estabilidad | Lo que la vista afirma | Mi lectura (separada) |
|---|---|---|---|---|---|

3. Construya una versión que empuja de una de ellas, con una de las cuatro trampas de la mini app, y póngala al lado de la honesta. Esa pareja va al tablero como advertencia al lector.
4. Monte el tablero con los cinco paneles. Puede ser un archivo HTML con Plotly, un cuaderno exportado o un documento con las cinco figuras y sus pies. Lo que importa es que cada panel tenga las seis casillas.

## Guion de la sesión

| Minuto | Momento | Docente | Estudiante | Material |
|---|---|---|---|---|
| 0 a 10 | Apertura | Proyecta una gráfica de prensa con eje recortado y pregunta qué afirma | Escribe en una línea lo que la gráfica le hizo creer | Tablero |
| 10 a 30 | Lectura | Discute integridad gráfica y *capta*; calcula un factor de mentira en vivo | Responde la guía con una vista propia | Lecturas centrales |
| 30 a 50 | Mecanismo | Recorre las cuatro trampas de la mini app y lee en voz alta lo que cada vista afirma | Identifica cuál de las trampas ha usado alguna vez | App de vistas |
| 50 a 60 | Pausa | | | |
| 60 a 100 | Taller | Acompaña el llenado de los paneles y el montaje del tablero | Llena la tabla de cinco vistas | Cuaderno, semana 7 |
| 100 a 115 | Revisión cruzada | Organiza parejas: cada uno busca en el tablero del otro una frase que cruza la frontera | Corrige un pie | Tableros |
| 115 a 120 | Cierre | Recuerda qué se entrega la semana 8 | Anota qué le falta | Bitácora |

Notas para el docente. Lo que suele fallar: el estudiante quiere que el tablero "se vea bien" y la discusión se va a colores y tipografías; devolverla a las seis casillas. Segundo fallo: la frase de lo que afirma la vista y la lectura se funden en una sola, en general con un título que ya es conclusión; exigir la línea punteada entre las dos. Tercero: la versión que empuja sale demasiado convincente y alguien propone usarla; esa propuesta es el mejor momento de la sesión para hablar de a quién le sirve el tablero.

## Bitácora

Registre la tabla de cinco vistas, el tablero montado y la pareja que empuja y declara. Añada una línea sobre qué decisión de escala o color le costó más declarar y por qué. Esta bitácora es la base del producto final.

## Para la próxima semana

Leer Peirce (1903) y releer Timmermans y Tavory (2012). Elegir un patrón del tablero que lo haya sorprendido, y leer las plantillas `plantillas/ficha-de-patron.md` y `plantillas/registro-de-frontera-computacional.md`. Preparar una presentación de ocho minutos: el tablero, el patrón, la hipótesis y la frontera.
