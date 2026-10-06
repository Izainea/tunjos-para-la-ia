# Semana 7. Gobernanza

## Pregunta de la semana

Cuando un resultado producido con un modelo entra en un informe con nombre institucional, ¿quién decidió que entrara, qué quedó registrado y ante quién responde la institución?

## Por qué esta semana

<p class="lede">El tercer frente es el que convierte los otros dos en obligaciones. Un investigador puede cuidar su material y auditar su modelo por convicción; un equipo o una institución solo lo hace si alguien escribió que hay que hacerlo, quién lo hace y qué pasa si no se hace. Esa escritura es la gobernanza. La semana lee tres textos colombianos recientes que la exigen a las entidades públicas, el documento CONPES 4144 de 2025, la Sentencia T-067 de 2025 y la Directiva Conjunta 007 de 2025, y extrae de ellos lo que un protocolo de investigación puede adoptar aunque la ley no lo obligue: transparencia activa sobre los sistemas que se usan, evaluación de impacto antes de desplegarlos, canales para objetar sus resultados y una persona con nombre detrás de cada decisión. Después presenta los tres componentes del protocolo que el curso construye: la declaración de uso de IA, los roles y los registros.</p>

De las semanas anteriores llegan tres insumos: la matriz de riesgos y derechos, el perfil de exclusiones de la auditoría y la tabla de fases con los andamiajes. El protocolo los ordena en reglas.

## Contenido de la sesión

1. El documento CONPES 4144 de 2025, aprobado el 14 de febrero de 2025, es la política nacional de inteligencia artificial de Colombia. Fija un horizonte de implementación de 2024 a 2030, 106 acciones a cargo de varias entidades y una inversión aproximada de 479.273 millones de pesos, y organiza sus objetivos específicos en seis ejes, el primero de los cuales es fortalecer los mecanismos de gobernanza y aplicar principios éticos a los sistemas de IA para asegurar un desarrollo y uso responsable<sup class="mark">a</sup>. Para el curso importa menos el plan de acción que el gesto: el Estado colombiano trata la gobernanza de la IA como la primera condición de su uso, antes que la infraestructura y el talento. Un protocolo de investigación puede adoptar el mismo orden.

<aside class="glosa"><span class="mark">a</span> Documento CONPES 4144 de 2025, *Política nacional de inteligencia artificial*. Departamento Nacional de Planeación. Versión aprobada, 126 páginas. https://colaboracion.dnp.gov.co/CDT/Conpes/Econ%C3%B3micos/4144.pdf. El eje de ética y gobernanza está en la sección 5.3.1.</aside>

2. La Sentencia T-067 de 2025 de la Corte Constitucional, del 26 de febrero de 2025, resolvió la tutela de un ciudadano que pidió el código fuente de la aplicación CoronApp, usada durante la pandemia, y a quien tres entidades se lo negaron por razones de seguridad y protección de datos. La Corte revocó las decisiones de instancia, ordenó entregar el código con salvaguardas para los datos de los usuarios y sostuvo que la transparencia algorítmica es una garantía del derecho de acceso a la información pública: la complejidad técnica no justifica una negativa en bloque, y suprimir los datos sensibles es una alternativa a negar el acceso<sup class="mark">b</sup>. La sentencia no trata de investigación ni de modelos de lenguaje. Lo que trae al curso es un principio de máxima divulgación aplicado a sistemas: quien usa un sistema para decidir debe poder mostrar cómo decide.

<aside class="glosa"><span class="mark">b</span> Corte Constitucional de Colombia, Sentencia T-067 de 2025. https://www.corteconstitucional.gov.co/relatoria/2025/T-067-25.htm. La sentencia ordenó además al Estado desarrollar estrategias de transparencia algorítmica en sus herramientas digitales, y de esa orden nace la directiva siguiente.</aside>

3. La Directiva Conjunta 007 de 2025, expedida el 30 de septiembre de 2025 por la Procuraduría General de la Nación y la Defensoría del Pueblo, fija estándares de transparencia algorítmica para los sistemas que usa el Estado, en cumplimiento de la sentencia anterior<sup class="mark">c</sup>. Obliga a los sujetos de la Ley 1712 de 2014 que desarrollen, adquieran o implementen sistemas con IA, sistemas de decisión automatizada o sistemas que recojan datos personales de geolocalización. Les exige publicar de forma activa, para cada sistema, su nombre, objetivo, función, estado, si trata datos personales y de qué tipo, quién lo desarrolló y cómo reclamar; para los sistemas que evalúan beneficios, predicen riesgos o perfilan personas, exige además los criterios de decisión, los resultados de una evaluación de impacto, las medidas de mitigación y la documentación de los datos de entrenamiento. Da seis meses para cumplir. Es, con otras palabras, una matriz de riesgos y una declaración de uso convertidas en obligación.

