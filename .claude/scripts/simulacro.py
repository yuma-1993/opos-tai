"""Generador y corrector de simulacros TAI (acceso libre) para el agente opos-simulacro.

Subcomandos:
  pdf      <examen.json>                      -> cuestionario.pdf + plantilla.pdf junto al JSON
  corregir <examen.json> "<respuestas>" [--supuesto I|II] [--anular 12,S5] [--corte2 0.5]
                                             -> imprime la corrección en Markdown y guarda correccion.json

Formato de respuestas (separadas por espacios o comas, mayúsculas o minúsculas):
  1a 2c 3-      primera parte ("-" o ausente = en blanco)
  R1b           reserva de la primera parte
  S1a S2d       supuesto elegido (--supuesto I o II si el examen trae dos)
  SR1c          reserva del supuesto
También vale una ráfaga posicional por parte: P:acb-d...  S:ba-c...

Criterios aplicados (TAI-LI, criterios CPS 18-05-2026 y Anexo V de la convocatoria 22-12-2025):
  puntuación directa por parte = A - E/3; blanco no penaliza.
  1ª parte apta si directa >= 50 % de la máxima (la CPS puede bajarlo hasta el 30 %).
  2ª parte solo se evalúa si la 1ª es apta; corte real por ranking (mín. 30 %): aquí orientativo.
  calificación 0-50 por parte: máxima -> 50, nota de corte -> 25, lineal entre ambas.
"""
import html
import json
import os
import re
import subprocess
import sys

EDGE_CANDIDATES = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
]

CSS = """
@page { size: A4; margin: 16mm 15mm 16mm 15mm; }
* { box-sizing: border-box; }
body { font-family: Arial, Helvetica, sans-serif; font-size: 9.6pt; color: #111; line-height: 1.32; }
h1 { font-size: 15pt; text-align: center; margin: 0 0 4mm; letter-spacing: .3px; }
h2 { font-size: 11pt; text-align: center; border: 1px solid #111; padding: 1.5mm; margin: 5mm 0 3mm; page-break-after: avoid; }
h3 { font-size: 10pt; margin: 4mm 0 2mm; text-decoration: underline; page-break-after: avoid; }
.cab { text-align: center; font-size: 9pt; color: #333; margin-bottom: 8mm; }
.caja { border: 1.5px solid #111; padding: 3mm 5mm; margin: 4mm auto; width: 85%; text-align: center; font-weight: bold; font-size: 12pt; }
.instr ol { padding-left: 6mm; }
.instr li { margin-bottom: 2.2mm; text-align: justify; }
.q { margin: 0 0 2.6mm; page-break-inside: avoid; }
.q .st { font-weight: bold; }
.q .op { margin-left: 6mm; }
.q .op div { margin: .4mm 0; }
pre, code { font-family: Consolas, "Courier New", monospace; font-size: 8.6pt; }
pre { background: #f3f3f3; border: 1px solid #ccc; padding: 2mm 3mm; white-space: pre-wrap; margin: 1.5mm 0; page-break-inside: avoid; }
.enun { text-align: justify; margin-bottom: 3mm; }
table { border-collapse: collapse; }
.hoja { width: auto; }
.hoja td { padding: .7mm 1.2mm; font-size: 8.6pt; }
.hoja .n { text-align: right; width: 9mm; font-weight: bold; }
.hoja .b { width: 6mm; height: 4.4mm; border: 1px solid #555; text-align: center; color: #888; font-size: 7pt; }
.grid { display: flex; gap: 8mm; flex-wrap: wrap; align-items: flex-start; }
.grid table { margin-bottom: 3mm; }
.pl td, .pl th { border: 1px solid #999; padding: 1mm 2mm; font-size: 8.8pt; vertical-align: top; }
.pl th { background: #eee; }
.pl { width: 100%; margin-bottom: 4mm; }
.just { font-size: 8.8pt; }
.pie { font-size: 8pt; color: #555; text-align: center; margin-top: 6mm; }
.salto { page-break-before: always; }
"""


