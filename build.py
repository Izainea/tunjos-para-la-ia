# -*- coding: utf-8 -*-
"""Genera el sitio estático en docs/ a partir del markdown de todos los cursos.

Uso: python build.py
Requiere: pip install markdown

Para cada carpeta cursos/curso-N-slug/ produce docs/curso-N/ con: index (README + syllabus), semana-01..08,
evaluacion, bibliografia, plantillas (todas las plantillas), practicas (todas las prácticas) y la copia de apps/.
Las carpetas propuestas/ nunca se publican. La portada docs/index.html lista los cursos y las rutas; docs/docente.html
publica docente.md.
"""
from __future__ import annotations

import re
import shutil
from pathlib import Path

import markdown

ROOT = Path(__file__).parent
DOCS = ROOT / "docs"
CURSOS_DIR = ROOT / "cursos"
SITE = "https://izainea.github.io/tunjos-para-la-ia"
REPO = "https://github.com/Izainea/tunjos-para-la-ia"
YEAR = 2026

MD = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists", "attr_list", "md_in_html"])

CORTOS = {1: "Las tres inferencias", 2: "Corpus textual", 3: "Corpus visual", 4: "Codificación asistida",
          5: "Métodos computacionales", 6: "Validación e interpretación", 7: "Ética y gobernanza"}
CAPAS = {1: "Fundamentos", 2: "Oficio", 3: "Oficio", 4: "Oficio", 5: "Juicio", 6: "Juicio", 7: "Juicio"}
RUTAS = [
    ("Fundamentos", "1, 6", "Quien ya investiga y quiere criterio, no herramientas"),
    ("Texto", "1, 2, 4, 6", "Sociología, historia, comunicación, derecho"),
    ("Imagen", "1, 3, 4, 6", "Estudios visuales, museos, archivos"),
    ("Computacional", "2, 3, 5", "Quien ya tiene método y quiere escala"),
    ("Programa completo", "1 a 7 y proyecto integrador", "Posgrado y grupos de investigación"),
]
# Cursos previstos aunque su carpeta aún no exista
PREVISTOS = {
    1: ("Las tres inferencias en el razonamiento humano y el artificial", "Qué tipo de inferencia hace la máquina, cuál hace el investigador y cuál puede validarse sin un sujeto que responda."),
    2: ("Del documento al corpus textual trazable", "Cómo convertir documentos dispersos en un corpus con procedencia, reproducible y listo para analizar."),
    3: ("Del archivo al corpus visual descrito", "Cómo catalogar, describir y cuidar un corpus de imágenes con ayuda de modelos multimodales sin perder el juicio."),
    4: ("Codificación asistida por una máquina que configura", "Qué hace un modelo cuando propone códigos y categorías, con qué criterio se juzga y quién responde por el libro de códigos."),
    5: ("Métodos computacionales para el sentido", "Cuándo un patrón computacional es una hipótesis que vale la pena perseguir y cuándo es un artefacto del método."),
    6: ("Validación e interpretación como refiguración del investigador", "Qué significa validar lo configurado, con qué criterios, y cómo escribir hallazgos por los que se pueda responder."),
    7: ("Ética, exterioridad y gobernanza", "Qué excluye, a quién expone y a quién exime un flujo asistido por modelos, y qué reglas lo hacen defendible."),
}


