# Wijzigingen MIM-skill, 30 oktober 2026

Doel van deze ronde: de skill leesbaar maken voor een informatiemodelleur zonder programmeerachtergrond, zonder de instructies voor agents af te zwakken. Het vastgestelde doel en de opzet met twee skills en een gedeelde kern zijn niet veranderd. Er is geen nieuwe functionaliteit bijgekomen.

## Nieuwe namen

| Was | Wordt | Waarom |
| --- | --- | --- |
| gouden mapping / gold table / gold map | **vastgestelde veldkoppeling** (*verified field mapping*) | "Gold" is vakjargon uit de testwereld. De nieuwe naam zegt wat het is: een handmatig gecontroleerde tabel die elk veld van een dataproduct (PDOK BAG `pand`) koppelt aan het modelelement dat het representeert. |
| elementkaart / element card | **elementsamenvatting** (*element summary*) | Een korte samenvatting in vaste vorm van één modelelement (definitie, type, kardinaliteit, mogelijk geen waarde, authentiek, historie, waardelijst), zodat de agent niet het hele model hoeft te lezen. |
| `mim-core/assets/imbag-cards.json` | `mim-core/assets/imbag-element-summaries.json` | Bestandsnaam volgt de nieuwe term. |
| scriptopdracht `card` | `summary` | Idem. `card` werkt nog, zodat oude instructies niet breken. |
| JSON-sleutel `goldMapping` (in `model-catalog.json`) | `verifiedMapping` | Idem. |
| interpret-regels `1`, `M`, `11+` | **D1, D2, D3** (dataregels) | De oude nummering was onlogisch en botste met de nummering van de MIM-leesregels. |
| "honesty path" | "no-model fallback" | Uitgeschreven: geen model gevonden → zeg dat, label het antwoord als afgeleid, verzin geen elementen. |
| "digest", "skim" | "geladen modelbron", "snelle labelscan" | Minder jargon. |
| afkorting MGW | uitgeschreven: *mogelijk geen waarde* | Alleen in de MIM-leesregels staat de afkorting nog, met uitleg. |
| "gold answers" van modelleurs | **referentieantwoorden** van modelleurs | Zelfde reden als "gouden mapping". |

## Wat er verder is veranderd

