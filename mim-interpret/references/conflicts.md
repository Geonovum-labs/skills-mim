# Conflicts, extra-standard work, prior art

Where **geonovum-mim-interpret** is stricter, narrower, or extra-standard relative to MIM 1.2 or to sibling artefacts. The standard and the published information model win.

Shared reading (kardinaliteit, mogelijk geen waarde, authentiek, homonyms, …) is documented in `mim-core`. This file is about the *interpret* plugin.

## Extra-standard by MIM's own scope

MIM does not cover data (M0) or beschouwingsniveau 4. Field-to-element mapping, product projections (snapshot vs full extract), and verified field mappings are **this skill's work**, not MIM. Label mapping claims as mapping, not as model-stated.

## Deliberate choices (uitgangspunten, not besluiten)

- **Consume-only.** Do not author or validate models. Do not implement models in software (that is `mim-implement`, not built). Imvertor and the MIM toolbox cover conformance; `geo-model` covers authoring-ish guidance.
- **Any MIM model, no built-in model.** Rules and scripts are generic. Model-specific knowledge (catalog entries, verified field mappings, element summaries, eval cases) lives in data files that are passed in. BAG is shipped only as a worked example.
- **RDF preferred, not exclusive.** Uitgangspunt: needed models are published as RDF like `modellen.geostandaarden.nl`. v1 still treats HTML/PDF catalogs and SKOS as first-class, because not every model is published as RDF.
- **Deterministic lookups over SHACL.** The verified field mapping, element summaries and helper scripts give small models exact, repeatable lookups. SHACL may come later; it is not the v1 product. The scripts are optional: the same JSON files can be read directly.
- **English SKILL.md, Dutch MIM terms.** Sibling NL-SBB skills are Dutch-only; this follows the design recommendation. Answers follow the user's language.
- **The model of this product over a look-alike.** Mixing same-named elements from different models is a named failure mode. Relating them is allowed: say when they likely describe the same real-world object, and use links the models state.
- **Two skills, one core.** Do not fold an implement-in-software workflow into this SKILL.md.

## Repairs vs an earlier 16-rule draft

Repaired rule *bodies* live in mim-core `reading-rules.md`. This plugin still depends on them for data answers:

| Draft claim | v1 |
|---|---|
| `0..1` means known not to exist | Only if mogelijk geen waarde = Nee |
| Historie flags mean the dataset keeps history | Conceptual flags mean the property can change; product docs say whether voorkomens are served |
| Authentiek is boolean | Value range; Basisgegeven ≠ Authentiek |
| Prefer logical XMI | Prefer the model of *this* product, conceptual or logical, in whatever form it is published |
| Rule 15 (order) in SKILL.md | Dropped (paper-only) |

## Relation to `geo-model` (skills-geo)

Authoring-oriented, known inaccuracies on beschouwingsniveaus and stereotypes. Complementary, not replaced. Description of this skill says “Not for authoring”. Coordinate after v1 has a working example loop.

## Licence friction

- Skill text and scripts: EUPL-1.2.
- MIM quotations: CC-BY 4.0, attributed, paraphrased where possible.
- Model catalogs may forbid derivative works (e.g. CC-BY-ND). Element summaries then paraphrase definitions and cite the source; enumeratiewaarde *namen* are reproduced because they are the exchanged data values.
- Do not copy Imvertor code or XSDs (GPL-3.0) into this skill.

## What v1 will still get wrong

- Only one worked example (BAG) ships with a verified field mapping and element summaries. Other models need their own data files first.
- No XMI / MIM XML parser.
- `rdf-labels` is a quick stdlib label scan of Turtle/RDF-XML, not a full RDF stack and not SHACL; it does not build element summaries for you.
- *Indicatie in onderzoek* is noted as a flag only; registries implement it differently.
- Example-specific gaps: [`../examples/bag/README.md`](../examples/bag/README.md#known-gaps).
