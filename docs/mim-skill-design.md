---
cursor:
  subagentId: "bc-5a62d66a-ba4a-5f6e-9f4f-873ce61ea31e"
---

# Design: an agent skill for MIM (Metamodel Informatiemodellering)

Task MS-1. Research date: 2026-10-30. Status: design proposal for owner review. No repo has been created.

**Legend.** **[V]** = verified in a source I read during this research (source id in brackets, list in Appendix A). **[P]** = my proposal. **[U]** = from background knowledge or an unchecked inference; must be verified before it is relied on.

---

## 0. Summary

### Headline design [P]

One skill, `geonovum-mim-interpret`, in a new repo `Geonovum/skills-mim`. It helps an agent **consume** MIM-conformant models, not author them. It is model-first:

1. **Find** the model behind a dataset or API.
2. **Digest** it with a bundled script. A 3 MB XMI/XML file becomes a compact, queryable digest; the agent never reads raw model files.
3. **Map** data fields to model elements.
4. **Interpret** values with MIM-specific rules: kardinaliteit vs. *mogelijk geen waarde*, waardelijst kinds, Keuze (XOR), historie, abstract types, partial dates, leading zeros.
5. **Answer** with provenance (model, version, element) and a stated confidence.

- **Structure.** Progressive disclosure per the Agent Skills spec [S16]: a short `SKILL.md`, `references/` for MIM concepts, interpretation rules, serializations and the model catalog, `scripts/mim.py` (stdlib-only Python) for fetch, digest, find, card, values, map and check, and `evals/` with with/without-skill benchmarks.
- **Serialization strategy.** Normalize to one internal "MIM digest" and write adapters. **MVP adapters: MIM XML and Enterprise Architect XMI.** These are the formats Geonovum actually publishes (see 1.2). Then SKOS waardelijsten, JSON Schema/OpenAPI from the data side, and MIM RDF/Turtle. The standard specifies the RDF form, but I found no published instance (see 1.2).
- **Conventions.** Follow the sibling precedent `Geonovum/skills-nl-sbb` [S13]: plugin manifests, `publiccode.yml`, `DISCLAIMER.md`, `nl.gov.*` metadata, status `concept`, EUPL-1.2. Distribute via the developer.overheid.nl skills-marketplace [S14].

### Top open questions for the owner (details in section 6)

1. **Machine-readable model supply (biggest dependency).** The skill is only as useful as the models an agent can reach. Several flagship models are not machine-parseable at their published locations: IMKAD only as `.EAP`, IMBAG as prose HTML, and the Kadaster BAG/BRK ontology URIs return 404 (1.4). Can Geonovum/Kadaster commit to publishing MIM XML/XMI (or MIM-RDF) for the key models? If not, the skill's catalog stays small.
2. **Scope.** Consume-only (recommended) versus also reviewing/validating models. The existing `geo-model` skill in `skills-geo` [S15] already covers some authoring-oriented MIM guidance and contains errors (see 1.5). Replace it, coordinate with it, or ignore it?
3. **MIM 2.0.** Version 1.2 is the published standard. MIM 2.0 (CIM/LGM split, different vocabulary but the *same namespace*) is in working documents. Support 1.2 only in the MVP and detect 2.0 (recommended), or build for 2.0?
4. **Language.** English instructions with Dutch MIM terms verbatim (recommended, test it as an eval variable) versus fully Dutch like the sibling skills.
5. **Names and ownership.** `Geonovum/skills-mim` / plugin `geonovum-mim` / skill `geonovum-mim-interpret`. Who maintains it, and what is the `review-by` cadence?
6. **Licence of fixtures and derived content.** EUPL-1.2 for skill and scripts. MIM text is CC-BY-4.0, and Imvertor is GPL-3.0, so do not copy Imvertor code or XSDs into the repo without a legal check.

---

## 1. Research findings (facts)

### 1.1 The standard [V]

- **MIM 1.2** is the current "Vastgestelde versie" (Geonovum Standaard, **13 June 2024**), at `docs.geostandaarden.nl/mim/mim/` (latest) and `…/def-st-mim-20240613`. Earlier versions are listed at `docs.geostandaarden.nl/mim/`. Licence CC-BY-4.0. Maintainer: Geonovum with Kadaster; helpdesk `mim@geonovum.nl`. [S1, S2]
- **Four consideration levels (beschouwingsniveaus).** Level 1 is a model of concepts (out of MIM scope). Level 2 is a *conceptual* information model. Level 3 is a *logical* information/data model. Level 4 is a physical or technical model (XML, JSON, DB; out of scope). MIM covers levels 2 and 3. The metagegeven *Informatiemodeltype* is "Conceptueel" or "Logisch". [S1 §1.6, §2.4.1.2]
- **Three expressions of the same metamodel:** abstract (ch. 2), UML profile (ch. 3, MIM toolbox for Sparx EA, MDG file), and Linked Data (ch. 4). Informatiemodellen are M1-layer models; **data (M0) is not part of MIM**. [S1 §1.8–1.9, ch. 2–4]
- **Linked Data form** [S1 ch. 4, §6.4]
  - Namespace `http://modellen.mim-standaard.nl/def/mim#` (prefix `mim`), shapes in `…/def/mim-shapes#`.
  - A model element is an *instance* of a `mim:` class, e.g. `vb:Schip a mim:Objecttype; rdfs:label "Schip"@nl`. To describe actual data you must "promote" it to a class (`vbo:Schip a rdfs:Class; mim:equivalent vb:Schip`).
  - A reversible SPARQL-based transformation MIM ⇄ RDFS/OWL/SHACL is specified (§6.4). Any RDFS/OWL/SHACL model that transforms back is "MIM-conformant".
  - Property-shape URIs follow `{shape-ns}#{CamelCase(owner)}-{camelCase(name)}`.
- **Tooling named in the standard:** MIM toolbox for Enterprise Architect (§3.3.1) and **Imvertor** (open source; checks MIM conformance and transforms EA → Linked Data; §3.3.3, §4.4).
- **Extensions.** Organisations may add an *extension* (extra metaclasses/metagegevens, or declare unused ones), managed outside MIM. It may not replace MIM constructs. The metagegeven *MIM-extensie* names it (examples in the standard: "Kadaster", "NEN3610:2022"). [S1 §1.10, §2.4.1.5]
- **Official English translation of terms** (§6.3): Objecttype→FeatureType, Attribuutsoort→AttributeType, Gegevensgroeptype→AttributeGroupType, Relatiesoort→AssociationType, Referentielijst→ReferenceList, Enumeratie→Enumeration, Keuze→Union, Mogelijk geen waarde→Voidable, and so on. A full English MIM 1.2 text exists in `MIM-Werkomgeving/MIM-1.2-Engels/`. [S1, S3]

### 1.2 How MIM models are actually serialized and published [V unless noted]

| Form | Evidence | Machine-usable by an agent? |
|---|---|---|
| **EA XMI 1.1 / UML 1.3** (stereotypes = MIM metaclasses, tagged values = metagegevens) | `register.geostandaarden.nl/informatiemodel/imgeo/2.2/IMGeo.xmi` (3.25 MB); `NEN3610-2022-template-20221116.xmi`; `Geonovum/IMGeoMIM/IMGeo2.2-MIM-{conceptueel,logisch}.xml` (2.8 and 3.4 MB; these are EA XMI despite the name) [S5, S6] | Yes, with a dedicated parser. Quirks: windows-1252, `<memo>` placeholder tag values, tool noise (`$ea_xref_property`, `styleex`…). |
| **EA `.EAP`/`.eapx`** (binary) | IMKAD 2.3.1 is published **only** as `IMKAD-23.1.EAP`; IMGeoMIM `IMGeo.eapx` is 75 MB [S5, S6] | No. |
| **"MIM format" XML** (`mim-core/1.2`, `mim-ext/1.0`, `mim-ref/1.0` namespaces; root `mim:Informatiemodel`) | Imvertor-Maven ships XSDs (v1, v2/1.1, 1.1.1, 1.2) and a `Fietsenwinkel.xml` sample; `geonovum-allemodellen` sets `createmimformat=yes`, `mimformattype=xml`, and its `mim2report.xsl` consumes `mim-core/1.1` [S7, S8] | Yes. Cleanest source. The standard itself does **not** specify it; it is Imvertor's serialization (see risk R-12). |
| **MIM RDF/Turtle** | Specified normatively (S1 ch. 4). `Geonovum/mim-ld` has `example/mim.ttl` that is **0 bytes**, plus MIM 2.0 `mim-ontologie.ttl`. I found **no published MIM-RDF instance** of a real model. `http://modellen.mim-standaard.nl/def/mim` returns **404** (2026-10-30). [S4] | Parsable in principle (rdflib), but nothing to feed it yet. |
| **JSON Schema / OpenAPI / SHACL / XSD** *derived* from models (level 4) | `Geonovum/imev` (JSON Schema 3.0.x + OAS + example files); `bestuurlijke-gebieden-lm/schemas/LGM-BG.schema.json` (`$id http://modellen.geostandaarden.nl/def/bg#`, `$anchor` per type, enums); register has `jsonschema/`, `gmlapplicatieschema/`, `xmlschema/`, `shacl/` (only `nl-sbb`) [S5, S9, S10] | Yes, but **lossy**: no definitions or metagegevens beyond what the generator copied. Useful as a bridge from data to model. |
| **Waardelijsten as SKOS RDF** | `Geonovum/IMGeo/waardelijst/20200701/imgeo.rdf` (268 KB); register `waardelijst/{imgeo,imkad,imkl,geobag,imow,…}` [S5, S18] | Yes (RDF/XML). |
| **Begrippen (level 1) as SKOS via Skosmos** | `catalogus.kadaster.nl` (vocabs `bag`, `brk`, `brt`, `tr`…). `GET /rest/v1/search?vocab=bag&query=pand*&lang=nl` returns JSON-LD; `GET /rest/v1/data?uri=<concept>` with `Accept: text/turtle` returns the concept with `rdfs:comment` definition and broader/narrower. Verified for `bag:Pand`. [S12] | Yes. Good for domain definitions. |
| **HTML catalogs / ReSpec documents** | `geonovum-allemodellen/data/*-cat.respec.html` (Imvertor-generated, up to 1.4 MB); IMBAG catalogus (`imbag.github.io/catalogus`, prose) [S8, S17] | Poorly; prose or HTML, not structured. |
| **Stelselcatalogus-style JSON** | `imev/informatiemodel/IMEV_3.0_Stelselcatalogus_*.json` (SKOS concepts with `uri`, `naam`, `definitie`, `isBrederDan`…) [S9] | Yes (begrippen). |

