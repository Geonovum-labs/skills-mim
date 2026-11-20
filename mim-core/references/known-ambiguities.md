# Known ambiguities in MIM 1.2

Places where the MIM 1.2 text says two different things, or names one thing two ways. Reading a model that touches one of these is where an agent is most likely to be silently wrong.

**Behaviour.** Do not resolve an ambiguity silently. Read the bound model as published, say that the MIM text is ambiguous here, state which reading you used, and label it *inferred*. Do not "correct" a model because of an ambiguity in the standard.

**Status: preliminary.** I1–I5 were first collected in the airco prototype ([`mim-kennis-skill/overdracht.md` §8](https://github.com/Geonovum-labs/airco/blob/main/mim-kennis-skill/overdracht.md)). On 2026-11-19 the contradicting passages were found in the source texts of [Geonovum/MIM-Werkomgeving](https://github.com/Geonovum/MIM-Werkomgeving) (`master`), and the key phrases of each also occur in `DEF-mim-20240613.html`, the vastgestelde version. The readings below are proposals. They are not confirmed by a MIM modeller or by MIM-beheer.

| # | Ambiguity | Preliminary reading when reading a model |
|---|---|---|
| I1 | What a *Gegevensgroeptype* may contain. The definition text says it may contain attribuutsoorten, relatiesoorten and further gegevensgroeptypen; the richtlijn says it contains only attribuutsoorten. | The richtlijn is a modelling recommendation. When reading, accept what the bound model actually contains and do not call it invalid. |
| I2 | Value range of *Authentiek*. The explanation lists `Authentiek`, `Basisgegeven`, `Landelijk kerngegeven`, **`Gemeentelijk kerngegeven`**, `Overig`. The table of allowed values lists `Authentiek`, `Basisgegeven`, **`Wettelijk gegeven`**, `Landelijk kerngegeven`, `Overig`. | Treat the table of allowed values as the value range (this is what [reading rule 12](reading-rules.md) uses). If a model carries `Gemeentelijk kerngegeven`, quote it literally and note that it is outside the table. Only `Authentiek` carries the gebruiksplicht. |
| I3 | Which element carries *Aggregatietype*. The explanation says it is modelled with an *Attribuutsoort*; the stated application is *Relatiesoort* and *Externe koppeling*, and the UML and Linked Data tables put it on the relation. | Read it as a metagegeven of a relation (Relatiesoort, Externe koppeling): `Compositie`, `Gedeeld` or `Geen` (default). Do not look for it on an attribuutsoort. |
| I4 | Spelling. The UML stereotype and the Linked Data class are *Gestructuurd datatype* / `mim:GestructuurdDatatype`; the prose says *Gestructureerd datatype*. | The same element. Accept both spellings when matching names. |
| I5 | How a model instance links to the class it is turned into. The introduction example uses `rdfs:seeAlso`; the Linked Data chapter and the transformation annex use `mim:equivalent` (and `mim:seeAlso` once). | All three point from a promoted class or shape back to the originating MIM element. Cite them as *model-stated* links. Do not read `mim:equivalent` as OWL equivalence. |

## How to use this

- Rule 12 (Authentiek) and rule 14 (conceptueel vs logisch) in [`reading-rules.md`](reading-rules.md) already follow the readings above. This file explains why they are phrased as they are.
- If you meet another place where the MIM text contradicts itself, report it the same way: what is ambiguous and which reading you used. Reporting upstream goes through [Geonovum/MIM-Werkomgeving](https://github.com/Geonovum/MIM-Werkomgeving/issues) or `mim@geonovum.nl`; that is for the skill owner to decide, not for the agent.
