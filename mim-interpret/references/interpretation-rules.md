# Interpretation rules (data Q&A)

This plugin maps **product fields → modelelementen** and then applies MIM reading rules to the values. Core how-to-read lives in [`../../mim-core/references/reading-rules.md`](../../mim-core/references/reading-rules.md). Do not duplicate those rule bodies here.

Normative source: [MIM 1.2](https://docs.geostandaarden.nl/mim/def-st-mim-20240613/) (CC-BY 4.0). Mapping is extra-standard: MIM does not cover data (M0) or beschouwingsniveau 4.

Always-on for SKILL.md: core reading rules 2–14, P, H, I, L (especially repaired 2, 10, 12) **plus** the data rules D1–D3 below. Terms such as *verified field mapping*, *element summary* and *mapping type* are defined in the glossary of [`../SKILL.md`](../SKILL.md#words-used-in-this-skill). The same rules applied to one dataset: [`../examples/bag/worked-example.md`](../examples/bag/worked-example.md) (Example: BAG).

## D1. Model ≠ data

An *objecttype* describes a kind of real-world thing. Tables, API collections and files may split, merge or denormalize it (MIM §2.3.2.1, §1.5.2). A collection with the same name as an objecttype is not that objecttype. Always name the mapping type.

## D2. Product ≠ model

An API, extract or “actueel” snapshot is a level-4 projection of the model. Fields missing from a filter list (queryables), extra fields copied from related objects, and the choice between snapshot and full history are product choices. They do not tell you what is in the model.

## D3. Derived on the product

Core rule 11 (`indicatieAfleidbaar`) still applies. Products often do **not** set that flag on fields they compute themselves (counts, totals, labels). Then the **mapping type** `derived` / `denormalized` / `unmapped` is the signal: such a field is not independent evidence about the model element.

## Apply core reading, then answer

After the verified field mapping names an element, read its element summary and apply the mim-core reading rules:

| Need | Core rule |
|---|---|
| Blank / NULL | 2 (kardinaliteit × mogelijk geen waarde) |
| Repeating values / groups | 3 |
| Directed relations; inverse counts | 4 |
| Abstract types; inherited members | 5 |
| Closed vs external lists; exact *naam* | 6 |
| Leading zeros; model type vs JSON type | 7 |
| Composite vs group | 8 |
| XOR / Keuze | 9 |
| Historie flags vs what this product serves | 10 — flags are conceptual. Check whether the product has version fields (`beginGeldigheid`, `voorkomen`, …) before claiming history is present. |
| Authentiek vs Basisgegeven | 12 |
| Conceptual model vs missing XMI/RDF | 14 |
| Who is in the registration | P |
| Same name, different model (may be related) | H |
| J/N enumeratie is not Boolean | I |
| `status` is life-cycle, not a time-axis | L |

## Mapping types

| Type | Meaning |
|---|---|
| `direct` | Same name, same element |
| `renamed` | Product name ≠ model name (product `geometry` → model `geometrie`) |
| `denormalized` | Value belongs to another (related) objecttype and was copied onto this record |
| `derived` | Computed by the product; not independent evidence |
| `technical` | Transport, paging, links, dead URI |
| `unmapped` | Not a modelelement; say so |
| `homonym-rejected` | Element of a different model with the same name; not this field's element. Do not use its definitie or kardinaliteit; mention a relation or explicit link if there is one (rule H) |
