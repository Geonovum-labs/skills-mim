---
id: domein
titel: Domein
metaclass: Domein
bron: ["2.3.6.2", "3.2.5.1", "4.3.5.2", "6.4.7.1"]
mim-versie: "1.2"
status: normatief
---

# Domein

**In het kort.** Een domein is een package binnen het eigen informatiemodel waarin een samenhangend deel van het model staat, bijvoorbeeld "Recht" of "Stukken" in de BRK.

## 1. Definitie

> Een groepering van modelelementen die een semantisch samenhangend gedeelte van een informatiemodel beschrijven.
>
> — MIM 1.2, §2.3.6.2 (normatief)

## 2. Uitleg

> Een domein package bevat de modelelementen waaruit een informatiemodel is samengesteld, zoals het objecttype Persoon en het objecttype Nummeraanduiding en de relatiesoort woonadres. Een informatiemodel is het hoofdpackage, en kent een aantal domein packages als subpackage.
>
> — MIM 1.2, §2.3.6.2 (normatief)

Eigen uitleg. "Domein" heeft in MIM twee betekenissen. Hier is het een **package**. Daarnaast spreekt MIM over "het beschouwde domein" als het deel van de werkelijkheid dat een model beschrijft (§1.5.2). Haal ze niet door elkaar. Het metagegeven **Informatiedomein** van het informatiemodel is weer iets anders: de aanduiding van het functionele domein, zoals BRK (§2.4.1.1).

## 3. Uitdrukking in UML en Linked Data

| | UML | Linked Data |
|---|---|---|
| Uitdrukking | stereotype «Domein» op een (UML) Package (§3.1.3.5) | `mim:Domein` (§4.2.3.5) |
| Metagegevens | §3.2.5.1 | §4.3.5.2 |
| Transformatie naar RDFS/OWL/SHACL | | `owl:Ontology` (§6.4.4.1, §6.4.7.1) |

## 4. Metagegevens en bindingen

Lees de tabel zoals beschreven in `metagegevens.md` (paragraaf "Zo lees je de tabellen").

<!-- BEGIN GEGENEREERD: metagegevens domein -->
| Metagegeven | Betekenis | UML | LD | Verplicht | Verschil UML/LD |
|---|---|---|---|---|---|
| Identificatie | §2.4.2.2 | `1` (§3.2.5.1) | `1` (§4.3.5.2) | verplicht |  |
| Naam | §2.4.3.1 | `1` (§3.2.5.1) | `1` (§4.3.5.2) | verplicht |  |
| Alias | §2.4.3.2 | `0..1` (§3.2.5.1) | `0..1` (§4.3.5.2) | optioneel |  |
| Herkomst | §2.4.3.4 | `1` (§3.2.5.1) | - | verplicht | ja |
| Definitie | §2.4.3.5 | `1` (§3.2.5.1) | - | verplicht | ja |
| Herkomst definitie | §2.4.3.6 | `1` (§3.2.5.1) | - | verplicht | ja |
| Toelichting | §2.4.3.7 | `0..1` (§3.2.5.1) | - | optioneel | ja |
| Datum opname | §2.4.3.8 | `1` (§3.2.5.1) | `1` (§4.3.5.2) | verplicht |  |
| heeft constraint | §2.4.4.17 | `0..*` (§3.2.5.1) | `0..*` (§4.3.5.2) | optioneel |  |
| Basis-URI | §2.4.2.1 | `0..1` (§3.2.5.1) | `0..1` (§4.3.5.2) | optioneel |  |
| bevat modelelement | §2.4.4.9 | `0..*` (§3.2.5.1) | - | optioneel | ja |
<!-- EINDE GEGENEREERD -->

## 5. Voorbeeld en tegenvoorbeeld

**Voorbeeld uit MIM.**

> Voorbeeld: Recht, of Stukken. De BRK houdt deze domeininformatie in aparte packages apart bij, voor het overzicht, en om de packages afzonderlijke te kunnen aanpassen, zonder impact op de andere packages.
>
> — MIM 1.2, §2.3.6.2 (niet-normatief, voorbeeld)

**Tegenvoorbeeld (eigen voorbeeld).** Een package met ongewijzigd overgenomen NEN 3610-datatypen is geen domein maar een extern package.

## Zie ook

- `modelelementen/package.md`
- Letterlijke tekst: `python3 scripts/mim.py paragraaf 2.3.6.2`
