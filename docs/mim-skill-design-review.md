---
cursor:
  subagentId: "bc-affd2fad-febb-5656-8217-110581ae8fc4"
---

# Review: MIM skill design (`geonovum-mim-interpret`)

Reviewed: [mim-skill-design.md](mim-skill-design.md) (MS-1). Review date: 2026-10-30. This is a critique, not a rewrite.

Checked against: MIM 1.2 (Vastgestelde versie 13 June 2024) at `docs.geostandaarden.nl/mim/mim/` (full text, especially beschouwingsniveaus, §2.3–2.4, waardelijsten, Keuze, historie, authentiek, mogelijk geen waarde, datatypes); IMBAG Catalogus 2018 (HTML + PDF); PDOK BAG OGC API v2 `pand` queryables; IMKAD 2.3.1 register listing; `modellen.mim-standaard.nl/def/mim/` (unavailable: 500 on this pass; design reported 404).

---

## 1. Direct answer

**Yes, with caveats** — and the caveats decide whether the owner’s goal is met.

The design correctly identifies the job: agents already guess from column names; MIM-conformant *informatiemodellen* hold the definitions, kardinaliteit, *mogelijk geen waarde*, waardelijst kind, Keuze, historie flags, and *authentiek* that would stop those guesses. The 16 rules are, in the main, faithfully derived from MIM 1.2. Digest + cards is the right way to keep a 3 MB EA XMI out of context. Consume-only is the right scope.

It would **not**, as phased, reliably help an agent interpret the open data people actually ask about.

MIM describes **M1 models** (levels 2–3). Published data is **M0 / level 4** (OGC API, JSON, GML, CSV). The skill only changes answers when three things are all true: (1) a machine-readable model exists, (2) that model is the one that describes *this* dataset, (3) fields are mapped to the right modelelementen. The design itself shows that (1) fails for IMBAG and IMKAD, (2) is easy to get wrong (IMGeo `Pand` vs IMBAG `Pand`), and (3) is deferred to Phase 2 and left heuristic. Phase 1 (`fetch` / `digest` / `find` / `card` / `values`) makes the agent better at **reading models**, not at **interpreting data**.

For IMGeo/BGT-class datasets that already publish EA XMI plus SKOS waardelijsten: yes, this would help. For BAG and BRK — MIM-conformant standards whose data is the usual Q&A target — the MVP as designed would often point at the wrong artefact, or at none.

---

## 2. What would actually help

Map of proposed capabilities to the agent failure they prevent. “Paper-only” means the artefact looks serious but would not change answers about data.