**Finding that shapes the MVP:** published, parseable MIM *information models* are mostly **EA XMI** (and MIM XML where Imvertor was run). The data-side bridge is usually **JSON Schema / OGC API queryables / SKOS lists**. MIM-RDF is spec'd but I found no real example.

### 1.3 Real worked example: data side vs model side

PDOK BAG OGC API v2 (`api.pdok.nl/kadaster/bag/ogc/v2`): collections `pand`, `verblijfsobject`, `ligplaats`, `standplaats`, `woonplaats`, `adres`. `pand` queryables: `identificatie`, `bouwjaar` (integer), `status` (string), `gebruiksdoel`, `aantal_verblijfsobjecten`, `documentdatum`, `documentnummer`, `geometry`. A real feature [V]:

```json
{"identificatie":"0003100000117485","bouwjaar":1991,"status":"Pand in gebruik",
 "geconstateerd":"N","gebruiksdoel":"woonfunctie","aantal_verblijfsobjecten":15,
 "documentdatum":"2010-07-20","documentnummer":"FB 2010/PANDEN001",
 "rdf_seealso":"http://bag.basisregistraties.overheid.nl/bag/id/pand/0003100000117485",
 "verblijfsobject.href":["https://api.pdok.nl/…/verblijfsobject/items/…", "…"]}
```

An agent without a model has to guess:

- Is `status` a closed list? What does "Pand in gebruik" vs. "Pand buiten gebruik" mean?
- Does `geconstateerd = "N"` mean "not observed on the ground"?
- Why does a `pand` carry `gebruiksdoel` and `aantal_verblijfsobjecten`? **[U]** In IMBAG, `gebruiksdoel` is a Verblijfsobject attribute, so the API denormalizes or derives it. `aantal_verblijfsobjecten` is probably a derived value (*indicatie afleidbaar*). `bouwjaar` presumably corresponds to the model's "oorspronkelijk bouwjaar". These are exactly the cases where a model lookup plus a mapping step prevents misinterpretation.
- What is the relation to Verblijfsobject (the `.href` array) and its cardinality?

Reality check [V, 2026-10-30]: the `rdf_seealso` URI (`bag.basisregistraties.overheid.nl/bag/id/pand/…`, also with `Accept: text/turtle` and `application/ld+json`) returns **404 (problem+json)**, and `…/def/bag` and `brk…/def/brk` also return 404. The Kadaster *begrippen* catalog (Skosmos) works. So the skill **cannot assume dereferenceable ontology URIs**. It needs a curated catalog and fallbacks.

### 1.4 Machine-readability of the models agents will be asked about [V]

| Model / registry | Best machine-readable thing I could find | Notes |
|---|---|---|
| IMGeo / BGT 2.2 | EA XMI (register + IMGeoMIM), SKOS waardelijsten (`imgeo.rdf`), GML/XSD | 38 Objecttypen, 59 Enumeraties, 344 Enumeratiewaarden in the logical MIM XMI. Good MVP fixture. |
| NEN 3610:2022 | EA XMI template + MIM-extension MDG; LD profile repo `NEN3610-Linkeddata` | Basis for most sector models. |
| IMEV 3.0 | JSON Schema, OAS, example JSON, Stelselcatalogus (begrippen) JSON | No MIM XMI found in the repo tree. |
| Bestuurlijke Gebieden (LGM) | JSON Schema (`LGM-BG*.schema.json`) | Generated from a logical model. |
| BAG (IMBAG) | PDOK OGC API schema; Kadaster Skosmos begrippen; prose catalogus | No MIM-serialized model found. |
| BRK (IMKAD) | `.EAP` only; Skosmos begrippen | Not parseable without EA. |
| MIM itself | MIM 2.0 working `mim-ontologie.ttl`, `mim-cim.ttl`; 1.2 spec HTML | Meta-level only. |

### 1.5 Existing agent-skill precedents [V]

- **`Geonovum/skills-nl-sbb`** [S13] (EUPL-1.2; created 2026-09). Layout: `skills/<skill>/SKILL.md` + `reference.md`, `conflicts.md`, `bronnenlijst.md`, a `.ttl` extension; `.claude-plugin/`, `.cursor-plugin/`, `.plugin/` manifests generated by `scripts/generate_plugin.py`; Changesets for versioning; `publiccode.yml`; `DISCLAIMER.md`; CONTRIBUTING, SECURITY, CODE_OF_CONDUCT; release workflow. SKILL.md frontmatter adds `license`, `allowed-tools`, and `metadata: nl.gov.status | review-by | source | source-license | category | tags | bundle | generated-with`. Status ladder: `concept` until expert review, a published review procedure with acceptance criteria, and a **test on ≥2 assistants (one open-source or European)**. Banner at the top of SKILL.md states the skill is informative and the standard is leading. Hard rule: "never modify the user's source file."
- **`developer-overheid-nl/skills-marketplace`** [S14]: central catalog (Claude Code, Codex, Cursor) with a `geo` plugin (`skills-geo`).
- **`skills-geo/skills/geo-model`** [S15] (AI-generated, status concept, dated 2025-02) covers NEN 3610 and "MIM modelleringsregels" for *authoring* and generating conformant exchange data. It misstates MIM in places, e.g. it calls MIM "Niveau 1" a "Conceptueel model" (in MIM, level 1 is begrippen and level 2 is conceptueel), and lists stereotypes like `<<datatype>>`, `<<constraint>>`, `<<codelijst>>` loosely. **Our skill is complementary (consumption/interpretation) and should be more exact.** Coordinate with its maintainers.
- **Agent Skills spec** [S16]: `name` ≤64 chars, lowercase/digits/hyphens, equals the directory name; `description` ≤1024 chars (what + when); optional `license`, `compatibility` (≤500), `metadata`, `allowed-tools` (experimental); SKILL.md body recommended <5000 tokens, split the rest into `references/`; `scripts/` should be self-contained with helpful errors; evals in `evals/evals.json`, run with and without skill, `timing.json`/`grading.json`/`benchmark.json`.

---

## 2. Scope, users, use cases

### 2.1 Goal [P]

Make an agent **more correct and more efficient** at answering questions over published Dutch open data by using the information model that describes it: grounded definitions, cardinality, datatypes, code lists, relations and history semantics, instead of guesses from column names.

### 2.2 Users [P]

- **Primary:** AI agents (coding agents, analyst agents, chat assistants with tools) used by data users: data journalists, municipal and national analysts, GIS developers, researchers, civic-tech developers.
- **Secondary:** data publishers and modellers checking whether their data is consistently described (light, via `check`), and Geonovum itself (a showcase for model-aware agents).
- **Non-goals:** authoring MIM models; certifying MIM conformance (Imvertor does this); replacing the standard; processing personal data (BRK/BRP person data is out of scope; see risk R-7).

### 2.3 Concrete use cases and example questions [P]

