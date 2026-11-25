---
id: relatierol
titel: Relatierol
metaclass: Relatierol
bron: ["2.3.3.5", "2.2.4.2", "3.1.3.3", "3.2.2", "3.2.2.3", "3.2.2.4", "4.2.3.3", "4.3.2.3", "4.3.2.4", "6.4.5.9"]
mim-versie: "1.2"
status: normatief
---

# Relatierol

**In het kort.** Een relatierol benoemt hoe een object meedoet aan een relatie, zoals "eigenaar" of "woonadres". Een relatie heeft een bronkant en een doelkant; aan beide kanten kan een rol worden benoemd. Of de rol of de relatiesoort leidend is, kiest het informatiemodel.

## 1. Definitie

> De benaming van de manier waarop een object deelneemt aan een relatie met een ander object.
>
> — MIM 1.2, §2.3.3.5 (normatief)

Relatierol is abstract; er zijn twee concrete soorten:

> De relatierol die de rol beschrijft van de bron van de relatie.
>
> — MIM 1.2, §2.3.3.5 (normatief)

(dat is de definitie van **Relatierol bron**)

> De relatierol die de rol beschrijft van het doel van de relatie.
>
> — MIM 1.2, §2.3.3.5 (normatief)

(dat is de definitie van **Relatierol doel**)

## 2. Uitleg

> Met relatie wordt in deze de volgende bedoeld: `«Relatiesoort»`, `«Relatieklasse»` of `«Externe koppeling»`. Voor `«Generalisatie»` speelt het niet. Een relatie heeft een bronkant, die de eigenaar is van de relatie, en is gericht naar de doelkant. De relatierol kan aan beide kanten een `Naam` en een `Definitie` krijgen.
>
> — MIM 1.2, §2.3.3.5 (normatief)

**Relatiesoort leidend of relatierol leidend.** Dit is de enige modelleerkeuze die MIM aan de modelleur laat (§1.11). In UML:

> **Alternatief 1: Relatiesoort is leidend**
>
> Relatiesoort is verplicht, met een naam en met een definitie en deze is leidend. Metadata aspecten worden hierbij altijd vastgelegd. Het gebruik van relatierol is optioneel (zowel bij source en target). Áls er een relatierol target wordt vastgelegd, dan is de metadata hierbij wel verplicht.
>
> — MIM 1.2, §3.2.2 (normatief)

> **Alternatief 2: Relatierol is leidend**
>
> Verplichte benoeming van de rol van de target in een relatie met de bijbehoren de metagegevens en optioneel de benoeming van de naam van de relatie.
>
> — MIM 1.2, §3.2.2 (normatief)

Eigen uitleg. Bij relatierol leidend verhuizen de "kenmerk"-metagegevens (kardinaliteit, historie, authentiek, mogelijk geen waarde) van de relatiesoort naar de relatierol aan de doelkant. Vergelijk de twee varianten in de tabel hieronder en in `modelelementen/relatiesoort.md`. Zie verder `onderwerpen/relatiemodellering.md`.

## 3. Uitdrukking in UML en Linked Data

| | UML | Linked Data |
|---|---|---|
| Uitdrukking | stereotype «Relatierol» op een Property; in EA: AssociationEnd. In de tabel van §3.1.3.3 heten de concrete soorten "Relatierol source" en "Relatierol target". | `mim:Relatierol` (abstract), `mim:RelatierolBron`, `mim:RelatierolDoel` (§4.2.3.3) |
| Metagegevens | §3.2.2.3 (relatiesoort leidend), §3.2.2.4 (relatierol leidend) | §4.3.2.3, §4.3.2.4 |
| Transformatie naar RDFS/OWL/SHACL | | `sh:PropertyShape` en `owl:ObjectProperty` (§6.4.4.1, §6.4.5.9) |

In LD verwijst een relatiesoort bij relatierol leidend met `mim:relatierol` (kardinaliteit `1..2`) naar zijn rollen (§4.3.2.2).

## 4. Metagegevens en bindingen

Lees de tabel zoals beschreven in `metagegevens.md` (paragraaf "Zo lees je de tabellen").

<!-- BEGIN GEGENEREERD: metagegevens relatierol -->
**Variant: alt 1: relatiesoort leidend**

