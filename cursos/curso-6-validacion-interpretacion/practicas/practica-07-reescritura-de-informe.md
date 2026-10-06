# Práctica 7. Reescritura de un informe generado hasta convertirlo en aserciones propias

Duración estimada: 3 horas, de las cuales 1 en la sesión sincrónica.
Requisitos: un informe o borrador propio en el que un modelo haya redactado al menos un párrafo, o un párrafo de hallazgos que se le pide al modelo al empezar; la matriz de triangulación entregada en la semana 5; las plantillas `plantillas/declaracion-de-uso-de-ia.md` e `plantillas/informe-analitico.md`; la mini app `apps/asercion-sin-aserente.html` para calibrar.
No requiere programar.

## Objetivo

Convertir cada frase de un párrafo generado en una aserción con sujeto, base, criterio, alcance y procedencia, separar las frases que no se pueden firmar, y redactar la declaración de uso de IA del párrafo.

## Antes de la sesión

1. Si no tiene un párrafo generado, pídale al modelo uno a partir de su matriz. Ejemplo:

```
Esta es mi matriz de triangulación: [pegar la lectura por columnas]. Redacta
un párrafo de hallazgos de unas 200 palabras, en el registro de un artículo
de ciencias sociales, que presente los tres hallazgos principales.
```

2. Guarde el párrafo literal en el anexo. No lo corrija todavía.
3. Pídale al modelo, en la misma conversación, que justifique cada afirmación del párrafo. Guarde esa justificación también. La va a necesitar para ver qué forma tiene una justificación sin aserente.

## Durante la sesión (cuatro pasos)

### Paso 1. Marcar

Resalte en el párrafo todos los marcadores de autoridad que atribuyen la afirmación a algo que no puede afirmar: "los datos muestran", "el análisis revela", "es evidente que", "se observa que", "los resultados indican", "resulta claro", "como puede apreciarse", "la evidencia sugiere", "se concluye que". Cuente cuántos hay. La mini app lo hace sobre un párrafo de ejemplo y sirve para calibrar el ojo.

### Paso 2. Desarmar

Una fila por frase del párrafo, en la tabla de la semana:

| Frase original | Marcador | Verificado (sí, no, cómo) | Criterio | Aserente y alcance | Procedencia | Frase reescrita o retirada |
|---|---|---|---|---|---|---|

Para cada frase, responda en orden:

- Verificar. ¿Hay en la frase un dato, una cifra, una cita, una referencia? ¿Lo comprobó contra el material o la fuente? Si no puede comprobarlo ahora, anote "no" y siga; la frase no se firma hasta que se compruebe.
- Criterio. ¿Sobre qué patas de la matriz se sostiene lo afirmado? ¿Qué prueba pasó, de qué tipo? ¿Por qué esta categoría o lectura y no otra? Si la matriz no lo sostiene, anótelo.
- Aserente y alcance. ¿Quién afirma esto? ¿Desde qué trasfondo? ¿A qué material, período o contexto se limita? Escriba la frase con sujeto en primera persona y alcance explícito.
- Procedencia. ¿La frase es output aceptado tal cual, output corregido, output rechazado y reemplazado, o propia? Anótelo con una palabra.

### Paso 3. Reescribir o retirar

Escriba la frase nueva. Una frase reescrita tiene esta forma, con variaciones: "Sostengo que X, porque A y B convergen y la prueba C pasó; el modelo propuso X y lo acepté por D; lo afirmo para el material E". Es más larga que la original porque ahora tiene a alguien detrás.

Si al intentar la reescritura descubre que no puede sostener la frase, no la mejore: retírela y anote por qué. Las frases retiradas van a la sección 4 del informe, "Lo que cayó y lo que se retiró". Son el resultado esperado de la práctica y se evalúan.

### Paso 4. Declarar

Con la plantilla de declaración de uso de IA, llene al menos las secciones 2, 3 y 7 para este párrafo: qué se pidió, qué produjo, qué se aceptó, corrigió y rechazó, con qué criterio, y la tabla de procedencia de cada hallazgo. Adjunte las instrucciones literales.

## Después de la sesión

1. Compare la justificación que el modelo dio en el paso previo con las columnas de criterio que usted llenó. Anote qué tenía la justificación del modelo: conectores, forma de argumento, referencias a "los datos". Anote qué le faltaba: patas, prueba, alguien que responda. Esa comparación va a la bitácora.
2. Extienda la reescritura al resto del borrador del informe. No hace falta que todo el informe pase por la tabla, pero sí todo párrafo de hallazgos.
3. Entregue el borrador del informe con la sección de validación en el estado en que esté y la declaración de uso de IA. Se devuelve con observaciones antes de la entrega final.

## Qué se evalúa

En el borrador no se califica. En el informe final se evalúa que ningún hallazgo conserve marcadores sin aserente, que cada reescritura haya añadido base y criterio y no solo sujeto, que las frases retiradas estén en la sección 4 con razón, y que la declaración diga qué fue de quién. Una reescritura que cambia "los datos muestran" por "considero que" sin añadir nada se devuelve.

## Variante para grupos

Dos estudiantes intercambian párrafos reescritos y cada uno intenta formular, para cada frase del otro, la pregunta que un jurado haría. Las frases que no resisten la pregunta vuelven a la tabla. Es un ensayo de la semana 8.
