---
id: gegevensgroep-vs-gestructureerd-datatype
titel: Gegevensgroep of gestructureerd datatype
bron: ["5.2.2", "2.3.2.3", "2.3.2.4", "2.3.5.3", "2.3.5.4", "2.1"]
mim-versie: "1.2"
status: toelichtend
---

# Gegevensgroep of gestructureerd datatype?

**In het kort.** Beide bundelen meerdere stukjes informatie, maar ze doen iets anders. Een gegevensgroep groepeert *kenmerken van een object* die elk eigen betekenis hebben. Een gestructureerd datatype beschrijft *de vorm van één waarde* die uit onderdelen bestaat. Vraag: heeft elk onderdeel los betekenis voor het object? Dan gegevensgroep. Alleen samen? Dan gestructureerd datatype.

## Wat MIM zegt

> Een gegevensgroep is niet hetzelfde als een Gestructureerd datatype.
>
> - Een datatype beschrijft de structuur van data, een gegevensgroep beschrijft de semantiek van een kenmerk van een object.
> - Als één kenmerk van een object uit verschillende stukjes data bestaat, dan wordt een Gestructureerd datatype gebruikt. Dit is bijvoorbeeld het geval bij het gestructureerde datatype Bedrag. Deze bestaat uit een 'hoeveelheid' en 'muntsoort'.
> - Als een object meerdere kenmerken heeft, gemodelleerd als afzonderlijke attribuutsoorten, dan heeft elk kenmerk op zichzelf betekenis. Als één kenmerk wordt weggelaten, of niet bekend of ingewonnen is, dan verandert er niets aan de betekenis van de andere attribuutsoorten.
> - Een ander goed criterium is: als het datatype wordt weggelaten uit het informatiemodel, dan verliest het informatiemodel geen semantiek. Alleen de structuur van een gegeven is dan niet meer bekend.
>
> — MIM 1.2, §5.2.2 (normatief)

> Regel: het is niet de bedoeling dat eenzelfde kenmerk van een object in het ene model als een gegevensgroep gemodelleerd wordt en in het andere model als een Gestructureerd datatype. Er raakt dan semantiek verloren of er ontbreekt dan semantiek.
>
> — MIM 1.2, §5.2.2 (normatief)

## Vergelijking (eigen uitleg)

| | Gegevensgroep + gegevensgroeptype | Gestructureerd datatype |
|---|---|---|
| Wat is het? | een kenmerk van het object, met als type een groep attribuutsoorten | een datatype: de structuur van één waarde |
| Onderdelen heten | attribuutsoorten (kenmerken van het object) | data-elementen (géén kenmerken van het object) |
| Onderdeel los betekenisvol? | ja | nee, alleen in samenhang |
| Weglaten kost betekenis? | ja | nee, alleen structuur (§2.1) |
| "Identificeert zichzelf"? | nee (er zijn veel "Jan Jansen"s) | ja (er is maar één "35 euro") |
| Historie per onderdeel | per attribuutsoort mogelijk | meestal niet zinvol (§2.3.1.2) |
| Conceptueel → logisch | blijft gegevensgroep | blijft gestructureerd datatype |

## Beslisvragen (eigen uitleg)

1. Zou je één onderdeel los kunnen weglaten of als onbekend kunnen registreren, zonder dat de andere onderdelen hun betekenis verliezen? Ja → gegevensgroep.
2. Is de combinatie van onderdelen een waarde die zichzelf identificeert (bedrag, hoeveelheid met eenheid, datum)? Ja → gestructureerd datatype.
3. Heeft het "ding" een eigen bestaan, eigen eigenaar of eigen relaties? Dan is het geen van beide maar een objecttype (§5.2).

## Voorbeelden uit MIM

- **Gestructureerd datatype:** Bedrag (som en valuta), 1 liter, datum 6 april 2017 (§2.3.5.3).
- **Gegevensgroeptype:** Naam met voornaam en achternaam (§2.3.5.3); Motor van een schip in de BRK (§2.3.2.4); Brondocument in de BAG (§5.2.1).

## Drie soorten "onderdelen"

Eigen uitleg. Drie modelelementen lijken op elkaar omdat ze allemaal een naam, een datatype en een kardinaliteit hebben:

| | Attribuutsoort | Data-element | Referentie-element |
|---|---|---|---|
| Hoort bij | objecttype, gegevensgroeptype of relatieklasse | gestructureerd datatype | referentielijst |
| Is een kenmerk van | een object | een waarde | een item in een externe lijst |
| Historie, authentiek | ja (metagegevens van een kenmerk) | nee | nee |
| Bestand | `modelelementen/attribuutsoort.md` | `modelelementen/data-element.md` | `modelelementen/referentie-element.md` |

## Zie ook

- `modelelementen/gegevensgroep.md`, `modelelementen/gegevensgroeptype.md`, `modelelementen/gestructureerd-datatype.md`
