# Semana 6. Acuerdo no es validez

## Pregunta de la semana

Si el investigador y el modelo ponen el mismo código en el 85 % de los fragmentos, ¿qué se ha demostrado, y qué se aprende del 15 % restante?

## Por qué esta semana

<p class="lede">La forma dominante de evaluar la codificación con modelos es medir cuánto coinciden con codificadores humanos. Un acuerdo alto se presenta como prueba de que el modelo "codifica bien", y a veces como licencia para delegarle el resto del corpus. Esta semana desmonta esa inferencia sin desechar la medida. El acuerdo entre codificadores mide consistencia: que dos aplicaciones del mismo libro de códigos dan lo mismo. No mide validez: que el código esté bien puesto. Dos codificadores pueden coincidir en un error, y pueden discrepar porque uno vio algo que el libro de códigos aún no sabe nombrar. McDonald, Schoenebeck y Forte (2019) lo argumentan para la investigación cualitativa en general; el curso lo lleva al caso en que uno de los dos codificadores es un modelo.</p>

La semana enseña a calcular las dos medidas de uso común, kappa de Cohen y alfa de Krippendorff, a interpretarlas como lo que son, y sobre todo a leer los desacuerdos uno a uno como datos sobre el libro de códigos. El segundo producto, la matriz de acuerdo con análisis de desacuerdos, se entrega hoy.

## Contenido de la sesión

1. La fiabilidad entre codificadores nació en el análisis de contenido para responder a una pregunta precisa: si las instrucciones de codificación son lo bastante claras para que personas distintas las apliquen igual. Krippendorff (2004) distingue estabilidad, reproducibilidad y exactitud, y sostiene que la reproducibilidad es la que importa: codificadores que trabajan por separado, con las mismas instrucciones, sobre las mismas unidades. Si no coinciden, las instrucciones son ambiguas o las categorías se solapan. El remedio es corregir el libro de códigos, no a los codificadores. Esa lectura, en la que el desacuerdo es información sobre el instrumento, es la que el curso adopta.

2. Las medidas corrigen el acuerdo observado por el acuerdo esperado por azar. El porcentaje de acuerdo simple engaña cuando una categoría domina: dos codificadores que pusieran "otro" en todo coincidirían siempre. Kappa de Cohen (1960) calcula el acuerdo esperado a partir de las distribuciones marginales de cada codificador y lo descuenta: kappa igual a cero significa acuerdo al nivel del azar, uno significa acuerdo perfecto.<sup class="mark">a</sup> Alfa de Krippendorff generaliza la idea a cualquier número de codificadores, a datos faltantes y a escalas no nominales, y por eso Hayes y Krippendorff (2007) lo proponen como medida estándar. Para dos codificadores y datos nominales completos, los dos valores suelen ser cercanos. El cuaderno de apoyo calcula ambos.

<aside class="glosa"><span class="mark">a</span> Los umbrales que circulan (0,80 como fiable, 0,67 como provisional) vienen de Krippendorff, que los propone para alfa y advierte que dependen del uso que se dará a los datos. No hay un umbral que convierta un acuerdo en validez: el umbral dice cuándo la consistencia es suficiente para seguir, no cuándo los códigos están bien puestos.</aside>

3. McDonald, Schoenebeck y Forte (2019) revisaron cómo la comunidad de interacción humano-computador usa estas medidas y encontraron que a menudo se reportan como si fueran una prueba de calidad del análisis. Su argumento es que la fiabilidad entre codificadores es apropiada cuando el libro de códigos está fijo y los codificadores lo aplican, e inapropiada o irrelevante cuando los códigos se construyen durante el análisis, como en la teoría fundamentada o en el análisis temático reflexivo. En el segundo caso, el desacuerdo no es un defecto que haya que reducir sino el lugar donde el análisis avanza. Braun y Clarke (2019) dicen lo mismo desde su tradición: la fiabilidad presupone que hay una codificación correcta esperando en los datos, y el análisis reflexivo no lo presupone.

4. Cuando uno de los codificadores es un modelo, el argumento cambia de dos maneras. La primera es que el acuerdo con el modelo tiene un valor instrumental real: si el investigador y el modelo coinciden en el 90 % de los fragmentos con un libro de códigos fijo, el modelo puede aplicar ese libro al resto del corpus bajo verificación por muestreo, y eso es lo que hace posible codificar corpus grandes. Es un uso legítimo del acuerdo como consistencia. La segunda es que el acuerdo con el modelo puede ser alto por una razón que no tiene nada que ver con el corpus: el investigador y el modelo comparten la literatura, y coinciden en poner "barreras de acceso" donde el fragmento habla de esperar cinco horas. Gilardi, Alizadeh y Kubli (2023) encontraron que un modelo superaba a anotadores humanos en varias tareas de clasificación; ese resultado mide consistencia con un estándar, y lo que el estándar valía es otra pregunta.<sup class="mark">b</sup>