# ----------------------------------------------------------------- markdown
def rewrite_links(html: str, slug_map: dict[str, str]) -> str:
    def fix(m):
        href = m.group(1)
        if href.startswith(("http", "mailto:", "#")):
            return m.group(0)
        h = href
        h = re.sub(r"^\.\./?$", "../index.html", h)
        h = h.replace("../../USO-DE-IA.md", "../uso-de-ia.html").replace("../USO-DE-IA.md", "uso-de-ia.html")
        # enlaces entre cursos: ../../curso-N-slug/README.md o .../programa/semana-0M.md → ../curso-N/<página>.html
        m2 = re.match(r"^(?:\.\./)+curso-(\d)-[a-z0-9-]+/?(README\.md|programa/(semana-0\d|syllabus|evaluacion|bibliografia)\.md|(plantillas|practicas|apps)/?.*)?$", h)
        if m2:
            n, resto = m2.group(1), m2.group(2) or ""
            if resto.startswith("programa/"):
                pagina = "index.html" if "syllabus" in resto else resto.split("/")[1].replace(".md", ".html")
            elif resto.startswith(("plantillas", "practicas", "apps")):
                pagina = resto.split("/")[0] + ".html"
            else:
                pagina = "index.html"
            return f'href="../curso-{n}/{pagina}"'
        h = re.sub(r"^\.\./(plantillas|practicas|apps|programa)(/|$)", r"\1\2", h)  # desde programa/ hacia carpetas hermanas
        h = re.sub(r"^programa/?$", "index.html", h)
        h = re.sub(r"^(plantillas|practicas|apps)/?$", r"\1.html", h)
        h = re.sub(r"^programa/", "", h)
        h = re.sub(r"^plantillas/[^#]+\.md$", lambda x: "plantillas.html#" + Path(x.group(0)).stem, h)
        h = re.sub(r"^practicas/[^#]+\.md$", lambda x: "practicas.html#" + Path(x.group(0)).stem, h)
        h = re.sub(r"^syllabus\.md$", "index.html", h)
        h = re.sub(r"^README\.md$", "index.html", h)
        h = re.sub(r"\.md(#|$)", r".html\1", h)
        for k, v in slug_map.items():
            h = h.replace(k, v)
        return f'href="{h}"'
    return re.sub(r'href="([^"]+)"', fix, html)


def render_md(paths: list[Path], slug_map: dict[str, str] | None = None) -> str:
    parts = []
    for p in paths:
        MD.reset()
        texto = p.read_text(encoding="utf-8")
        # Dentro de bloques HTML (lede, glosas, figuras) Python-Markdown no procesa markdown:
        # se convierten a mano los enlaces y las cursivas de esas líneas.
        def en_html(linea: str) -> str:
            if not linea.lstrip().startswith(("<p", "<aside", "<figcaption", "<figure")):
                return linea
            linea = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a href="\2">\1</a>', linea)
            linea = re.sub(r"(?<![\w*])\*([^*\n]+?)\*(?![\w*])", r"<em>\1</em>", linea)
            return linea
        texto = "\n".join(en_html(l) for l in texto.splitlines())
        html = MD.convert(texto)
        html = html.replace("<table>", '<div class="table-wrap"><table>').replace("</table>", "</table></div>")
        html = html.replace("<h1>", f'<h1 id="{p.stem}">', 1)
        html = re.sub(r'(?<!href=")(?<!">)(?<!src=")(https?://[^\s<]+?)(?=[\s<]|\.$|\.<)', r'<a href="\1">\1</a>', html)
        parts.append(html)
    return rewrite_links("\n<hr />\n".join(parts), slug_map or {})


# ----------------------------------------------------------------- cursos
class Curso:
    def __init__(self, path: Path):
        self.path = path
        m = re.match(r"curso-(\d+)-(.+)", path.name)
        self.n = int(m.group(1))
        self.slug = f"curso-{self.n}"
        readme = (path / "README.md").read_text(encoding="utf-8") if (path / "README.md").exists() else ""
        t = re.search(r"^#\s*Curso\s*\d+\.\s*(.+)$", readme, re.M)
        self.titulo = t.group(1).strip() if t else PREVISTOS.get(self.n, ("Curso", ""))[0]
        d = re.search(r"\*\*Pregunta del curso\.\*\*\s*(.+)", readme)
        self.desc = d.group(1).strip() if d else PREVISTOS.get(self.n, ("", ""))[1]
        self.semanas = sorted((path / "programa").glob("semana-0*.md"))
        self.completo = len(self.semanas) == 8 and (path / "programa" / "syllabus.md").exists()

    def titulo_semana(self, p: Path) -> str:
        s = p.read_text(encoding="utf-8")
        m = re.search(r"^#\s*Semana\s*\d+\.\s*(.+)$", s, re.M)
        return m.group(1).strip() if m else p.stem


