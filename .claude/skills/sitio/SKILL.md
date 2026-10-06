---
name: sitio
description: Regenera el sitio del programa en docs/ con build.py, comprueba términos prohibidos, enlaces y apps, captura la portada con Edge y deja el commit local listo. No publica. Uso: /sitio.
---

Regenera y verifica el sitio sin publicarlo.

1. Lanza el subagente **publicador** (`.claude/agents/publicador.md`) con la instrucción explícita de detenerse después del commit local (pasos 1 a 5 de su procedimiento), sin ninguna operación remota.
2. Al recibir el informe, confirma con `git log --oneline -3` y `git status` que el commit existe y el árbol está limpio.
3. Responde en el chat con: páginas generadas, cursos publicados y excluidos, resultado de las comprobaciones de términos y enlaces, capturas miradas, y el hash del commit. Indica que publicar requiere `/publicar` y confirmación.
