# Voorbeeld BAG: vastgestelde veldkoppeling PDOK BAG `pand` → IMBAG 2018

Leesbare versie van [`veldkoppeling-pdok-bag-pand.json`](veldkoppeling-pdok-bag-pand.json). Formaat: [veldkoppeling.md](../../modellen-lezen/veldkoppeling.md). Gecontroleerd door de collega tegen de IMBAG-catalogus en een PDOK-voorbeeld op 30 oktober 2026; beoordeling door een modelleur staat nog open (status concept).

Dit valt buiten MIM: MIM gaat niet over de data zelf of over technische formaten. Elementsamenvattingen: [`imbag-elementsamenvattingen.json`](imbag-elementsamenvattingen.json).

Herkomst: skills-mim (`mim-interpret/examples/bag/pdok-bag-pand-mapping.md`), vertaald.

**Product.** PDOK BAG OGC API v2, collectie `pand`: `https://api.pdok.nl/kadaster/bag/ogc/v2/collections/pand`
**Model.** IMBAG Catalogus 2018 (conceptueel, termen uit MIM 1.0), <https://imbag.github.io/catalogus/>, CC BY-ND 3.0 NL. Definities zijn geparafraseerd; letterlijke waarden (enumeratiewaarden, veldnamen) zijn exact.
**Niet het model.** IMGeo 2.2 `Pand`. NEN 3610 `Gebouw`. IMX-Geo `Gebouw`, `Bouwwerk`, `Adres`. De ontologie-URI's van Kadaster (`bag.basisregistraties.overheid.nl/def/bag`) gaven op 30 oktober 2026 een 404.

## Zelfde naam, ander model

| Naam | Koppelen aan | Niet koppelen aan | Verband |
|---|---|---|---|
| `Pand` op `api.pdok.nl/kadaster/bag` | IMBAG `Pand` (code 55) | IMGeo `Pand`, NEN 3610 `Gebouw`, IMX-Geo `Gebouw`/`Bouwwerk` | Alle beschrijven gebouwen. IMGeo `Pand` verwijst naar IMBAG via `identificatieBAGPND`; IMX-Geo via `mim:equivalent` / `dct:subject`. |
| `identificatieBAGPND` | alleen IMGeo | nooit als veld van IMBAG of PDOK | De waarde is de identificatie van het IMBAG-pand (expliciete koppeling). |
| `nummeraanduidingreeks` | alleen IMGeo | nooit IMBAG Pand | — |

Is alleen een IMGeo-model gegeven bij een BAG-vraag: lees de BAG-velden niet met de definities, kardinaliteiten of waardelijsten van IMGeo; zeg dat IMBAG nodig is. Je mag zeggen dat het IMGeo-pand hetzelfde gebouw beschrijft, gekoppeld via `identificatieBAGPND`.

## Objecttype Pand (IMBAG-catalogus, paragraaf 6.4)

Parafrase: kleinste eenheid die bij de totstandkoming functioneel en bouwkundig-constructief zelfstandig is, met de aarde verbonden, betreedbaar en afsluitbaar. Wettelijke bron: art. 1 Wet BAG. Niet abstract.

**Populatie (parafrase).** Panden op Nederlands grondgebied die aan de definitie voldoen. Nieuwe gegevens komen er bij een vergunning of constatering in. Gegevens blijven bestaan nadat het pand verdwenen is. Objecten die op 1 juli 2009 al niet meer bestonden, staan er in principe niet in.

| Attribuutsoort | Kardinaliteit | Datatype | Authentiek | Mogelijk geen waarde | Historie materieel / formeel | In onderzoek |
|---|---|---|---|---|---|---|
| identificatie (55.01) | 1 | Objectnummering (16 tekens, voorloopnullen; objecttypecode `10`) | Authentiek | Nee | Nee / Nee | Nee |
| geometrie (55.20) | 1 | GM_Surface | Authentiek | Nee | Ja / Ja | Ja |
| oorspronkelijk bouwjaar (55.30) | 1 | Year | Authentiek | Nee | Ja / Ja | Ja |
| status (55.31) | 1 | Enumeratie StatusPand | Authentiek | Nee | Ja / Ja | Ja |
| geconstateerd (55.02) | 1 | Enumeratie Indicatie `{J,N}` | **Basisgegeven** | Nee | Ja / Ja | Nee |
| documentdatum (55.97) | 1 | Date | Basisgegeven | Nee | Ja / Ja | Nee |
| documentnummer (55.98) | 1 | AN 1..40 | Basisgegeven | Nee | Ja / Ja | Nee |

Geen `gebruiksdoel` bij Pand. Geen `aantal_verblijfsobjecten` bij Pand.

Relatie vanaf de andere kant: Verblijfsobject `maakt deel uit van` / `gerelateerd pand` → Pand, kardinaliteit `1..*` (IMBAG-catalogus, paragraaf 7.8.9). Een verblijfsobject kan in meerdere panden liggen.

## Velden van PDOK `pand` → IMBAG

