---
id: leesregels
titel: Leesregels voor een MIM-model
bron: ["5.11", "2.4.3.19", "2.4.3.14", "2.4.3.15", "2.4.1.3", "2.4.3.33", "2.3.4", "5.1.1", "2.4.3.29", "5.1.3", "5.2.2", "2.3.7.2", "5.8.2", "2.4.3.17", "2.4.3.9", "2.4.3.16", "2.4.5.1", "2.4.3.6", "2.4.3.3", "1.9", "2.4.3.34"]
mim-versie: "1.2"
status: toelichtend
---

# Leesregels voor een MIM-model

**In het kort.** Deze regels zeggen hoe je een bestaand informatiemodel volgens MIM leest als je er een vraag over data mee wilt beantwoorden. Ze zijn een eigen samenvatting; de MIM-tekst staat in de citaten en in de genoemde kennisbankbestanden. Het **gebonden model** (het model van de dataset waar de vraag over gaat) gaat altijd boven de voorbeelden in de MIM-tekst.

Herkomst: de leesregels van skills-mim (`mim-core/references/reading-rules.md`, regels 2 tot en met 14, P, H, I, L), vertaald, tegen MIM 1.2 gecontroleerd en aangevuld met citaten. Waar een regel verder gaat dan MIM, staat "Niet uit MIM 1.2:".

| Nr | Regel | Meer in |
|---|---|---|
| LR1 | Leeg is niet hetzelfde als "bestaat niet" | `onderwerpen/mogelijk-geen-waarde.md` |
| LR2 | Kardinaliteit, ook binnen een gegevensgroep | `metagegevens.md` |
| LR3 | Relaties hebben een richting | `onderwerpen/relatiemodellering.md` |
| LR4 | Overerving en abstracte objecttypen | `onderwerpen/abstracte-objecttypen.md` |
| LR5 | Welke soort waardelijst | `onderscheidingen/enumeratie-vs-referentielijst-vs-codelijst.md` |
| LR6 | Datatypen | `onderwerpen/datatypen.md` |
| LR7 | Gestructureerd datatype of gegevensgroep | `onderscheidingen/gegevensgroep-vs-gestructureerd-datatype.md` |
| LR8 | Een keuze is er precies één | `onderwerpen/keuze.md` |
| LR9 | Historie-indicaties zijn conceptueel | `onderwerpen/historie.md` |
| LR10 | Afleidbare gegevens | `metagegevens.md` |
| LR11 | Identificerend en Authentiek | `metagegevens.md` |
| LR12 | Definities hebben een herkomst | `onderwerpen/begrippen-en-definities.md` |
| LR13 | Conceptueel of logisch | `onderwerpen/beschouwingsniveaus.md` |
| LR14 | Populatie | `metagegevens.md` |
| LR15 | Homoniemen: zelfde naam, ander element | `datavragen.md` |
| LR16 | Een J/N-enumeratie is geen Boolean | `onderwerpen/datatypen.md` |
| LR17 | Levenscyclus is geen historie | `onderwerpen/historie.md` |
| LR18 | Alleen MIM 1.x | `model-vinden.md` |

## LR1. Leeg is niet hetzelfde als "bestaat niet"

Kardinaliteit en Mogelijk geen waarde zijn twee aparte assen. Lees ze samen:

| Kardinaliteit | Mogelijk geen waarde | Een lege waarde betekent | Voorbeeld in MIM |
|---|---|---|---|
| `1` | Nee | Mag niet voorkomen (fout als het ontbreekt) | identificatie |
| `1` | Ja | Onbekend; **niet** "bestaat niet" | geboortedatum; RSIN bij oude gegevens (§2.4.3.19) |
| `0..1` | Nee | Bekend dat het hier niet bestaat | officiële straatnaam |
| `0..1` | Ja | Onbekend **of** afwezig: je kunt niets concluderen | overlijdensdatum |

> Het ontbreken van een optionele waarde heeft daarom de betekenis dat het bekend is dat er in de betreffende situatie in de werkelijkheid geen waarde bestaat.
>
> — MIM 1.2, §5.11 (normatief)

