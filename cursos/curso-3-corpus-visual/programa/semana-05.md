# Semana 5. Auditoría de la descripción

## Pregunta de la semana

¿Cómo se sabe qué parte de una descripción producida por un modelo está en la imagen, qué parte no está y qué parte solo puede juzgar alguien que conoce el lugar de donde viene la imagen?

## Por qué esta semana

<p class="lede">Es la semana central del curso. Las descripciones de la semana 4 llegaron con la forma de una observación experta y el estudiante ya sabe que esa forma no garantiza nada. Lo que falta es un procedimiento para decidir, afirmación por afirmación, qué se acepta. El procedimiento es una auditoría por muestra con tres columnas: lo que el modelo afirma y no está en la imagen, lo que está en la imagen y el modelo no describe, y lo que está pero solo se lee con contexto local. Las dos primeras columnas miden el rendimiento; la tercera mide otra cosa: la precomprensión ajena. Pouget et al. (2024) y Schneider et al. (2025) muestran con cifras que los modelos de visión y lenguaje conocen mejor las culturas occidentales y mejor lo tangible que lo intangible. La semana convierte esos resultados en una práctica sobre el corpus propio.</p>

## Contenido de la sesión

1. Auditar es comparar la descripción con la imagen bajo una gramática fija. Sin gramática, la auditoría se reduce a "me parece bien". Con la gramática de la semana 3, cada frase de la descripción es una afirmación de tipo conocido y se puede confrontar: una denotación se confronta mirando; un índice, conociendo el proceso; un símbolo, participando de la convención. La tabla de tres columnas del curso ordena el resultado de esa confrontación.

2. La primera columna recoge lo que el modelo afirma y no está. Es el infortunio más visible: la cuarta figura que no existe, el uniforme que se atribuye a una institución, el "celebración" sobre una mesa con botellas. La hipótesis de trabajo del curso es que este tipo de error se concentra en la capa de suposiciones y se cuela en la de denotación cuando el prompt no las separa bien; el prompt por capas reduce el daño sin eliminarlo. El curso no dispone de una cifra validada para el corpus del caso y no la inventa: en la sesión el docente audita en vivo descripciones reales del caso, y la cifra que se obtiene es la de esa muestra y así se declara.

3. La segunda columna recoge lo que está y el modelo no describe. Es más difícil de ver, porque exige que el auditor haya mirado la imagen antes de leer la descripción, y por eso el taller de la semana 1 y el esquema ciego existen. Lo que el modelo omite con regularidad en el caso: texto visible en español con ortografía no estándar, objetos de uso local sin nombre en inglés, gestos y disposiciones corporales que un lector local lee como señal de clase o de región, y marcas del dispositivo (logotipo del medio, marca de agua, recorte de miniatura).

4. La tercera columna es la que da sentido al curso dentro del programa. Recoge lo que está en la imagen, el modelo describe en parte, y solo se juzga con contexto local: que la fachada es de un barrio concreto, que el vestuario cita una estética que una telenovela hizo reconocible, que el altar de la foto es de un santo popular con un uso específico. Aquí no hay error del modelo en sentido estricto: hay una descripción hecha desde una forma de vida en que esos signos no significan. Schneider et al. (2025) encuentran con un banco de pruebas sobre 144 países que los modelos conocen mejor lo tangible (comida, vestuario) que lo intangible (rituales, prácticas), y que el sesgo hacia lo occidental atraviesa modelos y tareas.<sup class="mark">a</sup>

<aside class="glosa"><span class="mark">a</span> GIMMICK (Schneider, Holtermann, Biemann y Lauscher, 2025) evalúa 20 modelos de visión y lenguaje y 11 de solo texto sobre 728 eventos o facetas culturales. Pouget et al. (2024) muestran, para modelos contrastivos, que filtrar los datos de entrenamiento a pares imagen-texto en inglés degrada la comprensión de otras culturas sin que lo capturen las métricas habituales.</aside>

