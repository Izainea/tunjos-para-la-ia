---
name: curso
description: Escribe un curso completo del programa Tunjos para la IA (ocho semanas, plantillas, prácticas, mini apps, figuras, contenido de propuestas) con el agente autor-curso, siguiendo herramientas/GUIA-AUTORIA.md. Uso: /curso N "Título" [alcance en una o dos frases].
---

Escribe el curso indicado en `$ARGUMENTS` (número, título entre comillas y, si viene, el alcance).

1. Si no existe `cursos/curso-N-*/`, crea el andamio: `python herramientas/nuevo_curso.py N "Título" slug` (slug en minúsculas con guiones, derivado del título).
2. Lanza el subagente **autor-curso** (`.claude/agents/autor-curso.md`) con: número, título, slug, alcance, los productos esperados si se dieron, y la fila de `docente.md` que respalda el curso. Recuérdale que trabaja solo en esa carpeta, que la modalidad es híbrida, que fuera de `propuestas/` no se nombran universidades destinatarias, y que debe terminar con `python herramientas/verificar_curso.py cursos/curso-N-slug --capturas` en cero errores.
3. Al recibir el informe, ejecuta tú mismo el verificador una vez más y `python build.py`. Si hay errores, devuélvelos al agente con la lista exacta.
4. Responde en el chat con: ruta del curso, número de semanas, apps y figuras, resultado del verificador, referencias dudosas que el agente señaló, y qué queda pendiente. No pegues el contenido del curso.

Nunca publiques ni hagas push desde esta skill; eso es de `/publicar`.
