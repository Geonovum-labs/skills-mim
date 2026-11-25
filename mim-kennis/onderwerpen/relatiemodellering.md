---
id: relatiemodellering
titel: Relatiesoort leidend of relatierol leidend
bron: ["1.11", "2.4.1.3", "3.2.2", "3.2.2.1", "3.2.2.2", "3.2.2.3", "3.2.2.4", "4.3.2.2"]
mim-versie: "1.2"
status: normatief
---

# Relatiesoort leidend of relatierol leidend

**In het kort.** Dit is de enige modelleerkeuze die MIM openlaat. Bij **relatiesoort leidend** heeft elke relatie een verplichte naam en definitie, en zijn rollen optioneel. Bij **relatierol leidend** is de rol aan de doelkant verplicht, met de metagegevens, en is de naam van de relatie optioneel. Het informatiemodel legt de keuze vast in het metagegeven Relatiemodelleringstype.

## Wat MIM zegt

> In het MIM is op één punt sprake van een keuze tussen twee modelleringsalternatieven, waarvan de modelleur van een informatiemodel één van beide alternatieven kiest. Welke toegepast is wordt aangegeven.
>
> — MIM 1.2, §1.11 (normatief)

> Dit kan zijn `"Relatiesoort leidend"` of `"Relatierol leidend"`. Dit betreft de keuze die je maakt voor het in 1.11 Alternatieven gekozen alternatief. Er moet een keuze gemaakt worden.
>
> — MIM 1.2, §2.4.1.3 (normatief)

De keuze geldt voor relatiesoort en relatierol, en in het verlengde daarvan ook voor de externe koppeling (§2.4.1.3).

## Wat verschilt (eigen samenvatting van §3.2.2 en de tabellen)

| | Relatiesoort leidend (alt 1) | Relatierol leidend (alt 2) |
|---|---|---|
| Naam en definitie van de relatiesoort | verplicht | optioneel volgens §3.2.2 (de UML-tabel §3.2.2.2 zegt 1, de LD-tabel 0..1) |
| Relatierol | optioneel; als de doelrol er is, zijn de metagegevens verplicht | doelrol verplicht, met metagegevens |
| Kardinaliteit, historie, authentiek, mogelijk geen waarde | op de relatiesoort (§3.2.2.1) | op de relatierol doel (§3.2.2.4) |
| Bron, doel, unidirectioneel, aggregatietype | op de relatiesoort (§3.2.2.1) | niet in de tabel van §3.2.2.2 |
| LD | `mim:Relatiesoort` met alle kenmerk-metagegevens (§4.3.2.1) | `mim:Relatiesoort` met `mim:relatierol` `1..2` (§4.3.2.2) |
| Waarde in LD | `mim:RelatiesoortLeidend` | `mim:RelatierolLeidend` |

Vergelijk de tabellen zelf met `python3 scripts/mim.py metagegeven relatiesoort --variant "alt 1"` en `--variant "alt 2"`, of in `modelelementen/relatiesoort.md` en `modelelementen/relatierol.md`.

## Waar staat de keuze?

Het metagegeven Relatiemodelleringstype op het informatiemodel (§2.4.1.3). §3.2.2 zegt dat de keuze "in de eigen extensie" wordt aangegeven. Zie `bekende-onduidelijkheden.md`.

## Bij twijfel

MIM nodigt uit om vóór de keuze contact op te nemen met de beheerders van MIM (§1.11).

## Zie ook

- `modelelementen/relatiesoort.md`, `modelelementen/relatierol.md`
- Letterlijke tekst: `python3 scripts/mim.py paragraaf 3.2.2`