| Rendimiento | Precomprensión |
|---|---|
| Se mide: afirmaciones correctas sobre afirmaciones totales. | No se mide con una tasa: se localiza y se nombra. |
| Mejora con mejores modelos y mejores prompts. | Cambia con los datos de entrenamiento y con la lengua, no con el tamaño. |
| Lo juzga cualquiera que mire la imagen. | Lo juzga quien participa de la forma de vida que produjo la imagen. |
| Columnas uno y dos de la auditoría. | Columna tres. |
| *Un modelo con 95 % de aciertos puede seguir sin ver lo que importa.* | *Lo que no ve no es un error: es una ausencia de mundo.* |

5. La muestra se diseña, no se improvisa. Quince descripciones no bastan para estimar una tasa del corpus, pero bastan para encontrar los tipos de error y para calibrar al auditor. El curso recomienda una muestra estratificada: cinco imágenes por escena o por periodo, incluyendo a propósito las que el estudiante considera más locales.<sup class="mark">b</sup> Aquí la auditoría es diagnóstico. En [*Validación e interpretación*](../../curso-6-validacion-interpretacion/README.md), el curso del programa dedicado a validar lo ya configurado, se distinguen tres sentidos de validar, comprobar la corrección del resultado, justificar el proceso y responder por lo afirmado, y se enseña a triangular con el modelo como segundo codificador; una auditoría como esta se convierte allí en una pieza del protocolo de validación del proyecto entero. Lo que sí se exige desde ya es que el tamaño y el criterio de la muestra queden escritos.

<aside class="glosa"><span class="mark">b</span> Estratificar es dividir el corpus en grupos conocidos (por escena, por periodo) y tomar de cada uno una parte, para que la muestra no quede dominada por el grupo más grande. En el caso demostrativo, el periodo 2000 a 2025 tiene 699 de 1.830 imágenes; una muestra al azar sería en un 38 % de ese periodo y casi nunca tocaría el siglo XIX.</aside>

6. El resumen del sesgo es un párrafo, no una tabla. Después de auditar, el estudiante escribe qué tipo de cosas afirma el modelo sin base, qué tipo de cosas calla y qué tipo de cosas describe sin entender, con un ejemplo de cada una. Ese párrafo es la declaración de límites que acompaña a todas las descripciones del corpus cuando se usan en la semana 6 para preclasificar. Una descripción sin declaración de límites es una descripción que alguien va a tomar por observación.

<figure class="wide">
  <svg viewBox="0 0 680 290" style="width:100%;max-width:42rem;height:auto;display:block" role="img" aria-label="Frontera entre lo que el modelo describe y lo que el investigador decide. Arriba, la zona del modelo: denotación, índices visibles, suposiciones declaradas. Una línea roja punteada marca la frontera. Abajo, la zona del investigador: las tres columnas de la auditoría (no está, no describe, requiere contexto local), el resumen del sesgo y la decisión de qué se acepta. Una flecha de retroalimentación vuelve al prompt.">
    <style>.bx{fill:var(--surface);stroke:var(--rule);stroke-width:1.2} .t{font-family:var(--text);font-size:12.5px;fill:var(--ink)} .s{font-family:var(--text);font-size:11px;fill:var(--muted)} .k{font-family:var(--mono);font-size:9.5px;letter-spacing:.08em;fill:var(--muted)} .kf{font-family:var(--mono);font-size:9.5px;letter-spacing:.08em;fill:var(--c-fil)} .ar{stroke:var(--muted);stroke-width:1.3;fill:none} .fr{stroke:var(--c-fil);stroke-width:1.6;stroke-dasharray:6 5;fill:none} .ah{fill:var(--muted)} .c1{fill:var(--c-fil)} .c2{fill:var(--c-app)} .c3{fill:var(--accent)}</style>
    <defs><marker id="s5-ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 1L9 5L0 9z" class="ah"/></marker></defs>
    <rect x="40" y="20" width="600" height="86" rx="3" class="bx"/>
    <text x="52" y="38" class="k">MODELO · configura la descripción</text>
    <text x="52" y="62" class="t">Denotación</text><text x="52" y="78" class="s">qué hay, dónde, texto</text>
    <text x="250" y="62" class="t">Índices visibles</text><text x="250" y="78" class="s">tipo, grano, marcas</text>
    <text x="450" y="62" class="t">Suposiciones declaradas</text><text x="450" y="78" class="s">época, lugar, género</text>
    <text x="52" y="98" class="s">Rápido, a escala, en el género de las leyendas con que fue entrenado.</text>
    <path class="fr" d="M20 130 L660 130"/>
    <text x="660" y="124" text-anchor="end" class="kf">FRONTERA</text>
    <path class="ar" d="M340 106 L340 150" marker-end="url(#s5-ah)"/>
    <rect x="40" y="152" width="600" height="118" rx="3" class="bx"/>
    <text x="52" y="170" class="k">INVESTIGADOR · audita y decide</text>
    <circle cx="60" cy="194" r="5" class="c1"/><text x="72" y="198" class="t">Afirma y no está</text><text x="72" y="212" class="s">se rechaza; se cuenta</text>
    <circle cx="260" cy="194" r="5" class="c2"/><text x="272" y="198" class="t">Está y no describe</text><text x="272" y="212" class="s">se añade; se cuenta</text>
    <circle cx="460" cy="194" r="5" class="c3"/><text x="472" y="198" class="t">Requiere contexto local</text><text x="472" y="212" class="s">lo pone quien conoce el lugar</text>
    <text x="52" y="242" class="t">Resumen del sesgo</text><text x="190" y="242" class="s">qué afirma sin base, qué calla, qué describe sin entender; va con cada descripción del corpus.</text>
    <text x="52" y="262" class="s">Lo que cruza la frontera hacia arriba es un prompt corregido; lo que cruza hacia abajo es una propuesta, nunca una observación.</text>
    <path class="ar" d="M640 230 C 672 230 672 60 642 60" marker-end="url(#s5-ah)"/>
  </svg>
  <figcaption><b>Figura 5.</b> La frontera entre lo que el modelo describe y lo que el investigador decide. Hay que ver que la tercera columna no es un error del modelo sino el lugar donde la precomprensión ajena se hace visible, y que solo un lector situado puede llenarla.</figcaption>
