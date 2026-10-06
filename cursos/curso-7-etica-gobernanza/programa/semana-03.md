# Semana 3. Consentimiento y plataformas

## Pregunta de la semana

Si una pieza está a la vista de cualquiera en una plataforma, ¿eso me autoriza a recogerla, a tratarla con un modelo y a publicar lo que resulte?

## Por qué esta semana

<p class="lede">Buena parte del material con que hoy se investiga no se recogió en una entrevista ni se pidió a un archivo: se descargó de una plataforma. Publicaciones, comentarios, fotografías, videos, hilos. La intuición común dice que lo que está a la vista es de uso libre, y esa intuición se equivoca dos veces. Se equivoca con la plataforma, que fijó términos de uso que son un contrato y que casi siempre restringen la recolección automatizada. Y se equivoca con las personas, que publicaron para una audiencia y una finalidad que no incluían ser datos de una investigación ni insumos de un modelo. La semana distingue dato público de dato abierto, lee los términos de uso como lo que son, examina la anonimización y sus límites, y cierra con la primera entrega: la matriz de riesgos y derechos del propio material.</p>

La semana anterior fijó la escala de usos (citar, describir, exhibir con reserva, no usar) y la columna de derechos de la matriz. Hoy se llenan las columnas de riesgo: qué daño, a quién, con qué probabilidad, con qué mitigación.

## Contenido de la sesión

1. Público no significa abierto. Un dato es público cuando cualquiera puede verlo; es abierto cuando quien tiene derechos sobre él autorizó su reutilización bajo una licencia explícita. Entre ambos hay una zona enorme: lo visible sin licencia. Un comentario en una red social, una fotografía en un perfil, un video en una plataforma, son públicos y no son abiertos. La Ley 1581 de 2012 lo recoge a su modo: el artículo 10 exime de autorización el tratamiento de datos de naturaleza pública, pero la definición de dato público del decreto reglamentario es estrecha, y un dato personal publicado por su titular en una red social no deja de ser personal<sup class="mark">a</sup>.

<aside class="glosa"><span class="mark">a</span> El Decreto 1377 de 2013, artículo 3, define dato público como el que no es semiprivado, privado ni sensible, y da como ejemplos el estado civil, la profesión y la calidad de comerciante o servidor público. Nada de eso cubre una opinión publicada en una red social, que sigue siendo dato personal y, según su contenido, sensible.</aside>

2. Los términos de uso de una plataforma son un contrato de adhesión, y casi todos prohíben la recolección automatizada sin autorización. Leerlos es una tarea de la semana, no una formalidad: en ellos se decide si el corpus puede existir. Hay tres salidas honestas. Usar la interfaz de programación oficial de la plataforma con las restricciones que impone, que suelen limitar volumen y uso. Recoger a mano, lo que limita la escala pero no la licitud. O decidir que el corpus no puede construirse así y buscar otro. La cuarta salida, recoger de forma automatizada sin permiso y no decirlo, es un infortunio en el sentido del curso: el informe presenta como fundamentado un material cuya procedencia no puede defenderse.

3. Fiesler y Proferes (2018) preguntaron a usuarios de una red social qué pensaban de que sus publicaciones se usaran en investigación. La mayoría no sabía que eso ocurría, y una parte considerable no estaba de acuerdo, sobre todo si se citaban de forma textual y con nombre, aunque las publicaciones fueran públicas<sup class="mark">b</sup>. El hallazgo tiene una consecuencia directa para la escala de usos de la semana 2: en material de plataformas, citar expone más que describir, porque una cita textual se puede buscar y lleva a la persona. La descripción densa y el parafraseo con verificación son, en este material, la regla y no la excepción.

<aside class="glosa"><span class="mark">b</span> Fiesler, C. y Proferes, N. (2018). "'Participant' Perceptions of Twitter Research Ethics". *Social Media + Society* 4(1). La comilla en el título es de las autoras: la pregunta es si quien publica puede llamarse participante de una investigación que no sabe que existe.</aside>

4. Enviar material de plataformas a un servicio de modelos añade una segunda plataforma con sus propios términos. La pregunta que hay que responder antes de la primera consulta es si el proveedor conserva lo que recibe y si lo usa para entrenar. Las condiciones varían entre servicios, entre planes del mismo servicio y en el tiempo, y por eso el curso no da una lista: da una regla. El estudiante localiza la cláusula, la copia en la bitácora con fecha, y decide. Si no la encuentra, asume que el proveedor conserva y entrena, y actúa en consecuencia: material con datos personales no sale hacia ese servicio sin anonimización previa. Esa decisión queda registrada y es parte de la matriz.

