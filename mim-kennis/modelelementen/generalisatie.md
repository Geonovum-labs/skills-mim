---
id: generalisatie
titel: Generalisatie
metaclass: Generalisatie
bron: ["2.3.3.1", "3.2.2.5", "3.2.2.6", "4.3.2.5", "4.3.2.6", "6.4.5.5", "2.4.3.41", "5.1.2"]
mim-versie: "1.2"
status: normatief
---

# Generalisatie

**In het kort.** Een generalisatie legt vast dat het ene modelelement een specifiekere soort is van het andere en daarom zijn eigenschappen overerft, zoals Docent is een soort Persoon. In MIM kan dat alleen tussen objecttypen en tussen datatypen.

## 1. Definitie

> De typering van het hiërarchische verband tussen een meer generiek en een meer specifiek modelelement van hetzelfde soort, waarbij het meer specifieke modelelement eigenschappen van het meer generieke modelelement overerft. Dit verband is alleen gedefinieerd voor objecttypen en datatypen.
>
> — MIM 1.2, §2.3.3.1 (normatief)

## 2. Uitleg

MIM onderscheidt twee soorten generalisatie, met elk een eigen metagegevenstabel.

**Tussen objecttypen.** Het subtype erft de eigenschappen van het supertype:

> Een generalisatierelatie geeft aan dat bepaalde eigenschappen van een objecttype (vaak attribuutsoorten en/of relatiesoorten) ook gelden voor de gerelateerde objecttypen, én dat deze qua semantiek, structuur en syntax gelijk zijn. We spreken dan van een supertype met subtypen.
>
> — MIM 1.2, §2.3.3.1 (normatief)

Meervoudige overerving mag: een subtype kan meer supertypen hebben (§2.3.3.1). Voor logische modellen is daarom het metagegeven **Mixin** toegevoegd: `Mixin = Ja` betekent dat de supertype-klasse niet in de implementatie terugkomt, maar haar eigenschappen wel naar het subtype gaan (§2.4.3.41). Mixin geldt alleen voor generalisaties tussen objecttypen en alleen op niveau 3.

**Tussen datatypen.** Het specifiekere datatype is een beperking van het generiekere:

> Het meer specifieke datatype brengt een verbijzondering aan in de vorm van een meer restrictieve definitie, of een meer restrictief patroon/formeel patroon.
>
> — MIM 1.2, §2.3.3.1 (normatief)

Eigen uitleg. Het soort modelelement verandert niet door generalisatie: een zelfgedefinieerd primitief datatype generaliseert naar een primitief datatype, een gestructureerd datatype naar een gestructureerd datatype (§5.1.2).

**Wat erft wel en wat niet?** Eigenschappen (attribuutsoorten, relatiesoorten) erven over. Metagegevens van het modelelement zelf erven niet over (§2.4.3, inleiding). De kardinaliteit van een generalisatie is altijd 1..1 en hoeft nooit te worden aangegeven (§2.4.3.14).

**Metagegevens erven niet over** is iets anders dan **overerving in UML**. MIM neemt geen semantiek over van UML (§1.8); wat overerft staat in de MIM-tekst hierboven.

## 3. Uitdrukking in UML en Linked Data

| | UML | Linked Data |
|---|---|---|
| Uitdrukking | stereotype «Generalisatie» op een (UML) Generalization; in EA: Generalization (§3.1.1) | `mim:Generalisatie` met `mim:subtype` en `mim:supertype` (§4.2.1, §4.3.2.5) |
| Metagegevens | §3.2.2.5 (objecttypen), §3.2.2.6 (datatypen) | §4.3.2.5, §4.3.2.6 |
| Transformatie naar RDFS/OWL/SHACL | | `rdfs:subClassOf` (§6.4.5.5) |

## 4. Metagegevens en bindingen

Lees de tabel zoals beschreven in `metagegevens.md` (paragraaf "Zo lees je de tabellen").

<!-- BEGIN GEGENEREERD: metagegevens generalisatie -->
**Variant: tussen objecttypen**

| Metagegeven | Betekenis | UML | LD | Verplicht | Verschil UML/LD |
|---|---|---|---|---|---|
| Identificatie | §2.4.2.2 | `1` (§3.2.2.5) | `1` (§4.3.2.5) | verplicht |  |
| Subtype | - | `1` (§3.2.2.5) | `1` (§4.3.2.5) | verplicht |  |
| verwijst naar supertype | §2.4.4.4 | `1` (§3.2.2.5) | `1` (§4.3.2.5) | verplicht |  |
| Datum opname | §2.4.3.8 | `1` (§3.2.2.5) | `1` (§4.3.2.5) | verplicht |  |
| heeft constraint | §2.4.4.17 | `0..*` (§3.2.2.5) | - | optioneel | ja |
| Mixin | §2.4.3.41 | `1` (§3.2.2.5) | `1` (§4.3.2.5) | verplicht |  |

**Variant: tussen datatypen**

| Metagegeven | Betekenis | UML | LD | Verplicht | Verschil UML/LD |
|---|---|---|---|---|---|
| Identificatie | §2.4.2.2 | `1` (§3.2.2.6) | `1` (§4.3.2.6) | verplicht |  |
| Subtype | - | `1` (§3.2.2.6) | `1` (§4.3.2.6) | verplicht |  |
| verwijst naar supertype | §2.4.4.4 | `1` (§3.2.2.6) | `1` (§4.3.2.6) | verplicht |  |
| Datum opname | §2.4.3.8 | `1` (§3.2.2.6) | - | verplicht | ja |
| heeft constraint | §2.4.4.17 | `0..*` (§3.2.2.6) | - | optioneel | ja |
<!-- EINDE GEGENEREERD -->

Eigen uitleg bij de tabel: in de LD-tabellen (§4.3.2.5, §4.3.2.6) verwijzen de aspecten Subtype en Supertype naar de eigenschap `mim:definitie`. De vocabulaire kent `mim:subtype` en `mim:supertype` (§4.3, overzichtstabel), en de transformatie gebruikt die ook (§6.4.4.2). Dit is een fout in de tabel; zie `bekende-onduidelijkheden.md`.

## 5. Voorbeeld en tegenvoorbeeld

**Voorbeeld uit MIM (objecttypen).** Docent en Leerling zijn specialisaties van Persoon. Als een persoon altijd óf docent óf leerling is, is Persoon een abstract objecttype (§5.5.1).

**Voorbeeld uit MIM (datatypen).** Een zelfgedefinieerd datatype `Postcode` of `NietNegatiefGetal` op basis van `CharacterString` of `Integer` (§2.3.3.1).

**Tegenvoorbeeld (eigen voorbeeld).** Een generalisatie van een gegevensgroeptype naar een ander gegevensgroeptype valt buiten de definitie, die alleen objecttypen en datatypen noemt. Let op: de UML-tabel van het gegevensgroeptype (§3.2.1.4) noemt wel "verwijst naar supertype". Meld dat verschil.

## 6. Wordt vaak verward met

- **Relatiesoort.** Een generalisatie is geen relatie tussen objecten: er is geen "Jan heeft-als-supertype Persoon". Jan ís een persoon. Generalisatie heeft daarom ook geen relatierol (§2.3.3.5).
- **Indicatie classificerend.** Een attribuutsoort als "type gebouw" kan subtypen aanduiden zonder generalisatie (§2.4.3.18).

## Zie ook

- `onderwerpen/abstracte-objecttypen.md`
- Letterlijke tekst: `python3 scripts/mim.py paragraaf 2.3.3.1`