</figure>

7. La mini app de la semana reproduce la auditoría sobre cuatro imágenes sintéticas con cartela. Para cada una, la app muestra una "descripción de modelo" escrita para la ocasión, con errores de los tres tipos, y pide marcar cada frase en una de las tres columnas. Al final resume el sesgo con las marcas del estudiante y las compara con las del docente. Las discrepancias en la tercera columna son las más instructivas: ahí no hay respuesta correcta sin decir desde dónde se mira.

<iframe class="app" src="apps/auditoria-descripcion.html" title="Auditoría de una descripción de modelo sobre cuatro imágenes sintéticas con cartela" loading="lazy"></iframe>

## IA y exigencia

Esta semana al modelo no se le pide nada nuevo: se auditan sus descripciones de la semana anterior. Se le exige al estudiante que audite 15 descripciones con la tabla de tres columnas, que escriba el resumen del sesgo con un ejemplo por columna, y que pueda explicar sin la tabla por qué la tercera columna no es un error de rendimiento y qué haría falta para que el modelo la llenara. Si usa un segundo modelo para auditar al primero, declara que eso desplaza la frontera, no la elimina.

## Lecturas

**Central**

- Pouget, A., Beyer, L., Bugliarello, E., Wang, X., Steiner, A. P., Zhai, X. y Alabdulmohsin, I. (2024). "No Filter: Cultural and Socioeconomic Diversity in Contrastive Vision-Language Models". *Advances in Neural Information Processing Systems*, 37. https://arxiv.org/abs/2405.13777
- Schneider, F., Holtermann, C., Biemann, C. y Lauscher, A. (2025). "GIMMICK: Globally Inclusive Multimodal Multitask Cultural Knowledge Benchmarking". *Findings of the Association for Computational Linguistics: ACL 2025*. https://aclanthology.org/2025.findings-acl.500/

**Complementaria**

- Nayak, S. et al. (2024). "Benchmarking Vision Language Models for Cultural Understanding". *Proceedings of EMNLP 2024*. https://aclanthology.org/2024.emnlp-main.329/
- Ananthram, A. et al. (2025). "See It from My Perspective: How Language Affects Cultural Bias in Image Understanding". *ICLR 2025*. https://arxiv.org/abs/2406.11665
- Zainea, C. I. (2026). "Agencia sin imputación: por qué «la máquina no comprende» no cierra la discusión". https://izainea.github.io/blog/agencia-sin-imputacion/

## Guía de lectura