Die zin geldt dus alleen als Mogelijk geen waarde Nee is. Een enumeratiewaarde "onbekend" hoort niet in een eigen model, behalve bij gegevens die één op één uit een registratie zijn overgenomen die "onbekend" wél gebruikt (§5.11).

## LR2. Kardinaliteit, ook binnen een gegevensgroep

`1` betekent altijd aanwezig, `*` onbegrensd; andere bereiken (`2..*`, `0..2`) betekenen wat er staat.

> Voor de uiteindelijke kardinaliteit van hoe vaak een gegeven voorkomt bij het object moet rekening gehouden worden met de kardinaliteit van de gegevensgroep en met de kardinaliteit van de `«Attribuutsoort»`.
>
> — MIM 1.2, §2.4.3.14 (normatief)

Eigen lezing: vermenigvuldig de twee (een attribuutsoort `0..1` in een gegevensgroep `1..*` kan dus nul of meer keer voorkomen). MIM schrijft het woord "vermenigvuldigen" niet voor.

> De kardinaliteit van de bron en van het doel is hier altijd en per definitie `1..1`.
>
> — MIM 1.2, §2.4.3.14 (normatief)

Dat gaat over een generalisatie: die krijgt geen kardinaliteit.

## LR3. Relaties hebben een richting

Een relatiesoort loopt van bron naar doel. De bron "heeft" het gegeven. Kardinaliteit zegt hoeveel doelen er per bron zijn; Kardinaliteit relatie bron (§2.4.3.15) zegt hoeveel bronnen er per doel zijn. Kijk naar het Relatiemodelleringstype (§2.4.1.3) om te weten of de naam op de relatiesoort of op de relatierol staat.

Een telling van de omgekeerde kant (hoeveel bronnen naar één doel wijzen) is geen attribuutsoort van het doel, ook niet als een product die telling als veld toont.

## LR4. Overerving en abstracte objecttypen

Vraagt iemand wat een objecttype "heeft", neem dan de eigen attribuutsoorten en relatiesoorten samen met de geërfde. Een abstract objecttype (Indicatie abstract object, §2.4.3.33) heeft geen eigen exemplaren; kijk naar de subtypen. Bij overerving gaan de kenmerken over, niet de waarden van de metagegevens van het supertype (zie `modelelementen/generalisatie.md`).

## LR5. Welke soort waardelijst

| Soort | Bij het lezen van data |
|---|---|
| Enumeratie | Gesloten lijst in het model; een waarde toevoegen vraagt een modelwijziging. De uitgewisselde waarde is de naam van de enumeratiewaarde. Gebruik die letterlijk, met dezelfde spelling en hoofdletters. |
| Referentielijst | Lijst buiten het model, die kan veranderen; de structuur staat wel in het model. Zoek de waarde op via het metagegeven Locatie (§2.4.3.24). |
| Codelijst | Lijst buiten het model; de structuur staat niet in het model. Waarde-item (§2.4.3.26) zegt welk veld van de lijst wordt gebruikt. |

## LR6. Datatypen

> Een getal dat voorloopnullen mag hebben, zoals `gemeentecode`: `"0060"`, wordt gespecificeerd als een `CharacterString`.
>
> — MIM 1.2, §2.4.3.29 (normatief)

- Lees een identificatie met voorloopnullen dus als tekst, nooit als Integer.
- Real is een benadering, Decimal is exact (§5.1.1).
- Lengte en Patroon gelden bovenop het datatype.
- Datum mogelijk onvolledig (DMO) mag `JJJJ`, `JJJJ-MM` of `JJJJ-MM-DD` zijn; lees het niet als een volledige Date (§5.1.3).
- Niet uit MIM 1.2: het type in het model gaat boven het JSON-type in een product. Een JSON-integer voor een kenmerk van type Year blijft een Year.

## LR7. Gestructureerd datatype of gegevensgroep