| Capability | Failure mode it can prevent | Would it change answers? |
|---|---|---|
| **Digest** (XMI/XML → bounded JSON) | Agent never opens the 3 MB IMGeo XMI, truncates it, or invents attributes. Efficiency failure, not a semantics failure. | Yes, **when a parseable model is the right model**. No effect on BAG/BRK. |
| **Element cards** (incl. inherited members, kardinaliteit, flags) | Incomplete “what does Pand have?”; treating abstract supertypes as rows; missing that a Gegevensgroep is not one value. | Yes for model lookup. Still silent on denormalized API fields that are not members of that objecttype. |
| **Rule 1 — model ≠ data** | Treating a collection/table as the objecttype; missing denormalization (`gebruiksdoel` on PDOK `pand`). | Yes, **if the agent is forced to apply it**. Easy to recite and then ignore. Needs mapping examples, not a slogan. |
| **Rule 2 — blank ≠ none / *mogelijk geen waarde*** | Inferring “does not exist” or “person still alive” from NULL. The four combinations in MIM 1.2 (verplicht×MGW) are the real gold. | Yes. Highest-value rule in the set. **The first sentence of the design’s rule 2 is wrong** (see §3): `0..1` means known-absent *only* when MGW = Nee. |
| **Rule 3 — kardinaliteit** (incl. groep × attribuut) | Treating `0..1` as “nullable integer”; missing `1..*` on `gebruiksdoel`; treating generalisatie as optional. | Yes, after mapping. |
| **Rule 4 — directed relations / kardinaliteitBron** | Answering “can a VBO lie in several panden?” from the `.href` array shape instead of the relatiesoort. | Yes, if the relation is in the digest. BAG’s “maakt onderdeel uit van gerelateerd pand” lives in IMBAG prose, not in IMGeo XMI. |
| **Rule 5 — inheritance / abstract types** | Querying for rows of an abstract objecttype (`Adresseerbaar object`, `Contact`). | Yes on models that use abstract types. Cheap and worth keeping. |
| **Rule 6 — waardelijst kind** | Treating `status` as free text; using enum `code` as the exchanged value; not resolving a Referentielijst via `locatie`. | Yes. Directly stops “Pand in gebruik” being paraphrased. Needs the actual list, not the rule text. |
| **Rule 7 — datatypes / DMO / leading zeros** | Casting `gemeentecode` `"0060"` to int; parsing `"1985-03"` as a full Date; treating BAG `bouwjaar` as a calendar date. | Yes. PDOK types `bouwjaar` as integer; IMBAG types *oorspronkelijk bouwjaar* as `Year`. The rule helps only if the **model** type wins over the API schema. |
| **Rule 8 — Gestructureerd datatype vs Gegevensgroep** | Splitting a Bedrag into independently historied facts; treating a flattened group as one column. | Rare in typical open-data Q&A. Keep as a reference, do not spend MVP on it. |
| **Rule 9 — Keuze = XOR** | Accepting two filled alternatives as “unusual”. | Yes on models that use Keuze (IMGeo has 5). Almost never in BAG OGC API payloads. |
| **Rule 10 — historie flags** | Mixing current snapshot with voorkomen; assuming `heeft tijdlijn geldigheid = Ja` means the API exposes history. | **Intended yes, as written no.** MIM 1.2 is explicit: on conceptual level the flag does *not* mean the administration keeps a timeline; it means the property *can change* / the registration moment *must be queryable*. History field names are implementation (BAG: `beginGeldigheid`, `tijdstipRegistratie`, `voorkomen`, `tijdstipInactief`). Cards that echo XMI tags will make agents *more* confident and still wrong about a PDOK snapshot. |
| **Rule 11 — *indicatieAfleidbaar*** | Treating `aantal_verblijfsobjecten` as an independent fact. | Yes, **if the flag is present in the model of this dataset**. IMGeo/IMBAG may not mark PDOK-derived properties at all. |
| **Rule 12 — identificerend / authentiek** | Joining on the wrong key; treating every BAG field as legally authentic. | Partially. *Authentiek* is a **value range** (Authentiek / Basisgegeven / Wettelijk gegeven / Landelijk kerngegeven / Overig), not a boolean. IMBAG: `status` and *oorspronkelijk bouwjaar* are Authentiek; `geconstateerd` is **Basisgegeven** (no gebruiksplicht). Collapsing this to “authentiek ⇒ authoritative” is itself a failure mode. |
| **Rule 13 — herkomst / begrip vs definitie / Extern·View** | Using a SKOS begrip as the information definition; applying local meaning to an NEN3610ID. | Yes for cross-model types. Secondary for single-dataset Q&A. |
| **Rule 14 — conceptueel vs logisch** | Reading a technology-neutral conceptual model as if it were the API contract. | Yes. IMBAG is explicitly a **conceptueel** model (MIM 1.0 UML in `.eap` + catalogus). Preferring “logical XMI” would skip it. |
| **Rule 15 — order not significant** | None in Q&A over data. | **Paper-only.** Model-equivalence trivia. Cut from SKILL.md. |
| **Rule 16 — version / extensie** | Silently reading a MIM 2.0 file in the same `mim:` namespace. | Parser safety, not interpretation quality. Keep as a hard fail, not as an “interpretation rule.” |
| **Mapping (`mim.py map`)** | The whole class of “wrong element, confident answer”: `bouwjaar` ↔ *oorspronkelijk bouwjaar*; `gebruiksdoel` on `pand`; IMGeo `Pand` vs IMBAG `Pand`; `identificatie` vs `identificatieBAGPND`. | **This is the product.** Phase 2 is too late. Heuristic name matching will not survive Dutch compounds, API snake_case, and denormalization. |
| **Waardelijsten (`values` + SKOS)** | Codes as prose; missing sibling values; mixing Enumeratie literals with Referentielijst ids. | Yes, when `locatie` resolves. SKOS on the register is already the best machine-readable part of several models. |
| **Provenance in the answer** | Ungrounded claims; citing a model that was not used. | Changes *calibration*, not the interpretation. Keep as output contract; do not confuse it with correctness. |
| **Evals** | (Measurement, not a runtime capability.) | Only if they score the **semantic conclusion**. As written, several score “mentioned the model.” |
| **PDOK BAG example** | Motivating story for UC1/UC3/UC4. | **As specified, it teaches the wrong pairing.** PDOK `pand` is IMBAG (plus API denormalization). The worked card is IMGeo `Pand` (`identificatieBAGPND`, `geometrie`, `nummeraanduidingreeks`). Same word, different objecttype, different attributes. An agent that “uses the skill” on this example can look disciplined and still misread `geconstateerd`, `status`, `bouwjaar`, `gebruiksdoel`. |
| **Query templates (OGC/SQL/SPARQL/pandas)** | Wrong CQL2 literals / dtypes. | Marginal. Queryables already give names and JSON types. The model is needed for *meaning* of the literal, not for CQL2 syntax. Defer. |
| **Repo/plugin/marketplace scaffolding** | Distribution. | **Paper-only for the owner’s goal.** Copy from `skills-nl-sbb` after the interpretation loop works on one dataset. |
| **`check`** | Invalid values slipping through. | Useful after mapping exists. Not an interpretation aid by itself. |
| **MIM-RDF adapter** | None today: no published instance; ontology URI was 404/500. | Cut from MVP. |