<aside class="glosa"><span class="mark">b</span> La justificación metodológica de la tesis doctoral del docente (Zainea, 2026) dice que cuando las categorías emergen del propio modelo no hay contra qué medir el acuerdo, porque el modelo es a la vez instrumento y estándar. Por eso la matriz de esta semana se hace con el libro de códigos del estudiante, fijado en la semana 4, y no con códigos que el modelo proponga sobre la marcha.</aside>

5. Los desacuerdos, leídos uno a uno, se reparten en unos pocos tipos que la matriz de la semana obliga a clasificar. El fragmento es ambiguo y el libro no dice qué hacer: hace falta una regla de decisión. La definición de un código es estrecha y el fragmento muestra un caso que debería incluir: hace falta ampliarla. Dos códigos se solapan: hace falta fusionarlos o distinguirlos con un criterio. El modelo aplicó la palabra y no el sentido: hace falta un ejemplo negativo en la definición. El modelo forzó una categoría de fuera: hace falta anotarlo como señal de la semana 4. El investigador se equivocó: ocurre, y el registro lo muestra. Cada tipo produce una decisión sobre el libro de códigos, y esa es la razón por la que el análisis de desacuerdos vale más que la cifra.

6. El acuerdo entre el investigador y el modelo no es triangulación en el sentido de Denzin (1970), y conviene decirlo en la sesión. La triangulación entre investigadores exige observadores independientes con trasfondos propios. El modelo tiene un trasfondo, su entrenamiento, que se solapa de manera desconocida con el del investigador. Lo que sí es triangulación es contrastar la codificación del investigador y del modelo con la de un tercero que conozca el campo, o contrastar dos familias de modelos entre sí y con el investigador. El curso no exige esa triangulación completa, pero exige que la matriz diga qué es y qué no es.

La distinción puede resumirse en una tabla de contraste que conviene tener a la vista durante la práctica.

| Acuerdo entre codificadores | Validez del código |
|---|---|
| Mide si dos aplicaciones del libro dan lo mismo | Mide si el código recoge lo que el fragmento sostiene |
| Se calcula sobre el registro: kappa, alfa | Se juzga con el criterio de la tradición declarada |
| Alto cuando el libro es claro o cuando ambos comparten el mismo sesgo | No depende de cuántos coincidan |
| Un desacuerdo lo baja | Un desacuerdo puede ser el dato que la mejora |
| *Una máquina lo verifica.* | *Alguien responde por ella.* |

7. Queda la frase que la semana quiere dejar fija. Un acuerdo alto dice que el libro de códigos se puede aplicar con consistencia, incluida la consistencia de una máquina; no dice que los códigos estén bien puestos, y menos aún que el libro diga algo verdadero sobre el corpus. Un acuerdo bajo dice que el libro tiene problemas o que el material resiste al libro, y las dos cosas se averiguan leyendo los desacuerdos. En los términos del programa: el acuerdo es un criterio de registro, verificable con el rastro; la validez de cada código recae, en última instancia, sobre quien lo sostiene.

