---
id: keuze-vs-constraint
titel: Keuze of constraint
bron: ["2.2.4.1", "2.3.7.1", "2.3.7.2", "5.7"]
mim-versie: "1.2"
status: toelichtend
---

# Keuze of constraint?

**In het kort.** Beide leggen een extra voorwaarde op. Een keuze is een modelconstructie voor "precies één van deze": ze houdt de kardinaliteiten zuiver. Een constraint is een vrije regel in tekst (en eventueel OCL) voor alles wat niet met modelelementen kan.

## Wat MIM zegt

> De `Keuze` en de `Constraint` zijn verschillende manieren om een voorwaarde of een beperking op te leggen aan een modelelement. Beide methoden hebben voor- en nadelen.
>
> — MIM 1.2, §2.2.4.1 (normatief)

> Bij het gebruik van een constraint zie je vaak dat de kardinaliteit van bijvoorbeeld twee kenmerken optioneel gemaakt is en om vervolgens via de constraint toch weer verplicht gemaakt te worden, voor precies één van de mogelijkheden.
>
> — MIM 1.2, §2.3.7.2 (normatief)

## Vergelijking (eigen uitleg)

| | Keuze | Constraint |
|---|---|---|
| Wat drukt het uit? | precies één van meerdere modelelementen (XOR) | elke conditie of beperking |
| Vorm | modelconstructie (vijf use cases) | gewone tekst, optioneel OCL |
| Kardinaliteiten | blijven zuiver (`1..1`) | worden vaak kunstmatig `0..1` |
| Machineleesbaar | ja, via de modelstructuur | alleen als er een formele specificatie is |
| Paragrafen | §2.3.7.2, §5.3 | §2.3.7.1, §5.7 |

## Beslisvragen (eigen uitleg)

1. Is de regel "precies één van deze datatypen, attribuutsoorten, relatiedoelen of relatiesoorten"? → keuze (zie de use cases in `modelelementen/keuze.md`).
2. Kan het met lengte, patroon of kardinaliteit? → gebruik die, geen constraint (§5.7).
3. Anders → constraint. Is de regel beleid dat vaak wijzigt, overweeg dan een validatieregel buiten het model (§5.7).

## Zie ook

- `modelelementen/keuze.md`, `modelelementen/constraint.md`, `onderwerpen/keuze.md`
