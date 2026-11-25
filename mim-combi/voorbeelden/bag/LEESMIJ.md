# Voorbeeld: BAG

Deze map past de route voor datavragen toe op één echte dataset: de **PDOK BAG OGC API v2**, collectie `pand`, gelezen met de **IMBAG Catalogus 2018** (het informatiemodel van de Basisregistratie Adressen en Gebouwen). Het is een voorbeeld, geen regel: de algemene bestanden van de skill hangen er niet van af.

Herkomst: skills-mim (`mim-interpret/examples/bag/` en `mim-core/examples/bag/`), vertaald en samengevoegd. Laatst gecontroleerd door de collega: 30 oktober 2026. Niet beoordeeld door een BAG-modelleur.

## Bestanden

| Bestand | Wat | Formaat |
|---|---|---|
| [`modelcatalogus.json`](modelcatalogus.json) | PDOK BAG-collecties → IMBAG 2018, plus modellen met gelijknamige elementen die niet gekoppeld mogen worden (IMGeo, NEN 3610, IMX-Geo) | [modelcatalogus.md](../../modellen-lezen/modelcatalogus.md) |
| [`veldkoppeling-pdok-bag-pand.json`](veldkoppeling-pdok-bag-pand.json) | Vastgestelde veldkoppeling PDOK `pand` → IMBAG | [veldkoppeling.md](../../modellen-lezen/veldkoppeling.md) |
| [`veldkoppeling-pdok-bag-pand.md`](veldkoppeling-pdok-bag-pand.md) | Leesbare versie, met enumeraties en de opmerking over de momentopname | — |
| [`imbag-elementsamenvattingen.json`](imbag-elementsamenvattingen.json) | Elementsamenvattingen IMBAG 2018 (Pand, Verblijfsobject, Adresseerbaar object, hun attribuutsoorten, waardelijsten Indicatie, StatusPand, Gebruiksdoel) | [elementsamenvatting.md](../../modellen-lezen/elementsamenvatting.md) |
| [`uitgewerkt-voorbeeld.md`](uitgewerkt-voorbeeld.md) | Uitgewerkte vraag en antwoord over één pand, met een weigering | — |
| [`evaluatie.json`](evaluatie.json) | Tien evaluatievragen E-BAG-01 tot en met E-BAG-10 | [`LEESMIJ.md`](../../evaluatie/LEESMIJ.md) |

## Uitvoeren (vanuit de map van de skill)

```bash
python3 scripts/mim_data.py catalogus --catalogus voorbeelden/bag/modelcatalogus.json
python3 scripts/mim_data.py koppel --catalogus voorbeelden/bag/modelcatalogus.json --product pdok-bag-pand --velden identificatie,bouwjaar,status,geconstateerd,gebruiksdoel,aantal_verblijfsobjecten,geometry
python3 scripts/mim_data.py samenvatting --samenvattingen voorbeelden/bag/imbag-elementsamenvattingen.json Pand.geconstateerd
python3 scripts/mim_data.py waardelijst --samenvattingen voorbeelden/bag/imbag-elementsamenvattingen.json StatusPand
```

## Koppelingen in dit voorbeeld

| Product of collectie | Model | Type | Bronkwaliteit | Niet koppelen (homoniemen; mogelijk verwant) |
|---|---|---|---|---|
| PDOK BAG OGC API v2 `pand` (met veldkoppeling), `verblijfsobject` (nog zonder) | IMBAG Catalogus 2018 | Conceptueel | catalog-prose | IMGeo Pand; NEN 3610 Gebouw; IMX-Geo Gebouw, Bouwwerk, Adres; dode `rdf_seealso` |
| PDOK / BGT IMGeo-collecties | IMGeo 2.2 | Conceptueel en logisch | ea-xmi + skos | IMBAG Pand |
| Linked Data op basis van NEN 3610 | NEN 3610-2022-ontologie | Logisch / LD | rdf | BAG-objecttypen |
| IMX-Geo (registratie-overstijgend) | IMX-Geo | RDF-laag | rdf | Niet IMBAG; `Adres` is een samenstelling |

Wat het voorbeeld laat zien: `geconstateerd = "N"` is een J/N-enumeratiewaarde, geen Boolean; `gebruiksdoel` op `pand` is overgenomen van Verblijfsobject; `aantal_verblijfsobjecten` is afgeleid; de PDOK-collectie is een momentopname, ook al zet IMBAG historie op Ja; IMGeo `Pand` mag niet gebruikt worden om BAG-velden te lezen, maar mag genoemd worden als beschrijving van hetzelfde gebouw (gekoppeld via `identificatieBAGPND`).

## Bronnen (laatst gecontroleerd door de collega op 30 oktober 2026)

| Model | Type | Bronkwaliteit | Bron |
|---|---|---|---|
| IMBAG Catalogus 2018 | Conceptueel | catalog-prose | <https://imbag.github.io/catalogus/>; PDF Catalogus-BAG-2018 |
| IMGeo 2.2 | Conceptueel en logisch | ea-xmi + skos | `register.geostandaarden.nl/informatiemodel/imgeo/2.2/` |
| NEN 3610-2022-ontologie | Logisch / LD | rdf | <https://modellen.geostandaarden.nl/def/nen3610> |
| IMX-Geo | RDF-laag | rdf | <https://modellen.geostandaarden.nl/def/imx-geo/> |
| IMKAD 2.3.1 (BRK) | — | niet leesbaar | register: alleen `IMKAD-23.1.EAP` |