def cursos_existentes() -> list[Curso]:
    return sorted((Curso(p) for p in CURSOS_DIR.glob("curso-*") if p.is_dir()), key=lambda c: c.n)


# ----------------------------------------------------------------- plantilla html
def panel(active: str, depth: int, curso: Curso | None, cursos: list[Curso]) -> str:
    base = "../" if depth else ""
    items = [f'<a href="{base}index.html"{" class=\"is-active\"" if active == "programa" else ""}>Programa</a>',
             f'<a href="{base}docente.html"{" class=\"is-active\"" if active == "docente" else ""}>Docente</a>',
             f'<a href="{base}uso-de-ia.html"{" class=\"is-active\"" if active == "uso-de-ia" else ""}>Uso de IA</a>']
    if curso:
        nav = [("index.html", f"{curso.n} · {CORTOS.get(curso.n, 'Curso')}", False)]
        nav += [(f"semana-0{i}.html", f"Semana {i}", True) for i in range(1, 9)]
        nav += [("evaluacion.html", "Evaluación", False), ("bibliografia.html", "Bibliografía", False),
                ("plantillas.html", "Plantillas", False), ("practicas.html", "Prácticas", False),
                ("apps.html", "Mini apps", False)]
        for href, label, sub in nav:
            cls = ([] if not sub else ["sub"]) + (["is-active"] if active == href else [])
            attr = f' class="{" ".join(cls)}"' if cls else ""
            items.append(f'<a href="{href}"{attr}>{label}</a>')
        otros = [c for c in cursos if c.n != curso.n and c.completo]
        if otros:
            items.append('<span class="nav-sep">Otros cursos</span>')
            items += [f'<a class="sub" href="../{c.slug}/index.html">{c.n} · {CORTOS.get(c.n, "Curso")}</a>' for c in otros]
    else:
        for c in cursos:
            if c.completo:
                items.append(f'<a class="sub" href="{base}{c.slug}/index.html">{c.n} · {CORTOS.get(c.n, "Curso")}</a>')
    nav_html = "\n          ".join(items)
    return f"""<header class="panel">
        <div>
          <a class="home" href="https://izainea.github.io/" aria-label="Inicio">
            <span class="id-row">
              <span class="photo" role="img" aria-label="Foto de Carlos Isaac Zainea Maya"></span>
              <svg class="glyph" viewBox="0 0 46 46" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round">
                <circle cx="8" cy="36" r="4" fill="currentColor" stroke="none"></circle>
                <circle cx="23" cy="9" r="4" fill="currentColor" stroke="none"></circle>
                <circle cx="39" cy="33" r="4" fill="currentColor" stroke="none"></circle>
                <path d="M11 31 L20 14"></path><path d="M26.5 13 L36 28"></path><path d="M13 35.5 L34 33.5"></path>
                <path d="M16.5 14.8 L20 14 L21 17.6"></path><path d="M32.3 27.3 L36 28 L36.4 24.2"></path><path d="M30.8 31 L34 33.5 L31.3 36.5"></path>
              </svg>
            </span>
            <p class="name">Carlos Isaac<br />Zainea Maya</p>
          </a>
          <p class="role">Tunjos para la IA<br />Programa de cursos</p>
          <p class="tagline">Razonamiento, validación e inteligencia artificial en ciencias sociales y humanidades.</p>
        </div>
        <nav aria-label="Secciones">
          {nav_html}
        </nav>
        <div class="links">
          <a href="{REPO}" target="_blank" rel="noopener">GitHub</a>
          <a href="https://izainea.github.io/" target="_blank" rel="noopener">Sitio</a>
          <a href="mailto:cizaineam@gmail.com">Correo</a>
          <button type="button" class="theme-btn" id="tema-btn" aria-label="Cambiar entre papel y pizarra">papel / pizarra</button>
        </div>
      </header>"""


