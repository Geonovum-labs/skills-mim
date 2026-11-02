# Evals

Goal of these cases: **conclusions about data**, not MIM metamodel literacy.

Format follows the Agent Skills eval idea (`prompt`, `must`, `must_not`, `conclusion`). Template: [`../templates/evals.template.json`](../templates/evals.template.json).

| File | Cases |
|---|---|
| [`generic-evals.json`](generic-evals.json) | Model-independent calibration: mogelijk geen waarde, no-model fallback. |
| [`../examples/bag/evals.json`](../examples/bag/evals.json) | Example: BAG — ten cases on PDOK BAG `pand` → IMBAG 2018. |

Model-specific cases live next to their example, so a new model brings its own `evals.json`.

## How to run (later)

Run each case with and without the skill: A0 web access only, A1 skill, A2 references only. The A0 baseline **must** be allowed to fetch the model's published catalogus; otherwise a large gap only shows that the baseline did not open the source.

## How to score

Deterministic assertions on the **conclusion**. An answer that names the right model but still reads the value wrongly **fails**.

Generic checks that every model-specific suite should include:

- Binds the model of this product; does not take definitie, kardinaliteit or waardelijst from a same-named element in another model; does say when that element likely describes the same real-world object, and uses an explicit link between the models when one exists.
- Does not read a J/N enumeratiewaarde as Boolean.
- Reads blank values with kardinaliteit × mogelijk geen waarde (rule 2), not as “does not exist”.
- Labels fields copied from a related objecttype as `denormalized`, and product-computed fields as `derived` / `unmapped`.
- Does not claim the data holds history because a historie flag is Ja.
- Keeps identifiers with leading zeros as text.
- Distinguishes Authentiek from Basisgegeven.
- Uses the no-model fallback when no model is bound.

## Not yet

- Reference answers from modellers (candidates: Pano, Jesse Bakker).
- Multi-LLM runs (Mistral, Copilot, small models).
- airco's 35 questions. Those target explaining MIM; they were **planned** in airco `uitgangspunten.md` U19 and were not present as files on 2026-10-30. Keep them as a separate suite if they ship.