def esc(s):
    """Escapa HTML; respeta ```bloques``` como <pre> y `código` en línea."""
    if s is None:
        return ""
    parts = re.split(r"```(?:[a-zA-Z0-9_+-]*)\n?(.*?)```", s, flags=re.S)
    out = []
    for i, p in enumerate(parts):
        if i % 2:
            out.append("<pre>" + html.escape(p.strip("\n")) + "</pre>")
        else:
            t = html.escape(p)
            t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
            t = t.replace("\n", "<br>")
            out.append(t)
    return "".join(out)


def pregunta_html(n, q):
    ops = "".join(f"<div>{k}) {esc(q['opciones'][k])}</div>" for k in "abcd")
    return f"<div class='q'><div class='st'>{n}. {esc(q['enunciado'])}</div><div class='op'>{ops}</div></div>"


def hoja_tabla(etiqueta, total, prefijo=""):
    filas = "".join(
        f"<tr><td class='n'>{prefijo}{i}</td>" + "".join(f"<td class='b'>{k}</td>" for k in "abcd") + "</tr>"
        for i in range(1, total + 1)
    )
    return f"<table class='hoja'><tr><td colspan='5'><b>{etiqueta}</b></td></tr>{filas}</table>"


def hoja_respuestas(ex):
    p1 = ex["parte1"]
    bloques = []
    preg = len(p1["preguntas"])
    # trocea la primera parte en columnas de 25
    for ini in range(1, preg + 1, 25):
        fin = min(preg, ini + 24)
        filas = "".join(
            f"<tr><td class='n'>{i}</td>" + "".join(f"<td class='b'>{k}</td>" for k in "abcd") + "</tr>"
            for i in range(ini, fin + 1)
        )
        bloques.append(f"<table class='hoja'><tr><td colspan='5'><b>1ª parte {ini}-{fin}</b></td></tr>{filas}</table>")
    if p1.get("reserva"):
        bloques.append(hoja_tabla("1ª parte · reserva", len(p1["reserva"]), "R"))
    for s in ex.get("supuestos", []):
        bloques.append(hoja_tabla(f"Supuesto {s['id']}", len(s["preguntas"]), "S"))
        if s.get("reserva"):
            bloques.append(hoja_tabla(f"Supuesto {s['id']} · reserva", len(s["reserva"]), "SR"))
    marca = ""
    if len(ex.get("supuestos", [])) > 1:
        marca = "<p><b>SUPUESTO ELEGIDO:</b> &nbsp; ☐ I &nbsp;&nbsp; ☐ II &nbsp; (marque solo uno; sin marca no se corrige la 2ª parte)</p>"
    return (
        "<div class='salto'></div><h2>HOJA DE RESPUESTAS</h2>" + marca +
        "<p style='font-size:8.5pt'>Para corregir, dicta las respuestas en el chat, por ejemplo: <code>1a 2c 3- … R1b … S1d …</code></p>"
        "<div class='grid'>" + "".join(bloques) + "</div>"
    )


