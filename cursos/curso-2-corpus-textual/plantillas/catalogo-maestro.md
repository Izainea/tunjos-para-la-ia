# Catálogo maestro

**Estudiante:**
**Proyecto:**
**Archivo:** `catalogo.csv`, generado por `cuadernos/02-catalogo.ipynb`
**Fecha de la última regeneración:**

## Para qué sirve este documento

El catálogo es la tabla que sabe, de cada pieza del corpus, lo que hace falta para reconstruirla, citarla y defenderla. Lo genera el cuaderno, no se edita a mano; las decisiones a mano van en `decisiones.csv`, que el cuaderno lee y une por `id`. Este documento describe el esquema, da un ejemplo y lista las reglas de integridad.

## Esquema

Los campos obligatorios no pueden estar vacíos en ninguna fila. Un proyecto puede añadir columnas; no puede quitar las obligatorias ni cambiar sus nombres, para que los catálogos de distintos proyectos se puedan comparar y para que los cursos siguientes del programa los reciban sin traducción.

| Campo | Obligatorio | Formato | Qué responde | Ejemplo |
|---|---|---|---|---|
| `id` | Sí | Prefijo de una letra, guion, cuatro dígitos. Propio, estable, opaco | Cuál pieza es, sin depender de la fuente | `P-0042` |
| `titulo` | Sí | Texto. Si la pieza no tiene título, las primeras ocho palabras | Cómo se nombra | `Sesión de la junta de ayer` |
| `autor` | No | Texto o vacío. "Anónimo" cuando la fuente lo dice | Quién firma | `Anónimo` |
| `fuente` | Sí | Nombre de la fuente tal como aparece en el protocolo | De dónde salió | `Hemeroteca digital BNC` |
| `url` | Sí | Dirección completa de donde se tomó, o ruta del soporte físico | Dónde está el original | `https://…/1910/03/02/p3` |
| `fecha_documento` | Sí | ISO 8601: `AAAA-MM-DD`. Si solo se conoce el año, `AAAA`; si el mes, `AAAA-MM` | Cuándo fue producida | `1910-03-02` |
| `fecha_descarga` | Sí | ISO 8601 con hora: `AAAA-MM-DDThh:mm` | Cuándo fue tomada | `2027-03-14T18:22` |
| `escena` | Sí | Productor, género y situación, separados por punto y coma | Quién la produjo y en qué situación | `El Tiempo; nota; página 3, sección local` |
| `derechos` | Sí | Uno de: `dominio_publico`, `norma_oficial`, `licencia_abierta`, `uso_academico_con_cita`, `restringido` | Bajo qué régimen se usa | `dominio_publico` |
| `criterio_inclusion` | Sí | Número del criterio del protocolo. Si la pieza fue excluida, `E` más el número | Por qué está aquí | `2` |
| `hash_sha256` | Sí | 64 caracteres hexadecimales del archivo en `ruta_crudo` | Es el mismo archivo que se tomó | `9f86d08…` |
| `ruta_crudo` | Sí | Ruta relativa al archivo intacto | Dónde está lo que llegó | `crudo/P-0042.html` |
| `ruta_limpio` | No | Ruta relativa al archivo limpio en UTF-8 | Dónde está lo que se analiza | `limpio/P-0042.txt` |
| `notas` | No | Texto libre: duplicados, error de OCR estimado, dudas | Lo que no cabe en otra columna | `Duplicado exacto de P-0017; excluido` |

Columnas opcionales frecuentes que un proyecto puede añadir: `propuesta_modelo` (lo que un modelo propuso para `escena` o `criterio_inclusion`, al lado del valor decidido), `error_ocr` (porcentaje estimado sobre cien palabras), `unidad` (unidad de segmentación aplicada).

## Ejemplo

Tres filas de un catálogo sobre el caso demostrativo del curso. Las direcciones son ilustrativas.

| id | titulo | autor | fuente | url | fecha_documento | fecha_descarga | escena | derechos | criterio_inclusion | hash_sha256 | ruta_crudo | ruta_limpio | notas |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P-0001 | Sesión de la junta de ayer | Anónimo | Hemeroteca digital BNC | https://…/1910/03/02/p3 | 1910-03-02 | 2027-03-14T18:22 | El Tiempo; nota; página 3, sección local | dominio_publico | 2 | 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08 | crudo/P-0001.html | limpio/P-0001.txt | error_ocr 4 % sobre 100 palabras |
| N-0001 | Ley 23 de 1982 | Congreso de Colombia | Secretaría del Senado | http://www.secretariasenado.gov.co/senado/basedoc/ley_0023_1982.html | 1982-01-28 | 2027-03-14T18:40 | Congreso; ley; texto consolidado | norma_oficial | 4 | 2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae | crudo/N-0001.html | limpio/N-0001.txt | |
| P-0002 | Sesión de la junta de ayer | Anónimo | Hemeroteca digital BNC | https://…/1910/03/02/p3-bis | 1910-03-02 | 2027-03-14T18:23 | El Tiempo; nota; página 3, sección local | dominio_publico | E1 | 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08 | crudo/P-0002.html | | Duplicado exacto de P-0001; excluido; conserva id |

## Reglas de integridad

El cuaderno las aplica en una función que se ejecuta cada vez que el catálogo se regenera. Una fila que falla cualquiera de las cinco se lista; un catálogo con filas que fallan no entra al análisis.

| Regla | Qué comprueba | Qué se rompe si falla |
|---|---|---|
| 1 | Ningún campo obligatorio vacío | Una pregunta de la cadena de procedencia sin respuesta |
| 2 | Fechas en formato ISO; `fecha_descarga` posterior a `fecha_documento` | La pieza no se puede situar en el tiempo |
| 3 | `hash_sha256` igual al hash recalculado del archivo en `ruta_crudo` | No se sabe si el archivo es el que se tomó |
| 4 | Ningún `id` repetido | Dos piezas se citan igual |
| 5 | `criterio_inclusion` existe en el protocolo | La pieza entró sin razón escrita |

## Tabla de decisiones a mano

`decisiones.csv` tiene las columnas `id`, `escena`, `derechos`, `criterio_inclusion`, `notas`, `fecha_decision`, `propuesta_modelo`. El cuaderno la une al catálogo por `id`. Así las decisiones que ningún programa puede tomar quedan en un archivo con fecha que el programa lee, y el catálogo sigue siendo regenerable.

## Cómo se cita una pieza

En el informe, cada cita lleva el `id` y la posición en la tabla de unidades: `(P-0001, oración 12)`. Un lector va del `id` al catálogo, del catálogo a `ruta_crudo`, y del hash a la certeza de que lee lo mismo.
