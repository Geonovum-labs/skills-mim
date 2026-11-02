# Example: BAG — worked Q&A (PDOK BAG pand → IMBAG)

Question (NL): *Wat betekent `geconstateerd = "N"` op dit pand, is `gebruiksdoel` een Pand-gegeven, en zijn dit historische versies?*

This example runs the generic workflow of [`../../SKILL.md`](../../SKILL.md#workflow) on one dataset. Do **not** open IMGeo XMI. Run commands from `mim-interpret/`. Without Python, read the same keys in [`model-catalog.json`](model-catalog.json), [`pdok-bag-pand-mapping.json`](pdok-bag-pand-mapping.json) and [`../../../mim-core/examples/bag/imbag-element-summaries.json`](../../../mim-core/examples/bag/imbag-element-summaries.json).

## Input (dataset-observed)

PDOK BAG OGC API v2 `pand` item, last verified 2026-10-30, `identificatie=0003100000117485`:

```json
{
  "identificatie": "0003100000117485",
  "bouwjaar": 1991,
  "status": "Pand in gebruik",
  "geconstateerd": "N",
  "gebruiksdoel": "woonfunctie",
  "aantal_verblijfsobjecten": 15,
  "documentdatum": "2010-07-20",
  "documentnummer": "FB 2010/PANDEN001",
  "rdf_seealso": "http://bag.basisregistraties.overheid.nl/bag/id/pand/0003100000117485"
}
```

Queryables on the same collection do **not** list `geconstateerd`. Geometry omitted.

## Bind

```text
python3 scripts/mim_interpret.py catalog --catalog examples/bag/model-catalog.json
```

Product `api.pdok.nl/kadaster/bag` + collection `pand` → **IMBAG Catalogus 2018** (conceptueel, fidelity `catalog-prose`).  
Reject: IMGeo `Pand`, NEN 3610 `Gebouw`, IMX-Geo `Gebouw`/`Bouwwerk`.  
`rdf_seealso` is a dead URI; do not follow it as an ontology.

## Map (verified field mapping)

```text
python3 scripts/mim_interpret.py map --catalog examples/bag/model-catalog.json --product pdok-bag-pand \
  --fields identificatie,bouwjaar,status,geconstateerd,gebruiksdoel,aantal_verblijfsobjecten,geometry,rdf_seealso
```

| field | type | element |
|---|---|---|
| identificatie | direct | Pand.identificatie |
| bouwjaar | renamed | Pand.oorspronkelijk bouwjaar (Year) |
| status | direct | Pand.status / StatusPand |
| geconstateerd | direct | Pand.geconstateerd / Indicatie |
| geometry | renamed | Pand.geometrie |
| gebruiksdoel | **denormalized** | **Verblijfsobject**.gebruiksdoel `1..*` |
| aantal_verblijfsobjecten | **derived / unmapped** | — |
| rdf_seealso | technical | — |

## Element summaries

```text
python3 scripts/mim_interpret.py summary --summaries ../mim-core/examples/bag/imbag-element-summaries.json Pand.geconstateerd
python3 scripts/mim_interpret.py values --summaries ../mim-core/examples/bag/imbag-element-summaries.json Indicatie
python3 scripts/mim_interpret.py values --summaries ../mim-core/examples/bag/imbag-element-summaries.json StatusPand
python3 scripts/mim_interpret.py summary --summaries ../mim-core/examples/bag/imbag-element-summaries.json Verblijfsobject.gebruiksdoel
python3 scripts/mim_interpret.py summary --summaries ../mim-core/examples/bag/imbag-element-summaries.json Verblijfsobject.maaktDeelUitVan
```

## Answer

`geconstateerd = "N"` means **Nee** on the closed enumeratie *Indicatie* `{J, N}` (*model-stated*). The pand was **not** entered via feitelijke constatering without a regular brondocument. It is **not** Boolean false and it is **not** “this building was not observed in the field”. Authentiek = **Basisgegeven**, so there is no gebruiksplicht (*model-stated*). The field is missing from queryables but present on the item: product ≠ model (*dataset-observed*).

`gebruiksdoel = "woonfunctie"` is **not** a Pand attribuutsoort. It is Verblijfsobject.gebruiksdoel, kardinaliteit `1..*`, enumeratie Gebruiksdoel (Bouwbesluit), Authentiek. The API denormalizes it onto `pand`. It is not planologische bestemming and not feitelijk gebruik. With 15 related VBO, a single leaked value is at best a sample, not “the pand has woonfunctie” as an independent Pand fact.

`aantal_verblijfsobjecten = 15` is a product-derived count, not an IMBAG Pand attribuutsoort. The model relation is the other way: a VBO `maakt deel uit van` one or more panden (`1..*`). A VBO **can** lie in several panden (*model-stated*). The href array shape is not that kardinaliteit.

`status = "Pand in gebruik"` is the exact enumeratiewaarde: previously `Pand in gebruik (niet ingemeten)` and the definitive geometrie has been surveyed. It is a **life-cycle** value, not a time-axis, and not a synonym of “occupied as a dwelling”.

`bouwjaar = 1991` maps to *oorspronkelijk bouwjaar* (Year, Authentiek, kardinaliteit 1, mogelijk geen waarde Nee). Later verbouw does not change it. API JSON type integer does not override the model type. IMBAG tags materiële historie Ja for this attribute — use the instance model, not the spec’s pedagogical “bouwjaar → Nee” example. This snapshot still does **not** include `beginGeldigheid` / `voorkomen`; do not claim historical versions are present.

`identificatie` is a 16-character string with leading zeros (gemeentecode `0003` + objecttypecode `10` + volgnummer). Do not cast to integer.

**Basis.** Model IMBAG Catalogus 2018 (Conceptueel, MIM 1.0 terms) › Pand / Verblijfsobject; source https://imbag.github.io/catalogus/ ; product PDOK BAG OGC API v2 collection `pand`. Fidelity `catalog-prose`. No IMBAG RDF published at `modellen.geostandaarden.nl` on 2026-10-30.

## Counterexample (other model on hand)

Given the same payload plus IMGeo logical XMI: do **not** read `geconstateerd`, `status` or `bouwjaar` with IMGeo `Pand` (`homonym-rejected`); those are IMBAG attribuutsoorten. Do say that IMGeo `Pand` describes the same kind of real-world building, and that IMGeo's `identificatieBAGPND` is the explicit link to this IMBAG pand (*model-stated* in IMGeo). `nummeraanduidingreeks` is IMGeo-only and says nothing about this BAG record.
