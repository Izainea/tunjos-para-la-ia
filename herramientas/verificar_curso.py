# -*- coding: utf-8 -*-
"""Verifica un curso contra la guía de autoría.

Uso:
    python herramientas/verificar_curso.py cursos/curso-1-tres-inferencias [--capturas]
    python herramientas/verificar_curso.py --todos [--capturas]

Comprueba:
  1. Estructura de carpetas y archivos obligatorios (README, syllabus, 8 semanas, evaluación, bibliografía,
     plantillas, prácticas, apps, propuestas/contenido.py).
  2. Secciones obligatorias de cada semana, en orden.
  3. Términos prohibidos fuera de propuestas/: universidades destinatarias, "convocatoria", palabras de relleno, rayas.
  4. Enlaces internos de markdown que apuntan a archivos inexistentes.
  5. Mínimos didácticos: al menos 3 apps, 4 figuras, glosas en cada semana.
  6. Sintaxis JavaScript de cada app (esprima).
  7. Con --capturas: captura de cada app con Edge sin interfaz, en el scratchpad indicado por CAPTURAS_DIR
     (por defecto, una carpeta capturas/ junto a este script, ignorada por git).

Sale con código 1 si hay errores; los avisos no detienen.
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import quote

RAIZ = Path(__file__).resolve().parent.parent
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

SECCIONES = [
    "## Pregunta de la semana", "## Por qué esta semana", "## Contenido de la sesión", "## IA y exigencia",
    "## Lecturas", "## Guía de lectura", "## Taller de la segunda hora", "## Guion de la sesión",
    "## Para la próxima semana",
]
PROHIBIDOS_PUBLICO = [r"\bAndes\b", r"\bUniandes\b", r"\bUNAL\b", r"\bPEEC\b", r"convocatoria", r"Qualtrics"]
RELLENO = [r"\bfundamental(es)?\b", r"\bcrucial(es)?\b", r"\besencial(es)?\b", r"\brobust[oa]s?\b",
           r"\bpoderos[oa]s?\b", r"\bfascinante\b"]
RAYA = "—"


def md_files(curso: Path):
    for p in curso.rglob("*.md"):
        if "propuestas" in p.parts:
            continue
        yield p


def check_estructura(curso: Path, err: list, av: list) -> None:
    oblig = ["README.md", "programa/syllabus.md", "programa/evaluacion.md", "programa/bibliografia.md",
             "propuestas/contenido.py"] + [f"programa/semana-0{i}.md" for i in range(1, 9)]
    for o in oblig:
        if not (curso / o).exists():
            err.append(f"falta {o}")
    for d in ("plantillas", "practicas", "apps"):
        if not (curso / d).is_dir() or not any((curso / d).iterdir()):
            err.append(f"carpeta {d}/ vacía o inexistente")


def check_semanas(curso: Path, err: list, av: list) -> None:
    for i in range(1, 9):
        p = curso / "programa" / f"semana-0{i}.md"
        if not p.exists():
            continue
        s = p.read_text(encoding="utf-8")
        pos = -1
        for sec in SECCIONES:
            j = s.find(sec)
            if j < 0 and sec == "## Taller de la segunda hora":
                m = re.search(r"^## Taller\b", s, re.M)
                j = m.start() if m else -1
            if j < 0 and i == 8 and sec == "## Para la próxima semana":
                m = re.search(r"^## (Después del curso|Después del programa|Cierre)", s, re.M)
                j = m.start() if m else -1
            if j < 0:
                err.append(f"{p.name}: falta la sección '{sec}'")
            elif j < pos:
                av.append(f"{p.name}: la sección '{sec}' está fuera de orden")
            else:
                pos = j
        if 'class="glosa"' not in s:
            av.append(f"{p.name}: sin glosas al margen")
    # Títulos con dos puntos de gancho ("Tema: subtítulo"), prohibidos en todo el material
    for p in md_files(curso):
        en_codigo = False
        for k, l in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            if l.startswith("```"):
                en_codigo = not en_codigo
                continue
            if not en_codigo and re.match(r"^#{1,4} .*\S:\s", l + " "):
                err.append(f"{p.relative_to(curso)}:{k}: título con dos puntos de gancho; reformular como frase nominal")
        for k, l in enumerate(s.splitlines(), 1):
            if l.lstrip().startswith("<aside") and "</aside>" not in l:
                err.append(f"{p.name}:{k}: glosa sin cerrar en la misma línea (el renderizador absorbe el párrafo siguiente)")
        if s.count('<sup class="mark">') != s.count('<aside class="glosa">'):
            av.append(f"{p.name}: {s.count('<sup class=\"mark\">')} marcas y {s.count('<aside class=\"glosa\">')} glosas; deberían coincidir")
        if 'class="lede"' not in s:
            av.append(f"{p.name}: sin párrafo con capitular (lede)")
        n = len(s.splitlines())
        if n < 110:
            av.append(f"{p.name}: {n} líneas; la guía pide entre 120 y 180")


def check_prohibidos(curso: Path, err: list, av: list) -> None:
    for p in list(md_files(curso)) + list((curso / "apps").glob("*.html")):
        s = p.read_text(encoding="utf-8", errors="replace")
        rel = p.relative_to(curso)
        for pat in PROHIBIDOS_PUBLICO:
            for m in re.finditer(pat, s, re.I):
                linea = s.count("\n", 0, m.start()) + 1
                err.append(f"{rel}:{linea}: término no permitido fuera de propuestas/: '{m.group(0)}'")
        for pat in RELLENO:
            for m in re.finditer(pat, s, re.I):
                linea = s.count("\n", 0, m.start()) + 1
                av.append(f"{rel}:{linea}: palabra de relleno '{m.group(0)}'")
        if p.suffix == ".md" and RAYA in s:
            av.append(f"{rel}: contiene rayas (—); la guía pide evitarlas")


def check_enlaces(curso: Path, err: list, av: list) -> None:
    for p in md_files(curso):
        s = p.read_text(encoding="utf-8")
        for m in re.finditer(r"\]\(([^)#\s]+)(#[^)]*)?\)", s):
            href = m.group(1)
            if href.startswith(("http://", "https://", "mailto:")):
                continue
            destino = (p.parent / href).resolve()
            if not destino.exists():
                err.append(f"{p.relative_to(curso)}: enlace roto '{href}'")
        for m in re.finditer(r'src="(apps/[^"]+)"', s):
            if not (curso / m.group(1)).exists():
                err.append(f"{p.relative_to(curso)}: iframe a app inexistente '{m.group(1)}'")


def check_autocontenido(curso: Path, err: list, av: list) -> None:
    """Prohíbe referencias a otros cursos por número o posición; deben ir con nombre, enlace y resumen."""
    pats = [r"\bcursos? [1-7]\b", r"\bcursos? (anterior|anteriores|siguiente|siguientes|previo|previos)\b",
            r"\bsemana \d+ del curso\b", r"\ben los cursos [1-7]"]
    for p in md_files(curso):
        s = p.read_text(encoding="utf-8")
        for pat in pats:
            for m in re.finditer(pat, s, re.I):
                linea = s.count("\n", 0, m.start()) + 1
                texto_linea = s.splitlines()[linea - 1]
                if re.match(r"^#\s*Curso\s*\d+\.", texto_linea):
                    continue  # el título del propio curso
                err.append(f"{p.relative_to(curso)}:{linea}: referencia a otro curso por número o posición ('{m.group(0)}'); use nombre, enlace y resumen")


def check_didactica(curso: Path, err: list, av: list) -> None:
    apps = list((curso / "apps").glob("*.html"))
    if len(apps) < 3:
        err.append(f"solo {len(apps)} apps; la guía pide al menos 3")
    figs = 0
    for p in (curso / "programa").glob("semana-*.md"):
        figs += len(re.findall(r"<figure", p.read_text(encoding="utf-8")))
    if figs < 4:
        err.append(f"solo {figs} figuras en las semanas; la guía pide al menos 4")
    embebidas = set()
    for p in (curso / "programa").glob("semana-*.md"):
        embebidas |= set(re.findall(r'src="apps/([^"]+)"', p.read_text(encoding="utf-8")))
    for a in apps:
        if a.name not in embebidas:
            av.append(f"la app {a.name} no está embebida en ninguna semana")


def check_js(curso: Path, err: list, av: list) -> None:
    try:
        import esprima
    except ImportError:
        av.append("esprima no instalado (pip install esprima); se omite la sintaxis JS")
        return
    for a in (curso / "apps").glob("*.html"):
        s = a.read_text(encoding="utf-8")
        for i, bloque in enumerate(re.findall(r"<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>", s, re.S)):
            try:
                esprima.parseScript(bloque, {"tolerant": False})
            except Exception as e:  # noqa: BLE001
                err.append(f"apps/{a.name}: error de sintaxis JS en el bloque {i + 1}: {e}")


def capturas(curso: Path, err: list, av: list) -> None:
    if not Path(EDGE).exists():
        av.append("Edge no encontrado; se omiten capturas")
        return
    destino = Path(os.environ.get("CAPTURAS_DIR", RAIZ / "herramientas" / "capturas")) / curso.name
    destino.mkdir(parents=True, exist_ok=True)
    for a in (curso / "apps").glob("*.html"):
        url = "file:///" + quote(str(a.resolve()).replace("\\", "/"), safe="/:")
        png = destino / (a.stem + ".png")
        try:
            subprocess.run([EDGE, "--headless=new", "--disable-gpu", f"--screenshot={png}", "--window-size=1000,800", url],
                           check=False, timeout=60, capture_output=True)
        except subprocess.TimeoutExpired:
            av.append(f"captura de {a.name}: tiempo agotado")
            continue
        if not png.exists() or png.stat().st_size < 2000:
            av.append(f"captura de {a.name} vacía o ausente")
        else:
            print(f"  captura: {png}")


def verificar(curso: Path, con_capturas: bool) -> int:
    err, av = [], []
    check_estructura(curso, err, av)
    check_semanas(curso, err, av)
    check_prohibidos(curso, err, av)
    check_enlaces(curso, err, av)
    check_didactica(curso, err, av)
    check_autocontenido(curso, err, av)
    check_js(curso, err, av)
    if con_capturas:
        capturas(curso, err, av)
    print(f"== {curso.name}: {len(err)} errores, {len(av)} avisos")
    for e in err:
        print(f"  ERROR  {e}")
    for a in av:
        print(f"  aviso  {a}")
    return 1 if err else 0


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    con_capturas = "--capturas" in sys.argv
    if "--todos" in sys.argv:
        cursos = sorted((RAIZ / "cursos").glob("curso-*"))
    elif args:
        cursos = [RAIZ / a for a in args]
    else:
        raise SystemExit(__doc__)
    codigo = 0
    for c in cursos:
        codigo |= verificar(c, con_capturas)
    sys.exit(codigo)
