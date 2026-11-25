---
name: mim-kennis
description: >-
  Kennisbank over MIM 1.2 (Metamodel Informatie Modellering, Geonovum, vastgesteld
  13 juni 2024): modelelementen, metagegevens, afspraken en regels, en de
  uitdrukking in UML en Linked Data, met letterlijke brontekst en opzoekscripts.
  Gebruik bij elke vraag over MIM of over een informatiemodel volgens MIM, ook als
  het woord MIM niet valt: objecttype, attribuutsoort, gegevensgroep(type),
  relatiesoort, relatierol, relatieklasse, externe koppeling, generalisatie,
  datatype, enumeratie, referentielijst, codelijst, keuze, constraint, package,
  view, metagegeven, stereotype, tagged value, kardinaliteit, mogelijk geen
  waarde, authentiek, historie, tijdlijn geldigheid, conceptueel of logisch
  informatiemodel, beschouwingsniveau, mim:-vocabulaire, MIM-toolbox, Imvertor.
  Niet voor MIM-extensies (Kadaster, NEN 3610) of MIM 2.x.
license: EUPL-1.2
compatibility: Python 3.8+ (alleen standaardbibliotheek) voor de optionele scripts. Zonder Python werkt de kennisbank ook; zie "Zonder scripts".
metadata:
  version: "0.1.0"
  nl.gov.status: concept
  nl.gov.review-by: "2027-05-23"
  nl.gov.source: https://docs.geostandaarden.nl/mim/def-st-mim-20240613
  nl.gov.source-license: CC-BY-4.0
  nl.gov.category: standaarden
  nl.gov.tags: mim, informatiemodel, metamodel, geostandaarden, uml, linked-data
  nl.gov.generated-with: Claude (Anthropic), 2026-11-23
---

# mim-kennis: kennis over MIM 1.2

> **Status: concept (0.1.0, 23 november 2026).** Hulpmiddel bij de standaard MIM, geen onderdeel ervan. Niet gereviewd door MIM-modelleurs en nog niet getest op meerdere assistenten. De gepubliceerde MIM 1.2 is leidend: <https://docs.geostandaarden.nl/mim/def-st-mim-20240613>. Overheden die generatieve AI inzetten, volgen het Overheidsbreed standpunt voor de inzet van generatieve AI.

Deze skill helpt vragen over MIM correct te **beantwoorden en uit te leggen**. De kennis is ook bruikbaar bij modelleren, toetsen of transformeren, maar daar is versie 0.1 niet op ontworpen.

## Grondregels

Volg deze regels altijd, in deze volgorde.

1. **De kennisbank gaat boven je eigen kennis over MIM.** Wijkt wat je denkt te weten af van de kennisbank, volg dan de kennisbank.
2. **Alles geldt voor MIM 1.2.** Gaat een vraag over een andere versie, zeg dat en lees `versies.md`.
3. **Opzoeken gaat vóór redeneren.** Wat een script of tabel kan vaststellen (paragraaf, metagegeven, kardinaliteit, waarde, default, term), zoek je op. Verzin nooit een paragraafnummer, metagegeven, waarde of citaat.
4. **Staat het er niet in, zeg dat eerst.** Regelt MIM 1.2 iets niet, of staat het niet in de kennisbank, schrijf dan eerst: "Dit staat niet in MIM 1.2" of "Dit staat niet in deze kennisbank". Eigen kennis mag daarna alleen met het label "Niet uit MIM 1.2:".
5. **Houd drie soorten tekst uit elkaar** in je antwoord: letterlijke MIM-tekst die normatief is, letterlijke MIM-tekst die niet normatief is (voorbeeld, noot), en uitleg.
6. **Citeer alleen letterlijke tekst uit de kennisbank**, met paragraafnummer. Letterlijke tekst staat in een blockquote die eindigt op "— MIM 1.2, §…", of in de map `bron/`. Al het andere in de kennisbank is uitleg.
7. **Geef MIM-begrippen nooit een UML-betekenis.** UML is alleen een notatie voor MIM (§1.8). Een relatiesoort is geen "UML-associatie", een objecttype geen "UML-klasse".
8. **Los tegenstrijdigheden in MIM niet zelf op.** Staat het onderwerp in `bekende-onduidelijkheden.md`, noem dan beide vindplaatsen en de voorlopige lezing. Vind je een nieuwe tegenstrijdigheid, meld die.
9. **Geen officieel oordeel.** Je mag uitleggen wat MIM over een model zegt, maar je geeft geen conformiteitsverklaring.
10. **Buiten scope:** MIM-extensies (Kadaster, NEN 3610 en andere) en MIM 2.x. Zeg dat de kennisbank die niet bevat.

## Werkwijze

1. Bepaal waar de vraag over gaat met de tabel **Waar staat het?** hieronder.
2. Kan een script het opzoeken, gebruik dan eerst het script (zie **Scripts**). Kun je geen scripts draaien, gebruik **Zonder scripts**.
3. Open het genoemde bestand. Lees alleen wat je nodig hebt; elk bestand begint met **In het kort**.
4. Zoek de definitie of regel als citaat op. Neem het citaat letterlijk over met de paragraaf.
5. Kijk of het onderwerp in `bekende-onduidelijkheden.md` staat.
6. Schrijf het antwoord volgens het **Antwoordsjabloon**.

