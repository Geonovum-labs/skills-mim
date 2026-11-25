---
id: enumeratiewaarde
titel: Enumeratiewaarde
metaclass: Enumeratiewaarde
bron: ["2.3.4.4", "3.2.3.3", "4.3.6.2", "6.4.5.13", "2.4.3.2", "2.4.3.32"]
mim-versie: "1.2"
status: normatief
---

# Enumeratiewaarde

**In het kort.** Een enumeratiewaarde is één waarde uit een enumeratie, zoals "Plein" of "M". Alleen deze waarden mogen worden gebruikt.

## 1. Definitie

> Een gedefinieerde waarde, in de vorm van een eenmalig vastgesteld constant gegeven.
>
> — MIM 1.2, §2.3.4.4 (normatief)

## 2. Uitleg

> De waarde van de data zelf. Bijvoorbeeld: Plein, Brug, Spoor, M (man). Alleen deze waarde mag gebruikt worden.
>
> — MIM 1.2, §2.3.4.4 (normatief)

Eigen uitleg. Bij een enumeratiewaarde is de naam de waarde zelf. Daarom gaat MIM anders om met Alias en Code:

- Een **Code** is een unieke code die aan de waarde is toegekend (§2.4.3.32).
- In UML wordt de **Alias** van een UML-EnumerationLiteral niet als alternatieve naam gebruikt, maar alleen om de Code vast te leggen:

> De `Alias` wordt hier, mede daarom, gebruikt voor (alleen) de modellering van het metagegeven aspect Code die aanvullend is op naam (niet een alternatief van naam).
>
> — MIM 1.2, §2.4.3.2 (normatief)

Volgens §2.4.3.2 is Alias "expliciet niet" van toepassing op Enumeratiewaarde, terwijl de alinea ervoor de Alias wel noemt voor een codering van een enumeratiewaarde. Zie `bekende-onduidelijkheden.md`.

## 3. Uitdrukking in UML en Linked Data

| | UML | Linked Data |
|---|---|---|
| Uitdrukking | een (UML) EnumerationLiteral zonder stereotype; in EA: EnumerationLiteral (tabel §3.1.2) | `mim:Enumeratiewaarde` (§4.2.2), gekoppeld via `mim:waarde` |
| Metagegevens | §3.2.3.3 | §4.3.6.2 |
| Transformatie naar RDFS/OWL/SHACL | | instantie van de enumeratieklasse; `mim:code` wordt `skos:notation` (§6.4.4.1, §6.4.4.2, §6.4.5.13) |

## 4. Metagegevens en bindingen

Lees de tabel zoals beschreven in `metagegevens.md` (paragraaf "Zo lees je de tabellen").

<!-- BEGIN GEGENEREERD: metagegevens enumeratiewaarde -->
| Metagegeven | Betekenis | UML | LD | Verplicht | Verschil UML/LD |
|---|---|---|---|---|---|
| Identificatie | §2.4.2.2 | `1` (§3.2.3.3) | `1` (§4.3.6.2) | verplicht |  |
| Naam | §2.4.3.1 | `1` (§3.2.3.3) | `1` (§4.3.6.2) | verplicht |  |
| Code | §2.4.3.32 | `0..1` (§3.2.3.3) | `0..1` (§4.3.6.2) | optioneel |  |
| Herkomst | §2.4.3.4 | `0..1` (§3.2.3.3) | - | optioneel | ja |
| Begrip | §2.4.3.3 | `0..*` (§3.2.3.3) | `0..*` (§4.3.6.2) | optioneel |  |
| Definitie | §2.4.3.5 | `0..1` (§3.2.3.3) | `0..1` (§4.3.6.2) | optioneel |  |
| Herkomst definitie | §2.4.3.6 | `0..1` (§3.2.3.3) | - | optioneel | ja |
| Toelichting | §2.4.3.7 | `0..1` (§3.2.3.3) | `0..1` (§4.3.6.2) | optioneel |  |
| Datum opname | §2.4.3.8 | `1` (§3.2.3.3) | `1` (§4.3.6.2) | verplicht |  |
| heeft constraint | §2.4.4.17 | `0..*` (§3.2.3.3) | `0..*` (§4.3.6.2) | optioneel |  |
| Begripsterm | - | - | `0..*` (§4.3.6.2) | optioneel | ja |
<!-- EINDE GEGENEREERD -->

Eigen uitleg bij de tabel: Definitie is bij een enumeratiewaarde optioneel (UML-tabel §3.2.3.3).

## 5. Voorbeeld en tegenvoorbeeld

**Voorbeeld uit MIM.** Plein, Brug, Spoor, M (man) (§2.3.4.4).

**Tegenvoorbeeld (eigen voorbeeld).** "Nederland" in een lijst van landen die buiten het model wordt beheerd is geen enumeratiewaarde maar een item in een referentielijst of codelijst.

## 6. Wordt vaak verward met

- **Referentie-element.** Een referentie-element is een kenmerk van een item in een referentielijst; een enumeratiewaarde is zelf de waarde.

## Zie ook

- `modelelementen/enumeratie.md`
- Letterlijke tekst: `python3 scripts/mim.py paragraaf 2.3.4.4`