def shell(title: str, description: str, body: str, active: str, depth: int, url: str,
          curso: Curso | None, cursos: list[Curso]) -> str:
    css = ("../" if depth else "") + "styles.css"
    description = description.replace('"', "&quot;")
    return f"""<!doctype html>
<html lang="es">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{title} · Carlos Isaac Zainea</title>
    <meta name="description" content="{description}" />
    <meta name="author" content="Carlos Isaac Zainea Maya" />
    <link rel="canonical" href="{url}" />
    <meta property="og:title" content="{title}" />
    <meta property="og:description" content="{description}" />
    <meta property="og:type" content="website" />
    <meta property="og:url" content="{url}" />
    <meta property="og:locale" content="es_CO" />
    <link rel="icon" type="image/svg+xml" href="https://izainea.github.io/favicon.svg" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=PT+Sans:ital,wght@0,400;0,700;1,400;1,700&display=swap" />
    <link rel="stylesheet" href="{css}" />
    <script>
      var t = null; try {{ t = localStorage.getItem('tema'); }} catch (e) {{}}
      document.documentElement.dataset.theme = t || 'light';
    </script>
  </head>
  <body>
    <div class="page">
      {panel(active, depth, curso, cursos)}
      <main>
        {body}
        <footer>© {YEAR} Carlos Isaac Zainea Maya · Material bajo CC BY-SA 4.0 · <a href="{REPO}">Fuente en GitHub</a> · <a href="{'../' if depth else ''}uso-de-ia.html">Declaración de uso de IA</a></footer>
      </main>
    </div>
    <script>
      document.getElementById('tema-btn').addEventListener('click', function () {{
        var root = document.documentElement;
        var dark = root.dataset.theme ? root.dataset.theme === 'dark' : matchMedia('(prefers-color-scheme: dark)').matches;
        root.dataset.theme = dark ? 'light' : 'dark';
        try {{ localStorage.setItem('tema', root.dataset.theme); }} catch (e) {{}}
        document.querySelectorAll('iframe.app').forEach(function (f) {{ try {{ f.contentDocument.documentElement.dataset.theme = root.dataset.theme; }} catch (e) {{}} }});
      }});
    </script>
  </body>
</html>
"""


# ----------------------------------------------------------------- páginas de un curso
def paginas_curso(c: Curso) -> list[tuple[str, str, str, str, list[Path]]]:
    P = c.path
    pages = [("index", f"Curso {c.n}", c.titulo, c.desc, [P / "README.md", P / "programa" / "syllabus.md"])]
    for i, s in enumerate(c.semanas, 1):
        t = c.titulo_semana(s)
        txt = s.read_text(encoding="utf-8")
        q = re.search(r"## Pregunta de la semana\s*\n+([^\n#<]+)", txt)
        pages.append((s.stem, f"Curso {c.n} · Semana {i}", f"Semana {i}. {t}", (q.group(1).strip() if q else t), [s]))
    pages += [
        ("evaluacion", f"Curso {c.n} · Evaluación", "Evaluación", "Rúbricas de los productos y la bitácora.", [P / "programa" / "evaluacion.md"]),
        ("bibliografia", f"Curso {c.n} · Bibliografía", "Bibliografía", "Lecturas por semana, con enlaces de acceso abierto.", [P / "programa" / "bibliografia.md"]),
        ("plantillas", f"Curso {c.n} · Plantillas", "Plantillas", "Plantillas de los productos del curso.", sorted((P / "plantillas").glob("*.md"))),
        ("practicas", f"Curso {c.n} · Prácticas", "Prácticas", "Guías de las prácticas y cuaderno de apoyo.", sorted((P / "practicas").glob("*.md"))),
    ]
    return [p for p in pages if all(f.exists() for f in p[4]) and p[4]]


