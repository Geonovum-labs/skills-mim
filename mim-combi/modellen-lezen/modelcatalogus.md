---
id: modelcatalogus
titel: Formaat van een modelcatalogus
bron: []
mim-versie: "1.2"
status: toelichtend
---

# Formaat van een modelcatalogus

**In het kort.** Een modelcatalogus is een JSON-bestand dat per dataproduct (API, collectie, bestand, versie) zegt welk MIM-model het beschrijft, en welke modellen met gelijknamige elementen er niet voor gekoppeld mogen worden. De skill heeft geen vaste catalogus: je geeft er een mee. Geen onderdeel van MIM.

Sjabloon: `sjablonen/modelcatalogus.sjabloon.json`. Ingevuld voorbeeld: `voorbeelden/bag/modelcatalogus.json`. De sleutels zijn Engels gebleven, zodat bestanden van skills-mim ook hier werken.

## Velden per vermelding (`products`)

| Sleutel | Betekenis |
|---|---|
| `id`, `name` | Id van het product op de opdrachtregel, en een leesbare naam. |
| `match` | Hoe je het product herkent: `hosts`, `pathContains`, `collections`. |
| `model` | `id`, `name`, `informatiemodeltype` (`Conceptueel` of `Logisch`), `mimVersion`, `fidelity` (bronkwaliteit). |
| `sources` | Waar het model en het product gepubliceerd zijn. |
| `homonymReject` | Model-id's met gelijknamige elementen die **niet** als model van dit product gekoppeld mogen worden. Ze kunnen wel dezelfde dingen beschrijven (LR15). |
| `verifiedMapping` | Bestandsnaam van de vastgestelde veldkoppeling (`veldkoppeling.md`), of `null`. |
| `elementSummaries` | Bestandsnaam van de elementsamenvattingen van het model (`elementsamenvatting.md`), of weggelaten. |
| `note` | Gaten of waarschuwingen. |

Bestandspaden zijn relatief aan het catalogusbestand. Een catalogus kan ook `deadUrls` noemen.

## Gebruik

1. Een modelbestand van de gebruiker, als het bij het product hoort.
2. Anders de modelcatalogus, op host, pad en collectie.
3. Anders de volgorde in `model-vinden.md`.

Heeft een vermelding `verifiedMapping: null`, koppel dan het model maar koppel geen velden op naam: zeg welke velden je niet kon koppelen.

```bash
python3 scripts/mim_data.py catalogus --catalogus <catalogus.json>
```