def instrucciones(ex):
    p1 = ex["parte1"]
    n1, r1 = len(p1["preguntas"]), len(p1.get("reserva", []))
    sup = ex.get("supuestos", [])
    li = [
        "No abra este cuestionario hasta que se le indique.",
        (f"Este ejercicio consta de {'dos partes, ambas obligatorias y eliminatorias' if sup else 'una parte'}. "
         f"En la primera parte deberá contestar un cuestionario de <b>{n1}</b> preguntas de respuesta múltiple"
         + (f" y <b>{r1}</b> preguntas adicionales de reserva, que serán valoradas en el caso de que se anule alguna de las anteriores." if r1 else ".")),
    ]
    if sup:
        if len(sup) > 1:
            li.append("La segunda parte consiste en la resolución de un supuesto de carácter práctico <b>a elegir entre dos</b> "
                      "propuestos, correspondientes a los bloques III y IV del programa (SUPUESTO I y SUPUESTO II). "
                      "<b>MUY IMPORTANTE: marque en la hoja de respuestas el supuesto elegido</b> para que puedan ser corregidas las preguntas.")
        else:
            s = sup[0]
            li.append(f"La segunda parte consiste en la resolución de un supuesto de carácter práctico (SUPUESTO {s['id']}, bloque {s['bloque']}).")
        li.append(f"Cada supuesto consta de <b>{len(sup[0]['preguntas'])}</b> preguntas"
                  + (f" y <b>{len(sup[0].get('reserva', []))}</b> preguntas adicionales de reserva." if sup[0].get("reserva") else "."))
    li += [
        "Si encuentra dificultad en alguna de las preguntas no se detenga y continúe contestando las restantes.",
        f"Recuerde que el tiempo de realización de este ejercicio es de <b>{ex['tiempo_min']} MINUTOS</b>.",
        "Todas las preguntas del cuestionario tienen el mismo valor y contienen una sola respuesta correcta. "
        "Las respuestas erróneas serán penalizadas con <b>1/3</b> del valor de cada respuesta correcta. Las respuestas en blanco no penalizan.",
        "Para superar la primera parte se necesita una puntuación directa (A − E/3) igual o superior al 50 % de la máxima posible; "
        "la segunda parte solo se corrige si se supera la primera.",
    ]
    return "<div class='instr'><ol>" + "".join(f"<li>{x}</li>" for x in li) + "</ol></div>"


def cuestionario_html(ex):
    temas = ", ".join(t["codigo"] for t in ex["temas"])
    h = [f"<html><head><meta charset='utf-8'><title>{esc(ex['titulo'])}</title><style>{CSS}</style></head><body>"]
    h.append("<div class='cab'>SIMULACRO DE EXAMEN · CUERPO DE TÉCNICOS AUXILIARES DE INFORMÁTICA · INGRESO LIBRE<br>"
             "Elaborado a partir de las notas de la bóveda de estudio — no es un cuestionario oficial</div>")
    h.append(f"<h1>{esc(ex['titulo'])}</h1>")
    h.append(f"<div class='caja'>CUESTIONARIO {esc(ex['id'])}<br><span style='font-size:9pt;font-weight:normal'>Temas: {esc(temas)}</span></div>")
    h.append(instrucciones(ex))
    h.append("<div class='salto'></div><h2>PRIMERA PARTE</h2>")
    for i, q in enumerate(ex["parte1"]["preguntas"], 1):
        h.append(pregunta_html(i, q))
    if ex["parte1"].get("reserva"):
        h.append("<h3>Preguntas de reserva</h3>")
        for i, q in enumerate(ex["parte1"]["reserva"], 1):
            h.append(pregunta_html(i, q))
    for s in ex.get("supuestos", []):
        h.append(f"<div class='salto'></div><h2>SUPUESTO {s['id']}</h2>")
        h.append(f"<div class='enun'>{esc(s['enunciado'])}</div>")
        for i, q in enumerate(s["preguntas"], 1):
            h.append(pregunta_html(i, q))
        if s.get("reserva"):
            h.append("<h3>Preguntas de reserva</h3>")
            for i, q in enumerate(s["reserva"], 1):
                h.append(pregunta_html(i, q))
    h.append(hoja_respuestas(ex))
    h.append("</body></html>")
    return "".join(h)


