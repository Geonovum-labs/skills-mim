#!/usr/bin/env python3
"""check_kennisbank.py - controleert de kennisbank mim-kennis zelf (alleen standaardbibliotheek).

Controles:
  1. frontmatter: verplichte velden en toegestane waarden per kennisbestand
  2. citaten: elke blockquote die eindigt op '— MIM 1.2, §<nr> (...)' staat woordelijk in die paragraaf
  3. paragraafverwijzingen: elk '§<nr>' in de tekst bestaat in MIM 1.2
  4. links: relatieve links en bestandsnamen tussen backticks wijzen naar een bestaand bestand
  5. gegenereerde blokken (metagegevenstabellen) zijn gelijk aan data/metagegevens.json
  6. SKILL.md telt minder dan 500 regels
  7. elk JSON-bestand in data/ heeft een veld 'about'

Gebruik: python3 scripts/check_kennisbank.py [--stil]
Exitcode 0 = alles in orde, 1 = fouten gevonden.
"""
import json
import os
import re
import sys

BASIS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASIS, "scripts"))
import mim  # noqa: E402

SLA_OVER = {"bron", "beheer", "assets", "evaluatie"}
STATUS = {"normatief", "toelichtend"}
VERPLICHT = ["id", "titel", "bron", "mim-versie", "status"]
CITAAT_BRON = re.compile(r"^—\s*MIM 1\.2,\s*§([0-9A-Z][0-9.]*[0-9A-Z])\s*(?:\(([^)]*)\))?\s*$")
BEGIN = re.compile(r"<!-- BEGIN GEGENEREERD: metagegevens ([a-z\-]+) -->")
EINDE = "<!-- EINDE GEGENEREERD -->"

fouten = []


def fout(bestand, tekst):
    fouten.append(f"{bestand}: {tekst}")


def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("´", "'")
    s = s.replace("\\|", "|")
    s = re.sub(r"[`*_]", "", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"^\s*>\s?", "", s, flags=re.M)
    s = re.sub(r"^\s*(?:[-*]|\d+\.)\s+", "", s, flags=re.M)
    return re.sub(r"\s+", " ", s).strip()


def kennisbestanden():
    for wortel, mappen, bestanden in os.walk(BASIS):
        rel = os.path.relpath(wortel, BASIS)
        if rel.split(os.sep)[0] in SLA_OVER:
            continue
        for b in bestanden:
            if b.endswith(".md"):
                yield os.path.relpath(os.path.join(wortel, b), BASIS)


def frontmatter(tekst):
    if not tekst.startswith("---\n"):
        return None, tekst
    eind = tekst.find("\n---", 4)
    if eind < 0:
        return None, tekst
    fm = {}
    for r in tekst[4:eind].split("\n"):
        m = re.match(r"^([a-z\-]+):\s*(.*)$", r)
        if m:
            fm[m.group(1)] = m.group(2).strip()
    return fm, tekst[eind + 4:]


def check_frontmatter(rel, fm):
    if rel in ("SKILL.md", "LEESMIJ.md"):
        return
    if fm is None:
        fout(rel, "frontmatter ontbreekt")
        return
    for v in VERPLICHT:
        if v not in fm:
            fout(rel, f"frontmatter mist '{v}'")
    if fm.get("status") and fm["status"] not in STATUS:
        fout(rel, f"status '{fm['status']}' niet in {sorted(STATUS)}")
    if fm.get("mim-versie") and fm["mim-versie"].strip('"') != "1.2":
        fout(rel, "mim-versie moet \"1.2\" zijn")
    if rel.startswith("modelelementen/") and "metaclass" not in fm:
        fout(rel, "frontmatter mist 'metaclass'")
    if fm.get("id") and rel.startswith(("modelelementen/", "onderwerpen/", "onderscheidingen/", "uitdrukkingen/")):
        verwacht = os.path.splitext(os.path.basename(rel))[0]
        if fm["id"] != verwacht:
            fout(rel, f"id '{fm['id']}' wijkt af van bestandsnaam '{verwacht}'")


def zonder_codeblokken(tekst):
    """Vervangt regels binnen ``` ... ``` door lege regels (voorbeelden worden niet gecontroleerd)."""
    uit = []
    binnen = False
    for r in tekst.split("\n"):
        if r.strip().startswith("```"):
            binnen = not binnen
            uit.append("")
            continue
        uit.append("" if binnen else r)
    return "\n".join(uit)


