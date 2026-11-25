#!/usr/bin/env python3
"""mim_data.py - deterministisch opzoeken voor datavragen met een MIM-model (mim-combi).

Alleen Python-standaardbibliotheek. Zoekt op in vaste JSON-bestanden en drukt het resultaat af;
het script interpreteert niets en gokt niets. Het bevat zelf geen modelkennis: je geeft de
modelcatalogus (--catalogus) of de elementsamenvattingen (--samenvattingen) van het model mee.
Vindt het script iets niet, dan zegt het "NIET GEVONDEN" (exitcode 1). Verzin dan niets.

Opdrachten:
  catalogus     --catalogus <bestand>                           product -> model, modellen die je niet koppelt
  koppel        --catalogus <bestand> --product <id> --velden a,b,c
                                                                veld -> element + koppeltype
  samenvatting  --samenvattingen <bestand> <Objecttype[.attribuut]>
                                                                één elementsamenvatting
  waardelijst   --samenvattingen <bestand> <Waardelijst>        exacte waarden van een waardelijst
  rdf-labels    <bestand-of-url> [--sta-toe <host>]             snelle scan van labels en typen in RDF

Optie --json (overal) geeft machineleesbare uitvoer.

Formaten: modellen-lezen/modelcatalogus.md, veldkoppeling.md, elementsamenvatting.md.
De JSON-sleutels volgen het formaat van skills-mim (Engels), zodat bestanden uitwisselbaar zijn.
Herkomst: mim_core.py en mim_interpret.py uit skills-mim, samengevoegd en vertaald.
"""
import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from urllib.parse import urlparse

STANDAARD_HOSTS = (
    "geostandaarden.nl",
    "overheid.nl",
    "pdok.nl",
    "kadaster.nl",
    "catalog.modeldesk.io",
)
GITHUB_HOSTS = ("raw.githubusercontent.com", "github.com")

OK = 0
NIET_GEVONDEN = 1
GEBRUIK = 2
NIET_TOEGESTAAN = 4
OPHALEN_MISLUKT = 5


def laad(pad):
    if not os.path.isfile(pad):
        print(f"NIET GEVONDEN: bestand {pad}", file=sys.stderr)
        sys.exit(NIET_GEVONDEN)
    with open(pad, encoding="utf-8") as f:
        return json.load(f)


