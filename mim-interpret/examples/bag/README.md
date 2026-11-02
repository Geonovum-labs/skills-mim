# Example: BAG

This folder runs the generic skill on one real dataset: the **PDOK BAG OGC API v2**, collection `pand`, interpreted with **IMBAG Catalogus 2018** (the information model of the Basisregistratie Adressen en Gebouwen). It is an example, not part of the rules: the generic files in this skill do not depend on it. The element summaries for IMBAG and the reading rules applied to IMBAG are in [`../../../mim-core/examples/bag/`](../../../mim-core/examples/bag/README.md).

## Files

| File | What | Format |
|---|---|---|
| [`model-catalog.json`](model-catalog.json) | Model catalog: PDOK BAG collections → IMBAG 2018, plus models with same-named elements not to bind for BAG data (IMGeo, NEN 3610, IMX-Geo, IMKAD) | [`../../references/model-catalog.md`](../../references/model-catalog.md) |
| [`pdok-bag-pand-mapping.json`](pdok-bag-pand-mapping.json) | Verified field mapping PDOK `pand` → IMBAG | [`../../references/field-mapping-format.md`](../../references/field-mapping-format.md) |
| [`pdok-bag-pand-mapping.md`](pdok-bag-pand-mapping.md) | Readable version of the mapping, with enumeraties and the snapshot note | — |
| [`worked-example.md`](worked-example.md) | Worked Q&A on one `pand` record, including a refusal case | — |
| [`evals.json`](evals.json) | Ten eval cases E-BAG-01 … E-BAG-10 | [`../../evals/README.md`](../../evals/README.md) |

## Run it (from `mim-interpret/`)

```text
python3 scripts/mim_interpret.py catalog --catalog examples/bag/model-catalog.json
python3 scripts/mim_interpret.py map --catalog examples/bag/model-catalog.json --product pdok-bag-pand --fields identificatie,bouwjaar,status,geconstateerd,gebruiksdoel,aantal_verblijfsobjecten,geometry
python3 scripts/mim_interpret.py summary --summaries ../mim-core/examples/bag/imbag-element-summaries.json Pand.geconstateerd
python3 scripts/mim_interpret.py values --summaries ../mim-core/examples/bag/imbag-element-summaries.json StatusPand
```

## Bindings in this example

| Product / collection | Model | Type | Fidelity | Do not bind (homonyms; may be related) |
|---|---|---|---|---|
| PDOK BAG OGC API v2 `pand` (verified field mapping), `verblijfsobject` (no mapping yet) | IMBAG Catalogus 2018 | Conceptueel | catalog-prose | IMGeo Pand; NEN 3610 Gebouw; IMX-Geo Gebouw/Bouwwerk/Adres; dead `rdf_seealso` |
| PDOK / BGT IMGeo collections | IMGeo 2.2 | Conceptueel + Logisch | ea-xmi + skos | IMBAG Pand |
| Linked Data built on NEN 3610 | NEN 3610-2022 ontology | Logisch / LD | rdf | BAG objecttypen |
| IMX-Geo cross-registry overlay | IMX-Geo | overlay RDF | rdf | Not IMBAG; `Adres` is a composition |

What the example shows: `geconstateerd = "N"` is a J/N enumeratiewaarde, not Boolean; `gebruiksdoel` on `pand` is denormalized from Verblijfsobject; `aantal_verblijfsobjecten` is derived; the PDOK collection is a snapshot even though IMBAG tags historie = Ja; IMGeo `Pand` must not be used to read BAG fields, but may be named as describing the same building (linked via `identificatieBAGPND`).

## Known gaps

- Verified field mapping only for `pand`. `verblijfsobject`, `ligplaats`, `standplaats`, `woonplaats`, `adres` are bound to IMBAG but not mapped (`adres` is a product composition, not an IMBAG objecttype).
- No IMGeo mapping; IMGeo is listed to block binding it to BAG data and to record the link.
- No IMBAG MIM-RDF to read (not published on 2026-10-30).
- The mapping is not yet reviewed by a modeller (`reviewedBy: null`).
- IMBAG *in onderzoek* (ch. 9.2 object Onderzoek) is only noted as a flag.
- BRK / IMKAD is listed as unparseable; object-only BRK questions may mention IMKAD as unbound.

## Licence

IMBAG Catalogus 2018 is CC-BY-ND 3.0 NL. Element summaries and this mapping paraphrase definitions and cite the catalog; enumeratiewaarde *namen* are reproduced because they are the exchanged data values. Do not link BAG addresses to persons.