5. La anonimización tiene límites que conviene conocer antes de confiar en ella. Suprimir nombres no basta cuando el relato contiene lugar, fecha y hecho, porque la combinación identifica. Reemplazar por seudónimos conserva la estructura del dato y permite el análisis, pero el investigador guarda la tabla de correspondencia y con ella la responsabilidad. Generalizar (cambiar una vereda por un municipio, una fecha por un mes) protege más y pierde información que el análisis puede necesitar. Y un modelo puede desanonimizar: si recibe un relato con seudónimo y un corpus de prensa, puede proponer el nombre real como si fuera una inferencia más. La regla del curso es que la anonimización se documenta como una transformación del dato, con lo que se quitó y lo que se perdió, y no como un trámite cumplido.

| Técnica | Qué protege | Qué pierde el análisis | Qué conserva el investigador |
|---|---|---|---|
| Suprimir nombres | Poco: lugar, fecha y hecho identifican | Casi nada | Nada que lo comprometa |
| Seudonimizar | La identidad ante terceros | Nada: la estructura se conserva | La tabla de correspondencia, y con ella la responsabilidad |
| Generalizar lugares y fechas | Más: rompe el cruce con otras fuentes | Precisión que el análisis puede necesitar | Un registro de qué se generalizó |
| *Ninguna técnica protege contra un modelo que cruza el relato con un corpus público* | | | *La decisión de qué no sale hacia el modelo* |

<figure class="wide">
  <svg viewBox="0 0 680 250" style="width:100%;max-width:42rem;height:auto;display:block" role="img" aria-label="Tres regiones anidadas: lo abierto, con licencia explícita, dentro de lo público, visible para cualquiera, dentro de lo recogido, todo lo que un flujo podría tomar. Un dato personal publicado en una red social está en lo público pero fuera de lo abierto.">
    <style>.f3-h{font-family:var(--display);font-weight:700;font-size:14px;fill:var(--ink)} .f3-d{font-family:var(--text);font-size:11.5px;fill:var(--muted)} .f3-k{font-family:var(--mono);font-size:10px;letter-spacing:.08em;fill:var(--muted)} .f3-kf{font-family:var(--mono);font-size:10px;letter-spacing:.08em;fill:var(--c-fil)} .f3-r1{fill:none;stroke:var(--rule);stroke-width:1.2;stroke-dasharray:5 4} .f3-r2{fill:var(--surface);stroke:var(--muted);stroke-width:1.2} .f3-r3{fill:var(--surface);stroke:var(--c-inv);stroke-width:1.6} .f3-pt{fill:var(--c-fil)}</style>
    <rect x="20" y="20" width="640" height="210" rx="4" class="f3-r1"/>
    <text x="34" y="40" class="f3-k">LO QUE UN FLUJO PODRÍA RECOGER</text>
    <rect x="120" y="55" width="520" height="160" rx="4" class="f3-r2"/>
    <text x="134" y="75" class="f3-k">PÚBLICO · visible para cualquiera</text>
    <rect x="360" y="95" width="260" height="105" rx="4" class="f3-r3"/>
    <text x="374" y="115" class="f3-k" style="fill:var(--c-inv)">ABIERTO · con licencia explícita</text>
    <text x="374" y="140" class="f3-d">datos abiertos del Estado</text>
    <text x="374" y="156" class="f3-d">obras con licencia libre</text>
    <text x="374" y="172" class="f3-d">dominio público</text>
    <circle cx="210" cy="140" r="6" class="f3-pt"/>
    <text x="224" y="136" class="f3-h">opinión en una red social</text>
    <text x="224" y="152" class="f3-d">visible, sin licencia, dato personal</text>
    <circle cx="210" cy="185" r="6" class="f3-pt"/>
    <text x="224" y="181" class="f3-h">fotografía de prensa</text>
    <text x="224" y="197" class="f3-d">visible, con autor, con personas</text>
    <text x="34" y="215" class="f3-kf">FUERA: lo privado, lo que exige autorización</text>
  </svg>
  <figcaption><b>Figura 3.</b> Público no es abierto. Lo que casi todo corpus de plataformas contiene está en la franja del medio: visible, sin licencia y con personas.</figcaption>
</figure>

6. La matriz de riesgos y derechos es el instrumento que reúne todo lo anterior y es la primera entrega del curso. Para cada tipo de pieza del corpus, no para cada pieza, el estudiante registra los derechos que pesan sobre ella (semana 2), el daño que su uso puede causar, a quién, con qué probabilidad, y qué mitigación adopta. La mini app construye la matriz paso a paso y la exporta como texto para pegarla en la plantilla. La regla de llenado es que ninguna celda de daño puede decir "ninguno": si el estudiante no ve daño posible, el ejercicio es imaginar al lector menos benévolo de su informe y a la persona menos protegida de su corpus.

<iframe class="app" src="apps/matriz-de-riesgos.html" title="Constructor de matriz de riesgos y derechos exportable como texto" loading="lazy"></iframe>

