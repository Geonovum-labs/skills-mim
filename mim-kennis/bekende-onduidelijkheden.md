---
id: bekende-onduidelijkheden
titel: Bekende onduidelijkheden in MIM 1.2
bron: ["7", "2.3.2.4", "5.2", "2.4.3.16", "2.4.5.1", "2.4.3.23", "3.1.2", "4.2.2", "1.9.3", "4.1"]
mim-versie: "1.2"
status: toelichtend
---

# Bekende onduidelijkheden in MIM 1.2

**In het kort.** Op deze plekken zegt de tekst van MIM 1.2 twee verschillende dingen, of noemt hij één ding op twee manieren. Een agent lost dat nooit zelf op. Noem beide vindplaatsen, zeg welke lezing je gebruikt en dat die voorlopig is.

Laatst geverifieerd: 23 november 2026, tegen `DEF-mim-20240613.html` (vastgestelde versie) en de werkbron MIM-Werkomgeving (master, commit 3990766).

**Status van de lezingen: voorlopig.** Ze zijn een voorstel van de kennisbank en nog niet bevestigd door een MIM-modelleur of MIM-beheer (stap 6 en 9 van het project). Terugmelden aan MIM-beheer valt voorlopig buiten het project.

## Zo gebruik je dit bestand

1. Raakt een vraag een onderwerp hieronder, noem dan dat MIM 1.2 hier niet eenduidig is.
2. Citeer of noem beide vindplaatsen.
3. Geef de voorlopige lezing en zeg dat het een lezing van de kennisbank is, niet van de standaard.
4. Kom je een nieuwe tegenstrijdigheid tegen, meld die op dezelfde manier. Verzin geen oplossing.

## Overzicht

| # | Onderwerp | Vindplaatsen | Soort |
|---|---|---|---|
| I1 | Mag een gegevensgroeptype relatiesoorten bevatten? | §2.3.2.4 ↔ §5.2 | inhoud |
| I2 | Waardebereik van Authentiek | §2.4.3.16 ↔ §2.4.5.1, §5.10 | inhoud |
| I3 | Bij welk element hoort Aggregatietype? | §2.4.3.23 | inhoud |
| I4 | "Gestructuurd" of "Gestructureerd" datatype | §3.1.2, §4.2.2 ↔ §3.2.4.2, §4.3.4.2, §6.4.4.1 | schrijfwijze |
| I5 | `rdfs:seeAlso` of `mim:equivalent` | §1.9.3 ↔ §4.1, §6.4.1, §6.4.5 | inhoud (LD) |
| I6 | Kardinaliteit relatie bron: verplicht of optioneel? | §3.2.2.1 ↔ §4.3.2.1, §2.4.3.15, §2.4.5.2 | inhoud |
| I7 | Fouten in eigenschapsnamen in de LD-tabellen | §4.3, §4.3.1.2, §4.3.2.5, §4.3.2.6, §4.3.5.1 | LD |
| I8 | Historie-metagegevens bij relatieklasse en externe koppeling | §3.2.2.7, §3.2.2.8 ↔ §2.4.3.10, §4.3.2.7 | tabellen |
| I9 | Generalisatie bij een gegevensgroeptype | §2.3.3.1 ↔ §3.2.1.4 | inhoud |
| I10 | Waar staat de keuze relatiesoort of relatierol leidend? | §3.2.2 ↔ §2.4.1.3 | inhoud |
| I11 | "Keuze-element" vervallen maar nog gebruikt | §3.2.4.4 ↔ §5.3 | terminologie |
| I12 | Vertaaltabel gebruikt MIM 1.1-namen | §6.3 | terminologie |
| I13 | Alias bij een enumeratiewaarde | §2.4.3.2 | inhoud |
| I14 | Basis-URI verplicht of optioneel? | §2.4.2.1 ↔ §3.2.5.3, §4.3.5.1 | tabellen |
| I15 | Hoofdletter of kleine letter voor relatienamen | §5.15.4 | inhoud |
| I16 | Specificatie in tekst bij een constraint | §2.3.7.1 ↔ §3.2.6.1, §4.3.6.3 | tabellen |
| I17 | Naam en definitie bij relatierol leidend | §3.2.2 ↔ §3.2.2.2, §4.3.2.2 | tabellen |
| I18 | Wat is normatief? Regels in noten en voorbeelden in lopende tekst | §7 | normativiteit |
| I19 | Overige verschillen tussen de UML- en LD-tabellen | §3.2 ↔ §4.3 | tabellen |
| R | Kleine redactionele fouten | diverse | redactioneel |

