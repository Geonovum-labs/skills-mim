---
id: referentie-element
titel: Referentie-element
metaclass: Referentie-element
bron: ["2.3.4.2", "3.2.3.5", "4.3.3.2", "6.4.5.11"]
mim-versie: "1.2"
status: normatief
---

# Referentie-element

**In het kort.** Een referentie-element is één kenmerk van de items in een referentielijst, bijvoorbeeld de landcode of de landnaam in een lijst van landen.

## 1. Definitie

> Een eigenschap van een object in een referentielijst in de vorm van een gegeven.
>
> — MIM 1.2, §2.3.4.2 (normatief)

## 2. Uitleg

> Een referentie-element kan uniek zijn, zoals een code, en is dan op zichzelf geschikt om gebruikt te worden als referentie (zoals bedoeld in de definitie van Referentielijst). Bij het referentie-element kan een definitie en toelichting worden opgenomen, die aangeven hoe de externe waardelijst in het eigen informatiemodel gebruikt wordt.
>
> — MIM 1.2, §2.3.4.2 (normatief)

Eigen uitleg. Een referentie-element lijkt op een attribuutsoort (het heeft een datatype, een kardinaliteit, een lengte), maar het is een kenmerk van een item in de lijst, niet van een objecttype in het model. Het metagegeven Identificerend geeft aan welk referentie-element een item uniek aanduidt (§2.4.3.9).

## 3. Uitdrukking in UML en Linked Data

| | UML | Linked Data |
|---|---|---|
| Uitdrukking | stereotype «Referentie-element» op een (UML) Property; in EA: Attribute (§3.1.2) | `mim:ReferentieElement` (§4.2.2) |
| Metagegevens | §3.2.3.5 | §4.3.3.2 |
| Transformatie naar RDFS/OWL/SHACL | | `owl:Class` en `sh:NodeShape` volgens de tabel in §6.4.4.1; zie §6.4.5.11 |

## 4. Metagegevens en bindingen

Lees de tabel zoals beschreven in `metagegevens.md` (paragraaf "Zo lees je de tabellen").

<!-- BEGIN GEGENEREERD: metagegevens referentie-element -->
| Metagegeven | Betekenis | UML | LD | Verplicht | Verschil UML/LD |
|---|---|---|---|---|---|
| Identificatie | §2.4.2.2 | `1` (§3.2.3.5) | `1` (§4.3.3.2) | verplicht |  |
| Naam | §2.4.3.1 | `1` (§3.2.3.5) | `1` (§4.3.3.2) | verplicht |  |
| Alias | §2.4.3.2 | `0..1` (§3.2.3.5) | `0..1` (§4.3.3.2) | optioneel |  |
| Herkomst | §2.4.3.4 | `1` (§3.2.3.5) | - | verplicht | ja |
| Begrip | §2.4.3.3 | `0..*` (§3.2.3.5) | `0..*` (§4.3.3.2) | optioneel |  |
| Definitie | §2.4.3.5 | `1` (§3.2.3.5) | `1` (§4.3.3.2) | verplicht |  |
| Herkomst definitie | §2.4.3.6 | `1` (§3.2.3.5) | - | verplicht | ja |
| Toelichting | §2.4.3.7 | `0..1` (§3.2.3.5) | `0..1` (§4.3.3.2) | optioneel |  |
| Datum opname | §2.4.3.8 | `1` (§3.2.3.5) | `1` (§4.3.3.2) | verplicht |  |
| Lengte | §2.4.3.29 | `0..1` (§3.2.3.5) | `0..1` (§4.3.3.2) | optioneel |  |
| Patroon | §2.4.3.30 | `0..1` (§3.2.3.5) | `0..1` (§4.3.3.2) | optioneel |  |
| Formeel patroon | §2.4.3.31 | `0..1` (§3.2.3.5) | `0..1` (§4.3.3.2) | optioneel |  |
| Kardinaliteit | §2.4.3.14 | `1` (§3.2.3.5) | `1` (§4.3.3.2) | verplicht |  |
| Identificerend | §2.4.3.9 | `0..1` (§3.2.3.5) | `0..1` (§4.3.3.2) | optioneel |  |
| Minimumwaarde inclusief | §2.4.3.37 | `0..1` (§3.2.3.5) | `0..1` (§4.3.3.2) | optioneel |  |
| Minimumwaarde exclusief | §2.4.3.38 | `0..1` (§3.2.3.5) | `0..1` (§4.3.3.2) | optioneel |  |
| Maximumwaarde inclusief | §2.4.3.39 | `0..1` (§3.2.3.5) | `0..1` (§4.3.3.2) | optioneel |  |
| Maximumwaarde exclusief | §2.4.3.40 | `0..1` (§3.2.3.5) | `0..1` (§4.3.3.2) | optioneel |  |
| Eenheid | §2.4.3.36 | `0..1` (§3.2.3.5) | `0..1` (§4.3.3.2) | optioneel |  |
| Type (heeft datatype) | §2.4.3.28 / §2.4.4.5 | `1` (§3.2.3.5) | `1` (§4.3.3.2) | verplicht |  |
| heeft constraint | §2.4.4.17 | `0..*` (§3.2.3.5) | `0..*` (§4.3.3.2) | optioneel |  |
| Begripsterm | - | - | `0..*` (§4.3.3.2) | optioneel | ja |
<!-- EINDE GEGENEREERD -->

Eigen uitleg bij de tabel: in de LD-tabel staat Constraint twee keer (§4.3.3.2). Dat verandert niets aan de betekenis.

## 5. Voorbeeld en tegenvoorbeeld

**Eigen voorbeeld.** In de referentielijst Land: `landcode` (identificerend, CharacterString, lengte 2), `naam`, `datum ingang`.

**Tegenvoorbeeld (eigen voorbeeld).** De attribuutsoort `geboorteland` van Persoon is geen referentie-element maar een attribuutsoort met als type de referentielijst Land.

## 6. Wordt vaak verward met

- **Attribuutsoort** en **data-element.** Zie de vergelijking in `onderscheidingen/gegevensgroep-vs-gestructureerd-datatype.md` (paragraaf "Drie soorten 'onderdelen'").

## Zie ook

- `modelelementen/referentielijst.md`
- Letterlijke tekst: `python3 scripts/mim.py paragraaf 2.3.4.2`
