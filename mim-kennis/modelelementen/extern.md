---
id: extern
titel: Extern
metaclass: Extern
bron: ["2.3.6.3", "3.2.5.2", "4.3.5.3", "6.4.7.2", "5.12"]
mim-versie: "1.2"
status: normatief
---

# Extern

**In het kort.** Een extern package bevat modelelementen die een andere partij beheert en die het eigen model ongewijzigd gebruikt, bijvoorbeeld de datatypen uit NEN 3610. Het staat buiten het eigen informatiemodel-package.

## 1. Definitie

> Een groepering van modelelementen die een externe instantie beheert en beschikbaar stelt aan een informatiemodel en die in het informatiemodel ongewijzigd gebruikt worden.
>
> — MIM 1.2, §2.3.6.3 (normatief)

## 2. Uitleg

> Deze packages worden dan wel buiten het eigen informatiemodel gehouden. Ze zijn extern aan het eigen model. Het beheer en de definitie vindt dan ook buiten het eigen model plaats.
>
> — MIM 1.2, §5.12 (normatief)

> De packages bevatten alleen de constructies die ook daadwerkelijk binnen het ‘eigen’ informatiemodel wordt gebruikt.
>
> — MIM 1.2, §5.12 (normatief)

Eigen uitleg. Een organisatie kan ook een eigen extern package maken, bijvoorbeeld voor datatypen die over meerdere informatiemodellen worden hergebruikt (§5.12). Een element uit een extern package kan als datatype worden gebruikt, of via een relatie worden aangesproken (§5.12).

## 3. Uitdrukking in UML en Linked Data

| | UML | Linked Data |
|---|---|---|
| Uitdrukking | stereotype «Extern» op een (UML) Package (§3.1.3.5) | `mim:Extern` (§4.2.3.5) |
| Metagegevens | §3.2.5.2 | §4.3.5.3 |
| Transformatie naar RDFS/OWL/SHACL | | `owl:imports` (§6.4.4.1, §6.4.7.2) |

## 4. Metagegevens en bindingen

Lees de tabel zoals beschreven in `metagegevens.md` (paragraaf "Zo lees je de tabellen").

<!-- BEGIN GEGENEREERD: metagegevens extern -->
| Metagegeven | Betekenis | UML | LD | Verplicht | Verschil UML/LD |
|---|---|---|---|---|---|
| Identificatie | §2.4.2.2 | `1` (§3.2.5.2) | `1` (§4.3.5.3) | verplicht |  |
| Naam | §2.4.3.1 | `1` (§3.2.5.2) | `1` (§4.3.5.3) | verplicht |  |
| Alias | §2.4.3.2 | `0..1` (§3.2.5.2) | `0..1` (§4.3.5.3) | optioneel |  |
| Herkomst | §2.4.3.4 | `1` (§3.2.5.2) | `1` (§4.3.5.3) | verplicht |  |
| Definitie | §2.4.3.5 | `1` (§3.2.5.2) | `1` (§4.3.5.3) | verplicht |  |
| Herkomst definitie | §2.4.3.6 | `1` (§3.2.5.2) | - | verplicht | ja |
| Toelichting | §2.4.3.7 | `0..1` (§3.2.5.2) | `0..1` (§4.3.5.3) | optioneel |  |
| Datum opname | §2.4.3.8 | `1` (§3.2.5.2) | `1` (§4.3.5.3) | verplicht |  |
| Locatie | §2.4.3.24 | `1` (§3.2.5.2) | `1` (§4.3.5.3) | verplicht |  |
| Basis-URI | §2.4.2.1 | `0..1` (§3.2.5.2) | `0..1` (§4.3.5.3) | optioneel |  |
| heeft constraint | §2.4.4.17 | `0..*` (§3.2.5.2) | `0..*` (§4.3.5.3) | optioneel |  |
| bevat modelelement | §2.4.4.9 | `0..*` (§3.2.5.2) | - | optioneel | ja |
<!-- EINDE GEGENEREERD -->

## 5. Voorbeeld en tegenvoorbeeld

**Voorbeeld uit MIM.**

> Voorbeeld: het Externe package NEN3610 met datatype NEN3610ID. Het datatype van attribuutsoort Identificatie wegdeel in RSGB verwijst naar het datatype NEN3610ID zoals opgenomen in het Externe package.
>
> — MIM 1.2, §2.3.6.3 (niet-normatief, voorbeeld)

**Tegenvoorbeeld (eigen voorbeeld).** Een selectie van BRP-gegevens die de BRK zelf vastlegt en voor eigen gebruik beschrijft, is geen extern package maar een view.

## 6. Wordt vaak verward met

- **View.** Zie `onderscheidingen/relatiesoort-externe-koppeling-view-extern.md`.

## Zie ook

- Letterlijke tekst: `python3 scripts/mim.py paragraaf 2.3.6.3`
