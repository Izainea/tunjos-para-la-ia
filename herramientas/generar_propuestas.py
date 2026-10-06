# -*- coding: utf-8 -*-
"""Genera las dos propuestas en formato de convocatoria de un curso a partir de su propuestas/contenido.py.

Uso:
    python herramientas/generar_propuestas.py cursos/curso-1-tres-inferencias
    python herramientas/generar_propuestas.py --todos

Entradas:
    plantillas-externas/uniandes-credenciales.docx      plantilla docx (27 filas pregunta/respuesta)
    plantillas-externas/unal-B-FT-06.003.008.xlsx       formato xlsx de tres hojas
    <curso>/propuestas/contenido.py                     variables con el texto (ver curso 1)

Salidas (en <curso>/propuestas/, carpeta ignorada por git):
    propuesta-uniandes.docx
    propuesta-unal.xlsx

Edita el XML directamente para conservar logos, estilos y celdas combinadas. Si un archivo de salida
está abierto en Office, escribe junto a él con sufijo -nuevo.
"""
from __future__ import annotations

import importlib.util
import os
import re
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

RAIZ = Path(__file__).resolve().parent.parent
PLANTILLA_DOCX = RAIZ / "plantillas-externas" / "uniandes-credenciales.docx"
PLANTILLA_XLSX = RAIZ / "plantillas-externas" / "unal-B-FT-06.003.008.xlsx"

# ----------------------------------------------------------------- utilidades
def cargar_contenido(curso: Path):
    ruta = curso / "propuestas" / "contenido.py"
    if not ruta.exists():
        raise SystemExit(f"No existe {ruta}")
    spec = importlib.util.spec_from_file_location("contenido", ruta)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def escribible(dest: Path) -> Path:
    try:
        if dest.exists():
            dest.unlink()
        return dest
    except PermissionError:
        alt = dest.with_name(dest.stem + "-nuevo" + dest.suffix)
        if alt.exists():
            alt.unlink()
        print(f"AVISO: {dest.name} está abierto en Office; se escribe {alt.name}")
        return alt


def rezipear(carpeta: Path, dest: Path) -> None:
    with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(carpeta):
            for f in files:
                full = Path(root) / f
                z.write(full, full.relative_to(carpeta).as_posix())


# ----------------------------------------------------------------- docx
RPR = '<w:rPr><w:rFonts w:ascii="Verdana" w:hAnsi="Verdana"/></w:rPr>'


def parrafo(texto: str) -> str:
    return (f'<w:p><w:pPr><w:spacing w:before="46" w:after="46"/><w:jc w:val="both"/>{RPR}</w:pPr>'
            f'<w:r>{RPR}<w:t xml:space="preserve">{escape(texto)}</w:t></w:r></w:p>')


def respuestas_docx(C) -> dict[int, list[str]]:
    return {
        0: [C.NOMBRE], 2: C.DESCRIPCION, 3: C.COMPETENCIA, 4: C.RESULTADOS, 5: C.MODALIDAD, 6: C.HORAS,
        7: C.SEMANAS, 8: C.CONTENIDO, 9: C.COMO, 10: C.METODOLOGIAS, 11: C.NECESIDADES, 12: C.DIRIGIDO,
        13: C.CARRERAS, 14: C.OCUPACIONES, 15: C.SECTORES, 16: C.AREAS, 17: C.PALABRAS, 18: C.PROFESOR,
        19: C.OTORGA_CREDITOS, 20: C.NUM_CREDITOS, 21: C.HOMOLOGABLE, 22: C.HOMOLOGA_POR, 23: C.PROGRAMAS,
        24: C.INTEGRACION, 25: C.INDEPENDIENTE, 26: C.COMPLEMENTA,
    }


