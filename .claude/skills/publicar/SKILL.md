---
name: publicar
description: Regenera y verifica el sitio, prepara el commit, y hace push a Izainea/tunjos-para-la-ia y activa GitHub Pages solo después de que Carlos confirme la lista exacta de acciones remotas. Uso: /publicar.
---

Publica el sitio del programa. La publicación es visible para terceros, así que sigue la regla global: ninguna acción remota sin confirmación explícita en el mismo turno.

1. Lanza el subagente **publicador** (`.claude/agents/publicador.md`) con la instrucción de ejecutar los pasos 1 a 6 y detenerse en el 7 devolviendo la lista exacta de acciones remotas pendientes (repositorio, rama, commits, creación de repositorio si aplica, activación de Pages).
2. Muestra esa lista a Carlos tal cual y pregunta si procede. No ejecutes nada remoto hasta tener el "sí" a esa lista.
3. Con el "sí", vuelve a lanzar o continúa el subagente para ejecutar el paso 7, verificar `gh api repos/Izainea/tunjos-para-la-ia/pages` y comprobar que la URL publicada responde.
4. Responde en el chat con la URL publicada, el hash enviado y cualquier acción que haya quedado sin hacer. Si Carlos no confirmó, deja constancia de que el commit local existe y nada salió de la máquina.
