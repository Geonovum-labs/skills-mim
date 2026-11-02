# Verified field mapping format

A *verified field mapping* (vastgestelde veldkoppeling) is a hand-checked table linking each field of one data product to the model element it represents. One JSON file per product. Template: [`../templates/field-mapping.template.json`](../templates/field-mapping.template.json). Filled-in example: [`../examples/bag/pdok-bag-pand-mapping.json`](../examples/bag/pdok-bag-pand-mapping.json) with a readable version in [`../examples/bag/pdok-bag-pand-mapping.md`](../examples/bag/pdok-bag-pand-mapping.md) (Example: BAG).

The mapping is outside MIM: MIM does not cover the data itself (M0) or technical formats (level 4). Label mapping claims as mapping, not as *model-stated*.

## File

| Key | Meaning |
|---|---|
| `about` | One sentence on what the file contains. |
| `product`, `model` | Product id and model id, as in the model catalog. |
| `lastVerified` | Date the mapping was checked. |
| `checkedAgainst` | What it was checked against (model source, sample records). |
| `reviewedBy` | Modeller who reviewed it, or `null` while review is pending. |
| `fields` | One row per product field. |

## One row

| Key | Meaning |
|---|---|
| `field` | Field name exactly as in the product. |
| `mappingType` | `direct`, `renamed`, `denormalized`, `derived`, `technical`, `unmapped`, `homonym-rejected` ([definitions](interpretation-rules.md#mapping-types)). |
| `element` | `Objecttype.attribuut` in the model, or `null`. For `denormalized`, the element of the *other* objecttype. |
| `modelName`, `waardelijst` | Model name when renamed; waardelijst name when the value comes from a list. |
| `confidence` | `exact`, `probable`, or `none`. |
| `reasons` | Short tags for why the row is what it is. |
| `notes` | Warning against a likely misreading. |

A field not listed counts as `unmapped`. Never fill a gap by name-matching.

## How to make one

1. Bind the model with the model catalog.
2. Take a real sample record and the product's field list (schema, queryables).
3. For each field, find the element in the model source and check type, kardinaliteit and waardelijst.
4. Mark fields that belong to another objecttype as `denormalized`, computed fields as `derived`, transport fields as `technical`.
5. Record `checkedAgainst`; ask a modeller to review and fill `reviewedBy`.