**Rules that are enough, if fixed:** 1–7, 9, 11, a repaired 10, a repaired 12, 14. That is the SKILL.md set. 8, 13, 15, 16 belong in `references/`, not in the always-on list.

---

## 3. Gaps that would still leave the agent wrong

### 3.1 Machine-readable models (the design already knows this; it is not priced as a gate)

Verified this pass:

- **IMKAD 2.3.1** at `register.geostandaarden.nl/informatiemodel/imkad/2.3.1/` is still only `IMKAD-23.1.EAP` (12 MB). Unparseable.
- **IMBAG** is MIM-conformant (Catalogus 2018 §2.7, modelled in MIM 1.0 terms) and is the model behind PDOK BAG. Published as HTML/PDF catalogus + `.eap`. No MIM XML/XMI found. Chapter 9 *does* specify historie implementation (`beginGeldigheid`, `voorkomen`, `tijdstipInactief`, …) — which MIM 1.2 refuses to standardize.
- **BAG Extract XSDs** (Kadaster `bag-leveranciers`, IMBAGLV) are level-4 and parseable, but lossy for metagegevens.
- **Kadaster ontology URIs** and `rdf_seealso` on PDOK features: design’s 404s still the working assumption. `https://modellen.mim-standaard.nl/def/mim/` returned **500** here (design: 404). Do not depend on dereference.
- **IMGeo 2.2 XMI + SKOS** remains the only flagship model that fits the MVP adapters.

D9 is not an “open question.” It is a **go/no-go** for the owner’s goal. A catalog of “4–6 parseable models” that does not include IMBAG is a BGT skill, not an open-data skill.

A0 (web access, no skill) can already read IMBAG HTML tables: Stereotype, Definitie, Kardinaliteit, Authentiek, Mogelijk geen waarde, domeinwaarden `J`/`N`. On BAG questions, A0-with-catalogus can beat A1-with-IMGeo-XMI.

### 3.2 Consume-only vs authoring

Keep consume-only. Correct call. Authoring overlaps Imvertor and `geo-model`; reviewing overlaps Imvertor. Do **not** block MVP on coordinating `geo-model`. Mention it in `conflicts.md` and in the description (“Not for authoring”). Trigger evals later.