Een gestructureerd datatype is één samengestelde waarde; de delen zijn geen losse feiten en hebben geen eigen historie. Een gegevensgroep is een benoemde verzameling losse attribuutsoorten; die kunnen wél elk een eigen historie hebben. MIM geeft de toets in §5.2.2; zie `onderscheidingen/gegevensgroep-vs-gestructureerd-datatype.md`.

## LR8. Een keuze is er precies één

Er is altijd precies één van de mogelijkheden; twee gevuld is fout. In data komt alleen de gekozen mogelijkheid voor.

> `kenmerkOfOmschrijving` staat er wel maar is geen attribuutsoort maar een `Keuze`. De naam daarvan is arbitrair omdat het geen betekenis heeft en bij de implementatie in data niet voorkomt.
>
> — MIM 1.2, §2.3.7.2 (normatief)

Welke van de vijf use cases van toepassing is, zegt waaraan de keuze gebonden is; zie `onderwerpen/keuze.md`. Een constraint is de andere manier om "precies één" of "minstens één" uit te drukken; negeer constraints niet.

## LR9. Historie-indicaties zijn conceptueel

> Merk op: de _heeft tijdlijn geldigheid_ geeft op conceptueel niveau niet aan dat er voor het gegeven een tijdlijn geldigheid wordt bijgehouden in de administratie. Het geeft aan _dat een eigenschap_ kan veranderen en er op de tijdlijn geldigheid verschillende waarden kunnen bestaan (op verschillende momenten).
>
> — MIM 1.2, §5.8.2 (normatief)

- Indicatie materiële historie en Indicatie formele historie zijn de oudere namen; accepteer beide.
- Of een product eerdere versies (voorkomens) levert, is een feit van het product. Controleer de data (velden als `beginGeldigheid`, `tijdstipRegistratie`, `voorkomen`), niet de indicatie.
- MIM gebruikt bouwjaar als voorbeeld van een kenmerk zonder tijdlijn geldigheid (§5.8.2, niet-normatief voorbeeld). Zet het gebonden model het anders, volg dan het model.

## LR10. Afleidbare gegevens

> Het afgeleide gegeven is zelf geen brongegeven en moet aangepast worden als de brongegevens aangepast worden.
>
> — MIM 1.2, §2.4.3.17 (normatief)

Een afleidbaar gegeven is geen zelfstandig bewijs. Spreekt het de brongegevens tegen, vertrouw dan de brongegevens.

## LR11. Identificerend en Authentiek

Identificerend (§2.4.3.9) kan één kenmerk zijn of een combinatie, eventueel met een relatiesoort. Dat is de sleutel om records te koppelen of dubbelingen te vinden.

Authentiek is een waardebereik, geen ja/nee: `Authentiek`, `Basisgegeven`, `Wettelijk gegeven`, `Landelijk kerngegeven`, `Overig` (§2.4.5.1). Alleen `Authentiek` brengt de verplichting mee om het gegeven zonder nader onderzoek te gebruiken:

> Authentieke gegevens moeten door alle overheidsinstellingen verplicht en zonder nader onderzoek, worden gebruikt bij de uitvoering van publiekrechtelijke taken.
>
> — MIM 1.2, §2.4.3.16 (normatief)

Basisgegeven is dus niet hetzelfde als Authentiek. De toelichting in §2.4.3.16 noemt `Gemeentelijk kerngegeven` in plaats van `Wettelijk gegeven`; zie I2 in `bekende-onduidelijkheden.md`.

## LR12. Definities hebben een herkomst

Gebruik Herkomst definitie (§2.4.3.6) en Begrip (§2.4.3.3). De definitie van een modelelement (informatie) is iets anders dan de definitie van een begrip (domein of wet). Bij een element uit een package Extern of View geldt de betekenis uit het bronmodel. Een begrippenkader (niveau 1, vaak SKOS) helpt bij begrippen, maar vervangt de attribuutsoorten van het informatiemodel niet.

## LR13. Conceptueel of logisch

