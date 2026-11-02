# Example: BAG (mim-core)

This folder shows the generic `mim-core` files applied to one real model: **IMBAG Catalogus 2018**, the model behind the BAG (Basisregistratie Adressen en Gebouwen). It is an example, not part of the rules. The interpret side of the same example (verified field mapping for PDOK BAG `pand`, model catalog, worked Q&A, eval cases) is in [`../../../mim-interpret/examples/bag/`](../../../mim-interpret/examples/bag/README.md).

| File | What |
|---|---|
| [`imbag-element-summaries.json`](imbag-element-summaries.json) | Element summaries for IMBAG 2018 (Pand, Verblijfsobject, Adresseerbaar object, their attribuutsoorten, waardelijsten Indicatie / StatusPand / Gebruiksdoel). Format: [`../../references/element-summary-format.md`](../../references/element-summary-format.md). |

```text
python3 scripts/mim_core.py summary --summaries examples/bag/imbag-element-summaries.json Pand.geconstateerd
python3 scripts/mim_core.py values  --summaries examples/bag/imbag-element-summaries.json StatusPand
```

(run from `mim-core/`)

## Sources (last verified 2026-10-30)

| Model | Type | Fidelity | Source | Do not confuse with |
|---|---|---|---|---|
| IMBAG Catalogus 2018 | Conceptueel | catalog-prose | https://imbag.github.io/catalogus/ ; PDF Catalogus-BAG-2018 | IMGeo Pand; NEN 3610 Gebouw; IMX-Geo Gebouw/Bouwwerk/Adres |
| IMGeo 2.2 | Conceptueel + Logisch | ea-xmi + skos | `register.geostandaarden.nl/informatiemodel/imgeo/2.2/` | IMBAG Pand |
| NEN 3610-2022 ontology | Logisch / LD | rdf | https://modellen.geostandaarden.nl/def/nen3610 | BAG objecttypen |
| IMX-Geo | overlay RDF | rdf | https://modellen.geostandaarden.nl/def/imx-geo/ | Not IMBAG; `Adres` is a composition |
| IMKAD 2.3.1 (BRK) | — | unparseable | register: `IMKAD-23.1.EAP` only | Do not claim a parseable model in v1 |

No IMBAG MIM-RDF was published on 2026-10-30, so the HTML catalogus is the first-class source. IMBAG is MIM 1.0 terms. The IMBAG catalogus is CC-BY-ND 3.0 NL: the summaries paraphrase definitions; enumeratiewaarde *namen* are exact because they are the exchanged values. `imbag.github.io` is not a default fetch host; pass `--allow imbag.github.io`.

Dead links for this domain: `https://bag.basisregistraties.overheid.nl/def/bag` and the `rdf_seealso` URIs on PDOK features (404 `application/problem+json`); `https://brk.basisregistraties.overheid.nl/def/brk` (404). Kadaster Skosmos (`catalogus.kadaster.nl`, vocab `bag`) has the begrippen (level 1), not the information model.

## Reading rules applied to IMBAG

Rule numbers refer to [`../../references/reading-rules.md`](../../references/reading-rules.md).

| Rule | In IMBAG 2018 |
|---|---|
| 2 | Pand.identificatie: kardinaliteit `1`, mogelijk geen waarde Nee — blank is invalid. |
| 4 | Relatiesoort `maakt deel uit van` / rol `gerelateerd pand`: Verblijfsobject → Pand, kardinaliteit `1..*` (a VBO may lie in several panden). How many VBO per pand is *kardinaliteitBron*, not a Pand attribuutsoort. |
| 5 | `Adresseerbaar object` is abstract; subtypes Ligplaats, Standplaats, Verblijfsobject. |
| 6 | `StatusPand`, `Indicatie`, `Gebruiksdoel` are closed enumeraties. Use literals exactly (`Pand in gebruik`, `N`, `woonfunctie`). |
| 7 | `identificatie` is a 16-character string with leading zeros. IMBAG types *oorspronkelijk bouwjaar* as Year; PDOK serves it as a JSON integer. |
| 8 | `objectnummering` (identificatie parts) is a composite. Brondocument (`documentdatum` + `documentnummer`) behaves as a shared groep. |
| 9 | VBO geometrie domain `puntOfVlak` is a Keuze: point XOR surface. |
| 10 | MIM's teaching example says bouwjaar has no tijdlijn geldigheid; IMBAG tags *oorspronkelijk bouwjaar* with materiële historie = Ja. Follow IMBAG. IMBAG ch. 9 names the extract history fields. |
| 12 | Pand.`status` and *oorspronkelijk bouwjaar* are Authentiek; Pand.`geconstateerd` is **Basisgegeven**. |
| 14 | IMBAG 2018 is explicitly conceptual; do not skip it because there is no XMI. |
| P | Pand: all panden on NL territory that meet the definition; records remain after the building is gone; objects already gone on 1 July 2009 are in principle absent. |
| H | IMGeo `Pand` ≠ IMBAG `Pand`, but both describe buildings. Explicit link: IMGeo `identificatieBAGPND` holds the identificatie of the IMBAG pand. NEN 3610 `Gebouw` is a third, more general element. IMX-Geo `Gebouw` / `Bouwwerk` is an overlay that links to BAG via `mim:equivalent` / `dct:subject`; it is not IMBAG. For PDOK BAG data, read definitie, kardinaliteit and waardelijst from IMBAG only. |
| I | `geconstateerd: "N"` is enumeratiewaarde Nee of *Indicatie* `{J, N}`: not recorded via feitelijke constatering without a regular brondocument. Not `false`, not “not observed on the ground”. |
| L | `status = Pand in gebruik` is a life-cycle phase (IMBAG ch. 8 / 9.1.3), not a time-axis. |