<aside class="glosa"><span class="mark">c</span> Procuraduría General de la Nación y Defensoría del Pueblo, Directiva Conjunta 007 de 2025, *Estándares sobre transparencia algorítmica para los sistemas algorítmicos utilizados por el Estado*. Texto compilado en el normograma del Ministerio TIC: https://normograma.mintic.gov.co/mintic/compilacion/docs/directiva_procuraduria_0007_2025.htm. El docente la usó, con el CONPES y la sentencia, para la matriz de alineación normativa de la política institucional de IA de una entidad estadística nacional.</aside>

4. Lo que estas tres normas tienen en común es que devuelven la responsabilidad a su lugar. Ninguna admite que un sistema "se equivocó" como explicación: exigen que alguien haya decidido usarlo, haya evaluado su impacto, haya publicado qué hace y responda por sus resultados. Esa es la tesis del tercer frente, formulada por el docente en términos del programa: la metáfora de la alucinación exime a quien despliega, y el protocolo explícito lo vuelve a poner en la escena (Zainea, 2026). La figura muestra el flujo de la responsabilidad con y sin protocolo.

<figure class="wide">
  <svg viewBox="0 0 680 300" style="width:100%;max-width:42rem;height:auto;display:block" role="img" aria-label="Dos flujos. Sin protocolo: el modelo produce, el investigador acepta, el informe sale, el error se atribuye a la herramienta y nadie responde. Con protocolo: el modelo produce, un rol revisa contra registros declarados, se rechaza o se acepta con razón, el informe sale con declaración de uso, y una persona con nombre responde.">
    <style>.f7-h{font-family:var(--display);font-weight:700;font-size:13px;fill:var(--ink)} .f7-d{font-family:var(--text);font-size:11px;fill:var(--muted)} .f7-k{font-family:var(--mono);font-size:10px;letter-spacing:.08em;fill:var(--muted)} .f7-kf{font-family:var(--mono);font-size:10px;letter-spacing:.08em;fill:var(--c-fil)} .f7-ki{font-family:var(--mono);font-size:10px;letter-spacing:.08em;fill:var(--c-inv)} .f7-bx{fill:var(--surface);stroke:var(--rule);stroke-width:1.2} .f7-bf{fill:var(--surface);stroke:var(--c-fil);stroke-width:1.4} .f7-bi{fill:var(--surface);stroke:var(--c-inv);stroke-width:1.4} .f7-ar{stroke:var(--muted);stroke-width:1.3;fill:none} .f7-ah{fill:var(--muted)} .f7-rule{stroke:var(--rule);stroke-width:1}</style>
    <defs><marker id="f7-m" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 1L9 5L0 9z" class="f7-ah"/></marker></defs>
    <text x="20" y="28" class="f7-kf">SIN PROTOCOLO</text>
    <rect x="20" y="40" width="120" height="50" rx="3" class="f7-bx"/>
    <text x="30" y="60" class="f7-h">Modelo</text>
    <text x="30" y="78" class="f7-d">produce</text>
    <rect x="170" y="40" width="120" height="50" rx="3" class="f7-bx"/>
    <text x="180" y="60" class="f7-h">Investigador</text>
    <text x="180" y="78" class="f7-d">acepta</text>
    <rect x="320" y="40" width="120" height="50" rx="3" class="f7-bx"/>
    <text x="330" y="60" class="f7-h">Informe</text>
    <text x="330" y="78" class="f7-d">sale sin declaración</text>
    <rect x="470" y="40" width="190" height="50" rx="3" class="f7-bf"/>
    <text x="480" y="60" class="f7-h">"La herramienta alucinó"</text>
    <text x="480" y="78" class="f7-d">nadie responde</text>
    <path class="f7-ar" d="M140 65 L168 65" marker-end="url(#f7-m)"/>
    <path class="f7-ar" d="M290 65 L318 65" marker-end="url(#f7-m)"/>
    <path class="f7-ar" d="M440 65 L468 65" marker-end="url(#f7-m)"/>
    <path class="f7-rule" d="M20 120 L660 120"/>
    <text x="20" y="148" class="f7-ki">CON PROTOCOLO</text>
    <rect x="20" y="160" width="120" height="50" rx="3" class="f7-bx"/>
    <text x="30" y="180" class="f7-h">Modelo</text>
    <text x="30" y="198" class="f7-d">produce, con registro</text>
    <rect x="170" y="160" width="120" height="50" rx="3" class="f7-bi"/>
    <text x="180" y="180" class="f7-h">Rol revisor</text>
    <text x="180" y="198" class="f7-d">contrasta con registros</text>
    <rect x="320" y="160" width="120" height="50" rx="3" class="f7-bi"/>
    <text x="330" y="180" class="f7-h">Decisión</text>
    <text x="330" y="198" class="f7-d">acepta o rechaza, con razón</text>
    <rect x="470" y="160" width="190" height="50" rx="3" class="f7-bi"/>
    <text x="480" y="180" class="f7-h">Informe con declaración</text>
    <text x="480" y="198" class="f7-d">una persona con nombre responde</text>
    <path class="f7-ar" d="M140 185 L168 185" marker-end="url(#f7-m)"/>
    <path class="f7-ar" d="M290 185 L318 185" marker-end="url(#f7-m)"/>
    <path class="f7-ar" d="M440 185 L468 185" marker-end="url(#f7-m)"/>
    <text x="340" y="250" text-anchor="middle" class="f7-d">Lo que cambia no es el modelo sino quién aparece en la escena cuando algo sale mal.</text>
    <text x="340" y="275" text-anchor="middle" class="f7-k">MATRIZ DE RIESGOS · PERFIL DE EXCLUSIONES · ANDAMIAJES · DECLARACIÓN DE USO</text>
  </svg>
  <figcaption><b>Figura 7.</b> El flujo de la responsabilidad con y sin protocolo. En el de arriba el error termina en la herramienta; en el de abajo, en una persona que puede dar razones.</figcaption>