---

## I1. Mag een gegevensgroeptype relatiesoorten bevatten?

> Een gegevensgroeptype kan, naast attribuutsoorten en relatiesoorten, ook zelf weer gegevensgroeptypen bevatten.
>
> — MIM 1.2, §2.3.2.4 (normatief)

> Richtlijn: een gegevensgroeptype bevat alleen «Attribuutsoort»en en geen «Relatiesoort»en. Als er wel een relatie aan de orde is, dan wordt de gegevensgroep gezien als een apart te beheren object. Er wordt dan een apart «Objecttype» gemaakt.
>
> — MIM 1.2, §5.2 (normatief)

Ook: de definitie van Gegevensgroeptype noemt alleen attribuutsoorten (§2.3.2.4). De bindingen heeft relatiesoort en heeft externe koppeling noemen het gegevensgroeptype wel (§2.4.4.6, §2.4.4.7), net als de UML-tabel (§3.2.1.4).

**Voorlopige lezing.** Het metamodel staat een relatiesoort vanuit een gegevensgroeptype toe; §5.2 is een richtlijn die het afraadt. Bij uitleg: noem beide. Bij een modelleervraag: volg de richtlijn uit §5.2 en meld de tegenstrijdigheid. Een bestaand model met zo'n relatie is daarom niet zonder meer fout.

## I2. Waardebereik van Authentiek

> Bijvoorbeeld:`"Authentiek"`,`"Basisgegeven"`,`"Landelijk kerngegeven"`,`"Gemeentelijk kerngegeven"`,`"Overig"`.
>
> — MIM 1.2, §2.4.3.16 (normatief)

De waardebereiktabel (§2.4.5.1), de tabel in §5.10 en de LD-tabel (§4.3.1.2) noemen `Wettelijk gegeven` (LD: `mim:WettelijkGegeven`) en niet `Gemeentelijk kerngegeven`. De vertaaltabel §6.3 (MIM 1.1-namen) noemt wel `Gemeentelijk kerngegeven`.

**Voorlopige lezing.** Het waardebereik is `Authentiek`, `Basisgegeven`, `Wettelijk gegeven`, `Landelijk kerngegeven`, `Overig` (§2.4.5.1). §2.4.3.16 geeft voorbeelden ("Bijvoorbeeld") en is waarschijnlijk niet bijgewerkt. Komt een model `Gemeentelijk kerngegeven` tegen, noem dan dat die waarde buiten de tabel van §2.4.5.1 valt.

## I3. Bij welk element hoort Aggregatietype?

> Een object kan samengesteld zijn uit samenstellende delen die ook individueel in het informatiemodel als objecttypen herkenbaar zijn. Dit wordt een aggregatie genoemd. Dit wordt gemodelleerd met een `Attribuutsoort` waarbij dit metagegeven is ingevuld met een type aggregatie.
>
> — MIM 1.2, §2.4.3.23 (normatief)

> *Toepassing*: Relatiesoort en Externe koppeling.
>
> — MIM 1.2, §2.4.3.23 (normatief)

De UML- en LD-tabellen zetten Aggregatietype bij relatiesoort, relatieklasse en externe koppeling, niet bij de attribuutsoort (§3.2.2.1, §4.3.2.1).

**Voorlopige lezing.** Aggregatietype is een metagegeven van een relatie. "Attribuutsoort" in de toelichting is waarschijnlijk een vergissing.

## I4. "Gestructuurd" of "Gestructureerd" datatype

De tabellen schrijven het stereotype als «Gestructuurd datatype» (§3.1.2) en de LD-klasse en -shape als `mim:GestructuurdDatatype` / `shape:GestructuurdDatatype` (§4.2.2). De tekst, de koppen (§3.2.4.2, §4.3.4.2), de transformatie (§6.4.4.1) en de vocabulaire in de werkbron (`assets/mim.ttl`) schrijven "Gestructureerd" / `mim:GestructureerdDatatype`.

**Voorlopige lezing.** Het is hetzelfde modelelement. In Linked Data geldt de naam uit de vocabulaire, `mim:GestructureerdDatatype`. Accepteer beide schrijfwijzen bij het herkennen van een element.

## I5. `rdfs:seeAlso` of `mim:equivalent`