def generar_docx(C, curso: Path) -> Path:
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        with zipfile.ZipFile(PLANTILLA_DOCX) as z:
            z.extractall(tmp)
        p = tmp / "word" / "document.xml"
        x = p.read_text(encoding="utf-8")
        filas = list(re.finditer(r"<w:tr[ >].*?</w:tr>", x, re.S))
        if len(filas) != 27:
            raise SystemExit(f"La plantilla docx tiene {len(filas)} filas; se esperaban 27")
        resp = respuestas_docx(C)
        salida, ultimo = [], 0
        for i, m in enumerate(filas):
            fila = m.group(0)
            if i in resp:
                celdas = list(re.finditer(r"<w:tc>.*?</w:tc>", fila, re.S))
                objetivo = celdas[1] if len(celdas) > 1 else celdas[0]
                tcpr = re.search(r"<w:tcPr>.*?</w:tcPr>", objetivo.group(0), re.S).group(0)
                nueva = "<w:tc>" + tcpr + "".join(parrafo(t) for t in resp[i]) + "</w:tc>"
                fila = fila[:objetivo.start()] + nueva + fila[objetivo.end():]
            salida.append(x[ultimo:m.start()]); salida.append(fila); ultimo = m.end()
        salida.append(x[ultimo:])
        p.write_text("".join(salida), encoding="utf-8")
        dest = escribible(curso / "propuestas" / "propuesta-uniandes.docx")
        rezipear(tmp, dest)
    return dest


# ----------------------------------------------------------------- xlsx
def poner_celda(xml: str, ref: str, texto) -> str:
    t = escape(str(texto))
    m = re.search(rf'<c r="{ref}"( s="\d+")?[^>]*?(/>|>.*?</c>)', xml, re.S)
    if not m:
        raise SystemExit(f"celda {ref} no encontrada en el formato")
    s = m.group(1) or ""
    nueva = f'<c r="{ref}"{s} t="inlineStr"><is><t xml:space="preserve">{t}</t></is></c>'
    return xml[:m.start()] + nueva + xml[m.end():]


def alto_fila(xml: str, r: int, ht: float) -> str:
    m = re.search(rf'<row r="{r}"[^>]*>', xml)
    if not m:
        raise SystemExit(f"fila {r} no encontrada")
    tag = re.sub(r' ht="[^"]*"', "", m.group(0))
    tag = re.sub(r' customHeight="[^"]*"', "", tag)
    tag = tag[:-1] + f' ht="{ht}" customHeight="1">'
    return xml[:m.start()] + tag + xml[m.end():]


