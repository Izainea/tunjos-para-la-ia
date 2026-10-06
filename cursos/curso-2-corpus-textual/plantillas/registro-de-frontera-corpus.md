# Registro de frontera del corpus

**Estudiante:**
**Proyecto:**
**Modelos usados, versiones y fechas:**
**Instrucciones versionadas (archivos):**
**Registro de llamadas (archivo `.jsonl` con fecha, modelo, instrucción y respuesta):**

## Para qué sirve este registro

No es un informe de uso de IA. Es la evidencia de que usted sabe, operación por operación, dónde terminó la máquina y dónde empezó usted en la construcción de su corpus. Un registro bien hecho permite que otra persona reconstruya qué parte del corpus es salida de un sistema y qué parte es decisión suya, por la que responde. Se llena a lo largo del curso y se entrega completo con el informe de la semana 8.

## Operaciones del curso con la máquina

Una fila por operación. Si una operación tuvo varias iteraciones, una fila por iteración. La columna "tipo de inferencia" usa las tres categorías que [*Las tres inferencias*](../../curso-1-tres-inferencias/README.md), el curso de fundamentos del programa, distingue por su régimen de validez, con la conclusión de que una máquina puede verificar las dos primeras y solo un investigador puede responder por la tercera: D (deductiva: se sigue por forma), I (inductiva: generaliza sobre lo que hay), A (abductiva: introduce una hipótesis o categoría nueva).

| Semana | Operación | Qué propuso el modelo (literal o resumen fiel) | Tipo de inferencia | Qué decidí (aceptar, corregir, rechazar, reformular) | Criterio de mi decisión | ¿Quién responde si está mal? |
|---|---|---|---|---|---|---|
| 1 | Lista de tipos de documento y fuentes | | | | | |
| 2 | Corrección de errores de Python | | | | | |
| 3 | Función de descarga | | | | | |
| 4 | Valores de `escena` y `criterio_inclusion` para diez piezas | | | | | |
| 5 | Expresiones regulares de limpieza | | | | | |
| 5 | Corrección de OCR en un fragmento | | | | | |
| 6 | Palabras para dominios léxicos | | | | | |
| 6 | Interpretación de una lista de colocaciones | | | | | |
| 7 | Etiquetas sobre la muestra auditada | | | | | |
| 8 | Borrador de la declaración de datos | | | | | |

## La auditoría de la semana 7 en detalle

**Instrucción (versión):**
**Muestra (tamaño y regla de selección):**
**Proporción de acuerdo:**
**Kappa:**

| Tipo de desacuerdo | Cuántos | Ejemplo (id de la unidad) |
|---|---|---|
| El modelo generalizó desde su entrenamiento algo que aquí significa otra cosa | | |
| El modelo forzó una categoría cuando ninguna aplicaba | | |
| El modelo ignoró un contexto local que yo conozco | | |
| El modelo leyó literalmente una ironía o una fórmula | | |
| Yo me equivoqué | | |
| Otro | | |

**Decisión** (aceptar con tasa declarada, corregir la instrucción y repetir, rechazar) **y razón:**

**Si acepté, qué categorías quedan marcadas como problemáticas en el informe:**

## Lo que no se le pidió al modelo

Confirme que ninguna de estas dos cosas ocurrió y, si ocurrió, explique cómo se corrigió:

- Decidir qué unidades entran al corpus.
- Producir un texto que luego se citó como fuente.

## Los casos difíciles

Señale al menos una operación en que la distinción entre lo que propuso el modelo y lo que decidió usted fue difícil de trazar. Explique por qué. Esos casos son los más valiosos del registro.

## Aceptaciones acríticas

Revise el registro y marque las operaciones en que aceptó la propuesta del modelo sin un criterio que pueda nombrar. No las borre: anótelas. Diga qué habría hecho falta para que la aceptación fuera una decisión.

## Balance

**Operaciones que la máquina podría haber verificado sola** (por ejemplo, el hash, las reglas de integridad):

**Operaciones que exigieron mi conocimiento del tema, del periodo o de las fuentes:**

**Operaciones por las que respondo yo y nadie más:**

**Dónde está la frontera en la construcción de este corpus, en una frase:**
