# mim-core (shared pack)

Shared MIM **reading** pack for the plugins in this repository. It is **not** a skill and not a third product. It works for any MIM-conformant information model.

Plugins that depend on it:

| Plugin | Role |
| --- | --- |
| [`../mim-interpret/`](../mim-interpret/) | Interpret models so agents can answer questions about the data those models describe. |
| [`../mim-implement/`](../mim-implement/) | Implement a MIM model correctly in software. **Not built yet.** |

## What this pack is

How to **read** a MIM-conformant information model:

- objecttypen, attribuutsoorten, relaties, kardinaliteit, datatypes, waardelijsten, constraints, generalisatie, populatie;
- homonyms (same name in different models is not the same element, though they may be related and describe the same real-world object); J/N enumeratie vs Boolean; Basisgegeven ≠ Authentiek;
- where the MIM 1.2 text is ambiguous or contradicts itself, so an agent reports it instead of resolving it silently ([`known-ambiguities.md`](references/known-ambiguities.md));
- how to recognise MIM elements in UML and in Linked Data;
- where to fetch models (in the experiment first the [Geonovum catalog](https://catalog.modeldesk.io/geonovum); then RDF at [modellen.geostandaarden.nl](http://modellen.geostandaarden.nl); HTML/PDF catalogus when RDF is missing);
- **element summaries**: short, fixed-format summaries of one model element (definitie, type, kardinaliteit, mogelijk geen waarde, authentiek, historie, waardelijst), so an agent does not have to read the whole model;
- an optional helper script that looks those up exactly.

## What this pack is not

- No Q&A / data-interpretation workflow (that is `mim-interpret`).
- No codegen / schema / API implementation workflow (that is `mim-implement`, later).
- No authoring or validation of models (Imvertor / MIM toolbox / `geo-model`).

Do not load this folder as if it were a `SKILL.md`. There is none.

## Layout

```text
mim-core/
├── README.md                                   # this file
├── references/
│   ├── mim-core.md                             # compact metamodel, MIM uitgangspunten, UML/LD forms, 1.2 vs 2.0, serializations
│   ├── reading-rules.md                        # how metagegevens change what a model means
│   ├── known-ambiguities.md                    # where the MIM 1.2 text contradicts itself (I1–I5)
│   ├── fetch.md                                # where models live, discovery order
│   └── element-summary-format.md               # format of an element-summaries file
├── templates/element-summaries.template.json   # empty format to copy for a new model
├── scripts/mim_core.py                         # summary | values | rdf-labels
└── examples/bag/                               # Example: BAG (IMBAG 2018 summaries, rule illustrations)
```

Generic files never depend on `examples/`.

## Script (optional)

The script does exact, repeatable lookups in the element-summaries file you pass; it never interprets. That helps small models (Mistral, Copilot, small LLMs) that misread long tables. An agent without Python reads the same JSON: element summaries under `elements` (key `Objecttype` or `Objecttype.attribuut`), waardelijsten under `valuelists`. Stdlib only.

```text
python3 scripts/mim_core.py summary --summaries <file> <Objecttype[.attribuut]>
python3 scripts/mim_core.py values  --summaries <file> <Waardelijst>
python3 scripts/mim_core.py rdf-labels <turtle-or-rdfxml-file-or-url> [--allow <host>]
```

`--json` (before the command) is available on every command; `card` still works as an old name for `summary`. Default allowed fetch hosts: `*.geostandaarden.nl`, `*.overheid.nl`, `*.pdok.nl`, `*.kadaster.nl`, `catalog.modeldesk.io`, GitHub paths under `Geonovum/`; add others with `--allow`.

Example: BAG — `python3 scripts/mim_core.py summary --summaries examples/bag/imbag-element-summaries.json Pand.status`

Never invent a modelelement that the element summary, catalog or loaded model source did not return.