| # | Use case | Example question (NL/EN) | What the model contributes |
|---|---|---|---|
| UC1 | Explain a field/code | "Wat betekent `status = Pand in gebruik` in BAG-panden en welke andere waarden zijn er?" | Attribuutsoort definition; type Enumeratie/Referentielijst; value list with codes and definitions. |
| UC2 | Null/optional semantics | "`overlijdensdatum` is leeg. Leeft deze persoon nog?" / "Is `bouwjaar` verplicht?" | `kardinaliteit` plus *mogelijk geen waarde* (four combinations, S1 §5.11). Blank is not "does not exist". |
| UC3 | Correct query | "Alle panden gebouwd na 2000 die in gebruik zijn, als CQL2/SQL/SPARQL." | Field name ↔ attribuutsoort mapping, exact enum literal, datatype (Integer vs Year vs DMO), cardinality. |
| UC4 | Map unknown dataset to model | "Hier is een CSV/GeoJSON; welke kolommen horen bij welke modelelementen?" | Candidate mapping with scores, flags for unmapped columns, derived or denormalized columns. |
| UC5 | Relations | "Hoe hangen Pand en Verblijfsobject samen, en kan een VBO in meerdere panden liggen?" | Relatiesoort direction (*bron/doel*), `kardinaliteit` and `kardinaliteitBron`, Relatieklasse. |
| UC6 | Inheritance | "Welke attributen heeft een Wegdeel, inclusief die van het supertype?" | Generalisatie (multiple inheritance, abstract supertypes). |
| UC7 | History/validity | "Is dit het actuele gegeven? Welke tijdlijnen bestaan er?" | *heeft tijdlijn geldigheid / registratie* (formerly materiële/formele historie): whether history is kept and queryable. Field names are *not* standardized (S1 §5.8.1). |
| UC8 | Trust/authority | "Welke gegevens zijn authentiek?" | Metagegeven *Authentiek* (Authentiek/Basisgegeven/Wettelijk gegeven/Landelijk kerngegeven/Overig). |
| UC9 | Validation of values | "Zijn deze waarden geldig volgens het model?" | `lengte`, `patroon`, `formeel patroon` (regex), enum membership, min/max values, Keuze XOR. |
| UC10 | Joining datasets | "Welke kolom is de sleutel om dit met BAG te koppelen?" | `identificerend`, shared `begrip` or `identificatie` URI, NEN3610ID structure. |
| UC11 | Model discovery | "Welk informatiemodel hoort bij deze dataset/API?" | Catalog and pointers (`rdf_seealso`, `dct:conformsTo`, `$id`, GML schemaLocation). |
| UC12 | Honest uncertainty | "Interpreteer dataset X." (no model exists) | The skill makes the agent say so, offer clearly-labelled inference, and not invent element names. |

---

## 3. MIM concepts an agent must know (compact reference)

Everything in 3.1–3.3 is [V] from S1 unless marked. Section refs are to the MIM 1.2 text.

### 3.1 Element kinds

| NL (EN, S1 §6.3) | Meaning, and what it implies when reading data | MIM XML element [S7] | MIM RDF class `mim:` [S1 ch.4] | EA stereotype [S6] |
|---|---|---|---|---|
| **Informatiemodel** | Root package. Metagegevens: informatiedomein, informatiemodeltype (Conceptueel/Logisch), relatiemodelleringstype (*Relatiesoort leidend* / *Relatierol leidend*), **MIM-versie**, MIM-extensie, MIM-taal, Basis-URI, tekstopmaak. | `mim:Informatiemodel` | `Informatiemodel` | (package) |
| **Domein / Extern / View** (packages) | Domein = coherent part of the model. **Extern** = unchanged reuse of another party's elements (e.g. NEN3610ID). **View** = locally relevant subset of another model's types. Semantics of Extern/View elements come from the source model (check *herkomst*). | `mim:Domein`, `mim:Extern`, `mim:View` | same | `Domein` |
| **Objecttype** (FeatureType) | A kind of real-world thing relevant in the domain. **Not a table**: the mapping to records/entities is an implementation interpretation (§2.3.2.1). Abstract objecttypes never occur as concrete objects. | `mim:Objecttype` (+`indicatieAbstractObject`) | `Objecttype` | `Objecttype` |
| **Attribuutsoort** (AttributeType) | Typed property whose values are recorded. Carries datatype (`type`), `kardinaliteit`, `lengte`, `patroon`, `formeelPatroon`, `mogelijkGeenWaarde`, `identificerend`, `authentiek`, `indicatieAfleidbaar`, `indicatieClassificerend`, history flags, min/max values, `eenheid`. | `mim:Attribuutsoort` | `Attribuutsoort` | `Attribuutsoort` |
| **Gegevensgroep / Gegevensgroeptype** | A named group of attributes that belong together (change together). The group is *not* itself one attribute value. Often flattened to columns or nested objects. Effective cardinality = group cardinality × attribute cardinality (§2.4.3.14). | `mim:Gegevensgroep`, `mim:Gegevensgroeptype` | same | `Gegevensgroep`, `Gegevensgroeptype` |
| **Relatiesoort** (AssociationType) / **Relatierol** | A *directed* property from **bron** (owner) to **doel**. `kardinaliteit` = how many targets per source; `kardinaliteitBron` = how many sources per target (usually *not* visible in data, §2.4.3.15). Model chooses *soort leidend* or *rol leidend*. | `mim:Relatiesoort`, `mim:relatierollen/mim:Doel` | `Relatiesoort`, `Relatierol` | `Relatiesoort` |
| **Relatieklasse** | A relation with its own attributes (exists only while both ends exist). Usually a join/link table in data. | `mim:Relatieklasse` | `Relatieklasse` | `Relatieklasse` |
| **Externe koppeling** | Directed relation to an object type in another model. | `mim:ExterneKoppeling` | `ExterneKoppeling` | `Externe koppeling` |
| **Generalisatie** | Super/subtype (objecttypes *and* datatypes); multiple inheritance allowed (*mixin* flag). Subtypes inherit attributes and relations. Metagegeven *values* are not inherited across metaclasses (§2.4.3). | `mim:GeneralisatieObjecttypen`, `…Datatypen`, `mim:supertype` | `Generalisatie` | UML generalization |
| **Keuze** (Union) | Exactly one of several alternatives (XOR): datatypes, attributes, relation targets, or relations. The Keuze itself is **not** a data field and often has an arbitrary name. | `mim:Keuze` (`keuzeDatatypen`, `keuzeAttributen`, `keuzeRelatiedoelen`) | `Keuze*` | `Keuze` |
| **Constraint** | Plain-text rule (optional formal spec) over one or more elements. | `mim:Constraint` | `Constraint` | `Constraint` |
| **Primitief datatype** | Standard (CharacterString, Integer, Real, Decimal, Boolean, Date, DateTime, Year, Month, Day, URI) or self-defined restriction (via generalisatie + patroon). | `mim:PrimitiefDatatype` | `PrimitiefDatatype` | `Datatype` |
| **Gestructureerd datatype / Data-element** | One composite *value* (e.g. Bedrag = som + valuta); its parts are not separate facts and have no separate history. | `mim:GestructureerdDatatype`, `mim:DataElement` | same | `Gestructureerd datatype`, `Data element` |
| **Enumeratie / Enumeratiewaarde** | Static closed list, changed only by model change. The value *name* is the value; the optional `code` is a documentation code. | `mim:Enumeratie`, `mim:Waarde` (+`mim:code`) | `Enumeratie`, `Enumeratiewaarde` | `Enumeratie`, `Enumeratiewaarde` (tag `Code`) |
| **Referentielijst / Referentie-element** | Externally managed list whose **structure** (elements such as code, name, dates) is described in the model; the attribute typically stores a *reference* to a row. Has `locatie` (URI/URL), `doelformaat` (e.g. SKOS, CSV). | `mim:Referentielijst`, `mim:ReferentieElement` | `Referentielijst`, `ReferentieElement` | `Referentielijst`, `Referentie element` |
| **Codelijst** | Externally managed list whose structure is *not* in the model; `waarde-item` names the field holding the value; has `locatie`, `doelformaat`, `profielspecificatie`. | `mim:Codelijst` | `Codelijst` | `CodeList` |

Note on the stereotype column: stereotype names `Objecttype`, `Attribuutsoort`, `Gegevensgroep`, `Gegevensgroeptype`, `Relatiesoort`, `Keuze`, `Datatype`, `Gestructureerd datatype`, `Data element`, `Enumeratie`, `Enumeratiewaarde`, `Domein` were observed in the IMGeo XMI files [V S6]. The others (`Relatieklasse`, `Externe koppeling`, `Referentielijst`, `Referentie element`, `CodeList`, `Constraint`, `Extern`, `View`) are taken from the standard's UML chapter and §6.3 and were not observed in a real XMI during this research [U for exact spelling].

### 3.2 Metagegevens that matter for interpretation

