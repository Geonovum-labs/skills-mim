#!/usr/bin/env python3
"""mim.py - deterministisch opzoeken in de kennisbank mim-kennis (MIM 1.2).

Alleen Python-standaardbibliotheek. Elke uitvoer noemt de MIM-paragraaf.
Vindt het script iets niet, dan zegt het dat (exitcode 1). Verzin dan niets.

Opdrachten:
  paragraaf <nr> [--met-sub]          letterlijke MIM-tekst van een paragraaf, bv. 2.3.2.1
  zoek <term>                         term, synoniem of Engelse term -> bestand en paragraaf
  element <naam>                      gegevens van een modelelement (stereotype, LD-klasse, paragrafen)
  metagegeven <element> [<naam>]      metagegevens van een element: kardinaliteit UML en LD, verplicht
        [--variant <tekst>]           alleen deze variant, bv. "alt 1" of "objecttypen"
  waarden <metagegeven>               toegestane waarden en defaultwaarde
  lijst elementen|metagegevens|termen alle namen die het script kent

Optie --json geeft machineleesbare uitvoer.

Zonder Python: zie de tabel 'Zonder scripts' in SKILL.md; dezelfde gegevens staan in data/*.json
en de letterlijke tekst in bron/*.md onder de kop "§<nr>".
"""
import json
import os
import re
import sys
import difflib
import unicodedata

BASIS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASIS, "data")
BRON = os.path.join(BASIS, "bron")


def laad(naam):
    with open(os.path.join(DATA, naam), encoding="utf-8") as f:
        return json.load(f)


def sleutel(s):
    """Vergelijkingssleutel: kleine letters, zonder accenten, «», streepjes en spaties."""
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower().replace("«", "").replace("»", "")
    s = re.sub(r"^mim:", "", s)
    return re.sub(r"[\s_\-./]+", "", s)


# ---------------------------------------------------------------- paragrafen
def bron_paragrafen():
    """Leest bron/*.md en geeft {nr: (titel, bestand, tekst_eigen)}."""
    index = laad_index()
    res = {}
    for bestand in sorted({p["bestand"] for p in index}):
        pad = os.path.join(BASIS, bestand)
        with open(pad, encoding="utf-8") as f:
            regels = f.read().split("\n")
        huidig = None
        buf = []
        for r in regels:
            m = re.match(r"^#{2,6} §([0-9A-Z][0-9.]*) (.*)$", r)
            if m:
                if huidig:
                    res[huidig[0]] = (huidig[1], bestand, "\n".join(buf).strip())
                huidig = (m.group(1), m.group(2))
                buf = []
            elif huidig:
                buf.append(r)
        if huidig:
            res[huidig[0]] = (huidig[1], bestand, "\n".join(buf).strip())
    return res


def laad_index():
    with open(os.path.join(BRON, "paragrafen.json"), encoding="utf-8") as f:
        return json.load(f)["paragrafen"]


def paragraaf_tekst(nr, met_sub=False):
    nr = nr.strip().lstrip("§").rstrip(".")
    par = bron_paragrafen()
    if nr not in par:
        return None
    if not met_sub:
        titel, bestand, tekst = par[nr]
        return {"nr": nr, "titel": titel, "bestand": bestand, "tekst": tekst}
    delen = []
    for k, (titel, bestand, tekst) in par.items():
        if k == nr or k.startswith(nr + "."):
            delen.append(f"§{k} {titel}\n\n{tekst}")
    return {"nr": nr, "titel": par[nr][0], "bestand": par[nr][1], "tekst": "\n\n".join(delen)}


def cmd_paragraaf(args, als_json):
    if not args:
        return gebruik()
    met_sub = "--met-sub" in args
    nr = [a for a in args if not a.startswith("--")][0]
    p = paragraaf_tekst(nr, met_sub)
    if p is None:
        return niet_gevonden(f"Paragraaf §{nr} bestaat niet in MIM 1.2 (zie bron/paragrafen.json).", als_json)
    p["bron"] = "MIM 1.2, vastgestelde versie 13 juni 2024 (CC BY 4.0)"
    if als_json:
        print(json.dumps(p, ensure_ascii=False, indent=1))
    else:
        print(f"MIM 1.2 §{p['nr']} {p['titel']}  [{p['bestand']}]\n")
        print(p["tekst"] or "(geen eigen tekst; zie subparagrafen met --met-sub)")
    return 0


