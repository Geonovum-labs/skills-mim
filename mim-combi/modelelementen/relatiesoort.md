---
id: relatiesoort
titel: Relatiesoort
metaclass: Relatiesoort
bron: ["2.3.3.2", "3.2.2", "3.2.2.1", "3.2.2.2", "4.3.2.1", "4.3.2.2", "6.4.5.6", "1.11", "2.4.1.3"]
mim-versie: "1.2"
status: normatief
---

# Relatiesoort

**In het kort.** Een relatiesoort legt vast dat objecten van het ene objecttype in verband staan met objecten van een (ander of hetzelfde) objecttype, bijvoorbeeld "Persoon heeft woonadres Nummeraanduiding". De relatie is gericht: ze hoort bij de bron, en wijst naar het doel.

## 1. Definitie

> De typering van het structurele verband tussen een object van een objecttype en een (ander) object van een ander (of hetzelfde) objecttype.
>
> — MIM 1.2, §2.3.3.2 (normatief)

## 2. Uitleg

Een relatiesoort is, net als een attribuutsoort, een kenmerk van het bron-objecttype:

> Objecten hebben eigenschappen die gemodelleerd kunnen worden met attribuutsoorten maar ook met relatiesoorten naar andere objecttypen. Relatiesoort is de metaklasse waarmee deze eigenschappen worden beschreven.
>
> — MIM 1.2, §2.3.3.2 (normatief)

> Wanneer een relatie gebruikt wordt om objecten aan elkaar te verbinden, zonder dat er eigenschappen over deze relatie worden vastgelegd, dan betreft dit de MIM-metaclass «Relatiesoort».
>
> — MIM 1.2, §2.3.3.2 (normatief)

**Richting en eigenaar.** Alle relaties zijn gericht van bron naar doel; de bron is de eigenaar van de relatie (§2.4.3.22, Unidirectioneel, default `Ja`). Bron en doel zijn metagegevens van de relatiesoort (§2.4.3.20, §2.4.3.21).

**Kardinaliteit aan twee kanten.** De kardinaliteit geeft aan met hoeveel doelobjecten één bronobject verbonden is; Kardinaliteit relatie bron geeft de andere kant (§2.4.3.15). Aan de doelkant is de kardinaliteit altijd verplicht; aan de bronkant optioneel en zonder default (noot bij §2.4.5.2).

> Voorbeeld: een verblijfsobject ligt in een pand. De eigenaar van de relatie is het verblijfsobject (de bron van de relatie) en het doel van de relatie is een pand.
>
> — MIM 1.2, §2.4.3.15 (normatief)

**Bron en doel.** Bron is altijd een objecttype of gegevensgroeptype; doel is altijd een objecttype. Een gegevensgroeptype mag geen doel zijn (§2.2.4.1, §4.2.1).

**De ene modelleerkeuze van MIM.** Een informatiemodel kiest of de relatiesoort of de relatierol leidend is. Dat bepaalt welke metagegevens verplicht zijn op de relatiesoort en welke op de relatierol. De keuze staat in het metagegeven Relatiemodelleringstype van het informatiemodel (§2.4.1.3). Zie `onderwerpen/relatiemodellering.md`.

## 3. Uitdrukking in UML en Linked Data

| | UML | Linked Data |
|---|---|---|
| Uitdrukking | stereotype «Relatiesoort» op een (UML) Association; in EA: Association (§3.1.1) | `mim:Relatiesoort` (§4.2.1) |
| Metagegevens | §3.2.2.1 (relatiesoort leidend), §3.2.2.2 (relatierol leidend) | §4.3.2.1, §4.3.2.2 |
| Transformatie naar RDFS/OWL/SHACL | | `sh:PropertyShape` en `owl:ObjectProperty` (§6.4.4.1, §6.4.5.6) |

Identificerend: als een relatiesoort identificerend is, krijgt die in UML het stereotype «id» (noot bij §3.2).

## 4. Metagegevens en bindingen

Lees de tabel zoals beschreven in `metagegevens.md` (paragraaf "Zo lees je de tabellen"). De tabel heeft twee varianten, één per relatiemodelleringstype.