- Pouget et al. muestran que el filtro a inglés mejora las métricas habituales y empeora la comprensión cultural, y que las dos cosas no se ven en la misma prueba. *¿Qué prueba habría que diseñar para que el sesgo sobre su corpus fuera visible, y qué imágenes entrarían en ella?*
- Schneider et al. distinguen lo tangible de lo intangible y encuentran que los modelos saben menos de lo segundo. *Haga la lista de lo intangible en su corpus: prácticas, rituales, usos. ¿Cuánto de eso aparece en las descripciones que obtuvo?*
- Ananthram et al. encuentran que el idioma del prompt reduce el sesgo sin eliminarlo. *Repita una descripción con el prompt en español y en inglés. ¿Qué cambia en la tercera columna?*
- Nayak et al. encuentran que los modelos aciertan más en vestuario y rituales que en comida y bebida, y mucho menos en África que en Norteamérica. *¿Qué facetas de su corpus se parecen a las que los modelos conocen, y cuáles no están en ningún banco de pruebas?*
- En la entrada sobre agencia sin imputación, la prefiguración del modelo se llama ajena. *¿Qué significa, para su corpus, que el modelo describa desde una precomprensión que no es la de la comunidad que produjo las imágenes?*

## Taller de la segunda hora

Auditoría de 15 descripciones por capas de la práctica 2, con la muestra estratificada que el estudiante diseñó. Una fila por afirmación auditada; las que se aceptan sin más también se cuentan.

| Imagen | Afirmación del modelo | Capa en que la puso | Columna (no está / no describe / contexto local / aceptada) | Qué sé yo que el modelo no | Cómo lo sé |
|---|---|---|---|---|---|

Al final, el resumen del sesgo en un párrafo, con un ejemplo por columna, y la cifra de afirmaciones por columna sobre el total auditado, declarando que es sobre la muestra.

Variante para grupos. Dos estudiantes auditan las mismas cinco descripciones por separado y comparan columna por columna. Las discrepancias en la primera columna se resuelven mirando; las de la tercera no siempre se resuelven, y esas se anotan con la posición de cada uno.

## Guion de la sesión

| Minuto | Momento | Qué hace el docente | Qué hace el estudiante | Material |
|---|---|---|---|---|
| 0 a 15 | Apertura | Audita en vivo una descripción del caso, frase por frase, con la figura 5 | Propone la columna de cada frase antes de que el docente la diga | Figura 5, una descripción del caso |
| 15 a 35 | Las tres columnas | Expone con ejemplos del caso; distingue rendimiento de precomprensión | Nombra un caso propio por columna | Pizarra |
| 35 a 50 | La evidencia | Resume Pouget et al. y Schneider et al. con sus cifras | Ubica su corpus respecto de lo tangible e intangible | Lecturas |
| 50 a 60 | Mini app | Muestra una de las cuatro imágenes y su descripción | Marca las frases; discute la tercera columna | Mini app |
| 60 a 105 | Auditoría | Acompaña; cuestiona las aceptaciones | Audita 15 descripciones con la tabla | Tabla del taller |
| 105 a 115 | Resumen | Lee dos resúmenes de sesgo en voz alta | Compara con el suyo | Bitácoras |
| 115 a 120 | Cierre | Fija la entrega de la semana 6 | Anota qué le falta | Syllabus |

Notas para el docente. Suele fallar que la auditoría se haga leyendo la descripción antes de mirar la imagen; obligar al orden inverso. Suele fallar que todo lo dudoso vaya a la tercera columna; la tercera columna exige nombrar qué contexto haría falta, no solo "no sé". Y suele fallar que la cifra de la muestra se presente como tasa del corpus; corregirlo en la sesión y en la rúbrica.

## Bitácora

Registre la tabla de auditoría completa, el diseño de la muestra, el resumen del sesgo y las cifras por columna. Marque las afirmaciones que aceptó sin poder decir cómo lo sabía. Esas filas son el material del registro de frontera visual de la semana 7.

## Para la próxima semana

Leer Rincón (2009) y el capítulo 4 de Banks (2010). Tener las descripciones por capas de todo el corpus propio, o de la parte que el presupuesto permitió, en una tabla con una fila por imagen y una columna por capa, para preclasificarlas en la semana 6. Es la segunda entrega.