7. Una matriz bien hecha no elimina el riesgo; lo pone a nombre de alguien. Esa es la diferencia con el párrafo de consideraciones éticas al final de un informe. La matriz dice qué puede salir mal, a quién le ocurriría y qué hizo el investigador para que no ocurra, y por eso es el primer documento del protocolo de gobernanza que el curso construye hasta la semana 8.

## IA y exigencia

Esta semana se le pide al modelo que proponga daños posibles para cada tipo de pieza y que estime su probabilidad. El estudiante debe poder, sin el modelo, decir a quién le ocurriría cada daño con nombre de grupo o de persona, y cuál de los daños propuestos por el modelo es genérico (aplicaría a cualquier corpus) y cuál es propio de su material. La matriz se evalúa por lo segundo.

## Lecturas

**Central**

- Fiesler, C. y Proferes, N. (2018). "'Participant' Perceptions of Twitter Research Ethics". *Social Media + Society* 4(1). https://doi.org/10.1177/2056305118763366
- Congreso de la República de Colombia. Ley estatutaria 1581 de 2012. Artículos 9 y 10. https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=49981
- Los términos de uso del servicio de modelos que el estudiante usa, en la versión vigente, con atención a las cláusulas de conservación de datos y de entrenamiento.

**Complementaria**

- Presidencia de la República de Colombia. Decreto 1377 de 2013. Artículo 3, definiciones.
- Floridi, L. (2023). *The Ethics of Artificial Intelligence*. Oxford University Press. Parte 2, capítulo sobre los retos de la práctica.

## Guía de lectura

- Fiesler y Proferes encuentran que la aceptación cambia según cómo se use la publicación: agregada, parafraseada o citada con nombre. *¿En qué escalón de la escala de usos está cada una de esas tres formas, y por qué la cita textual es la que más expone en este material?*
- El artículo 9 de la Ley 1581 exige autorización previa, expresa e informada, y el 10 enumera cuándo no se requiere. *¿Cabe su corpus en alguna de las excepciones del artículo 10? Si la respuesta es "datos de naturaleza pública", vuelva a la definición del decreto.*
- Los términos de uso de su proveedor de modelos dicen algo sobre entrenamiento, o no dicen nada. *¿Qué cláusula encontró, con qué fecha, y qué decidió a partir de ella? Si no encontró ninguna, ¿qué asumió?*

## Taller de la segunda hora

El taller construye la matriz en la mini app y la pasa a la plantilla. Cada estudiante trabaja sobre los tipos de pieza de su corpus, entre tres y seis.

| Tipo de pieza | Derechos que pesan (semana 2) | Daño posible | A quién | Probabilidad (baja, media, alta) | Mitigación | Uso que decido |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |

En la segunda mitad del taller, dos estudiantes intercambian matrices y cada uno busca en la del otro un daño que falta. La regla es que el daño que falta suele ser el que afecta a quien no está en la mesa.

## Guion de la sesión

| Momento | Docente | Estudiante | Material |
|---|---|---|---|
| 0 a 20 min | Distingue público de abierto con la Figura 3 y el Decreto 1377 | Ubica su corpus en la figura | Figura 3 |
| 20 a 40 min | Lee con el grupo una cláusula de términos de uso traída por un estudiante | Localiza la cláusula del servicio que usa | Términos de uso |
| 40 a 55 min | Discute Fiesler y Proferes y la cita que expone | Decide si en su corpus citar es defendible | Lectura central |
| 55 a 60 min | Presenta la mini app | Observa | Mini app |
| 60 a 95 min | Acompaña la construcción de la matriz | Construye su matriz y la exporta | Mini app y plantilla |
| 95 a 115 min | Organiza el intercambio de matrices | Busca el daño que falta en la matriz de un par | Matrices |
| 115 a 120 min | Cierra con las condiciones de entrega | Anota lo pendiente | Plantilla |

Notas para el docente. Suele fallar que la columna de daño se llene con generalidades ("mal uso de la información"); pedir que cada daño tenga un verbo y un afectado. Suele fallar que la probabilidad se ponga baja en todo por optimismo; pedir que al menos un daño por matriz sea alto y que se justifique por qué los otros no. Y conviene no dejar que la discusión sobre términos de uso se vuelva sobre si son justos: lo son o no, pero son el contrato.

## Entrega

Matriz de riesgos y derechos del propio material, en la plantilla `plantillas/matriz-de-riesgos-y-derechos.md`, con la columna de derechos de la semana 2 y las columnas de riesgo de esta semana. Incluye la cláusula de términos de uso copiada con fecha y la decisión tomada a partir de ella. Rúbrica en `evaluacion.md`.

## Para la próxima semana

Leer el capítulo 7 de Fricker (2007), el artículo de Kay, Kasirzadeh y Mohamed (2024) y el de Muldoon y Wu (2023). Traer tres piezas del corpus que el estudiante considere cargadas de sentido local: una expresión, un objeto o una escena que alguien de fuera no entendería sin explicación. Esas piezas abren el segundo frente del curso.
