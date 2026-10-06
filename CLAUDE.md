# Tunjos para la IA · programa de microcredenciales

Repositorio del programa de siete microcredenciales de Carlos Isaac Zainea Maya sobre razonamiento, validación e inteligencia artificial en ciencias sociales y humanidades. Aquí se escriben los cursos, se generan sus páginas y se preparan las propuestas para convocatorias. Idioma de todo: español de Colombia.

## Fuentes de verdad

- `herramientas/GUIA-AUTORIA.md` define estructura, didáctica, verificación y estilo de cada curso. Toda escritura de material la cumple; ante una duda, prevalece la guía.
- `docente.md` es el perfil público del docente y la evidencia de idoneidad por curso. Se construye desde su hoja de vida; no se le añaden méritos que no estén documentados.
- `cursos/curso-1-tres-inferencias/` es el modelo de forma de los demás cursos.
- Los modelos de estilo están fuera del repositorio: las entradas de blog en `../izainea.github.io/src/content/blog/` y el anteproyecto en `../Doctorado Filosofía/Coloquio/scripts/contenido_proyecto.md`.

## Estructura

```
cursos/curso-N-slug/      README, programa/ (syllabus, semana-01..08, evaluacion, bibliografia), plantillas/, practicas/, apps/, propuestas/
docs/                     sitio generado por build.py (GitHub Pages, carpeta docs de la rama main). No se edita a mano.
herramientas/             GUIA-AUTORIA.md, app-base.html, generar_propuestas.py, verificar_curso.py, nuevo_curso.py
plantillas-externas/      plantillas de convocatorias de terceros. Local, no versionada.
.claude/agents, skills    agentes y skills de este repositorio (ver abajo)
build.py, docente.md, README.md, LICENSE
```

## Reglas del repositorio

- Las carpetas `propuestas/` y `plantillas-externas/`, y todo `.docx` y `.xlsx`, están en `.gitignore`. Nunca se versionan ni se publican: contienen nombres de universidades destinatarias y datos personales.
- Fuera de `propuestas/` está prohibido nombrar universidades destinatarias, la palabra "convocatoria", "PEEC" o "Qualtrics". `herramientas/verificar_curso.py` lo comprueba. La biografía del docente sí puede nombrar las instituciones donde estudió y trabajó.
- Modalidad de todos los cursos: híbrida. La virtual es alternativa y se dice así.
- No se afirma ninguna tesis ontológica sobre lo que la máquina no puede hacer. El programa trabaja la pregunta epistémica: quién valida y cómo.
- Las referencias bibliográficas se incluyen solo si son verificables (autor, año, título, revista o editorial, enlace o DOI). Si hay duda, se omite y se anota en el informe de trabajo.
- Identidad git de este repositorio: `izainea <cizaineam@gmail.com>`. Ningún `Co-Authored-By` ni mención a Claude en commits, PR o páginas.
- `git push`, la creación de repositorios, la activación de GitHub Pages y cualquier publicación requieren confirmación explícita de Carlos para esa acción concreta, en el mismo turno, con la lista exacta de lo que se va a hacer. La cuenta activa de `gh` debe ser `Izainea`; comprobar con `gh auth status` antes de cualquier operación remota.
- Los archivos abiertos en Office no se pueden sobrescribir en Windows; el generador escribe entonces con sufijo `-nuevo` y lo informa.
- No crear carpetas nuevas de primer nivel sin proponerlo antes.

## Comandos

```
python build.py                                              genera docs/ para todos los cursos completos
python herramientas/verificar_curso.py cursos/curso-N-slug   verifica estructura, estilo, enlaces, apps (añadir --capturas para Edge)
python herramientas/verificar_curso.py --todos --capturas
python herramientas/generar_propuestas.py cursos/curso-N-slug   genera propuestas/propuesta-uniandes.docx y propuesta-unal.xlsx
python herramientas/nuevo_curso.py 8 "Título" slug           andamio de un curso nuevo
```

Verificación de páginas con Edge sin interfaz: `"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --headless=new --screenshot=<png> --window-size=1400,1000 "file:///<ruta codificada>"`. Sintaxis JS con `esprima` desde Python.

## Agentes y skills

| Skill | Agente | Qué hace |
|---|---|---|
| `/curso N "Título" [alcance]` | `autor-curso` | Escribe un curso completo según la guía, con apps y figuras, y lo verifica |
| `/revisar N` | `revisor-curso` | Audita un curso: estructura, estilo, referencias, apps con capturas; propone y aplica correcciones |
| `/apps N [semana]` | `constructor-apps` | Crea o repara mini apps y figuras SVG de un curso |
| `/propuestas N` | `propuestas-curso` | Rellena `propuestas/contenido.py` desde el material del curso y genera los dos formatos |
| `/sitio` | `publicador` | Regenera docs/, comprueba términos prohibidos y enlaces, captura la portada, deja el commit listo |
| `/publicar` | `publicador` | Lo anterior y, solo con confirmación explícita, push y GitHub Pages |

Los agentes escriben solo dentro de la carpeta del curso que atienden. Sus informes finales son breves: archivos creados o modificados, resultado de cada verificación y lo que no se pudo verificar.

## Criterio de entrega

Al terminar una tarea se informan las rutas creadas o modificadas y un resumen verificable: número de semanas, apps, figuras y glosas; resultado de `verificar_curso.py`; referencias dudosas; y cualquier elemento que haya quedado fuera. Lo que no se verificó se dice que no se verificó.