1. **Uitleg waarom er Python in zit.** In `SKILL.md` (Engels) en in de README (Nederlands, sectie "Waarom Python?"). Kort: de scripts doen alleen opzoekwerk in vaste JSON-bestanden en geven elke keer exact hetzelfde antwoord. Ze interpreteren niets. Dat helpt kleine taalmodellen (Mistral, Copilot, kleine LLM's), die fouten maken bij het opzoeken in lange tabellen. Dit is het uitgangspunt *deterministische sturing*.
2. **De skill werkt ook zonder Python.** `SKILL.md` heeft een tabel die per opdracht zegt welk bestand de agent dan zelf leest en welke sleutel hij opzoekt. De JSON-bestanden beginnen nu met een veld `about` dat in één zin uitlegt wat erin staat. In `compatibility` staat Python nu als optioneel.
3. **Begrippenlijst.** Bovenaan `SKILL.md` staat "Words used in this skill": de eigen werktermen van de skill (dataproduct, modelcatalogus, model koppelen, vastgestelde veldkoppeling, koppeltype, overgenomen/denormalized, elementsamenvatting, homoniem, fidelity, bewijslabels, snapshot, M0 / niveau 4, no-model fallback), met Nederlandse vertaling. De README heeft een korte Nederlandse versie.
4. **Eerlijk over de status van de veldkoppeling.** "Vastgesteld" betekent hier: gecontroleerd tegen de IMBAG-catalogus en een live PDOK-voorbeeld. Een review door een modelleur moet nog gebeuren. Dat staat nu in `bag-imbag-mapping.md` en in de lijst "What v1 will still get wrong" in `conflicts.md`.
5. **Kleinere verbeteringen.** Kolomkoppen in de BAG-tabel uitgeschreven ("Mogelijk geen waarde", "Historie materieel / formeel"). De scriptuitvoer schrijft `mogelijkGeenWaarde` en `historie materieel/formeel` voluit. De lijst met toegestane hosts in `SKILL.md` noemt nu ook `imbag.github.io` (stond al in het script). Plugin-manifesten en `publiccode.yml` gebruiken de nieuwe termen.

## Wat niet is veranderd

- Alle regels voor agents (nooit elementen verzinnen, IMGeo `Pand` weigeren voor BAG, MIM 2.0 stoppen, bewijslabels, outputcontract) staan er nog, in dezelfde volgorde.
- `SKILL.md` blijft kort (150 regels) en verwijst voor details door naar de referentiebestanden.
- Geen implement-skill, geen GitHub-repo.

## Controle

Alle scriptopdrachten opnieuw gedraaid (`catalog`, `map`, `summary`, de oude naam `card`, `values`, `rdf-labels`, foutgevallen). Alle JSON-bestanden zijn geldig. Alle interne links in de Markdown-bestanden werken.

Oudere ontwerpdocumenten (`mim-skill-design.md`, `mim-skill-design-review.md`, `two-projects.md`) gebruiken nog de oude termen. Die zijn bewust niet aangepast, omdat ze de geschiedenis van het ontwerp vastleggen.

## Tweede ronde: generiek in plaats van BAG

Feedback van Linda: de skill is voor elk MIM-conform model en elke dataset, niet alleen voor de BAG. De regels en de werkwijze waren te veel op BAG geschreven.

**Wat generiek is geworden.**

- `SKILL.md`: beschrijving, tags, doel, begrippenlijst, werkwijze, dataregels D1–D3, outputcontract en fouttabel noemen geen BAG, PDOK of Pand meer. De homoniemregel is algemeen: *dezelfde naam in verschillende modellen is niet hetzelfde element*, met één kort voorbeeld (IMGeo `Pand` is niet IMBAG `Pand`).
- MIM-leesregels (`mim-core/references/reading-rules.md`), het compacte metamodel en de ophaalregels: alleen nog algemene uitleg en voorbeelden uit de MIM-tekst zelf. Regel I heet nu "J/N-enumeratie is geen Boolean".
- De hulpscripts bevatten geen modelkennis meer. Je geeft altijd het bestand van het model mee: `--catalog <bestand>` voor modelcatalogus en veldkoppeling, `--summaries <bestand>` voor elementsamenvattingen. `imbag.github.io` staat niet meer in de standaardlijst van toegestane hosts (meegeven met `--allow`).
- Nieuwe formaatbeschrijvingen en lege sjablonen, zodat een nieuw model zonder scriptwijziging kan worden toegevoegd:
  - `mim-interpret/references/model-catalog.md` + `templates/model-catalog.template.json`
  - `mim-interpret/references/field-mapping-format.md` + `templates/field-mapping.template.json`
  - `mim-core/references/element-summary-format.md` + `mim-core/templates/element-summaries.template.json`
  - `mim-interpret/templates/evals.template.json`
- Evals: `mim-interpret/evals/README.md` is nu een algemene eval-spec met algemene controles. De twee modelonafhankelijke cases staan in `evals/generic-evals.json`.
- README, `publiccode.yml`, pluginmanifesten, stub-README en disclaimer zijn algemeen geformuleerd. De README heeft een korte sectie "Een nieuw model toevoegen".

**Wat naar de voorbeeldmap is verhuisd (Voorbeeld: BAG).**

| Was | Wordt |
| --- | --- |
| `mim-core/assets/imbag-element-summaries.json` | `mim-core/examples/bag/imbag-element-summaries.json` |
| BAG-illustraties in de leesregels, BAG-bronnen en dode BAG-links in `fetch.md` | `mim-core/examples/bag/README.md` |
| `mim-interpret/assets/model-catalog.json` | `mim-interpret/examples/bag/model-catalog.json` |
| `mim-interpret/assets/bag-pdok-pand-mapping.json` | `mim-interpret/examples/bag/pdok-bag-pand-mapping.json` |
| `mim-interpret/references/bag-imbag-mapping.md` | `mim-interpret/examples/bag/pdok-bag-pand-mapping.md` |
| `mim-interpret/examples/pdok-bag-pand.md` | `mim-interpret/examples/bag/worked-example.md` |
| `mim-interpret/evals/evals.json` (tien BAG-cases) | `mim-interpret/examples/bag/evals.json` |
| BAG-tabel "Ondersteunde modellen", BAG-hiaten en IMBAG-licentie | `mim-interpret/examples/bag/README.md` |

De mappen `assets/` bestaan niet meer. Elke voorbeeldmap heeft een eigen README met "Example: BAG" en de opdrachten om het voorbeeld te draaien. De generieke bestanden verwijzen alleen naar het voorbeeld; ze hangen er niet van af.

**Waar BAG nog genoemd wordt, en waarom.** Alleen in de voorbeeldmappen, in verwijzingen met het label "Example: BAG", en in het ene homoniemvoorbeeld. `pdok.nl` en `kadaster.nl` staan nog in de standaardlijst van toegestane hosts, omdat het algemene overheidsbronnen zijn met veel datasets. Het vaste doel in `project-context.md` is ongewijzigd.

**Controle.** Alle opdrachten opnieuw gedraaid, voor het BAG-voorbeeld en voor de sjablonen: `catalog`, `map` (ook met een onbekend veld), `summary`, `card`, `values`, `rdf-labels`, plus de foutgevallen (geen `--catalog`/`--summaries`, product zonder veldkoppeling, onbekend element, host niet toegestaan). Alle JSON-bestanden zijn geldig. Alle links en alle bestandsverwijzingen in de catalogi werken.

**Homoniemregel verfijnd (Linda).** Zelfde naam in verschillende modellen is niet hetzelfde element, maar ze kunnen wel verwant zijn en hetzelfde object in de werkelijkheid beschrijven: de agent neemt geen definitie, kardinaliteit of waardelijst over uit het andere model, zegt wél wanneer elementen waarschijnlijk verwant zijn, en gebruikt een expliciete koppeling (identificatie-verwijzing, NEN 3610-generalisatie, externe koppeling) als die er is; eval E-BAG-08 verwacht geen botte weigering meer.
