---
id: data-element
titel: Data-element
metaclass: Data-element
bron: ["2.3.5.4", "3.2.4.3", "4.3.4.3", "6.4.6.4", "2.3.1.2"]
mim-versie: "1.2"
status: normatief
---

# Data-element

**In het kort.** Een data-element is een onderdeel van een gestructureerd datatype, zoals "som" en "valuta" in Bedrag. Het is geen kenmerk van een object, maar een stukje van de vorm van één waarde.

## 1. Definitie

> Een onderdeel/element van een Gestructureerd datatype die als type een datatype heeft.
>
> — MIM 1.2, §2.3.5.4 (normatief)

## 2. Uitleg

> Het data-element is een eigenschap van een Gestructureerd datatype en beschrijft de structuur van een gegeven. Het is niet een eigenschap van een object en niet hetzelfde als een attribuutsoort.
>
> — MIM 1.2, §2.3.5.4 (normatief)

Eigen uitleg. Omdat een data-element maar een deel van een waarde is, is historie bijhouden per data-element meestal niet zinvol (§2.3.1.2). Een data-element kan wel mogelijk geen waarde hebben, bijvoorbeeld de dag in een datum mogelijk onvolledig (§5.11).

## 3. Uitdrukking in UML en Linked Data

| | UML | Linked Data |
|---|---|---|
| Uitdrukking | stereotype «Data-element» op een (UML) Property; in EA: Attribute (§3.1.2) | `mim:DataElement` (§4.2.2), gekoppeld via `mim:dataElement` |
| Metagegevens | §3.2.4.3 | §4.3.4.3 |
| Transformatie naar RDFS/OWL/SHACL | | `owl:ObjectProperty` of `owl:DatatypeProperty`, plus `sh:PropertyShape` (§6.4.4.1, §6.4.6.4) |

## 4. Metagegevens en bindingen

Lees de tabel zoals beschreven in `metagegevens.md` (paragraaf "Zo lees je de tabellen").

<!-- BEGIN GEGENEREERD: metagegevens data-element -->
| Metagegeven | Betekenis | UML | LD | Verplicht | Verschil UML/LD |
|---|---|---|---|---|---|
| Identificatie | §2.4.2.2 | `1` (§3.2.4.3) | `1` (§4.3.4.3) | verplicht |  |
| Naam | §2.4.3.1 | `1` (§3.2.4.3) | `1` (§4.3.4.3) | verplicht |  |
| Alias | §2.4.3.2 | `0..1` (§3.2.4.3) | `0..1` (§4.3.4.3) | optioneel |  |
| Herkomst | §2.4.3.4 | `0..1` (§3.2.4.3) | - | optioneel | ja |
| Begrip | §2.4.3.3 | `0..*` (§3.2.4.3) | `0..*` (§4.3.4.3) | optioneel |  |
| Definitie | §2.4.3.5 | `0..1` (§3.2.4.3) | `1` (§4.3.4.3) | afwijkend tussen UML en LD | ja |
| Herkomst definitie | §2.4.3.6 | `0..1` (§3.2.4.3) | - | optioneel | ja |
| Toelichting | §2.4.3.7 | `0..1` (§3.2.4.3) | `0..1` (§4.3.4.3) | optioneel |  |
| Datum opname | §2.4.3.8 | `1` (§3.2.4.3) | `1` (§4.3.4.3) | verplicht |  |
| Lengte | §2.4.3.29 | `0..1` (§3.2.4.3) | `0..1` (§4.3.4.3) | optioneel |  |
| Patroon | §2.4.3.30 | `0..1` (§3.2.4.3) | `0..1` (§4.3.4.3) | optioneel |  |
| Formeel patroon | §2.4.3.31 | `0..1` (§3.2.4.3) | `0..1` (§4.3.4.3) | optioneel |  |
| Kardinaliteit | §2.4.3.14 | `1` (§3.2.4.3) | `1` (§4.3.4.3) | verplicht |  |
| Minimumwaarde inclusief | §2.4.3.37 | `0..1` (§3.2.4.3) | `0..1` (§4.3.4.3) | optioneel |  |
| Minimumwaarde exclusief | §2.4.3.38 | `0..1` (§3.2.4.3) | `0..1` (§4.3.4.3) | optioneel |  |
| Maximumwaarde inclusief | §2.4.3.39 | `0..1` (§3.2.4.3) | `0..1` (§4.3.4.3) | optioneel |  |
| Maximumwaarde exclusief | §2.4.3.40 | `0..1` (§3.2.4.3) | `0..1` (§4.3.4.3) | optioneel |  |
| Type (heeft datatype) | §2.4.3.28 / §2.4.4.5 | `1` (§3.2.4.3) | `1` (§4.3.4.3) | verplicht |  |
| heeft constraint | §2.4.4.17 | `0..*` (§3.2.4.3) | `0..*` (§4.3.4.3) | optioneel |  |
| Begripsterm | - | - | `0..*` (§4.3.4.3) | optioneel | ja |
<!-- EINDE GEGENEREERD -->

## 5. Voorbeeld en tegenvoorbeeld

**Voorbeeld uit MIM.** Objectnummering bestaat uit de data-elementen Gemeentecode (AN, lengte 4), Objecttypecode (AN, lengte 2) en Nummer (AN, lengte 10) (§5.1.4.1).

**Tegenvoorbeeld (eigen voorbeeld).** "voornaam" en "achternaam" van een persoon zijn geen data-elementen maar attribuutsoorten (eventueel in een gegevensgroeptype Naam): elk heeft eigen betekenis voor het object.

## 6. Wordt vaak verward met

- **Attribuutsoort.** Zie de vergelijking in `onderscheidingen/gegevensgroep-vs-gestructureerd-datatype.md`.

## Zie ook

- `modelelementen/gestructureerd-datatype.md`
- Letterlijke tekst: `python3 scripts/mim.py paragraaf 2.3.5.4`
