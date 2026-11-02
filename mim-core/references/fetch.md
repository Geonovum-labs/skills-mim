# Fetch a MIM-conformant model

Find-the-model is a **curated list**, not a crawler. Models with the same element names (homonyms) are the main risk. Last verified: 2026-10-30.

This pack tells you **where models live** and in which serialization. Binding a *data product* (API, file, collection) to a model is extra-standard work of `mim-interpret` (its model catalog). Generating software from a bound model is extra-standard work of `mim-implement` (not built yet).

## Discovery order (stop at the first hit that is the model of this subject)

1. User-supplied model file **if** it matches the identified model (check model id; do not bind a model just because it has same-named elements).
2. RDF at `modellen.geostandaarden.nl` **if** the ontology is the model of this subject.
3. HTML/PDF catalog of the model owner.
4. SKOS waardelijsten / begrippen as supplements, never as the whole model.
5. Level-4 schema (queryables, JSON Schema, XSD) labelled `derived-technical`.
6. EA XMI / MIM XML when present; no parser in v1.
7. Nothing: no-model fallback (say so, label any answer *inferred*, invent no element names).

Do **not** search GitHub for an objecttype name.

## Where Geonovum models live

| Source | What | Use |
|---|---|---|
| [modellen.geostandaarden.nl](http://modellen.geostandaarden.nl) | RDF publications of information models (index page lists them) | Preferred source **when** the RDF is the model of this subject |
| `register.geostandaarden.nl/informatiemodel/<model>/<version>/` | Register of model files (EA, XMI, PDF, SKOS) | When no RDF is published |
| Owner catalogus (HTML/PDF) | MIM catalog tables published by the model owner | First-class when RDF is missing; fidelity `catalog-prose` |

Which model belongs to which product is recorded per product in a model catalog (`mim-interpret`), not here. A filled-in list of models, dead links and homonyms for one domain: [`../examples/bag/README.md`](../examples/bag/README.md) (Example: BAG).

## Element summaries

Once a model is bound, its element summaries (short fixed-format summary per element) live in one JSON file. Format: [`element-summary-format.md`](element-summary-format.md). Look up with `python3 scripts/mim_core.py summary --summaries <file> <element>`, or read the JSON directly.

## Unreliable URLs (2026-10-30)

- `http://modellen.mim-standaard.nl/def/mim` and `/def/mim-shapes`: 404/500
- `Geonovum/mim-ld/example/mim.ttl`: 0 bytes

If an RDF URI 404s, fall back to the catalogus and element summaries. Do not claim the link worked.

## Quick RDF label scan

```text
python3 scripts/mim_core.py rdf-labels <turtle-or-rdfxml-file-or-url> [--allow <extra-host>]
```

Use `rdf-labels` only after the model id is bound. It lists labels and types; it is not a full RDF parser. Default allowed hosts: `*.geostandaarden.nl`, `*.overheid.nl`, `*.pdok.nl`, `*.kadaster.nl`, GitHub paths under `Geonovum/`. Add others with `--allow`.
