# Ficha de patrón

**Estudiante:**
**Corpus (una frase: qué es, cuántas unidades, de qué fechas):**
**Versión:** semana 3 (representación y agrupamiento) / semana 8 (ficha de hipótesis sobre un patrón propio)
**Modelos de lenguaje usados y para qué (código, nombres propuestos, lecturas preliminares):**

## Para qué sirve esta ficha

Un patrón que sale de un método es un candidato. Esta ficha lo acompaña desde que aparece hasta que se convierte en hipótesis o se descarta como artefacto. Las secciones 1 a 4 se llenan en la semana 3; la sección 5 se añade en la semana 8 sobre el patrón elegido. Nada de lo que aquí se escribe lo produce el método: el método produce el patrón y los números de la sección 3.

## 0. Lo que esperaba antes de correr el método

Escríbalo antes. Después ya no podrá. Qué grupos, qué relaciones o qué tendencias creía que iba a encontrar, y por qué.

**Esperaba:**

**Porque (trasfondo: teoría, lecturas, lo que conozco del material):**

## 1. Representación

| | |
|---|---|
| Representación usada (bolsa de palabras, TF-IDF, embeddings de texto, embeddings de imagen, anotaciones) | |
| Modelo, versión y dimensión, si aplica | |
| Qué conserva esta representación que importa para mi pregunta | |
| Qué pierde que también importa | |
| Segunda representación con la que comparé | |

Lectura de vecinos (semana 2): diez documentos con sus cinco vecinos más cercanos, marcando los que tienen sentido y los que no.

| Documento | Vecinos con sentido | Vecinos sin sentido | Choque con la precomprensión del modelo |
|---|---|---|---|

## 2. El patrón

| | |
|---|---|
| Instrumento (agrupamiento, red, serie, temas) | |
| Parámetros usados (k, semilla, umbral, ventana, K; todos) | |
| Descripción del patrón en una frase que no lo interprete | |
| Dónde está la vista (archivo, panel del tablero) | |

## 3. Prueba de estabilidad

Un patrón es candidato si sobrevive a mover el parámetro. Llene una fila por grupo, comunidad, ruptura o tema.

| Elemento | Tamaño | Sobrevive a cambiar la semilla (Jaccard medio) | Sobrevive a k±1, umbral vecino o ventana vecina (Jaccard medio) | Sobrevive a otra representación (Jaccard) | ¿Candidato o artefacto? |
|---|---|---|---|---|---|

Índice de Rand ajustado entre particiones completas, cuando aplique:

| Comparación | Índice |
|---|---|
| Semilla 1 contra semillas 2 a 5 | |
| k contra k−1 | |
| k contra k+1 | |
| Representación A contra B | |

**Elementos que no sobrevivieron y qué creo que dicen sobre el método, la representación o el corpus:**

## 4. Lectura

Una entrada por candidato. El nombre es una hipótesis; los contraejemplos son su prueba.

| Candidato | Nombre propuesto por mí | Nombre propuesto por el modelo de lenguaje | Tres miembros que el nombre explica | Tres miembros que el nombre no explica | Decisión: adopto, corrijo, rechazo |
|---|---|---|---|---|---|

**Comparación con lo que esperaba (sección 0): qué coincidió, qué no, qué me sorprendió.**

## 5. Ficha de hipótesis sobre un patrón propio (semana 8)

**Patrón elegido (de la sección 2 o de otra entrega):**

**Desde qué trasfondo sorprende. Qué esperaba, qué teoría o qué conocimiento del material contradice:**

**¿Le sorprendería a un investigador con otro trasfondo? ¿Por qué?**

**Descarte de artefactos.** Diga qué prueba hizo para descartar cada tipo.

| Tipo de artefacto | Prueba hecha | Resultado |
|---|---|---|
| Del método (depende de k, umbral, ventana, K, semilla) | | |
| De la representación (aparece con una y no con otra) | | |
| Del corpus (coincide con un cambio en la recolección o en la composición) | | |
| De la vista (lo produce la escala, el color, la proyección o el dibujo) | | |

**Hipótesis.** Si A fuera verdad, el patrón sería natural. A es:

**Hipótesis alternativas consideradas (al menos una propia y una del modelo de lenguaje):**

| | Hipótesis | Origen | Explica el patrón | Es verificable, y cómo | Economía: costo de probar, rendimiento, no cierra otras vías | Plausibilidad en mi trasfondo |
|---|---|---|---|---|---|---|
| H1 | | | | | | |
| H2 | | | | | | |
| H3 | | | | | | |

**Persigo la hipótesis:**

**Porque:**

**Si la hipótesis la formuló el modelo, por qué la decisión es mía y qué costo asumo:**

**Qué cálculo o qué dato nuevo necesito para probarla, y cuánto cuesta obtenerlo:**

## 6. Declaración

Declaro que la representación, los parámetros y las pruebas de esta ficha son reproducibles con el código y las semillas del anexo, y que la lectura y la hipótesis son mi decisión. Donde usé un modelo de lenguaje lo he indicado, y respondo por lo que adopté.

Firma y fecha:
