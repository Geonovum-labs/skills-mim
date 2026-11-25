---
id: datavragen
titel: Datavragen beantwoorden met een MIM-model
bron: ["1.6", "2.3.2.1", "2.4.3.17"]
mim-versie: "1.2"
status: toelichtend
---

# Datavragen beantwoorden met een MIM-model

**In het kort.** Een datavraag gaat over wat een veld, code of record in een dataset betekent. Je zoekt eerst het model van precies die dataset, koppelt de velden aan modelelementen, en leest dan de waarden met de leesregels. Het koppelen van data aan een model is geen onderdeel van MIM: data en technische formaten (beschouwingsniveau 4) vallen erbuiten (§1.6). Dit bestand is dus eigen werkwijze, geen standaard.

Herkomst: skills-mim (`mim-interpret/SKILL.md` en `references/interpretation-rules.md`), vertaald en ingepast.

## Werktermen

MIM-termen (objecttype, attribuutsoort, kardinaliteit, waardelijst, …) houden hun MIM-betekenis. Daarnaast gebruikt deze skill deze werktermen:

| Term | Betekenis |
|---|---|
| Dataproduct | Een concrete dataset, download of API, bijvoorbeeld één collectie van een OGC API. Niet het model. |
| Modelcatalogus | Bestand dat zegt welk informatiemodel welk dataproduct beschrijft, en welke modellen met gelijknamige elementen niet gekoppeld mogen worden. Formaat: `modelcatalogus.md`. |
| Model koppelen | Vaststellen welk model dit product beschrijft, met de modelcatalogus. Het gekoppelde model heet het **gebonden model**. |
| Vastgestelde veldkoppeling | Met de hand gecontroleerde tabel die elk veld van een dataproduct koppelt aan het modelelement dat het weergeeft. Formaat: `veldkoppeling.md`. |
| Koppeltype | Hoe een veld zich tot het element verhoudt; zie de tabel hieronder. |
| Elementsamenvatting | Korte samenvatting in vaste vorm van één modelelement, zodat je niet het hele model hoeft te lezen. Formaat: `elementsamenvatting.md`. |
| Homoniem | Zelfde naam, ander modelelement. Niet uitwisselbaar, wel mogelijk verwant (leesregel LR15). |
| Bronkwaliteit | Uit wat voor bron de kennis over het model komt: `rdf`, `catalog-prose` (HTML- of PDF-catalogus), `skos`, `derived-technical` (een API-schema) of `ea-xmi`. |
| Bewijslabel | Waar een bewering vandaan komt: *volgens het model* (het model zegt het), *in de data gezien*, of *afgeleid* (redenering, staat nergens). |
| Momentopname (snapshot) | Het product toont alleen de huidige stand, geen eerdere versies (voorkomens). |
| Zonder-model-route | Geen model gevonden: zeg dat, label elk antwoord *afgeleid* en verzin geen elementnamen. |

## Drie regels voor data

| # | Regel | Gevolg voor de data |
|---|---|---|
| D1 | **Model is niet data.** Een objecttype is een soort ding, geen tabel of API-collectie (§2.3.2.1). Producten kunnen velden platslaan, overnemen of weglaten. | Een veld op een collectie is niet vanzelf een attribuutsoort van het gelijknamige objecttype. Noem altijd het koppeltype. |
| D2 | **Product is niet model.** Een API, extract of "actueel"-bestand is een projectie op niveau 4. Ontbrekende filtervelden (queryables), velden overgenomen van verwante objecten en de keuze tussen momentopname en volledige historie zijn keuzes van het product. | Een veld dat niet in de filterlijst staat, kan toch in het model staan. |
| D3 | **Afgeleid in het product.** Indicatie afleidbaar (§2.4.3.17) geldt nog steeds, maar producten zetten die vaak niet bij velden die ze zelf berekenen (tellingen, totalen, labels). | Dan is het koppeltype `derived`, `denormalized` of `unmapped` het signaal: zo'n veld is geen zelfstandig bewijs over het modelelement. |

Het gebonden model gaat boven de lesvoorbeelden in de MIM-tekst.

## Koppeltypen

De waarden blijven Engels, omdat ze in de JSON-bestanden staan.

| Koppeltype | Betekenis |
|---|---|
| `direct` | Zelfde naam, zelfde element. |
| `renamed` | Naam in het product wijkt af van de naam in het model (product `geometry`, model `geometrie`). |
| `denormalized` | De waarde hoort bij een ander, verwant objecttype en is op dit record overgenomen. |
| `derived` | Door het product berekend; geen zelfstandig bewijs. |
| `technical` | Transport, paginering, links, dode URI. |
| `unmapped` | Geen modelelement; zeg dat. Een veld dat niet in de veldkoppeling staat, is `unmapped`. |
| `homonym-rejected` | Gelijknamig element uit een ander model; niet het element van dit veld. Gebruik de definitie en kardinaliteit niet; noem een verwantschap of expliciete koppeling als die er is (LR15). |

## Welke leesregel bij welke vraag

Na de veldkoppeling weet je het element. Lees de elementsamenvatting en pas de leesregels uit `leesregels.md` toe:

| Vraag over de waarde | Leesregel |
|---|---|
| Leeg veld of NULL | LR1 (kardinaliteit × mogelijk geen waarde) |
| Herhaalde waarden of groepen | LR2 |
| Relaties; tellingen van de omgekeerde kant | LR3 |
| Abstracte typen; geërfde kenmerken | LR4 |
| Gesloten of externe lijst; exacte naam | LR5 |
| Voorloopnullen; modeltype tegenover JSON-type | LR6 |
| Samengestelde waarde of groep | LR7 |
| Precies één van meerdere | LR8 |
| Historie-indicatie tegenover wat het product levert | LR9; kijk of het product versievelden heeft voordat je historie beweert |
| Authentiek tegenover Basisgegeven | LR11 |
| Conceptueel model zonder XMI of RDF | LR13 |
| Wie staat er in de registratie | LR14 |
| Zelfde naam in een ander model | LR15 |
| J/N is geen Boolean | LR16 |
| `status` is levenscyclus, geen tijdlijn | LR17 |

## Wat bij welke situatie

| Situatie | Doe |
|---|---|
| Geen model voor dit product | Zonder-model-route. |
| Model gekoppeld, maar geen vastgestelde veldkoppeling | Noem de velden niet-gekoppeld; koppel niet op naam. |
| Gelijknamig element uit een ander model | Gebruik de definitie, kardinaliteit en waardelijst niet (`homonym-rejected`); koppel het model van deze dataset. Zeg of het waarschijnlijk hetzelfde ding beschrijft; gebruik een expliciete koppeling als die er is. |
| Alleen een ander model bij de hand | Beantwoord de vraag niet vanuit dat model alsof het het model van deze dataset is; zeg welk model nodig is. Je mag zeggen wat het andere model beschrijft, duidelijk gelabeld. |
| Model in MIM 2.0-vocabulaire | Stop (LR18). |
| URI van model of ontologie geeft 404 | Val terug op catalogus en elementsamenvattingen. Beweer niet dat de link werkte. |
| Geen netwerk | Gebruik de lokale modelcatalogus, veldkoppeling en elementsamenvattingen. |
| Geen Python | Lees de JSON-bestanden zelf (zie SKILL.md, "Zonder scripts"). |
| Iemand wil code of een schema laten genereren | Buiten deze skill. Begin niet met implementeren. |

Zie `voorbeelden/bag/uitgewerkt-voorbeeld.md` voor de hele route op één dataset.