<figure class="wide">
  <svg viewBox="0 0 680 300" style="width:100%;max-width:42rem;height:auto;display:block" role="img" aria-label="Cuadrícula de dos por dos. Eje horizontal: los codificadores coinciden o discrepan. Eje vertical: el código está bien puesto o mal puesto. Cuadrante coinciden y bien: consistencia y validez, lo que se quiere. Cuadrante coinciden y mal: consistencia sin validez, el caso invisible para kappa, por ejemplo ambos ponen 'barreras de acceso' por compartir la literatura. Cuadrante discrepan y bien: uno de los dos vio algo que el libro no nombra; el desacuerdo es un dato. Cuadrante discrepan y mal: el libro es ambiguo; hay que corregirlo. Kappa solo distingue las columnas, no las filas.">
    <style>.t{font-family:var(--text);font-size:12px;fill:var(--ink)} .s{font-family:var(--text);font-size:10.5px;fill:var(--muted)} .k{font-family:var(--mono);font-size:9.5px;letter-spacing:.08em;fill:var(--muted)} .q{fill:var(--surface);stroke:var(--rule);stroke-width:1.2} .qa{fill:var(--surface);stroke:var(--c-inv);stroke-width:1.4} .qn{fill:var(--surface);stroke:var(--c-fil);stroke-width:1.4} .kf{font-family:var(--mono);font-size:9.5px;letter-spacing:.08em;fill:var(--c-fil)} .ax{stroke:var(--muted);stroke-width:1.2;fill:none}</style>
    <text x="250" y="16" text-anchor="middle" class="k">COINCIDEN</text>
    <text x="520" y="16" text-anchor="middle" class="k">DISCREPAN</text>
    <text x="14" y="90" class="k" transform="rotate(-90 14 90)">BIEN PUESTO</text>
    <text x="14" y="230" class="k" transform="rotate(-90 14 230)">MAL PUESTO</text>
    <rect x="120" y="26" width="260" height="110" rx="3" class="qa"/>
    <text x="132" y="48" class="t">consistencia y validez</text>
    <text x="132" y="66" class="s">lo que se quiere, y lo que kappa</text>
    <text x="132" y="80" class="s">no puede distinguir del cuadrante de abajo</text>
    <rect x="390" y="26" width="260" height="110" rx="3" class="q"/>
    <text x="402" y="48" class="t">uno de los dos vio algo</text>
    <text x="402" y="66" class="s">que el libro aún no nombra:</text>
    <text x="402" y="80" class="s">el desacuerdo es un dato sobre el libro</text>
    <text x="402" y="100" class="s">ampliar definición · añadir código · nueva regla</text>
    <rect x="120" y="146" width="260" height="110" rx="3" class="qn"/>
    <text x="132" y="168" class="t">consistencia sin validez</text>
    <text x="132" y="186" class="s">ambos ponen "barreras de acceso"</text>
    <text x="132" y="200" class="s">porque comparten la literatura, no el corpus</text>
    <text x="132" y="220" class="kf">INVISIBLE PARA KAPPA</text>
    <rect x="390" y="146" width="260" height="110" rx="3" class="q"/>
    <text x="402" y="168" class="t">el libro es ambiguo</text>
    <text x="402" y="186" class="s">o el material resiste al libro:</text>
    <text x="402" y="200" class="s">corregir el instrumento, no al codificador</text>
    <path class="ax" d="M120 142 L650 142" stroke-dasharray="4 4"/>
    <text x="120" y="282" class="s">Kappa y alfa distinguen las columnas. Las filas solo se distinguen leyendo cada fragmento con el criterio de la tradición declarada.</text>
  </svg>
  <figcaption><b>Figura 6.</b> Acuerdo frente a validez. Lo que hay que ver: las medidas de acuerdo separan las columnas; la validez está en las filas, y el cuadrante inferior izquierdo es el que un acuerdo alto con el modelo oculta.</figcaption>
</figure>

## IA y exigencia

Esta semana se le pide al modelo que aplique el libro de códigos del estudiante, fijado en la semana 4, a treinta fragmentos, con una sola instrucción y sin proponer códigos nuevos; el estudiante codifica los mismos treinta por separado y antes de ver la salida del modelo. Luego se le pide al modelo que explique, para cada desacuerdo, por qué eligió su código. El estudiante debe poder, sin el modelo, calcular o leer kappa y alfa, decir qué miden y qué no, clasificar cada desacuerdo en un tipo y derivar de él una decisión sobre el libro, y explicar por qué un acuerdo del 90 % no autoriza a decir que el libro es válido.

## Lecturas

**Central**

- McDonald, N., Schoenebeck, S. y Forte, A. (2019). "Reliability and Inter-rater Reliability in Qualitative Research: Norms and Guidelines for CSCW and HCI Practice". *Proceedings of the ACM on Human-Computer Interaction* 3(CSCW), art. 72. https://doi.org/10.1145/3359174
- Krippendorff, K. (2004). "Reliability in Content Analysis: Some Common Misconceptions and Recommendations". *Human Communication Research* 30(3), 411-433. https://doi.org/10.1111/j.1468-2958.2004.tb00738.x

**Complementaria**

- Cohen, J. (1960). "A Coefficient of Agreement for Nominal Scales". *Educational and Psychological Measurement* 20(1), 37-46. https://doi.org/10.1177/001316446002000104
- Hayes, A. F. y Krippendorff, K. (2007). "Answering the Call for a Standard Reliability Measure for Coding Data". *Communication Methods and Measures* 1(1), 77-89. https://doi.org/10.1080/19312450709336664
- Artstein, R. y Poesio, M. (2008). "Inter-Coder Agreement for Computational Linguistics". *Computational Linguistics* 34(4), 555-596. https://aclanthology.org/J08-4004/
- Gilardi, F., Alizadeh, M. y Kubli, M. (2023). "ChatGPT outperforms crowd workers for text-annotation tasks". *Proceedings of the National Academy of Sciences* 120(30), e2305016120. https://doi.org/10.1073/pnas.2305016120
- Braun, V. y Clarke, V. (2019). "Reflecting on reflexive thematic analysis". *Qualitative Research in Sport, Exercise and Health* 11(4), 589-597. https://doi.org/10.1080/2159676X.2019.1628806
- Krippendorff, K. (2018). *Content Analysis*. 4.ª ed. Thousand Oaks: Sage. Capítulo sobre fiabilidad.

