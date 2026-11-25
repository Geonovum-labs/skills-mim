# Evaluatie

Deze map hoort bij de route **datavragen**. De vragen toetsen **conclusies over data**, niet kennis van het metamodel. Voor kennisvragen over MIM is er de evaluatieset van het project (35 vragen, stap 3 van de takenlijst); die staat niet in deze skill.

Formaat (`prompt`, `must`, `must_not`, `conclusion`): `sjablonen/evaluatie.sjabloon.json`. Herkomst: skills-mim (`mim-interpret/evals/`), vertaald.

| Bestand | Vragen |
|---|---|
| `algemeen.json` | Modelonafhankelijk: mogelijk geen waarde, zonder-model-route. |
| `voorbeelden/bag/evaluatie.json` | Voorbeeld BAG: tien vragen over PDOK BAG `pand` → IMBAG 2018. |

Vragen voor een specifiek model staan bij het voorbeeld, zodat een nieuw model zijn eigen evaluatiebestand meebrengt.

## Uitvoeren (later)

Draai elke vraag met en zonder skill: A0 alleen webtoegang, A1 met skill, A2 alleen de naslagbestanden. De nulmeting A0 **moet** de gepubliceerde catalogus van het model mogen ophalen; anders laat een groot verschil alleen zien dat de nulmeting de bron niet heeft geopend.

## Beoordelen

Deterministische controles op de **conclusie**. Een antwoord dat het goede model noemt maar de waarde toch verkeerd leest, is **fout**.

Controles die in elke modelspecifieke set horen:

- Koppelt het model van dit product; neemt geen definitie, kardinaliteit of waardelijst over van een gelijknamig element in een ander model; zegt wél wanneer dat element waarschijnlijk hetzelfde ding beschrijft, en gebruikt een expliciete koppeling tussen de modellen als die er is.
- Leest een J/N-enumeratiewaarde niet als Boolean.
- Leest lege waarden met kardinaliteit × mogelijk geen waarde (LR1), niet als "bestaat niet".
- Labelt velden die van een verwant objecttype zijn overgenomen als `denormalized`, en door het product berekende velden als `derived` of `unmapped`.
- Beweert niet dat de data historie bevat omdat een historie-indicatie Ja is.
- Houdt identificaties met voorloopnullen als tekst.
- Onderscheidt Authentiek van Basisgegeven.
- Gebruikt de zonder-model-route als er geen model is.

Let op: de `must`- en `must_not`-zinnen in `voorbeelden/bag/evaluatie.json` komen uit skills-mim en zijn deels Engels gebleven. Een antwoord in het Nederlands kan dus een `must` missen terwijl de conclusie klopt. Beoordeel in dat geval op de `conclusion`.

## Nog niet

- Referentieantwoorden van modelleurs.
- Runs op meerdere assistenten (Mistral, Copilot, kleine modellen).