def check_citaten(rel, tekst, paragrafen):
    regels = zonder_codeblokken(tekst).split("\n")
    blok = []
    aantal = 0
    for r in regels + [""]:
        if r.startswith(">"):
            blok.append(r)
            continue
        if blok:
            inhoud = [re.sub(r"^>\s?", "", x) for x in blok]
            while inhoud and not inhoud[-1].strip():
                inhoud.pop()
            if inhoud:
                m = CITAAT_BRON.match(inhoud[-1].strip())
                if m:
                    aantal += 1
                    nr, aard = m.group(1), (m.group(2) or "")
                    if nr not in paragrafen:
                        fout(rel, f"citaat verwijst naar onbekende §{nr}")
                    else:
                        if not aard:
                            fout(rel, f"citaat §{nr}: aard ontbreekt, schrijf '(normatief)' of '(niet-normatief, ...)'")
                        elif not (aard.startswith("normatief") or aard.startswith("niet-normatief")):
                            fout(rel, f"citaat §{nr}: aard '{aard}' moet beginnen met 'normatief' of 'niet-normatief'")
                        bron = norm(sub_tekst(paragrafen, nr))
                        citaat = "\n".join(inhoud[:-1])
                        for deel in re.split(r"\[…\]|\[\.\.\.\]", citaat):
                            d = norm(deel)
                            if d and d not in bron:
                                fout(rel, f"citaat §{nr} staat niet letterlijk in de bron: '{d[:90]}…'")
            blok = []
    return aantal


_sub_cache = {}


def sub_tekst(paragrafen, nr):
    if nr not in _sub_cache:
        delen = [t for k, (_, _, t) in paragrafen.items() if k == nr or k.startswith(nr + ".")]
        _sub_cache[nr] = "\n".join(delen)
    return _sub_cache[nr]


def check_verwijzingen(rel, tekst, paragrafen):
    tekst = zonder_codeblokken(tekst)
    for m in re.finditer(r"§\s?([0-9]+(?:\.[0-9]+)*)", tekst):
        nr = m.group(1).rstrip(".")
        if nr not in paragrafen:
            fout(rel, f"verwijzing naar onbekende §{nr}")


def check_links(rel, tekst):
    map_ = os.path.dirname(os.path.join(BASIS, rel))
    for m in re.finditer(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", tekst):
        doel = m.group(1)
        if re.match(r"^[a-z]+:", doel):
            continue
        if not os.path.exists(os.path.normpath(os.path.join(map_, doel))):
            fout(rel, f"link naar niet-bestaand bestand '{doel}'")
    for m in re.finditer(r"`((?:modelelementen|onderwerpen|onderscheidingen|uitdrukkingen|data|scripts|bron|assets)/[^`\s]+?\.(?:md|json|csv|py|ttl))`", tekst):
        if "<" in m.group(1):
            continue  # sjabloon, bv. modelelementen/<naam>.md
        if not os.path.exists(os.path.join(BASIS, m.group(1))):
            fout(rel, f"verwijzing naar niet-bestaand bestand '{m.group(1)}'")
    for m in re.finditer(r"`([a-z\-]+\.md)`", tekst):
        b = m.group(1)
        if b in ("SKILL.md", "LEESMIJ.md") or os.path.exists(os.path.join(BASIS, b)):
            continue
        if os.path.exists(os.path.join(map_, b)):
            continue
        fout(rel, f"verwijzing naar niet-bestaand bestand '{b}'")


def check_gegenereerd(rel, tekst):
    for m in BEGIN.finditer(tekst):
        el = m.group(1)
        eind = tekst.find(EINDE, m.end())
        if eind < 0:
            fout(rel, f"gegenereerd blok '{el}' zonder einde")
            continue
        huidig = tekst[m.end():eind].strip()
        verwacht = mim.markdown_tabel(el).strip()
        if huidig != verwacht:
            fout(rel, f"gegenereerd blok metagegevens '{el}' is verouderd; draai beheer/bouw/vul_gegenereerd.py")


def main():
    stil = "--stil" in sys.argv
    paragrafen = mim.bron_paragrafen()
    n_bestanden = n_citaten = 0
    for rel in sorted(kennisbestanden()):
        with open(os.path.join(BASIS, rel), encoding="utf-8") as f:
            tekst = f.read()
        fm, lijf = frontmatter(tekst)
        check_frontmatter(rel, fm)
        n_citaten += check_citaten(rel, lijf, paragrafen)
        check_verwijzingen(rel, lijf, paragrafen)
        check_links(rel, lijf)
        check_gegenereerd(rel, lijf)
        if fm and fm.get("bron"):
            for nr in re.findall(r"[0-9]+(?:\.[0-9]+)*", fm["bron"]):
                if nr not in paragrafen:
                    fout(rel, f"frontmatter bron noemt onbekende §{nr}")
        n_bestanden += 1
    skill = os.path.join(BASIS, "SKILL.md")
    if os.path.exists(skill):
        n = sum(1 for _ in open(skill, encoding="utf-8"))
        if n >= 500:
            fout("SKILL.md", f"{n} regels; moet onder 500 blijven")
    else:
        fout("SKILL.md", "ontbreekt")
    for b in os.listdir(os.path.join(BASIS, "data")):
        if b.endswith(".json"):
            with open(os.path.join(BASIS, "data", b), encoding="utf-8") as f:
                if "about" not in json.load(f):
                    fout("data/" + b, "veld 'about' ontbreekt")
    if not stil or fouten:
        print(f"{n_bestanden} kennisbestanden, {n_citaten} letterlijke citaten gecontroleerd.")
    if fouten:
        print(f"{len(fouten)} fout(en):")
        for f_ in fouten:
            print("  - " + f_)
        return 1
    print("Geen fouten gevonden.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