# ---------------------------------------------------------------- woordenlijst
def cmd_zoek(args, als_json):
    if not args:
        return gebruik()
    term = " ".join(a for a in args if not a.startswith("--"))
    w = laad("woordenlijst.json")["termen"]
    k = sleutel(term)
    treffers = []
    for t in w:
        namen = [t["term"]] + t.get("synoniemen", []) + t.get("engels", [])
        if any(sleutel(n) == k for n in namen):
            treffers.append(t)
    for t in w:
        namen = [t["term"]] + t.get("synoniemen", []) + t.get("engels", [])
        if t not in treffers and any(k and len(k) > 2 and k in sleutel(n) for n in namen):
            treffers.append(t)
    treffers = treffers[:8]
    if not treffers:
        alle = {}
        for t in w:
            for n in [t["term"]] + t.get("synoniemen", []) + t.get("engels", []):
                alle[sleutel(n)] = t["term"]
        bijna = difflib.get_close_matches(k, list(alle), n=5, cutoff=0.75)
        tekst = f"'{term}' staat niet in de woordenlijst van mim-kennis."
        if bijna:
            tekst += " Bedoelde u: " + ", ".join(sorted({alle[b] for b in bijna})) + "?"
        tekst += " Meld de gebruiker dat de kennisbank dit niet bevat (zie SKILL.md, grondregel 4)."
        return niet_gevonden(tekst, als_json)
    if als_json:
        print(json.dumps(treffers, ensure_ascii=False, indent=1))
    else:
        for t in treffers:
            print(f"{t['term']}  ({t['soort']})")
            if t.get("paragrafen"):
                print("  MIM 1.2:   " + ", ".join("§" + p for p in t["paragrafen"]))
            print("  bestand:   " + t["bestand"])
            if t.get("synoniemen"):
                print("  ook:       " + ", ".join(t["synoniemen"]))
            if t.get("engels"):
                print("  Engels:    " + ", ".join(t["engels"]))
            if t.get("let_op"):
                print("  let op:    " + t["let_op"])
            print()
    return 0


# ---------------------------------------------------------------- elementen
def zoek_element(naam):
    els = laad("elementen.json")["elementen"]
    k = sleutel(naam)
    for e in els:
        namen = [e["id"], e["naam"]] + e.get("synoniemen", [])
        if e["ld"].get("klasse"):
            namen += re.findall(r"mim:([A-Za-z]+)", e["ld"]["klasse"])
        if any(sleutel(n) == k for n in namen):
            return e
    return None


def cmd_element(args, als_json):
    if not args:
        return gebruik()
    naam = " ".join(a for a in args if not a.startswith("--"))
    e = zoek_element(naam)
    if e is None:
        namen = [x["naam"] for x in laad("elementen.json")["elementen"]]
        bijna = difflib.get_close_matches(naam, namen, n=3, cutoff=0.6)
        return niet_gevonden(f"'{naam}' is geen MIM 1.2-modelelement in deze kennisbank."
                             + (f" Bedoelde u: {', '.join(bijna)}?" if bijna else "")
                             + " Gebruik 'zoek' voor andere termen.", als_json)
    if als_json:
        print(json.dumps(e, ensure_ascii=False, indent=1))
        return 0
    p = e["paragrafen"]
    print(f"{e['naam']}  (groep: {e['groep']})")
    print(f"  bestand:          {e['bestand']}")
    print(f"  definitie:        MIM 1.2 §{p['algemeen']}")
    if p["uml"]:
        print(f"  UML:              " + ", ".join("§" + x for x in p["uml"]))
    if p["ld"]:
        print(f"  Linked Data:      " + ", ".join("§" + x for x in p["ld"]))
    if p["transformatie"]:
        print(f"  transformatie:    " + ", ".join("§" + x for x in p["transformatie"]))
    if p["afspraken_regels"]:
        print(f"  afspraken/regels: " + ", ".join("§" + x for x in p["afspraken_regels"]))
    print(f"  UML-stereotype:   {e['uml'].get('stereotype') or '-'}")
    print(f"  UML-metaclass:    {e['uml'].get('uml_metaclass') or '-'}   (EA: {e['uml'].get('ea') or '-'})")
    print(f"  LD-klasse:        {e['ld'].get('klasse') or '-'}")
    if e.get("opmerking"):
        print(f"  opmerking:        {e['opmerking']}")
    return 0