## Guía de lectura

- McDonald, Schoenebeck y Forte distinguen situaciones en que la fiabilidad entre codificadores es apropiada de situaciones en que no lo es, y proponen que los autores declaren cuál es la suya. *¿En cuál está su proyecto, según la tradición que declaró en la semana 1? ¿Cambia la respuesta por el hecho de que uno de los codificadores sea un modelo?*
- Krippendorff enumera errores comunes: usar el porcentaje de acuerdo, usar medidas que no corrigen por azar, calcular sobre unidades no independientes. *¿Cuál de esos errores es más probable al medir acuerdo con un modelo, dado que el modelo ha visto en su entrenamiento textos parecidos a los que codifica?*
- Gilardi y colaboradores comparan al modelo con trabajadores de plataformas de anotación y con anotadores entrenados. *¿Contra qué estándar se mide "superar"? ¿Qué sentido de validación, de los tres del curso, está en juego?*
- Braun y Clarke sostienen que el consenso entre codificadores no es un criterio de calidad del análisis reflexivo. *Si es así, ¿para qué sirve la matriz de esta semana en un proyecto de análisis temático reflexivo? Hay una respuesta, y no es "para nada".*

## Taller de la segunda hora

Guía completa en `practicas/practica-06-matriz-de-acuerdo.md`. En resumen: el estudiante trae sus treinta fragmentos codificados a mano con el libro fijo; en la sesión obtiene la codificación del modelo con la misma instrucción, calcula el acuerdo con el cuaderno de apoyo o con la mini app de la semana 3 adaptada, y clasifica cada desacuerdo.

| Fragmento | Mi código | Código del modelo | Tipo de desacuerdo | Explicación del modelo (literal) | Decisión sobre el libro | Criterio |
|---|---|---|---|---|---|---|

Al final, en una frase, el estudiante escribe qué mide el acuerdo obtenido y qué no mide, con el valor de kappa y de alfa.

## Guion de la sesión

| Momento | Qué hace el docente | Qué hace el estudiante | Material |
|---|---|---|---|
| 0 a 15 min | Calcula en el tablero el acuerdo simple y kappa de un caso de seis fragmentos, con una categoría dominante, para mostrar el descuento por azar | Sigue el cálculo y repite con sus marginales | Tablero, cuaderno |
| 15 a 40 min | Expone McDonald et al., Krippendorff y la figura 6; presenta los tipos de desacuerdo | Ubica su proyecto en la clasificación de McDonald | Figura 6 |
| 40 a 100 min | Práctica 6: obtención de la codificación del modelo, cálculo, lectura de desacuerdos mesa por mesa | Calcula, clasifica, decide sobre el libro | Práctica 6, cuaderno, plantilla de matriz |
| 100 a 115 min | Pone en común dos desacuerdos del tipo "consistencia sin validez" encontrados en el grupo | Revisa si tiene alguno | Matrices |
| 115 a 120 min | Recibe el producto 2 y anuncia la saturación de la semana 7 | Entrega | Plantilla de matriz |

Notas para el docente. Suele fallar que el estudiante ve la salida del modelo antes de codificar a mano y luego la matriz mide memoria, no acuerdo; verificar el orden al inicio. Suele fallar que el modelo, aunque se le prohíba, propone un código nuevo para algún fragmento; se registra como categoría aparte en el cálculo y como señal de forzamiento en el análisis. Y suele ocurrir que un estudiante con kappa alto concluye que puede delegar el resto del corpus: la respuesta del curso es que puede, bajo verificación por muestreo y con el registro, y que lo que no puede delegar es la decisión sobre cada desacuerdo que el muestreo encuentre.

## Entrega

Matriz de acuerdo y análisis de desacuerdos, con la plantilla `plantillas/matriz-de-acuerdo.md`: los treinta fragmentos con los dos códigos, kappa y alfa con su cálculo, cada desacuerdo clasificado con su decisión sobre el libro, y la frase final sobre qué mide y qué no mide el acuerdo obtenido. Prompts literales en anexo. Rúbrica en `evaluacion.md`.

## Para la próxima semana

Leer Glaser y Strauss (1967), capítulos 3 y 5, y Saunders et al. (2018). Escribir, antes de leer, en una frase, la condición de terminación que el estudiante cree que usará, y guardarla para compararla después. La semana 7 decide cuándo parar.