Een model is óf conceptueel óf logisch (Informatiemodeltype, §2.4.1.2). Gebruik het model dat het onderwerp echt beschrijft; sla een conceptueel model niet over omdat er geen XMI of RDF van is. In Linked Data is het verschil kleiner:

> Voor modellen die zowel een UML als een Linked Data implementatie vereisen kan beter gekozen worden voor het type "conceptueel informatiemodel".
>
> — MIM 1.2, §1.9 (normatief)

Lees een verschil in type tussen twee uitdrukkingen van hetzelfde model daarom niet als een verschil in inhoud.

## LR14. Populatie

> Het metagegeven `Populatie` in een (basis)registratie kan in het gebruik echter beperkter zijn, omdat niet alle examplaren die aan de definitie voldoen, worden geregistreerd.
>
> — MIM 1.2, §2.4.3.34 (normatief)

Lees de populatie voordat je concludeert dat iets "niet bestaat" omdat het niet in de data staat.

## LR15. Homoniemen: zelfde naam, ander element

Niet uit MIM 1.2: deze regel komt uit de praktijk van het koppelen van data aan modellen.

- Dezelfde naam in verschillende modellen is niet hetzelfde element. Koppel eerst het model van deze dataset, dan pas het element. Alleen dat model levert definitie, kardinaliteit, waardelijst en attribuutsoorten.
- Neem nooit de definitie, kardinaliteit of waardelijst van een gelijknamig element uit een ander model over, en beantwoord de vraag niet vanuit een ander model alsof het het model van deze dataset is.
- Zeg wél wanneer elementen waarschijnlijk verwant zijn, bijvoorbeeld omdat ze hetzelfde soort ding in de werkelijkheid beschrijven. Label dat *afgeleid*, tenzij een model het zegt.
- Gebruik een expliciete koppeling als de modellen die geven: een attribuutsoort die naar de identificatie in het andere model verwijst, een generalisatie naar een gedeeld supertype (bijvoorbeeld NEN 3610), een externe koppeling, of een vastgelegde relatie of gelijkwaardigheid. Label dat *volgens het model*.

Eigen voorbeeld: IMGeo `Pand` en IMBAG `Pand` zijn verschillende elementen die allebei gebouwen beschrijven. IMGeo `Pand` heeft `identificatieBAGPND`, een expliciete verwijzing naar de identificatie van het IMBAG-pand.

## LR16. Een J/N-enumeratie is geen Boolean

> Wanneer u de Ja of Nee wilt gebruiken, gebruik dan bv. een Enumeratie
>
> — MIM 1.2, §5.1.1 (normatief)

Een waarde `"N"` uit een enumeratie als Indicatie `{J, N}` is een enumeratiewaarde (Nee), geen JSON `false`. Lees de betekenis uit de definitie van de attribuutsoort, niet uit de alledaagse betekenis van "nee".

## LR17. Levenscyclus is geen historie

Niet uit MIM 1.2. Een attribuutsoort `status` legt vaak een fase in de levenscyclus vast. Voorkomens en tijdlijnen zijn historie. Haal ze niet door elkaar: een levenscycluswaarde is geen tijdlijn.

## LR18. Alleen MIM 1.x

Niet uit MIM 1.2: deze skill leest alleen modellen volgens MIM 1.x. Werkversies van MIM 2.0 gebruiken dezelfde namespace `http://modellen.mim-standaard.nl/def/mim#` met andere klassennamen (zoals `mim:Attribuuttype` en `mim:Relatietype`). Zie je die, stop dan en zeg dat het model eerst moet worden omgezet. Lees een 2.0-bestand nooit als 1.2.

## Verschil met mim-kennis bij onduidelijkheden

`bekende-onduidelijkheden.md` geeft per onduidelijkheid een lezing voor uitleg en modelleren. Bij het **lezen** van een bestaand model geldt daarnaast: lees het model zoals het gepubliceerd is, zeg dat MIM hier niet eenduidig is, en "verbeter" het model niet. Een gegevensgroeptype met een relatiesoort (I1) is bij het lezen dus geen fout in het model.
