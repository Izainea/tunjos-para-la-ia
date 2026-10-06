---
name: apps
description: Crea o repara las mini apps HTML y las figuras SVG de un curso con el agente constructor-apps, verificadas con esprima y capturas de Edge. Uso: /apps N [semana M] [descripción de la app o figura que falta].
---

Construye o repara instrumentos didácticos del curso indicado en `$ARGUMENTS`.

1. Localiza `cursos/curso-N-*/`. Lee `programa/semana-0M.md` si se indicó semana, o el syllabus si no, para saber qué mecanismo debe hacerse visible.
2. Lanza el subagente **constructor-apps** (`.claude/agents/constructor-apps.md`) con: ruta del curso, semana, qué debe mostrar cada app o figura (si no se dio, que lo derive del contenido de la semana), y la exigencia de verificar con esprima y captura de Edge y de embeber la app en la semana.
3. Ejecuta `python herramientas/verificar_curso.py cursos/curso-N-slug --capturas` y mira las capturas nuevas con `Read`.
4. Responde en el chat con la lista de apps y figuras, dónde quedaron embebidas, y el resultado de la verificación.
