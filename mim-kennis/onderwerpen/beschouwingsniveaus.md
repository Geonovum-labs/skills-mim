---
id: beschouwingsniveaus
titel: Beschouwingsniveaus en soorten modellen
bron: ["1.5", "1.6", "1.6.1", "1.6.2", "1.6.3", "1.6.4", "1.6.5", "1.7", "1.9", "2.4.1.2"]
mim-versie: "1.2"
status: normatief
---

# Beschouwingsniveaus: begrippen, conceptueel, logisch, technisch

**In het kort.** MIM onderscheidt vier niveaus om naar een domein te kijken: (1) begrippen, (2) conceptueel informatiemodel, (3) logisch informatiemodel, (4) technisch datamodel. MIM gaat alleen over niveau 2 en 3. Een informatiemodel is altijd óf conceptueel óf logisch, nooit een mengvorm.

## De vier niveaus

| Niveau | Soort model | Voor wie | In scope van MIM? | Paragraaf |
|---|---|---|---|---|
| 1 | model van begrippen | mensen, "de business" | nee | §1.6.1 |
| 2 | conceptueel informatiemodel | mensen: business en ICT-specialisten | ja | §1.6.2 |
| 3 | logisch informatie- of gegevensmodel | ontwerpers, ontwikkelaars, beheerders van ICT | ja | §1.6.3 |
| 4 | fysiek of technisch gegevens- of datamodel | "machines", softwareontwikkelaars | nee | §1.6.4 |

> Het MIM concentreert zich namelijk op het tweede en derde niveau.
>
> — MIM 1.2, §1.6 (normatief)

## Conceptueel (niveau 2)

> Een conceptuele informatiemodel richt zich speciefiek op de semantiek van dingen en hun eigenschappen. Het definieert het ‘wat’: welke 'onderwerpen van gesprek' ('concepten', 'dingen’) worden onderscheiden in de beschouwde werkelijkheid, wat betekenen zij, hoe verhouden ze zich tot elkaar en welke informatie is daarvan relevant.
>
> — MIM 1.2, §1.6.2 (normatief)

> Met conceptueel wordt niet bedoeld abstract of hoog over, de beschrijvingen van de informatie die beschikbaar is zijn heel precies en concreet.
>
> — MIM 1.2, §1.6.2 (normatief)

## Logisch (niveau 3)

> Het gaat hierbij, in tegenstelling tot een conceptueel model, dus veel meer om het **‘hoe’**. Het slaat de brug tussen werkelijkheid en systemen maar beschrijft nog niet de implementatie in die systemen.
>
> — MIM 1.2, §1.6.3 (normatief)

## Verschillen conceptueel en logisch (eigen samenvatting)

| | Conceptueel (2) | Logisch (3) |
|---|---|---|
| Vraag | wat? | hoe? |
| Afhankelijk van uitwisselingsstandaarden | nee | ja (identificaties, geometrieversies, tijdlijnen) (§1.6.2) |
| Bereik | keten- en koppelvlakoverstijgend | specifiek voor een koppelvlak, keten of toepassing (§1.6.2) |
| Taal | natuurlijke taal | formele taal, waar mogelijk gegenereerd uit het conceptuele model (§1.6.3) |
| Naamgeving | alternatief 1: natuurlijke taal (§5.15.3) | alternatief 2: leesbaar door systemen (§5.15.4) |
| Historie | alleen de metagegevens heeft tijdlijn geldigheid/registratie | ook de attributen van de tijdlijnen (§5.8.2) |
| Mixin bij generalisatie | niet | mag (§2.4.3.41) |

## Nooit een mengvorm

> Het moge duidelijk zijn dat het altijd het één of het ander is, conceptueel of logisch. Een combinatie van beide in één model leidt tot verwarring.
>
> — MIM 1.2, §1.6.5 (normatief)

Het metagegeven Informatiemodeltype van het informatiemodel legt de keuze vast: `Conceptueel` of `Logisch` (§2.4.1.2).

Eigen uitleg. MIM schrijft geen volgorde voor. Eerst conceptueel en dan logisch ligt voor de hand, zeker bij meerdere koppelvlakken, maar alleen een logisch model maken mag ook (§1.6.5).

## Linked Data

In Linked Data vallen conceptueel en logisch grotendeels samen (§1.9). Voor modellen die zowel in UML als in Linked Data moeten worden uitgedrukt, adviseert MIM het type "conceptueel informatiemodel":

> Voor modellen die zowel een UML als een Linked Data implementatie vereisen kan beter gekozen worden voor het type "conceptueel informatiemodel".
>
> — MIM 1.2, §1.9 (normatief)

## Wat is een metamodel?

> Een metamodel is een model van een model. Het definieert een verzameling van modelleerconstructies in de vorm van bouwstenen, oftewel modelelementen zoals een objecttype, relatiesoort en attribuutsoort, met bijbehorende betekenis en met bijbehorende afspraken omtrent hoe deze toe te passen.
>
> — MIM 1.2, §1.7 (normatief)

## Zie ook

- `onderwerpen/begrippen-en-definities.md` (relatie met niveau 1)
- `modelelementen/informatiemodel.md`
- Letterlijke tekst: `python3 scripts/mim.py paragraaf 1.6 --met-sub`