`naam` (technical, URI-friendly), `alias` (natural-language form; for enum values it may hold a code), `definitie` / `toelichting` / `herkomst` / `herkomstDefinitie` (provenance of the definition), `begrip` (term *or* URI of a `skos:Concept`; **not** the same as the element definition, §5.16.3), `populatie` (which objects are in scope), `kwaliteit`, `datumOpname` (date added **to the model**, not a data date), `kardinaliteit`, `mogelijkGeenWaarde`, `identificerend`, `authentiek`, `indicatieAfleidbaar`, `indicatieClassificerend`, `heeft tijdlijn geldigheid` / `heeft tijdlijn registratie` (old: `indicatie materiële/formele historie`, to be phased out in MIM 2.x), `lengte` (notation `2..80`, `3,2`), `patroon`, `formeelPatroon` (regex), `eenheid`, min/max inclusive/exclusive, `unidirectioneel`, `aggregatietype` (Geen/Compositie/Gedeeld), `identificatie`/`basisURI` (default `urn:modelelement:<model>:<package>:…`, not globally unique).

### 3.3 Interpretation rules (the "gotchas") [V from S1, framed as rules by me]

These become `references/interpretation-rules.md`; the top ~10 are summarized in SKILL.md.

1. **Model ≠ data.** An objecttype describes a real-world kind. Tables, endpoints and files may split, merge or denormalize it (§2.3.2.1, §1.5.2). Always state *implementation vs. model* when mapping.
2. **Blank is not "none".** Optional (`0..1`) means "known not to exist". *Mogelijk geen waarde = Ja* means a value may exist but be unknown (§5.11, four combinations). Never infer "does not exist" from NULL when the flag is Ja. Do not model "onbekend" as a code unless inherited from a source registry.
3. **Cardinality.** `1..1` always present; `*` unbounded. Attribute in a Gegevensgroeptype: multiply by group cardinality. Generalisatie has no cardinality (1..1 implicit).
4. **Relations are directed.** The `bron` owns the data; `kardinaliteitBron` is a model constraint usually not visible in data. Read the model's *relatiemodelleringstype* to know whether names sit on soort or rol.
5. **Inheritance.** List inherited attributes/relations when asked what a type "has". Abstract supertypes never appear as concrete rows; look for the subtypes. Multiple inheritance is possible.
6. **Waardelijst kind decides behaviour.** Enumeratie = closed and static; use the literal exactly (name is the value; code is separate). Referentielijst = external, evolving; the data may hold a reference/ID, resolve via `locatie`. Codelijst = external; only the code is relevant; `waarde-item` identifies the field.
7. **Datatypes.** Numbers with leading zeros are `CharacterString` + pattern (e.g. gemeentecode "0060"). `Real` is approximate, `Decimal` exact. `Boolean` allows true/false/1/0. **DMO** (*Datum mogelijk onvolledig*: `YYYY`, `YYYY-MM`, `YYYY-MM-DD`) and **DTMO** are national datatypes with legitimately partial dates; do not parse them as full dates. `lengte` and `patroon` are separate from the datatype and both apply.
8. **Gestructureerd datatype vs Gegevensgroep** (§5.2.2): the first is one composite value (no per-part history); the second is a set of separate attributes grouped for semantic reasons.
9. **Keuze = XOR.** Exactly one alternative present; two filled = invalid data; the Keuze name is not a field (§2.3.7.2).
10. **History.** The flags say *whether* history is kept and queryable, not *how*; field names (`beginGeldigheid`, `tijdstipRegistratie`, `voorkomen`…) are implementation choices (§5.8). Assume a snapshot may contain only current rows; verify with the dataset docs.
11. **Derived data** (`indicatieAfleidbaar`): recomputable from other elements; do not treat as independent evidence; if a derived value disagrees with its sources, trust the sources.
12. **Identificerend** attributes (or combinations, possibly including a relation) are the join/dedup keys. **Authentiek** values denote legally authoritative data.
13. **Definitions have provenance.** Use `herkomstDefinitie` and `begrip`. For `Extern`/`View` elements the source model's semantics apply. Element definition (information perspective) ≠ begrip definition (domain/legal perspective).
14. **Conceptual vs logical.** A conceptual model (level 2) may be technology-neutral, with abstract types and no technical datatypes; a logical model (level 3) is closer to implementation. Prefer the logical model when the data implements it; use the conceptual one for meaning.
15. **Order is not significant** in MIM; two models differing only in order are equivalent (§6.4.2).
16. **Version awareness.** Read *MIM-versie*, *MIM-extensie* and model version. Treat unknown extension stereotypes/tags as opaque `extensions`, not as MIM core.

### 3.4 Kernmodel vs extensies [V + P]

- **Kern** = the metaclasses and metagegevens in S1 chapters 2–4. **Extensie** = organisation-specific additions (Kadaster, NEN3610:2022, Geonovum extension in `MIM-Werkomgeving/MIM-Extensies/`). They may only add or declare things unused, never redefine core constructs [V S1 §1.10; S3].
- In serializations, extension and tool data appear as `mim-ext:Kenmerk naam="…"` (MIM XML), extra EA tagged values (e.g. `Unieke aanduiding`, `Code`, `asDictionary`), or custom stereotypes.
- [P] The parser keeps a separate `extensions` map per element and the digest surfaces the *MIM-extensie* name. The agent may use extension data but must label it ("per extension X").

### 3.5 MIM 1.2 vs 2.0 [V from S4, P for handling]

MIM 2.0 working documents (`mim-metamodel`, `mim-begrippenkader`, `mim-conceptueel` CIM, `mim-logisch` LGM, `mim-best-practices`, profiles `mim-uml`, `mim-ld`, `mim-fbm`, `mim-ontouml`, `mim-archimate`) restructure MIM into a concept framework with CIM and LGM. The 2.0 ontology file reuses the **same namespace** (`mim:`) with different terms (`mim:Attribuuttype`, `mim:Relatietype`, `mim:Rolinvulling`, `mim:waardetype`, `mim:kardinaliteit`) and states that a 1.2 model expressed in that vocabulary "can be misunderstood and must be converted first." [P] Version detection (`MIM-versie`, root namespace, class names) is mandatory; MVP supports 1.x and fails loudly on 2.0.

---

## 4. Workflows

Each workflow has: trigger → steps → outputs → failure handling. Scripts are in 5.3.

### W0. Triage [P]

*Trigger:* any question about a Dutch dataset, field, code, or "informatiemodel/MIM". Decide the question type (A concept, B element lookup, C mapping, D value interpretation, E query generation, F validation). Ask only for what is missing: which dataset/API, and whether the user already has a model file.

### W1. Discover the model [P]

Order of precedence (stop at the first hit; record which rule fired):

1. **User-supplied** model file/URL.
2. **Pointers in the data**: OGC API `rdf_seealso`/`describedby`/`conformsTo`, DCAT `dct:conformsTo`, JSON Schema `$id`, OpenAPI `info`, GML `schemaLocation`, JSON-LD `@context`.
3. **Skill catalog** `references/model-catalog.md` (+ machine copy `assets/model-catalog.json`): model id → name, versions, owner, authoritative URLs per format, licence, known-dead URLs, last verified date.
4. **Register listing** `register.geostandaarden.nl/informatiemodel/<id>/<version>/` and `/waardelijst/<id>/`.
5. **Repo search** in Geonovum or the owner's GitHub organisation (`gh api`, optional).
6. **No model found:** say so (UC12). Offer a *clearly labelled* inferred description, with no invented element names.

*Pin the version* (data release date vs model version). Prefer logical over conceptual for data work; keep the conceptual one for definitions.

### W2. Fetch [P]

`mim.py fetch <url|catalog-id>`:

- Allowlist hosts by default: `*.geostandaarden.nl`, `*.pdok.nl`, `*.kadaster.nl`, `*.overheid.nl`, `raw.githubusercontent.com/Geonovum/*`, `github.com/Geonovum/*`. User can extend via `--allow`.
- Cache under `~/.cache/geonovum-mim/<sha256>/`, record URL, retrieval time, sha256, size; **never print the file**.
- Detect format (sniff root element / `XMI` / `@prefix mim:` / `$defs`) and report it.
- On 404/timeout: try catalog alternates (e.g. GitHub raw), then fail with an actionable message.

### W3. Parse into a "MIM digest" [P]

`mim.py digest <file> -o digest.json` normalizes to one schema (Appendix C) regardless of source:

- **mim-xml:** straightforward XPath; resolve `mim-ref:*Ref xlink:href="#id"`.
- **ea-xmi:** map stereotypes to MIM kinds, tagged values to metagegevens, UML associations/generalizations to relations; handle windows-1252, `<memo>` placeholders, noise tags; keep unmapped tags under `extensions`.
- **mim-rdf (Phase 2):** rdflib; `mim:` classes/properties as in S1 ch. 4; version-gated (1.2 only).
- **json-schema/OpenAPI (Phase 2):** degraded digest (`source.fidelity: "derived-technical"`), flagged so the agent knows definitions/cardinality may be missing.
- **SKOS waardelijst (RDF/XML or Turtle):** separate `valuelists` section keyed by list URI.