| Metagegeven | Betekenis | UML | LD | Verplicht | Verschil UML/LD |
|---|---|---|---|---|---|
| Identificatie | §2.4.2.2 | `1` (§3.2.2.3) | `1` (§4.3.2.3) | verplicht |  |
| Naam | §2.4.3.1 | `1` (§3.2.2.3) | `0..1` (§4.3.2.3) | afwijkend tussen UML en LD | ja |
| Alias | §2.4.3.2 | `0..1` (§3.2.2.3) | `0..1` (§4.3.2.3) | optioneel |  |
| Herkomst | §2.4.3.4 | `1` (§3.2.2.3) | - | verplicht | ja |
| Begrip | §2.4.3.3 | `0..*` (§3.2.2.3) | `0..*` (§4.3.2.3) | optioneel |  |
| Definitie | §2.4.3.5 | `1` (§3.2.2.3) | `0..1` (§4.3.2.3) | afwijkend tussen UML en LD | ja |
| Herkomst definitie | §2.4.3.6 | `1` (§3.2.2.3) | - | verplicht | ja |
| Toelichting | §2.4.3.7 | `0..1` (§3.2.2.3) | - | optioneel | ja |
| Datum opname | §2.4.3.8 | `1` (§3.2.2.3) | - | verplicht | ja |
| heeft constraint | §2.4.4.17 | `0..*` (§3.2.2.3) | `0..*` (§4.3.2.3) | optioneel |  |
| Begripsterm | - | - | `0..*` (§4.3.2.3) | optioneel | ja |

**Variant: alt 2: relatierol leidend**

| Metagegeven | Betekenis | UML | LD | Verplicht | Verschil UML/LD |
|---|---|---|---|---|---|
| Identificatie | §2.4.2.2 | `1` (§3.2.2.4) | `1` (§4.3.2.4) | verplicht |  |
| Naam | §2.4.3.1 | `1` (§3.2.2.4) | `1` (§4.3.2.4) | verplicht |  |
| Alias | §2.4.3.2 | `0..1` (§3.2.2.4) | `0..1` (§4.3.2.4) | optioneel |  |
| Herkomst | §2.4.3.4 | `1` (§3.2.2.4) | `1` (§4.3.2.4) | verplicht |  |
| Begrip | §2.4.3.3 | `0..*` (§3.2.2.4) | `0..*` (§4.3.2.4) | optioneel |  |
| Definitie | §2.4.3.5 | `1` (§3.2.2.4) | `1` (§4.3.2.4) | verplicht |  |
| Herkomst definitie | §2.4.3.6 | `1` (§3.2.2.4) | `1` (§4.3.2.4) | verplicht |  |
| Toelichting | §2.4.3.7 | `0..1` (§3.2.2.4) | `0..1` (§4.3.2.4) | optioneel |  |
| Datum opname | §2.4.3.8 | `1` (§3.2.2.4) | `1` (§4.3.2.4) | verplicht |  |
| Identificerend | §2.4.3.9 | `0..1` (§3.2.2.4) | `0..1` (§4.3.2.4) | optioneel |  |
| Kardinaliteit | §2.4.3.14 | `1` (§3.2.2.4) | `1` (§4.3.2.4) | verplicht |  |
| heeft tijdlijn geldigheid | §2.4.3.10 | `1` (§3.2.2.4) | `1` (§4.3.2.4) | verplicht |  |
| Indicatie materiële historie | §2.4.3.11 | `1` (§3.2.2.4) | `1` (§4.3.2.4) | verplicht |  |
| heeft tijdlijn registratie | §2.4.3.12 | `1` (§3.2.2.4) | `1` (§4.3.2.4) | verplicht |  |
| Indicatie formele historie | §2.4.3.13 | `1` (§3.2.2.4) | `1` (§4.3.2.4) | verplicht |  |
| Authentiek | §2.4.3.16 | `1` (§3.2.2.4) | `1` (§4.3.2.4) | verplicht |  |
| Mogelijk geen waarde | §2.4.3.19 | `1` (§3.2.2.4) | `1` (§4.3.2.4) | verplicht |  |
| heeft constraint | §2.4.4.17 | `0..*` (§3.2.2.4) | `0..*` (§4.3.2.4) | optioneel |  |
| Begripsterm | - | - | `0..*` (§4.3.2.4) | optioneel | ja |
<!-- EINDE GEGENEREERD -->

## 5. Voorbeeld en tegenvoorbeeld

**Voorbeeld uit MIM.** Bij use case 5 van Keuze heeft Vervoermiddel een keuze tussen de relatiesoorten/rollen `heeft als contactpersoon`/`eigenaar` en `wordt verhuurd door`/`verhuurbedrijf` (§2.3.7.2). "eigenaar" en "verhuurbedrijf" zijn de rollen aan de doelkant.

**Eigen voorbeeld.** Relatiesoort "woont op" van Persoon naar Nummeraanduiding, met doelrol "woonadres". Bij relatiesoort leidend is "woont op" verplicht en "woonadres" optioneel; bij relatierol leidend is "woonadres" verplicht en de naam van de relatiesoort optioneel.

## 6. Wordt vaak verward met

- **Relatiesoort.** De relatiesoort is het verband, de rol de deelname eraan.
- **Doel (metagegeven).** Het metagegeven Doel wijst het doel-objecttype aan; de relatierol doel benoemt de rol die dat object speelt.

## Zie ook

- `onderwerpen/relatiemodellering.md`
- Letterlijke tekst: `python3 scripts/mim.py paragraaf 2.3.3.5`
