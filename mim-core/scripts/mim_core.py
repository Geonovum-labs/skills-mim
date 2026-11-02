#!/usr/bin/env python3
"""Deterministic MIM reading helper (shared pack, not a skill).

Stdlib only. Looks things up in a fixed JSON file and prints the result; it
never interprets or guesses. Works for any MIM-conformant model: pass the
element-summaries file of that model with --summaries (format:
../references/element-summary-format.md, template:
../templates/element-summaries.template.json).
Commands: summary (alias: card) | values | rdf-labels

No Q&A workflow and no codegen workflow.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

DEFAULT_ALLOW = (
    "geostandaarden.nl",
    "overheid.nl",
    "pdok.nl",
    "kadaster.nl",
)
GEONOVUM_GITHUB = ("raw.githubusercontent.com", "github.com")

EXIT_OK = 0
EXIT_USAGE = 2
EXIT_NOT_FOUND = 3
EXIT_FORBIDDEN = 4
EXIT_FETCH = 5


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


def _norm(value: str) -> str:
    return re.sub(r"[^a-z0-9]", "", value.casefold())


def _aliases(summaries: dict[str, Any]) -> dict[str, str]:
    index: dict[str, str] = {}
    for key, elem in (summaries.get("elements") or {}).items():
        index[_norm(key)] = key
        naam = elem.get("naam")
        if naam:
            index[_norm(naam)] = key
            owner = elem.get("owner")
            if owner:
                index[_norm(f"{owner}.{naam}")] = key
        for alias in elem.get("alias") or []:
            index[_norm(alias)] = key
            owner = elem.get("owner")
            if owner:
                index[_norm(f"{owner}.{alias}")] = key
    return index


def cmd_summary(summaries_path: str, query: str, as_json: bool) -> int:
    summaries = load_json(summaries_path)
    elements = summaries.get("elements") or {}
    index = _aliases(summaries)
    key = elements.get(query) and query or index.get(_norm(query))
    if not key:
        hits = [k for k in elements if _norm(query) in _norm(k)]
        if len(hits) == 1:
            key = hits[0]
        elif hits:
            print(
                "error: ambiguous. candidates: " + ", ".join(hits[:10]),
                file=sys.stderr,
            )
            return EXIT_NOT_FOUND
        else:
            print(f"error: no element summary for '{query}'. Never invent an element.", file=sys.stderr)
            return EXIT_NOT_FOUND
    elem = elements[key]
    payload = {
        "id": key,
        "model": summaries.get("model"),
        "fidelity": summaries.get("fidelity"),
        "source": summaries.get("source"),
        "element": elem,
    }
    if as_json:
        emit(payload, True, "")
        return EXIT_OK
    lines = [
        f"{elem.get('kind')}: {elem.get('naam') or key}   [{summaries.get('model')}, {summaries.get('fidelity')}]",
        f"code: {elem.get('code', '—')}   owner: {elem.get('owner', '—')}",
    ]
    if "definitie" in elem:
        lines.append(f"definitie: {elem['definitie']}")
    if "populatie" in elem:
        lines.append(f"populatie: {elem['populatie']}")
    bits = []
    if "kardinaliteit" in elem:
        bits.append(f"kardinaliteit={elem['kardinaliteit']}")
    if "mogelijkGeenWaarde" in elem:
        bits.append(f"mogelijkGeenWaarde={'Ja' if elem['mogelijkGeenWaarde'] else 'Nee'}")
    if "authentiek" in elem:
        bits.append(f"authentiek={elem['authentiek']}")
    if "datatype" in elem:
        bits.append(f"type={elem['datatype']}")
    hist = elem.get("historie")
    if hist:
        bits.append(
            f"historie materieel/formeel={'Ja' if hist.get('materieel') else 'Nee'}/"
            f"{'Ja' if hist.get('formeel') else 'Nee'}"
        )
    if bits:
        lines.append("  ".join(bits))
    if elem.get("attributes"):
        lines.append("attributen: " + ", ".join(elem["attributes"]))
    if elem.get("note"):
        lines.append(f"note: {elem['note']}")
    lines.append(f"source: {summaries.get('source')}")
    emit(payload, False, "\n".join(lines))
    return EXIT_OK


def cmd_values(summaries_path: str, list_name: str, as_json: bool) -> int:
    summaries = load_json(summaries_path)
    lists = summaries.get("valuelists") or {}
    key = next((k for k in lists if _norm(k) == _norm(list_name)), None)
    if not key:
        print(
            f"error: no waardelijst '{list_name}'. known: {', '.join(lists)}",
            file=sys.stderr,
        )
        return EXIT_NOT_FOUND
    payload = {"id": key, **lists[key]}
    if as_json:
        emit(payload, True, "")
        return EXIT_OK
    kind = lists[key].get("kind") or "Enumeratie"
    lines = [f"{kind} {key}  (naam = exchanged value)", ""]
    for item in lists[key].get("values") or []:
        definition = item.get("definitie") or ""
        lines.append(f"- {item['naam']}" + (f"  — {definition}" if definition else ""))
    emit(payload, False, "\n".join(lines))
    return EXIT_OK


def _host_ok(url: str, extra_allow: list[str]) -> bool:
    host = (urlparse(url).hostname or "").casefold()
    if not host:
        return False
    allowed = list(DEFAULT_ALLOW) + extra_allow
    if any(host == d or host.endswith("." + d) for d in allowed):
        return True
    if host in GEONOVUM_GITHUB:
        path = urlparse(url).path.casefold()
        return "/geonovum/" in path or path.startswith("geonovum/")
    return False


def _fetch(url: str, extra_allow: list[str]) -> str:
    if not _host_ok(url, extra_allow):
        raise PermissionError(f"host not on allowlist: {url}")
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "geonovum-mim-core/0.1",
            "Accept": "text/turtle, application/rdf+xml, text/plain",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = resp.read(2_000_000)
    except urllib.error.URLError as exc:
        raise RuntimeError(f"fetch failed: {exc}") from exc
    return data.decode("utf-8", errors="replace")


_TTL_TYPE = re.compile(
    r"<([^>]+)>\s+a\s+([^\s;]+)",
    re.IGNORECASE,
)
_TTL_PRED = re.compile(
    r"<([^>]+)>\s+(rdfs:label|rdfs:comment|skos:prefLabel|dct:subject|mim:equivalent|"
    r"<http://www\.w3\.org/2000/01/rdf-schema#label>|"
    r"<http://www\.w3\.org/2000/01/rdf-schema#comment>)\s+\"([^\"]+)\"",
    re.IGNORECASE,
)
_XML_DESC = re.compile(
    r'<(?:rdf:)?Description[^>]*rdf:about="([^"]+)"[^>]*>(.*?)</(?:rdf:)?Description>',
    re.IGNORECASE | re.DOTALL,
)
_XML_LABEL = re.compile(
    r"<(?:rdfs:)?label[^>]*>([^<]+)</(?:rdfs:)?label>",
    re.IGNORECASE,
)
_XML_COMMENT = re.compile(
    r"<(?:rdfs:)?comment[^>]*>([^<]+)</(?:rdfs:)?comment>",
    re.IGNORECASE,
)
_XML_TYPE = re.compile(
    r'<(?:rdf:)?type[^>]*rdf:resource="([^"]+)"',
    re.IGNORECASE,
)


def _skim_rdf(text: str) -> list[dict[str, Any]]:
    found: dict[str, dict[str, Any]] = {}

    def rec(uri: str) -> dict[str, Any]:
        return found.setdefault(uri, {"uri": uri, "types": [], "labels": [], "comments": []})

    if "<rdf:RDF" in text or "<RDF" in text:
        for about, body in _XML_DESC.findall(text):
            node = rec(about)
            node["labels"].extend(x.strip() for x in _XML_LABEL.findall(body) if x.strip())
            node["comments"].extend(x.strip() for x in _XML_COMMENT.findall(body) if x.strip())
            node["types"].extend(_XML_TYPE.findall(body))
    else:
        _skim_turtle(text, rec)

    out = []
    for node in found.values():
        for field in ("types", "labels", "comments"):
            seen: list[str] = []
            for item in node[field]:
                if item not in seen:
                    seen.append(item)
            node[field] = seen
        out.append(node)
    return out


def _skim_turtle(text: str, rec) -> None:
    for uri, rdf_type in _TTL_TYPE.findall(text):
        rec(uri)["types"].append(rdf_type.rstrip(" ;,."))
    for uri, _pred, literal in _TTL_PRED.findall(text):
        pred = _pred.casefold()
        if "comment" in pred:
            rec(uri)["comments"].append(literal)
        else:
            rec(uri)["labels"].append(literal)
    ttl_block = re.compile(
        r"<([^>]+)>\s+a\s+[^\s;]+(?:\s*;\s*[^.]*)?\.",
        re.DOTALL,
    )
    for block in ttl_block.finditer(text):
        uri = block.group(1)
        body = block.group(0)
        node = rec(uri)
        node["labels"].extend(re.findall(r'(?:rdfs:label|skos:prefLabel)\s+"([^"]+)"', body))
        node["comments"].extend(re.findall(r'rdfs:comment\s+"([^"]+)"', body))
    prefixed = re.compile(
        r"\b([A-Za-z][\w\-]*:[A-Za-z][\w\-]*)\s+a\s+([^\s;]+).*?"
        r'(?:rdfs:label|skos:prefLabel)\s+"([^"]+)"',
        re.DOTALL,
    )
    for uri, rdf_type, label in prefixed.findall(text):
        node = rec(uri)
        node["types"].append(rdf_type.rstrip(" ;,."))
        node["labels"].append(label)


def cmd_rdf_labels(target: str, extra_allow: list[str], as_json: bool) -> int:
    path = Path(target)
    try:
        if path.is_file():
            text = path.read_text(encoding="utf-8", errors="replace")
            source = str(path)
        elif target.startswith("http://") or target.startswith("https://"):
            text = _fetch(target, extra_allow)
            source = target
        else:
            print(f"error: not a file or URL: {target}", file=sys.stderr)
            return EXIT_USAGE
    except PermissionError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return EXIT_FORBIDDEN
    except RuntimeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return EXIT_FETCH
    if "Attribuuttype" in text and "Relatietype" in text:
        print(
            "error: file looks like MIM 2.0 vocabulary (Attribuuttype/Relatietype). Unsupported in v1.",
            file=sys.stderr,
        )
        return EXIT_NOT_FOUND
    nodes = _skim_rdf(text)[:40]
    payload = {
        "source": source,
        "fidelity": "rdf-label-scan-stdlib",
        "note": "Quick label scan, not a full RDF parser and not a complete model. Bind the model first.",
        "count": len(nodes),
        "nodes": nodes,
    }
    if as_json:
        emit(payload, True, "")
        return EXIT_OK
    lines = [f"rdf-labels {source}  ({len(nodes)} nodes, quick label scan)", ""]
    for node in nodes[:20]:
        label = (node["labels"] or ["—"])[0]
        types = ",".join(node["types"][:3]) or "—"
        lines.append(f"- {node['uri']}: {label}  [{types}]")
    if len(nodes) > 20:
        lines.append(f"… {len(nodes) - 20} more (use --json)")
    emit(payload, False, "\n".join(lines))
    return EXIT_OK


def add_summaries_arg(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--summaries",
        required=True,
        help="Element-summaries JSON file of the bound model",
    )


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="mim_core.py",
        description="Deterministic MIM reading helper (element summaries, enumeraties, RDF label scan).",
    )
    p.add_argument("--json", action="store_true", help="JSON output")
    sub = p.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser(
        "summary", aliases=["card"], help="Print one element summary from a summaries file"
    )
    add_summaries_arg(c)
    c.add_argument("query", help="Objecttype or Objecttype.attribuut")

    v = sub.add_parser("values", help="Print the values of one waardelijst from a summaries file")
    add_summaries_arg(v)
    v.add_argument("list_name")

    r = sub.add_parser("rdf-labels", help="List rdfs:label/type from Turtle or RDF/XML (quick scan, not a full parser)")
    r.add_argument("target", help="File path or URL")
    r.add_argument("--allow", action="append", default=[], help="Extra allowed host")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    as_json = args.json
    if args.cmd in ("summary", "card"):
        return cmd_summary(args.summaries, args.query, as_json)
    if args.cmd == "values":
        return cmd_values(args.summaries, args.list_name, as_json)
    if args.cmd == "rdf-labels":
        return cmd_rdf_labels(args.target, args.allow, as_json)
    return EXIT_USAGE


if __name__ == "__main__":
    sys.exit(main())