def pagina_apps(c: Curso) -> str:
    """Lista todas las mini apps del curso, embebidas, con su título y la semana que las usa."""
    semanas = {}
    for s in c.semanas:
        for a in re.findall(r'src="apps/([^"]+)"', s.read_text(encoding="utf-8")):
            semanas.setdefault(a, []).append(s.stem.replace("semana-0", "semana "))
    bloques = []
    for a in sorted((c.path / "apps").glob("*.html")):
        html = a.read_text(encoding="utf-8", errors="replace")
        t = re.search(r"<title>(.*?)</title>", html, re.S)
        titulo = (t.group(1).strip() if t else a.stem)
        d = re.search(r"<h1>.*?</h1>\s*<p>(.*?)</p>", html, re.S)
        desc = re.sub(r"<[^>]+>", "", d.group(1)).strip() if d else ""
        usada = ", ".join(semanas.get(a.name, [])) or "no embebida en una semana"
        bloques.append(f'<h2 id="{a.stem}">{titulo}</h2>\n<p class="note">Se usa en: {usada}. '
                       f'<a href="apps/{a.name}">Abrir en pestaña propia</a>.</p>\n<p>{desc}</p>\n'
                       f'<iframe class="app" src="apps/{a.name}" title="{titulo}" loading="lazy"></iframe>')
    return "\n".join(bloques)


def pager(slug: str, pages) -> str:
    order = [p[0] for p in pages]
    labels = {p[0]: p[2] for p in pages}
    i = order.index(slug)
    prev_ = order[i - 1] if i > 0 else None
    next_ = order[i + 1] if i + 1 < len(order) else None
    left = f'<a href="{prev_}.html">← {labels[prev_]}</a>' if prev_ else "<span></span>"
    right = f'<a href="{next_}.html">{labels[next_]} →</a>' if next_ else "<span></span>"
    return f'<nav class="pager" aria-label="Páginas">{left}{right}</nav>'


def build_curso(c: Curso, cursos: list[Curso]) -> None:
    out = DOCS / c.slug
    # Dropbox o un navegador pueden retener la carpeta: se borra lo que se pueda y se sobrescribe el resto
    if out.exists():
        for p in sorted(out.rglob("*"), reverse=True):
            try:
                p.unlink() if p.is_file() else p.rmdir()
            except OSError:
                pass
    out.mkdir(parents=True, exist_ok=True)
    if (c.path / "apps").is_dir():
        shutil.copytree(c.path / "apps", out / "apps", dirs_exist_ok=True)
    pages = paginas_curso(c)
    if (c.path / "apps").is_dir() and any((c.path / "apps").glob("*.html")):
        pages.append(("apps", f"Curso {c.n} · Mini apps", "Mini apps", "Instrumentos interactivos del curso, en la semana que los usa.", []))
    slug_map = {f"../curso-{k}-": f"../curso-{k}/" for k in range(1, 10)}
    for slug, title, h1, desc, files in pages:
        content = pagina_apps(c) if slug == "apps" else render_md(files, slug_map)
        if len(files) == 1:
            # el encabezado de primer nivel ya está en la cabecera de la página
            content = re.sub(r'<h1 id="[^"]*">.*?</h1>\s*', "", content, count=1)
        head = f"""<div class="post-head">
          <div class="meta"><span>Curso {c.n} · {CAPAS.get(c.n, '')} · ocho sesiones · híbrido</span></div>
          <h1>{h1}</h1>
          <p class="desc">{desc}</p>
        </div>"""
        body = f'{head}\n<article class="prose">\n{content}\n</article>\n{pager(slug, pages)}'
        (out / f"{slug}.html").write_text(
            shell(title, desc, body, f"{slug}.html", 1, f"{SITE}/{c.slug}/{slug}.html", c, cursos), encoding="utf-8")


