---
id: gestructureerd-datatype
titel: Gestructureerd datatype
metaclass: Gestructureerd datatype
bron: ["2.3.5.3", "3.1.2", "3.2.4.2", "4.2.2", "4.3.4.2", "6.4.6.3", "5.1.4", "5.1.4.1", "5.2.2"]
mim-versie: "1.2"
status: normatief
---

# Gestructureerd datatype

**In het kort.** Een gestructureerd datatype is een datatype dat uit minstens twee onderdelen bestaat die alleen samen betekenis hebben, zoals een bedrag (35) met een valuta (euro). Het geheel "identificeert zichzelf": er is maar één "35 euro".

## 1. Definitie

> Specifiek benoemd datatype dat de structuur van een gegeven beschrijft, samengesteld uit minimaal twee elementen die in samenhang betekenisvol zijn.
>
> — MIM 1.2, §2.3.5.3 (normatief)

## 2. Uitleg

> De introductie van één datatype Bedrag, uitgedrukt in som en valuta, legt dus vast dat som en valuta onlosmakelijk met elkaar zijn verbonden.
>
> — MIM 1.2, §2.3.5.3 (normatief)

> Het identificerend zijn geldt bijvoorbeeld niet voor Jan Jansen. Er zijn meerdere personen met deze naam en dat zijn verschillende personen (Jan Jansen is dan ook een gegevensgroeptype Naam met voornaam Jan en achternaam Jansen en geen Gestructureerd datatype).
>
> — MIM 1.2, §2.3.5.3 (normatief)

Eigen uitleg. De onderdelen heten data-elementen. Elk data-element heeft zelf een datatype, meestal een primitief datatype; in bijzondere gevallen weer een gestructureerd datatype (§5.1.4). Een gestructureerd datatype heeft altijd twee of meer data-elementen (§5.1.2).

**Als één waarde uitwisselen.** Heeft het gestructureerde datatype als geheel een patroon of formeel patroon, dan worden de data-elementen altijd als één gegevenselement uitgewisseld; anders als losse elementen (§5.1.4.1). Voorbeeld: Objectnummering met patroon `Gemeentecode.Objecttypecode.Nummer`.

**Regel conceptueel en logisch.** Een gestructureerd datatype in een conceptueel model blijft een gestructureerd datatype in het bijbehorende logische model (§5.2.2).

**Schrijfwijze.** De tabellen in MIM 1.2 schrijven het stereotype als «Gestructuurd datatype» (§3.1.2) en de LD-klasse als `mim:GestructuurdDatatype` (§4.2.2). De koppen van §3.2.4.2 en §4.3.4.2, de transformatie (§6.4.4.1) en de vocabulaire (`assets/mim.ttl`) schrijven "Gestructureerd". Zie onduidelijkheid I4. In MIM 1.1 heette dit element "Complex datatype" (§6.3).

## 3. Uitdrukking in UML en Linked Data

| | UML | Linked Data |
|---|---|---|
| Uitdrukking | stereotype «Gestructureerd datatype» (tabel: «Gestructuurd datatype») op een (UML) Datatype; in EA: Datatype (§3.1.2) | `mim:GestructureerdDatatype` (vocabulaire; tabel §4.2.2: `mim:GestructuurdDatatype`) |
| Metagegevens | §3.2.4.2 | §4.3.4.2 |
| Transformatie naar RDFS/OWL/SHACL | | `sh:NodeShape` (§6.4.4.1, §6.4.6.3) |

## 4. Metagegevens en bindingen

Lees de tabel zoals beschreven in `metagegevens.md` (paragraaf "Zo lees je de tabellen").

<!-- BEGIN GEGENEREERD: metagegevens gestructureerd-datatype -->
| Metagegeven | Betekenis | UML | LD | Verplicht | Verschil UML/LD |
|---|---|---|---|---|---|
| Identificatie | §2.4.2.2 | `1` (§3.2.4.2) | `1` (§4.3.4.2) | verplicht |  |
| Naam | §2.4.3.1 | `1` (§3.2.4.2) | `1` (§4.3.4.2) | verplicht |  |
| Alias | §2.4.3.2 | `0..1` (§3.2.4.2) | `0..1` (§4.3.4.2) | optioneel |  |
| Herkomst | §2.4.3.4 | `0..1` (§3.2.4.2) | `1` (§4.3.4.2) | afwijkend tussen UML en LD | ja |
| Begrip | §2.4.3.3 | `0..*` (§3.2.4.2) | `0..*` (§4.3.4.2) | optioneel |  |
| Definitie | §2.4.3.5 | `0..1` (§3.2.4.2) | `1` (§4.3.4.2) | afwijkend tussen UML en LD | ja |
| Herkomst definitie | §2.4.3.6 | `0..1` (§3.2.4.2) | - | optioneel | ja |
| Toelichting | §2.4.3.7 | `0..1` (§3.2.4.2) | `0..1` (§4.3.4.2) | optioneel |  |
| Datum opname | §2.4.3.8 | `1` (§3.2.4.2) | `1` (§4.3.4.2) | verplicht |  |
| Patroon | §2.4.3.30 | `0..1` (§3.2.4.2) | `0..1` (§4.3.4.2) | optioneel |  |
| Formeel patroon | §2.4.3.31 | `0..1` (§3.2.4.2) | `0..1` (§4.3.4.2) | optioneel |  |
| heeft data-element | §2.4.4.8 | `0..*` (§3.2.4.2) | `0..*` (§4.3.4.2) | optioneel |  |
| heeft constraint | §2.4.4.17 | `0..*` (§3.2.4.2) | `0..*` (§4.3.4.2) | optioneel |  |
| Begripsterm | - | - | `0..*` (§4.3.4.2) | optioneel | ja |
<!-- EINDE GEGENEREERD -->

Eigen uitleg bij de tabel: "bevat data-element" heeft in beide tabellen kardinaliteit `0..*`, terwijl de definitie minimaal twee elementen vraagt. De definitie is de inhoudelijke regel; de tabel legt de binding vast.

## 5. Voorbeeld en tegenvoorbeeld

**Voorbeeld uit MIM.** Bedrag (som en valuta), 1 liter, de datum 6 april 2017 (§2.3.5.3). Bestaande gestructureerde datatypen om te hergebruiken: NEN 3610-identificatie, Kadastrale aanduiding, Objectnummering (§5.1.4).

**Tegenvoorbeeld uit MIM.** De naam Jan Jansen (zie citaat hierboven): een gegevensgroeptype, geen gestructureerd datatype.

## 6. Wordt vaak verward met

- **Gegevensgroep / gegevensgroeptype.** Zie `onderscheidingen/gegevensgroep-vs-gestructureerd-datatype.md`.
- **Primitief datatype.** Enkelvoudig, zonder data-elementen.

## Zie ook

- `modelelementen/data-element.md`
- Letterlijke tekst: `python3 scripts/mim.py paragraaf 2.3.5.3`
