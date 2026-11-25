---
id: view
titel: View
metaclass: View
bron: ["2.3.6.4", "3.2.5.4", "4.3.5.4", "6.4.7.3", "5.13", "6.4.3"]
mim-versie: "1.2"
status: normatief
---

# View

**In het kort.** Een view is een package in het eigen informatiemodel met een selectie uit een ander (extern) informatiemodel: alleen de gegevens die voor het eigen model relevant zijn. De definities blijven die van het externe model.

## 1. Definitie

> Een groepering van modelelementen die gespecificeerd zijn in een extern informatiemodel en vanuit het perspectief van het eigen informatiemodel inzicht geeft welke gegevens van deze objecttypen relevant zijn binnen het eigen informatiemodel.
>
> — MIM 1.2, §2.3.6.4 (normatief)

## 2. Uitleg

> Uitgangspunten hierbij zijn dat de definitie van de structuur van gegevens van het andere informatiemodel één op één overgenomen wordt, waarbij expliciet gemaakt wordt welke gegevens tot het eigen model behoren en welke tot het andere model.
>
> — MIM 1.2, §5.13 (normatief)

Eigen uitleg. Een view staat, anders dan een extern package, binnen het eigen informatiemodel-package (§2.3.6). Een objecttype in de view wordt vanuit het eigen model bereikt met een externe koppeling.

In Linked Data krijgen de elementen in een view de URI's van het externe model; de shapes krijgen de basis-URI van het eigen model (§6.4.3).

## 3. Uitdrukking in UML en Linked Data

| | UML | Linked Data |
|---|---|---|
| Uitdrukking | stereotype «View» op een (UML) Package (§3.1.3.5) | `mim:View` (§4.2.3.5) |
| Metagegevens | §3.2.5.4 | §4.3.5.4 |
| Transformatie naar RDFS/OWL/SHACL | | `owl:imports` (§6.4.4.1, §6.4.7.3) |

## 4. Metagegevens en bindingen

Lees de tabel zoals beschreven in `metagegevens.md` (paragraaf "Zo lees je de tabellen").

<!-- BEGIN GEGENEREERD: metagegevens view -->
| Metagegeven | Betekenis | UML | LD | Verplicht | Verschil UML/LD |
|---|---|---|---|---|---|
| Identificatie | §2.4.2.2 | `1` (§3.2.5.4) | `1` (§4.3.5.4) | verplicht |  |
| Naam | §2.4.3.1 | `1` (§3.2.5.4) | `1` (§4.3.5.4) | verplicht |  |
| Alias | §2.4.3.2 | `0..1` (§3.2.5.4) | `0..1` (§4.3.5.4) | optioneel |  |
| Herkomst | §2.4.3.4 | `1` (§3.2.5.4) | `1` (§4.3.5.4) | verplicht |  |
| Definitie | §2.4.3.5 | `1` (§3.2.5.4) | `1` (§4.3.5.4) | verplicht |  |
| Herkomst definitie | §2.4.3.6 | `1` (§3.2.5.4) | - | verplicht | ja |
| Toelichting | §2.4.3.7 | `0..1` (§3.2.5.4) | `0..1` (§4.3.5.4) | optioneel |  |
| Datum opname | §2.4.3.8 | `1` (§3.2.5.4) | `1` (§4.3.5.4) | verplicht |  |
| Locatie | §2.4.3.24 | `1` (§3.2.5.4) | `1` (§4.3.5.4) | verplicht |  |
| Basis-URI | §2.4.2.1 | `0..1` (§3.2.5.4) | `0..1` (§4.3.5.4) | optioneel |  |
| heeft constraint | §2.4.4.17 | `0..*` (§3.2.5.4) | `0..*` (§4.3.5.4) | optioneel |  |
| bevat modelelement | §2.4.4.9 | `0..*` (§3.2.5.4) | - | optioneel | ja |
<!-- EINDE GEGENEREERD -->

## 5. Voorbeeld en tegenvoorbeeld

**Voorbeeld uit MIM.**

> IMKAD-BRP. Een aantal van de gegevens uit de basisregistratie personen (BRP) zijn relevant voor de basisregistratie Kadaster. Deze relevante subset is door de beheerder van IMKAD ondergebracht in de view IMKAD-BRP.
>
> — MIM 1.2, §2.3.6.4 (niet-normatief, voorbeeld)

**Tegenvoorbeeld (eigen voorbeeld).** Ongewijzigd gebruikte NEN 3610-datatypen horen in een extern package, niet in een view.

## 6. Wordt vaak verward met

- **Extern** en **externe koppeling.** Zie `onderscheidingen/relatiesoort-externe-koppeling-view-extern.md`.

## Zie ook

- Letterlijke tekst: `python3 scripts/mim.py paragraaf 2.3.6.4`
