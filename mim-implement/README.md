# geonovum-mim-implement (stub)

**Not built yet.** There is no `SKILL.md` here on purpose: do not treat this folder as a ready agent skill.

## Purpose (when it exists)

Read a MIM-conformant information model and **implement it correctly in software** — types, persistence, endpoints, constraints, validation — so generated artefacts match the model. Typical act: map modelelementen → code/schema/API. Failure modes to prevent: inventing fields, dropping kardinaliteit, mixing up same-named elements from different models (they may be related, but are not interchangeable).

This is **not** the interpret skill. It will not answer citizen or open-data questions about data. It will not author or “fix” models.

## Depends on mim-core

When built, this plugin will depend on the sibling pack [`../mim-core/`](../mim-core/README.md) for:

- how to read MIM (objecttypen, attributen, relaties, kardinaliteit, datatypes, waardelijsten, constraints, generalisatie, populatie, homonyms, J/N enumeratie vs Boolean, Basisgegeven ≠ Authentiek);
- where to fetch RDF / catalogus;
- element summaries (short fixed-format summary per model element).

Do not duplicate those rules here. Do not follow [`../mim-interpret/SKILL.md`](../mim-interpret/SKILL.md) as if it were an implementation workflow.

## Status

Stub only (30 Oct 2026). Names are placeholders (`geonovum-mim-implement`). Shared repo: `Geonovum-labs/skills-mim` (this repository).
