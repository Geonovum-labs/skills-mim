---
id: referentielijst
titel: Referentielijst
metaclass: Referentielijst
bron: ["2.3.4.1", "3.2.3.4", "4.3.3.1", "6.4.5.10", "5.4.2"]
mim-versie: "1.2"
status: normatief
---

# Referentielijst

**In het kort.** Een referentielijst is een waardelijst die buiten het informatiemodel wordt beheerd en waarvan het model de structuur wél beschrijft: elk item heeft meerdere kenmerken (bijvoorbeeld een landcode, een naam en een ingangsdatum). De lijst mag veranderen zonder dat het model verandert.

## 1. Definitie

> De representatie van een lijst met een opsomming van de mogelijke domeinwaarden van een attribuutsoort, die buiten het model in een externe waardelijst worden beheerd. De domeinwaarden in de lijst kunnen in de loop van de tijd aangepast, uitgebreid, of verwijderd worden, zonder dat het informatiemodel aangepast wordt (in tegenstelling tot bij een enumeratie). De representatie bevat een aantal kenmerken, die overgenomen zijn van de specificatie van de externe waardelijst.
>
> — MIM 1.2, §2.3.4.1 (normatief)

## 2. Uitleg

> De referentielijst bevat representaties van objecten, die in het informatiemodel niet als een objecttype onderwerp van gesprek zijn. De referentielijst wordt gebruikt als type van een attribuut van een object.
>
> — MIM 1.2, §2.3.4.1 (normatief)

Eigen uitleg. In de registratie staat bij het attribuut meestal alleen een verwijzing naar één item uit de lijst, niet alle gegevens van dat item (§2.3.4.1). De kenmerken van een item heten referentie-elementen. Eén referentie-element kan identificerend zijn; de referentielijst is de enige soort waardelijst die dat kent (§2.4.3.9).

**Modelleerrichtlijn.** Modelleer elke waardelijst bij voorkeur apart, met een eigen naam en locatie. Hebben meerdere lijsten dezelfde structuur, dan kan een generieke abstracte referentielijst waarvan de specifieke lijsten overerven (§5.4.2).

> Let op, wanneer er voor een bepaald attribuut in een informatiemodel of koppelvlak van een andere organisatie gekozen is voor een `«Referentielijst»`, en uw organisatie koppelt hiermee, dan is het (meestal) onverstandig om in het eigen informatiemodel dit te behandelen als enumeratie.
>
> — MIM 1.2, §5.4.2 (normatief)

Metagegevens erven niet over van Datatype: een referentielijst heeft bijvoorbeeld geen Patroon (§2.4.3, inleiding).

## 3. Uitdrukking in UML en Linked Data

| | UML | Linked Data |
|---|---|---|
| Uitdrukking | stereotype «Referentielijst» op een (UML) Datatype; in EA: Datatype (§3.1.2) | `mim:Referentielijst` (§4.2.2) |
| Metagegevens | §3.2.3.4 | §4.3.3.1 |
| Transformatie naar RDFS/OWL/SHACL | | `owl:Class` en `sh:NodeShape` (§6.4.4.1, §6.4.5.10) |

## 4. Metagegevens en bindingen

Lees de tabel zoals beschreven in `metagegevens.md` (paragraaf "Zo lees je de tabellen").

<!-- BEGIN GEGENEREERD: metagegevens referentielijst -->
| Metagegeven | Betekenis | UML | LD | Verplicht | Verschil UML/LD |
|---|---|---|---|---|---|
| Identificatie | §2.4.2.2 | `1` (§3.2.3.4) | `1` (§4.3.3.1) | verplicht |  |
| Naam | §2.4.3.1 | `1` (§3.2.3.4) | `1` (§4.3.3.1) | verplicht |  |
| Alias | §2.4.3.2 | `0..1` (§3.2.3.4) | `0..1` (§4.3.3.1) | optioneel |  |
| Herkomst | §2.4.3.4 | `1` (§3.2.3.4) | `1` (§4.3.3.1) | verplicht |  |
| Begrip | §2.4.3.3 | `0..*` (§3.2.3.4) | `0..*` (§4.3.3.1) | optioneel |  |
| Definitie | §2.4.3.5 | `1` (§3.2.3.4) | `1` (§4.3.3.1) | verplicht |  |
| Herkomst definitie | §2.4.3.6 | `1` (§3.2.3.4) | `1` (§4.3.3.1) | verplicht |  |
| Toelichting | §2.4.3.7 | `0..1` (§3.2.3.4) | `0..1` (§4.3.3.1) | optioneel |  |
| Datum opname | §2.4.3.8 | `1` (§3.2.3.4) | `1` (§4.3.3.1) | verplicht |  |
| Locatie | §2.4.3.24 | `1` (§3.2.3.4) | `1` (§4.3.3.1) | verplicht |  |
| bevat referentie-element | §2.4.4.11 | `1..*` (§3.2.3.4) | `1..*` (§4.3.3.1) | verplicht |  |
| verwijst naar supertype | §2.4.4.4 | `0..*` (§3.2.3.4) | - | optioneel | ja |
| heeft constraint | §2.4.4.17 | `0..*` (§3.2.3.4) | `0..*` (§4.3.3.1) | optioneel |  |
| Begripsterm | - | - | `0..*` (§4.3.3.1) | optioneel | ja |
<!-- EINDE GEGENEREERD -->

Eigen uitleg bij de tabel: **Locatie** is verplicht; het is de gepubliceerde plek (bij voorkeur een URI) waar de lijst te vinden is (§2.4.3.24). In de UML-tabel kan een referentielijst een supertype hebben, wat aansluit bij de modelleerrichtlijn hierboven.

## 5. Voorbeeld en tegenvoorbeeld

**Voorbeeld uit MIM.** Land: in het model geen objecttype, wel een lijst met per land een naam, ontstaansdatum, omschrijving en ISO-code (§2.3.4.1). Ook `CultuurcodeOnbebouwd` (§5.4.2).

**Tegenvoorbeeld (eigen voorbeeld).** Geslachtsaanduiding met de vaste waarden M, V, X en O, die alleen via een modelwijziging verandert: dat is een enumeratie, geen referentielijst.

## 6. Wordt vaak verward met

- **Codelijst.** Ook extern beheerd, maar het model beschrijft de structuur niet. Zie `onderscheidingen/enumeratie-vs-referentielijst-vs-codelijst.md`.
- **Objecttype.** Een referentielijst bevat representaties van objecten die in het model géén onderwerp van gesprek zijn.

## Zie ook

- `modelelementen/referentie-element.md`, `onderwerpen/waardelijsten.md`
- Letterlijke tekst: `python3 scripts/mim.py paragraaf 2.3.4.1`