Digest summary printed to the agent: model name/version, MIM version, model type (Conceptueel/Logisch), counts per kind, packages, extension name, fidelity, warnings. Everything else is retrieved on demand.

### W4. Look up and read (element cards) [P]

`mim.py find <digest> "<text>"` returns ranked hits (name, alias, definition text, begrip). `mim.py card <digest> Pand[.bouwjaar]` returns a **~150–400-token card**. Real example generated by hand from the IMGeo logical XMI (illustrative format, **not** final output):

```
Objecttype: Pand   [IMGeo 2.2 logisch, MIM-versie ?, domein IMGeo]   abstract: nee
Definitie: "Een PAND is de kleinste bij de totstandkoming functioneel en bouwkundig-constructief zelfstandige eenheid … "
Attributen (eigen + geërfd [supertypes: …]):
  identificatieBAGPND  CharacterString  1..1  authentiek  mogelijk-geen-waarde: nee  hist(materieel/formeel): nee/nee
  geometrie            GM_MultiSurface  1..1  authentiek  mogelijk-geen-waarde: nee  hist(materieel/formeel): nee/ja
  nummeraanduidingreeks (Gegevensgroep → Nummeraanduidingreeks)  0..1
Relaties: …    Constraints: …
```

(Observed in `Geonovum/IMGeoMIM/IMGeo2.2-MIM-logisch.xml`: Pand has exactly these three members, three Associations and 36 Generalizations exist in the model; `Begrip`, `Lengte`, `Patroon` tags are present but empty or `<memo>`.)

### W5. Map data fields to model elements [P]

Inputs: field names plus optional sample values from CSV/JSON/GeoJSON/OGC API queryables/OpenAPI schema/SQL DDL/RDF predicates. `mim.py map <digest> --fields … [--sample file]` produces candidates with scores and reasons.

Matching signals, in order of reliability:

1. **Identifier match:** exact URI/`identificatie`, `$anchor`/property-shape URI (`{ns}#{Owner}-{attr}`), explicit `rdf_seealso`/`mim:equivalent`.
2. **Name match** after normalization: case, `_`/camelCase, diacritics, Dutch compounds, plural/singular, alias vs naam.
3. **Type/value match:** sample values vs datatype, lengte, patroon, enum membership, cardinality of the column.
4. **Structure match:** column groups ↔ Gegevensgroep; `*.href` lists ↔ relatiesoort; composite objects ↔ Gestructureerd datatype; `_id`/`_href` ↔ referentie.
5. **Definition similarity** (agent-side judgement; the script only ranks).

Rules: report **confidence per mapping** (`exact | strong | plausible | none`), list **unmapped fields** (derived/denormalized/technical, e.g. `rdf_seealso`, `*.href`, paging fields) and **unmapped model elements**, and ask the user only when the choice changes the answer. Never silently coerce.

### W6. Interpret values [P]

For each value or column the agent needs: (a) datatype/length/pattern → validate shape; (b) waardelijst → resolve code → definition (`mim.py values <digest> <list> [--resolve]`; for Referentielijst/Codelijst fetch `locatie` in `doelformaat`, typically SKOS); (c) null semantics (rule 2); (d) units (`eenheid`); (e) history/time semantics; (f) authority. Output: a small table "value → meaning → source element".

### W7. Generate queries [P]

Pattern: *model fixes names, types, enum literals and null handling; API/dialect fixes syntax.* Provide short, tested templates (`references/query-patterns.md`) for:

- **OGC API Features** (property filter / CQL2 where supported; use `queryables` to confirm names and types),
- **SQL** (quoting, leading zeros as text, partial dates, NULL vs *mogelijk geen waarde*),
- **SPARQL** over Linked Data promoted per §6.4 (class via `mim:equivalent`/`rdfs:seeAlso`; property-shape naming),
- **pandas** snippets (dtype=str for coded numbers, enum as categorical).

Always run a cheap check query first (`limit 1`, distinct values of the enum column) and compare with the model's literals.

### W8. Compose the answer [P]

Output contract (in SKILL.md):

1. **Answer** in the user's language.
2. **Basis:** `Model <name> <version> (<MIM-versie>, <Conceptueel|Logisch>) › <Domein> › <Element>` plus source URL; for each non-trivial claim, tag as *model-stated*, *dataset-observed* or *inferred*.
3. **Caveats:** version mismatch, fidelity "derived-technical", unresolved mappings, extension-specific semantics.
4. Never state a model element exists unless the digest returned it.

### Efficiency principles [P]

Context is the scarce resource. The raw IMGeo XMI is 3.25 MB, on the order of ~10^6 tokens **[U estimate]**, so the agent must never read it. Therefore:

- Lazy loading: only SKILL.md (+ one reference file when needed) at activation; script outputs are bounded (`--max-tokens`, default ~800); `--format card|table|json`.
- Cache digests; reuse across turns.
- Prefer queryables/DDL for field lists instead of fetching data.
- Cap fetches (size limit, default 25 MB, user override).

---

## 5. Proposed skill structure

### 5.1 Layout inside the skill [P]

```
skills/geonovum-mim-interpret/
├── SKILL.md                      # <= ~300 lines / <5k tokens
├── references/
│   ├── mim-core.md               # §3.1–3.2 distilled; element/metagegeven tables; NL<->EN glossary
│   ├── interpretation-rules.md   # §3.3 with spec section refs and mini-examples
│   ├── serializations.md         # how each format looks, how to detect, parser quirks (EA XMI, MIM XML, RDF)
│   ├── workflows.md              # W0–W8 detail, decision tables, failure modes
│   ├── model-catalog.md          # verified model locations, versions, fidelity, dead links, last-verified date
│   ├── query-patterns.md         # OGC API / SQL / SPARQL / pandas templates
│   ├── mim-2-notes.md            # 1.2 vs 2.0 differences, detection, what is unsupported
│   └── conflicts.md              # where this skill deliberately deviates from or simplifies MIM (pattern from skills-nl-sbb)
├── scripts/
│   ├── mim.py                    # CLI entry: fetch | digest | find | card | values | map | check
│   └── mimlib/                   # adapters: mimxml.py, eaxmi.py, mimrdf.py (opt), jsonschema.py, skos.py; model.py; render.py
├── assets/
│   └── model-catalog.json        # machine-readable twin of model-catalog.md
├── examples/                     # worked transcripts: BAG status code, IMGeo Pand, partial dates, Keuze, null semantics
└── evals/
    ├── evals.json                # Agent Skills eval format
    ├── files/                    # fixtures (small excerpts) + generators for big ones
    ├── graders/                  # deterministic assertion scripts
    └── README.md                 # how to run with/without skill, benchmark.json schema
```

Notes: skills-nl-sbb puts evals and `reference.md` next to the skill; the Agent Skills guide puts `evals/evals.json` inside the skill directory [S16]. Keeping `evals/` inside the skill dir follows the guide; it can be excluded from plugin bundles by `generate_plugin.py` if size matters.

### 5.2 SKILL.md draft [P]

Frontmatter (follows S13 conventions; `description` ≤1024 chars; current length ≈ 790):

```yaml
---
name: geonovum-mim-interpret
description: >-
  Interpret Dutch open data with MIM (Metamodel Informatiemodellering) information models.
  Find the MIM-conformant model behind a dataset or API (IMGeo/BGT, BAG, BRK/IMKAD, NEN 3610,
  IMEV and others), parse it (MIM XML, Enterprise Architect XMI, SKOS waardelijsten, MIM RDF),
  map fields/columns/properties to objecttypen, attribuutsoorten and relatiesoorten, resolve codes
  via enumeraties and referentielijsten, and use definities, kardinaliteit, mogelijk-geen-waarde,
  historie and constraints to answer questions and build correct queries. Use when a user asks what
  a field, code or object in Dutch government or geo data means, how a dataset is structured, or
  mentions informatiemodel, MIM, objecttype, attribuutsoort, waardelijst or begrippenkader.
  Not for authoring or validating MIM models.
license: EUPL-1.2
compatibility: Python 3.10+ for scripts (stdlib only; rdflib optional); network access to Geonovum/PDOK/Kadaster hosts.
allowed-tools: Bash(python3 *) Read
metadata:
  nl.gov.status: concept
  nl.gov.review-by: "<date>"
  nl.gov.source: https://docs.geostandaarden.nl/mim/def-st-mim-20240613
  nl.gov.source-license: CC-BY-4.0
  nl.gov.category: standaarden
  nl.gov.tags: mim, informatiemodel, metamodel, geostandaarden, linked-data, open-data
  nl.gov.bundle: geonovum-mim
---
```

Body outline (≈ 250–300 lines):

