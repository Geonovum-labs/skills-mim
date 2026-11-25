---
id: enumeratie-vs-referentielijst-vs-codelijst
titel: Enumeratie, referentielijst of codelijst
bron: ["5.4", "5.4.1", "5.4.2", "5.4.3", "2.3.4.1", "2.3.4.3", "2.3.4.5"]
mim-versie: "1.2"
status: toelichtend
---

# Enumeratie, referentielijst of codelijst?

**In het kort.** Alle drie geven de toegestane waarden van een attribuutsoort. Een **enumeratie** staat vast in het model. Een **referentielijst** en een **codelijst** worden buiten het model beheerd en mogen veranderen zonder modelwijziging. Bij een referentielijst beschrijft het model de kenmerken van de items; bij een codelijst niet.

## Wat MIM zegt

> Als sprake is van dynamiek in de domeinwaarden wordt een **Referentielijst** of **Codelijst** gebruikt. Dit betreft de situaties waarin domeinwaarden kunnen veranderen en/of het aantal domeinwaarden kan toe- of afnemen.
>
> — MIM 1.2, §5.4.1 (normatief)

> Gebruik een `«Codelijst»` als in het informatiemodel de attributen, zoals bij een `«Referentielijst»`, niet relevant zijn en je voor de definitie alleen wilt verwijzen naar de externe waardelijst.
>
> — MIM 1.2, §5.4.3 (normatief)

## Vergelijking (eigen uitleg)

| | Enumeratie | Referentielijst | Codelijst |
|---|---|---|---|
| Waarden beheerd | in het model | buiten het model | buiten het model |
| Nieuwe waarde vraagt | modelwijziging | geen modelwijziging | geen modelwijziging |
| Structuur van een item in het model | n.v.t. (de waarde is een constante) | ja, met referentie-elementen | nee |
| Identificerend kenmerk in het model | n.v.t. (de waarde zelf) | ja, via Identificerend op een referentie-element | nee, buiten het model |
| Locatie (verplicht) | nee | ja | ja |
| Specifieke metagegevens | Code (per waarde) | Locatie | Locatie, Doelformaat, Waarde-item, Profielspecificatie |
| UML | Enumeration (geen stereotype) | «Referentielijst» op Datatype | «Codelijst» op Datatype |
| LD | `mim:Enumeratie` | `mim:Referentielijst` | `mim:Codelijst` |
| Paragrafen | §2.3.4.3, §5.4.1 | §2.3.4.1, §5.4.2 | §2.3.4.5, §5.4.3 |

## Beslisvragen (eigen uitleg)

1. Verandert de lijst niet of nauwelijks, en mag een nieuwe waarde een nieuwe modelversie betekenen? → enumeratie.
2. Moet het model vastleggen welke kenmerken een item heeft (code, naam, ingangsdatum)? → referentielijst.
3. Wil je alleen verwijzen naar een extern gepubliceerde lijst en zeggen welk veld de waarde is? → codelijst.
4. Koppel je met een ander model dat al een referentielijst gebruikt? Maak er dan geen enumeratie van (§5.4.2).

## Voorbeelden uit MIM

- **Enumeratie:** Naamgebruik met waarden ‘eigen’, ‘eigen, partner’ (§5.4.1).
- **Referentielijst:** Land, CultuurcodeOnbebouwd (§2.3.4.1, §5.4.2).
- **Codelijst:** MIM geeft geen concreet voorbeeld; wel dat de codelijst in gebruik "analoog aan een Enumeratie" is (§2.3.4.5).

## Let op

- MIM raadt een waarde als "onbekend" in een eigen enumeratie af; gebruik Mogelijk geen waarde (§5.11).
- Modelleer elke waardelijst bij voorkeur apart, met eigen naam en locatie (§5.4.2).

## Zie ook

- `modelelementen/enumeratie.md`, `modelelementen/referentielijst.md`, `modelelementen/codelijst.md`, `onderwerpen/waardelijsten.md`
