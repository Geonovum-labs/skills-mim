# Example: BAG — verified field mapping PDOK BAG `pand` → IMBAG 2018

A *verified field mapping* (vastgestelde veldkoppeling) is a hand-checked table linking each field of a data product to the model element it represents (format: [`../../references/field-mapping-format.md`](../../references/field-mapping-format.md)). This one covers PDOK BAG `pand`. It was checked against the IMBAG catalogus and a live PDOK sample on 2026-10-30; review by a modeller is still pending (status `concept`).

It is outside MIM: MIM does not cover the data itself (M0) or technical formats (level 4). Machine copy: [`pdok-bag-pand-mapping.json`](pdok-bag-pand-mapping.json). Element summaries: [`../../../mim-core/examples/bag/imbag-element-summaries.json`](../../../mim-core/examples/bag/imbag-element-summaries.json).

**Product.** PDOK BAG OGC API v2, collection `pand`: `https://api.pdok.nl/kadaster/bag/ogc/v2/collections/pand`  
**Model.** IMBAG Catalogus 2018 (conceptueel, MIM 1.0 terms), HTML: https://imbag.github.io/catalogus/ — CC-BY-ND 3.0 NL. Element summaries paraphrase; literals (enumeratiewaarden, field names) are exact.  
**Not the model.** IMGeo 2.2 `Pand`. NEN 3610 `Gebouw`. IMX-Geo `Gebouw` / `Bouwwerk` / `Adres`. Kadaster ontology URIs (`bag.basisregistraties.overheid.nl/def/bag`) 404 as of 2026-10-30.

Last verified: 2026-10-30. Sample feature `identificatie=0003100000117485` (PDOK snapshot).

## Same names, different models

| Token | Bind | Do not bind | Relation |
|---|---|---|---|
| `Pand` on `api.pdok.nl/kadaster/bag` | IMBAG `Pand` (code 55) | IMGeo `Pand`, NEN 3610 `Gebouw`, IMX-Geo `Gebouw`/`Bouwwerk` | All describe buildings. IMGeo `Pand` links to IMBAG via `identificatieBAGPND`; IMX-Geo via `mim:equivalent` / `dct:subject`. |
| `identificatieBAGPND` | IMGeo only | never as an IMBAG/PDOK field | Its value is the IMBAG Pand identificatie (explicit link). |
| `nummeraanduidingreeks` | IMGeo only | never IMBAG Pand | — |

If only an IMGeo model is supplied for a BAG question: do not read the BAG fields with IMGeo definities, kardinaliteiten or waardelijsten; say that IMBAG is needed. You may say that the IMGeo pand describes the same building, linked via `identificatieBAGPND`.

## Objecttype Pand (IMBAG §6.4)

Paraphrase of the catalog definition: smallest unit that is functionally and structurally independent at creation, connected to the ground, enterable and lockable. Legal source: art. 1 Wet BAG. Not abstract.

**Populatie (paraphrase).** Panden on NL territory that meet the definition. New records enter on permit or constatering. Records remain after the pand is gone. Objects that had already ceased to exist on 1 July 2009 are in principle absent.

Attribuutsoorten (catalog tables 6.4.b / 7.4.x):

| Attribuutsoort | Kardinaliteit | Datatype | Authentiek | Mogelijk geen waarde | Historie materieel / formeel | In onderzoek |
|---|---|---|---|---|---|---|
| identificatie (55.01) | 1 | Objectnummering (16-char, leading zeros; objecttypecode `10`) | Authentiek | Nee | Nee / Nee | Nee |
| geometrie (55.20) | 1 | GM_Surface | Authentiek | Nee | Ja / Ja | Ja |
| oorspronkelijk bouwjaar (55.30) | 1 | Year | Authentiek | Nee | Ja / Ja | Ja |
| status (55.31) | 1 | Enumeratie StatusPand | Authentiek | Nee | Ja / Ja | Ja |
| geconstateerd (55.02) | 1 | Enumeratie Indicatie `{J,N}` | **Basisgegeven** | Nee | Ja / Ja | Nee |
| documentdatum (55.97) | 1 | Date | Basisgegeven | Nee | Ja / Ja | Nee |
| documentnummer (55.98) | 1 | AN 1..40 | Basisgegeven | Nee | Ja / Ja | Nee |

No `gebruiksdoel` on Pand. No `aantal_verblijfsobjecten` on Pand.

Relation from the other end: Verblijfsobject `maakt deel uit van` / `gerelateerd pand` → Pand, kardinaliteit `1..*` (IMBAG §7.8.9). A VBO may lie in several panden.

## PDOK `pand` fields → IMBAG

