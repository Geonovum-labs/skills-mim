---
id: buiten-mim
titel: Waar deze skill verder gaat dan MIM
bron: ["1.6"]
mim-versie: "1.2"
status: toelichtend
---

# Waar deze skill verder gaat dan MIM

**In het kort.** De route voor datavragen doet werk dat MIM niet regelt: data koppelen aan modelelementen. Dit bestand zegt waar de skill strenger, smaller of buiten de standaard is. De standaard en het gepubliceerde informatiemodel gaan altijd voor.

Herkomst: skills-mim (`mim-interpret/references/conflicts.md`), vertaald en ingekort.

## Buiten de reikwijdte van MIM

MIM richt zich op beschouwingsniveau 2 en 3 (§1.6). Data en technische formaten (niveau 4) vallen erbuiten. Veldkoppelingen, de projectie van een product (momentopname of volledig extract) en de keuze voor een vastgestelde veldkoppeling zijn werk van deze skill. Label zulke beweringen als koppeling, niet als *volgens het model*.

## Bewuste keuzes (uitgangspunten, geen besluiten)

- **Lezen, niet maken.** De skill schrijft, wijzigt of toetst geen modellen en genereert geen code of schema's. Conformiteit toetsen is het werk van Imvertor en de MIM-toolbox.
- **Elk MIM-model, geen ingebouwd model.** Regels en scripts zijn algemeen. Kennis over een specifiek model (modelcatalogus, veldkoppeling, elementsamenvattingen, evaluatievragen) staat in gegevensbestanden die je meegeeft. BAG is alleen een uitgewerkt voorbeeld.
- **RDF heeft de voorkeur, maar is niet de enige bron.** Niet elk model is als RDF gepubliceerd; HTML- en PDF-catalogi en SKOS zijn gelijkwaardig.
- **Deterministisch opzoeken.** De veldkoppeling, elementsamenvattingen en scripts geven ook kleine modellen exacte, herhaalbare antwoorden. De scripts zijn optioneel; dezelfde JSON-bestanden zijn ook direct leesbaar.
- **Het model van dit product boven een lookalike.** Gelijknamige elementen uit verschillende modellen door elkaar halen is een benoemde fout. Ze in verband brengen mag wel (LR15).

## Aangepaste regels ten opzichte van een eerder concept (van de collega)

| Eerdere bewering | Nu |
|---|---|
| `0..1` betekent: bekend dat het niet bestaat | Alleen als Mogelijk geen waarde Nee is (LR1) |
| Historie-indicaties betekenen dat de dataset historie bijhoudt | De indicatie zegt dat de eigenschap kan veranderen; of het product voorkomens levert, staat in de productdocumentatie (LR9) |
| Authentiek is ja/nee | Waardebereik; Basisgegeven is niet Authentiek (LR11) |
| Logische XMI heeft de voorkeur | Het model van dit product, conceptueel of logisch, in de vorm waarin het gepubliceerd is (LR13) |

## Licenties

- Eigen tekst en scripts: EUPL-1.2 (voorstel, in lijn met de Geonovum-skillrepo's).
- MIM-tekst: CC BY 4.0, met bronvermelding.
- Modelcatalogi kunnen afgeleid werk verbieden (bijvoorbeeld IMBAG, CC BY-ND 3.0 NL). Elementsamenvattingen parafraseren dan de definities en verwijzen naar de bron; namen van enumeratiewaarden worden letterlijk overgenomen omdat het de uitgewisselde waarden zijn.
- Kopieer geen code of XSD's van Imvertor (GPL-3.0) in deze skill.

## Wat de skill nog fout zal doen

- Alleen voor BAG zijn er een vastgestelde veldkoppeling en elementsamenvattingen. Andere modellen hebben eerst eigen gegevensbestanden nodig.
- Geen lezer voor XMI of MIM-XML.
- `rdf-labels` is een snelle scan met de standaardbibliotheek, geen volledige RDF-lezer en geen SHACL; het maakt geen elementsamenvattingen.
- Indicatie in onderzoek (een uitbreiding die sommige registraties gebruiken, geen MIM 1.2-metagegeven) wordt alleen genoemd.
- Gaten in het voorbeeld: `voorbeelden/bag/LEESMIJ.md`.

## Privacy

De skill is niet bedoeld om persoonsgegevens op te vragen of te verwerken. Koppel adressen of objecten niet aan personen.