def plantilla_html(ex):
    h = [f"<html><head><meta charset='utf-8'><title>Plantilla {esc(ex['id'])}</title><style>{CSS}</style></head><body>"]
    h.append(f"<h1>PLANTILLA DE RESPUESTAS</h1><div class='caja'>{esc(ex['titulo'])}<br>"
             f"<span style='font-size:9pt;font-weight:normal'>Cuestionario {esc(ex['id'])}</span></div>")

    def tabla_letras(nombre, qs, pref=""):
        celdas = "".join(f"<td><b>{pref}{i}</b> {q['correcta']}</td>" + ("</tr><tr>" if i % 10 == 0 else "")
                         for i, q in enumerate(qs, 1))
        return f"<h3>{nombre}</h3><table class='pl'><tr>{celdas}</tr></table>"

    h.append(tabla_letras("Primera parte", ex["parte1"]["preguntas"]))
    if ex["parte1"].get("reserva"):
        h.append(tabla_letras("Primera parte · reserva", ex["parte1"]["reserva"], "R"))
    for s in ex.get("supuestos", []):
        h.append(tabla_letras(f"Supuesto {s['id']}", s["preguntas"], "S"))
        if s.get("reserva"):
            h.append(tabla_letras(f"Supuesto {s['id']} · reserva", s["reserva"], "SR"))

    def just(nombre, qs, pref=""):
        filas = []
        for i, q in enumerate(qs, 1):
            filas.append(
                f"<tr><td><b>{pref}{i}</b></td><td><b>{q['correcta']}</b></td><td class='just'>{esc(q['justificacion'])}"
                f"<br><i>Fuente: {esc(q.get('fuente', ''))}</i></td><td>{esc(q.get('tema', ''))}</td></tr>")
        return (f"<h3>{nombre}</h3><table class='pl'><tr><th>Nº</th><th>Resp.</th><th>Por qué (y por qué no las otras)</th><th>Tema</th></tr>"
                + "".join(filas) + "</table>")

    h.append("<div class='salto'></div><h2>JUSTIFICACIÓN DE CADA RESPUESTA</h2>")
    h.append(just("Primera parte", ex["parte1"]["preguntas"]))
    if ex["parte1"].get("reserva"):
        h.append(just("Primera parte · reserva", ex["parte1"]["reserva"], "R"))
    for s in ex.get("supuestos", []):
        h.append(just(f"Supuesto {s['id']}", s["preguntas"], "S"))
        if s.get("reserva"):
            h.append(just(f"Supuesto {s['id']} · reserva", s["reserva"], "SR"))
    h.append("<div class='pie'>Puntuación por parte: A − E/3 · blanco no penaliza · corte 1ª parte: 50 % de la máxima</div>")
    h.append("</body></html>")
    return "".join(h)


def edge():
    for c in EDGE_CANDIDATES:
        if os.path.exists(c):
            return c
    sys.exit("No se encuentra Microsoft Edge ni Google Chrome para imprimir a PDF.")


def html_a_pdf(html_path, pdf_path):
    url = "file:///" + os.path.abspath(html_path).replace("\\", "/")
    cmd = [edge(), "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
           f"--print-to-pdf={os.path.abspath(pdf_path)}", url]
    subprocess.run(cmd, check=True, capture_output=True, timeout=120)
    if not os.path.exists(pdf_path):
        sys.exit(f"Edge no generó {pdf_path}")


def validar(ex):
    errores = []
    def chk(qs, et):
        for i, q in enumerate(qs, 1):
            for campo in ("enunciado", "opciones", "correcta", "justificacion", "fuente", "tema"):
                if campo not in q:
                    errores.append(f"{et}{i}: falta '{campo}'")
            if set(q.get("opciones", {})) != set("abcd"):
                errores.append(f"{et}{i}: opciones deben ser exactamente a,b,c,d")
            if q.get("correcta") not in ("a", "b", "c", "d"):
                errores.append(f"{et}{i}: 'correcta' inválida")
            ops = [q.get("opciones", {}).get(k, "").strip().lower() for k in "abcd"]
            if len(set(ops)) < 4:
                errores.append(f"{et}{i}: opciones repetidas")
            if q.get("fuera_de_notas"):
                errores.append(f"{et}{i}: marcada fuera_de_notas; solo se admiten preguntas sostenidas por las notas de la bóveda")
    chk(ex["parte1"]["preguntas"], "P")
    chk(ex["parte1"].get("reserva", []), "R")
    for s in ex.get("supuestos", []):
        chk(s["preguntas"], f"S{s['id']}-")
        chk(s.get("reserva", []), f"SR{s['id']}-")
    return errores


