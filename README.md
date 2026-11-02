# skills-mim (v1 outline)

Agent-skills van [Geonovum](https://www.geonovum.nl) voor [MIM](https://docs.geostandaarden.nl/mim/mim/), het Metamodel Informatiemodellering. Ze werken voor elk MIM-conform informatiemodel en elke dataset die zo'n model beschrijft.

**Twee plugins, één gedeelde MIM-kern** (afgesproken 30 Oct 2026). Auteur van modellen is een derde job en zit in geen van beide.

Dit is versie 0.1, status `concept`, geschreven in de Project store als voorloper van een later te publiceren repository `Geonovum/skills-mim`. Er is **geen** GitHub-repo aangemaakt in deze stap. Inrichting volgt [Geonovum/skills-nl-sbb](https://github.com/Geonovum/skills-nl-sbb) voor zover dat dit doel dient (plugin manifests, `publiccode.yml`, `DISCLAIMER.md`, EUPL-1.2, status `concept`).

> **Let op.** De skills zijn hulpmiddelen en maken geen deel uit van de standaard. MIM 1.2 en het gepubliceerde informatiemodel van de dataset zijn leidend. Zie [DISCLAIMER.md](DISCLAIMER.md).

## Plugins

| Plugin | Status | Doel |
| --- | --- | --- |
| [`mim-interpret/`](mim-interpret/SKILL.md) (`geonovum-mim-interpret`) | concept | Interpreteert MIM-conforme informatiemodellen zodat vragen over de data die die modellen beschrijven correcter en efficiënter beantwoord worden. Consume-only. |
| [`mim-implement/`](mim-implement/README.md) (`geonovum-mim-implement`) | stub | Een MIM-model lezen om het correct in software te implementeren. **Nog niet gebouwd** — alleen deze README, geen `SKILL.md`. |
| [`mim-core/`](mim-core/README.md) | pack (geen skill) | Gedeelde leeslaag: MIM lezen, RDF/catalogus ophalen, elementsamenvattingen. Geen Q&A-workflow, geen codegen-workflow. |

De status `concept` betekent dat de skill nog niet is vastgesteld. Een hogere status vraagt een expertreview, een gepubliceerde reviewprocedure met acceptatiecriteria, en een test met minstens twee assistenten waarvan één open source of Europees (zelfde lat als [skills-nl-sbb](https://github.com/Geonovum/skills-nl-sbb)).

**Doel van interpret (vast).** Help agents interpret MIM-conformant information models so they can answer questions about the data those models describe more correctly and more efficiently. The model is the lens; the data questions are the outcome.

## Wat v1 wel en niet is

**Wel.** Generieke leesregels en een generieke werkwijze voor elk MIM-conform model: product → model (modelcatalogus) → velden (vastgestelde veldkoppeling) → elementsamenvattingen → MIM-regels → antwoord over de data. Vaste formaten en lege sjablonen (`templates/`) voor modelcatalogus, veldkoppeling, elementsamenvattingen en evals. Optionele deterministische hulpscripts (Python, alleen standaardbibliotheek) zonder ingebouwde modelkennis. Eén uitgewerkt voorbeeld: **BAG** (zie hieronder).

**Niet.** Modellen schrijven of valideren (dat is het doel van de prior-art `mim-kennis-skill` in airco, niet van deze skills). Geen implement-in-software-workflow tot `mim-implement` bestaat. Geen marketplace-scaffolding, geen query-templates, geen EA-MCP, geen MIM-RDF-als-enig-formaat. RDF op [modellen.geostandaarden.nl](http://modellen.geostandaarden.nl) is de voorkeursbron **wanneer het het model van dit product is**. Als die RDF er niet is, is de HTML/PDF-catalogus van de modelbeheerder first-class.

## Begrippen

De skill gebruikt MIM-termen in hun MIM-betekenis. Daarnaast een paar eigen werktermen (volledige lijst in [`mim-interpret/SKILL.md`](mim-interpret/SKILL.md#words-used-in-this-skill)):

| Term | Betekenis |
| --- | --- |
| **Vastgestelde veldkoppeling** (*verified field mapping*) | Een handmatig gecontroleerde tabel die elk veld van een dataproduct koppelt aan het modelelement dat het representeert. Voorheen "gouden mapping". |
| **Elementsamenvatting** (*element summary*) | Een korte samenvatting in vaste vorm van één modelelement (definitie, type, kardinaliteit, mogelijk geen waarde, authentiek, historie, waardelijst), zodat de agent niet het hele model hoeft te lezen. Voorheen "elementkaart". |
| **Modelcatalogus** | Lijst van welk informatiemodel welk dataproduct beschrijft, en welke modellen met gelijknamige elementen niet als model van dat product gebruikt mogen worden. |
| **Koppeltype** (*mapping type*) | Hoe een veld zich tot het element verhoudt: `direct`, `renamed`, `denormalized` (overgenomen van een ander objecttype), `derived`, `technical`, `unmapped`, `homonym-rejected`. |
| **Homoniem** | Zelfde naam in verschillende modellen is niet hetzelfde element, maar ze kunnen wel verwant zijn en hetzelfde object in de werkelijkheid beschrijven. De agent leest definitie, kardinaliteit en waardelijst alleen uit het model van déze dataset, zegt wanneer elementen waarschijnlijk verwant zijn, en gebruikt een expliciete koppeling als de modellen die geven. Bijvoorbeeld: `Pand` in IMGeo en `Pand` in IMBAG beschrijven allebei gebouwen; IMGeo verwijst met `identificatieBAGPND` naar het BAG-pand. |

## Waarom Python?

De skill bevat twee kleine hulpscripts. Die doen alleen opzoekwerk in vaste JSON-bestanden: welk model hoort bij dit product, op welk modelelement komt dit veld uit, wat staat er in de elementsamenvatting, welke waarden heeft deze waardelijst. Ze interpreteren niets; dat doet de agent. Kleine taalmodellen (Mistral, Copilot, kleine lokale LLM's) maken fouten bij het opzoeken in lange tabellen. Een script geeft elke keer exact hetzelfde antwoord. Dat is het uitgangspunt *deterministische sturing*.

De scripts bevatten zelf geen modelkennis: je geeft het bestand van het model mee (`--catalog`, `--summaries`). Ze zijn ook optioneel. Kan de agent geen Python draaien, dan leest hij dezelfde JSON-bestanden (of de Markdown-versies in `references/`) direct. [`mim-interpret/SKILL.md`](mim-interpret/SKILL.md#helper-scripts) noemt per opdracht welk bestand dat is.

## Layout (deze map = latere repo-root)

```text
docs/skill/                          # deze map; later: Geonovum/skills-mim
├── README.md                        # dit bestand (twee plugins + shared core)
├── DISCLAIMER.md
├── LICENSE                          # EUPL-1.2
├── publiccode.yml
├── .claude-plugin/plugin.json
├── .plugin/plugin.json              # Cursor-manifest (displayName); zie nota
├── mim-core/                        # shared pack, geen SKILL.md
│   ├── README.md
│   ├── references/                  # mim-core, reading-rules, fetch, element-summary-format
│   ├── templates/                   # leeg sjabloon elementsamenvattingen
│   ├── scripts/mim_core.py          # summary | values | rdf-labels
│   └── examples/bag/                # Voorbeeld BAG: IMBAG-elementsamenvattingen, regels toegepast
├── mim-interpret/                   # skill geonovum-mim-interpret
│   ├── SKILL.md
│   ├── README.md
│   ├── references/                  # interpretation-rules, model-catalog, field-mapping-format, conflicts
│   ├── templates/                   # lege sjablonen: modelcatalogus, veldkoppeling, evals
│   ├── scripts/mim_interpret.py     # catalog | map (+ summary/values/rdf-labels via mim-core)
│   ├── evals/                       # generieke eval-spec + generieke cases
│   └── examples/bag/                # Voorbeeld BAG: catalogus, veldkoppeling, Q&A, evals
└── mim-implement/                   # stub only
    └── README.md
```

**Nota `.cursor-plugin/`.** skills-nl-sbb heeft identieke manifests in `.plugin/` en `.cursor-plugin/`. Deze store kan `.cursor-plugin/` niet aanmaken. Bij publicatie naar GitHub: kopieer `.plugin/plugin.json` naar `.cursor-plugin/plugin.json`. In de latere GitHub-repo kunnen de plugins onder `skills/` komen te staan, zoals bij NL-SBB; v1 houdt `mim-interpret/` en `mim-implement/` naast `mim-core/` zodat de split zichtbaar is.

Niet in v1 (bewust): `generate_plugin.py`, Changesets, GitHub workflows, marketplace-listing, query-templates, Imvertor/XSD-kopieën, EA-MCP, implement-SKILL.md.

## Installeren (later)

Via de [skills-marketplace van developer.overheid.nl](https://github.com/developer-overheid-nl/skills-marketplace) als plugin `geonovum-mim`, zodra de skill die lat haalt. Nu: kopieer `mim-interpret/` **samen met** sibling `mim-core/` naar de skillmap van de assistent. `mim-implement/` is geen laadbare skill.

## Gebruik (interpret)

Vraag de assistent wat een veld of code in een dataset betekent, of hoe records zich tot het informatiemodel verhouden. De agent zoekt het model bij het product, zoekt de velden op in de vastgestelde veldkoppeling en past MIM-regels toe.

Voorbeeldprompts:

- Wat betekent waarde `N` in dit veld?
- Is dit veld een attribuut van dit objecttype, of komt het van een ander objecttype?
- Het veld is leeg. Betekent dat dat er geen waarde is?

Zonder skill raadt een agent vanaf kolomnamen. Met skill leest hij kardinaliteit, mogelijk geen waarde, waardelijst en authentiek uit het model van precies dit product.

Fidelity zegt uit wat voor bron de modelkennis komt: `rdf`, `catalog-prose` (HTML/PDF-catalogus), `skos`, `derived-technical` (een API-schema) of `ea-xmi`.

## Een nieuw model toevoegen

Geen scriptwijziging nodig. Vul de sjablonen in:

1. Modelcatalogus: `mim-interpret/templates/model-catalog.template.json` (uitleg: `mim-interpret/references/model-catalog.md`).
2. Vastgestelde veldkoppeling per product: `mim-interpret/templates/field-mapping.template.json` (uitleg: `mim-interpret/references/field-mapping-format.md`).
3. Elementsamenvattingen van het model: `mim-core/templates/element-summaries.template.json` (uitleg: `mim-core/references/element-summary-format.md`).
4. Evals: `mim-interpret/templates/evals.template.json` (uitleg: `mim-interpret/evals/README.md`).

## Voorbeeld: BAG

Eén uitgewerkt voorbeeld laat de hele werkwijze zien: PDOK BAG OGC API v2, collectie `pand` → IMBAG Catalogus 2018 (HTML-catalogus, geen gepubliceerde MIM-RDF). Het staat apart, zodat de generieke bestanden er niet van afhangen:

- [`mim-interpret/examples/bag/`](mim-interpret/examples/bag/README.md) — modelcatalogus, vastgestelde veldkoppeling, uitgewerkte Q&A, tien evals;
- [`mim-core/examples/bag/`](mim-core/examples/bag/README.md) — IMBAG-elementsamenvattingen, bronnen, en de leesregels toegepast op IMBAG.

Laatst gecontroleerd: 2026-10-30.

## Requirements

- Optioneel: Python 3.10+ voor `mim-core/scripts/mim_core.py` en `mim-interpret/scripts/mim_interpret.py` (alleen standaardbibliotheek). Zonder Python werkt de skill ook; de agent leest dan de JSON-bestanden.
- Netwerk optioneel (met lokale catalogus-, veldkoppeling- en samenvattingsbestanden werkt alles offline).
- Geen telemetry; fetch alleen naar een host-allowlist.

## Relatie tot de standaard en andere skills

| Bron | Rol |
| --- | --- |
| [MIM 1.2, vastgesteld 13 juni 2024](https://docs.geostandaarden.nl/mim/def-st-mim-20240613/) | Normatieve tekst (`nl.gov.source`) |
| [MIM, laatste versie](https://docs.geostandaarden.nl/mim/mim/) | Controleren of er een nieuwere versie is |
| [modellen.geostandaarden.nl](http://modellen.geostandaarden.nl) | Uitgangspunt: benodigde informatiemodellen als RDF |
| [Geonovum/skills-nl-sbb](https://github.com/Geonovum/skills-nl-sbb) | Layout, metadata, disclaimer, statusladder |
| [airco `mim-kennis-skill`](https://github.com/Geonovum-labs/airco/tree/main/mim-kennis-skill) | Prior art met **ander doel** (MIM uitleggen / modelleren). Zie `mim-interpret/references/conflicts.md`. |
| `skills-geo/geo-model` | Authoring-gericht; overlap in triggers, niet in product. Niet vervangen in v1. |

Issues over de standaard MIM horen in [Geonovum/MIM-Werkomgeving](https://github.com/Geonovum/MIM-Werkomgeving). Helpdesk: `mim@geonovum.nl`.

## Evaluatie

Generieke eval-spec en cases in `mim-interpret/evals/`; de BAG-cases staan bij het voorbeeld. Conclusies over data, geen metamodel-quiz. Referentieantwoorden van modelleurs (kandidaten: Pano, Jesse Bakker) en runs op Mistral / Copilot / kleine modellen komen later. De 35 vragen uit airco zijn daar **gepland** (`uitgangspunten.md` U19) maar stonden op 2026-10-30 niet als bestanden in de repo. Eval-lat voor implement (artefact vs model) bestaat nog niet.

## Licentie

Copyright © 2026 Geonovum. Licensed under the EUPL.

De skills vallen onder [EUPL-1.2](LICENSE). MIM zelf valt onder CC-BY 4.0 van Geonovum. Elementsamenvattingen parafraseren de bron en verwijzen ernaar wanneer de licentie van een modelcatalogus geen afgeleid werk toestaat (zoals IMBAG, CC-BY-ND 3.0 NL, in het voorbeeld).

## English summary

This folder is the v1 outline of `Geonovum/skills-mim`: two plugins and one shared MIM reading pack. `geonovum-mim-interpret` uses any MIM-conformant information model as a lens on the data it describes; model knowledge lives in data files (model catalog, verified field mapping, element summaries) with templates for new models, and one worked example (BAG: PDOK `pand` → IMBAG 2018) sits in `examples/bag/`. `mim-core` is how to read MIM, fetch RDF/catalogus, and look up element summaries — no Q&A, no codegen. The Python helpers are optional deterministic lookups; agents without Python read the same JSON files. `geonovum-mim-implement` is a stub only (read a MIM model to implement it correctly in software; not built). RDF is preferred when it is the model of the product; HTML catalogs are first-class when it is not. Not for authoring or validating models. Status `concept`. No GitHub repository was created in this step.

## Bijdragen

Fouten in de skill: later via issues op `Geonovum/skills-mim`. Fouten in MIM: [Geonovum/MIM-Werkomgeving](https://github.com/Geonovum/MIM-Werkomgeving). Contact: Linda van den Brink, Geonovum.