### 3.3 MIM 2.0

Detect-and-refuse is right. Same `mim:` namespace with `Attribuuttype` / `Relatietype` is a real footgun. Do not “build for 2.0.” Do not spend Phase 1 on `mim-2-notes.md` beyond a version sniff.

Published sector models still speak **MIM 1.0 tagged values** (`Indicatie materiële historie`, not `heeft tijdlijn geldigheid`). The parser must accept both names or IMBAG/IMGeo cards will drop history flags.

### 3.4 Language

Secondary. Dutch terms *are* the identifiers. English instruction with verbatim Dutch terms is fine. Do not wait on arm A3. If anything, a Dutch SKILL.md matches sibling skills and Dutch questions; it is not what makes answers correct.

### 3.5 Relation to `geo-model`

Real trigger-collision risk, low interpretation risk. Coordinate after there is something worth linking to. Do not replace `geo-model` in this project.

### 3.6 “Find the model” is not realistic as discovery

W1’s precedence list looks orderly and will fail in the cases that matter:

1. User-supplied file — rare.
2. Pointers in the data — BAG `rdf_seealso` 404s; `dct:conformsTo` usually points at a landing page, not XMI.
3. Skill catalog — only as good as hand-maintained pairs **(dataset/API, version) → model**. This is the only realistic path.
4. Register listing — IMKAD gives an `.EAP`; IMBAG is not there as XML.
5. GitHub search — noisy, easy to pick IMGeo for a BAG question because both contain `Pand`.

**Find-the-model must be a curated allowlist of (product, collection) → model**, not a crawler. Homonyms are the bug: IMGeo `Pand` ≠ IMBAG `Pand`. NEN3610 `Gebouw` ≠ either.

### 3.7 Mapping from data fields to model elements is underspecified — and is the actual problem

W5’s signal ranking (URI, then name, then type, then structure) is reasonable as a sketch and insufficient as a design.

Concrete counterexamples the heuristic will miss, all from the design’s own BAG sample vs IMBAG 2018:

| PDOK `pand` field | IMBAG element | Why name-match fails |
|---|---|---|
| `identificatie` | Pand.identificatie | Works — lucky. IMGeo uses `identificatieBAGPND`. |
| `bouwjaar` (JSON integer) | *oorspronkelijk bouwjaar* (`Year`, Authentiek, kardinaliteit 1, MGW Nee) | Compound name; API type ≠ model type. |
| `status` | Pand.status, domein `StatusPand` | Name works; still need the **enumeratie**, not a paraphrase. |
| `geconstateerd` = `"N"` | Pand.geconstateerd, domein `Indicatie` {J, N}, **Authentiek = Basisgegeven**, MGW Nee | Not in PDOK *queryables*. Easy to read as boolean or as “not observed in the field.” It means: *not* recorded via feitelijke constatering without a regular brondocument. |
| `gebruiksdoel` | **Verblijfsobject**.gebruiksdoel `[1..*]` (Bouwbesluit enumeratie) | Not a Pand attribuutsoort. API denormalizes / derives. Rule 1 must fire as a mapping *type*, not a caveat. |
| `aantal_verblijfsobjecten` | Not an IMBAG Pand attribuutsoort | Derived/technical. Unmapped is the correct answer; “plausible match to something” is harmful. |
| `geometry` | Pand.geometrie | Name mismatch (`geometry` vs `geometrie`). |
| `documentdatum` / `documentnummer` | Brondocument gegevensgroep (shared across objecttypes) | Structure match, not name match. |

There is no gold mapping table in the design for any live API. Without that, `map` will produce confident wrong links, which is **worse** than no skill (R-2). Also missing: mapping *types* (direct / renamed / denormalized / derived / technical / homonym-rejected); pinning **model version to data product version**; preferring IMBAG over IMGeo when the collection is `api.pdok.nl/kadaster/bag`.