## Waar staat het?

| De vraag gaat over | Eerst (met Python) | Dan lezen |
|---|---|---|
| wat een modelelement is (objecttype, keuze, view, …) | `scripts/mim.py element <naam>` | `modelelementen/<naam>.md` |
| het verschil tussen twee modelelementen | | zie **Onderscheidingen** hieronder |
| welke metagegevens een element heeft, of ze verplicht zijn | `scripts/mim.py metagegeven <element> [<metagegeven>]` | `modelelementen/<naam>.md` paragraaf 4, `metagegevens.md` |
| wat een metagegeven betekent | `scripts/mim.py zoek <metagegeven>` | `metagegevens.md`, kop met de naam |
| toegestane waarden of default van een metagegeven | `scripts/mim.py waarden <metagegeven>` | `metagegevens.md` paragraaf 3 |
| een onbekende term, synoniem, Engelse term of afkorting | `scripts/mim.py zoek <term>` | `woordenlijst.md` |
| conceptueel, logisch, beschouwingsniveaus, wat een metamodel is | | `onderwerpen/beschouwingsniveaus.md` |
| historie, tijdlijn geldigheid of registratie | | `onderwerpen/historie.md` |
| de vijf use cases van keuze | | `onderwerpen/keuze.md` |
| waardelijsten in het algemeen | | `onderwerpen/waardelijsten.md` |
| mogelijk geen waarde, verplicht of optioneel | | `onderwerpen/mogelijk-geen-waarde.md` |
| abstracte objecttypen | | `onderwerpen/abstracte-objecttypen.md` |
| relatiesoort leidend of relatierol leidend | | `onderwerpen/relatiemodellering.md` |
| primitieve, landelijke en zelfgedefinieerde datatypen | | `onderwerpen/datatypen.md` |
| naamgeving, unieke namen, CamelCase | | `onderwerpen/naamgeving.md` |
| begrippen, definities, stelselcatalogus | | `onderwerpen/begrippen-en-definities.md` |
| extensies op MIM | | `onderwerpen/extensies.md` |
| UML, stereotypes, Enterprise Architect, Imvertor | | `uitdrukkingen/uml.md` |
| Linked Data, RDF, SHACL, `mim:`, transformatie naar OWL | | `uitdrukkingen/linked-data.md` |
| verschil tussen MIM-versies | | `versies.md` |
| een tegenstrijdigheid of twijfel over de tekst | | `bekende-onduidelijkheden.md` |
| de exacte tekst van een paragraaf | `scripts/mim.py paragraaf <nr>` | `bron/` (zie **Zonder scripts**) |

### Onderscheidingen

| Twijfel tussen | Bestand |
|---|---|
| gegevensgroep en gestructureerd datatype (en attribuutsoort, data-element, referentie-element) | `onderscheidingen/gegevensgroep-vs-gestructureerd-datatype.md` |
| enumeratie, referentielijst en codelijst | `onderscheidingen/enumeratie-vs-referentielijst-vs-codelijst.md` |
| relatieklasse en objecttype | `onderscheidingen/relatieklasse-vs-objecttype.md` |
| attribuutsoort en relatiesoort | `onderscheidingen/attribuutsoort-vs-relatiesoort.md` |
| relatiesoort, externe koppeling, view en extern | `onderscheidingen/relatiesoort-externe-koppeling-view-extern.md` |
| keuze en constraint | `onderscheidingen/keuze-vs-constraint.md` |
| object, objecttype en gegeven | `onderscheidingen/object-objecttype-gegeven.md` |

### Modelelementen

Eén bestand per MIM-metaclass in `modelelementen/`, met steeds dezelfde opbouw: In het kort, 1 Definitie, 2 Uitleg, 3 Uitdrukking in UML en Linked Data, 4 Metagegevens en bindingen, 5 Voorbeeld en tegenvoorbeeld, 6 Wordt vaak verward met.

| Groep | Bestanden |
|---|---|
| Kern | `objecttype`, `attribuutsoort`, `gegevensgroep`, `gegevensgroeptype`, `generalisatie`, `relatiesoort`, `relatieklasse`, `relatierol`, `externe-koppeling` |
| Datatypen | `datatype`, `primitief-datatype`, `gestructureerd-datatype`, `data-element` |
| Waardelijsten | `enumeratie`, `enumeratiewaarde`, `referentielijst`, `referentie-element`, `codelijst` |
| Packages | `package`, `informatiemodel`, `domein`, `extern`, `view` |
| Overig | `constraint`, `keuze`, `modelelement` |

## Scripts

Alleen Python-standaardbibliotheek. Draai vanuit de map van deze skill. Optie `--json` geeft machineleesbare uitvoer. Exitcode 1 en de tekst "NIET GEVONDEN" betekenen: het bestaat niet in MIM 1.2 of niet in de kennisbank. Pas dan grondregel 4 toe.