In §1.9.3 verwijst de klasse na transformatie met `rdfs:seeAlso` naar het MIM-element; in §4.1 en §6.4.1 met `mim:equivalent`.

> Om de relatie tussen het originele MIM-model het het getransformeerde model op basis van RDFS te behouden, wordt de eigenschap `mim:equivalent` gebruikt.
>
> — MIM 1.2, §6.4.5 (normatief)

**Voorlopige lezing.** Gebruik `mim:equivalent`; dat staat in de transformatieregels en de vocabulaire. Het voorbeeld in §1.9.3 is illustratief. `mim:equivalent` is geen OWL-equivalentie: de transformatie wil de semantiek van de Linked Data-vocabulaires en die van MIM juist niet vermengen (§6.4.3).

## I6. Kardinaliteit relatie bron: verplicht of optioneel?

De UML-tabellen geven Kardinaliteit relatie bron kardinaliteit `1` (§3.2.2.1, §3.2.2.7, §3.2.2.8). De LD-tabel geeft `0..1` (§4.3.2.1).

> Wanneer de kardinaliteit aan de bronkant van de relatie niet is gespecificeerd dan is er geen sprake van een defaultwaarde.
>
> — MIM 1.2, §2.4.3.15 (normatief)

> De kardinaliteit van een relatie staat niet in de tabel, omdat hiervoor defaultwaarden bestaan. De kardinaliteit aan de doelkant moet altijd worden aangegeven. De kardinaliteit aan de bron/eigenaar kant van een relatie is optioneel om in te vullen.
>
> — MIM 1.2, §2.4.5.2 (niet-normatief, noot)

De noot zegt eerst dat er defaultwaarden "bestaan" en daarna dat de bronkant geen default kent.

**Voorlopige lezing.** De bronkant is optioneel en heeft geen default (§2.4.3.15). In de praktijk wordt een lege bronkant geïmplementeerd als `0..*` (noot bij §2.4.5.2).

## I7. Fouten in eigenschapsnamen in de LD-tabellen

| Vindplaats | In de tabel | In de vocabulaire en transformatie |
|---|---|---|
| §4.3.1.2, Indicatie classificerend | `mim:indicatieAfleidbaar` | `mim:indicatieClassificerend` (§6.4.4.2) |
| §4.3.2.5 en §4.3.2.6, Subtype en Supertype | `mim:definitie` | `mim:subtype`, `mim:supertype` (§4.3 overzicht, §6.4.4.2) |
| §4.3 overzicht, MIM-versie/-extensie/-taal | `mim:versie`, `mim:extensie`, `mim:taal` | `mim:mimversie`, `mim:mimextensie`, `mim:mimtaal` (§4.3.5.1, vocabulaire) |
| §4.2.3.1, keuzeconstraint | `mim:Keuzeconstraint` | `mim:KeuzeConstraint` (vocabulaire); §6.4.4.1 schrijft `mim:Keuzeconstraint` |

**Voorlopige lezing.** Gebruik de namen uit de vocabulaire (`assets/mim.ttl`). Noem de afwijking als iemand de tabel citeert.

## I8. Historie-metagegevens bij relatieklasse en externe koppeling

De UML-tabellen van relatieklasse (§3.2.2.7) en externe koppeling (§3.2.2.8) noemen alleen Indicatie materiële historie en Indicatie formele historie. De LD-tabellen (§4.3.2.7, §4.3.2.8) noemen ook heeft tijdlijn geldigheid en heeft tijdlijn registratie. Volgens de toepassing in §2.4.3.10 en §2.4.3.12 gelden de nieuwe metagegevens voor "Attribuutsoort en relaties (Relatiesoort, Relatieklasse, Externe Koppeling)".

**Voorlopige lezing.** Beide paren gelden (ze zijn gelijkwaardig, noten bij §2.4.3.11 en §2.4.3.13). De UML-tabellen zijn waarschijnlijk niet bijgewerkt.

## I9. Generalisatie bij een gegevensgroeptype

> Dit verband is alleen gedefinieerd voor objecttypen en datatypen.
>
> — MIM 1.2, §2.3.3.1 (normatief)

De UML-tabel van het gegevensgroeptype (§3.2.1.4) noemt "verwijst naar supertype" (`0..*`); de LD-tabel niet. Ook "verwijst naar supertype" (§2.4.4.4) noemt als toepassing "Objecttype en Datatype".

**Voorlopige lezing.** Volg de definitie: generalisatie alleen tussen objecttypen en tussen datatypen.