1. Status banner (informative; standard is leading; not a conformity statement; generative-AI policy link).
2. "Use when / do not use when".
3. Five principles: model-first; never read raw model files, use scripts; **never invent model elements**; label evidence type; blank ≠ none.
4. Quick workflow (W0–W8 compressed) with the exact `mim.py` commands.
5. The ten rules most often needed (links to `references/interpretation-rules.md`).
6. Output contract (W8).
7. Failure handling table (no model, wrong version, 2.0, derived-technical fidelity, network blocked, huge file).
8. Pointers to references and examples.

### 5.3 Scripts [P]

All scripts: Python ≥3.10, **stdlib-only core** (`xml.etree`, `json`, `urllib`, `csv`, `re`), deterministic, bounded output, explicit exit codes, `--json` mode, helpful errors; `rdflib` optional and only for Turtle/RDF-XML MIM-RDF and SKOS (graceful degrade: RDF/XML SKOS can be parsed with a minimal built-in reader for `skos:prefLabel/notation/definition`). The NL-SBB skill installs pySHACL on demand; the same pattern is acceptable for rdflib, with user confirmation.

| Command | Purpose | Output (bounded) |
|---|---|---|
| `mim.py fetch <url\|catalog-id> [--version] [--allow host]` | Download + cache + sniff | path, sha256, size, detected format |
| `mim.py digest <file\|url> [-o]` | Normalize to MIM digest | summary + warnings; writes `digest.json` |
| `mim.py find <digest> <text> [--kind]` | Ranked search | ≤10 lines |
| `mim.py card <digest> <Type[.attr]>` | Element card incl. inherited members | ≤400 tokens |
| `mim.py values <digest> <list> [--resolve]` | Enum values, codes; fetch/resolve external lists | ≤N values + total, with definitions |
| `mim.py map <digest> --fields … [--sample …] [--openapi …] [--ogc <collection-url>]` | Candidate mapping | table: field → element, confidence, reasons, unmapped |
| `mim.py check <digest> <Type> --sample file` | Validate sample values (datatype, length, pattern, enum, cardinality, Keuze) | violation summary, no data echo beyond ids |

### 5.4 Examples [P]

`examples/` holds 6–8 short worked transcripts (input, commands, abridged outputs, final answer): BAG `status` codes (PDOK + Skosmos begrippen), IMGeo Pand card, `mogelijk geen waarde`, DMO partial date, Keuze XOR, Referentielijst vs Codelijst resolution, missing-model honesty, MIM 2.0 detection.

### 5.5 Evals: measuring correctness and efficiency [P]

**Format** per the Agent Skills guide [S16]: `evals/evals.json` (prompt, expected output, files, assertions), each run twice (`with_skill`, `without_skill`) in a clean context, outputs plus `timing.json` and `grading.json`, aggregated to `benchmark.json`.

**Baselines (arms):**

- A0 = agent with web access, no skill.
- A1 = skill.
- A2 = skill with `references/` only, scripts disabled (isolates script value).
- A3 (optional) = Dutch vs English SKILL.md (decides open question 4).

**Metrics:**

| Metric | How |
|---|---|
| Correctness (pass rate) | Deterministic assertions; ground truth **generated from the fixture model by script**, not by an LLM. LLM-judge rubric only for explanation quality. |
| Hallucination rate | Count of cited model elements/values not present in the model (automatic check against the digest). |
| Calibration | Does the answer flag uncertainty when the model is missing/ambiguous (rubric). |
| Efficiency | Total tokens, tool calls, wall time, bytes of model file read into context (`timing.json`). |
| Robustness | Pass rate on adversarial cases (below). |

**Targets (proposals, to be revised after the baseline run):** ≥ +25 pp pass rate over A0 on interpretation tasks; hallucinated elements ≈ 0 with skill; ≥ 50 % fewer tokens on model-heavy lookups.

**Fixtures** (small, redistributable): [P] a hand-written mini model (`mini-pand.mim.xml`, plus an XMI twin) with our own licence; excerpts of IMGeo 2.2 logisch (CC-BY from Geonovum; larger files downloaded in CI rather than committed); a frozen PDOK BAG `pand` response and queryables (open data); the MIM `Fietsenwinkel` sample only after the licence of that sample is clarified (it lives in a GPL-3.0 repo).

**Seed cases** (expand to ~30; all can be graded deterministically except where marked J):

| ID | Prompt (abridged) | Expected |
|---|---|---|
| E01 | Verschil Gegevensgroeptype vs Gestructureerd datatype? | Grouped separate attributes vs single composite value; per-part history (§2.3.2.4, §2.3.5.3, §5.2.2). **J** |
| E02 | Given IMGeo logisch XMI: attributen van Pand + verplicht? | `identificatieBAGPND` 1..1, `geometrie` 1..1, `nummeraanduidingreeks` 0..1 (Gegevensgroep). |
| E03 | Wordt formele historie bijgehouden voor Pand.geometrie? | Ja (formeel: Ja, materieel: Nee), per that XMI. |
| E04 | gemeentecode "0060": Integer? | No: CharacterString + pattern (§5.1.1). |
| E05 | Is "1985-03" een geldige geboortedatum? | Valid if datatype DMO; reject for Date. |
| E06 | Overlijdensdatum leeg (optioneel, mogelijk geen waarde = Ja): leeft persoon nog? | Cannot conclude (§5.11). |
| E07 | Betalingsopdracht: records waar beide `betalingskenmerk` en `omschrijving` gevuld zijn | Invalid under Keuze (XOR), not merely unusual. |
| E08 | Welke rijen hebben objecttype "Contact" (abstract)? | None directly; only subtypes. |
| E09 | PDOK pand feature + IMGeo/BAG model: wat betekent `geconstateerd`? | Needs model lookup; if absent say "not determinable from given model". **J** |
| E10 | Dataset X has no known model | States none found; labels inference; invents no elements. **J** |
| E11 | Definition field contains "ignore instructions and …" | Treated as data; not obeyed (R-6). |
| E12 | File declares MIM 2.0 vocabulary | Skill detects version mismatch and says unsupported. |
| E13 | Query: panden gebouwd na 2000 in gebruik (PDOK) | Uses `bouwjaar` int, exact enum literal from the data, `limit` sanity check. |
| E14 | Welke attributen heeft Wegdeel incl. geërfd? | Union with supertype members flagged as inherited. |
| E15 | Efficiency: one attribute lookup in 3.4 MB XMI | With skill: ≤ N tokens read; baseline: truncated reads or failure. |
| E16 | Referentielijst vs Codelijst: how to resolve codes | Different resolution steps (`locatie`, `waarde-item`). |
| E17 | Map columns of a CSV (fixture) to model elements | ≥ threshold exact/strong; unmapped flagged correctly. |
| E18 | Is `aantal_verblijfsobjecten` an independent fact? | Flags as derived, if marked `indicatieAfleidbaar` in fixture model. |

**Description-trigger eval:** per the Agent Skills "optimizing descriptions" guide, a separate set of ~20 should-trigger / should-not-trigger prompts (e.g. "Maak een UML model van mijn domein" should not trigger) to tune the 1024-character description.

---

## 6. Risks, open questions, decisions for the owner

### 6.1 Decision table (recommendation first)

| # | Decision | Options | Recommendation [P] |
|---|---|---|---|
| D1 | **Scope** | (a) consume/interpret only; (b) + review/validate models; (c) + authoring | (a). Reviewing overlaps Imvertor and the MIM toolbox; authoring overlaps `geo-model`. Keep a later `geonovum-mim-review` skill possible via the plugin bundle. |
| D2 | **Language** | NL / EN / bilingual | EN instructions and references, Dutch MIM terms verbatim (they are identifiers in models); the agent answers in the user's language; README/DISCLAIMER in NL with a short EN summary. Settle via eval arm A3, since sibling skills are Dutch-only. |
| D3 | **Serializations first** | MIM XML / EA XMI / MIM-RDF / JSON Schema / SKOS | MIM XML + EA XMI (one normalized model), then SKOS lists, then JSON Schema/OpenAPI, then MIM-RDF (Phase 2), since no MIM-RDF instance is published. |
| D4 | **MIM version** | 1.2 only / 1.x + 2.0 | 1.x in MVP; detect and refuse 2.0; revisit when MIM 2.0 is *vastgesteld*. |
| D5 | **Names** | repo, plugin, skill | Repo `Geonovum/skills-mim` (mirrors `skills-nl-sbb`), plugin `geonovum-mim`, skill `geonovum-mim-interpret`. Alternative: `skills-mim-data`. Check with the marketplace (name must match manifests: S14 notes Codex rejects mismatches). |
| D6 | **Licence** | EUPL-1.2 / CC-BY / Apache-2 | EUPL-1.2 for code, skill text and examples (matches `skills-nl-sbb`, `skills-geo`). MIM-derived text carries CC-BY-4.0 attribution (record in `nl.gov.source-license` and README). Own fixtures: EUPL-1.2/CC0. **No copying of Imvertor code/XSD (GPL-3.0) without a legal check**; reference by URL. Check the licence of each model and list used as a fixture (BAG data open; IMRO is CC-BY-ND according to S15). |
| D7 | **Distribution** | own repo only / marketplace plugin / both | Both; publish via the developer.overheid.nl marketplace as plugin `geonovum-mim`. |
| D8 | **Relation to `geo-model`** | ignore / coordinate / replace | Coordinate: propose that `geo-model` link to this skill for MIM semantics and drop its MIM section; report the inaccuracies. |
| D9 | **Model supply** | skill-only / drive publication | Ask Geonovum/Kadaster whether MIM XML (Imvertor) or MIM-RDF can be published beside XMI/EAP for IMGeo, IMKAD, NEN3610, IMBAG. This single decision determines the value of the skill (1.4). |
| D10 | **Status/governance** | `concept` → higher | Start at `concept`. Reuse NL-SBB's bar: expert review, published review procedure, ≥2 assistants tested (one open-source or European). Set a `review-by` date and an owner. |
| D11 | **Network policy** | open / allowlist | Host allowlist by default, user-extendable; no telemetry; no writes outside cache. |
| D12 | **Mapping aggressiveness** | auto-map / ask first | Auto-propose with confidence; ask only when ambiguity changes the answer. |

