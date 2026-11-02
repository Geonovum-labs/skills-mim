# Model catalog (product → model)

A *model catalog* says which MIM-conformant model describes which data product (API host, collection, file, version), and which models with same-named elements must not be bound for it. Models with the same element names (homonyms) are the main risk. One catalog is a JSON file; the skill does not ship a fixed one.

Template: [`../templates/model-catalog.template.json`](../templates/model-catalog.template.json). Filled-in example: [`../examples/bag/model-catalog.json`](../examples/bag/model-catalog.json) (Example: BAG).

How to **fetch** a bound model (RDF / catalogus / SKOS / XMI): [`../../mim-core/references/fetch.md`](../../mim-core/references/fetch.md). Do not copy that discovery order here.

## Entry fields

| Key | Meaning |
|---|---|
| `id`, `name` | Product id used on the command line, and a readable name. |
| `match` | How to recognise the product: `hosts`, `pathContains`, `collections`. |
| `model` | `id`, `name`, `informatiemodeltype` (`Conceptueel` / `Logisch`), `mimVersion`, `fidelity`. |
| `sources` | Where the model and the product are published. |
| `homonymReject` | Model ids that share element names with this model and must **not** be bound as the model of this product. They may still describe the same real-world objects (rule H). |
| `verifiedMapping` | File name of the verified field mapping for this product (format: [`field-mapping-format.md`](field-mapping-format.md)), or `null` if none exists. |
| `elementSummaries` | File name of the element summaries of the model (format: [`../../mim-core/references/element-summary-format.md`](../../mim-core/references/element-summary-format.md)), or omitted. |
| `note` | Gaps or warnings. |

File paths are relative to the catalog file. A catalog may also list `deadUrls`.

## Product discovery (stop at the first entry that matches)

1. User-supplied model file **if** it matches the product (check model id; do not bind a model just because it has same-named elements).
2. The model catalog, matched on `(host, path, collection)`.
3. Then mim-core fetch (RDF → HTML catalog → SKOS → derived-technical → no-model fallback).

If an entry has `verifiedMapping: null`, bind the model but do not map fields by name: say which fields you could not map.

Do **not** search GitHub for an objecttype name.

```text
python3 scripts/mim_interpret.py catalog --catalog <catalog.json>
```