MIM will not save this. MIM’s own scope (data is out of scope; level 4 is out of scope; historie implementation is not standardized) means **the mapping is extra-standard work** and must be curated.

### 3.8 Are the 16 rules enough, and correctly derived?

**Mostly correctly derived, not enough, two of them overclaim.**

Verified against MIM 1.2:

- Four MGW×kardinaliteit combinations, “do not encode onbekend as an enum except when inherited,” Keuze XOR and “Keuze name is not a field,” Enumeratiewaarde *naam* is the value (alias/code is documentation), Referentielijst vs Codelijst, CharacterString for leading zeros (`gemeentecode` `"0060"`), DMO/DTMO, gegevensgroep cardinality multiplication, objecttype ≠ table, historie not standardized at logical level — all match the spec.
- **Rule 2 overclaim:** “Optional (`0..1`) means known not to exist.” Only true when *mogelijk geen waarde* = Nee (combination 3, e.g. officiële straatnaam). Combination 4 (optional + MGW Ja, *overlijdensdatum*) is the design’s own UC2. Fix the sentence or the rule will fight E06.
- **Rule 10 overclaim:** flags are *not* “whether history is kept in the dataset.” Conceptual `heeft tijdlijn geldigheid` means the property can take different values over the validity timeline; it “geeft op conceptueel niveau niet aan dat er voor het gegeven een tijdlijn geldigheid wordt bijgehouden in de administratie.” E03 (“formele historie bijgehouden voor Pand.geometrie? Ja, because the XMI tag says so”) tests tag-copying, not interpretation of a snapshot API.
- **Rule 12 overclaim:** *Authentiek* is not boolean. IMBAG `geconstateerd` = Basisgegeven is the teaching case.
- Pedagogical conflict: MIM 1.2 uses “bouwjaar pand → tijdlijn geldigheid Nee” as an example; IMBAG 2018 tags *oorspronkelijk bouwjaar* with **Indicatie materiële historie = Ja**. Instance model beats the spec’s example. Encode that.

Missing rules that *do* change open-data answers:

1. **Populatie** — which instances are in the registration (BAG: NL municipalities, not “all buildings”; objects withdrawn before 1 July 2009 generally absent).
2. **Product ≠ model** — OGC API / Extract / “actueel” snapshot are level-4 projections; missing fields (`geconstateerd` absent from queryables, present on items) are product choices.
3. **Homonym objecttypes** — never bind `Pand` without the model id.
4. **Constraint vs Keuze** — constraints are the other XOR/OR vehicle (plain text + optional formal spec). Ignoring them misses validity rules the 16 do not cover.
5. **Void reasons** — when MGW = Ja, allowed reasons may sit in *toelichting*; inventing “onbekend” is forbidden unless the source registry does.
6. **Indicatie / J-N vs Boolean** — BAG `geconstateerd: "N"` is an enumeratiewaarde, not `false`.
7. **Levenscyclus vs historie** — `status` (`Pand in gebruik`) is not a time-axis; voorkomen is. Mixing them is a common BAG error the 16 never name.

### 3.9 HTML catalogs are not a footnote

IMBAG chapters 6–8 are already MIM-shaped tables. For the owner’s goal, a **catalog-table adapter** (or even hand-extracted cards for one dataset) beats a perfect EA XMI parser that has nothing to chew. The design rates HTML as “poorly” machine-usable and then builds the whole MVP around XMI. That inverts the availability of models.

Licence caution the design underplays: IMBAG catalogus is **CC-BY-ND 3.0 NL**. Fixtures that excerpt it are not a free copy-paste, unlike IMGeo CC-BY.

### 3.10 Other gaps (lower but real)

- **Extensions** (Kadaster, NEN3610:2022) carry interpretation-relevant tags (`Unieke aanduiding`, *in onderzoek*). Dumping them in `extensions` without a short allowlist of known tags hides BAG “in onderzoek.”
- **Stdlib-only + optional rdflib** is fine. Do not add an MCP wrapper in MVP.
- **Personal-data non-goal** is right; BRK remains in the description’s example list (`BRK/IMKAD`) and will get asked anyway. The skill can interpret *object* data (kadastraal object) without retrieving persoonsgegevens — say so more sharply, or drop BRK from the description until IMKAD is parseable.