<!-- BEGIN GEGENEREERD: metagegevens relatiesoort -->
**Variant: alt 1: relatiesoort leidend**

| Metagegeven | Betekenis | UML | LD | Verplicht | Verschil UML/LD |
|---|---|---|---|---|---|
| Identificatie | §2.4.2.2 | `1` (§3.2.2.1) | `1` (§4.3.2.1) | verplicht |  |
| Naam | §2.4.3.1 | `1` (§3.2.2.1) | `1` (§4.3.2.1) | verplicht |  |
| Alias | §2.4.3.2 | `0..1` (§3.2.2.1) | `0..1` (§4.3.2.1) | optioneel |  |
| Herkomst | §2.4.3.4 | `1` (§3.2.2.1) | `1` (§4.3.2.1) | verplicht |  |
| Begrip | §2.4.3.3 | `0..*` (§3.2.2.1) | `0..*` (§4.3.2.1) | optioneel |  |
| Definitie | §2.4.3.5 | `1` (§3.2.2.1) | `1` (§4.3.2.1) | verplicht |  |
| Herkomst definitie | §2.4.3.6 | `1` (§3.2.2.1) | `1` (§4.3.2.1) | verplicht |  |
| Toelichting | §2.4.3.7 | `0..1` (§3.2.2.1) | `0..1` (§4.3.2.1) | optioneel |  |
| Datum opname | §2.4.3.8 | `1` (§3.2.2.1) | `1` (§4.3.2.1) | verplicht |  |
| Identificerend | §2.4.3.9 | `0..1` (§3.2.2.1) | `0..1` (§4.3.2.1) | optioneel |  |
| Unidirectioneel | §2.4.3.22 | `1` (§3.2.2.1) | `1` (§4.3.2.1) | verplicht |  |
| Bron | §2.4.3.20 | `1` (§3.2.2.1) | `1` (§4.3.2.1) | verplicht |  |
| Doel | §2.4.3.21 | `1` (§3.2.2.1) | `1` (§4.3.2.1) | verplicht |  |
| Aggregatietype | §2.4.3.23 | `1` (§3.2.2.1) | `1` (§4.3.2.1) | verplicht |  |
| Kardinaliteit | §2.4.3.14 | `1` (§3.2.2.1) | `1` (§4.3.2.1) | verplicht |  |
| Kardinaliteit relatie bron | §2.4.3.15 | `1` (§3.2.2.1) | `0..1` (§4.3.2.1) | afwijkend tussen UML en LD | ja |
| heeft tijdlijn geldigheid | §2.4.3.10 | `1` (§3.2.2.1) | `1` (§4.3.2.1) | verplicht |  |
| Indicatie materiële historie | §2.4.3.11 | `1` (§3.2.2.1) | `1` (§4.3.2.1) | verplicht |  |
| heeft tijdlijn registratie | §2.4.3.12 | `1` (§3.2.2.1) | `1` (§4.3.2.1) | verplicht |  |
| Indicatie formele historie | §2.4.3.13 | `1` (§3.2.2.1) | `1` (§4.3.2.1) | verplicht |  |
| Authentiek | §2.4.3.16 | `1` (§3.2.2.1) | `1` (§4.3.2.1) | verplicht |  |
| Indicatie afleidbaar | §2.4.3.17 | `1` (§3.2.2.1) | `1` (§4.3.2.1) | verplicht |  |
| Mogelijk geen waarde | §2.4.3.19 | `1` (§3.2.2.1) | `1` (§4.3.2.1) | verplicht |  |
| verwijst naar relatiedoel | - | `0..*` (§3.2.2.1) | - | optioneel | ja |
| heeft constraint | §2.4.4.17 | `0..*` (§3.2.2.1) | `0..*` (§4.3.2.1) | optioneel |  |
| Begripsterm | - | - | `0..*` (§4.3.2.1) | optioneel | ja |

**Variant: alt 2: relatierol leidend**

