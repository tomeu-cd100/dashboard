# Parser genèric: llegeix tots els .xlsx de la carpeta i genera data.js
# Estructura esperada (full de notes Institut Consell de Cent):
#   Fila 1: títol a B1, després parelles [Matèria | Rec.] i al final Mitjana | Suspesos
#   Files d'alumnes: columna B numèrica
#   Fila "Mitjana Matèria": resum per matèria (final de la llista d'alumnes)
import zipfile, re, json, glob, os
import xml.etree.ElementTree as ET

NS = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"

def col_to_idx(col):
    n = 0
    for ch in col:
        n = n * 26 + (ord(ch) - 64)
    return n

def idx_to_col(n):
    s = ""
    while n > 0:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return s

def parse_xlsx(path):
    z = zipfile.ZipFile(path)
    root = ET.fromstring(z.read("xl/sharedStrings.xml"))
    ss = ["".join(t.text or "" for t in si.iter(f"{NS}t")) for si in root.findall(f"{NS}si")]

    sheet = ET.fromstring(z.read("xl/worksheets/sheet1.xml"))
    cells = {}
    for c in sheet.iter(f"{NS}c"):
        ref = c.get("r"); t = c.get("t"); v = c.find(f"{NS}v")
        if v is None: continue
        cells[ref] = ss[int(v.text)] if t == "s" else v.text

    def get(col, row): return cells.get(f"{col}{row}")

    # --- detectar matèries i columnes especials a la fila 1
    row1 = sorted([(col_to_idx(re.match(r"[A-Z]+", k).group()), k, val)
                   for k, val in cells.items() if k.endswith("1") and re.match(r"[A-Z]+1$", k)])
    subjects = []       # (nom, columna)
    avg_col = fails_col = None
    for idx, ref, val in row1:
        col = idx_to_col(idx)
        if col in ("A", "B"):     # A buit, B = títol
            continue
        if val == "Mitjana": avg_col = col; continue
        if val == "Suspesos": fails_col = col; continue
        if val and val.strip():
            subjects.append((val.strip(), col))

    title_cell = get("B", 1) or ""
    parts = [p.strip() for p in re.split(r"\n", title_cell) if p.strip()]
    title = parts[0] if parts else "Institut"
    group = parts[1] if len(parts) > 1 else os.path.splitext(os.path.basename(path))[0]
    term  = parts[2].title() if len(parts) > 2 else ""

    # --- files d'alumnes (B numèric) fins a la fila resum "Mitjana Matèria"
    students = []
    r = 3
    while True:
        b = get("B", r)
        if b is None and get("C", r) is None and r > 60:
            break
        if b == "Mitjana Matèria" or get("B", r) == "Mitjana Matèria":
            break
        if b is not None and re.fullmatch(r"\d+", str(b).strip() or ""):
            grades = {}
            for name, col in subjects:
                g = get(col, r)
                grades[name] = g.strip() if g else None
            avg_raw = get(avg_col, r) if avg_col else None
            avg = None
            if avg_raw:
                m = re.search(r"(\d+(?:\.\d+)?)", avg_raw)
                if m: avg = float(m.group(1))
            fails_raw = get(fails_col, r) if fails_col else None
            try: fails = int(fails_raw) if fails_raw else 0
            except: fails = 0
            students.append({"id": int(b), "grades": grades, "avg": avg, "fails": fails})
        r += 1
        if r > 250: break

    return {
        "title": title, "group": group, "term": term,
        "subjects": [s[0] for s in subjects],
        "students": students,
    }

groups = []
for path in sorted(glob.glob("*.xlsx")):
    if path.startswith("~$"): continue
    try:
        groups.append(parse_xlsx(path))
        print(f"OK {path}: {len(groups[-1]['students'])} alumnes, {len(groups[-1]['subjects'])} materies")
    except Exception as e:
        print(f"ERROR {path}: {e}")

with open("data.js", "w", encoding="utf-8") as f:
    f.write("window.GROUPS = " + json.dumps(groups, ensure_ascii=False, indent=1) + ";")
print("data.js escrit amb", len(groups), "grups")
