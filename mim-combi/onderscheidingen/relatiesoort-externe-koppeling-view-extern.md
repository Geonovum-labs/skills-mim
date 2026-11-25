---
id: relatiesoort-externe-koppeling-view-extern
titel: Relatiesoort, externe koppeling, view en extern
bron: ["2.3.3.2", "2.3.3.4", "2.3.6", "2.3.6.3", "2.3.6.4", "5.12", "5.13"]
mim-versie: "1.2"
status: toelichtend
---

# Relatiesoort, externe koppeling, view of extern?

**In het kort.** Twee hiervan zijn relaties (relatiesoort, externe koppeling), twee zijn packages (view, extern). Een relatiesoort blijft binnen het eigen model. Een externe koppeling wijst naar een objecttype uit een ander model, dat in een view staat. Een extern package bevat elementen die een andere partij beheert en die ongewijzigd worden gebruikt, zoals NEN 3610-datatypen.

## Wat MIM zegt

> Deze stereotypes zijn alleen van toepassing binnen een informatiemodel in situaties waarbij het ene informatiemodel afhankelijk is van een andere informatiemodel.
>
> — MIM 1.2, §5.13 (normatief)

> Merk op dat er ook een relatie rechtstreeks naar de BRP gelegd had kunnen worden. Er is dan geen sprake van gegevens uit de BRP die overgenomen zijn in de eigen registratie. Er kan dan volstaan worden met alleen de unieke aanduiding van GeregistreerdPersoon. Dit is de BSN. Dit wordt niet gezien als een «externe koppeling» maar als een referentie.
>
> — MIM 1.2, §5.13 (niet-normatief, voorbeeld)

## Vergelijking (eigen uitleg)

| | Relatiesoort | Externe koppeling | View | Extern |
|---|---|---|---|---|
| Soort modelelement | relatie | relatie | package | package |
| Waar staat het doel? | in het eigen model | in een ander informatiemodel | binnen het eigen informatiemodel-package (§2.3.6) | buiten het eigen informatiemodel-package (§2.3.6) |
| Wie beheert de definities? | het eigen model | het andere model | het andere model; het eigen model kiest de relevante deelverzameling | een externe instantie; ongewijzigd gebruikt |
| Typisch gebruik | Persoon woont op Nummeraanduiding | Persoon (IMKAD) → GeregistreerdPersoon (view BRP) | view IMKAD-BRP | package NEN3610 met NEN3610ID |
| LD-transformatie | `owl:ObjectProperty` | `owl:ObjectProperty` | `owl:imports` | `owl:imports` |

## Beslisvragen (eigen uitleg)

1. Staat het doel-objecttype in het eigen model? → relatiesoort.
2. Neem je gegevens van een object uit een ander model over in het eigen model? → zet dat objecttype in een view en leg een externe koppeling.
3. Neem je alleen de unieke aanduiding over (bijvoorbeeld het BSN)? → een referentie; geen externe koppeling (§5.13).
4. Gebruik je elementen (vaak datatypen) van een andere beheerder ongewijzigd? → extern package (§5.12).

## Zie ook

- `modelelementen/relatiesoort.md`, `modelelementen/externe-koppeling.md`, `modelelementen/view.md`, `modelelementen/extern.md`