def cmd_pdf(json_path):
    ex = json.load(open(json_path, encoding="utf-8"))
    err = validar(ex)
    if err:
        sys.exit("JSON inválido:\n" + "\n".join(err))
    d = os.path.dirname(os.path.abspath(json_path))
    for nombre, fn in (("cuestionario", cuestionario_html), ("plantilla", plantilla_html)):
        hp = os.path.join(d, f"_{nombre}.html")
        open(hp, "w", encoding="utf-8").write(fn(ex))
        html_a_pdf(hp, os.path.join(d, f"{nombre}.pdf"))
        os.remove(hp)
    # reparto de letras correctas, para vigilar sesgos
    from collections import Counter
    todas = [q["correcta"] for q in ex["parte1"]["preguntas"]] + [q["correcta"] for s in ex.get("supuestos", []) for q in s["preguntas"]]
    print("OK", os.path.join(d, "cuestionario.pdf"), os.path.join(d, "plantilla.pdf"))
    print("Reparto de respuestas correctas:", dict(sorted(Counter(todas).items())))


def parse_respuestas(txt):
    r = {"P": {}, "R": {}, "S": {}, "SR": {}}
    for tok in re.split(r"[\s,;]+", txt.strip()):
        if not tok:
            continue
        m = re.fullmatch(r"(?i)(P|S):([a-d\-]+)", tok)
        if m:
            for i, c in enumerate(m.group(2).lower(), 1):
                if c != "-":
                    r[m.group(1).upper()][i] = c
            continue
        m = re.fullmatch(r"(?i)(SR|S|R)?(\d+)[:.)=]?([a-d\-])", tok)
        if not m:
            sys.exit(f"No entiendo la respuesta '{tok}'")
        pref = (m.group(1) or "P").upper()
        if m.group(3).lower() != "-":
            r[pref][int(m.group(2))] = m.group(3).lower()
    return r


def puntuar(qs, reserva, resp, resp_res, anuladas):
    """Sustituye anuladas por reservas en orden y calcula A, E, B."""
    efectivas = []  # (etiqueta, pregunta, respuesta)
    res_iter = iter(enumerate(reserva, 1))
    for i, q in enumerate(qs, 1):
        if i in anuladas:
            try:
                j, rq = next(res_iter)
                efectivas.append((f"R{j}", rq, resp_res.get(j)))
            except StopIteration:
                pass  # sin reserva: la pregunta desaparece y baja la máxima
            continue
        efectivas.append((str(i), q, resp.get(i)))
    A = sum(1 for _, q, x in efectivas if x == q["correcta"])
    E = sum(1 for _, q, x in efectivas if x and x != q["correcta"])
    B = len(efectivas) - A - E
    return efectivas, A, E, B


def escala(directa, maxima, corte):
    if directa < corte:
        return None
    if maxima == corte:
        return 50.0
    return 25 + 25 * (directa - corte) / (maxima - corte)