# ---------------------------------------------------------------- metagegevens
def metagegevens_van(element_id, naam=None, variant=None):
    regels = laad("metagegevens.json")["regels"]
    res = [r for r in regels if r["element"] == element_id]
    if variant:
        v = sleutel(variant)
        res = [r for r in res if r["variant"] and v in sleutel(r["variant"])]
    if naam:
        k = sleutel(naam)
        exact = [r for r in res if sleutel(r["metagegeven"]) == k
                 or sleutel(r["metagegeven"]).replace("heeft", "") == k
                 or any(sleutel(x.get("label_in_bron", "")) == k for x in (r["uml"] or {}, r["ld"] or {}))]
        if not exact:
            exact = [r for r in res if k in sleutel(r["metagegeven"])]
        res = exact
    return res


def markdown_tabel(element_id):
    """Tabel zoals opgenomen in modelelementen/<id>.md (gegenereerd blok)."""
    regels = metagegevens_van(element_id)
    if not regels:
        return "_MIM 1.2 geeft voor dit element geen eigen metagegevenstabel in §3.2 of §4.3._\n"
    varianten = []
    for r in regels:
        if r["variant"] not in varianten:
            varianten.append(r["variant"])
    uit = []
    for v in varianten:
        if v:
            uit.append(f"**Variant: {v}**\n")
        uit.append("| Metagegeven | Betekenis | UML | LD | Verplicht | Verschil UML/LD |")
        uit.append("|---|---|---|---|---|---|")
        for r in [x for x in regels if x["variant"] == v]:
            u = r["uml"]
            l = r["ld"]
            uc = f"`{u['kardinaliteit']}` (§{u['paragraaf']})" if u else "-"
            lc = f"`{l['kardinaliteit']}` (§{l['paragraaf']})" if l else "-"
            pa = " / ".join("§" + x.strip() for x in r["paragraaf_algemeen"].split("/")) if r["paragraaf_algemeen"] else "-"
            vs = "ja" if r["verschil"] else ""
            uit.append(f"| {r['metagegeven']} | {pa} | {uc} | {lc} | {r['verplicht']} | {vs} |")
        uit.append("")
    return "\n".join(uit)


def cmd_metagegeven(args, als_json):
    pos = [a for a in args if not a.startswith("--")]
    variant = None
    if "--variant" in args:
        i = args.index("--variant")
        if i + 1 < len(args):
            variant = args[i + 1]
            pos = [a for a in pos if a != variant]
    if not pos:
        return gebruik()
    e = zoek_element(pos[0])
    if e is None:
        return niet_gevonden(f"'{pos[0]}' is geen MIM 1.2-modelelement in deze kennisbank.", als_json)
    naam = " ".join(pos[1:]) if len(pos) > 1 else None
    res = metagegevens_van(e["id"], naam, variant)
    if not res:
        if naam:
            return niet_gevonden(f"Metagegeven '{naam}' staat niet in de tabellen van MIM 1.2 voor {e['naam']} "
                                 f"(§{', §'.join(e['paragrafen']['uml'] + e['paragrafen']['ld'])}). "
                                 "Dat betekent: niet toegestaan voor dit element, tenzij een extensie het toevoegt.", als_json)
        return niet_gevonden(f"MIM 1.2 geeft voor {e['naam']} geen metagegevenstabel.", als_json)
    if als_json:
        print(json.dumps(res, ensure_ascii=False, indent=1))
        return 0
    print(f"Metagegevens van {e['naam']} volgens MIM 1.2 (§3.2 UML, §4.3 LD):\n")
    for r in res:
        v = f" [{r['variant']}]" if r["variant"] else ""
        u = r["uml"]
        l = r["ld"]
        print(f"- {r['metagegeven']}{v}: {r['verplicht']}")
        if r["paragraaf_algemeen"]:
            print(f"    betekenis: §{r['paragraaf_algemeen']}")
        print(f"    UML: {u['kardinaliteit'] + ' (§' + u['paragraaf'] + ')' if u else 'niet in de UML-tabel'}")
        ldt = 'niet in de LD-tabel'
        if l:
            ldt = l['kardinaliteit'] + ' (§' + l['paragraaf'] + ')'
            if l.get('ld_eigenschap'):
                ldt += ', eigenschap ' + l['ld_eigenschap']
        print(f"    LD:  {ldt}")
        if r["verschil"]:
            print(f"    let op: {r['verschil']} - niet zelf oplossen, meld het verschil.")
    return 0


