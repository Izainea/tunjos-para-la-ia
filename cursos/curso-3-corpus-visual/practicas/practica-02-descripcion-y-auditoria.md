# Práctica 2. Descripción por capas con un modelo multimodal y auditoría de una muestra

Duración estimada: 5 horas, repartidas entre las sesiones de las semanas 4 y 5 y el trabajo autónomo.
Requisitos: 20 imágenes del catálogo que se puedan enviar a un modelo (públicas, de dominio público o sin personas identificables); acceso a un modelo multimodal de uso gratuito en su versión web, o el cuaderno de apoyo con la clave en `.env`; la plantilla `plantillas/ficha-semiotica.md`, sección "auditoría".
No requiere programar.

## Objetivo

Obtener descripciones de 20 imágenes con dos prompts, uno plano y uno por capas; guardar cada salida con sus metadatos; auditar una muestra de 15 descripciones por capas con la tabla de tres columnas; y escribir el resumen del sesgo del modelo sobre el corpus propio.

## Antes de la sesión de la semana 4

1. Elija las 20 imágenes. Compruebe en el catálogo que ninguna está marcada como sensible. Si su corpus entero es sensible, use para esta práctica una muestra de imágenes públicas del mismo tema o de un tema vecino, y dígalo.
2. Para tres de las 20, escriba su lectura propia: diez afirmaciones etiquetadas como en el taller de la semana 3. Guárdela sin mostrarla al modelo.
3. Abra una cuenta en un servicio con modelo multimodal gratuito, o configure el `.env` del cuaderno. Pruebe con una imagen.

## Describir en la semana 4

### Prompt plano

```
Describe esta imagen en detalle.
```

### Prompt por capas

```
Describe esta imagen en cuatro partes separadas, con estos títulos exactos y en este orden.

1. DENOTACIÓN. Solo lo que se ve: personas (cuántas, dónde en el cuadro, postura, vestimenta), objetos, lugar, disposición, texto visible transcrito literal. Sin interpretar, sin adjetivos de valor, sin nombrar instituciones ni lugares que no estén escritos en la imagen.

2. ÍNDICES MATERIALES. Tipo de imagen (fotografía, grabado, captura de pantalla, ilustración), señales de época o de proceso (grano, color, desenfoque, compresión), marcas de agua, bordes, recortes, interfaz visible.

3. SUPOSICIONES. Lo que supones y no ves: época probable, lugar probable, género de la imagen, función, qué está pasando. Para cada suposición, di en qué te basas y tu grado de confianza (alta, media, baja).

4. LO QUE NO PUEDES SABER. Lista lo que un lector local o el contexto de la fuente sabrían y tú no puedes inferir de la imagen.

Responde en español.
```

Adapte el prompt a su corpus en dos frases como máximo (por ejemplo, pida transcribir texto en una lengua específica). No añada en el prompt información sobre la imagen: el modelo debe describir sin pistas.

### Registro de cada salida

Por imagen y por prompt, guarde: id de la imagen, modelo y versión, fecha y hora, prompt literal, salida literal, y lo que pueda del costo (tokens, llamadas, tiempo). Vía manual: una fila por salida en una hoja de cálculo, con la salida pegada. Vía por programa: el bloque "describir" del cuaderno lo hace y escribe `descripciones.jsonl`.

### Comparar los dos prompts

Para las tres imágenes con lectura propia, llene la tabla de la semana 4: afirmaciones en la capa de denotación, cuántas habría escrito usted igual, suposiciones declaradas, cuántas rechazaría, qué declaró el modelo no saber. Anote en la bitácora qué cambió entre prompts: no la cantidad de detalle sino su clasificación.

### Presupuesto

Con el costo de las 40 salidas, extrapole al corpus completo: dinero, tiempo de ejecución, tiempo de lectura. Decida y escriba qué parte del corpus describirá con el presupuesto que tiene.

## Auditar en la semana 5

### Diseñar la muestra

Quince descripciones por capas, estratificadas por escena o periodo (cinco por estrato si hay tres estratos), incluyendo a propósito las imágenes que usted considera más locales. Escriba el criterio antes de auditar.

### El orden obligatorio

Para cada imagen de la muestra: primero mire la imagen y escriba tres frases propias; después lea la descripción del modelo. Nunca al revés. La auditoría hecha leyendo primero es una aprobación.

### La tabla de tres columnas

Una fila por afirmación del modelo. Las cuatro columnas de destino:

- No está: el modelo lo afirma y la imagen no lo muestra.
- No describe: la imagen lo muestra y el modelo no lo dice (se añade como fila con la afirmación que falta).
- Contexto local: está en la imagen, el modelo lo describe en parte o mal, y solo se juzga sabiendo del lugar, el periodo o la comunidad. Diga qué contexto haría falta.
- Aceptada: está y el modelo lo dice bien.

| Imagen | Afirmación del modelo | Capa en que la puso | Columna | Qué sé yo que el modelo no | Cómo lo sé |
|---|---|---|---|---|---|

### Cifras y resumen

Cuente las afirmaciones por columna sobre el total auditado. Declare que son cifras sobre la muestra, no tasas del corpus. Escriba el resumen del sesgo en un párrafo: qué tipo de cosas afirma el modelo sin base, qué tipo de cosas calla, qué tipo de cosas describe sin entender, con un ejemplo de cada una tomado de su corpus. Ese párrafo acompaña a todas las descripciones del corpus desde ahora.

### Variante con dos modelos o dos lenguas

Si tiene acceso a dos modelos, o repite con el prompt en inglés, audite cinco imágenes con ambos y compare la tercera columna. Ananthram et al. (2025) encuentran que la lengua del prompt cambia el sesgo sin eliminarlo; compruebe si pasa en su corpus.

## Después de la sesión de la semana 5

1. Describa con el prompt por capas la parte del corpus que el presupuesto permitió, por programa o a mano, y consolide todo en una tabla con una fila por imagen y una columna por capa.
2. Adjunte a la tabla el resumen del sesgo y las cifras de la muestra.
3. Marque en el registro de frontera visual las afirmaciones que aceptó sin poder decir cómo lo sabía.

## Qué se evalúa

La precisión de la auditoría, no la calidad de la descripción. Una descripción mediocre auditada afirmación por afirmación vale más que una brillante aprobada en bloque. La tercera columna se evalúa por si nombra el contexto que falta, no por su tamaño.
