---
id: veldkoppeling
titel: Formaat van een vastgestelde veldkoppeling
bron: ["1.6"]
mim-versie: "1.2"
status: toelichtend
---

# Formaat van een vastgestelde veldkoppeling

**In het kort.** Een vastgestelde veldkoppeling is een met de hand gecontroleerde tabel die elk veld van één dataproduct koppelt aan het modelelement dat het weergeeft. Eén JSON-bestand per product. Het koppelen valt buiten MIM, want MIM gaat niet over de data zelf of over technische formaten (§1.6). Label een koppeling dus als koppeling, niet als *volgens het model*.

Sjabloon: `sjablonen/veldkoppeling.sjabloon.json`. Ingevuld voorbeeld: `voorbeelden/bag/veldkoppeling-pdok-bag-pand.json`, met een leesbare versie in `voorbeelden/bag/veldkoppeling-pdok-bag-pand.md`. De sleutels zijn Engels gebleven (formaat van skills-mim).

## Bestand

| Sleutel | Betekenis |
|---|---|
| `about` | Eén zin over de inhoud. |
| `product`, `model` | Id van product en model, zoals in de modelcatalogus. |
| `lastVerified` | Datum van de laatste controle. |
| `checkedAgainst` | Waartegen gecontroleerd (modelbron, voorbeeldrecords). |
| `reviewedBy` | Modelleur die het beoordeeld heeft, of `null` zolang dat nog niet is gebeurd. |
| `fields` | Eén rij per veld van het product. |

## Eén rij

| Sleutel | Betekenis |
|---|---|
| `field` | Veldnaam precies zoals in het product. |
| `mappingType` | Koppeltype: `direct`, `renamed`, `denormalized`, `derived`, `technical`, `unmapped`, `homonym-rejected` (zie `datavragen.md`). |
| `element` | `Objecttype.attribuut` in het model, of `null`. Bij `denormalized` het element van het *andere* objecttype. |
| `modelName`, `waardelijst` | Naam in het model als die afwijkt; naam van de waardelijst als de waarde uit een lijst komt. |
| `confidence` | `exact`, `probable` of `none`. |
| `reasons` | Korte labels waarom de rij is wat hij is. |
| `notes` | Waarschuwing tegen een waarschijnlijke misvatting. |

Een veld dat er niet in staat, telt als `unmapped`. Vul een gat nooit op door namen te vergelijken.

## Zo maak je er een

1. Koppel het model met de modelcatalogus.
2. Neem een echt voorbeeldrecord en de veldenlijst van het product (schema, queryables).
3. Zoek per veld het element in de modelbron en controleer type, kardinaliteit en waardelijst.
4. Markeer velden van een ander objecttype als `denormalized`, berekende velden als `derived` en transportvelden als `technical`.
5. Vul `checkedAgainst` in; laat een modelleur het beoordelen en vul `reviewedBy` in.

```bash
python3 scripts/mim_data.py koppel --catalogus <catalogus.json> --product <id> --velden <a,b,c>
```