def cmd_waarden(args, als_json):
    if not args:
        return gebruik()
    naam = " ".join(a for a in args if not a.startswith("--"))
    k = sleutel(naam)
    w = laad("waardebereik.json")["metagegevens"]
    res = [x for x in w if sleutel(x["metagegeven"]) == k] or [x for x in w if k in sleutel(x["metagegeven"])]
    if not res:
        return niet_gevonden(f"Voor '{naam}' legt MIM 1.2 geen waardebereik of default vast in §2.4.5 "
                             "(of het metagegeven bestaat niet). Zie metagegevens.md.", als_json)
    if als_json:
        print(json.dumps(res, ensure_ascii=False, indent=1))
        return 0
    for x in res:
        print(x["metagegeven"])
        if x.get("waarden"):
            print(f"  waarden: {', '.join(x['waarden'])}  (§{x['paragraaf_waarden']})")
        elif x.get("patroon"):
            print(f"  patroon: {x['patroon']}  (§{x['paragraaf_waarden']})")
        else:
            print("  waarden: geen waardebereik vastgelegd in §2.4.5.1")
        if x.get("ld_waarden"):
            print(f"  LD:      {', '.join(x['ld_waarden'])}  (§{x['paragraaf_ld']})")
        print(f"  default: {x['default'] + '  (§' + x['paragraaf_default'] + ')' if x.get('default') else 'geen default'}")
        if x.get("opmerking"):
            print(f"  let op:  {x['opmerking']}")
    return 0


def cmd_lijst(args, als_json):
    soort = args[0] if args else "elementen"
    if soort.startswith("element"):
        namen = [e["naam"] for e in laad("elementen.json")["elementen"]]
    elif soort.startswith("metagegeven"):
        namen = sorted({r["metagegeven"] for r in laad("metagegevens.json")["regels"]})
    elif soort.startswith("term"):
        namen = sorted(t["term"] for t in laad("woordenlijst.json")["termen"])
    else:
        return gebruik()
    print(json.dumps(namen, ensure_ascii=False) if als_json else "\n".join(namen))
    return 0


# ---------------------------------------------------------------- algemeen
def niet_gevonden(tekst, als_json):
    if als_json:
        print(json.dumps({"gevonden": False, "melding": tekst}, ensure_ascii=False))
    else:
        print("NIET GEVONDEN: " + tekst)
    return 1


def gebruik():
    print(__doc__)
    return 2


def main(argv):
    als_json = "--json" in argv
    argv = [a for a in argv if a != "--json"]
    if not argv:
        return gebruik()
    cmd, args = argv[0], argv[1:]
    tabel = {"paragraaf": cmd_paragraaf, "zoek": cmd_zoek, "element": cmd_element,
             "metagegeven": cmd_metagegeven, "metagegevens": cmd_metagegeven,
             "waarden": cmd_waarden, "lijst": cmd_lijst}
    if cmd not in tabel:
        return gebruik()
    return tabel[cmd](args, als_json)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