---

## 4. Strength of the eval plan

**Too weak to measure interpretation quality.** It would mostly measure metamodel literacy, parser success, and whether the agent cited a digest.

| Seed | What it actually measures | Verdict |
|---|---|---|
| E01 Gegevensgroep vs Gestructureerd | Spec recitation. **J**. | Cut from correctness target. Reference quiz. |
| E02 IMGeo Pand attributes | Parser + card. Right *if* the question is about IMGeo, not BAG. | Keep as a **parser** test, not an interpretation test. |
| E03 Formele historie tag on IMGeo geometrie | Tag copy. Encodes rule-10 overclaim. | Rewrite: given a PDOK *snapshot* feature and a Ja-flag, must **not** claim historical versions are present. |
| E04 gemeentecode `"0060"` | Real interpretation. | Keep. |
| E05 DMO `"1985-03"` | Real interpretation. | Keep. |
| E06 overlijdensdatum / MGW | Real interpretation. The prize case. | Keep. Assert the *conclusion* (“cannot conclude alive”), not “mentioned §5.11.” |
| E07 Keuze XOR | Real, fixture-bound. | Keep. |
| E08 abstract Contact | Real, fixture-bound. | Keep. |
| E09 PDOK `geconstateerd` + “IMGeo/BAG model” | The one live-data case, and it **mixes models**. Expected text currently allows “not determinable from given model.” | **Must become:** bind IMBAG; `N` = Indicatie Nee = not recorded via constatering; Authentiek = Basisgegeven; do **not** use IMGeo. If only IMGeo is supplied, the correct answer is refusal, not a guess. |
| E10 no model | Calibration / honesty. | Keep. |
| E11 prompt injection | Safety. | Keep, out of band. |
| E12 MIM 2.0 | Parser gate. | Keep, out of band. |
| E13 query panden na 2000 | Uses API field names and “exact enum from the data.” | Does not prove model use. Rewrite: wrong enum spelling / integer gemeente-code must fail; *bouwjaar* vs *oorspronkelijk bouwjaar* must be explained. |
| E14 Wegdeel inherited | Parser + rule 5. | Keep as parser test. |
| E15 efficiency 3.4 MB XMI | Tokens. | Keep as efficiency, not correctness. |
| E16 Referentielijst vs Codelijst | Spec recitation. | Keep as reference quiz. |
| E17 CSV map | The right *kind* of test, but no gold mapping, no denormalized columns, no homonyms. | Rebuild around PDOK `pand` → IMBAG with explicit unmapped/derived. |
| E18 afleidbaar | Good *if* the fixture actually marks the field. Synthetic flags train the agent to look for a tag that live APIs will not have. | Prefer a real derived API field with gold “unmapped/derived.” |

Ground-truth-from-digest is good **against invented element names**. It does not score “was the data interpreted correctly.” An agent can pass E02–E03, cite `IMGeo 2.2 logisch › Pand`, and still tell a journalist that `geconstateerd = N` means the building was not observed, that `gebruiksdoel` is a Pand authentic attribute, and that empty optional fields mean absence.

LLM-judge on “explanation quality” will reward mentioning MIM. Put **deterministic assertions on the conclusion**:

- Must not conclude the person is alive (E06).
- Must not treat `"0060"` as integer (E04).
- Must not bind IMGeo `Pand` to a BAG feature (new E09).
- Must label `gebruiksdoel` on `pand` as denormalized from Verblijfsobject.
- Must not treat `geconstateerd` as Authentiek.
- Must not claim PDOK items include voorkomen because a historie tag is Ja.

Arms A0/A1/A2 are the right idea. Run A0 **with** web access to IMBAG catalogus on BAG prompts, or the +25 pp target is an artefact of “A0 didn’t fetch the HTML.” A2 (references, no scripts) will likely capture most of the MGW/DMO/Keuze gains; scripts only win when the model file is large and parseable.