# ----------------------------------------------------------------- portada y docente
def build_index(cursos: list[Curso]) -> None:
    por_n = {c.n: c for c in cursos}
    rows = []
    for n in range(1, 8):
        c = por_n.get(n)
        titulo, desc = (c.titulo, c.desc) if c else PREVISTOS[n]
        if c and c.completo:
            inner = (f'<span class="when">Curso {n} · {CAPAS[n]}</span><span class="name">{titulo}</span>'
                     f'<span class="status ok">material completo</span><p>{desc}</p>')
            rows.append(f'<li><a class="row" href="{c.slug}/index.html">{inner}</a></li>')
        else:
            inner = (f'<span class="when">Curso {n} · {CAPAS[n]}</span><span class="name">{titulo}</span>'
                     f'<span class="status">en preparación</span><p>{desc}</p>')
            rows.append(f'<li><div class="row">{inner}</div></li>')
    rutas = "".join(f"<tr><td>{r}</td><td>{cs}</td><td>{q}</td></tr>" for r, cs, q in RUTAS)
    body = f"""<div class="post-head">
          <div class="meta"><span>Programa de cursos</span><span>Siete cursos · tres capas · rutas apilables</span></div>
          <h1>Tunjos para la IA</h1>
          <p class="desc">Razonamiento, validación e inteligencia artificial en ciencias sociales y humanidades.</p>
        </div>
        <section class="prose">
          <p class="lede">Quien investiga con modelos de lenguaje necesita tres cosas que se enseñan por separado o no se enseñan. Saber qué tipo de inferencia hace la máquina y cuál hace el investigador. Saber construir un flujo técnico que deje rastro auditable. Saber validar y responder por el resultado ante una comunidad. El programa integra las tres sobre corpus reales del estudiante.</p>
          <p>El principio de diseño es que cada curso se enseña con el método que enseña. El estudiante configura con la máquina, valida, registra la frontera entre ambos y entrega el registro. La evidencia de aprendizaje no es el producto sino el registro de validación. El programa nace de la investigación doctoral <a href="https://izainea.github.io/escritos/agencia-sin-imputacion.pdf"><i>Agencia sin imputación</i></a> y del concepto de <a href="https://izainea.github.io/blog/protesis-hermeneutica/">prótesis hermenéutica</a>: un sistema en el que la máquina configura, el investigador valida, y la frontera entre ambos es el principio de diseño.</p>
          <p>Todos los cursos tienen ocho sesiones en modalidad híbrida, y se adaptan al formato de microcredencial o de educación continua de cada institución: una sesión presencial semanal con participación remota sincrónica y trabajo asincrónico guiado. Quien dicta el programa se presenta en la página del <a href="docente.html">docente</a>.</p>
        </section>
        <section class="prose" id="nombre">
          <div class="sec-head wide"><span class="no">§0</span><h2>Por qué el nombre</h2></div>
          <p>El nombre viene del <i>tunjo</i>, la pequeña figura de oro o tumbaga que los muiscas del altiplano cundiboyacense ofrecían en lagunas y santuarios para pedir algo y hablar con sus deidades<sup class="mark">a</sup>. Cada tunjo lleva una escena, un oficio, un gesto; por eso en el Museo del Oro se dice que los tunjos hablan. Un tunjo es un acto hecho con oficio, un mensaje que queda como registro y alguien que lo entrega y responde ante su comunidad.</p>
          <aside class="glosa"><span class="mark">a</span> Sobre los tunjos: Museo del Oro, Banco de la República, Bogotá; Eduardo Londoño, <a href="https://www.eltiempo.com/archivo/documento/CMS-12959343">«Hablan los tunjos»</a>, <i>El Tiempo</i>. La raíz muisca es <i>chunso</i>, según el diccionario <a href="https://muysca.cubun.org/chunso">Muysc cubun</a>.</aside>
          <p>Hoy muchos le ofrecen el tunjo a la inteligencia artificial: le entregan la pregunta y esperan el favor, como ante una laguna. Este programa propone lo contrario. El tunjo no es lo que se le da a la máquina; es lo que el investigador hace con oficio, deja como registro y por lo que responde. La máquina configura; quien ofrece el tunjo, valida.</p>
          <p class="note">El nombre se toma como homenaje a la tradición muisca y a quienes la estudian y la conservan. No designa ningún objeto sagrado de uso restringido ni pretende hablar por los pueblos del altiplano.</p>
        </section>
        <section>
          <div class="sec-head"><span class="no">§1</span><h2>Cursos</h2></div>
          <ul class="rows">
            {"".join(rows)}
          </ul>
        </section>
        <section class="prose">
          <div class="sec-head wide"><span class="no">§2</span><h2>Rutas apilables</h2></div>
          <div class="table-wrap"><table><thead><tr><th>Ruta</th><th>Cursos</th><th>Para quién</th></tr></thead><tbody>{rutas}</tbody></table></div>
          <p>Un estudiante puede tomar un curso solo, una ruta, o el programa completo con un proyecto integrador: una investigación propia, pequeña pero completa, ejecutada como prótesis hermenéutica y defendida ante pares.</p>
        </section>
        <section class="prose">
          <div class="sec-head wide"><span class="no">§3</span><h2>Por qué es distinto</h2></div>
          <p>Los cursos de IA para investigación enseñan a pedirle cosas a la máquina. Los cursos de método cualitativo ignoran la máquina. Los cursos de programación para humanidades enseñan a programar sin preguntar qué se valida. Este programa parte de una tesis filosófica sobre qué puede y qué no puede validar un sistema artificial, y convierte esa tesis en un oficio.</p>
          <p class="note">Todo el material es de acceso abierto bajo CC BY-SA 4.0 y está en <a href="{REPO}">GitHub</a>. Se elaboró con ayuda de modelos de lenguaje bajo la guía y la responsabilidad del autor: <a href="uso-de-ia.html">declaración de uso de IA</a>.</p>
        </section>"""
    (DOCS / "index.html").write_text(shell("Tunjos para la IA",
        "Programa de cursos sobre razonamiento, validación e inteligencia artificial en ciencias sociales y humanidades.",
        body, "programa", 0, f"{SITE}/", None, cursos), encoding="utf-8")


