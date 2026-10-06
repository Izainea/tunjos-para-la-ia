# Práctica 3. Recolección reproducible

Duración estimada: 3 horas, de las cuales 1 en la sesión sincrónica.
Requisitos: el cuaderno de la semana 2 funcionando, las bibliotecas `requests` y `pandas` instaladas, la ficha de delimitación revisada y la plantilla `plantillas/protocolo-de-corpus.md`. Bloques de código en `practicas/cuaderno-apoyo.md`, sección "Semana 3".

## Objetivo

Ejecutar una recolección pequeña sobre el caso demostrativo y sobre una fuente propia, de modo que otra persona pueda repetirla con el mismo cuaderno y obtener el mismo resultado, y producir con eso el anexo del protocolo de corpus.

## Antes de la sesión

1. Elija una fuente propia con no más de diez piezas para esta práctica. Puede ser la más fácil de sus fuentes; la práctica es sobre el método, no sobre el volumen.
2. Abra en el navegador el `robots.txt` de esa fuente (la dirección del sitio seguida de `/robots.txt`) y sus términos de uso. Anote qué dicen sobre descarga y reproducción.
3. Escriba a mano la lista de las piezas que va a pedir, con su dirección completa. Revísela. Esa lista es el insumo del programa, no su resultado.
4. Cree la carpeta `crudo` vacía dentro de su proyecto.

## Durante la sesión: tres rondas

### Ronda 1. Leer lo que el sitio declara

Con el bloque de `robots.txt` del cuaderno de apoyo, compruebe por programa lo que leyó a mano para datos.gov.co, para la Secretaría del Senado y para su fuente. Anote en el cuaderno, en una celda de texto, qué permite cada uno y qué ritmo de petición va a usar. Si su fuente no permite la descarga automática, la práctica continúa con recolección manual: descargue cada pieza con el navegador, guárdela en `crudo` y llene la bitácora a mano con los mismos campos.

### Ronda 2. Descargar el caso demostrativo

Ejecute la función `descargar` sobre la norma de la Secretaría del Senado y sobre un conjunto de datos.gov.co. Abra la bitácora `bitacora_descarga.jsonl` y lea una fila: debe tener la dirección, el destino, la fecha, el estado, el hash y el tamaño. Abra el archivo de `crudo` sin editarlo y confirme que es lo que la fuente mostraba.

Preguntas que debe poder responder antes de seguir:

- ¿Cuánto esperó el programa entre las dos peticiones? ¿Dónde está escrito?
- ¿Con qué nombre y correo se identificó? ¿Dónde está escrito?
- Si la fuente hubiera respondido con error, ¿qué habría hecho el programa?

### Ronda 3. Descargar la fuente propia

Pase su lista revisada al bloque `pedidos` y ejecute. Al terminar, reinicie el núcleo, borre nada, y ejecute el cuaderno completo de nuevo. Compare los hash de las dos ejecuciones con el bloque de comparación. Si coinciden, su recolección es reproducible hoy. Si no coinciden, averigüe por qué: la fuente cambió, la página incluye la fecha de consulta, o algo en el programa no es determinista. Las tres cosas se anotan.

## Después de la sesión

1. Llene en el protocolo la tabla de fuentes con lo aprendido: forma de entrega, robots.txt y términos, ritmo, método.
2. Llene la tabla de lo que no se descarga. Debe tener al menos una fila; si no la tiene, no ha mirado con cuidado.
3. Guarde el cuaderno de recolección como `cuadernos/01-recoleccion.ipynb` y adjúntelo al protocolo.
4. Anote en el registro de frontera qué código propuso el modelo, qué corrigió usted antes de ejecutarlo y por qué.

## Qué se evalúa

Que el cuaderno corra de arriba abajo sobre una fuente propia con bitácora, pausa e identificación, y que el protocolo diga lo que no se descarga con su razón. Una recolección de tres piezas bien registrada vale más que una de trescientas sin bitácora.

## Variante para grupos

Dos estudiantes intercambian cuadernos y listas, y cada uno ejecuta la recolección del otro. Las diferencias de hash entre lo que obtuvo el autor y lo que obtuvo el par son el mejor material de discusión de la sesión siguiente.
