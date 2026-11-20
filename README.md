# MIM-skills

Agent-skills van [Geonovum](https://www.geonovum.nl) voor [MIM](https://docs.geostandaarden.nl/mim/mim/), het Metamodel Informatiemodellering. Ze werken voor elk MIM-conform informatiemodel en elke dataset die zo'n model beschrijft.

Een agent-skill is een map met een instructiedocument (`SKILL.md`) dat een AI-assistent erbij pakt zodra het onderwerp langskomt. De skills staan in de repository van de standaardbeheerder. De metadata staat in `publiccode.yml` en in de frontmatter van elke skill, en de status per skill staat in `nl.gov.status`.

> **Let op.** De skills zijn hulpmiddelen en maken geen deel uit van de standaard. MIM 1.2 en het gepubliceerde informatiemodel van de dataset zijn leidend. Zie [DISCLAIMER.md](DISCLAIMER.md).

> **Nog niet vastgesteld.** Alle onderdelen in deze repository hebben de status `concept`. Het is niet vastgesteld dat de skills goed werken: er is geen expertreview geweest, geen modelleur heeft de veldkoppelingen en referentieantwoorden gecontroleerd, en de skills zijn nog niet getest met meerdere assistenten. De eerste versie is met behulp van AI gemaakt (zie `nl.gov.generated-with` in de frontmatter) en nog niet inhoudelijk beoordeeld. Gebruik de uitkomsten niet zonder controle in een situatie waar ze ertoe doen.

## Skills

| Skill | Status | Doel |
| --- | --- | --- |
| [`geonovum-mim-interpret`](mim-interpret/SKILL.md) | concept | Interpreteert MIM-conforme informatiemodellen zodat vragen over de data die die modellen beschrijven correcter en efficiënter beantwoord worden. Zoekt het model bij een dataset, koppelt de velden aan modelelementen en past de MIM-leesregels toe op de waarden. Schrijft, wijzigt of valideert geen modellen. |
| [`geonovum-mim-implement`](mim-implement/README.md) | stub | Een MIM-model lezen om het correct in software te implementeren. **Nog niet gebouwd**: alleen een README, geen `SKILL.md`, dus niet bruikbaar door een agent. |
| [`mim-core`](mim-core/README.md) | gedeelde laag (geen skill) | Hoe je MIM leest, waar je modellen ophaalt en het formaat van elementsamenvattingen. Gedeeld door beide skills. Geen vraag-en-antwoordworkflow en geen codegeneratie. |

De status `concept` betekent dat de skill nog niet is vastgesteld. Een hogere status vraagt een expertreview, een gepubliceerde reviewprocedure met acceptatiecriteria, en een test met minstens twee assistenten waarvan één open source of Europees. Dat is dezelfde lat als bij [skills-nl-sbb](https://github.com/Geonovum/skills-nl-sbb).

Wat daarvan ontbreekt:

- **Expertreview:** nog niet gedaan.
- **Veldkoppeling:** de BAG-veldkoppeling is gecontroleerd tegen de IMBAG-catalogus en een PDOK-voorbeeld, niet door een modelleur.
- **Referentieantwoorden:** de evals bevatten nog geen antwoorden van modelleurs.
- **Meerdere assistenten:** nog niet getest. De skill is ontworpen voor meer dan één model, maar daar is nog geen run voor gedaan (bijvoorbeeld Mistral, Copilot of een klein lokaal model).
- **Reviewprocedure:** nog niet gepubliceerd, en er zijn nog geen acceptatiecriteria.

Auteur van modellen is een derde taak en zit in geen van beide skills.

## Installeren

De skills worden later aangeboden via de [skills-marketplace van developer.overheid.nl](https://github.com/developer-overheid-nl/skills-marketplace) als plugin `geonovum-mim`, zodra ze de lat voor een hogere status halen. Nu is dat nog niet zo.

Zonder marketplace: kopieer de map `mim-interpret/` **samen met** de naastgelegen map `mim-core/` naar de skillmap van je assistent. Welke map dat is, staat in de documentatie van de assistent. De skill verwijst naar `../mim-core/`, dus beide mappen moeten naast elkaar staan. `mim-implement/` is geen laadbare skill.

## Gebruik

Vraag je assistent wat een veld of code in een dataset betekent, of hoe records zich tot het informatiemodel verhouden. De skill zoekt het model bij het product, zoekt de velden op in de veldkoppeling en past de MIM-regels toe.

Voorbeeldvragen:

- Wat betekent waarde `N` in dit veld?
- Is dit veld een attribuut van dit objecttype, of komt het van een ander objecttype?
- Het veld is leeg. Betekent dat dat er geen waarde is?

Zonder skill raadt een assistent vanaf kolomnamen. Met skill leest hij kardinaliteit, mogelijk geen waarde, waardelijst en authentiek uit het model van precies dit product.

Python is optioneel. Zie [Waarom Python?](#waarom-python) hieronder.

## Een nieuw model toevoegen

Geen scriptwijziging nodig. Vul de sjablonen in:

1. Modelcatalogus: [`mim-interpret/templates/model-catalog.template.json`](mim-interpret/templates/model-catalog.template.json) (uitleg: [`model-catalog.md`](mim-interpret/references/model-catalog.md)).
2. Veldkoppeling per product: [`mim-interpret/templates/field-mapping.template.json`](mim-interpret/templates/field-mapping.template.json) (uitleg: [`field-mapping-format.md`](mim-interpret/references/field-mapping-format.md)).
3. Elementsamenvattingen van het model: [`mim-core/templates/element-summaries.template.json`](mim-core/templates/element-summaries.template.json) (uitleg: [`element-summary-format.md`](mim-core/references/element-summary-format.md)).
4. Evals: [`mim-interpret/templates/evals.template.json`](mim-interpret/templates/evals.template.json) (uitleg: [`evals/README.md`](mim-interpret/evals/README.md)).

## Voorbeeld: BAG

Eén uitgewerkt voorbeeld laat de hele werkwijze zien: PDOK BAG OGC API v2, collectie `pand`, gekoppeld aan de IMBAG Catalogus 2018 (HTML-catalogus; er is geen gepubliceerde MIM-RDF van de BAG). Het staat apart, zodat de generieke bestanden er niet van afhangen:

- [`mim-interpret/examples/bag/`](mim-interpret/examples/bag/README.md): modelcatalogus, veldkoppeling, uitgewerkte vraag en antwoord, en tien evals.
- [`mim-core/examples/bag/`](mim-core/examples/bag/README.md): IMBAG-elementsamenvattingen, bronnen, en de leesregels toegepast op IMBAG.

Laatst gecontroleerd: 2026-10-30. Het voorbeeld is niet door een BAG-modelleur beoordeeld.

## Begrippen

De skill gebruikt MIM-termen in hun MIM-betekenis. Daarnaast zijn er een paar eigen werktermen. De volledige lijst staat in [`mim-interpret/SKILL.md`](mim-interpret/SKILL.md#words-used-in-this-skill).

| Term | Betekenis |
| --- | --- |
| **Veldkoppeling** (*field mapping*) | Een tabel die elk veld van een dataproduct koppelt aan het modelelement dat het representeert. In deze versie opgesteld met behulp van AI en nog niet door een modelleur vastgesteld. |
| **Elementsamenvatting** (*element summary*) | Een korte samenvatting in vaste vorm van één modelelement (definitie, type, kardinaliteit, mogelijk geen waarde, authentiek, historie, waardelijst), zodat de agent niet het hele model hoeft te lezen. |
| **Modelcatalogus** | Lijst van welk informatiemodel welk dataproduct beschrijft, en welke modellen met gelijknamige elementen niet als model van dat product gebruikt mogen worden. |
| **Koppeltype** (*mapping type*) | Hoe een veld zich tot het element verhoudt: `direct`, `renamed`, `denormalized` (overgenomen van een ander objecttype), `derived`, `technical`, `unmapped`, `homonym-rejected`. |
| **Homoniem** | Zelfde naam in verschillende modellen is niet hetzelfde element, maar ze kunnen wel verwant zijn en hetzelfde object in de werkelijkheid beschrijven. De agent leest definitie, kardinaliteit en waardelijst alleen uit het model van déze dataset, zegt wanneer elementen waarschijnlijk verwant zijn, en gebruikt een expliciete koppeling als de modellen die geven. Bijvoorbeeld: `Pand` in IMGeo en `Pand` in IMBAG beschrijven allebei gebouwen; IMGeo verwijst met `identificatieBAGPND` naar het BAG-pand. |
| **Fidelity** (*bronkwaliteit*) | Uit wat voor bron de modelkennis komt: `rdf`, `catalog-prose` (HTML/PDF-catalogus), `skos`, `derived-technical` (een API-schema) of `ea-xmi`. |

## Waarom Python?

De skill bevat twee kleine hulpscripts. Die doen alleen opzoekwerk in vaste JSON-bestanden: welk model hoort bij dit product, op welk modelelement komt dit veld uit, wat staat er in de elementsamenvatting, welke waarden heeft deze waardelijst. Ze interpreteren niets; dat doet de agent. Kleine taalmodellen maken fouten bij het opzoeken in lange tabellen. Een script geeft elke keer exact hetzelfde antwoord. Dat is het uitgangspunt *deterministische sturing*.

De scripts bevatten zelf geen modelkennis: je geeft het bestand van het model mee (`--catalog`, `--summaries`). Ze zijn ook optioneel. Kan de agent geen Python draaien, dan leest hij dezelfde JSON-bestanden (of de Markdown-versies in `references/`) direct. [`mim-interpret/SKILL.md`](mim-interpret/SKILL.md#helper-scripts) noemt per opdracht welk bestand dat is.

Vereist voor de scripts: Python 3.10 of hoger, alleen de standaardbibliotheek. Er is geen telemetrie; ophalen gebeurt alleen van een lijst toegestane hosts, en met lokale bestanden werkt alles offline.

## Indeling van de repository

```text
.
├── README.md
├── DISCLAIMER.md
├── LICENSE                          # EUPL-1.2
├── publiccode.yml
├── .claude-plugin/plugin.json       # plugin-manifest
├── .cursor-plugin/plugin.json       # plugin-manifest (identiek aan .plugin/)
├── .plugin/plugin.json              # plugin-manifest
├── docs/                            # ontwerpgeschiedenis (zie hieronder)
├── mim-core/                        # gedeelde laag, geen SKILL.md
│   ├── README.md
│   ├── references/                  # mim-core, reading-rules, known-ambiguities, fetch, element-summary-format
│   ├── templates/                   # leeg sjabloon voor elementsamenvattingen
│   ├── scripts/mim_core.py          # summary | values | rdf-labels
│   └── examples/bag/                # voorbeeld BAG
├── mim-interpret/                   # skill geonovum-mim-interpret
│   ├── SKILL.md
│   ├── README.md
│   ├── references/                  # interpretation-rules, model-catalog, field-mapping-format, conflicts
│   ├── templates/                   # lege sjablonen: modelcatalogus, veldkoppeling, evals
│   ├── scripts/mim_interpret.py     # catalog | map (+ summary/values/rdf-labels via mim-core)
│   ├── evals/                       # generieke eval-spec en cases
│   └── examples/bag/                # voorbeeld BAG
└── mim-implement/                   # stub
    └── README.md
```

De map `docs/` bevat de ontwerpnotities uit de ontwikkeling, zoals ze zijn vastgelegd: ontwerp en review, de keuze voor twee skills met een gedeelde kern, projectcontext, aanvullende input en het wijzigingsoverzicht van 30 oktober 2026. Ze beschrijven de ontwikkeling en zijn geen onderdeel van de skills. Ze gebruiken deels oudere termen (zoals "gouden mapping" en "elementkaart").

Niet in deze versie, bewust: `generate_plugin.py`, Changesets, GitHub workflows, marketplace-listing, querysjablonen, Imvertor- of XSD-kopieën, EA-MCP en een `SKILL.md` voor implement.

## Relatie tot de standaard en andere skills

| Bron | Rol |
| --- | --- |
| [MIM 1.2, vastgesteld 13 juni 2024](https://docs.geostandaarden.nl/mim/def-st-mim-20240613/) | Normatieve tekst waarop de skills zijn gebouwd (`nl.gov.source`) |
| [MIM, laatste versie](https://docs.geostandaarden.nl/mim/mim/) | Startpunt om te controleren of er een nieuwere versie is |
| [catalog.modeldesk.io/geonovum](https://catalog.modeldesk.io/geonovum) | Experimentele publieke catalogus met informatiemodellen van Geonovum (onder meer IMBAG, IMGeo en NEN 3610:2022, MIM 1.2, werkversies zonder release). In de experimentele setting de eerste plek waar de skill een model zoekt. |
| [modellen.geostandaarden.nl](http://modellen.geostandaarden.nl) | Voorkeursbron voor informatiemodellen als RDF, wanneer het het model van het product is. Zonder RDF is de HTML- of PDF-catalogus van de modelbeheerder gelijkwaardig. |
| [Geonovum/skills-nl-sbb](https://github.com/Geonovum/skills-nl-sbb) | Voorbeeld voor indeling, metadata, disclaimer en statusladder |
| [airco `mim-kennis-skill`](https://github.com/Geonovum-labs/airco/tree/main/mim-kennis-skill) | Eerder werk met een iets ander doel (MIM uitleggen en modelleren). Zie [`conflicts.md`](mim-interpret/references/conflicts.md). |
| `skills-geo/geo-model` | Gericht op het maken van modellen. Overlap in triggers, niet in doel. Niet vervangen door deze skills. |

Alleen MIM 1.x wordt ondersteund. Modellen in MIM 2.0-vocabulaire worden niet gelezen. Waar de skill regels toepast die MIM zelf niet geeft (koppelen van data aan modelelementen), staat dat met reden in [`conflicts.md`](mim-interpret/references/conflicts.md).

## Evaluatie

De eval-spec en generieke cases staan in [`mim-interpret/evals/`](mim-interpret/evals/README.md); de BAG-cases staan bij het voorbeeld. De cases toetsen conclusies over data, geen kennis van het metamodel. De evals zijn nog niet uitgevoerd op meerdere assistenten en bevatten nog geen referentieantwoorden van modelleurs. De eerdere vragenlijst van 35 vragen uit airco is gepland maar niet als bestand overgenomen. Een evalmaat voor implement bestaat nog niet.

## Bijdragen

Fouten in een skill meld je als [issue](https://github.com/Geonovum-labs/skills-mim/issues). Fouten in de standaard zelf horen in [Geonovum/MIM-Werkomgeving](https://github.com/Geonovum/MIM-Werkomgeving/issues). Vragen over MIM kunnen naar `mim@geonovum.nl`. Contactpersoon voor deze skills: Linda van den Brink, Geonovum.

## Licentie

Copyright © 2026 Geonovum. Licensed under the EUPL.

De skills vallen onder de [EUPL-1.2](LICENSE). Alle taalversies van de EUPL zijn gelijkwaardig; de [Nederlandse tekst](https://eur-lex.europa.eu/legal-content/NL/TXT/?uri=CELEX:32017D0863) staat in het Publicatieblad van de EU. De standaard MIM zelf valt onder CC-BY 4.0 van Geonovum. Elementsamenvattingen parafraseren de bron en verwijzen ernaar wanneer de licentie van een modelcatalogus geen afgeleid werk toestaat (zoals IMBAG, CC-BY-ND 3.0 NL, in het voorbeeld).