Er was op 30 oktober 2026 geen MIM-RDF van IMBAG gepubliceerd, dus de HTML-catalogus is de bron. IMBAG gebruikt termen uit MIM 1.0. `imbag.github.io` is geen standaard toegestane host; geef `--sta-toe imbag.github.io` mee.

Dode links voor dit domein: `https://bag.basisregistraties.overheid.nl/def/bag` en de `rdf_seealso`-URI's op PDOK-features (404); `https://brk.basisregistraties.overheid.nl/def/brk` (404). Kadaster Skosmos (`catalogus.kadaster.nl`, vocabulaire `bag`) heeft de begrippen (niveau 1), niet het informatiemodel.

## De leesregels toegepast op IMBAG

Regelnummers verwijzen naar [leesregels.md](../../modellen-lezen/leesregels.md). Hoofdstuknummers van IMBAG staan er als "IMBAG-hoofdstuk".

| Regel | In IMBAG 2018 |
|---|---|
| LR1 | Pand.identificatie: kardinaliteit `1`, mogelijk geen waarde Nee. Leeg is fout. |
| LR3 | Relatiesoort `maakt deel uit van` / relatierol `gerelateerd pand`: Verblijfsobject → Pand, kardinaliteit `1..*` (een verblijfsobject kan in meerdere panden liggen). Hoeveel verblijfsobjecten per pand is Kardinaliteit relatie bron, geen attribuutsoort van Pand. |
| LR4 | `Adresseerbaar object` is abstract; subtypen Ligplaats, Standplaats, Verblijfsobject. |
| LR5 | `StatusPand`, `Indicatie` en `Gebruiksdoel` zijn gesloten enumeraties. Gebruik de waarden letterlijk (`Pand in gebruik`, `N`, `woonfunctie`). |
| LR6 | `identificatie` is een tekenreeks van 16 tekens met voorloopnullen. IMBAG typeert oorspronkelijk bouwjaar als Year; PDOK levert het als JSON-integer. |
| LR7 | `objectnummering` (delen van de identificatie) is samengesteld. Brondocument (`documentdatum` + `documentnummer`) gedraagt zich als een gedeelde groep. |
| LR8 | Het geometriedomein `puntOfVlak` van Verblijfsobject is een keuze: punt of vlak, niet allebei. |
| LR9 | MIM gebruikt bouwjaar als voorbeeld zonder tijdlijn geldigheid; IMBAG zet bij oorspronkelijk bouwjaar materiële historie op Ja. Volg IMBAG. IMBAG-hoofdstuk 9 noemt de historievelden van het extract. |
| LR11 | Pand.`status` en oorspronkelijk bouwjaar zijn Authentiek; Pand.`geconstateerd` is **Basisgegeven**. |
| LR13 | IMBAG 2018 is uitdrukkelijk conceptueel; sla het niet over omdat er geen XMI is. |
| LR14 | Pand: alle panden op Nederlands grondgebied die aan de definitie voldoen; gegevens blijven bestaan nadat het gebouw verdwenen is; objecten die op 1 juli 2009 al weg waren, staan er in principe niet in. |
| LR15 | IMGeo `Pand` is niet IMBAG `Pand`, maar beide beschrijven gebouwen. Expliciete koppeling: IMGeo `identificatieBAGPND` bevat de identificatie van het IMBAG-pand. NEN 3610 `Gebouw` is een derde, algemener element. IMX-Geo `Gebouw` en `Bouwwerk` zijn een laag die met `mim:equivalent` en `dct:subject` naar BAG verwijst; dat is niet IMBAG. Lees voor PDOK BAG-data definitie, kardinaliteit en waardelijst alleen uit IMBAG. |
| LR16 | `geconstateerd: "N"` is enumeratiewaarde Nee van Indicatie `{J, N}`: niet opgevoerd via feitelijke constatering zonder regulier brondocument. Geen `false`, niet "niet in het terrein waargenomen". |
| LR17 | `status = Pand in gebruik` is een fase in de levenscyclus (IMBAG-hoofdstuk 8 en 9.1.3), geen tijdlijn. |

## Bekende gaten

- Alleen voor `pand` is er een veldkoppeling. `verblijfsobject`, `ligplaats`, `standplaats`, `woonplaats` en `adres` zijn aan IMBAG gekoppeld maar niet uitgewerkt (`adres` is een samenstelling van het product, geen objecttype van IMBAG).
- Geen veldkoppeling voor IMGeo; IMGeo staat er alleen om koppeling aan BAG-data te blokkeren en de verwijzing vast te leggen.
- Geen MIM-RDF van IMBAG om te lezen.
- De veldkoppeling is nog niet door een modelleur beoordeeld (`reviewedBy: null`).
- In onderzoek (IMBAG-hoofdstuk 9.2) is alleen als vlag genoemd.

## Licentie

De IMBAG Catalogus 2018 valt onder CC BY-ND 3.0 NL. Elementsamenvattingen en de veldkoppeling parafraseren de definities en verwijzen naar de catalogus; namen van enumeratiewaarden zijn letterlijk overgenomen omdat het de uitgewisselde waarden zijn. Koppel BAG-adressen niet aan personen.
