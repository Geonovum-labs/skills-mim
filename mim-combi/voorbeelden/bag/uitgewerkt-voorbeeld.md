# Voorbeeld BAG: uitgewerkte vraag (PDOK BAG pand → IMBAG)

Vraag: *Wat betekent `geconstateerd = "N"` op dit pand, is `gebruiksdoel` een gegeven van Pand, en zijn dit historische versies?*

Dit voorbeeld loopt de route voor datavragen uit `SKILL.md` door op één dataset. Open geen IMGeo-XMI. Draai de opdrachten vanuit de map van de skill. Zonder Python lees je dezelfde sleutels in [`modelcatalogus.json`](modelcatalogus.json), [`veldkoppeling-pdok-bag-pand.json`](veldkoppeling-pdok-bag-pand.json) en [`imbag-elementsamenvattingen.json`](imbag-elementsamenvattingen.json).

Herkomst: skills-mim (`mim-interpret/examples/bag/worked-example.md`), vertaald.

## Invoer (in de data gezien)

Item uit PDOK BAG OGC API v2 `pand`, gecontroleerd door de collega op 30 oktober 2026, `identificatie=0003100000117485`:

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

De queryables van dezelfde collectie noemen `geconstateerd` **niet**. Geometrie weggelaten.

## 1. Model koppelen

```bash
python3 scripts/mim_data.py catalogus --catalogus voorbeelden/bag/modelcatalogus.json
```

Product `api.pdok.nl/kadaster/bag` + collectie `pand` → **IMBAG Catalogus 2018** (conceptueel, bronkwaliteit `catalog-prose`).
Niet koppelen: IMGeo `Pand`, NEN 3610 `Gebouw`, IMX-Geo `Gebouw` en `Bouwwerk`.
`rdf_seealso` is een dode URI; volg hem niet als ontologie.

## 2. Velden koppelen (vastgestelde veldkoppeling)

```bash
python3 scripts/mim_data.py koppel --catalogus voorbeelden/bag/modelcatalogus.json --product pdok-bag-pand \
  --velden identificatie,bouwjaar,status,geconstateerd,gebruiksdoel,aantal_verblijfsobjecten,geometry,rdf_seealso
```

| veld | koppeltype | element |
|---|---|---|
| identificatie | direct | Pand.identificatie |
| bouwjaar | renamed | Pand.oorspronkelijk bouwjaar (Year) |
| status | direct | Pand.status / StatusPand |
| geconstateerd | direct | Pand.geconstateerd / Indicatie |
| geometry | renamed | Pand.geometrie |
| gebruiksdoel | **denormalized** | **Verblijfsobject**.gebruiksdoel `1..*` |
| aantal_verblijfsobjecten | **derived** | — |
| rdf_seealso | technical | — |

## 3. Elementsamenvattingen

```bash
python3 scripts/mim_data.py samenvatting --samenvattingen voorbeelden/bag/imbag-elementsamenvattingen.json Pand.geconstateerd
python3 scripts/mim_data.py waardelijst --samenvattingen voorbeelden/bag/imbag-elementsamenvattingen.json Indicatie
python3 scripts/mim_data.py waardelijst --samenvattingen voorbeelden/bag/imbag-elementsamenvattingen.json StatusPand
python3 scripts/mim_data.py samenvatting --samenvattingen voorbeelden/bag/imbag-elementsamenvattingen.json Verblijfsobject.gebruiksdoel
python3 scripts/mim_data.py samenvatting --samenvattingen voorbeelden/bag/imbag-elementsamenvattingen.json Verblijfsobject.maaktDeelUitVan
```

## 4. Antwoord

**Antwoord.** `geconstateerd = "N"` betekent **Nee** in de gesloten enumeratie Indicatie `{J, N}` (*volgens het model*). Het pand is **niet** opgevoerd via een feitelijke constatering zonder regulier brondocument. Het is geen Boolean `false` en betekent niet "dit gebouw is niet in het terrein waargenomen". Authentiek is **Basisgegeven**, dus er geldt geen gebruiksplicht (*volgens het model*). Het veld ontbreekt in de queryables maar staat wel op het item: product is niet model (*in de data gezien*).

`gebruiksdoel = "woonfunctie"` is **geen** attribuutsoort van Pand. Het is Verblijfsobject.gebruiksdoel, kardinaliteit `1..*`, enumeratie Gebruiksdoel (Bouwbesluit), Authentiek. De API neemt het over op `pand`. Het is geen planologische bestemming en geen feitelijk gebruik. Met 15 gekoppelde verblijfsobjecten is één overgenomen waarde hooguit een steekproef, geen zelfstandig gegeven "het pand heeft een woonfunctie".

`aantal_verblijfsobjecten = 15` is een door het product berekende telling, geen attribuutsoort van Pand. De relatie in het model loopt andersom: een verblijfsobject `maakt deel uit van` één of meer panden (`1..*`). Een verblijfsobject **kan** in meerdere panden liggen (*volgens het model*).

`status = "Pand in gebruik"` is de exacte enumeratiewaarde: eerder `Pand in gebruik (niet ingemeten)`, en de definitieve geometrie is ingemeten. Het is een fase in de **levenscyclus**, geen tijdlijn, en geen synoniem van "bewoond".

`bouwjaar = 1991` hoort bij *oorspronkelijk bouwjaar* (Year, Authentiek, kardinaliteit 1, mogelijk geen waarde Nee). Een latere verbouwing verandert het niet. Het JSON-type integer gaat niet boven het modeltype. IMBAG zet materiële historie op Ja voor deze attribuutsoort; volg het model, niet het lesvoorbeeld "bouwjaar → geen tijdlijn geldigheid" in MIM. Deze momentopname bevat toch **geen** `beginGeldigheid` of `voorkomen`; beweer niet dat er historische versies zijn.

`identificatie` is een tekenreeks van 16 tekens met voorloopnullen (gemeentecode `0003` + objecttypecode `10` + volgnummer). Zet hem niet om naar een getal.

**Basis.** Model IMBAG Catalogus 2018 (Conceptueel, termen uit MIM 1.0) › Pand / Verblijfsobject; bron <https://imbag.github.io/catalogus/>; product PDOK BAG OGC API v2, collectie `pand`. Bronkwaliteit `catalog-prose`. Geen IMBAG-RDF gepubliceerd op `modellen.geostandaarden.nl` (30 oktober 2026).

## Tegenvoorbeeld (een ander model bij de hand)

Dezelfde gegevens, plus een logische IMGeo-XMI: lees `geconstateerd`, `status` en `bouwjaar` **niet** met IMGeo `Pand` (`homonym-rejected`); dat zijn attribuutsoorten van IMBAG. Zeg wél dat IMGeo `Pand` hetzelfde soort gebouw beschrijft, en dat `identificatieBAGPND` in IMGeo de expliciete koppeling naar dit IMBAG-pand is (*volgens het model*, in IMGeo). `nummeraanduidingreeks` bestaat alleen in IMGeo en zegt niets over dit BAG-record.