def cmd_corregir(json_path, txt, supuesto=None, anular="", corte2=0.5):
    ex = json.load(open(json_path, encoding="utf-8"))
    r = parse_respuestas(txt)
    an_p = {int(x) for x in re.findall(r"(?<![SR\d])(\d+)", anular.upper())}
    an_s = {int(x) for x in re.findall(r"S(\d+)", anular.upper())}
    out = {"id": ex["id"], "partes": []}
    lineas = [f"## Corrección · {ex['titulo']}", ""]

    def bloque(nombre, qs, res, rp, rr, anul, corte_frac, orientativo):
        ef, A, E, B = puntuar(qs, res, rp, rr, anul)
        maxima = len(ef)
        d = round(A - E / 3, 4)
        corte = corte_frac * maxima
        cal = escala(d, maxima, corte)
        por_tema = {}
        for et, q, x in ef:
            t = por_tema.setdefault(q.get("tema", "?"), {"A": 0, "E": 0, "B": 0})
            t["A" if x == q["correcta"] else ("E" if x else "B")] += 1
        fallos = [(et, q, x) for et, q, x in ef if x != q["correcta"]]
        lineas.append(f"### {nombre}")
        lineas.append(f"Aciertos **{A}** · Errores **{E}** · Blancos **{B}** · de {maxima}")
        lineas.append(f"Puntuación directa: {A} − {E}/3 = **{d:.2f} / {maxima}**  ({100 * d / maxima:.1f} %)")
        lineas.append(f"Nota de corte {'orientativa ' if orientativo else ''}({int(corte_frac * 100)} %): {corte:.2f} → "
                      + (f"**APTO**, calificación {cal:.2f} / 50" if cal is not None else "**NO APTO**"))
        lineas.append("")
        lineas.append("| Tema | A | E | B | Directa |")
        lineas.append("|---|---|---|---|---|")
        for t, v in por_tema.items():
            lineas.append(f"| {t} | {v['A']} | {v['E']} | {v['B']} | {v['A'] - v['E'] / 3:.2f} |")
        lineas.append("")
        if fallos:
            lineas.append("| Nº | Tu resp. | Correcta | Tema |")
            lineas.append("|---|---|---|---|")
            for et, q, x in fallos:
                lineas.append(f"| {et} | {x or '—'} | {q['correcta']} | {q.get('tema', '')} |")
            lineas.append("")
        parte = {"parte": nombre, "A": A, "E": E, "B": B, "maxima": maxima, "directa": d, "corte": corte,
                 "calificacion": cal, "por_tema": por_tema,
                 "fallos_y_blancos": [{"n": et, "resp": x, "correcta": q["correcta"], "tema": q.get("tema")} for et, q, x in fallos]}
        out["partes"].append(parte)
        return parte

    p1 = bloque("Primera parte", ex["parte1"]["preguntas"], ex["parte1"].get("reserva", []), r["P"], r["R"], an_p, 0.5, False)
    sups = ex.get("supuestos", [])
    if sups:
        if len(sups) > 1 and not supuesto:
            supuesto = None
            lineas.append("**Segunda parte: no se ha indicado el supuesto elegido (I o II) → no se corrige** (igual que en el examen real).")
        else:
            s = next((x for x in sups if x["id"] == (supuesto or sups[0]["id"])), None)
            if s is None:
                sys.exit(f"No existe el supuesto {supuesto}")
            if p1["calificacion"] is None:
                lineas.append("> ⚠ En el examen real la segunda parte **no se evaluaría** porque la primera no alcanza el corte. "
                              "Se corrige igualmente a efectos de entrenamiento.")
                lineas.append("")
            bloque(f"Supuesto {s['id']}", s["preguntas"], s.get("reserva", []), r["S"], r["SR"], an_s, corte2, True)
            c = [p["calificacion"] for p in out["partes"]]
            if all(x is not None for x in c):
                lineas.append(f"**Calificación total orientativa: {sum(c):.2f} / 100**")
    print("\n".join(lineas))
    json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(json_path)), "correccion.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    if sys.argv[1] == "pdf":
        cmd_pdf(sys.argv[2])
    elif sys.argv[1] == "corregir":
        args = sys.argv[3:]
        txt, sup, anu, c2 = "", None, "", 0.5
        i = 0
        while i < len(args):
            if args[i] == "--supuesto":
                sup = args[i + 1].upper(); i += 2
            elif args[i] == "--anular":
                anu = args[i + 1]; i += 2
            elif args[i] == "--corte2":
                c2 = float(args[i + 1]); i += 2
            else:
                txt += " " + args[i]; i += 1
        cmd_corregir(sys.argv[2], txt, sup, anu, c2)
    else:
        sys.exit(__doc__)
