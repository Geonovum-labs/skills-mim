---
id: objecttype
titel: Objecttype
metaclass: Objecttype
bron: ["2.3.2.1", "2.3.1.1", "3.2.1.1", "4.3.1.1", "6.4.5.1", "5.5"]
mim-versie: "1.2"
status: normatief
---

# Objecttype

**In het kort.** Een objecttype is de soort ding waarover een informatiemodel informatie vastlegt, zoals Persoon, Pand of Perceel. De afzonderlijke dingen (Jan, het pand op de hoek) zijn objecten; die staan niet in het model, het objecttype wel.

## 1. Definitie

> De typering van een groep objecten die binnen een domein relevant zijn en als gelijksoortig worden beschouwd.
>
> — MIM 1.2, §2.3.2.1 (normatief)

## 2. Uitleg

Eigen uitleg. Een objecttype hoort altijd bij een domein: wat in het ene domein een objecttype is, kan in een ander domein iets anders zijn. MIM geeft daar zelf een voorbeeld van:

> Jan, Piet en Marie zijn mensen die vanuit het Burgerzaken-domein beschouwd worden als objecten van het `«Objecttype»` `NatuurlijkPersoon`. In een ander domein, ‘de volksmond’, noemen we dit `Mens` wat ook een `«Objecttype»` is.
>
> — MIM 1.2, §2.3.2.1 (normatief)

Een objecttype beschrijft de werkelijkheid binnen het domein, niet de manier waarop gegevens in een registratie worden opgeslagen:

> Objecttypen zijn een abstractie van de werkelijkheid oftewel we beogen hiermee de werkelijkheid zo getrouw mogelijk te beschrijven, binnen de context van het domein. Dit staat geheel los van het vastleggen van gegevens over objecten van een type in een registratie.
>
> — MIM 1.2, §2.3.2.1 (normatief)

Een objecttype kan abstract zijn. Dan bestaan er geen objecten die alleen van dat type zijn; elk object hoort bij een concreet subtype. Zie `onderwerpen/abstracte-objecttypen.md` en het metagegeven Indicatie abstract object in `metagegevens.md`.

> De objecten die in het beschouwde domein onderkend worden zijn zelf nooit abstract. Ze behoren altijd tot een concreet `«Objecttype»`, en niet tot een abstract `«Objecttype»`.
>
> — MIM 1.2, §2.3.2.1 (normatief)

Kenmerken van een objecttype worden gemodelleerd met attribuutsoorten, gegevensgroepen, relatiesoorten en externe koppelingen. Een objecttype is nooit rechtstreeks met een ander objecttype verbonden; daarvoor is er altijd een relatiesoort:

> Een `Objecttype` kan dus *niet* rechtstreeks verbonden worden met een ander `Objecttype`.
>
> — MIM 1.2, §2.2.2 (normatief)

## 3. Uitdrukking in UML en Linked Data

| | UML | Linked Data |
|---|---|---|
| Uitdrukking | stereotype «Objecttype» op een (UML) Class; in EA: Class (§3.1.1) | `mim:Objecttype` (§4.2.1) |
| Metagegevens | §3.2.1.1 | §4.3.1.1 |
| Transformatie naar RDFS/OWL/SHACL | | `owl:Class` en `sh:NodeShape` (§6.4.4.1, §6.4.5.1) |

De UML-Class is alleen de notatie. De betekenis komt uit de MIM-definitie hierboven, niet uit UML (zie `uitdrukkingen/uml.md`).

## 4. Metagegevens en bindingen

Lees de tabel zoals beschreven in `metagegevens.md` (paragraaf "Zo lees je de tabellen").

