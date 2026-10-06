# -*- coding: utf-8 -*-
"""Crea el andamio de un curso nuevo con la estructura obligatoria de la guía de autoría.

Uso:
    python herramientas/nuevo_curso.py 8 "Título del curso" slug-del-curso

Crea cursos/curso-8-slug-del-curso/ con README, programa (syllabus, 8 semanas con las secciones en orden,
evaluación, bibliografía), plantillas/, practicas/, apps/ y propuestas/contenido.py copiado del curso 1 para
rellenar. No sobrescribe si la carpeta existe.
"""
from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
MODELO = RAIZ / "cursos" / "curso-1-tres-inferencias"

SEMANA = """# Semana {n}. {titulo}

## Pregunta de la semana

## Por qué esta semana

<p class="lede"></p>

## Contenido de la sesión

1.
2.
3.
4.
5.

## IA y exigencia

## Lecturas

**Central**

**Complementaria**

## Guía de lectura

## Taller de la segunda hora

## Guion de la sesión

| Minuto | Momento | Docente | Estudiante | Material |
|---|---|---|---|---|
| 0 a 10 | | | | |

Notas para el docente.

## Bitácora

## Para la próxima semana
"""


def main() -> None:
    if len(sys.argv) < 4:
        raise SystemExit(__doc__)
    n, titulo, slug = sys.argv[1], sys.argv[2], sys.argv[3]
    if not re.fullmatch(r"[a-z0-9-]+", slug):
        raise SystemExit("El slug lleva solo minúsculas, dígitos y guiones")
    curso = RAIZ / "cursos" / f"curso-{n}-{slug}"
    if curso.exists():
        raise SystemExit(f"Ya existe {curso}")
    for d in ("programa", "plantillas", "practicas", "apps", "propuestas"):
        (curso / d).mkdir(parents=True)
    (curso / "README.md").write_text(f"# Curso {n}. {titulo}\n\nMicrocredencial de 2 créditos, 8 semanas, modalidad híbrida.\n\n"
                                     "**Pregunta del curso.**\n\n**Respuesta que el curso construye.**\n\n## Contenido\n\n"
                                     "| Carpeta | Qué hay |\n|---|---|\n| [programa/](programa/) | |\n| [plantillas/](plantillas/) | |\n"
                                     "| [practicas/](practicas/) | |\n| [apps/](apps/) | |\n\n## Productos del estudiante\n\n1.\n2.\n3.\n",
                                     encoding="utf-8")
    (curso / "programa" / "syllabus.md").write_text(f"# Syllabus\n\n## Datos generales\n\n| | |\n|---|---|\n| Nombre | {titulo} |\n"
                                                    f"| Programa | Tunjos para la IA, curso {n} de 7 |\n| Créditos | 2 |\n"
                                                    "| Modalidad | Híbrida |\n\n## Problema que atiende\n\n## Competencias\n\n"
                                                    "## Resultados de aprendizaje y evidencias\n\n## Programa por semanas\n\n"
                                                    "## Metodología\n\n## Evaluación\n\n## Articulación\n\n## Política de uso de modelos de lenguaje\n",
                                                    encoding="utf-8")
    for i in range(1, 9):
        (curso / "programa" / f"semana-0{i}.md").write_text(SEMANA.format(n=i, titulo="Título"), encoding="utf-8")
    (curso / "programa" / "evaluacion.md").write_text("# Evaluación\n", encoding="utf-8")
    (curso / "programa" / "bibliografia.md").write_text("# Bibliografía\n", encoding="utf-8")
    shutil.copy(MODELO / "propuestas" / "contenido.py", curso / "propuestas" / "contenido.py")
    shutil.copy(RAIZ / "herramientas" / "app-base.html", curso / "apps" / "app-ejemplo.html")
    print(f"Creado {curso.relative_to(RAIZ)}. Siguiente paso: /curso {n} o el agente autor-curso.")


if __name__ == "__main__":
    main()
