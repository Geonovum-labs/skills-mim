---
id: codelijst
titel: Codelijst
metaclass: Codelijst
bron: ["2.3.4.5", "3.2.3.1", "4.3.3.3", "6.4.5.14", "5.4.3", "2.4.3.26", "2.4.3.27"]
mim-versie: "1.2"
status: normatief
---

# Codelijst

**In het kort.** Een codelijst is een waardelijst die buiten het model wordt beheerd en waarvan het model alleen zegt wáár hij staat en welk veld de waarde bevat. De structuur van de lijst beschrijft het model niet. In gebruik lijkt een codelijst op een enumeratie.

## 1. Definitie

> De representatie van een lijst met een opsomming van de mogelijke domeinwaarden van een attribuutsoort, die buiten het model in een externe waardelijst worden beheerd. De domeinwaarden in de lijst kunnen in de loop van de tijd aangepast, uitgebreid, of verwijderd worden, zonder dat het informatiemodel aangepast wordt. De representatie bevat in tegenstelling tot een referentielijst geen metagegevens die de structuur beschrijven.
>
> — MIM 1.2, §2.3.4.5 (normatief)

## 2. Uitleg

> Zowel referentielijsten als codelijsten zijn in feite waardelijsten. In tegenstelling echter tot de referentielijst wordt de structuur van een codelijst *niet* in het informatiemodel beschreven, omdat die niet (nader) geduid hoeft te worden in het informatiemodel.
>
> — MIM 1.2, §2.3.4.5 (normatief)

> Welk specifiek attribuut dat is staat in het metagegeven Waarde-item. In het gebruik is een Codelijst daarom analoog aan een Enumeratie.
>
> — MIM 1.2, §2.3.4.5 (normatief)

> Als het wel van belang is om de structuur van een Codelijst in het model te definieren, dan moet een `«Referentielijst»` worden gebruikt.
>
> — MIM 1.2, §2.3.4.5 (normatief)

Eigen uitleg. Specifieke metagegevens van de codelijst:

- **Locatie**: waar de lijst gepubliceerd is (§2.4.3.24);
- **Doelformaat**: in welk formaat, bijvoorbeeld SKOS of CSV (§2.4.3.25);
- **Waarde-item**: welk item van de lijst de waarde bevat (§2.4.3.26);
- **Profielspecificatie**: verwijzing naar het profiel dat de technische implementatie beschrijft (§2.4.3.27).

De definitie en toelichting van de codelijst zijn in MIM 1.2 aangepast (versielog, issue 253).

## 3. Uitdrukking in UML en Linked Data

| | UML | Linked Data |
|---|---|---|
| Uitdrukking | stereotype «Codelijst» op een (UML) Datatype; in EA: Datatype (§3.1.2) | `mim:Codelijst` (§4.2.2) |
| Metagegevens | §3.2.3.1 | §4.3.3.3 |
| Transformatie naar RDFS/OWL/SHACL | | `owl:Class` en `sh:NodeShape` (§6.4.4.1, §6.4.5.14) |

## 4. Metagegevens en bindingen

Lees de tabel zoals beschreven in `metagegevens.md` (paragraaf "Zo lees je de tabellen").

<!-- BEGIN GEGENEREERD: metagegevens codelijst -->
| Metagegeven | Betekenis | UML | LD | Verplicht | Verschil UML/LD |
|---|---|---|---|---|---|
| Identificatie | §2.4.2.2 | `1` (§3.2.3.1) | `1` (§4.3.3.3) | verplicht |  |
| Naam | §2.4.3.1 | `1` (§3.2.3.1) | `1` (§4.3.3.3) | verplicht |  |
| Alias | §2.4.3.2 | `0..1` (§3.2.3.1) | `0..1` (§4.3.3.3) | optioneel |  |
| Herkomst | §2.4.3.4 | `1` (§3.2.3.1) | `1` (§4.3.3.3) | verplicht |  |
| Begrip | §2.4.3.3 | `0..*` (§3.2.3.1) | `0..*` (§4.3.3.3) | optioneel |  |
| Definitie | §2.4.3.5 | `1` (§3.2.3.1) | `1` (§4.3.3.3) | verplicht |  |
| Herkomst definitie | §2.4.3.6 | `1` (§3.2.3.1) | - | verplicht | ja |
| Toelichting | §2.4.3.7 | `0..1` (§3.2.3.1) | `0..1` (§4.3.3.3) | optioneel |  |
| Datum opname | §2.4.3.8 | `1` (§3.2.3.1) | `1` (§4.3.3.3) | verplicht |  |
| Locatie | §2.4.3.24 | `1..1` (§3.2.3.1) | `1` (§4.3.3.3) | verplicht |  |
| Doelformaat | §2.4.3.25 | `1..1` (§3.2.3.1) | - | verplicht | ja |
| Waarde-item | §2.4.3.26 | `0..1` (§3.2.3.1) | - | optioneel | ja |
| Profielspecificatie | §2.4.3.27 | `0..1` (§3.2.3.1) | - | optioneel | ja |
| heeft constraint | §2.4.4.17 | `0..*` (§3.2.3.1) | `0..*` (§4.3.3.3) | optioneel |  |
| Begripsterm | - | - | `0..*` (§4.3.3.3) | optioneel | ja |
<!-- EINDE GEGENEREERD -->

Eigen uitleg bij de tabel: de LD-tabel (§4.3.3.3) noemt Doelformaat, Waarde-item en Profielspecificatie niet. De vocabulaire definieert ze ook niet als aparte eigenschap. Meld dit verschil als iemand een codelijst in Linked Data wil beschrijven.

## 5. Voorbeeld en tegenvoorbeeld

**Eigen voorbeeld.** Een attribuutsoort `soortWerkzaamheid` met als type de codelijst `SoortWerkzaamheid`, gepubliceerd als SKOS-begrippenlijst (Locatie: een URI, Doelformaat: SKOS, Waarde-item: `skos:prefLabel`).

**Tegenvoorbeeld uit MIM.** Moet het model de kenmerken van de items beschrijven (zoals bij Land: code, naam, ingangsdatum), dan is het een referentielijst (§2.3.4.5, §5.4.3).

## 6. Wordt vaak verward met

- **Referentielijst** en **enumeratie.** Zie `onderscheidingen/enumeratie-vs-referentielijst-vs-codelijst.md`.

## Zie ook

- `onderwerpen/waardelijsten.md`
- Letterlijke tekst: `python3 scripts/mim.py paragraaf 2.3.4.5`
