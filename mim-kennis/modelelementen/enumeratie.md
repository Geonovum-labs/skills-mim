---
id: enumeratie
titel: Enumeratie
metaclass: Enumeratie
bron: ["2.3.4.3", "3.1.2", "3.2.3.2", "4.3.6.1", "6.4.5.12", "5.4.1"]
mim-versie: "1.2"
status: normatief
---

# Enumeratie

**In het kort.** Een enumeratie is een vaste, in het model opgesomde lijst waarden. Komt er een waarde bij, dan verandert het model.

## 1. Definitie

> Een datatype waarvan de mogelijke waarden limitatief zijn opgesomd in een statische lijst.
>
> — MIM 1.2, §2.3.4.3 (normatief)

## 2. Uitleg

> In de registratie krijgt een attribuut één van deze waarden. De lijst is een statische lijst met constanten (meerdere attributen, zoals bij een referentielijst, zijn nooit aan de orde).
>
> — MIM 1.2, §2.3.4.3 (normatief)

> Dit zijn statische lijsten, waaruit één waarde gekozen kan worden. De registratie en bijbehorende koppelvlakken kunnen erop vertrouwen dat er geen nieuwe waardes worden toegevoegd. Als er een nieuwe waarde bij komt wordt dit via een modelwijziging doorgevoerd.
>
> — MIM 1.2, §5.4.1 (normatief)

Eigen uitleg. Gebruik een enumeratie voor lijsten die niet of weinig veranderen. Bij dynamiek is een referentielijst of codelijst de keuze (§5.4.1).

MIM raadt af om in een eigen enumeratie een waarde als "onbekend" op te nemen; daarvoor is het metagegeven Mogelijk geen waarde (§5.11). Uitzondering: gegevens die één-op-één uit een andere registratie worden overgenomen die "onbekend" wel gebruikt.

## 3. Uitdrukking in UML en Linked Data

| | UML | Linked Data |
|---|---|---|
| Uitdrukking | een (UML) Enumeration zonder stereotype; in EA: Enumeration (tabel §3.1.2). De kop van §3.2.3.2 noemt wel «Enumeratie». | `mim:Enumeratie` (§4.2.2) |
| Metagegevens | §3.2.3.2 | §4.3.6.1 |
| Transformatie naar RDFS/OWL/SHACL | | `owl:Class`, `sh:NodeShape` en `skos:ConceptScheme` (§6.4.4.1, §6.4.5.12) |

## 4. Metagegevens en bindingen

Lees de tabel zoals beschreven in `metagegevens.md` (paragraaf "Zo lees je de tabellen").

<!-- BEGIN GEGENEREERD: metagegevens enumeratie -->
| Metagegeven | Betekenis | UML | LD | Verplicht | Verschil UML/LD |
|---|---|---|---|---|---|
| Identificatie | §2.4.2.2 | `1` (§3.2.3.2) | `1` (§4.3.6.1) | verplicht |  |
| Naam | §2.4.3.1 | `1` (§3.2.3.2) | `1` (§4.3.6.1) | verplicht |  |
| Alias | §2.4.3.2 | `0..1` (§3.2.3.2) | `0..1` (§4.3.6.1) | optioneel |  |
| Herkomst | §2.4.3.4 | `1` (§3.2.3.2) | - | verplicht | ja |
| Begrip | §2.4.3.3 | `0..*` (§3.2.3.2) | `0..*` (§4.3.6.1) | optioneel |  |
| Definitie | §2.4.3.5 | `1` (§3.2.3.2) | `1` (§4.3.6.1) | verplicht |  |
| Herkomst definitie | §2.4.3.6 | `1` (§3.2.3.2) | - | verplicht | ja |
| Toelichting | §2.4.3.7 | `0..1` (§3.2.3.2) | `0..1` (§4.3.6.1) | optioneel |  |
| Datum opname | §2.4.3.8 | `1` (§3.2.3.2) | `1` (§4.3.6.1) | verplicht |  |
| bevat enumeratiewaarde | §2.4.4.10 | `1..*` (§3.2.3.2) | `1..*` (§4.3.6.1) | verplicht |  |
| heeft constraint | §2.4.4.17 | `0..*` (§3.2.3.2) | `0..*` (§4.3.6.1) | optioneel |  |
| Begripsterm | - | - | `0..*` (§4.3.6.1) | optioneel | ja |
<!-- EINDE GEGENEREERD -->

## 5. Voorbeeld en tegenvoorbeeld

**Voorbeeld uit MIM.** De attribuutsoort Naamgebruik met een enumeratie met onder meer de waarden ‘eigen’ en ‘eigen, partner’ (§5.4.1).

**Tegenvoorbeeld (eigen voorbeeld).** De lijst van gemeenten verandert bij elke gemeentelijke herindeling. Dat is geen enumeratie maar een referentielijst of codelijst.

## 6. Wordt vaak verward met

- **Referentielijst** en **codelijst.** Zie `onderscheidingen/enumeratie-vs-referentielijst-vs-codelijst.md`.
- **Keuze.** Een keuze somt modelelementen op (datatypen, attribuutsoorten, relatiedoelen), geen waarden.

## Zie ook

- `modelelementen/enumeratiewaarde.md`, `onderwerpen/waardelijsten.md`
- Letterlijke tekst: `python3 scripts/mim.py paragraaf 2.3.4.3`
