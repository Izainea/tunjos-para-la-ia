---
name: revisar
description: Audita un curso ya escrito contra la guía de autoría y el estilo del docente con el agente revisor-curso (estructura, estilo, referencias verificadas, términos prohibidos, apps con capturas) y aplica las correcciones si se pide. Uso: /revisar N [corregir].
---

Revisa el curso indicado en `$ARGUMENTS`.

1. Localiza `cursos/curso-N-*/`. Si no existe, dilo y detente.
2. Lanza el subagente **revisor-curso** (`.claude/agents/revisor-curso.md`) con la ruta del curso y la instrucción de corregir solo si `$ARGUMENTS` incluye `corregir`. Pídele la lista de hallazgos ordenada por bloqueo con ruta y línea, y la lista de referencias `NO-VERIFICADA`.
3. Si se corrigió, ejecuta `python herramientas/verificar_curso.py cursos/curso-N-slug` y `python build.py` para confirmar.
4. Responde en el chat con los hallazgos agrupados en bloqueantes, metodológicos y de estilo, las referencias no verificadas, y el antes y después del verificador si hubo corrección. Sin elogios ni narración del proceso.
