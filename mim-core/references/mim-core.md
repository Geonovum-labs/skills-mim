# MIM core (compact)

MIM 1.2, vastgesteld 13 June 2024. English instruction; Dutch terms are the identifiers. Official English labels: MIM §6.3.

MIM covers beschouwingsniveaus 2 (conceptueel informatiemodel) and 3 (logisch). Level 1 (begrippen) and level 4 (XML, JSON, DB, OGC API) are out of MIM. **Data (M0) is not part of MIM.** Mapping a product onto modelelementen is extra-standard work (see the interpret plugin). Generating code from a model is extra-standard work (see the implement plugin, later).

A model is always *Conceptueel* or *Logisch*, never a mix (`Informatiemodeltype`).

Reading rules that change what an element means: [`reading-rules.md`](reading-rules.md). Where the MIM text contradicts itself: [`known-ambiguities.md`](known-ambiguities.md). Where to fetch a model: [`fetch.md`](fetch.md). Compact per-element format: [`element-summary-format.md`](element-summary-format.md).

## Uitgangspunten of MIM

MIM states its own starting points (MIM 1.2, *Metamodel algemeen*). They explain why models look the way they do:

1. Every modelelement has a name and its own MIM-metaclass, by which you can recognise it anywhere.
2. Elements are explained first without any modelling language. UML and the W3C specifications (Linked Data) are *expression forms* of the same elements.
3. The description is tool-independent. (Sparx Enterprise Architect is described as an addition, because many organisations use it.)
4. **Extend, do not deviate.** Models use the metamodel uniformly; no alternative constructions for the same purpose. Own needs go into an extension, not into a different reading of a MIM element.
5. **Datatypes carry structure, not meaning.** Remove every datatype from a model and no meaning may be lost.

Consequence for reading: a MIM element means the same in every MIM-conformant model. What differs between models is the content (names, definitions, kardinaliteit), and which extensions are used.

## Reading MIM in UML and in Linked Data

The same model can be published in more than one form. Recognise the element kind in each:

- **UML (EA, XMI):** the kind is the stereotype, written like the metaclass: «Objecttype», «Attribuutsoort», «Gegevensgroeptype», «Relatiesoort», and so on. The stereotype for *Gestructureerd datatype* is spelled «Gestructuurd datatype» ([I4](known-ambiguities.md)).
- **Linked Data in the MIM vocabulary:** a model element is an *instance* of a `mim:` class in the namespace `http://modellen.mim-standaard.nl/def/mim#`, for example `vb:Schip a mim:Objecttype` with an `rdfs:label`. The kind is the `mim:` class.
- **Plain RDF / RDFS / OWL / SHACL:** MIM calls such a model conformant when it can be transformed to the MIM vocabulary with the transformation rules of the annex. The element kinds are then not stated in the model; label a kind you derive this way *inferred*. In the transformed model, a MIM element becomes a class or shape with its own URI and a link back to the MIM element (`mim:equivalent`, see [I5](known-ambiguities.md)).

A level-3 *logisch* model expressed in Linked Data is also a conceptual model (reading rule 14).

## Element kinds

| NL (EN §6.3) | When reading a model |
|---|---|
| **Objecttype** (FeatureType) | A kind of thing. Not a table. Abstract ones have no instances of their own. |
| **Attribuutsoort** (AttributeType) | Typed recorded property. Carries datatype, kardinaliteit, mogelijk geen waarde, authentiek, historie flags. |
| **Gegevensgroep / Gegevensgroeptype** | Named group of separate attributes. Often flattened in products. Multiply kardinaliteiten. |
| **Relatiesoort / Relatierol** (AssociationType / Role) | Directed bron → doel. |
| **Relatieklasse** | Relation with its own attributes; usually a link table. |
| **Externe koppeling** | Directed relation to another model's objecttype. |
| **Generalisatie** | Super/subtype; multiple inheritance allowed. Members are inherited; metagegeven *values* are not. |
| **Keuze** (Union) | XOR. The Keuze name is not a field. |
| **Constraint** | Plain-text rule; optional formal spec. The other XOR/OR vehicle. |
| **Primitief datatype** | CharacterString, Integer, Real, Decimal, Boolean, Date, DateTime, Year, Month, Day, URI, or a restriction. |
| **Gestructureerd datatype / Data-element** | One composite value; parts are not separate facts. |
| **Enumeratie / Enumeratiewaarde** | Closed list; *naam* is the value. |
| **Referentielijst / Referentie-element** | External list; structure in the model; `locatie`. |
| **Codelijst** | External list; structure not in the model; `waarde-item`. |
| **Domein / Extern / View** | Package kinds. Extern/View semantics come from the source model. |

## Metagegevens that change answers

`naam`, `alias`, `definitie`, `toelichting`, `herkomst`, `herkomstDefinitie`, `begrip`, **`populatie`**, `kardinaliteit`, `mogelijkGeenWaarde`, `identificerend`, `authentiek`, `indicatieAfleidbaar`, `indicatieClassificerend`, `heeft tijdlijn geldigheid` / `heeft tijdlijn registratie` (aliases: `indicatie materiële/formele historie`), `lengte`, `patroon`, `formeelPatroon`, `eenheid`, `indicatie in onderzoek` (extension used by some registries — keep, do not bury).

`datumOpname` is the date the element entered the **model**, not a data date.

## NL ⇄ EN (seed, §6.3)

Objecttype = FeatureType; Attribuutsoort = AttributeType; Gegevensgroeptype = AttributeGroupType; Relatiesoort = AssociationType; Relatieklasse = AssociationClass; Referentielijst = ReferenceList; Enumeratie = Enumeration; Codelijst = CodeList; Keuze = Union; Mogelijk geen waarde = Voidable; Populatie = Population; Authentiek = Indication authentic.

## MIM 1.2 vs 2.0

v1 supports 1.x only. MIM 2.0 working vocabularies reuse namespace `http://modellen.mim-standaard.nl/def/mim#` with different class names (`Attribuuttype`, `Relatietype`). If those appear, fail: convert first, do not read as 1.2.

`http://modellen.mim-standaard.nl/def/mim` was 404/500 on 2026-10-30. Do not depend on dereference of the metamodel URI.

## Serializations this pack accepts (v1)

Preference order once a **model** is identified:

1. Published RDF of *this* model at `modellen.geostandaarden.nl` (or the owner's equivalent).
2. HTML/PDF MIM catalog tables of the model owner.
3. SKOS waardelijsten.
4. Level-4 schema (JSON Schema, OGC queryables, XSD) as `derived-technical`.
5. EA XMI / MIM XML — useful when present; no parser in v1.

Fidelity labels (what kind of source the model knowledge came from): `rdf` | `catalog-prose` | `skos` | `derived-technical` | `ea-xmi`. Always state fidelity.

Never invent modelelementen. If the element summary, catalog or loaded model source does not contain it, say so. Never read raw multi-megabyte XMI/XML into context: use the element summaries of the bound model or `scripts/mim_core.py`.