## I10. Waar staat de keuze relatiesoort of relatierol leidend?

> Deze keuze wordt aangegeven in de eigen extensie, zoals beschreven in 1.11 Alternatieven.
>
> — MIM 1.2, §3.2.2 (normatief)

§2.4.1.3 legt dezelfde keuze vast als verplicht metagegeven Relatiemodelleringstype van het informatiemodel; §1.11 zegt alleen dat de gekozen variant wordt "aangegeven".

**Voorlopige lezing.** Het metagegeven Relatiemodelleringstype is de plek in het model. Een extensie mag de keuze daarnaast beschrijven.

## I11. "Keuze-element" vervallen maar nog gebruikt

> _Opmerking: de modelelementen waaruit gekozen kan worden heten sinds MIM 1.1 geen keuze-elementen meer. Keuze-element is komen te vervallen._
>
> — MIM 1.2, §3.2.4.4 (normatief)

§5.3 spreekt nog over "keuze element" en zegt dat de definitie ervan optioneel is.

**Voorlopige lezing.** In §5.3 betekent "keuze element" de optie in een keuze tussen datatypen (use case 1). Gebruik in antwoorden de huidige termen.

## I12. Vertaaltabel gebruikt MIM 1.1-namen

De tabel in §6.3 heeft de kolom "MIM 1.1" en noemt onder meer Complex datatype, Keuze element, Indicatie authentiek, Gemeentelijk kerngegeven, Beheerder, Eigenaar, Data locatie en Regels. Elementen en metagegevens die later zijn toegevoegd (zoals heeft tijdlijn geldigheid, Eenheid, Mixin) staan er niet in.

**Voorlopige lezing.** De Engelse namen in `woordenlijst.md` zijn indicatief. Voor wat niet in §6.3 staat, geeft de kennisbank geen Engelse naam.

## I13. Alias bij een enumeratiewaarde

§2.4.3.2 zegt eerst dat de Alias "ook gebruikt" wordt voor een alternatieve weergave van een enumeratiewaarde (een code), en noemt in de toepassing daarna enumeratiewaarde "_expliciet niet_". De opmerking erna zegt dat in UML de Alias van een EnumerationLiteral alleen wordt gebruikt voor het metagegeven Code. De UML-tabel (§3.2.3.3) noemt geen Alias.

**Voorlopige lezing.** Alias is geen metagegeven van een enumeratiewaarde. Een code legt je vast in Code; in UML mag daarvoor het alias-veld van de EnumerationLiteral worden gebruikt.

## I14. Basis-URI verplicht of optioneel?

§2.4.2.1 noemt als toepassing "informatiemodel (verplicht), domein, view, extern". De tabellen geven `0..1` (§3.2.5.3, §4.3.5.1). Zonder Basis-URI geldt een default op basis van `urn:modelelement:` (§2.4.2.1).

**Voorlopige lezing.** Er is altijd een Basis-URI: opgegeven of de default. Of het veld ingevuld *moet* worden, is niet eenduidig.

## I15. Hoofdletter of kleine letter voor relatienamen

§5.15.4 geeft als voorbeeld lowerCamelCase voor relatiesoorten en relatierollen. Een paar zinnen later:

> Bij namen van objecttypen, gegevensattributen, keuze, datatypen, en relaties wordt ook de beginletter een hoofdletter.
>
> — MIM 1.2, §5.15.4 (normatief)

**Voorlopige lezing.** MIM legt de precieze conventie niet vast; de organisatie kiest en documenteert die (§5.15.5, §6.2). Noem beide zinnen.

## I16. Specificatie in tekst bij een constraint

§2.3.7.1 zegt dat een constraint "altijd in _gewone tekst_" wordt omschreven; de tabellen geven Specificatie tekst kardinaliteit `0..1` (§3.2.6.1, §4.3.6.3).

**Voorlopige lezing.** Inhoudelijk is de tekst altijd nodig (§2.3.7.1, §5.7). In EA kan de tekst als commentaar in de OCL-specificatie staan (§5.7), wat de `0..1` kan verklaren.

## I17. Naam en definitie bij relatierol leidend

§3.2.2 noemt bij relatierol leidend "optioneel de benoeming van de naam van de relatie". De UML-tabel (§3.2.2.2) geeft Naam en Definitie van de relatiesoort kardinaliteit `1`; de LD-tabel (§4.3.2.2) `0..1`.