</figure>

5. La declaración de uso de IA es el componente más visible del protocolo y el que más se malentiende. No es una nota al pie que dice "se usó un modelo". Es un documento que acompaña cada producto y dice qué modelo, con qué versión y fecha, para qué fases, con qué instrucciones, qué material salió hacia él y bajo qué condiciones, qué se aceptó, qué se rechazó y por qué, qué no se pudo verificar, y quién firma. La plantilla del curso la formaliza en una página. Un lector que la tenga puede reconstruir dónde terminó la máquina y dónde empezó el investigador, que es lo que [*Validación del razonamiento con IA en ciencias sociales*, semana 7](../../curso-1-tres-inferencias/programa/semana-07.md) llamó registro de frontera: una tabla en que el investigador anota, paso a paso, qué propuso la máquina y qué decidió él, con qué criterio, de modo que quede a la vista dónde termina lo configurado por el modelo y dónde empieza lo que él afirma. La declaración es ese registro en formato para terceros.

6. Los roles son la parte del protocolo que un investigador solo tiende a saltarse y que un equipo no puede. El curso propone cuatro y admite que una persona ocupe varios si lo declara. Quien decide qué material sale hacia un modelo y bajo qué condiciones, con la matriz de riesgos en la mano. Quien revisa las lecturas del modelo contra el perfil de exclusiones y los registros, sin haberlas producido. Quien es lector situado para las piezas que la auditoría marcó. Y quien firma el producto y responde por él ante quienes se estudia y ante quienes lo leen. La regla que hace a los roles algo más que nombres es la separación entre quien produce y quien revisa, y la Directiva 007 la exige a su modo cuando pide canales de objeción distintos de quien opera el sistema.

7. Los registros son lo que permite que el protocolo se audite. El curso pide tres, que ya existen al llegar a esta semana: la matriz de riesgos con la cláusula de términos de uso copiada y fechada, el registro de lecturas del modelo con instrucción literal y versión, y el registro de rechazos con su razón. Con ellos un tercero puede verificar que el protocolo se cumplió sin confiar en la palabra de quien lo aplicó. Sin ellos, el protocolo es una declaración de intenciones, que es lo que las guías de principios ya ofrecen y que el curso quiere superar.

| Guía de principios | Protocolo de gobernanza |
|---|---|
| Dice qué valores respetar | Dice qué hace cada rol el lunes |
| Vale para cualquier proyecto | Vale para este proyecto, con esta matriz y este perfil |
| No tiene registros | Tiene tres registros que un tercero puede leer |
| Si algo sale mal, se revisa el principio | Si algo sale mal, se busca la fila del registro y la persona del rol |
| *Nadie la puede incumplir* | *Alguien la puede incumplir, y por eso obliga* |

## IA y exigencia

Esta semana se le pide al modelo un borrador de protocolo a partir de los tres insumos del estudiante. El estudiante debe poder, sin el modelo, señalar qué reglas del borrador no responden a ningún riesgo de su matriz, qué roles no tienen persona posible en su equipo o institución, y qué registro propuso el modelo que nadie podría llevar. Un protocolo con reglas sin riesgo es una guía de principios con otro nombre.

## Lecturas

**Central**

