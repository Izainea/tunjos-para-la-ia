# -*- coding: utf-8 -*-
"""Aplica un nombre nuevo a un curso en todo el programa.

Uso:
    python herramientas/renombrar_curso.py 3 "Descripción auditada de imágenes con IA" [--corto "Imágenes auditadas"]

Cambia: el encabezado del README del curso, NOMBRE y UNAL["nombre"] en propuestas/contenido.py, PREVISTOS y CORTOS en
build.py, la tabla del README del programa, docente.md, y el texto de los enlaces con que los demás cursos lo citan
([*Nombre viejo*](...curso-N-...)). No toca docs/: después hay que correr build.py y generar_propuestas.py.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent


def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) < 2:
        raise SystemExit(__doc__)
    n, nuevo = int(args[0]), args[1]
    corto = None
    if "--corto" in sys.argv:
        corto = sys.argv[sys.argv.index("--corto") + 1]
    if ":" in nuevo:
        raise SystemExit("El nombre no puede llevar dos puntos")
    carpeta = next(RAIZ.glob(f"cursos/curso-{n}-*"))
    readme = carpeta / "README.md"
    s = readme.read_text(encoding="utf-8")
    m = re.match(r"^#\s*Curso\s*\d+\.\s*(.+)$", s, re.M)
    viejo = m.group(1).strip()
    s = s.replace(m.group(0), f"# Curso {n}. {nuevo}", 1)
    readme.write_text(s, encoding="utf-8")
    print(f"README: {viejo!r} -> {nuevo!r}")

    # propuestas/contenido.py
    c = carpeta / "propuestas" / "contenido.py"
    if c.exists():
        t = c.read_text(encoding="utf-8")
        t = re.sub(r'^NOMBRE = "[^"]*"', lambda _: f'NOMBRE = "{nuevo}"', t, count=1, flags=re.M)
        t = re.sub(r'"nombre": "[^"]*"', lambda _: f'"nombre": "{nuevo}"', t, count=1)
        c.write_text(t, encoding="utf-8")
        print("propuestas/contenido.py: NOMBRE y UNAL['nombre'] actualizados (sin subtítulo)")

    # build.py: PREVISTOS y CORTOS
    b = RAIZ / "build.py"
    t = b.read_text(encoding="utf-8")
    t = re.sub(rf'(\n\s*{n}: \(")[^"]*(")', lambda mm: mm.group(1) + nuevo + mm.group(2), t, count=1)
    if corto:
        t = re.sub(rf'({n}: ")[^"]*(")', lambda mm: mm.group(1) + corto + mm.group(2), t, count=1)
    b.write_text(t, encoding="utf-8")

    # README del programa y docente.md: filas de tabla con el nombre viejo
    for p in (RAIZ / "README.md", RAIZ / "docente.md"):
        t = p.read_text(encoding="utf-8")
        if viejo in t:
            p.write_text(t.replace(viejo, nuevo), encoding="utf-8")

    # enlaces desde otros cursos: [*Nombre viejo*](...curso-N-...) y <a href="...curso-N-..."><em>Nombre viejo</em></a>
    cortos_previos = {viejo}
    for otro in RAIZ.glob("cursos/curso-*"):
        if otro == carpeta:
            continue
        for p in list(otro.rglob("*.md")):
            if "propuestas" in p.parts:
                continue
            t = p.read_text(encoding="utf-8")
            # [*Nombre viejo*](...) y [*Nombre viejo*, semana 4](...)
            t2 = re.sub(rf"\[\*([^*\]]+)\*([^\]]*)\](\((?:\.\./)+curso-{n}-[^)]*\))",
                        lambda mm: f"[*{nuevo}*{mm.group(2)}]{mm.group(3)}", t)
            t2 = re.sub(rf'(<a href="(?:\.\./)+curso-{n}-[^"]*"><em>)[^<]*(</em></a>)', lambda mm: mm.group(1) + nuevo + mm.group(2), t2)
            if t2 != t:
                p.write_text(t2, encoding="utf-8")
    print("enlaces desde otros cursos actualizados")


if __name__ == "__main__":
    main()