**Voorlopige lezing.** Volg §3.2.2 en de LD-tabel: bij relatierol leidend zijn naam en definitie van de relatiesoort optioneel. Noem het verschil met de UML-tabel.

## I18. Wat is normatief?

> Naast onderdelen die als niet normatief gemarkeerd zijn, zijn ook alle diagrammen, voorbeelden, en noten in dit document niet normatief. Verder is alles in dit document normatief.
>
> — MIM 1.2, §7 (normatief)

Twee onduidelijkheden:

1. Voorbeelden staan vaak ook in de lopende toelichting, niet in een voorbeeldkader. Is zo'n voorbeeld normatief?
2. Sommige regels staan in een noot, bijvoorbeeld "Metagegevens met een defaultwaarde mogen niet optioneel zijn" en de regel over de kardinaliteit aan doel- en bronkant (noten bij §2.4.5.2).

**Keuze van de kennisbank.** Een citaat krijgt `(niet-normatief, voorbeeld)` of `(niet-normatief, noot)` alleen als de tekst in MIM in een voorbeeld- of notitiekader staat. Al het andere krijgt `(normatief)`. Bij een regel uit een noot zeggen we dat het een noot is.

## I19. Overige verschillen tussen de UML- en LD-tabellen

Van de 408 combinaties van element en metagegeven in de tabellen van §3.2 (UML) en §4.3 (LD) verschillen er 99: een andere kardinaliteit, of het metagegeven staat maar in één van de twee tabellen. Ze staan per stuk in `data/metagegevens.json` (veld `verschil`) en in de tabellen in `modelelementen/`. Een deel is geen tegenstrijdigheid maar een verschil in uitdrukking: LD legt sommige bindingen andersom vast (§4.2). Opvallend zijn onder meer:

- Herkomst bij gegevensgroep: UML `0..1`, LD `1`;
- Definitie en Herkomst bij primitief en gestructureerd datatype: UML `0..1`, LD `1`;
- Definitie bij gegevensgroeptype: UML `1`, LD `0..1`;
- Codelijst: Doelformaat, Waarde-item en Profielspecificatie alleen in de UML-tabel (§3.2.3.1); ook niet in de vocabulaire;
- Referentielijst: §2.4.3.25 noemt Doelformaat ook voor de referentielijst, maar geen van beide tabellen (§3.2.3.4, §4.3.3.1) neemt het op;
- Begripsterm alleen in de LD-tabellen; Unieke aanduiding alleen in de UML-tabel van objecttype.

**Voorlopige lezing.** Geen. Noem bij een vraag beide kardinaliteiten met paragraaf.

## R. Kleine redactionele fouten

Deze veranderen de betekenis niet, maar kunnen een lezer of model op het verkeerde been zetten.

| Vindplaats | Wat er staat | Waarschijnlijk bedoeld |
|---|---|---|
| §5.8.3, opmerking | "heeft tijdlijn geldigheid en heeft tijdlijn geldigheid" | geldigheid en registratie |
| §2.4.3.39, toelichting | "Bijvoorbeeld de minimale waarde voor een geldigheidsdatum" (bij Maximumwaarde inclusief) | maximale waarde |
| §2.4.3.4, voorbeeld | herkomst "BRP" "(de basisregistratie Kadaster)" | basisregistratie Personen |
| §2.4.3.8 en §2.4.5.1 | voorbeeld datum opname "1-1-2012"; patroon `jjjjmmdd` | het patroon geldt |
| §4.2.3.5 | "Zie hiervoor sectie 2.6" | §2.3.6 (Packages) |
| §5.16 | metagegeven "begrip" "uit paragraaf Datatypen" | §2.4.3.3 |
| §5.1.1, CharacterString | "metagegeven Waardenverzameling attribuutsoort" | bestaat niet in MIM 1.2; waarschijnlijk Patroon of Formeel patroon |
| §2.4.4.2 | definitie noemt objecttype en gegevensgroeptype; toelichting noemt objecttypen en relatieklassen | alle drie (zie de tabellen) |
| §5.5 | `indAbstract = J` | waardebereik is `Ja`/`Nee` (§2.4.5.1) |
| §5.13 | aggregatietype "Composite" | waarde heet `Compositie` (§2.4.5.1) |

## Zie ook

- `metagegevens.md` (paragraaf "Zo lees je de tabellen")
- Vergelijkbare lijst in de collega-skill Geonovum-labs/skills-mim (bestand known-ambiguities.md), die I1–I5 uit dit project overnam.
