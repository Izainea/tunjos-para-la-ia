# Registro de frontera computacional

**Estudiante:**
**Corpus:**
**Periodo que cubre el registro (semanas):**
**Entorno: versiones de Python y de las bibliotecas, modelo de embeddings y versión, semillas (anexar el archivo de entorno del cuaderno):**
**Modelos de lenguaje usados, versión y fecha; prompts en anexo:**

## Para qué sirve este registro

No es un informe de uso de herramientas. Es la evidencia de que usted sabe, paso a paso, qué calculó la máquina y qué leyó usted. Lo que calculó la máquina es reproducible: con los mismos datos, el mismo código y la misma semilla, cualquiera obtiene lo mismo, y su validación recae sobre el registro del proceso. Lo que leyó usted es imputable: lleva su nombre y responde ante quien lo discuta. El registro tiene una fila por paso y en cada fila dice de qué lado de la frontera cae.

## El registro

Una fila por paso. Si un paso tuvo varias corridas con distintos parámetros, una fila por corrida o una fila con el rango y el resultado de la prueba de estabilidad.

| Paso | Semana | Qué hizo la máquina (cálculo, con parámetros y semilla) | Qué propuso el modelo de lenguaje, si intervino (literal o resumen fiel) | Qué decidí yo (elegir parámetro, nombrar, leer, aceptar, corregir, rechazar) | Criterio de mi decisión | ¿Reproducible o imputable? | ¿Quién responde si está mal? |
|---|---|---|---|---|---|---|---|
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |

Pasos habituales, para no olvidar ninguno: elegir el corpus y su estado; elegir la representación y el modelo; calcular vectores; leer vecinos; elegir k y semillas; agrupar; probar estabilidad; nombrar grupos; definir unidad y arista; construir el grafo; elegir umbrales; calcular medidas y comunidades; leer puentes; elegir periodo y normalización; suavizar; detectar rupturas; elegir K; modelar temas; nombrar temas; elegir escalas y colores; escribir pies; elegir el patrón; formular la hipótesis.

## Los casos difíciles

Señale al menos dos pasos en que fue difícil decir si el resultado era de la máquina o suyo. Ejemplos frecuentes: un parámetro que eligió "porque se veía mejor"; un nombre de grupo que el modelo de lenguaje propuso y que usted adoptó sin leer todos los miembros; un umbral que fijó para que apareciera la comunidad que esperaba. Explique por qué fue difícil. Esos casos son los más valiosos del registro.

## Adopciones sin criterio

Revise el registro y marque los pasos en que aceptó una propuesta del modelo de lenguaje, o un valor por defecto de una biblioteca, sin un criterio que pueda nombrar. No los borre: anótelos aquí. Diga qué habría hecho falta para que la aceptación fuera una decisión.

| Paso | Qué acepté | Qué habría hecho falta |
|---|---|---|

## Artefactos encontrados

Patrones que aparecieron y no sobrevivieron a las pruebas, con el tipo de artefacto y la prueba que lo mostró.

| Patrón | Tipo (método, representación, corpus, vista) | Prueba que lo mostró | Qué enseña sobre el instrumento o el corpus |
|---|---|---|---|

## Balance

**Pasos que cualquiera puede reproducir con el anexo, sin mí:**

**Pasos que exigieron mi conocimiento del corpus, del campo o de la comunidad que produjo el material:**

**Pasos por los que respondo yo y nadie más:**

**Dónde está la frontera en este proyecto, y si coincide con la que tracé en el mapa inferencial de [*Las tres inferencias*](../../curso-1-tres-inferencias/README.md), si lo hice. En ese mapa cada paso del flujo de investigación queda clasificado como deductivo, inductivo o abductivo, con la frontera entre lo que verifica la máquina y lo que responde el investigador:**

**Qué cambia de mi flujo de trabajo después del curso:**

Firma y fecha:
