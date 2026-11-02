#!/usr/bin/env python3
"""Deterministic helper for geonovum-mim-interpret (v1).

Stdlib only. Looks things up in fixed JSON files and prints the result; it
never interprets or guesses. Works for any MIM-conformant model and any data
product: pass the model catalog with --catalog (format:
../references/model-catalog.md, template: ../templates/model-catalog.template.json).
Verified field mapping files are named in the catalog and resolved relative to
the catalog file. Element summaries and the RDF label scan come from the
sibling mim-core pack.

Commands: catalog | map | summary (alias: card) | values | rdf-labels
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
CORE_SCRIPTS = ROOT.parent / "mim-core" / "scripts"

EXIT_OK = 0
EXIT_USAGE = 2
EXIT_NOT_FOUND = 3

if str(CORE_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(CORE_SCRIPTS))

try:
    import mim_core
except ImportError as exc:  # pragma: no cover - pack layout error
    raise SystemExit(
        "error: mim-core pack not found. This skill depends on sibling "
        f"../mim-core (looked for {CORE_SCRIPTS / 'mim_core.py'})."
    ) from exc


def load_json(path: str | Path) -> Any:
    path = Path(path)
    if not path.is_file():
        raise SystemExit(f"error: file not found: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def emit(data: Any, as_json: bool, text: str) -> None:
    if as_json:
        json.dump(data, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
    else:
        sys.stdout.write(text if text.endswith("\n") else text + "\n")


def cmd_catalog(catalog_path: str, as_json: bool) -> int:
    catalog = load_json(catalog_path)
    if as_json:
        emit(catalog, True, "")
        return EXIT_OK
    lines = [
        f"model catalog {catalog_path} v{catalog.get('version')} "
        f"lastVerified={catalog.get('lastVerified')}",
        "",
    ]
    for p in catalog.get("products", []):
        model = p.get("model") or {}
        mapping = p.get("verifiedMapping") or "none"
        lines.append(
            f"- {p['id']}: {p['name']}\n"
            f"    model={model.get('id')} ({model.get('informatiemodeltype')}, "
            f"fidelity={model.get('fidelity')}) verified-mapping={mapping}"
        )
        reject = p.get("homonymReject") or []
        if reject:
            lines.append(f"    do not bind: {', '.join(reject)}")
        if p.get("elementSummaries"):
            lines.append(f"    element-summaries: {p['elementSummaries']}")
    dead = catalog.get("deadUrls") or []
    if dead:
        lines.append("\ndead URLs:")
        lines.extend(f"  - {u}" for u in dead)
    emit(catalog, False, "\n".join(lines))
    return EXIT_OK


def cmd_map(catalog_path: str, product: str, fields: list[str], as_json: bool) -> int:
    catalog = load_json(catalog_path)
    products = {p["id"]: p for p in catalog.get("products", [])}
    if product not in products:
        known = ", ".join(sorted(products))
        print(f"error: unknown product '{product}'. known: {known}", file=sys.stderr)
        return EXIT_NOT_FOUND
    mapping_name = products[product].get("verifiedMapping")
    if not mapping_name:
        print(
            f"error: product '{product}' has no verified field mapping. "
            "Do not name-match. See references/model-catalog.md.",
            file=sys.stderr,
        )
        return EXIT_NOT_FOUND
    mapping = load_json(Path(catalog_path).resolve().parent / mapping_name)
    by_field = {row["field"]: row for row in mapping.get("fields", [])}
    rows = []
    unknown = []
    for raw in fields:
        field = raw.strip()
        if not field:
            continue
        hit = by_field.get(field) or by_field.get(field.replace(".", "_"))
        if hit is None:
            unknown.append(field)
            rows.append(
                {
                    "field": field,
                    "mappingType": "unmapped",
                    "element": None,
                    "confidence": "none",
                    "reasons": ["not-in-verified-mapping"],
                }
            )
        else:
            rows.append(hit)
    payload = {
        "product": product,
        "model": mapping.get("model"),
        "rows": rows,
        "unknownFields": unknown,
    }
    if as_json:
        emit(payload, True, "")
        return EXIT_OK
    lines = [f"{product} → {mapping.get('model')}  ({len(rows)} fields)", ""]
    lines.append(f"{'field':<28} {'type':<14} {'element':<36} confidence")
    lines.append("-" * 90)
    for row in rows:
        lines.append(
            f"{row['field']:<28} {row.get('mappingType',''):<14} "
            f"{str(row.get('element')):<36} {row.get('confidence')}"
        )
    emit(payload, False, "\n".join(lines))
    return EXIT_OK


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="mim_interpret.py",
        description="Deterministic MIM interpret helper (model catalog, verified field mapping; element summaries via mim-core).",
    )
    p.add_argument("--json", action="store_true", help="JSON output")
    sub = p.add_subparsers(dest="cmd", required=True)

    cat = sub.add_parser("catalog", help="List product → model bindings in a catalog file")
    cat.add_argument("--catalog", required=True, help="Model catalog JSON file")

    m = sub.add_parser("map", help="Look up fields of a product in its verified field mapping")
    m.add_argument("--catalog", required=True, help="Model catalog JSON file")
    m.add_argument("--product", required=True, help="Product id from the catalog")
    m.add_argument("--fields", required=True, help="Comma-separated field names")

    c = sub.add_parser(
        "summary", aliases=["card"], help="Print one element summary (mim-core)"
    )
    mim_core.add_summaries_arg(c)
    c.add_argument("query", help="Objecttype or Objecttype.attribuut")

    v = sub.add_parser("values", help="Print the values of one waardelijst (mim-core)")
    mim_core.add_summaries_arg(v)
    v.add_argument("list_name")

    r = sub.add_parser("rdf-labels", help="List rdfs:label/type from Turtle or RDF/XML (quick scan, mim-core)")
    r.add_argument("target", help="File path or URL")
    r.add_argument("--allow", action="append", default=[], help="Extra allowed host")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    as_json = args.json
    if args.cmd == "catalog":
        return cmd_catalog(args.catalog, as_json)
    if args.cmd == "map":
        fields = [part.strip() for part in args.fields.split(",") if part.strip()]
        if not fields:
            print("error: --fields is empty", file=sys.stderr)
            return EXIT_USAGE
        return cmd_map(args.catalog, args.product, fields, as_json)
    if args.cmd in ("summary", "card"):
        return mim_core.cmd_summary(args.summaries, args.query, as_json)
    if args.cmd == "values":
        return mim_core.cmd_values(args.summaries, args.list_name, as_json)
    if args.cmd == "rdf-labels":
        return mim_core.cmd_rdf_labels(args.target, args.allow, as_json)
    return EXIT_USAGE


if __name__ == "__main__":
    sys.exit(main())