| PDOK-veld | Koppeltype | IMBAG-element | Opmerking |
|---|---|---|---|
| `identificatie` | direct | Pand.identificatie | Als tekst houden; patroon `^[0-9]{4}10[0-9]{10}$`. Toevallig gelijke naam; IMGeo gebruikt `identificatieBAGPND`. |
| `bouwjaar` | renamed | Pand.oorspronkelijk bouwjaar | JSON-integer in de API; modeltype Year. Verandert **niet** bij een latere verbouwing. |
| `status` | direct | Pand.status / StatusPand | Gebruik de letterlijke waarde. Gesloten lijst van 10 waarden (hieronder). Levenscyclus, geen tijdlijn. |
| `geconstateerd` | direct | Pand.geconstateerd / Indicatie | Op de **items**, niet in de queryables (product is niet model). `"N"` = Nee. Basisgegeven. Geen Boolean, niet "niet waargenomen". |
| `geometry` | renamed | Pand.geometrie | Naam wijkt af: `geometry` tegenover `geometrie`. |
| `documentdatum` | direct | Pand.documentdatum | Datum van het brondocument. Basisgegeven. |
| `documentnummer` | direct | Pand.documentnummer | Kenmerk van het brondocument. Basisgegeven. |
| `gebruiksdoel` | denormalized | **Verblijfsobject**.gebruiksdoel `1..*` / Gebruiksdoel | Geen attribuutsoort van Pand. Enumeratie uit het Bouwbesluit; geen planologische bestemming en geen feitelijk gebruik. |
| `aantal_verblijfsobjecten` | derived | — | Geen attribuutsoort van IMBAG Pand. Telling van het product. De omgekeerde kant van `1..*` wordt niet bij Pand vastgelegd. |
| `verblijfsobject.href` | technical | omgekeerde kant van VBO.`maakt deel uit van` | De vorm van de array is niet de kardinaliteit. |
| `rdf_seealso` | technical | — | URI gaf 404 (30 oktober 2026). Geen werkende ontologielink. |
| `id` / paginering / `links` | technical | — | Niet gekoppeld. |

## Enumeraties (de naam is de uitgewisselde waarde)

**Indicatie:** `J` (Ja), `N` (Nee).

**StatusPand:** `Bouwvergunning verleend`, `Niet gerealiseerd pand`, `Bouw gestart`, `Pand in gebruik (niet ingemeten)`, `Pand in gebruik`, `Verbouwing pand`, `Sloopvergunning verleend`, `Pand gesloopt`, `Pand buiten gebruik`, `Pand ten onrechte opgevoerd`.

`Pand in gebruik` (parafrase): eerder `Pand in gebruik (niet ingemeten)` en de definitieve geometrie is ingemeten. Geen synoniem van "op dit moment bewoond".

**Gebruiksdoel** (bij Verblijfsobject, overgenomen op PDOK pand): `woonfunctie`, `bijeenkomstfunctie`, `celfunctie`, `gezondheidszorgfunctie`, `industriefunctie`, `kantoorfunctie`, `logiesfunctie`, `onderwijsfunctie`, `sportfunctie`, `winkelfunctie`, `overige gebruiksfunctie`.

## Product tegenover historie

De PDOK-items van `pand` (gezien op 30 oktober 2026) zijn een **momentopname**: geen `beginGeldigheid`, `voorkomen`, `tijdstipRegistratie` of `tijdstipInactief`. De historie-indicaties van IMBAG zeggen dat die attribuutsoorten in de tijd *kunnen* veranderen. IMBAG-hoofdstuk 9 noemt de velden van het extract. Leid niet af dat deze API historie levert.

## Verwante collecties (nog niet uitgewerkt)

| PDOK-collectie | IMBAG-objecttype | Let op |
|---|---|---|
| `verblijfsobject` | Verblijfsobject (56) | Hier hoort `gebruiksdoel` `1..*`. Relatie naar Pand `1..*`. Abstract supertype Adresseerbaar object. |
| `ligplaats` / `standplaats` | Ligplaats (58) / Standplaats (57) | Subtypen van Adresseerbaar object. |
| `woonplaats` / `adres` | Woonplaats / (samenstelling van Nummeraanduiding + Openbare ruimte + Woonplaats) | `adres` is een samenstelling van het product, verwant aan IMX-Geo `Adres`, **geen** IMBAG-objecttype Adres. |

## Geen RDF van IMBAG

Er was op 30 oktober 2026 geen MIM-RDF van IMBAG. Dichtstbijzijnde RDF:

- NEN 3610-2022-ontologie (niet BAG);
- IMX-Geo (`mim:equivalent`-UUID's, `dct:subject` naar BAG-begrippen): niet het model van dit product (`homonym-rejected`), maar de verwijzingen naar BAG zijn expliciet en mogen genoemd worden;
- Kadaster Skosmos-begrippen (`vocab=bag`): niveau 1, niet het informatiemodel;
- IMGeo SKOS-waardelijsten: verkeerd model.

Tot IMBAG als RDF (of MIM-XML of XMI) wordt gepubliceerd, zijn deze veldkoppeling en de HTML-catalogus de werkbron. Bronkwaliteit: `catalog-prose`.
