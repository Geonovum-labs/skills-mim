# MIM reading rules (MIM 1.2)

How to read any MIM-conformant model. Normative source: [MIM 1.2](https://docs.geostandaarden.nl/mim/def-st-mim-20240613/) (CC-BY 4.0). Rules 2, 10 and 12 are repaired against the spec and against a real instance model.

This file has **no** Q&A workflow and **no** codegen workflow. Data-side mapping lives in `mim-interpret`. Implementation mapping will live in `mim-implement`.

Rule numbers have gaps on purpose (they follow an earlier draft). How each rule plays out in one real model: [`../examples/bag/README.md`](../examples/bag/README.md) (Example: BAG).

## 2. Blank ≠ none (repaired)

*Mogelijk geen waarde* (MGW) means a value may exist but be unknown, or it may be unclear whether a value exists (MIM *Mogelijk geen waarde*). Kardinaliteit is a separate axis. Four combinations:

| Kardinaliteit | Mogelijk geen waarde | Blank / NULL means | Example (MIM text) |
|---|---|---|---|
| `1` / `1..1` | Nee | Must not occur (invalid if missing) | An identifying attribute |
| `1` / `1..1` | Ja | Unknown; **not** “does not exist” | RSIN on old records |
| `0..1` | Nee | Known not to apply / not present | tussenvoegsel, officiële straatnaam |
| `0..1` | Ja | Unknown **or** absent — **cannot conclude** | overlijdensdatum |

`0..1` does **not** by itself mean “known not to exist”. That reading holds only with mogelijk geen waarde = Nee.

Do not encode `onbekend` as an enumeratiewaarde unless the source registry already has it.

## 3. Kardinaliteit

`1`/`1..1` always present; `*` unbounded; other ranges (`2..*`, `0..2`) mean what they say. Attribute inside a *Gegevensgroeptype*: effective kardinaliteit = group × attribute. *Generalisatie* is implicitly `1..1` and is not given a kardinaliteit.

## 4. Relations are directed

*bron* owns the stored fact. *kardinaliteit* = how many doelen per bron. *kardinaliteitBron* = how many bronnen per doel. Read *relatiemodelleringstype* (*Relatiesoort leidend* vs *Relatierol leidend*) to know where the name sits.

The inverse count (how many bronnen point at one doel) is *kardinaliteitBron*. It is not an attribuutsoort of the doel, even when a product shows it as a field.

## 5. Inheritance / abstract types

When asked what a type “has”, union own + inherited attribuutsoorten and relatiesoorten. Abstract objecttypen never appear as concrete instances; look at subtypes.

## 6. Waardelijst kind

| Kind | Behaviour |
|---|---|
| *Enumeratie* | Closed, static; model change required to add a value. Exchanged value = *naam* of the *Enumeratiewaarde*. Optional `code`/`alias` is documentation. |
| *Referentielijst* | External, evolving. Data usually holds a reference. Resolve via `locatie` in `doelformaat` (often SKOS). |
| *Codelijst* | External; structure not in the model. Only the code matters; `waarde-item` names the field. |

Use enumeratiewaarden literally, with exact spelling and case.

## 7. Datatypes

- Numbers with leading zeros are CharacterString + *patroon* / *lengte*, never Integer (`gemeentecode` `"0060"`, 16-digit object identifiers).
- `Real` approximate, `Decimal` exact.
- `Boolean` is true/false/1/0. A J/N enumeratie is **not** Boolean (rule I).
- **DMO** / **DTMO** (*Datum mogelijk onvolledig*): `YYYY`, `YYYY-MM`, `YYYY-MM-DD` are legitimate. Do not parse as a full Date.
- *lengte* and *patroon* apply on top of the datatype.
- **Model type wins over a product JSON type.** A JSON integer for a field the model types as `Year` is still a Year.

## 8. Gestructureerd datatype vs Gegevensgroep

A *Gestructureerd datatype* is one composite value (parts are not separate facts, no per-part history). A *Gegevensgroep* is a named set of separate attribuutsoorten (they do have their own history). Effective kardinaliteit multiplies.

MIM's test: leave the datatype out of the model — if no meaning is lost, only the structure of the value, it is a Gestructureerd datatype (e.g. `Bedrag` = hoeveelheid + muntsoort). If a part can be missing or unknown without changing the meaning of the other parts, those parts are separate attribuutsoorten in a Gegevensgroep. This holds for all datatypes: they describe structure, not meaning (see [`mim-core.md`](mim-core.md#uitgangspunten-of-mim)).

## 9. Keuze = XOR

Exactly one alternative. Two filled = invalid. The Keuze name is not a field (MIM §2.3.7.2). A Keuze adds no new features and removes none: the features of the object stay the same, and in data only the chosen alternative appears. Constraints are the other XOR/OR vehicle (plain text + optional formal spec) — do not ignore them.

MIM describes five use cases. Which one applies tells you what the Keuze is bound to:

| # | Choice between | Bound to |
|---|---|---|
| 1 | datatypes of one attribuutsoort | the attribuutsoort |
| 2 | two or more attribuutsoorten, each meaningful | the objecttype (the Keuze name is not an attribuutsoort) |
| 3 | several ways to fill one meaningful attribuutsoort | the attribuutsoort: the Keuze is its type |
| 4 | several target objecttypen of one meaningful relatiesoort (relatiedoelen) | the relatiesoort |
| 5 | two or more relatiesoorten/relatierollen, each meaningful | the objecttype or gegevensgroeptype |

## 10. Historie flags are conceptual (repaired)

MIM 1.2: *heeft tijdlijn geldigheid* “geeft op conceptueel niveau **niet** aan dat er voor het gegeven een tijdlijn geldigheid wordt bijgehouden in de administratie. Het geeft aan dat een eigenschap kan veranderen en er op de tijdlijn geldigheid verschillende waarden kunnen bestaan.” *Indicatie materiële/formele historie* is the 1.x alias (to be phased out in 2.x). Parsers must accept both names.

Field names (`beginGeldigheid`, `tijdstipRegistratie`, `voorkomen`, …) are implementation, not MIM. Whether a product actually serves earlier versions is a product fact; check the data, not the flag.

**The instance model beats the spec's teaching examples.** When the MIM text uses an example (“bouwjaar → tijdlijn geldigheid Nee”) and the bound model tags that element differently, follow the bound model.

## 11. Derived (`indicatieAfleidbaar`)

Recomputable from other elements; not independent evidence. If a derived value disagrees with its sources, trust the sources.

## 12. Identificerend / Authentiek (repaired)

*identificerend* (or a combination, possibly including a relation) = join / dedup key.

*Authentiek* is a **value range**, not a boolean (MIM *Toegestane waarden metagegevens*):

`Authentiek` | `Basisgegeven` | `Wettelijk gegeven` | `Landelijk kerngegeven` | `Overig`

Only `Authentiek` carries the statutory gebruiksplicht. **Basisgegeven ≠ Authentiek.**

The MIM explanation text lists `Gemeentelijk kerngegeven` instead of `Wettelijk gegeven`. Use the table above; see [I2 in known-ambiguities.md](known-ambiguities.md).

## 13. Definitions have provenance

Use *herkomstDefinitie* and *begrip*. Element definition (information) ≠ begrip definition (domain/legal). For *Extern* / *View*, the source model's semantics apply.

A begrippenkader (level 1, often SKOS) is useful for begrippen. It is not a substitute for the attribuutsoorten of the information model.

## 14. Conceptueel vs logisch

A conceptual model (level 2) may be technology-neutral. A logical model (level 3) is closer to implementation. Prefer the model that actually describes the subject. Do not skip a conceptual model because there is no XMI or RDF.

In Linked Data the difference shrinks: a logical model expressed in RDF/RDFS/OWL/SHACL is also a conceptual model, and MIM advises the type *conceptueel* for a model that needs both a UML and a Linked Data form. Do not read a difference in type between two expressions of the same model as a difference in content.

## Extra reading rules

### P. Populatie

*Populatie* says which instances are in the registration: which real-world things are included, and whether records remain after the thing is gone. Read it before concluding that something “does not exist” because it is absent from the data.

### H. Homonyms

The same name in different models is not the same element. The elements may still be related, and may describe the same real-world object.

- **Bind the model of this dataset first**, then the element. That model alone supplies the definitie, kardinaliteit, waardelijst and attribuutsoorten.
- **Never substitute** another model's definitie, kardinaliteit, waardelijst or attributes for the bound element, and never answer from the other model as if it were this dataset's model.
- **Do say when elements are likely related**, e.g. both describe the same kind of real-world object. Label that *inferred* unless a model states it.
- **Use an explicit link when the models state one**: a reference or identifier attribute pointing to the other model's object, a generalisatie to a shared supertype (e.g. NEN 3610), an *Externe koppeling*, or a stated relation or equivalence. Cite it as *model-stated*.

Example: IMGeo `Pand` and IMBAG `Pand` are different elements that both describe buildings. IMGeo `Pand` carries `identificatieBAGPND`, an explicit reference to the identificatie of the IMBAG pand.

### I. J/N enumeratie vs Boolean

A value `"N"` from an enumeratie such as *Indicatie* `{J, N}` is an enumeratiewaarde (Nee), not JSON `false`. Read its meaning from the definition of the attribuutsoort, not from the everyday meaning of “no”.

### L. Levenscyclus vs historie

A `status` attribuutsoort often records a life-cycle phase. voorkomens / tijdlijnen are history. Do not mix them: a life-cycle value is not a time-axis.

Rule 15 (order not significant) is paper-only and omitted. Rule 16 is a parser gate (MIM 2.0 vocabulary), not a reading rule — see [`mim-core.md`](mim-core.md).
