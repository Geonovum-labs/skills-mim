---
id: attribuutsoort
titel: Attribuutsoort
metaclass: Attribuutsoort
bron: ["2.3.2.2", "3.2.1.2", "4.3.1.2", "6.4.5.2", "5.1", "5.9", "5.11"]
mim-versie: "1.2"
status: normatief
---

# Attribuutsoort

**In het kort.** Een attribuutsoort is een kenmerk van een objecttype waarvoor gegevens worden bijgehouden, zoals de naam of de geboortedatum van een persoon. De waarde zelf ("Jan", "1-1-1970") staat niet in het model; de attribuutsoort beschrijft wat die waarde betekent en aan welk datatype ze moet voldoen.

## 1. Definitie

> De typering van gelijksoortige gegevens die voor een objecttype van toepassing is.
>
> — MIM 1.2, §2.3.2.2 (normatief)

## 2. Uitleg

> Een `«Attribuutsoort»` is de metaklasse waarmee kenmerken van een `«Objecttype»` worden vastgelegd. Het zijn de kenmerken waarvoor gegevens worden bijgehouden.
>
> — MIM 1.2, §2.3.2.2 (normatief)

Eigen uitleg. Een attribuutsoort heeft altijd betekenis voor het objecttype: als je het datatype weglaat, moet duidelijk blijven wat het kenmerk betekent (§2.1, uitgangspunt 5). De structuur van de waarde staat in het datatype; de betekenis in de attribuutsoort.

Een objecttype kan nul, één of meer attribuutsoorten hebben. Ook gegevensgroeptypen en relatieklassen kunnen attribuutsoorten hebben (binding "heeft attribuut", §2.4.4.1).

Let op het woordgebruik: "kenmerk" of "eigenschap" is breder dan attribuutsoort.

> Attribuutsoorten worden ook wel _kenmerken_ of _eigenschappen_ genoemd. Dit zijn het ook, maar ook andere modelelementen vallen onder deze omschrijving. Zo is een `«Relatiesoort»` ook een kenmerk of eigenschap.
>
> — MIM 1.2, §2.3.2.2 (normatief)

Belangrijke metagegevens bij een attribuutsoort, elk met een eigen onderwerpbestand:

- kardinaliteit en mogelijk geen waarde: `onderwerpen/mogelijk-geen-waarde.md`;
- heeft tijdlijn geldigheid en heeft tijdlijn registratie: `onderwerpen/historie.md`;
- authentiek: `metagegevens.md`;
- indicatie afleidbaar: §5.9, in UML via `isDerived`;
- identificerend: in UML `isId = true` (noot bij §3.2).

## 3. Uitdrukking in UML en Linked Data

| | UML | Linked Data |
|---|---|---|
| Uitdrukking | stereotype «Attribuutsoort» op een (UML) Property; in EA: Attribute (§3.1.1) | `mim:Attribuutsoort` (§4.2.1) |
| Metagegevens | §3.2.1.2 | §4.3.1.2 |
| Transformatie naar RDFS/OWL/SHACL | | `owl:ObjectProperty` of `owl:DatatypeProperty`, plus `sh:PropertyShape` (§6.4.4.1, §6.4.5.2) |

## 4. Metagegevens en bindingen

Lees de tabel zoals beschreven in `metagegevens.md` (paragraaf "Zo lees je de tabellen").