Description-trigger evals: keep, but they measure routing, not interpretation.

---

## 5. Verdict and recommended changes

**Build a data-interpretation loop for one live product, not a metamodel toolkit.** The design is a strong research note and an over-broad skill spec. The owner’s goal is correctness and efficiency of Q&A over open data. That is served by: (dataset → the right model → field map → apply four or five MIM rules → answer with provenance). It is not served by a generic XMI digest, 16 rules, marketplace manifests, and a BAG example wired to IMGeo.

Decide D9 before writing `mim.py`. If Geonovum/Kadaster will not publish IMBAG/IMKAD as XML or XMI, the MVP adapters must include **HTML catalog tables + SKOS + level-4 schema**, or the skill should launch as **IMGeo/BGT-only** and say so in the description.

### Keep (high impact)

1. Consume-only scope; never invent modelelementen; output contract with *model-stated / dataset-observed / inferred*.
2. Bounded digest + cards **for models that are actually parseable** (IMGeo XMI is the right first parser spike).
3. Rules 1–7, 9, 11, repaired 10, repaired 12, 14 — as executable checks, not essays.
4. SKOS waardelijst resolution.
5. Curated catalog as **(API/collection/version) → model**, with homonym warnings and dead-URL notes.
6. Honesty path when there is no model (UC12).
7. MIM 2.0 hard fail; host allowlist; prompt-injection-as-data.

### Cut or defer (low impact on the owner’s goal)

- Rule 15; MIM-RDF adapter; SPARQL/`mim:equivalent` story; query-pattern library; MCP wrapper; marketplace/plugin/Changesets **until** one dataset loop beats A0; `check` as a product surface; bilingual eval arm A3 as a gate; coordinating/replacing `geo-model`; Fietsenwinkel unless licence is cleared; “4–6 models” breadth.

### Add, ordered by impact on correct Q&A

1. **Gold mappings for one flagship product (PDOK BAG `pand` + related collections → IMBAG 2018), including denormalized, derived, and unmapped fields.** Ship as data, not as a heuristic. This is the single change that makes the skill about *data*. Repeat later for BGT/IMGeo (where XMI already exists) and only then generalize `map`.
2. **Treat HTML/PDF MIM catalogs (and Extract XSD) as first-class sources**, with fidelity `catalog-prose` / `derived-technical`. Do not wait for D9 to interpret BAG. Hand-extracted cards for IMBAG objecttypes are acceptable in MVP; a table scraper is better than an unused XMI parser.
3. **Rewrite evals around semantic conclusions on live-shaped payloads.** Kill IMGeo/BAG mixing. Add homonym tests. Score “cannot conclude,” “Basisgegeven ≠ Authentiek,” “J/N Indicatie,” “unmapped derived.” Use A0-with-web as the real baseline.
4. **Fix rules 2, 10, 12 against MIM 1.2 and IMBAG** before they are copied into SKILL.md. Add populatie, product-vs-model, homonyms, Indicatie-vs-Boolean. Instance model overrides the spec’s pedagogical examples (bouwjaar historie).
5. **Phase 1 = mapping + cards + five rules on one dataset.** Parser spike on IMGeo is still worth doing *in parallel* as infrastructure, but it is not the MVP exit. Phase 2 is generalizing adapters, not introducing `map`.

### Decision the owner should take now

| If the owner wants… | Then… |
|---|---|
| Better Q&A on **BAG/BRK-class** open data | Do not start with XMI. Start with IMBAG catalog cards + gold PDOK mappings + evals on those payloads. Ask Kadaster for XML/XMI as a parallel track, not a dependency. |
| A showcase that **MIM serializations** can drive agents | Build IMGeo-only, say so, use BGT/PDOK IMGeo collections, drop BAG from the description. |
| Both | Two explicit catalog entries, two gold maps, never one `Pand`. |

Until that choice is made, building `scripts/mim.py` for “MIM XML + EA XMI” will produce an impressive repo that does not change answers to the questions in section 2.3 of the design.