- Departamento Nacional de Planeación (2025). Documento CONPES 4144, *Política nacional de inteligencia artificial*. Resumen ejecutivo y sección 5.3.1. https://colaboracion.dnp.gov.co/CDT/Conpes/Econ%C3%B3micos/4144.pdf
- Corte Constitucional de Colombia (2025). Sentencia T-067 de 2025. Síntesis de la decisión y consideraciones sobre transparencia algorítmica. https://www.corteconstitucional.gov.co/relatoria/2025/T-067-25.htm
- Procuraduría General de la Nación y Defensoría del Pueblo (2025). Directiva Conjunta 007 de 2025. https://normograma.mintic.gov.co/mintic/compilacion/docs/directiva_procuraduria_0007_2025.htm

**Complementaria**

- Floridi, L. (2023). *The Ethics of Artificial Intelligence*. Oxford University Press. Parte 3, sobre gobernanza y buenas prácticas.
- Floridi, L. (2026). "AI and the future of publishing: Not detection, but answerability". *Philosophy & Technology* 39(3), 129. https://doi.org/10.1007/s13347-026-01148-8
- Zainea, C. I. (2026). *Agencia sin imputación*. Sección sobre justificación social. https://izainea.github.io/escritos/agencia-sin-imputacion.pdf

## Guía de lectura

- El CONPES pone la ética y la gobernanza como primer objetivo y la infraestructura después. *¿En qué orden están en su proyecto o en su institución? ¿Qué cambiaría si se invirtiera?*
- La Corte sostiene que suprimir datos sensibles es alternativa a negar el acceso al código. *¿Qué equivale, en su protocolo, a entregar el código con salvaguardas? ¿Qué puede mostrar de su flujo sin exponer a las personas del corpus?*
- La Directiva exige evaluación de impacto antes de desplegar sistemas que perfilan o predicen riesgos. *¿Su flujo perfila a alguien, aunque no lo llame así? Una categorización de relatos por tipo de víctima, ¿es un perfil?*
- Floridi (2026) propone que el problema de la IA en la publicación no es la detección sino la *answerability*, que alguien pueda responder. *¿Qué parte de su declaración de uso sirve a la detección y qué parte a la respuesta? ¿Cuál de las dos pediría un revisor de su campo?*

## Taller de la segunda hora

El taller escribe el protocolo preliminar sobre la plantilla, con los tres insumos a la vista. La guía `practicas/practica-08-protocolo-con-equipo.md` tiene el paso a paso para equipos; quien trabaja solo la sigue ocupando los roles y declarándolo. En resumen:

| Regla | Riesgo de la matriz o exclusión del perfil que la motiva | Rol responsable | Registro donde se verifica | Condición de rechazo | Norma que la respalda, si la hay |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

Al terminar, cada estudiante marca la regla que más le cuesta cumplir y escribe por qué: esa regla es la que la revisión entre pares de la semana 8 examina primero.

## Guion de la sesión

| Momento | Docente | Estudiante | Material |
|---|---|---|---|
| 0 a 15 min | Presenta el CONPES y su orden de objetivos | Compara con el orden de su institución | Lectura central |
| 15 a 30 min | Expone la sentencia y el principio de máxima divulgación | Dice qué puede mostrar de su flujo | Lectura central |
| 30 a 45 min | Recorre las obligaciones de la Directiva 007 | Marca cuáles adoptaría aunque no lo obliguen | Lectura central |
| 45 a 60 min | Presenta la Figura 7 y los tres componentes del protocolo | Asigna personas posibles a los cuatro roles | Figura 7, plantillas |
| 60 a 100 min | Acompaña la escritura del protocolo preliminar | Escribe reglas con riesgo, rol, registro y condición de rechazo | Plantilla |
| 100 a 115 min | Recoge la regla más difícil de cada estudiante | La expone | Bitácora |
| 115 a 120 min | Explica el formato de la revisión entre pares | Anota qué debe traer | Semana 8 |

Notas para el docente. Suele fallar que las reglas se escriban como principios ("se usará la IA de forma responsable"); exigir verbo, rol y registro en cada una. Suele fallar que el estudiante que trabaja solo deje los roles vacíos; una persona puede ocupar varios, pero tiene que escribirlo y decir qué pierde con eso. Y hay que evitar que la lectura de las normas se convierta en una clase de derecho: lo que importa es lo que un protocolo de investigación puede adoptar de ellas.

## Entrega

Protocolo preliminar en la plantilla `plantillas/protocolo-de-gobernanza-epistemica.md`, con al menos seis reglas, los cuatro roles asignados y los tres registros identificados. No se califica por separado: es la versión que la semana 8 revisa entre pares y que se convierte en la entrega final.

## Para la próxima semana

Leer la sección sobre la prótesis hermenéutica de Zainea (2026) y la entrada del blog. Completar el protocolo preliminar y la declaración de uso de IA del propio proyecto con la plantilla `plantillas/declaracion-de-uso-de-ia.md`. Preparar una presentación de ocho minutos con el formato de la semana 8.
