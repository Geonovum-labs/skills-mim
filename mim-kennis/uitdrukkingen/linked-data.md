---
id: linked-data
titel: MIM uitgedrukt in Linked Data
bron: ["1.9", "1.9.1", "1.9.2", "1.9.3", "4.1", "4.2", "4.3", "4.4", "6.4", "6.4.1", "6.4.3", "6.4.4"]
mim-versie: "1.2"
status: normatief
---

# MIM in Linked Data

**In het kort.** In Linked Data is MIM een RDF-vocabulaire (klassen en eigenschappen, prefix `mim:`) plus SHACL-shapes die controleren of een model goed is opgebouwd. Een informatiemodel in de MIM-vocabulaire bestaat uit *instanties* van MIM-klassen (bijvoorbeeld `vb:Schip a mim:Objecttype`). Om er echte Linked Data mee te maken, moet het model eerst worden getransformeerd naar een RDFS/OWL/SHACL-ontologie (bijlage §6.4).

## Twee bestanden

> 1. de RDF vocabulaire, met de (meta)klassen en (meta)eigenschappen;
> 2. de RDF Shapesgraph, met "shapes", de structuur die gelden op het gebruik van de klassen en eigenschappen.
>
> — MIM 1.2, §4.2 (normatief)

Namespaces (§4.2.1):

| Prefix | Namespace |
|---|---|
| `mim:` | `http://modellen.mim-standaard.nl/def/mim#` |
| `shape:` | `http://modellen.mim-standaard.nl/def/mim-shapes#` |

Kopieën uit de werkbron (MIM-Werkomgeving, master): `assets/mim.ttl` en `assets/mim-shapes.ttl`. Let op: dat zijn de bestanden uit de werkomgeving, niet uit de gepubliceerde DEF-versie zelf.

## Omzettingsregels (§4.2, eigen samenvatting)

- Elke MIM-metaclass wordt een `owl:Class` en krijgt een `sh:NodeShape`.
- Een metagegeven met een gewone waarde (tekst, getal, boolean) wordt een `owl:DatatypeProperty`.
- Een metagegeven dat naar een ander modelelement verwijst, wordt een `owl:ObjectProperty`.
- `rdfs:label` bevat de naam, `rdfs:comment` de definitie.
- LD gebruikt alleen de rolnaam van een binding, bijvoorbeeld `mim:attribuut` in plaats van "heeft attribuut" (§4.2).

## Een informatiemodel is geen ontologie

> Op diezelfde manier levert het toepassen van het MIM in RDF geen ontologie of vocabulaire waarin RDF kan worden uitgedrukt: slechts het informatiemodel zelf is op deze manier in RDF uitgedrukt. Voor de vertaalslag naar een ontologie is een afzonderlijke transformatie nodig.
>
> — MIM 1.2, §4.1 (normatief)

```turtle
vb:Schip a mim:Objecttype;            # het modelelement (MIM-instantie)
  rdfs:label "Schip"@nl .

vbo:Schip a rdfs:Class;                # na transformatie: een klasse
  mim:equivalent vb:Schip .
vb:Pakjesboot12 a vbo:Schip .          # een object (M0)
```

Voorbeeld naar §4.1. In §1.9.3 staat hetzelfde voorbeeld met `rdfs:seeAlso` in plaats van `mim:equivalent` (onduidelijkheid I5).

## Wanneer voldoet een LD-model aan MIM?

> 1. Het informatiemodel is uitgedrukt in de MIM vocabulaire, zoals beschreven in 4. Metamodel in Linked Data (LD);
> 2. Het informatiemodel is uitgedrukt in RDF, RDFS, OWL en SHACL en is te transformeren naar de MIM vocabulaire op basis van de transformatieregels beschreven in bijlage, 6.4 Transformatie MIM - RDFS/OWL/SHACL.
>
> — MIM 1.2, §1.9.3 (normatief)

## Transformatie naar RDFS/OWL/SHACL (§6.4)

De transformatie is beschreven als SPARQL-regels en is omkeerbaar (§6.4.1, §6.4.10). Overzicht van de belangrijkste vertalingen (§6.4.4.1, §6.4.4.2):

| MIM | Wordt |
|---|---|
| `mim:Objecttype`, `mim:Gegevensgroeptype` | `owl:Class` + `sh:NodeShape` |
| `mim:Attribuutsoort`, `mim:DataElement` | `owl:DatatypeProperty` of `owl:ObjectProperty` + `sh:PropertyShape` |
| `mim:Relatiesoort`, `mim:ExterneKoppeling`, `mim:Relatierol` | `owl:ObjectProperty` + `sh:PropertyShape` |
| `mim:Generalisatie` | `rdfs:subClassOf` |
| `mim:Relatieklasse` | `rdf:Statement` |
| `mim:Enumeratie` | `owl:Class` + `sh:NodeShape` + `skos:ConceptScheme` |
| `mim:PrimitiefDatatype` | `rdfs:Datatype` |
| `mim:GestructureerdDatatype` | `sh:NodeShape` |
| `mim:Keuze` | `sh:xone` met `rdf:List` |
| `mim:Domein` | `owl:Ontology` |
| `mim:Extern`, `mim:View` | `owl:imports` |
| `mim:naam` → `rdfs:label`; `mim:definitie` → `rdfs:comment`; `mim:kardinaliteit` → `sh:minCount`/`sh:maxCount`; `mim:formeelPatroon` → `sh:pattern` | |

URI's: de URI van een element volgt uit `mim:basisUri` van zijn package en de naam; zonder basis-URI geldt een `urn:modelelement:`-default (§6.4.2, §2.4.2.1). Bij een view krijgen vocabulaire-elementen de URI's van het externe model en shapes de basis-URI van het eigen model (§6.4.3).

## Conceptueel of logisch in LD

In Linked Data is er nauwelijks verschil tussen een conceptueel en een logisch model (§1.9). Voor modellen die zowel UML als LD nodig hebben, adviseert MIM het type conceptueel (§1.9).

## Tooling

MIM-modellen in LD maak je met Enterprise Architect en Imvertor (UML naar LD), of direct in OWL en SHACL met bijvoorbeeld Protégé of PoolParty, en vertaal je terug met de SPARQL-regels uit §6.4.10 (§4.4).

## Zie ook

- `uitdrukkingen/uml.md`, `bekende-onduidelijkheden.md` (I4, I5 en de LD-tabellen)
- Letterlijke tekst: `python3 scripts/mim.py paragraaf 4.1` en `python3 scripts/mim.py paragraaf 6.4.4 --met-sub`