<!-- BEGIN GEGENEREERD: metagegevens objecttype -->
| Metagegeven | Betekenis | UML | LD | Verplicht | Verschil UML/LD |
|---|---|---|---|---|---|
| Identificatie | §2.4.2.2 | `1` (§3.2.1.1) | `1` (§4.3.1.1) | verplicht |  |
| Naam | §2.4.3.1 | `1` (§3.2.1.1) | `1` (§4.3.1.1) | verplicht |  |
| Alias | §2.4.3.2 | `0..1` (§3.2.1.1) | `0..1` (§4.3.1.1) | optioneel |  |
| Herkomst | §2.4.3.4 | `1` (§3.2.1.1) | `1` (§4.3.1.1) | verplicht |  |
| Begrip | §2.4.3.3 | `0..*` (§3.2.1.1) | `0..*` (§4.3.1.1) | optioneel |  |
| Definitie | §2.4.3.5 | `1` (§3.2.1.1) | `1` (§4.3.1.1) | verplicht |  |
| Herkomst definitie | §2.4.3.6 | `1` (§3.2.1.1) | `1` (§4.3.1.1) | verplicht |  |
| Toelichting | §2.4.3.7 | `0..1` (§3.2.1.1) | `0..1` (§4.3.1.1) | optioneel |  |
| Datum opname | §2.4.3.8 | `1` (§3.2.1.1) | `1` (§4.3.1.1) | verplicht |  |
| Unieke aanduiding | - | `1` (§3.2.1.1) | - | verplicht | ja |
| Populatie | §2.4.3.34 | `0..1` (§3.2.1.1) | `0..1` (§4.3.1.1) | optioneel |  |
| Kwaliteit | §2.4.3.35 | `0..1` (§3.2.1.1) | `0..1` (§4.3.1.1) | optioneel |  |
| Indicatie abstract object | §2.4.3.33 | `1` (§3.2.1.1) | `1` (§4.3.1.1) | verplicht |  |
| heeft attribuut | §2.4.4.1 | `0..*` (§3.2.1.1) | `0..*` (§4.3.1.1) | optioneel |  |
| heeft gegevensgroep | §2.4.4.2 | `0..*` (§3.2.1.1) | `0..*` (§4.3.1.1) | optioneel |  |
| heeft relatiesoort | §2.4.4.6 | `0..*` (§3.2.1.1) | - | optioneel | ja |
| heeft externe koppeling | §2.4.4.7 | `0..*` (§3.2.1.1) | - | optioneel | ja |
| verwijst naar supertype | §2.4.4.4 | `0..*` (§3.2.1.1) | - | optioneel | ja |
| heeft constraint | §2.4.4.17 | `0..*` (§3.2.1.1) | `0..*` (§4.3.1.1) | optioneel |  |
| Begripsterm | - | - | `0..*` (§4.3.1.1) | optioneel | ja |
<!-- EINDE GEGENEREERD -->

Eigen uitleg bij de tabel:

- **Unieke aanduiding** staat alleen in de UML-tabel. MIM zegt daar dat dit metagegeven afleidbaar is uit de attribuutsoorten en relaties die identificerend zijn, en dus niet apart hoeft te worden gespecificeerd (§3.2.1.1).
- **Indicatie abstract object** heeft kardinaliteit 1, maar ook een default (`Nee`, §2.4.5.2). Een model hoeft het dus alleen in te vullen als het objecttype abstract is.
- In Linked Data hangen relaties niet aan het objecttype maar aan de relatiesoort (via `mim:bron`). Daarom staan "heeft relatiesoort" en "heeft externe koppeling" niet in de LD-tabel. Dat is een verschil in uitdrukking, geen ander metamodel.

## 5. Voorbeeld en tegenvoorbeeld

**Voorbeeld uit MIM.**

> in de Basisregistratie Kadaster (BRK) wordt een `Perceel` gemodelleerd als een `«Objecttype»`. De `grens` van een perceel wordt gemodelleerd als een `«Attribuutsoort»`.
>
> — MIM 1.2, §2 (normatief)

**Tegenvoorbeeld (eigen voorbeeld).** De motor van een schip is in de BRK géén objecttype: niemand kan eigenaar zijn van alleen de motor, dus de motor is een kenmerk van het schip en wordt een gegevensgroep. In het model van een motorfabriek kan Motor wél een objecttype zijn. MIM gebruikt dit voorbeeld zelf in §2.3.2.4.

## 6. Wordt vaak verward met

- **Object.** Een object is een ding in de werkelijkheid en geen modelelement; het objecttype is wel een modelelement. Zie `onderscheidingen/object-objecttype-gegeven.md`.
- **Gegevensgroeptype.** Ook een groep kenmerken, maar zonder eigen bestaan: het hoort onlosmakelijk bij een objecttype. Zie `modelelementen/gegevensgroeptype.md`.
- **Relatieklasse.** Als dezelfde gegevens voor meer relaties tegelijk gelden, wordt een "relatie met gegevens" toch een objecttype. Zie `onderscheidingen/relatieklasse-vs-objecttype.md`.
- **Referentielijst.** Dingen waarover je wel gegevens wilt kennen maar die in het model geen onderwerp van gesprek zijn (zoals Land), komen in een referentielijst, niet in een objecttype. Zie `modelelementen/referentielijst.md`.

## Zie ook

- `modelelementen/attribuutsoort.md`, `modelelementen/relatiesoort.md`, `modelelementen/generalisatie.md`
- `onderwerpen/abstracte-objecttypen.md`
- Letterlijke tekst: `python3 scripts/mim.py paragraaf 2.3.2.1`