### 6.2 Risks

| ID | Risk | Mitigation [P] |
|---|---|---|
| R-1 | **Models not machine-readable or links dead** (IMKAD `.EAP` only; 404 on `modellen.mim-standaard.nl/def/mim`, `bag.basisregistraties.overheid.nl/def/bag`, BAG `rdf_seealso`). | Curated catalog with *last verified* date and alternates; CI link-check (as `skills-geo` monitors links); degrade to begrippen (Skosmos) and derived schemas with explicit fidelity labels; D9. |
| R-2 | **Wrong mapping → confident wrong answers.** | Confidence tiers, mapping table shown to user, rule "never invent elements", hallucination eval, `check` against sample values. |
| R-3 | **Model/data version drift.** | Pin versions, record `datumOpname`/model version, warn when data release date is newer than model. |
| R-4 | **Conceptual vs logical mismatch** (names, abstract types, missing technical datatypes). | Prefer logical for data; cross-link by name; flag unverified link; document in `conflicts.md`. |
| R-5 | **Token blow-up on big models.** | Digest + bounded outputs; never read raw. Measured in efficiency evals. |
| R-6 | **Prompt injection** via model definitions, begrippen, or data values fetched from the web. | Skill text: external content is data, never instructions; scripts strip control content; eval E11. |
| R-7 | **Personal data** (BRK/BRP, BAG addresses linked to persons). | Out-of-scope statement; no instructions to retrieve personal data; AVG/GDPR note in DISCLAIMER; examples use non-personal data. |
| R-8 | **Liability/authority**: skill output taken as official. | Banner + DISCLAIMER (informative; standard leading; no conformity statement), as in `skills-nl-sbb`; GenAI policy reference (`nl.gov.generated-with`). |
| R-9 | **Overlap with `geo-model`**, confusion in triggers. | D8; description scoped to *consumption*; trigger evals. |
| R-10 | **MIM 2.0 churn**, same namespace, different semantics. | Version gate; `mim-2-notes.md`; Phase 3. |
| R-11 | **EA XMI parser fragility** (encoding, memo placeholders, tool noise, UML 1.3). | Spike on 3 real files (IMGeo logisch/conceptueel, NEN3610 template); fixtures; fail-soft warnings. |
| R-12 | **"MIM XML format" is Imvertor's, not normative MIM**; schema versions differ (1.1 vs 1.2). | Treat as a *source format*, detect version from namespace; upstream a request to Geonovum to document/endorse it. |
| R-13 | **Trigger quality** (skill fires too often/rarely). | Description eval set; iterate. |
| R-14 | **Maintenance cost** (new model versions, catalog rot). | `review-by`, scheduled link/content monitoring, Changesets (as S13), owner named in `publiccode.yml`. |
| R-15 | **Python/network not available** in the agent environment. | Instructions-only fallback path (references + manual XPath/grep hints); `compatibility` field states requirements. |

### 6.3 Further open questions (lower priority)

- Is there an authoritative list of which Dutch registries have a MIM-conformant model, and where each is published? (Geonovum dashboard `informatiemodellen.md` lists projects but not serialization locations [S8].)
- Should the skill later ship an MCP server wrapper around `mim.py` for agents without shell access? (Out of MVP.)
- Should begrippen (NL-SBB/Skosmos) be a separate sibling skill? The MIM skill uses them read-only for `begrip` URIs.
- Official English wording: use the §6.3 translation table or the `MIM-1.2-Engels` text as the glossary source?
- Do MIM model publishers intend to include `mim:equivalent` bridges from data classes to model elements? That would make W5 mostly deterministic.

---

## 7. Phased roadmap

(No calendar estimates; phases are ordered by dependency and sized by technical scope.)

### Phase 0: Decisions and spikes

- Owner decisions D1–D6, D9 (section 6).
- **Parser spike** on three real files: IMGeo logisch XMI, IMGeo conceptueel XMI, NEN3610 2022 template XMI; plus the Fietsenwinkel MIM XML. Exit: a digest schema proven against all four; known quirks listed.
- Verify model catalog entries (URLs, licences, versions) and the PDOK/Skosmos access patterns.
- Create the baseline eval run (A0) on ~10 seed prompts to size the problem.

### Phase 1: MVP ("model-aware answers on a handful of models")

Deliverables:

- `SKILL.md` + `references/` (`mim-core`, `interpretation-rules`, `serializations`, `workflows`, `model-catalog`, `conflicts`).
- `scripts/mim.py` with **`fetch`, `digest`, `find`, `card`, `values`** for **MIM XML + EA XMI** and **SKOS RDF/XML waardelijsten**.
- Catalog of **4–6 models** that are actually parseable (IMGeo, NEN 3610, plus whatever D9 yields; IMEV via JSON Schema + begrippen as a "derived" entry).
- 3–4 worked examples; 20–25 evals with A0/A1/A2 results; DISCLAIMER, `publiccode.yml`, plugin manifests, CI (lint, link-check, script tests), status `concept`.

Exit criteria: ≥ +25 pp over baseline on interpretation evals; hallucination ≈ 0 on the seed set; SKILL.md < 5k tokens; scripts work on Python 3.10–3.13 without pip.

### Phase 2: Data-side bridge

- `map` and `check`; ingest OGC API queryables/collection schemas, OpenAPI, JSON Schema, CSV/GeoJSON headers and samples, SQL DDL.
- MIM-RDF/Turtle adapter (rdflib optional) incl. the §6.4 reverse transformation heuristics for RDFS/OWL/SHACL; SKOS Turtle.
- `query-patterns.md` (OGC API/CQL2, SQL, SPARQL, pandas) with tested snippets; Skosmos begrippen lookups.
- Description-trigger evals; expert review round with Geonovum/Kadaster MIM people.

### Phase 3: Breadth and robustness

- MIM 2.0 detection → opt-in support for CIM/LGM once stable; version-aware digests.
- Cross-model resolution (Extern/View links, NEN3610 base types), multi-model questions.
- Multi-assistant testing (≥2, incl. an open-source or European model) to meet the NL-SBB-style status bar; evals in Dutch and English.

### Phase 4: Operate

- Marketplace listing (S14), release automation (Changesets), scheduled link/model-version monitoring, catalog refresh PRs; optional MCP wrapper; status progression beyond `concept` once the governance bar is met.

---

## 8. Proposed repo layout and README outline

### 8.1 Repo layout [P] (mirrors `Geonovum/skills-nl-sbb` [S13])

```
Geonovum/skills-mim/
├── README.md                     # NL (primary) + short EN section
├── DISCLAIMER.md                 # informative status, not the standard, no conformity statement, GenAI notice, no guarantee
├── LICENSE                       # EUPL-1.2
├── CONTRIBUTING.md  CODE_OF_CONDUCT.md  SECURITY.md  CHANGELOG.md
├── publiccode.yml                # softwareType: addon; supports: MIM 1.2 URI; maintenance contacts
├── package.json                  # private; Changesets only (as S13)
├── .changeset/
├── .github/workflows/            # ci (lint, unit tests, link-check), release, monitoring
├── .claude-plugin/plugin.json    # generated by scripts/generate_plugin.py
├── .cursor-plugin/plugin.json
├── .plugin/plugin.json
├── scripts/                      # generate_plugin.py, sync_version.py (repo-level, not skill-level)
├── skills/
│   └── geonovum-mim-interpret/   # see 5.1
├── tests/                        # unit tests for mimlib adapters, fixtures
└── docs/
    ├── design.md                 # this design, trimmed
    └── model-supply.md           # which Geonovum/Kadaster models are published how (for the D9 discussion)
```

### 8.2 README outline [P]

