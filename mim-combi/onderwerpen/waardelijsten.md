---
id: waardelijsten
titel: Waardelijsten
bron: ["2.3.4", "5.4", "2.4.3.24", "2.4.3.25", "2.4.3.26", "2.4.3.27"]
mim-versie: "1.2"
status: normatief
---

# Waardelijsten

**In het kort.** Een waardelijst geeft de toegestane waarden van een attribuutsoort. MIM kent drie soorten: enumeratie (vast in het model), referentielijst (extern beheerd, met beschreven structuur) en codelijst (extern beheerd, zonder beschreven structuur). Welke je kiest, hangt af van hoe vaak de lijst verandert en of het model de structuur van de items moet kennen.

## Wat MIM zegt

> Een datatype waarvan de mogelijke waarden zijn opgesomd in een lijst. De waarde van een attribuutsoort moet één van de waarden zijn uit de gespecificeerde waardelijst.
>
> — MIM 1.2, §2.3.4 (normatief)

> In veel registraties wordt gewerkt met codetabellen om de mogelijke waarden van een attribuutsoort te specificeren. Deze mogelijke waarden kunnen op verschillende manieren worden opgenomen, afhankelijk van de gewenste stabiliteit.
>
> — MIM 1.2, §5.4 (normatief)

## Overzicht

| Soort | Onderdelen | Bestand |
|---|---|---|
| Enumeratie | enumeratiewaarden | `modelelementen/enumeratie.md` |
| Referentielijst | referentie-elementen | `modelelementen/referentielijst.md` |
| Codelijst | geen (structuur staat buiten het model) | `modelelementen/codelijst.md` |

De keuze tussen de drie staat in `onderscheidingen/enumeratie-vs-referentielijst-vs-codelijst.md`.

## Metagegevens die alleen bij extern beheerde lijsten horen

| Metagegeven | Referentielijst | Codelijst | Paragraaf |
|---|---|---|---|
| Locatie (waar de lijst gepubliceerd is) | verplicht | verplicht | §2.4.3.24 |
| Doelformaat (bijvoorbeeld SKOS, CSV) | - | verplicht | §2.4.3.25 |
| Waarde-item (welk item de waarde is) | - | optioneel | §2.4.3.26 |
| Profielspecificatie (technische implementatie) | - | optioneel | §2.4.3.27 |

Bron: de UML-tabellen §3.2.3.1 en §3.2.3.4. De LD-tabel van de codelijst noemt alleen Locatie (§4.3.3.3). Let op: volgens §2.4.3.25 geldt Doelformaat voor Codelijst én Referentielijst, maar de tabellen van de referentielijst noemen het niet (zie `bekende-onduidelijkheden.md`, I19).

## Richtlijnen (eigen samenvatting)

- Modelleer elke waardelijst apart, met eigen naam en locatie; gedeelde structuur kan via een abstracte referentielijst (§5.4.2).
- Behandel een referentielijst van een ander model niet als enumeratie in je eigen model (§5.4.2).
- Geen waarde "onbekend" in eigen enumeraties; gebruik Mogelijk geen waarde (§5.11).
- In MIM 1.2 is de schrijfwijze "waardelijst" (zonder -n) consistent gemaakt (versielog, issue 333).

## Zie ook

- `onderwerpen/mogelijk-geen-waarde.md`
- Letterlijke tekst: `python3 scripts/mim.py paragraaf 5.4 --met-sub`
