---
id: relatieklasse
titel: Relatieklasse
metaclass: Relatieklasse
bron: ["2.3.3.3", "3.2.2.7", "4.3.2.7", "6.4.5.7", "5.6"]
mim-versie: "1.2"
status: normatief
---

# Relatieklasse

**In het kort.** Een relatieklasse is een relatiesoort waarover zelf gegevens worden vastgelegd. De gegevens horen bij één relatie tussen twee objecten en bestaan alleen zolang die relatie bestaat.

## 1. Definitie

> Een relatiesoort met eigenschappen.
>
> — MIM 1.2, §2.3.3.3 (normatief)

## 2. Uitleg

> De relatieklasse geeft aan dat er een relatie is tussen twee objecten, waarbij er gegevens over deze relatie vastgelegd moeten worden. De relatie wordt in dit geval behandeld als een object, met gegevens. De gegevens over de relatie bestaan alleen zolang de relatie tussen beide objecten bestaat en zolang elk van beide objecten zelf (nog) bestaan.
>
> — MIM 1.2, §2.3.3.3 (normatief)

Eigen uitleg. Een relatieklasse met kardinaliteit `1..*` betekent op instantieniveau veel losse relaties, elk met een eigen setje gegevens (§5.6).

**Twee uitzonderingen** (§5.6):

1. Gelden dezelfde gegevens voor meerdere relaties tegelijk, dan kan het niet als relatieklasse. Dan wordt het een objecttype met één inkomende en één uitgaande relatie; de oorspronkelijke kardinaliteit blijft behouden. Geef in de toelichting van dat objecttype aan dat het bestaansafhankelijk is van beide objecttypen.
2. Een relatieklasse tussen drie of meer objecttypen ondersteunt MIM (nog) niet; dat kan in een eigen extensie.

> Het metamodel ondersteunt (nog) geen relatieklassen tussen drie of meer objecttypen. Dit kan in uw eigen extensie toegevoegd worden.
>
> — MIM 1.2, §5.6 (normatief)

MIM schrijft niet voor hoe een relatieklasse wordt geïdentificeerd: er is geen regel dat de identificatie bestaat uit die van bron en doel, en ook geen regel voor een nieuwe betekenisloze identificatie (§5.6).

## 3. Uitdrukking in UML en Linked Data

| | UML | Linked Data |
|---|---|---|
| Uitdrukking | stereotype «Relatieklasse» op (UML) Association én (UML) Class; in EA: Associationclass (§3.1.1) | `mim:Relatieklasse` (§4.2.1) |
| Metagegevens | §3.2.2.7 | §4.3.2.7 |
| Transformatie naar RDFS/OWL/SHACL | | `rdf:Statement` (§6.4.4.1, §6.4.5.7) |

## 4. Metagegevens en bindingen

Lees de tabel zoals beschreven in `metagegevens.md` (paragraaf "Zo lees je de tabellen").

