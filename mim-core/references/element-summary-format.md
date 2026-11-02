# Element summary format

An *element summary* (elementsamenvatting) is a short, fixed-format summary of one model element, so an agent does not have to read the whole model. All summaries of one model sit in one JSON file. Template: [`../templates/element-summaries.template.json`](../templates/element-summaries.template.json). Filled-in example: [`../examples/bag/imbag-element-summaries.json`](../examples/bag/imbag-element-summaries.json) (Example: BAG).

## File

| Key | Meaning |
|---|---|
| `about` | One sentence on what the file contains. |
| `model` | Model id, as used in the model catalog. |
| `fidelity` | Kind of source: `rdf`, `catalog-prose`, `skos`, `derived-technical`, `ea-xmi`. |
| `source`, `sourceLicense` | Where the model is published and under which licence. Paraphrase when the licence forbids copying. |
| `lastVerified` | Date the summaries were checked against the source. |
| `elements` | Element summaries, keyed `Objecttype` or `Objecttype.attribuut` (relaties: `Objecttype.relatienaam`). |
| `valuelists` | Waardelijsten, keyed by name: `kind` (`Enumeratie`, `Referentielijst`, `Codelijst`) and `values` (`naam`, optional `definitie`). |

## One element

Fill what the model states; leave a key out rather than guess.

| Key | Meaning |
|---|---|
| `kind` | `Objecttype`, `Attribuutsoort`, `Relatiesoort`, `Gegevensgroep`, … |
| `naam`, `alias`, `code`, `owner` | Name, alternative names, catalog code, owning objecttype. |
| `definitie`, `populatie` | Paraphrased definition; which instances are in the registration. |
| `datatype`, `waardelijstKind` | Datatype or waardelijst name, and the kind of list. |
| `kardinaliteit`, `mogelijkGeenWaarde` | As in the model (rule 2 in [`reading-rules.md`](reading-rules.md)). |
| `identificerend`, `authentiek` | Identifying flag; authentiek value (`Authentiek`, `Basisgegeven`, …). |
| `historie` | `{"materieel": bool, "formeel": bool}` — conceptual flags (rule 10). |
| `abstract`, `supertypes`, `attributes` | For objecttypen. |
| `rol`, `doel` | For relatiesoorten. |
| `note` | Short warning against a likely misreading. |

## Lookup

```text
python3 scripts/mim_core.py summary --summaries <file> <Objecttype[.attribuut]>
python3 scripts/mim_core.py values  --summaries <file> <Waardelijst>
```

Without Python, open the file and read `elements.<key>` or `valuelists.<name>`. A missing key means the element is not summarised: say so, do not invent it.