| Metagegeven | Betekenis | UML | LD | Verplicht | Verschil UML/LD |
|---|---|---|---|---|---|
| Identificatie | §2.4.2.2 | `1` (§3.2.2.2) | `1` (§4.3.2.2) | verplicht |  |
| Naam | §2.4.3.1 | `1` (§3.2.2.2) | `0..1` (§4.3.2.2) | afwijkend tussen UML en LD | ja |
| Alias | §2.4.3.2 | `0..1` (§3.2.2.2) | `0..1` (§4.3.2.2) | optioneel |  |
| Herkomst | §2.4.3.4 | `1` (§3.2.2.2) | - | verplicht | ja |
| Begrip | §2.4.3.3 | `0..*` (§3.2.2.2) | `0..*` (§4.3.2.2) | optioneel |  |
| Definitie | §2.4.3.5 | `1` (§3.2.2.2) | `0..1` (§4.3.2.2) | afwijkend tussen UML en LD | ja |
| Herkomst definitie | §2.4.3.6 | `1` (§3.2.2.2) | - | verplicht | ja |
| Toelichting | §2.4.3.7 | `0..1` (§3.2.2.2) | - | optioneel | ja |
| Datum opname | §2.4.3.8 | `1` (§3.2.2.2) | - | verplicht | ja |
| verwijst naar relatiedoel | - | `0..*` (§3.2.2.2) | - | optioneel | ja |
| heeft constraint | §2.4.4.17 | `0..*` (§3.2.2.2) | `0..*` (§4.3.2.2) | optioneel |  |
| Begripsterm | - | - | `0..*` (§4.3.2.2) | optioneel | ja |
| Relatierol | - | - | `1..2` (§4.3.2.2) | verplicht | ja |
<!-- EINDE GEGENEREERD -->

Eigen uitleg bij de tabel:

- Bij **relatierol leidend** zijn naam en definitie van de relatiesoort volgens §3.2.2 optioneel ("optioneel de benoeming van de naam van de relatie"), maar de UML-tabel §3.2.2.2 geeft Naam en Definitie kardinaliteit 1. De LD-tabel §4.3.2.2 geeft `0..1`. Meld dit verschil.
- **Kardinaliteit relatie bron** is in de UML-tabel `1` en in de LD-tabel `0..1`; de noot bij §2.4.5.2 zegt dat de bronkant optioneel is. Zie `bekende-onduidelijkheden.md`.
- **Aggregatietype** (`Compositie`, `Gedeeld`, `Geen`) hoort bij de relatiesoort, niet bij een attribuutsoort (onduidelijkheid I3).

## 5. Voorbeeld en tegenvoorbeeld

**Voorbeeld uit MIM.**

> Bijvoorbeeld: een persoon heeft een adres. Dit kun je modelleren door middel van een `«Relatiesoort»` tussen een `«Objecttype»` `Persoon` en een `«Objecttype»` `Adres`. Het metagegeven `Bron` van de `«Relatiesoort»` bevat dan als waarde: `"Persoon"`.
>
> — MIM 1.2, §2.4.3.20 (normatief)

**Tegenvoorbeeld uit MIM.** Moeten er gegevens over de relatie zelf worden vastgelegd (bijvoorbeeld de datum van een splitsing), dan is het geen relatiesoort maar een relatieklasse (§2.3.3.3). Gelden die gegevens voor meerdere relaties tegelijk, dan wordt het een objecttype (§5.6).

**Tegenvoorbeeld uit MIM.** Een relatie naar een objecttype in een ander informatiemodel is een externe koppeling, geen relatiesoort (§2.3.3.4).

## 6. Wordt vaak verward met

- **Relatierol.** De relatiesoort is het verband zelf; de relatierol benoemt hoe een object aan dat verband deelneemt. Zie `modelelementen/relatierol.md`.
- **Attribuutsoort.** Zie `onderscheidingen/attribuutsoort-vs-relatiesoort.md`.
- **Relatieklasse.** Zie `onderscheidingen/relatieklasse-vs-objecttype.md`.
- **Externe koppeling.** Zie `onderscheidingen/relatiesoort-externe-koppeling-view-extern.md`.
- **Generalisatie.** Geen relatie tussen objecten. Zie `modelelementen/generalisatie.md`.

## Zie ook

- `modelelementen/keuze.md` (use case 4 en 5: keuze tussen relatiedoelen of relatiesoorten)
- Letterlijke tekst: `python3 scripts/mim.py paragraaf 2.3.3.2`
