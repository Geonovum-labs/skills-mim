---
id: attribuutsoort-vs-relatiesoort
titel: Attribuutsoort of relatiesoort
bron: ["2.3.2.2", "2.3.3.2", "2.3.1.2", "5.13"]
mim-versie: "1.2"
status: toelichtend
---

# Attribuutsoort of relatiesoort?

**In het kort.** Beide zijn kenmerken van een objecttype. Een attribuutsoort heeft een waarde van een datatype ("geboortedatum = 1-1-1970"). Een relatiesoort verwijst naar een ander object ("woont in → Pand 0123"), dat zelf een objecttype in het model is.

## Wat MIM zegt

> Objecten hebben eigenschappen die gemodelleerd kunnen worden met attribuutsoorten maar ook met relatiesoorten naar andere objecttypen.
>
> — MIM 1.2, §2.3.3.2 (normatief)

> Bijvoorbeeld, een attribuutsoort van het objecttype PERSOON zou kunnen zijn ‘Naam geregistreerd partner’ (naast de attribuutsoort ‘Naam’ van PERSOON). De naam van de geregistreerde partner komt evenwel ook beschikbaar met een relatiesoort van PERSOON naar PERSOON: “heeft geregistreerd partnerschap met”.
>
> — MIM 1.2, §2.3.3.2 (normatief)

> De modelelementen waarmee een getypeerde _eigenschap_ van een object gemodelleerd kan worden zijn: _attribuutsoort_, _relatiesoort_ en _externe koppeling_.
>
> — MIM 1.2, §2.3.1.2 (normatief)

## Vergelijking (eigen uitleg)

| | Attribuutsoort | Relatiesoort |
|---|---|---|
| Waarde is | een waarde van een datatype | een verwijzing naar een object van een objecttype |
| Type of doel | datatype (heeft datatype) | objecttype (Doel) |
| Eigen metagegevens | Lengte, Patroon, Eenheid, Indicatie classificerend, min/max | Bron, Doel, Unidirectioneel, Aggregatietype, Kardinaliteit relatie bron |
| Gedeelde metagegevens | Kardinaliteit, historie, Authentiek, Indicatie afleidbaar, Mogelijk geen waarde, Identificerend | idem |

## Beslisvragen (eigen uitleg)

1. Is het "ding" waar het kenmerk naar wijst zelf een onderwerp van gesprek in dit model, met eigen kenmerken? → relatiesoort.
2. Ligt het in een ander informatiemodel? → externe koppeling (en een view), of alleen een referentie met de unieke aanduiding (§5.13).
3. Komt de waarde uit een lijst waarvan de items geen onderwerp van gesprek zijn (zoals Land)? → attribuutsoort met als type een referentielijst of codelijst.
4. Anders → attribuutsoort.

## Zie ook

- `modelelementen/attribuutsoort.md`, `modelelementen/relatiesoort.md`