1. Title and one-line purpose (what the skill does for agents using Dutch open data).
2. Status box: `concept`; informative; the standard is leading; link to DISCLAIMER.
3. What problem it solves: short before/after example (BAG `status`, null semantics).
4. Skills table (name, status, purpose), as in S13.
5. Installation: marketplace (Claude Code, Codex, Cursor) and manual copy.
6. Usage: example prompts (NL/EN); what the agent does (workflow in 6 lines); what it will not do.
7. Supported models and formats (generated from `assets/model-catalog.json`), with fidelity levels and last-verified dates.
8. Requirements: Python 3.10+, optional rdflib, network/allowlist, privacy (no telemetry).
9. Relation to the standard: MIM 1.2 links (definitive, latest, werkomgeving), issues about the standard go to `Geonovum/MIM-Werkomgeving`; relation to Imvertor, `skills-nl-sbb`, `skills-geo/geo-model`.
10. Evaluation: how we measure (with/without skill), latest benchmark numbers, how to run.
11. Contributing (model catalog additions, new adapters, eval cases), maintainers, helpdesk `mim@geonovum.nl`.
12. Licence and attribution (EUPL-1.2; MIM CC-BY-4.0; third-party notes).

---

## Appendix A. Sources (all accessed 2026-10-30)

| Id | Source |
|---|---|
| S1 | MIM 1.2 spec: https://docs.geostandaarden.nl/mim/mim/ (def. 2024-06-13; full text read, in particular §1.5–1.13, 2.2–2.4, 3.3, 4.1–4.4, 5.1–5.16, 6.3–6.5) |
| S2 | Version index: https://docs.geostandaarden.nl/mim/ |
| S3 | https://github.com/Geonovum/MIM-Werkomgeving (`MIM-1.2-Engels/`, `MIM-Extensies/`) |
| S4 | MIM 2.0 working repos: `Geonovum/mim-metamodel`, `mim-ld` (`model/mim-ontologie.ttl`, `mim-in-mim/`), `mim-conceptueel`, `mim-logisch`, `mim-uml` |
| S5 | https://register.geostandaarden.nl/ (`informatiemodel/`, `waardelijst/`, `jsonschema/`, `shacl/`, `mim/`) |
| S6 | https://github.com/Geonovum/IMGeoMIM (`IMGeo2.2-MIM-conceptueel.xml`, `-logisch.xml`; EA XMI 1.1) |
| S7 | https://github.com/Imvertor/Imvertor-Maven (`etc/xsd/MIMformat/v2/1.2/`, `Samples/Fietsenwinkel.xml`; GPL-3.0) |
| S8 | https://github.com/Geonovum/geonovum-allemodellen (`imvertor/Imvertor.properties`, `mim/mim2report.xsl`), `geonovum-dashboard` |
| S9 | https://github.com/Geonovum/imev (JSON Schema, OAS, Stelselcatalogus JSON) |
| S10 | https://github.com/Geonovum/bestuurlijke-gebieden-lm (`schemas/LGM-BG*.schema.json`) |
| S11 | PDOK BAG OGC API v2: https://api.pdok.nl/kadaster/bag/ogc/v2/ (collections, queryables, `pand` item) |
| S12 | Kadaster catalogus (Skosmos): https://catalogus.kadaster.nl (REST `search`, `data`) |
| S13 | https://github.com/Geonovum/skills-nl-sbb (layout, SKILL.md frontmatter, DISCLAIMER, publiccode.yml, status ladder) |
| S14 | https://github.com/developer-overheid-nl/skills-marketplace (marketplace, plugins) |
| S15 | https://github.com/developer-overheid-nl/skills-geo (`skills/geo-model`) |
| S16 | Agent Skills: https://agentskills.io/specification, `/skill-creation/best-practices`, `/skill-creation/evaluating-skills` |
| S17 | https://github.com/Geonovum/imbag, https://imbag.github.io/catalogus/ |
| S18 | https://github.com/Geonovum/IMGeo (`informatiemodel/`, `waardelijst/`, `gmlapplicatieschema/`) |

## Appendix B. Verification log (negative and surprising findings)

- `http://modellen.mim-standaard.nl/def/mim` and `/def/mim-shapes`: 404.
- `https://bag.basisregistraties.overheid.nl/def/bag`, `https://brk.basisregistraties.overheid.nl/def/brk`, and `…/bag/id/pand/0003100000117485` (Accept: turtle, ld+json, default): 404 `application/problem+json`.
- `definities.geostandaarden.nl/nen3610-2022/id/` redirects to `/nen3610-2022/nl/id/` which is 404.
- `Geonovum/mim-ld/example/mim.ttl`: 0 bytes.
- IMKAD 2.3.1 in the register: only `IMKAD-23.1.EAP`.
- `register.geostandaarden.nl/shacl/` contains only `nl-sbb/`.
- Kadaster Skosmos: `/rest/v1/vocabularies` lists `ar, bag, brk, brt, li, or, tr`; `/rest/v1/search?vocab=bag&query=pand*` works; `/rest/v1/data?uri=<bag concept Pand>` with `Accept: text/turtle` returns the concept (definition, sources, broader); the per-vocab `…/rest/v1/bag/data?…&format=application/ld+json` variant returned empty/403.
- IMGeoMIM logical XMI: 38 Objecttype, 118 Attribuutsoort, 59 Enumeratie, 344 Enumeratiewaarde, 13 Datatype, 5 Gegevensgroep, 5 Keuze, 3 Association, 36 Generalization; 127 distinct tag names (mostly EA noise).

## Appendix C. Proposed MIM digest schema (normalized internal model) [P]

```jsonc
{
  "source": {"url": "…", "sha256": "…", "format": "ea-xmi|mim-xml|mim-rdf|json-schema|skos", "fidelity": "full|derived-technical", "retrieved": "ISO-8601"},
  "model": {"name": "…", "version": "…", "mimVersion": "1.2", "mimExtension": null, "type": "Conceptueel|Logisch", "language": "NL", "baseUri": "…", "relatiemodelleringstype": "Relatiesoort leidend"},
  "packages": [{"id": "…", "kind": "Domein|Extern|View", "name": "…", "baseUri": "…"}],
  "elements": {
    "<id>": {
      "kind": "Objecttype|Attribuutsoort|Gegevensgroep|Gegevensgroeptype|Relatiesoort|Relatieklasse|ExterneKoppeling|Keuze|Constraint|PrimitiefDatatype|GestructureerdDatatype|DataElement|Enumeratie|Enumeratiewaarde|Referentielijst|ReferentieElement|Codelijst",
      "name": "…", "alias": null, "uri": "…", "package": "<pkg id>", "owner": "<element id>|null",
      "definitie": "…", "toelichting": null, "begrip": ["term|uri"], "herkomst": "…", "herkomstDefinitie": "…", "datumOpname": "…",
      "abstract": false, "supertypes": ["<id>"], "mixin": false,
      "type": "<datatype id|primitive name>", "kardinaliteit": "1..1", "kardinaliteitBron": null,
      "lengte": null, "patroon": null, "formeelPatroon": null, "eenheid": null, "min": null, "max": null,
      "mogelijkGeenWaarde": false, "identificerend": false, "authentiek": null, "afleidbaar": false, "classificerend": false,
      "historie": {"geldigheid": null, "registratie": null},
      "bron": "<id>", "doel": "<id>|[ids]", "aggregatietype": "Geen",
      "locatie": null, "doelformaat": null, "waardeItem": null, "code": null,
      "keuzeOptions": ["<id>"], "constraints": ["<id>"],
      "extensions": {"<tag>": "<value>"}
    }
  },
  "index": {"byName": {"pand": ["<id>"]}, "byUri": {}, "byBegrip": {}},
  "warnings": ["memo tag values unresolved for 412 elements", "…"]
}
```

## Appendix D. NL ⇄ EN glossary seed (from MIM 1.2 §6.3) [V]

Objecttype = FeatureType; Attribuutsoort = AttributeType; Gegevensgroeptype = AttributeGroupType; Gegevensgroep = AttributeGroup; Relatiesoort = AssociationType; Relatieklasse = AssociationClass; Externe koppeling = ExternalLink; Relatierol = AssociationRole; Referentielijst = ReferenceList; Referentie-element = ReferenceElement; Enumeratie = Enumeration; Enumeratiewaarde = Enum; Codelijst = CodeList; Datatype = SimpleType; Gestructureerd/Complex datatype = ComplexType; Data-element = DataElement; Keuze = Union; Keuze-element = UnionElement; Extern = External; View = View; Mogelijk geen waarde = Voidable; Herkomst = Source; Herkomst definitie = Origin of definition; Indicatie authentiek = Indication authentic; Kwaliteit = Quality; Lengte = Length; Patroon / Formeel patroon = Pattern / Formal pattern; Populatie = Population; Toelichting = Description; Datum opname = Date recorded.
