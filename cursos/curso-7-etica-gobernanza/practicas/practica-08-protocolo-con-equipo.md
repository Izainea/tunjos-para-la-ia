# Práctica 8. Redacción del protocolo de gobernanza epistémica con un equipo

Duración estimada: 6 horas repartidas entre las semanas 7 y 8, de las cuales 2 en sesiones sincrónicas.
Requisitos: la matriz de riesgos y derechos (semana 3), la auditoría de exterioridad con su perfil (semana 5), la tabla de fases y andamiajes (semana 6), y las plantillas `plantillas/protocolo-de-gobernanza-epistemica.md` y `plantillas/declaracion-de-uso-de-ia.md`.
Para equipos de dos a seis personas. Quien trabaja solo sigue la guía ocupando los roles y declarándolo, con la variante del final.

## Objetivo

Escribir un protocolo que una persona distinta de sus autores pueda ejecutar, ponerlo a prueba ante pares sobre un caso real, e incorporar lo que la prueba muestre.

## Antes de la primera sesión, lo que cada miembro trae

Cada miembro del equipo trae sus tres insumos. Si el equipo trabaja sobre un mismo proyecto, las matrices y auditorías se consolidan en una antes de la sesión: una matriz con todos los tipos de pieza, un perfil de exclusiones que reúne las muestras. Si cada miembro tiene su proyecto y el protocolo es para un equipo o una institución que los cubre a todos, los insumos se conservan separados y el protocolo tiene un alcance que los nombra.

## Primera sesión, las reglas (semana 7)

### Paso 1. Alcance y qué gobierna (20 minutos)

El equipo escribe la sección 1 de la plantilla y la frase de la sección 2: qué cuenta como afirmación válida en este proyecto y quién responde. Si no hay acuerdo sobre esa frase, el resto no puede escribirse; es preferible dedicarle más tiempo que avanzar sin ella.

### Paso 2. De los riesgos a las reglas (40 minutos)

Sobre la matriz consolidada, el equipo toma cada daño con probabilidad media o alta y escribe la regla que lo evita. La regla tiene verbo (qué se hace), rol (quién), registro (dónde se verifica) y condición de rechazo (cuándo un resultado no entra en un producto). Luego hace lo mismo con el perfil de exclusiones: la regla derivada de la auditoría entra tal cual. Un ejemplo de regla completa:

| Nº | Regla | Riesgo o exclusión | Rol | Registro | Condición de rechazo | Norma |
|---|---|---|---|---|---|---|
| 1 | Las piezas con datos sensibles se seudonimizan antes de cualquier consulta, y la tabla de correspondencia queda fuera del servicio | Reidentificación de personas del corpus por el proveedor (matriz, tipo 2, probabilidad alta) | Decide qué sale | Matriz y cláusulas; lecturas del modelo | Cualquier lectura obtenida de una pieza no seudonimizada se descarta aunque sea correcta | Ley 1581, arts. 5 y 6 |

Las reglas que no responden a ningún riesgo se anotan en una lista aparte y se discuten: casi siempre son principios disfrazados, y se eliminan o se devuelven a la matriz como riesgo que faltaba.

### Paso 3. Roles con persona (20 minutos)

El equipo asigna los cuatro roles a personas con nombre. La única restricción es que quien revisa no haya producido lo que revisa. Si el equipo es pequeño y una persona ocupa varios roles, la tabla dice qué se pierde. Si el lector situado no está en el equipo, se nombra y se dice cómo se le convoca y se le reconoce.

### Paso 4. Registros (20 minutos)

Los tres registros ya existen en borrador al llegar aquí. El equipo decide quién lleva cada uno, dónde está y quién puede leerlo. Un registro que solo puede leer quien lo lleva no sirve para auditar.

### Paso 5. La regla más difícil (20 minutos)

Cada miembro marca la regla que más le costaría cumplir y dice por qué. El equipo decide si la regla se mantiene, se modifica o se asume el costo con el andamiaje de la sección 6. Esa regla es la primera que la revisión entre pares examina.

## Entre sesiones

1. Completar la sección 6, andamiaje que preserva el juicio, con los costos y quién los paga.
2. Escribir las secciones 8 y 9: riesgos que el protocolo decide no cubrir, y dónde exige más o menos que las normas leídas en la semana 7.
3. Preparar el caso para la revisión: una pieza real del corpus (o su descripción, según la matriz) con la lectura del modelo, elegida porque exige aplicar al menos tres reglas del protocolo.
4. Redactar la declaración de uso de IA del propio proyecto con la plantilla, como si acompañara un producto real.
5. Preparar la presentación de ocho minutos con el formato de la semana 8.

## Segunda sesión, la prueba (semana 8)

### Paso 6. Presentación (8 minutos)

El equipo presenta con el formato de la semana 8: alcance, tres riesgos mayores y sus reglas, perfil de exclusiones y regla derivada, fase nunca delegada, roles con persona, regla más difícil.

### Paso 7. Ejecución por pares (20 minutos)

Dos revisores que no conocen el proyecto reciben el caso y el protocolo, y lo ejecutan sin preguntar al equipo: deciden si la pieza podía salir hacia el modelo, qué rol revisa, contra qué registro, si se acepta o se rechaza. Llenan la tabla de revisión de la semana 8. Donde el protocolo no dice qué hacer, falta una regla. Donde dice algo que no pueden hacer, hay un rol sin persona o un registro que nadie lleva. Responden las dos preguntas obligatorias: ante quién no sería defendible, y qué regla sobra.

### Paso 8. Incorporación (después de la sesión)

El equipo recibe la tabla de revisión y, por cada objeción, cambia una regla o explica por qué no la cambia. La sección 10 de la plantilla registra ambas cosas. Un protocolo que incorpora todo sin discutir nada es tan sospechoso como uno que no incorpora nada.

## Qué se evalúa

La rúbrica del protocolo en `programa/evaluacion.md`. Lo que pesa más es que los revisores hayan podido ejecutarlo sin preguntar, que cada regla tenga un riesgo detrás, y que la revisión se haya incorporado con razones.

## Variante para quien trabaja solo

Un investigador solo escribe el mismo protocolo con una diferencia: la tabla de roles tiene su nombre en varias filas y dice qué se pierde en cada una, casi siempre la separación entre producir y revisar. La sección 10 debe decir cómo se repetirá la revisión externa después del curso, con un colega, un director de tesis o un lector situado, y con qué periodicidad. En la sesión de la semana 8 el protocolo individual se revisa igual que el de un equipo.

## Variante para una institución

Cuando el protocolo es para una entidad y no para un proyecto, el alcance nombra los tipos de material y los procesos que cubre, los roles se escriben por cargo y no por persona, y la sección 9 se vuelve la más larga: qué obligaciones de la Directiva Conjunta 007 de 2025 y del CONPES 4144 adopta la entidad para su investigación interna, y qué canal de objeción ofrece a las personas sobre las que produce resultados. El docente construyó una matriz de alineación normativa de ese tipo para la política institucional de IA de una entidad pública, y puede mostrar su estructura en la sesión sin exponer su contenido.