```bash
python3 scripts/mim.py paragraaf 2.3.2.1            # letterlijke tekst van §2.3.2.1
python3 scripts/mim.py paragraaf 5.8 --met-sub       # met alle subparagrafen
python3 scripts/mim.py zoek voidable                 # term, synoniem of Engelse term
python3 scripts/mim.py element "gestructureerd datatype"
python3 scripts/mim.py metagegeven attribuutsoort kardinaliteit
python3 scripts/mim.py metagegeven relatiesoort --variant "alt 2"
python3 scripts/mim.py waarden authentiek
python3 scripts/mim.py lijst elementen
```

`scripts/check_kennisbank.py` controleert de kennisbank zelf (citaten, verwijzingen, tabellen). Dat is voor beheerders, niet om vragen te beantwoorden.

## Zonder scripts

| Script | Zonder Python |
|---|---|
| `paragraaf <nr>` | Zoek `<nr>` op in `bron/paragrafen.json` (veld `bestand`). Zoek in dat bestand de kop die begint met `§<nr> `. De tekst loopt tot de volgende kop. |
| `zoek <term>` | Zoek in `woordenlijst.md` in de kolommen Term, Ook genoemd en Engels. |
| `element <naam>` | Open `modelelementen/<naam>.md`, of zoek in `data/elementen.json`. |
| `metagegeven <element> …` | Tabel in paragraaf 4 van `modelelementen/<element>.md`, of `data/metagegevens.csv` (kolommen `element` en `metagegeven`, scheidingsteken `;`). |
| `waarden <metagegeven>` | Tabel in paragraaf 3 van `metagegevens.md`, of `data/waardebereik.json`. |

## Antwoordsjabloon

Gebruik deze vorm. Laat een onderdeel weg als het niet van toepassing is, maar nooit de bron.

```markdown
**Antwoord.** <1 tot 3 zinnen in gewone taal.>

**Wat MIM 1.2 zegt.**
> <letterlijk citaat uit de kennisbank>
> — MIM 1.2, §<nr>

**Uitleg.** <eigen uitleg; noem het zo.>

**Let op.** <onduidelijkheid uit bekende-onduidelijkheden.md, verschil tussen UML en LD, of "Niet uit MIM 1.2: …">

Bron: MIM 1.2, §<nr> (<bestand in de kennisbank>)
```

Regels voor het antwoord:

- Het citaat is letterlijk. Inkorten mag alleen met […].
- Noem bij een voorbeeld of noot dat het niet normatief is.
- Verschillen de UML-tabel en de LD-tabel, noem beide waarden met paragraaf.
- Een metagegeven dat verplicht is maar een default heeft, hoeft in een model niet te worden ingevuld zolang de default geldt (§2.4.5.2). Zeg dat erbij.
- Gebruik de MIM-termen zoals ze in de kennisbank staan (bijvoorbeeld "attribuutsoort", niet "attribuut" of "property").

## Voorbeeld van een goed antwoord

Vraag: "Moet ik een geboortedatum optioneel maken als die soms onbekend is?"

```markdown
**Antwoord.** Nee. De geboortedatum blijft verplicht (kardinaliteit 1). Je zet het
metagegeven Mogelijk geen waarde op Ja.

**Wat MIM 1.2 zegt.**
> Verder, wanneer er sprake is van mogelijk geen waarde dan het is expliciet niet de
> bedoeling om een verplicht veld optioneel maken.
> — MIM 1.2, §5.11

**Uitleg.** Verplicht of optioneel zegt of iets in de werkelijkheid altijd een waarde
heeft. Mogelijk geen waarde zegt of die waarde onbekend mag zijn. Dat zijn twee aparte
vragen; MIM noemt de geboortedatum als voorbeeld van "verplicht, mogelijk geen waarde: Ja".

Bron: MIM 1.2, §5.11 (onderwerpen/mogelijk-geen-waarde.md)
```

## Andere versies van MIM

Deze skill kent alleen MIM 1.2. Vraagt iemand of er een nieuwere versie is, zeg dat dan. Controleer alleen op verzoek, als je internet hebt, op <https://docs.geostandaarden.nl/mim/mim/>. Gebruik de kennisbank niet voor een andere versie zonder dat te melden.

## Over deze kennisbank

- Bron: MIM 1.2, vastgestelde versie 13 juni 2024, Geonovum. Licentie van de MIM-tekst: CC BY 4.0. De letterlijke tekst in `bron/` is automatisch omgezet uit de gepubliceerde HTML.
- Gegevens: `data/elementen.json`, `data/metagegevens.json` en `.csv`, `data/waardebereik.json`, `data/woordenlijst.json`. Elk bestand begint met een veld `about`.
- Linked Data-bestanden uit de werkbron: `assets/mim.ttl`, `assets/mim-shapes.ttl`.
- Beheer en herbouwen: `LEESMIJ.md`.