<!-- BEGIN GEGENEREERD: metagegevens relatieklasse -->
| Metagegeven | Betekenis | UML | LD | Verplicht | Verschil UML/LD |
|---|---|---|---|---|---|
| Identificatie | §2.4.2.2 | `1` (§3.2.2.7) | `1` (§4.3.2.7) | verplicht |  |
| Naam | §2.4.3.1 | `1` (§3.2.2.7) | `0..1` (§4.3.2.7) | afwijkend tussen UML en LD | ja |
| Alias | §2.4.3.2 | `0..1` (§3.2.2.7) | `0..1` (§4.3.2.7) | optioneel |  |
| Herkomst | §2.4.3.4 | `1` (§3.2.2.7) | `1` (§4.3.2.7) | verplicht |  |
| Begrip | §2.4.3.3 | `0..*` (§3.2.2.7) | `0..*` (§4.3.2.7) | optioneel |  |
| Definitie | §2.4.3.5 | `1` (§3.2.2.7) | `0..1` (§4.3.2.7) | afwijkend tussen UML en LD | ja |
| Toelichting | §2.4.3.7 | `0..1` (§3.2.2.7) | `0..1` (§4.3.2.7) | optioneel |  |
| Datum opname | §2.4.3.8 | `1` (§3.2.2.7) | `1` (§4.3.2.7) | verplicht |  |
| Herkomst definitie | §2.4.3.6 | `1` (§3.2.2.7) | `1` (§4.3.2.7) | verplicht |  |
| Unidirectioneel | §2.4.3.22 | `1` (§3.2.2.7) | `1` (§4.3.2.7) | verplicht |  |
| Bron | §2.4.3.20 | `1` (§3.2.2.7) | - | verplicht | ja |
| Doel | §2.4.3.21 | `1` (§3.2.2.7) | - | verplicht | ja |
| Aggregatietype | §2.4.3.23 | `1` (§3.2.2.7) | `1` (§4.3.2.7) | verplicht |  |
| Kardinaliteit | §2.4.3.14 | `1` (§3.2.2.7) | `1` (§4.3.2.7) | verplicht |  |
| Kardinaliteit relatie bron | §2.4.3.15 | `1` (§3.2.2.7) | - | verplicht | ja |
| Indicatie materiële historie | §2.4.3.11 | `1` (§3.2.2.7) | `1` (§4.3.2.7) | verplicht |  |
| Indicatie formele historie | §2.4.3.13 | `1` (§3.2.2.7) | `1` (§4.3.2.7) | verplicht |  |
| Authentiek | §2.4.3.16 | `1` (§3.2.2.7) | `1` (§4.3.2.7) | verplicht |  |
| Indicatie afleidbaar | §2.4.3.17 | `1` (§3.2.2.7) | `1` (§4.3.2.7) | verplicht |  |
| Mogelijk geen waarde | §2.4.3.19 | `1` (§3.2.2.7) | `1` (§4.3.2.7) | verplicht |  |
| heeft attribuut | §2.4.4.1 | `0..*` (§3.2.2.7) | - | optioneel | ja |
| verwijst naar relatiedoel | - | `0..*` (§3.2.2.7) | - | optioneel | ja |
| heeft gegevensgroep | §2.4.4.2 | `0..*` (§3.2.2.7) | - | optioneel | ja |
| heeft constraint | §2.4.4.17 | `0..*` (§3.2.2.7) | `0..*` (§4.3.2.7) | optioneel |  |
| Begripsterm | - | - | `0..*` (§4.3.2.7) | optioneel | ja |
| heeft tijdlijn geldigheid | §2.4.3.10 | - | `1` (§4.3.2.7) | verplicht | ja |
| heeft tijdlijn registratie | §2.4.3.12 | - | `1` (§4.3.2.7) | verplicht | ja |
<!-- EINDE GEGENEREERD -->

Eigen uitleg bij de tabel:

- De UML-tabel noemt alleen de oude historie-metagegevens (Indicatie materiële/formele historie); de LD-tabel noemt ook heeft tijdlijn geldigheid en heeft tijdlijn registratie. Volgens §2.4.3.10 en §2.4.3.12 gelden de nieuwe metagegevens voor relatieklassen. Meld het verschil.
- "heeft gegevensgroep" is in MIM 1.2 toegevoegd aan de tabel van de relatieklasse (versielog, issue 305).

## 5. Voorbeeld en tegenvoorbeeld

**Voorbeeld en tegenvoorbeeld uit MIM.**

> Een Perceel kan vanwege een Perceel splitsing overgaan in twee of meerdere andere Percelen. De ‘overgegaan in’ relatie wordt bijgehouden als een relatieklasse met eigen (splitsing) gegevens. Bij een splitsing ontstaan * nieuwe percelen en er is daarom sprake van meerdere relaties. De gegevens over de splitsing zijn echter altijd voor al deze relaties gelijk. Om deze reden wordt de relatieklasse 'overgegaan in' gemodelleerd als een objecttype.
>
> — MIM 1.2, §5.6 (niet-normatief, voorbeeld)

**Eigen voorbeeld.** Een arbeidsrelatie tussen één Persoon en één Werkgever met een begindatum en een functie: de gegevens horen bij die ene relatie. Dat is een relatieklasse.

## 6. Wordt vaak verward met

- **Objecttype.** Zie `onderscheidingen/relatieklasse-vs-objecttype.md`.
- **Relatiesoort.** Zonder eigen gegevens is het een relatiesoort.

## Zie ook

- Letterlijke tekst: `python3 scripts/mim.py paragraaf 5.6`