<!-- BEGIN GEGENEREERD: metagegevens attribuutsoort -->
| Metagegeven | Betekenis | UML | LD | Verplicht | Verschil UML/LD |
|---|---|---|---|---|---|
| Identificatie | §2.4.2.2 | `1` (§3.2.1.2) | `1` (§4.3.1.2) | verplicht |  |
| Naam | §2.4.3.1 | `1` (§3.2.1.2) | `1` (§4.3.1.2) | verplicht |  |
| Alias | §2.4.3.2 | `0..1` (§3.2.1.2) | `0..1` (§4.3.1.2) | optioneel |  |
| Herkomst | §2.4.3.4 | `1` (§3.2.1.2) | `1` (§4.3.1.2) | verplicht |  |
| Begrip | §2.4.3.3 | `0..*` (§3.2.1.2) | `0..*` (§4.3.1.2) | optioneel |  |
| Definitie | §2.4.3.5 | `1` (§3.2.1.2) | `1` (§4.3.1.2) | verplicht |  |
| Herkomst definitie | §2.4.3.6 | `1` (§3.2.1.2) | `1` (§4.3.1.2) | verplicht |  |
| Toelichting | §2.4.3.7 | `0..1` (§3.2.1.2) | `0..1` (§4.3.1.2) | optioneel |  |
| Datum opname | §2.4.3.8 | `1` (§3.2.1.2) | `1` (§4.3.1.2) | verplicht |  |
| Lengte | §2.4.3.29 | `0..1` (§3.2.1.2) | `0..1` (§4.3.1.2) | optioneel |  |
| Patroon | §2.4.3.30 | `0..1` (§3.2.1.2) | `0..1` (§4.3.1.2) | optioneel |  |
| Formeel patroon | §2.4.3.31 | `0..1` (§3.2.1.2) | `0..1` (§4.3.1.2) | optioneel |  |
| heeft tijdlijn geldigheid | §2.4.3.10 | `1` (§3.2.1.2) | `1` (§4.3.1.2) | verplicht |  |
| Indicatie materiële historie | §2.4.3.11 | `1` (§3.2.1.2) | `1` (§4.3.1.2) | verplicht |  |
| heeft tijdlijn registratie | §2.4.3.12 | `1` (§3.2.1.2) | `1` (§4.3.1.2) | verplicht |  |
| Indicatie formele historie | §2.4.3.13 | `1` (§3.2.1.2) | `1` (§4.3.1.2) | verplicht |  |
| Kardinaliteit | §2.4.3.14 | `1` (§3.2.1.2) | `1` (§4.3.1.2) | verplicht |  |
| Authentiek | §2.4.3.16 | `1` (§3.2.1.2) | `1` (§4.3.1.2) | verplicht |  |
| Indicatie afleidbaar | §2.4.3.17 | `1` (§3.2.1.2) | `1` (§4.3.1.2) | verplicht |  |
| Indicatie classificerend | §2.4.3.18 | `1` (§3.2.1.2) | `1` (§4.3.1.2) | verplicht |  |
| Mogelijk geen waarde | §2.4.3.19 | `1` (§3.2.1.2) | `1` (§4.3.1.2) | verplicht |  |
| Identificerend | §2.4.3.9 | `0..1` (§3.2.1.2) | `0..1` (§4.3.1.2) | optioneel |  |
| Minimumwaarde inclusief | §2.4.3.37 | `0..1` (§3.2.1.2) | `0..1` (§4.3.1.2) | optioneel |  |
| Minimumwaarde exclusief | §2.4.3.38 | `0..1` (§3.2.1.2) | `0..1` (§4.3.1.2) | optioneel |  |
| Maximumwaarde inclusief | §2.4.3.39 | `0..1` (§3.2.1.2) | `0..1` (§4.3.1.2) | optioneel |  |
| Maximumwaarde exclusief | §2.4.3.40 | `0..1` (§3.2.1.2) | `0..1` (§4.3.1.2) | optioneel |  |
| Eenheid | §2.4.3.36 | `0..1` (§3.2.1.2) | `0..1` (§4.3.1.2) | optioneel |  |
| Type (heeft datatype) | §2.4.3.28 / §2.4.4.5 | `1` (§3.2.1.2) | `1` (§4.3.1.2) | verplicht |  |
| heeft constraint | §2.4.4.17 | `0..*` (§3.2.1.2) | `0..*` (§4.3.1.2) | optioneel |  |
| Begripsterm | - | - | `0..*` (§4.3.1.2) | optioneel | ja |
<!-- EINDE GEGENEREERD -->

Eigen uitleg bij de tabel:

- **Kardinaliteit** heeft voor een attribuutsoort de default `1` (§2.4.5.2).
- **Indicatie classificerend** wordt in de LD-tabel (§4.3.1.2) gekoppeld aan de eigenschap `mim:indicatieAfleidbaar`. In de vocabulaire bestaat `mim:indicatieClassificerend` wel. Zie `bekende-onduidelijkheden.md`.
- **Eenheid** en de vier **minimum-/maximumwaarden** zijn nieuw in MIM 1.2 (zie `versies.md`).

## 5. Voorbeeld en tegenvoorbeeld

**Voorbeeld uit MIM.**

> De gegevens `"Jan"` en `"Katrien"` worden als gelijksoortig gezien en worden daarom ondergebracht in `«Attribuutsoort»` `naam`.
>
> — MIM 1.2, §2.3.2.2 (normatief)

**Tegenvoorbeeld uit MIM.** "Naam geregistreerd partner" kan een attribuutsoort van Persoon zijn, maar dezelfde informatie is ook beschikbaar via een relatiesoort van Persoon naar Persoon (§2.3.3.2). Gaat het om een ander object met eigen gegevens, dan is een relatiesoort de passende keuze. Zie `onderscheidingen/attribuutsoort-vs-relatiesoort.md`.

**Tegenvoorbeeld (eigen voorbeeld).** Een "bedrag" met som en valuta is géén twee attribuutsoorten "som" en "valuta" van het objecttype: som zonder valuta zegt niets. Het is één attribuutsoort met een gestructureerd datatype Bedrag (§2.3.5.3).

## 6. Wordt vaak verward met

- **Data-element.** Een data-element is een onderdeel van een gestructureerd datatype en géén kenmerk van een object. Zie `modelelementen/data-element.md`.
- **Gegevensgroep.** Een gegevensgroep is een kenmerk dat uit meerdere attribuutsoorten bestaat; die attribuutsoorten blijven elk een kenmerk van het object. Zie `onderscheidingen/gegevensgroep-vs-gestructureerd-datatype.md`.
- **Relatiesoort.** Zie `onderscheidingen/attribuutsoort-vs-relatiesoort.md`.
- **Referentie-element.** Een referentie-element is een eigenschap van een item in een referentielijst, niet van een objecttype.

## Zie ook

- `modelelementen/datatype.md`, `onderwerpen/datatypen.md`
- `modelelementen/keuze.md` (keuze tussen attribuutsoorten, use case 2 en 3)
- Letterlijke tekst: `python3 scripts/mim.py paragraaf 2.3.2.2`
