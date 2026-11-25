# mim-combi — leesmij voor beheerders

Samenvoeging van twee MIM-skills, gemaakt om naast beide te testen en te vergelijken. Agents beginnen bij `SKILL.md`; dit bestand is voor wie de skill bijhoudt.

- Versie: 0.1.0, status **concept** (25 november 2026).
- Eigenaar: Mats Braster (Geonovum).
- Bronnen van de samenvoeging:
  - **mim-kennis 0.1.0** (23 november 2026): kennisbank over MIM 1.2 met letterlijke brontekst, gegevens en `scripts/mim.py`. Ongewijzigd overgenomen.
  - **geonovum-mim-interpret en mim-core** uit Geonovum-labs/skills-mim (30 oktober 2026, aangevuld tot 20 november 2026): leesregels, werkwijze voor datavragen, formaten, sjablonen, scripts, BAG-voorbeeld en evaluatievragen. Vertaald naar het Nederlands, gecontroleerd tegen MIM 1.2 en ingepast.
- Uitgangspunten en voortgang: Claude-project "MIM kennis skills" en het logboek (Claude Doc).

## Opbouw

```
mim-combi/
├── SKILL.md                     grondregels, routekeuze A (kennisvraag) / B (datavraag), sjablonen
├── modelelementen/ onderwerpen/ onderscheidingen/ uitdrukkingen/
├── metagegevens.md versies.md bekende-onduidelijkheden.md woordenlijst.md
├── bron/ data/ assets/          letterlijke MIM-tekst, gegevens, mim.ttl      (route A, uit mim-kennis)
├── modellen-lezen/              leesregels, datavragen, model-vinden, formaten, buiten-mim  (route B)
├── sjablonen/                   lege JSON-sjablonen voor een nieuw model     (route B)
├── voorbeelden/bag/             PDOK BAG pand → IMBAG 2018                   (route B)
├── evaluatie/                   algemene evaluatievragen voor datavragen     (route B)
├── scripts/                     mim.py (route A), mim_data.py (route B), check_kennisbank.py
└── beheer/                      schrijfwijzer, rooktests, verpakken (niet in het skillpakket)
```

## Wat er bij het samenvoegen is gebeurd

| Onderdeel skills-mim | In mim-combi | Wijziging |
|---|---|---|
| `mim-interpret/SKILL.md` | `SKILL.md` route B, `modellen-lezen/datavragen.md` | Nederlands; samengevoegd met de grondregels van mim-kennis |
| `mim-core/references/reading-rules.md` | `modellen-lezen/leesregels.md` | Hernummerd tot LR1–LR18; citaten met paragraaf toegevoegd en door `check_kennisbank.py` gecontroleerd; beweringen die niet uit MIM komen gelabeld |
| `mim-core/references/mim-core.md` | grotendeels al in de kennisbank; rest in `modellen-lezen/leesregels.md` en `modellen-lezen/model-vinden.md` | Geen apart bestand |
| `mim-core/references/known-ambiguities.md` | `bekende-onduidelijkheden.md` (I1–I19, uit mim-kennis) | Ruimere set; lezingen voor modellen lezen in `modellen-lezen/leesregels.md`, laatste paragraaf |
| `mim-core/references/fetch.md` | `modellen-lezen/model-vinden.md` | Nederlands; catalogusgegevens niet opnieuw gecontroleerd |
| references/model-catalog.md, field-mapping-format.md, element-summary-format.md | `modellen-lezen/modelcatalogus.md`, `modellen-lezen/veldkoppeling.md`, `modellen-lezen/elementsamenvatting.md` | Nederlands |
| references/interpretation-rules.md, conflicts.md | `modellen-lezen/datavragen.md`, `modellen-lezen/buiten-mim.md` | Nederlands |
| `mim_core.py` + `mim_interpret.py` | `scripts/mim_data.py` | Eén script met Nederlandse opdrachten (`catalogus`, `koppel`, `samenvatting`, `waardelijst`, `rdf-labels`); exitcode 1 + "NIET GEVONDEN" zoals `mim.py`; Python 3.8+ |
| sjablonen en BAG-voorbeeld | `sjablonen/`, `voorbeelden/bag/` | Proza Nederlands; **JSON-sleutels en koppeltypen Engels gelaten**, zodat bestanden van skills-mim uitwisselbaar blijven |
| `evals/` + `examples/bag/evals.json` | `evaluatie/`, `voorbeelden/bag/evaluatie.json` | Alleen `about` en `conclusion` vertaald; `must`/`must_not` ongewijzigd voor een eerlijke vergelijking |
| `docs/`, `mim-implement/`, plugin-manifests, `publiccode.yml` | niet overgenomen | Ontwerpgeschiedenis en stub, geen skillinhoud |

## Controleren en testen

```bash
python3 scripts/check_kennisbank.py     # citaten, §-verwijzingen, links, tabellen, about-velden, modelcatalogi
python3 beheer/test_scripts.py          # rooktests voor mim.py en mim_data.py
```

## Verpakken

```bash
python3 beheer/verpak.py <uitvoermap>
```

Maakt `mim-combi.skill` (zip van deze map zonder `beheer/`) en draait eerst de controle.

## Herbouwen

De gegenereerde onderdelen van de kennisbank (`bron/`, `data/`, `woordenlijst.md`, gegenereerde blokken) komen uit mim-kennis. Herbouw ze daar met `beheer/bouw/bouw_alles.py` en kopieer ze hierheen, zodat beide skills dezelfde kennisbank houden.

## Licenties

- MIM-tekst (map `bron/` en alle citaten): CC BY 4.0, © Geonovum.
- `assets/mim.ttl` en `assets/mim-shapes.ttl`: uit Geonovum/MIM-Werkomgeving.
- IMBAG-voorbeeld: parafrases van de IMBAG Catalogus 2018 (CC BY-ND 3.0 NL).
- Eigen tekst en scripts: EUPL-1.2 (voorstel; skills-mim gebruikt EUPL-1.2).
