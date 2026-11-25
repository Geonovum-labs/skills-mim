---
id: naamgeving
titel: Naamgeving en definities
bron: ["5.15", "5.15.1", "5.15.2", "5.15.3", "5.15.4", "5.15.5", "6.2", "2.4.3.1", "2.4.3.2"]
mim-versie: "1.2"
status: normatief
---

# Naamgeving

**In het kort.** Een conceptueel model gebruikt namen in natuurlijke taal ("Natuurlijk persoon"), een logisch model namen die systemen makkelijk verwerken ("NatuurlijkPersoon"). Objecttypen en datatypen hebben een unieke naam in het hele model; kenmerken alleen binnen hun objecttype. Verdere conventies kiest de organisatie zelf.

## Uniekheid van namen

> - Objecttypes hebben een unieke naam binnen het hele informatiemodel
> - Datatypen hebben een unieke naam binnen het informatiemodel
> - Kenmerken van een objecttype hebben een unieke naam binnen het objecttype (attribuutsoort, gegevensgroep, relatiesoort et cetera)
> - De naam van kenmerken van een objecttype hoeven niet uniek te zijn over objecttypen heen.
> - De naam van elementen van een datatype hoeven niet uniek te zijn over datatypen heen.
>
> — MIM 1.2, §5.15.1 (normatief)

## Twee alternatieven

| | Alternatief 1: natuurlijke taal (§5.15.3) | Alternatief 2: (ook) leesbaar door systemen (§5.15.4) |
|---|---|---|
| Kenmerken | letters, cijfers, spaties; koppeltekens en diakrieten mogen | letters en cijfers, geen spaties, geen diakrieten |
| Voorbeeld | ‘Natuurlijk persoon’, ‘naam’ | `NatuurlijkPersoon`, `naam` |
| Verplicht voor | conceptuele modellen | logische modellen |

> Regel: voor conceptuele informatiemodellen wordt altijd alternatief 1 gehanteerd.
>
> — MIM 1.2, §5.15.3 (normatief)

> Regel: voor logische informatiemodellen wordt altijd alternatief 2 gehanteerd.
>
> — MIM 1.2, §5.15.4 (normatief)

Bij alternatief 2 neem je ook een verwijzing naar het element in het conceptuele model op, bijvoorbeeld met een trace of via de alias (§5.15.4).

Eigen uitleg. Bij CamelCase noemt §5.15.4 eerst lowerCamelCase voor relatiesoorten, en daarna een hoofdletter aan het begin van namen van "relaties". Zie `bekende-onduidelijkheden.md`.

## Naam en alias

De **Alias** is de naam in natuurlijke taal als de naam zelf technisch is geschreven, bijvoorbeeld naam `OnroerendeZaak`, alias "Onroerende zaak". Niet andersom (§2.4.3.2). Bij enumeratiewaarden werkt Alias anders; zie `modelelementen/enumeratiewaarde.md`.

## Dezelfde URI, naam of definitie

> - Als de **URI** van twee of meer modelelementen EXACT hetzelfde is, dan wordt hiermee bedoeld dat het dezelfde modelelementen zijn.
>
> — MIM 1.2, §5.15.2 (normatief)

Gelijke definitie betekent dezelfde definitie; gelijke naam én definitie betekent hetzelfde kenmerk. Een andere naam of andere definitie betekent: niet hetzelfde (§5.15.2).

## Metamodelelementen en eigen conventies

Stereotypes en metagegevens volgen alternatief 1 met een hoofdletter, behalve als een internationale standaard het anders voorschrijft (bijvoorbeeld codeList) (§5.15.5). Eigen conventies leg je vast in de eigen extensie met de template uit bijlage §6.2.

## Zie ook

- `onderwerpen/begrippen-en-definities.md`, `onderwerpen/extensies.md`
- Letterlijke tekst: `python3 scripts/mim.py paragraaf 5.15 --met-sub`
