---
id: elementsamenvatting
titel: Formaat van elementsamenvattingen
bron: ["2.4.3.19", "2.4.3.16"]
mim-versie: "1.2"
status: toelichtend
---

# Formaat van elementsamenvattingen

**In het kort.** Een elementsamenvatting is een korte samenvatting in vaste vorm van één element uit een informatiemodel (definitie, type, kardinaliteit, mogelijk geen waarde, authentiek, historie, waardelijst), zodat een agent niet het hele model hoeft te lezen. Alle samenvattingen van één model staan in één JSON-bestand. Niet te verwarren met de bestanden in `modelelementen/`: die beschrijven de MIM-metaclasses zelf, een elementsamenvatting beschrijft een element van een concreet model.

Sjabloon: `sjablonen/elementsamenvattingen.sjabloon.json`. Ingevuld voorbeeld: `voorbeelden/bag/imbag-elementsamenvattingen.json`. De sleutels zijn Engels gebleven (formaat van skills-mim).

## Bestand

| Sleutel | Betekenis |
|---|---|
| `about` | Eén zin over de inhoud. |
| `model` | Model-id, zoals in de modelcatalogus. |
| `fidelity` | Bronkwaliteit: `rdf`, `catalog-prose`, `skos`, `derived-technical`, `ea-xmi`. |
| `source`, `sourceLicense` | Waar het model staat en onder welke licentie. Parafraseer als de licentie kopiëren verbiedt. |
| `lastVerified` | Datum van de laatste controle tegen de bron. |
| `elements` | Samenvattingen, met als sleutel `Objecttype` of `Objecttype.attribuut` (relaties: `Objecttype.relatienaam`). |
| `valuelists` | Waardelijsten op naam: `kind` (`Enumeratie`, `Referentielijst`, `Codelijst`) en `values` (`naam`, eventueel `definitie`). |

## Eén element

Vul in wat het model zegt; laat een sleutel weg in plaats van te gokken.

| Sleutel | Betekenis |
|---|---|
| `kind` | `Objecttype`, `Attribuutsoort`, `Relatiesoort`, `Gegevensgroep`, … |
| `naam`, `alias`, `code`, `owner` | Naam, andere namen, cataloguscode, objecttype waar het bij hoort. |
| `definitie`, `populatie` | Geparafraseerde definitie; welke exemplaren in de registratie staan (LR14). |
| `datatype`, `waardelijstKind` | Datatype of naam van de waardelijst, en de soort lijst. |
| `kardinaliteit`, `mogelijkGeenWaarde` | Zoals in het model (LR1). |
| `identificerend`, `authentiek` | Identificerend; waarde van Authentiek (`Authentiek`, `Basisgegeven`, …; LR11). |
| `historie` | `{"materieel": bool, "formeel": bool}`: conceptuele indicaties (LR9). |
| `abstract`, `supertypes`, `attributes` | Bij objecttypen. |
| `rol`, `doel` | Bij relatiesoorten. |
| `note` | Korte waarschuwing tegen een waarschijnlijke misvatting. |

## Opzoeken

```bash
python3 scripts/mim_data.py samenvatting --samenvattingen <bestand> <Objecttype[.attribuut]>
python3 scripts/mim_data.py waardelijst --samenvattingen <bestand> <Waardelijst>
```

Zonder Python: open het bestand en lees `elements.<sleutel>` of `valuelists.<naam>`. Ontbreekt de sleutel, dan is het element niet samengevat: zeg dat en verzin het niet.
