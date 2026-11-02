# geonovum-mim-interpret

Skill: interpret MIM-conformant information models so agents can answer questions about the data those models describe more correctly and more efficiently. Works for any MIM-conformant model and any dataset it describes.

Depends on the sibling pack [`../mim-core/`](../mim-core/README.md). Do not copy core reading rules into this plugin.

- Agent instruction: [`SKILL.md`](SKILL.md) (glossary of the skill's own terms at the top)
- Formats: [`references/model-catalog.md`](references/model-catalog.md), [`references/field-mapping-format.md`](references/field-mapping-format.md); templates in [`templates/`](templates/)
- Evals: [`evals/README.md`](evals/README.md)
- Example: BAG (PDOK BAG `pand` → IMBAG 2018): [`examples/bag/README.md`](examples/bag/README.md)
- Repo context: [`../README.md`](../README.md)
- Not this skill: implementing a model in software — stub [`../mim-implement/`](../mim-implement/README.md)

Generic files never depend on `examples/`. To support a new model, fill in the templates; no script changes are needed.