def uit(data, als_json, tekst):
    if als_json:
        json.dump(data, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
    else:
        sys.stdout.write(tekst if tekst.endswith("\n") else tekst + "\n")


def norm(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").casefold())


# ------------------------------------------------------------------ catalogus
def cmd_catalogus(pad, als_json):
    cat = laad(pad)
    regels = [f"modelcatalogus {pad}  versie {cat.get('version')}  laatst gecontroleerd {cat.get('lastVerified')}", ""]
    for p in cat.get("products", []):
        m = p.get("model") or {}
        regels.append(f"- {p['id']}: {p.get('name')}")
        regels.append(f"    model={m.get('id')} ({m.get('informatiemodeltype')}, bronkwaliteit={m.get('fidelity')}, MIM {m.get('mimVersion')})")
        regels.append(f"    veldkoppeling={p.get('verifiedMapping') or 'geen'}")
        if p.get("homonymReject"):
            regels.append(f"    niet koppelen: {', '.join(p['homonymReject'])}")
        if p.get("elementSummaries"):
            regels.append(f"    elementsamenvattingen: {p['elementSummaries']}")
        if p.get("note"):
            regels.append(f"    let op: {p['note']}")
    if cat.get("deadUrls"):
        regels.append("\ndode URL's:")
        regels.extend(f"  - {u}" for u in cat["deadUrls"])
    uit(cat, als_json, "\n".join(regels))
    return OK


# ------------------------------------------------------------------ koppel
def cmd_koppel(pad, product, velden, als_json):
    cat = laad(pad)
    producten = {p["id"]: p for p in cat.get("products", [])}
    if product not in producten:
        print(f"NIET GEVONDEN: product '{product}'. Bekend: {', '.join(sorted(producten))}", file=sys.stderr)
        return NIET_GEVONDEN
    naam = producten[product].get("verifiedMapping")
    if not naam:
        print(f"NIET GEVONDEN: product '{product}' heeft geen vastgestelde veldkoppeling. "
              "Koppel niet op naam; noem de velden niet-gekoppeld.", file=sys.stderr)
        return NIET_GEVONDEN
    koppeling = laad(os.path.join(os.path.dirname(os.path.abspath(pad)), naam))
    per_veld = {r["field"]: r for r in koppeling.get("fields", [])}
    rijen, onbekend = [], []
    for v in velden:
        hit = per_veld.get(v) or per_veld.get(v.replace(".", "_"))
        if hit is None:
            onbekend.append(v)
            rijen.append({"field": v, "mappingType": "unmapped", "element": None,
                          "confidence": "none", "reasons": ["niet-in-veldkoppeling"]})
        else:
            rijen.append(hit)
    data = {"product": product, "model": koppeling.get("model"), "reviewedBy": koppeling.get("reviewedBy"),
            "rows": rijen, "unknownFields": onbekend}
    regels = [f"{product} → {koppeling.get('model')}  ({len(rijen)} velden; beoordeeld door: {koppeling.get('reviewedBy') or 'nog niemand'})", ""]
    regels.append(f"{'veld':<28} {'koppeltype':<17} {'element':<36} zekerheid")
    regels.append("-" * 92)
    for r in rijen:
        regels.append(f"{r['field']:<28} {r.get('mappingType', ''):<17} {str(r.get('element') or '—'):<36} {r.get('confidence')}")
        if r.get("notes"):
            regels.append(f"{'':<28} let op: {r['notes']}")
    if onbekend:
        regels.append("\nNiet in de veldkoppeling (unmapped): " + ", ".join(onbekend))
    uit(data, als_json, "\n".join(regels))
    return OK


# ------------------------------------------------------------------ samenvatting
def index_namen(sam):
    idx = {}
    for sleutel, el in (sam.get("elements") or {}).items():
        idx[norm(sleutel)] = sleutel
        eig = el.get("owner")
        for n in [el.get("naam")] + list(el.get("alias") or []):
            if n:
                idx[norm(n)] = sleutel
                if eig:
                    idx[norm(f"{eig}.{n}")] = sleutel
    return idx


def cmd_samenvatting(pad, vraag, als_json):
    sam = laad(pad)
    els = sam.get("elements") or {}
    sleutel = vraag if vraag in els else index_namen(sam).get(norm(vraag))
    if not sleutel:
        kandidaten = [k for k in els if norm(vraag) in norm(k)]
        if len(kandidaten) == 1:
            sleutel = kandidaten[0]
        elif kandidaten:
            print("NIET GEVONDEN: niet eenduidig. Kandidaten: " + ", ".join(kandidaten[:10]), file=sys.stderr)
            return NIET_GEVONDEN
        else:
            print(f"NIET GEVONDEN: geen elementsamenvatting voor '{vraag}'. Verzin geen element.", file=sys.stderr)
            return NIET_GEVONDEN
    el = els[sleutel]
    data = {"id": sleutel, "model": sam.get("model"), "fidelity": sam.get("fidelity"),
            "source": sam.get("source"), "element": el}
    jn = lambda b: "Ja" if b else "Nee"  # noqa: E731
    regels = [f"{el.get('kind')}: {el.get('naam') or sleutel}   [{sam.get('model')}, bronkwaliteit {sam.get('fidelity')}]",
              f"code: {el.get('code', '—')}   hoort bij: {el.get('owner', '—')}"]
    for k in ("definitie", "populatie"):
        if k in el:
            regels.append(f"{k}: {el[k]}")
    delen = []
    if "kardinaliteit" in el:
        delen.append(f"kardinaliteit={el['kardinaliteit']}")
    if "mogelijkGeenWaarde" in el:
        delen.append(f"mogelijk geen waarde={jn(el['mogelijkGeenWaarde'])}")
    if "authentiek" in el:
        delen.append(f"authentiek={el['authentiek']}")
    if "datatype" in el:
        delen.append(f"type={el['datatype']}" + (f" ({el['waardelijstKind']})" if el.get("waardelijstKind") else ""))
    if el.get("historie"):
        h = el["historie"]
        delen.append(f"historie materieel/formeel={jn(h.get('materieel'))}/{jn(h.get('formeel'))}")
    if delen:
        regels.append("  ".join(delen))
    for k, label in (("identificerend", "identificerend"), ("abstract", "abstract"), ("supertypes", "supertypen"),
                     ("attributes", "attribuutsoorten"), ("rol", "rol"), ("doel", "doel")):
        if k in el:
            w = el[k]
            regels.append(f"{label}: {', '.join(w) if isinstance(w, list) else (jn(w) if isinstance(w, bool) else w)}")
    if el.get("note"):
        regels.append(f"let op: {el['note']}")
    regels.append(f"bron: {sam.get('source')}")
    uit(data, als_json, "\n".join(regels))
    return OK


def cmd_waardelijst(pad, naam, als_json):
    sam = laad(pad)
    lijsten = sam.get("valuelists") or {}
    sleutel = next((k for k in lijsten if norm(k) == norm(naam)), None)
    if not sleutel:
        print(f"NIET GEVONDEN: geen waardelijst '{naam}'. Bekend: {', '.join(lijsten)}", file=sys.stderr)
        return NIET_GEVONDEN
    data = {"id": sleutel, **lijsten[sleutel]}
    soort = lijsten[sleutel].get("kind") or "Enumeratie"
    regels = [f"{soort} {sleutel}  (de naam is de uitgewisselde waarde; gebruik hem letterlijk)", ""]
    for w in lijsten[sleutel].get("values") or []:
        regels.append(f"- {w['naam']}" + (f"  — {w['definitie']}" if w.get("definitie") else ""))
    uit(data, als_json, "\n".join(regels))
    return OK


# ------------------------------------------------------------------ rdf-labels
def host_toegestaan(url, extra):
    host = (urlparse(url).hostname or "").casefold()
    if not host:
        return False
    if any(host == d or host.endswith("." + d) for d in list(STANDAARD_HOSTS) + extra):
        return True
    if host in GITHUB_HOSTS:
        pad = urlparse(url).path.casefold()
        return pad.startswith("/geonovum/")
    return False


def haal_op(url, extra):
    if not host_toegestaan(url, extra):
        raise PermissionError(f"host staat niet op de lijst van toegestane hosts: {url}")
    req = urllib.request.Request(url, headers={"User-Agent": "mim-combi/0.1",
                                               "Accept": "text/turtle, application/rdf+xml, text/plain"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.read(2_000_000).decode("utf-8", errors="replace")
    except urllib.error.URLError as e:
        raise RuntimeError(f"ophalen mislukt: {e}") from e


_TTL_TYPE = re.compile(r"<([^>]+)>\s+a\s+([^\s;]+)", re.I)
_TTL_PRED = re.compile(r"<([^>]+)>\s+(rdfs:label|rdfs:comment|skos:prefLabel|"
                       r"<http://www\.w3\.org/2000/01/rdf-schema#label>|"
                       r"<http://www\.w3\.org/2000/01/rdf-schema#comment>)\s+\"([^\"]+)\"", re.I)
_TTL_PREFIX = re.compile(r"\b([A-Za-z][\w\-]*:[A-Za-z][\w\-]*)\s+a\s+([^\s;]+).*?"
                         r"(?:rdfs:label|skos:prefLabel)\s+\"([^\"]+)\"", re.S)
_XML_DESC = re.compile(r'<(?:rdf:)?Description[^>]*rdf:about="([^"]+)"[^>]*>(.*?)</(?:rdf:)?Description>', re.I | re.S)
_XML_LABEL = re.compile(r"<(?:rdfs:)?label[^>]*>([^<]+)</(?:rdfs:)?label>", re.I)
_XML_COMMENT = re.compile(r"<(?:rdfs:)?comment[^>]*>([^<]+)</(?:rdfs:)?comment>", re.I)
_XML_TYPE = re.compile(r'<(?:rdf:)?type[^>]*rdf:resource="([^"]+)"', re.I)


def scan_rdf(tekst):
    gevonden = {}

    def knoop(uri):
        return gevonden.setdefault(uri, {"uri": uri, "types": [], "labels": [], "comments": []})

    if "<rdf:RDF" in tekst or "<RDF" in tekst:
        for about, lijf in _XML_DESC.findall(tekst):
            k = knoop(about)
            k["labels"] += [x.strip() for x in _XML_LABEL.findall(lijf) if x.strip()]
            k["comments"] += [x.strip() for x in _XML_COMMENT.findall(lijf) if x.strip()]
            k["types"] += _XML_TYPE.findall(lijf)
    else:
        for uri, t in _TTL_TYPE.findall(tekst):
            knoop(uri)["types"].append(t.rstrip(" ;,."))
        for uri, pred, lit in _TTL_PRED.findall(tekst):
            knoop(uri)["comments" if "comment" in pred.casefold() else "labels"].append(lit)
        for uri, t, label in _TTL_PREFIX.findall(tekst):
            k = knoop(uri)
            k["types"].append(t.rstrip(" ;,."))
            k["labels"].append(label)
    for k in gevonden.values():
        for veld in ("types", "labels", "comments"):
            k[veld] = list(dict.fromkeys(k[veld]))
    return list(gevonden.values())


def cmd_rdf_labels(doel, extra, als_json):
    try:
        if os.path.isfile(doel):
            with open(doel, encoding="utf-8", errors="replace") as f:
                tekst = f.read()
        elif doel.startswith(("http://", "https://")):
            tekst = haal_op(doel, extra)
        else:
            print(f"NIET GEVONDEN: geen bestand of URL: {doel}", file=sys.stderr)
            return GEBRUIK
    except PermissionError as e:
        print(f"NIET TOEGESTAAN: {e}. Voeg de host toe met --sta-toe als dat klopt.", file=sys.stderr)
        return NIET_TOEGESTAAN
    except RuntimeError as e:
        print(f"MISLUKT: {e}. Beweer niet dat de link werkte.", file=sys.stderr)
        return OPHALEN_MISLUKT
    if "Attribuuttype" in tekst and "Relatietype" in tekst:
        print("STOP: dit lijkt MIM 2.0-vocabulaire (Attribuuttype, Relatietype). Niet ondersteund; lees het niet als MIM 1.2.",
              file=sys.stderr)
        return NIET_GEVONDEN
    knopen = scan_rdf(tekst)[:40]
    data = {"source": doel, "note": "Snelle labelscan, geen volledige RDF-lezer en geen volledig model. Koppel eerst het model.",
            "count": len(knopen), "nodes": knopen}
    regels = [f"rdf-labels {doel}  ({len(knopen)} knopen, snelle labelscan)", ""]
    for k in knopen[:20]:
        regels.append(f"- {k['uri']}: {(k['labels'] or ['—'])[0]}  [{','.join(k['types'][:3]) or '—'}]")
    if len(knopen) > 20:
        regels.append(f"… nog {len(knopen) - 20} (gebruik --json)")
    uit(data, als_json, "\n".join(regels))
    return OK


# ------------------------------------------------------------------ main
def parser():
    p = argparse.ArgumentParser(prog="mim_data.py", description="Deterministisch opzoeken voor datavragen met een MIM-model.")
    p.add_argument("--json", action="store_true", help="machineleesbare uitvoer")
    sub = p.add_subparsers(dest="cmd")
    c = sub.add_parser("catalogus", help="product -> model uit een modelcatalogus")
    c.add_argument("--catalogus", required=True)
    k = sub.add_parser("koppel", help="velden opzoeken in de vastgestelde veldkoppeling")
    k.add_argument("--catalogus", required=True)
    k.add_argument("--product", required=True)
    k.add_argument("--velden", required=True, help="veldnamen, gescheiden door komma's")
    s = sub.add_parser("samenvatting", help="één elementsamenvatting")
    s.add_argument("--samenvattingen", required=True)
    s.add_argument("element", help="Objecttype of Objecttype.attribuut")
    w = sub.add_parser("waardelijst", help="waarden van één waardelijst")
    w.add_argument("--samenvattingen", required=True)
    w.add_argument("naam")
    r = sub.add_parser("rdf-labels", help="labels en typen uit Turtle of RDF/XML (snelle scan)")
    r.add_argument("doel", help="bestand of URL")
    r.add_argument("--sta-toe", action="append", default=[], help="extra toegestane host")
    return p


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    als_json = "--json" in argv
    argv = [a for a in argv if a != "--json"]
    args = parser().parse_args(argv)
    if args.cmd == "catalogus":
        return cmd_catalogus(args.catalogus, als_json)
    if args.cmd == "koppel":
        velden = [v.strip() for v in args.velden.split(",") if v.strip()]
        if not velden:
            print("--velden is leeg", file=sys.stderr)
            return GEBRUIK
        return cmd_koppel(args.catalogus, args.product, velden, als_json)
    if args.cmd == "samenvatting":
        return cmd_samenvatting(args.samenvattingen, args.element, als_json)
    if args.cmd == "waardelijst":
        return cmd_waardelijst(args.samenvattingen, args.naam, als_json)
    if args.cmd == "rdf-labels":
        return cmd_rdf_labels(args.doel, args.sta_toe, als_json)
    parser().print_help()
    return GEBRUIK


if __name__ == "__main__":
    sys.exit(main())