| PDOK field | Mapping type | IMBAG element | Notes |
|---|---|---|---|
| `identificatie` | direct | Pand.identificatie | Keep as string; pattern `^[0-9]{4}10[0-9]{10}$`. Lucky name match; IMGeo uses `identificatieBAGPND`. |
| `bouwjaar` | renamed | Pand.oorspronkelijk bouwjaar | API JSON integer; model type Year. Does **not** change on later verbouw. |
| `status` | direct | Pand.status / StatusPand | Use the literal. Closed list of 10 values (below). Life-cycle, not a time-axis. |
| `geconstateerd` | direct | Pand.geconstateerd / Indicatie | On **items**, not in queryables (product ≠ model). `"N"` = Nee. Basisgegeven. Not Boolean, not “unobserved”. |
| `geometry` | renamed | Pand.geometrie | Name mismatch `geometry` vs `geometrie`. |
| `documentdatum` | direct | Pand.documentdatum | Brondocument date. Basisgegeven. |
| `documentnummer` | direct | Pand.documentnummer | Brondocument id. Basisgegeven. |
| `gebruiksdoel` | denormalized | **Verblijfsobject**.gebruiksdoel `1..*` / Gebruiksdoel | Not a Pand attribuutsoort. Bouwbesluit enumeratie, not planologische bestemming, not feitelijk gebruik. |
| `aantal_verblijfsobjecten` | derived / unmapped | — | Not an IMBAG Pand attribuutsoort. Product count of related VBO. Inverse of `1..*` is not stored on Pand. |
| `verblijfsobject.href` | technical / relation-projection | inverse of VBO.`maakt deel uit van` | Array shape is not the kardinaliteit. |
| `rdf_seealso` | technical | — | URI 404 as of 2026-10-30. Do not treat as a working ontology link. |
| `id` / paging / `links` | technical | — | Unmapped. |

## Enumeraties (exchanged *naam* = value)

**Indicatie:** `J` (Ja), `N` (Nee).

**StatusPand:** `Bouwvergunning verleend`, `Niet gerealiseerd pand`, `Bouw gestart`, `Pand in gebruik (niet ingemeten)`, `Pand in gebruik`, `Verbouwing pand`, `Sloopvergunning verleend`, `Pand gesloopt`, `Pand buiten gebruik`, `Pand ten onrechte opgevoerd`.

`Pand in gebruik` (paraphrase): previously `Pand in gebruik (niet ingemeten)` and the definitive geometrie has been surveyed. It is not a synonym of “currently occupied as a dwelling”.

**Gebruiksdoel** (on Verblijfsobject, leaked onto PDOK pand): `woonfunctie`, `bijeenkomstfunctie`, `celfunctie`, `gezondheidszorgfunctie`, `industriefunctie`, `kantoorfunctie`, `logiesfunctie`, `onderwijsfunctie`, `sportfunctie`, `winkelfunctie`, `overige gebruiksfunctie`.

## Product vs history

PDOK `pand` items observed 2026-10-30 are a **snapshot**: no `beginGeldigheid`, `voorkomen`, `tijdstipRegistratie`, `tijdstipInactief`. IMBAG flags say those attribuutsoorten *can* change over time. IMBAG ch. 9 names the extract fields. Do not infer that this API returns history.

`status` remains a life-cycle value on the snapshot.

## Related collections (not fully mapped in v1)

| PDOK collection | IMBAG objecttype | Watch |
|---|---|---|
| `verblijfsobject` | Verblijfsobject (56) | `gebruiksdoel` `1..*` lives here. Relatie to Pand `1..*`. Abstract supertype Adresseerbaar object. |
| `ligplaats` / `standplaats` | Ligplaats (58) / Standplaats (57) | Subtypes of Adresseerbaar object. |
| `woonplaats` / `adres` | Woonplaats / (composite of Nummeraanduiding + Openbare ruimte + Woonplaats) | `adres` is a product composition, close to IMX-Geo `Adres`, **not** an IMBAG objecttype named Adres. |

## RDF gap

Uitgangspunt: publish needed models as RDF like `modellen.geostandaarden.nl`. **No IMBAG MIM-RDF instance was found on 2026-10-30.** Closest RDF:

- NEN 3610-2022 ontology (not BAG)
- IMX-Geo overlay (`mim:equivalent` UUIDs, `dct:subject` bag begrippen) — not the model of this product (`homonym-rejected`), but its links to BAG are explicit and may be cited
- Kadaster Skosmos begrippen (`vocab=bag`) — level 1, not the information model
- IMGeo SKOS waardelijsten — wrong model

Until Kadaster/Geonovum publish IMBAG as RDF (or MIM XML/XMI), this verified field mapping + HTML catalog are the working source. Fidelity: `catalog-prose`.
