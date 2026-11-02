# Additional project input (30 Oct 2026, Europe/Amsterdam)

Status: recorded only. Do not act until the owner asks.

## Existing prototype

- Path: https://github.com/Geonovum-labs/airco/tree/main/mim-kennis-skill
- Treat this as prior art for the MIM skill. Compare against it before designing or building further.

## Colleague review (to take as input, not yet applied)

Source: colleague comments on the current skill/work (quoted in the owner message of 30 Oct 2026).

1. **Call "besluiten" "uitgangspunten".** They have not been formally adopted, so they are starting points, not decisions.

2. **Test on Mistral and Copilot**, and aim to work on the smallest possible models. That implies as much deterministic control as possible — not only the SHACL validation already in the prototype.

3. **Involve modellers.** Candidates named: @pano and @Jesse Bakker. Store their answers to the 35 questions in a test suite so several LLMs can be compared against the same human gold answers.

4. **Later: combine with Sparx Enterprise Architect via MCP.** Interesting once the skill exists: https://www.sparxsystems.jp/en/MCP/

5. **Align with the nl-sbb skill setup** by Joost Farla: https://github.com/Geonovum/skills-nl-sbb

6. **Uitgangspunt: publish the needed information models as RDF**, in the same way as the models already at http://modellen.geostandaarden.nl

## Relation to earlier design questions

This input already answers or reframes some open questions from the MIM skill design:

- Repo/setup: follow `Geonovum/skills-nl-sbb`.
- Machine-readable models: do not wait for third parties; take as starting point that Geonovum publishes the needed models as RDF at `modellen.geostandaarden.nl`.
- There is already a prototype in `Geonovum-labs/airco` (`mim-kennis-skill`), including SHACL validation and 35 questions.
- Eval bar: human modeller answers + multi-LLM (including Mistral, Copilot, small models), not only large hosted models.
- EA MCP is out of MVP; interesting after the skill exists.