def alto_para(texto, cpl=110, pt=15, minimo=30) -> float:
    n = sum(max(1, -(-len(l) // cpl)) for l in str(texto).split("\n"))
    return max(minimo, n * pt + 6)


def generar_xlsx(C, curso: Path) -> Path:
    U = C.UNAL
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        with zipfile.ZipFile(PLANTILLA_XLSX) as z:
            z.extractall(tmp)
        hojas = tmp / "xl" / "worksheets"
        # Hoja 1
        p = hojas / "sheet1.xml"; x = p.read_text(encoding="utf-8")
        celdas = {
            "E13": U["nombre"], "G15": U["docente"], "E17": U["sintesis"], "G19": U["uab"], "E21": U["area"],
            "B25": U["justificacion"], "B29": U["objetivo_general"], "B33": U["objetivos_especificos"],
            "E35": U["modalidad"], "B39": U["metodologia"], "B43": U["dirigido"], "B46": U["difusion"],
            "G48": U["max_asistentes"], "G50": U["total_horas"], "D52": U["num_sesiones"], "J52": U["horas_sesion"],
            "E54": U["horario"], "E58": U["fecha_inicio"], "E62": U["tipo_salon"], "D64": U["equipos_sino"],
            "F64": U["equipos_cual"], "D67": U["logistico_sino"], "F67": U["logistico_cual"], "B72": U["producto_final"],
        }
        for ref, val in celdas.items():
            x = poner_celda(x, ref, val)
        for r, k, cpl in [(13, "nombre", 60), (17, "sintesis", 70), (25, "justificacion", 110), (29, "objetivo_general", 110),
                          (33, "objetivos_especificos", 110), (35, "modalidad", 70), (39, "metodologia", 110),
                          (43, "dirigido", 110), (46, "difusion", 110), (54, "horario", 70), (72, "producto_final", 110)]:
            x = alto_fila(x, r, alto_para(U[k], cpl))
        p.write_text(x, encoding="utf-8")
        # Hoja 2
        p = hojas / "sheet2.xml"; x = p.read_text(encoding="utf-8")
        for ref, val in {"F17": U["hv_nombre"], "F19": U["hv_documento"], "F21": U["hv_fijo"], "L21": U["hv_movil"],
                         "D23": U["hv_direccion"], "F25": U["hv_correo"], "B29": U["hv_resumen"], "B33": U["hv_perfil"],
                         "F35": U["hv_vinculacion"]}.items():
            x = poner_celda(x, ref, val)
        x = alto_fila(x, 29, alto_para(U["hv_resumen"], 120))
        x = alto_fila(x, 33, alto_para(U["hv_perfil"], 120))
        x = alto_fila(x, 35, alto_para(U["hv_vinculacion"], 80))
        p.write_text(x, encoding="utf-8")
        # Hoja 3
        p = hojas / "sheet3.xml"; x = p.read_text(encoding="utf-8")
        if len(U["sesiones"]) != 10:
            raise SystemExit(f"UNAL['sesiones'] tiene {len(U['sesiones'])} sesiones; el formato tiene 10 filas")
        for i, (tema, cont, bib) in enumerate(U["sesiones"]):
            r = 16 + i
            x = poner_celda(x, f"C{r}", tema); x = poner_celda(x, f"D{r}", cont)
            x = poner_celda(x, f"E{r}", U["horas_sesion"]); x = poner_celda(x, f"F{r}", bib)
            x = alto_fila(x, r, max(alto_para(cont, 55), alto_para(bib, 45)))
        x = poner_celda(x, "B34", U["producto_final"])
        x = alto_fila(x, 34, alto_para(U["producto_final"], 100))
        if "B34:F34" not in x:
            x = re.sub(r'<mergeCells count="(\d+)">', lambda m: f'<mergeCells count="{int(m.group(1)) + 1}">', x)
            x = x.replace("</mergeCells>", '<mergeCell ref="B34:F34"/></mergeCells>')
        p.write_text(x, encoding="utf-8")
        dest = escribible(curso / "propuestas" / "propuesta-unal.xlsx")
        rezipear(tmp, dest)
    return dest


def verificar(C) -> list[str]:
    """Comprobaciones de forma que los formatos exigen."""
    avisos = []
    if len(C.NOMBRE) > 58:
        avisos.append(f"NOMBRE tiene {len(C.NOMBRE)} caracteres; el máximo es 58")
    if len(C.UNAL["sintesis"]) > 600:
        avisos.append(f"UNAL['sintesis'] tiene {len(C.UNAL['sintesis'])} caracteres; el máximo es 600")
    horas = int(C.UNAL["num_sesiones"]) * int(C.UNAL["horas_sesion"])
    if horas != int(C.UNAL["total_horas"]):
        avisos.append(f"sesiones x horas = {horas}, pero total_horas = {C.UNAL['total_horas']}")
    for k in ("MODALIDAD",):
        if "híbrid" not in " ".join(getattr(C, k)).lower():
            avisos.append(f"{k} no menciona la modalidad híbrida")
    if "híbrid" not in C.UNAL["modalidad"].lower() and "semipresencial" not in C.UNAL["modalidad"].lower():
        avisos.append("UNAL['modalidad'] no es híbrida ni semipresencial")
    return avisos


def procesar(curso: Path) -> None:
    C = cargar_contenido(curso)
    for a in verificar(C):
        print(f"  AVISO ({curso.name}): {a}")
    d = generar_docx(C, curso)
    x = generar_xlsx(C, curso)
    print(f"  {d.relative_to(RAIZ)}\n  {x.relative_to(RAIZ)}")


if __name__ == "__main__":
    if not PLANTILLA_DOCX.exists() or not PLANTILLA_XLSX.exists():
        raise SystemExit("Faltan las plantillas en plantillas-externas/ (carpeta local, no versionada)")
    args = sys.argv[1:]
    if not args:
        raise SystemExit(__doc__)
    cursos = sorted((RAIZ / "cursos").glob("curso-*")) if args == ["--todos"] else [RAIZ / a for a in args]
    for c in cursos:
        if (c / "propuestas" / "contenido.py").exists():
            print(c.name)
            procesar(c)
        else:
            print(f"{c.name}: sin propuestas/contenido.py, se omite")
