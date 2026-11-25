---
id: relatieklasse-vs-objecttype
titel: Relatieklasse of objecttype
bron: ["2.3.3.3", "5.6"]
mim-versie: "1.2"
status: toelichtend
---

# Relatieklasse of objecttype?

**In het kort.** Gaat het om gegevens over één relatie tussen twee objecten, die verdwijnen als de relatie verdwijnt? Dan is het een relatieklasse. Gelden dezelfde gegevens voor meerdere relaties tegelijk, of zijn er drie of meer objecttypen betrokken? Dan wordt het een objecttype.

## Wat MIM zegt

> *Opmerking*: de gegevens van de relatie worden voor één relatie vastgelegd en niet voor meerdere relaties tegelijk. Als dit laatste het geval is, dan worden de gegevens vastgelegd in een «Objecttype».
>
> — MIM 1.2, §2.3.3.3 (normatief)

> Het is dan niet mogelijk om het te modelleren als relatieklasse. Wel gewenst, maar het kan niet als UML-associationClass. Als deze uitzondering het geval is, dan worden de relatieklasses gemodelleerd als «Objecttype», met één inkomende relatie en één uitgaande relatie. De oorspronkelijke kardinaliteit van de beoogde relatieklasse wordt hierbij behouden.
>
> — MIM 1.2, §5.6 (normatief)

> Geef daarom in de toelichting van het objecttype aan dat elk object van dit objecttype bestaansafhankelijk is van de beide objecttypen die verbonden zijn door deze geobjectiveerde relatie.
>
> — MIM 1.2, §5.6 (normatief)

## Beslisvragen (eigen uitleg)

| Vraag | Ja → | Nee → |
|---|---|---|
| Moeten er gegevens óver de relatie worden vastgelegd? | ga door | relatiesoort |
| Gelden die gegevens per relatie apart? | ga door | objecttype ("geobjectiveerde relatie") |
| Zijn er precies twee objecttypen betrokken? | relatieklasse | objecttype, of een eigen extensie (§5.6) |

## Voorbeelden uit MIM

- **Relatieklasse wordt objecttype:** de relatie ‘overgegaan in’ bij een perceelsplitsing. De splitsingsgegevens gelden voor alle nieuwe percelen tegelijk, dus het wordt een objecttype (§5.6).
- **Objecttype:** een CONTRACT tussen twee óf meer SUBJECTen, met voor alle betrokkenen dezelfde gegevens (§2.3.3.3, §5.6).

## Let op

- Na het objectiveren is aan de metaclass niet meer te zien dat het object bestaansafhankelijk is. Leg dat vast in de toelichting (§5.6).
- MIM heeft geen regel voor de identificatie van een (geobjectiveerde) relatieklasse; dat beslist de modelleur (§5.6).

## Zie ook

- `modelelementen/relatieklasse.md`, `modelelementen/objecttype.md`
