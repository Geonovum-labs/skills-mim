# Project context

## Goal

Help agents interpret MIM-conformant information models so they can answer questions about the data those models describe more correctly and more efficiently. A MIM model of the BAG, for example, should help an agent answer questions using BAG data.

The model is the lens; the data questions are the outcome. This differs from a skill that mainly authors or validates models.

The skill should live in a new GitHub repo under the Geonovum organization.

## Two skills (agreed 30 Oct 2026)

Two skills, one shared MIM reading core. Project 1 is `geonovum-mim-interpret` (goal above). Project 2 (implement models correctly in software) is a later skill, stub only for now. Authoring models is a third job. One `Geonovum/skills-mim` repo with two plugins is enough. Detail: [two-projects.md](/cursor/stores/bc-b13693ec-4022-437c-9694-059d7338cbfe/docs/two-projects.md).

## Uitgangspunten (not formally adopted)

Recorded 30 Oct 2026 from the owner and a colleague. Treat as starting points until the owner says otherwise.

- Compare with the existing prototype in [Geonovum-labs/airco `mim-kennis-skill`](https://github.com/Geonovum-labs/airco/tree/main/mim-kennis-skill). The goal above is not the prior-art goal.
- Follow the setup of [Geonovum/skills-nl-sbb](https://github.com/Geonovum/skills-nl-sbb).
- Publish the needed information models as RDF, in the same way as existing models at http://modellen.geostandaarden.nl
- Test on Mistral and Copilot, and aim to work on the smallest possible models. Prefer deterministic control, not only SHACL.
- Capture modeller reference answers (candidates: Pano, Jesse Bakker) to the 35 questions in a test suite for multi-LLM comparison.
- Combining the skill with Sparx Enterprise Architect via [MCP](https://www.sparxsystems.jp/en/MCP/) is interesting later, not MVP.

## Open

- Geonovum repo creation still waits for the owner.