def build_uso_ia(cursos: list[Curso]) -> None:
    content = render_md([ROOT / "USO-DE-IA.md"])
    content = re.sub(r'<h1 id="[^"]*">.*?</h1>\s*', "", content, count=1)
    body = f"""<div class="post-head">
          <div class="meta"><span>Transparencia</span></div>
          <h1>Declaración de uso de inteligencia artificial</h1>
          <p class="desc">Qué hizo la máquina, qué decidió el autor y quién responde por este material.</p>
        </div>
        <article class="prose">{content}</article>"""
    (DOCS / "uso-de-ia.html").write_text(shell("Uso de IA", "Declaración de uso de inteligencia artificial en la elaboración del programa.", body, "uso-de-ia", 0,
                                                f"{SITE}/uso-de-ia.html", None, cursos), encoding="utf-8")


def build_docente(cursos: list[Curso]) -> None:
    content = render_md([ROOT / "docente.md"])
    body = f"""<div class="post-head">
          <div class="meta"><span>Docente</span></div>
          <h1>Carlos Isaac Zainea Maya</h1>
          <p class="desc">Matemático, doctorando en Filosofía y en Matemáticas, científico de datos para entidades públicas.</p>
        </div>
        <article class="prose">{content}</article>"""
    (DOCS / "docente.html").write_text(shell("Docente", "Perfil y experiencia de quien dicta el programa.", body, "docente", 0,
                                              f"{SITE}/docente.html", None, cursos), encoding="utf-8")


if __name__ == "__main__":
    DOCS.mkdir(exist_ok=True)
    cursos = cursos_existentes()
    build_index(cursos)
    build_docente(cursos)
    build_uso_ia(cursos)
    for c in cursos:
        if c.completo:
            build_curso(c, cursos)
        else:
            print(f"{c.path.name}: incompleto ({len(c.semanas)} semanas), no se publica")
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")
    print("docs/ generado:", len(list(DOCS.rglob("*.html"))), "páginas")
