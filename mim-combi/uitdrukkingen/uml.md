---
id: uml
titel: MIM uitgedrukt in UML
bron: ["1.8", "3", "3.1", "3.1.1", "3.1.2", "3.1.3", "3.2", "3.3", "3.3.1", "3.3.2", "3.3.3", "2.1"]
mim-versie: "1.2"
status: normatief
---

# MIM in UML

**In het kort.** MIM kun je uitdrukken in UML met een UML-profiel: elk MIM-modelelement wordt een UML-element met een stereotype, en metagegevens worden tagged values. UML is daarbij alleen de notatie. De betekenis komt uit MIM, niet uit UML.

## Geen semantiek uit UML

> Nadrukkelijk moet daarbij worden vermeld dat het MIM metamodel **geen** semantiek overneemt van UML. Met het uitdrukken van het MIM metamodel in een UML profiel wordt het alleen mogelijk gemaakt om, zonder verlies van de originele semantiek van het MIM, een MIM model uit te drukken in UML.
>
> — MIM 1.2, §1.8 (normatief)

Eigen uitleg. Gevolg voor antwoorden: leg een MIM-begrip nooit uit met de UML-betekenis. Een relatiesoort is niet "een UML-associatie", een objecttype is niet "een UML-klasse". Ze worden er alleen mee genoteerd. Voorbeelden van waar het verschil uitmaakt: aggregatietype in MIM heeft eigen waarden en betekenis (§2.4.3.23); generalisatie is in MIM alleen gedefinieerd voor objecttypen en datatypen (§2.3.3.1).

## Uitgangspunten

> - Eén stereotype per modelelement hanteren.
> - Twee verschillende stereotypen hebben nooit dezelfde betekenis.
>
> — MIM 1.2, §3.1 (normatief)

MIM gebruikt UML 2.5 als basis en breidt UML alleen uit met stereotypes, tagged values en constraints, zonder bestaande UML-metaclasses te wijzigen (§1.8, §3.1).

## Vier lagen (OMG)

| Laag | Wat | In MIM |
|---|---|---|
| M3 | MOF: taal om metamodellen te definiëren | - |
| M2 | metamodellen zoals UML | MIM als UML-profiel |
| M1 | modellen | het informatiemodel (conceptueel of logisch) |
| M0 | objecten en data | Jan, Pand 0123 |

Bron: §1.8 (tabel en tekst).

## Stereotypen en UML-metaclasses (§3.1)

| MIM-metaclass | Stereotype | UML 2.5 | In Enterprise Architect |
|---|---|---|---|
| Objecttype | «Objecttype» | Class | Class |
| Attribuutsoort | «Attribuutsoort» | Property | Attribute |
| Gegevensgroep | «Gegevensgroep» | Property | Attribute |
| Gegevensgroeptype | «Gegevensgroeptype» | Class | Class |
| Generalisatie | «Generalisatie» | Generalization | Generalization |
| Relatiesoort | «Relatiesoort» | Association | Association |
| Relatieklasse | «Relatieklasse» | Association én Class | Associationclass |
| Primitief datatype | «Primitief datatype» | Primitive Type | Datatype |
| Gestructureerd datatype | «Gestructuurd datatype» (zo in de tabel; zie I4) | Datatype | Datatype |
| Data-element | «Data-element» | Property | Attribute |
| Enumeratie | - (geen stereotype) | Enumeration | Enumeration |
| Enumeratiewaarde | - (geen stereotype) | EnumerationLiteral | EnumerationLiteral |
| Referentielijst | «Referentielijst» | Datatype | Datatype |
| Referentie-element | «Referentie-element» | Property | Attribute |
| Codelijst | «Codelijst» | Datatype | Datatype |
| Constraint | - (geen stereotype) | Constraint | Constraint |
| Keuze | Keuze | Class, Datatype of Property | Class, Datatype of Attribute |
| Relatierol | «Relatierol» | Property | AssociationEnd |
| Externe koppeling | «Externe koppeling» | Association | Association |
| Informatiemodel, Domein, Extern, View | «Informatiemodel», «Domein», «Extern», «View» | Package | Package |

Datatype zelf heeft geen stereotype; het is abstract (noot bij §3.1.1).

## Metagegevens in UML

Per stereotype staat een tabel in §3.2 met per metagegeven de kardinaliteit en hoe het in UML en EA wordt vastgelegd (UML-eigenschap of tagged value). Die tabellen staan in de kennisbank als data: `data/metagegevens.json`, en per element in `modelelementen/`.

Enkele UML-specifieke uitdrukkingen (§3.2, §5.5.3, §5.9):

| Metagegeven | In UML |
|---|---|
| Identificerend (attribuutsoort) | `isId = true` |
| Identificerend (relatiesoort) | stereotype «id» |
| Indicatie abstract object | `isAbstract`; naam cursief |
| Indicatie afleidbaar | `isDerived` |
| Alias | Alias van een NamedElement; bij EnumerationLiteral alleen voor Code |

## Tooling

- **MIM-toolbox**: een UML-profiel voor Sparx Enterprise Architect, gemaakt door de MIM-beheerder. Gebruik is niet verplicht. Uitbreiden mag, wijzigen niet (§3.3.1, §3.3.2).
- **Imvertor**: open source tool die onder andere controleert of een model aan MIM voldoet (§3.3.3).

EA wordt in MIM genoemd omdat veel organisaties het gebruiken; MIM zelf is toolonafhankelijk (§2.1).

## Zie ook

- `uitdrukkingen/linked-data.md`, `onderwerpen/relatiemodellering.md`
- Letterlijke tekst: `python3 scripts/mim.py paragraaf 3.1 --met-sub`
