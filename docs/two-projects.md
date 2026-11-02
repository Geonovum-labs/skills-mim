# One skill or two?

Owner question (30 Oct 2026): can one MIM skill serve both (1) interpreting models to answer data questions and (2) using MIM knowledge so agents implement information models correctly in software — or should they be two skills?

## Recommendation

**Two skills, one shared MIM core.** Do not merge both jobs into the current `geonovum-mim-interpret` SKILL.md.

Shared (one `references/mim-core` pack, not a third product):

- How to read a MIM-conformant model: objecttypen, attributen, relaties, kardinaliteit, datatypes, waardelijsten, constraints, generalisatie, populatie, homonyms, Indicatie vs Boolean, Basisgegeven ≠ Authentiek.
- Where to fetch models (RDF at modellen.geostandaarden.nl; catalogus/HTML when RDF is missing).
- Deterministic helpers that produce compact element cards.

Not shared:

| | Project 1 — interpret data | Project 2 — implement software |
|---|---|---|
| Outcome | Correct answers over published data | Code, schema, API, validation that match the model |
| Typical act | Map product fields → modelelementen, then apply interpretation rules | Map modelelementen → types, persistence, endpoints, constraints |
| Failure | Wrong `Pand`, treating codes as free text, inventing values | Inventing fields, dropping kardinaliteit, mixing IMGeo with IMBAG |
| Eval bar | Data conclusions (PDOK BAG, later BRK) | Generated artifacts vs the model |
| Out of scope | Authoring or “fixing” the model | Answering citizen/open-data questions |

A single skill with two workflows looks cheaper and will mix the success bars: a coding agent will skip mapping and “just implement”, a Q&A agent will start generating schemas. The airco prototype already showed how a knowledge-bank / validation product drifts from data Q&A.

Authoring or reviewing models (the existing `geo-model` direction) is a **third** job. Keep it out of both.

## What to keep in v1

Leave `geonovum-mim-interpret` aimed at project 1. Extract `mim-core` so project 2 can depend on the same reading layer later (`geonovum-mim-implement` or similar). Do not add an implement-in-software workflow to v1 until that second skill exists.

## Uitgangspunt (not adopted)

Names are placeholders. Repo: still follow skills-nl-sbb; either two plugins in one `Geonovum/skills-mim` repo or two repos. One repo, two skills is enough if Geonovum wants a single maintenance unit.
