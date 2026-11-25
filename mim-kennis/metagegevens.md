---
id: metagegevens
titel: Metagegevens
bron: ["2.4", "2.4.1", "2.4.2", "2.4.3", "2.4.4", "2.4.5", "3.2", "4.3"]
mim-versie: "1.2"
status: normatief
---

# Metagegevens

**In het kort.** Metagegevens zijn de gegevens die je óver een modelelement vastlegt, zoals de naam, de definitie of de kardinaliteit van een attribuutsoort. Ze zijn geen kenmerken van objecten. Welke metagegevens bij welk modelelement horen, en of ze verplicht zijn, staat in tabellen per modelelement.

Inhoud van dit bestand:

1. Wat metagegevens zijn
2. Zo lees je de tabellen
3. Waardebereik en defaultwaarden
4. Metagegevens die vaak verkeerd worden begrepen
5. Definitie en toepassing per metagegeven (gegenereerd)

Per modelelement staat de tabel in het bestand van dat element in de map modelelementen/ (paragraaf 4). De gegevens zelf staan in `data/metagegevens.json` en `data/metagegevens.csv`. Opzoeken: `python3 scripts/mim.py metagegeven <element> [<metagegeven>]`.

## 1. Wat metagegevens zijn

> Bij de modelelementen in een informatiemodel kunnen metagegevens, zoals 'naam' van het modelelement, of 'datum opname' van het modelelement, worden bijgehouden. Dit zijn geen eigenschappen van een object en worden daarom niet als bijvoorbeeld een attribuutsoort van een objecttype gemodelleerd maar als metagegevens van een objecttype.
>
> — MIM 1.2, §2.4 (normatief)

MIM verdeelt de metagegevens in vier groepen (§2.4.1 tot en met §2.4.4):

| Groep | Voorbeelden | Geldt voor |
|---|---|---|
| Informatiemodel | Informatiemodeltype, Relatiemodelleringstype, MIM-versie | alleen het informatiemodel |
| Identificatie | Basis-URI, Identificatie | packages; alle modelelementen |
| Modelelementen | Naam, Definitie, Kardinaliteit, Authentiek | per modelelement verschillend |
| Bindingen | heeft attribuut, heeft datatype, bevat modelelement | hoe elementen aan elkaar vastzitten |

> Merk op, de metagegevens aspecten zijn specifiek voor elk modelelement apart. Dus als er in H2.2 sprake is van een generalisatie, dan worden deze metagegevens niet overerft (en de ingevulde waardes worden uiteraard zeker niet overerft).
>
> — MIM 1.2, §2.4.3 (normatief)

Eigen uitleg. In UML staan veel metagegevens als tagged value; sommige zijn onderdeel van UML zelf (zoals de naam). In Linked Data zijn het eigenschappen (`owl:DatatypeProperty` of `owl:ObjectProperty`) in de MIM-vocabulaire (§2.4.3, §4.2).

## 2. Zo lees je de tabellen

Elke tabel in `modelelementen/` heeft deze kolommen:

| Kolom | Betekenis |
|---|---|
| Metagegeven | naam zoals in §2.4; bindingen beginnen met "heeft", "bevat" of "verwijst naar" |
| Betekenis | de paragraaf in §2.4 waar de betekenis staat; `-` als het metagegeven niet in §2.4 voorkomt |
| UML | kardinaliteit en paragraaf in de UML-tabel (§3.2) |
| LD | kardinaliteit en paragraaf in de Linked Data-tabel (§4.3) |
| Verplicht | `verplicht` als de minimumkardinaliteit 1 of meer is, `optioneel` bij 0; `afwijkend tussen UML en LD` als de twee tabellen verschillen |
| Verschil UML/LD | `ja` als de tabellen verschillen of het metagegeven maar in één tabel staat |

Regels om een antwoord te geven (eigen uitleg, gebaseerd op de genoemde paragrafen):

1. **Staat een metagegeven niet in de tabel van een element, dan hoort het niet bij dat element.** Een extensie kan metagegevens toevoegen (§1.10).
2. **Verplicht met een default.** Sommige metagegevens zijn verplicht en hebben toch een defaultwaarde, zoals Indicatie abstract object. Een model hoeft die dan niet in te vullen zolang de default geldt:

   > Er zijn metagegevens die een defaultwaarde hebben. Het is echter niet nodig om deze defaultwaarde expliciet aan te geven in het informatiemodel. De default staat hier aangegeven. Alleen wanneer er afgeweken wordt van deze default wordt dit in het informatiemodel aangegeven.
   >
   > — MIM 1.2, §2.4.5.2 (normatief)

3. **Waarom verplicht?** Een leeg optioneel metagegeven betekent "niet aan de orde", niet "onbekend" of "nog niet ingevuld" (§2.4.3).
4. **Verschil tussen UML en LD.** Niet alle verschillen zijn tegenstrijdigheden. Linked Data legt sommige bindingen andersom vast: een relatiesoort verwijst met `mim:bron` naar het objecttype, dus "heeft relatiesoort" staat niet in de LD-tabel van het objecttype (§4.2). Andere verschillen zijn wel echte verschillen in kardinaliteit. Meld een verschil altijd, kies niet zelf, en verwijs zo nodig naar `bekende-onduidelijkheden.md`.
5. **Relatiesoort en relatierol** hebben twee varianten, afhankelijk van het Relatiemodelleringstype. Kijk eerst welk alternatief het model gebruikt (`onderwerpen/relatiemodellering.md`).

## 3. Waardebereik en defaultwaarden

Gegevens: `data/waardebereik.json`. Opzoeken: `python3 scripts/mim.py waarden <metagegeven>`.

| Metagegeven | Toegestane waarden (§2.4.5.1) | Default (§2.4.5.2) |
|---|---|---|
| heeft tijdlijn geldigheid | `Ja`, `Nee` | `Nee` |
| heeft tijdlijn registratie | `Ja`, `Nee` | `Nee` |
| Indicatie materiële historie | niet in de waardebereiktabel | `Nee` |
| Indicatie formele historie | niet in de waardebereiktabel | `Nee` |
| Indicatie classificerend | `Ja`, `Nee` | `Nee` |
| Indicatie abstract object | `Ja`, `Nee` | `Nee` |
| Mogelijk geen waarde | `Ja`, `Nee` | `Nee` |
| Mixin | `Ja`, `Nee` | `Nee` |
| Identificerend | niet in de waardebereiktabel | `Nee` |
| Unidirectioneel | niet in de waardebereiktabel | `Ja` |
| Kardinaliteit («Attribuutsoort») | zie §2.4.3.14 | `1` |
| Aggregatietype | `Compositie`, `Gedeeld`, `Geen` | `Geen` |
| Authentiek | `Authentiek`, `Basisgegeven`, `Wettelijk gegeven`, `Landelijk kerngegeven`, `Overig` | geen |

> De metagegevens met `Ja` en `Nee` zijn semantisch bedoeld als een boolean (er zijn geen andere waarden mogelijk zoals onbekend, overig of geen waarde (leeg)).
>
> — MIM 1.2, §2.4.5.1 (normatief)

> Metagegevens met een defaultwaarde mogen niet optioneel zijn. Kies de defaultwaarde defensief.
>
> — MIM 1.2, §2.4.5.2 (niet-normatief, noot)

> De kardinaliteit aan de doelkant moet altijd worden aangegeven. De kardinaliteit aan de bron/eigenaar kant van een relatie is optioneel om in te vullen.
>
> — MIM 1.2, §2.4.5.2 (niet-normatief, noot)

Datums in metagegevens volgen het patroon `jjjjmmdd`; lengtes zijn getallen (§2.4.5.1). Definitie en Toelichting mogen opmaak bevatten; het metagegeven Tekstopmaak van het informatiemodel zegt welke (§2.4.1.7, §2.4.5.1).

## 4. Metagegevens die vaak verkeerd worden begrepen

Eigen uitleg, met de paragraaf waarop hij steunt.

- **Kardinaliteit** gaat over hoe vaak een kenmerk bij één object voorkomt (§2.4.3.14). Een gegeven dat er wel is maar onbekend is, maak je niet optioneel; daarvoor is Mogelijk geen waarde (`onderwerpen/mogelijk-geen-waarde.md`).
- **Kardinaliteit bij een gegevensgroeptype.** Bij een attribuutsoort in een gegevensgroeptype staat de kardinaliteit binnen de groep; voor het object tellen de kardinaliteit van de gegevensgroep en die van de attribuutsoort samen (§2.4.3.14).
- **Historie.** heeft tijdlijn geldigheid (vroeger Indicatie materiële historie) en heeft tijdlijn registratie (vroeger Indicatie formele historie) zijn per paar gelijkwaardig; de oude namen vervallen in MIM 2.x (noten bij §2.4.3.11 en §2.4.3.13). Zie `onderwerpen/historie.md`.
- **Herkomst** gaat over waar het *modelelement* vandaan komt, niet over waar de *data* vandaan komen (§2.4.3.4).
- **Authentiek.** Het waardebereik in §2.4.5.1 wijkt af van de opsomming in §2.4.3.16 (onduidelijkheid I2). Alleen `Authentiek` betekent dat overheden het gegeven verplicht en zonder nader onderzoek gebruiken (§2.4.3.16, §5.10).
- **Aggregatietype** hoort bij een relatie (Relatiesoort, Externe koppeling), niet bij een attribuutsoort (onduidelijkheid I3).
- **Identificerend** kan op attribuutsoorten en relaties staan en ook op een referentie-element (§2.4.3.9). In UML: `isId = true` bij een attribuutsoort, stereotype «id» bij een relatiesoort (noot bij §3.2).
- **Indicatie afleidbaar** gaat over afleiden *binnen* het model (§2.4.3.17, §5.9).
- **Indicatie classificerend** geeft aan dat een attribuutsoort het objecttype in subtypen indeelt, zoals "type gebouw" (§2.4.3.18).
- **Minimum- en maximumwaarde** (inclusief of exclusief) mogen alleen bij primitieve datatypen Integer, Decimal, Float, Real, DateTime en Date; per kant maar één van de twee (§2.4.3.37 tot en met §2.4.3.40).
- **Eenheid** volgt het SI-stelsel; je vult de *unit expression* in, bijvoorbeeld `m` (§2.4.3.36).
- **Type** en **heeft datatype** zijn twee namen voor dezelfde binding: het datatype van een attribuutsoort, data-element, referentie-element of keuze (§2.4.3.28, §2.4.4.5).
- **Begripsterm** en **Unieke aanduiding** staan niet in §2.4. Begripsterm komt alleen voor in de LD-tabellen en de transformatie (§6.4.9.5); Unieke aanduiding alleen in de UML-tabel van het objecttype (§3.2.1.1) en de transformatie (§6.4.9.24).

## 5. Definitie en toepassing per metagegeven

Gegenereerd uit de tekst van MIM 1.2 door `beheer/bouw/maak_metagegevens_definities.py`. Niet met de hand wijzigen.

<!-- BEGIN GEGENEREERD: definities-metagegevens -->
### Metagegevens van het informatiemodel (§2.4.1)

#### Informatiedomein

> Aanduiding van het functionele domein waartoe het informatiemodel behoort.
>
> — MIM 1.2, §2.4.1.1 (normatief)

> Toepassing: Informatiemodel (verplicht)
>
> — MIM 1.2, §2.4.1.1 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.1.1`

#### Informatiemodeltype

> De beschrijving van de aard van het informatiemodel, hoe het geïnterpreteerd moet worden.
>
> — MIM 1.2, §2.4.1.2 (normatief)

> Toepassing: Informatiemodel (verplicht)
>
> — MIM 1.2, §2.4.1.2 (normatief)

Waardebereik: waarden `Conceptueel`, `Logisch` (§2.4.1.2).

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.1.2`

#### Relatiemodelleringstype

> Aanduiding van een in MIM gedefinieerd alternatief voor een modelleringswijze, en welke keuze hierbij is gemaakt.
>
> — MIM 1.2, §2.4.1.3 (normatief)

> Toepassing: Informatiemodel (verplicht)
>
> — MIM 1.2, §2.4.1.3 (normatief)

Waardebereik: waarden `Relatiesoort leidend`, `Relatierol leidend` (§2.4.1.3).

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.1.3`

#### MIM-versie

> De versie van de MIM-specificatie die gebruikt is om het informatiemodel in uit te drukken.
>
> — MIM 1.2, §2.4.1.4 (normatief)

> Toepassing: Informatiemodel (verplicht)
>
> — MIM 1.2, §2.4.1.4 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.1.4`

#### MIM-extensie

> De aanduiding van een extensie op MIM.
>
> — MIM 1.2, §2.4.1.5 (normatief)

> Toepassing: Informatiemodel (optioneel)
>
> — MIM 1.2, §2.4.1.5 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.1.5`

#### MIM-taal

> De aanduiding van de taal die gebruikt is voor de modelelementen.
>
> — MIM 1.2, §2.4.1.6 (normatief)

> Toepassing: Informatiemodel (optioneel)
>
> — MIM 1.2, §2.4.1.6 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.1.6`

#### Tekstopmaak

> De specificatie van de opmaak van een tekstuele beschrijving in het model.
>
> — MIM 1.2, §2.4.1.7 (normatief)

> Toepassing: Informatiemodel (optioneel)
>
> — MIM 1.2, §2.4.1.7 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.1.7`

### Identificatie (§2.4.2)

#### Basis-URI

> De standaard basis-URI voor elk element in dit informatiemodel.
>
> — MIM 1.2, §2.4.2.1 (normatief)

> Toepassing: informatiemodel (verplicht), domein, view, extern
>
> — MIM 1.2, §2.4.2.1 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.2.1`

#### Identificatie

> De identificatie van een modelelement.
>
> — MIM 1.2, §2.4.2.2 (normatief)

> Toepassing: alle modelelementen
>
> — MIM 1.2, §2.4.2.2 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.2.2`

### Metagegevens van modelelementen (§2.4.3)

#### Naam

> De naam van een modelelement.
>
> — MIM 1.2, §2.4.3.1 (normatief)

> Toepassing: alle modelelementen.
>
> — MIM 1.2, §2.4.3.1 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.3.1`

#### Alias

> De weergave van de naam van een modelelement in natuurlijke taal (niet technisch).
>
> — MIM 1.2, §2.4.3.2 (normatief)

> Toepassing: Objecttype, Attribuutsoort, Gegevensgroep, Relatiesoort, Relatierol, Relatieklasse, Externe Koppeling, Keuze, Enumeratie, Primitief datatype, Gestructureerd datatype, Data-element en _expliciet niet_ voor Packages, Enumeratiewaarde, en Constraint.
>
> — MIM 1.2, §2.4.3.2 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.3.2`

#### Begrip

> Verwijzing naar een begrip, vanuit een modelelement, waarmee wordt aangegeven op welk begrip, of begrippen, het informatiemodel element is gebaseerd. De verwijzing heeft de vorm van een term of een URI.
>
> — MIM 1.2, §2.4.3.3 (normatief)

> Toepassing: alle modelelementen met een naam, met uitzondering van Package en Constraint.
>
> — MIM 1.2, §2.4.3.3 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.3.3`

#### Herkomst

> De registratie of het informatiemodel waaraan het modelelement ontleend is dan wel de eigen organisatie indien het door de eigen organisatie toegevoegd is.
>
> — MIM 1.2, §2.4.3.4 (normatief)

> Toepassing: alle modelelementen.
>
> — MIM 1.2, §2.4.3.4 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.3.4`

#### Definitie

> De beschrijving van de betekenis van dit modelelement.
>
> — MIM 1.2, §2.4.3.5 (normatief)

> Toepassing: alle modelelementen.
>
> — MIM 1.2, §2.4.3.5 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.3.5`

#### Herkomst definitie

> De registratie of het informatiemodel waaruit de definitie is overgenomen dan wel een aanduiding die aangeeft uit welke bronnen de definitie is samengesteld.
>
> — MIM 1.2, §2.4.3.6 (normatief)

> Toepassing: alle modelelementen die het metagegeven `Definitie` kennen.
>
> — MIM 1.2, §2.4.3.6 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.3.6`

#### Toelichting

> Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding.
>
> — MIM 1.2, §2.4.3.7 (normatief)

> Toepassing: alle modelelementen die het metagegeven `definitie` kennen.
>
> — MIM 1.2, §2.4.3.7 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.3.7`

#### Datum opname

> De datum waarop het modelelement is opgenomen in het informatiemodel.
>
> — MIM 1.2, §2.4.3.8 (normatief)

> Toepassing: alle modelelementen, uitgezonderd datatype elementen, packages en overig.
>
> — MIM 1.2, §2.4.3.8 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.3.8`

#### Identificerend

> Een aanduiding dat een kenmerk of een combinatie van kenmerken van een objecttype uniek identificerend is voor alle objecten in de populatie van objecten van dit objecttype, of de aanduiding dat een referentie-element uniek identificerend is voor alle lijst items in een referentielijst.
>
> — MIM 1.2, §2.4.3.9 (normatief)

> Toepassing: attribuutsoort, alle relaties (relatiesoort, relatierol, relatieklasse, externe koppeling), referentie-element.
>
> — MIM 1.2, §2.4.3.9 (normatief)

Waardebereik: default `Nee` (§2.4.5.2).

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.3.9`

#### heeft tijdlijn geldigheid

> Indicatie of voor dit kenmerk een tijdlijn geldigheid bijgehouden wordt en te bevragen is.
>
> — MIM 1.2, §2.4.3.10 (normatief)

> Toepassing: alle modelelementen die een kenmerk (kunnen) zijn van een Objecttype, waarvoor data kan worden bijgehouden: Attribuutsoort en relaties (Relatiesoort, Relatieklasse, Externe Koppeling).
>
> — MIM 1.2, §2.4.3.10 (normatief)

Waardebereik: waarden `Ja`, `Nee` (§2.4.5.1); default `Nee` (§2.4.5.2).

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.3.10`

#### Indicatie materiële historie

> Indicatie of de materiële historie van het kenmerk van het object bijgehouden wordt en te bevragen is.
>
> — MIM 1.2, §2.4.3.11 (normatief)

> Toepassing: alle modelelementen die een kenmerk (kunnen) zijn van een Objecttype, waarvoor data kan worden bijgehouden: Attribuutsoort en relaties (Relatiesoort, Relatieklasse, Externe Koppeling).
>
> — MIM 1.2, §2.4.3.11 (normatief)

Waardebereik: default `Nee` (§2.4.5.2).

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.3.11`

#### heeft tijdlijn registratie

> Indicatie of voor dit kenmerk een tijdlijn registratie bijgehouden wordt en te bevragen is.
>
> — MIM 1.2, §2.4.3.12 (normatief)

> Toepassing: alle modelelementen die een kenmerk (kunnen) zijn van een Objecttype, waarvoor data kan worden bijgehouden: Attribuutsoort en relaties (Relatiesoort, Relatieklasse, Externe Koppeling).
>
> — MIM 1.2, §2.4.3.12 (normatief)

Waardebereik: waarden `Ja`, `Nee` (§2.4.5.1); default `Nee` (§2.4.5.2).

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.3.12`

#### Indicatie formele historie

> Indicatie of de formele historie van het kenmerk van het object bijgehouden wordt en te bevragen is.
>
> — MIM 1.2, §2.4.3.13 (normatief)

> Toepassing: alle modelelementen die een kenmerk (kunnen) zijn van een Objecttype, waarvoor data kan worden bijgehouden: Attribuutsoort en relaties (Relatiesoort, Relatieklasse, Externe Koppeling).
>
> — MIM 1.2, §2.4.3.13 (normatief)

Waardebereik: default `Nee` (§2.4.5.2).

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.3.13`

#### Kardinaliteit

> De kardinaliteit geeft aan hoeveel keer waarden van dit kenmerk van een object kunnen voorkomen bij een object van het betreffende objecttype.
>
> — MIM 1.2, §2.4.3.14 (normatief)

> Toepassing: alle modelelementen die een kenmerk (kunnen) zijn van een Objecttype.
>
> — MIM 1.2, §2.4.3.14 (normatief)

Waardebereik: waarden `1..1`, `1..*`, `0..1`, `0..*` (§2.4.3.14); default `1 (alleen voor «Attribuutsoort»)` (§2.4.5.2).

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.3.14`

#### Kardinaliteit relatie bron

> De kardinaliteit relatie bron geeft bij een relatiesoort aan hoeveel instanties van het bron objecttype in een relatie met één instantie van het doel objecttype verbonden kunnen zijn.
>
> — MIM 1.2, §2.4.3.15 (normatief)

> Toepassing: relatiesoort, externe koppeling en relatieklasse
>
> — MIM 1.2, §2.4.3.15 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.3.15`

#### Authentiek

> Aanduiding of het kenmerk een authentiek gegeven betreft.
>
> — MIM 1.2, §2.4.3.16 (normatief)

> Toepassing: alle modelelementen die een kenmerk (kunnen) zijn van een Objecttype.
>
> — MIM 1.2, §2.4.3.16 (normatief)

Waardebereik: waarden `Authentiek`, `Basisgegeven`, `Wettelijk gegeven`, `Landelijk kerngegeven`, `Overig` (§2.4.5.1).

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.3.16`

#### Indicatie afleidbaar

> Aanduiding dat gegeven afleidbaar is uit andere attribuut- en/of relatiesoorten.
>
> — MIM 1.2, §2.4.3.17 (normatief)

> Toepassing: de modelelementen waarvoor een waarde ingevuld kan worden, te weten de modelelementen Attribuutsoort en Relatiesoort.
>
> — MIM 1.2, §2.4.3.17 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.3.17`

#### Indicatie classificerend

> Indicatie dat een attribuutsoort het objecttype waar het bij hoort classificeert in (sub)typen.
>
> — MIM 1.2, §2.4.3.18 (normatief)

> Toepassing: Attribuutsoort.
>
> — MIM 1.2, §2.4.3.18 (normatief)

Waardebereik: waarden `Ja`, `Nee` (§2.4.5.1); default `Nee` (§2.4.5.2).

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.3.18`

#### Mogelijk geen waarde

> Aanduiding dat van een aspect geen waarde is geregistreerd, maar dat onduidelijk is of de waarde er werkelijk ook niet is.
>
> — MIM 1.2, §2.4.3.19 (normatief)

> Toepassing: de modelelementen waarvoor een waarde ingevuld kan worden, te weten de modelelementen Attribuutsoort en Relatiesoort.
>
> — MIM 1.2, §2.4.3.19 (normatief)

Waardebereik: waarden `Ja`, `Nee` (§2.4.5.1); default `Nee` (§2.4.5.2).

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.3.19`

#### Bron

> Aanduiding van het bronobject in een relatie tussen objecten. Een bronobject heeft middels een relatiesoort een relatie met een doelobject.
>
> — MIM 1.2, §2.4.3.20 (normatief)

> Toepassing: Relatiesoort en Externe koppeling.
>
> — MIM 1.2, §2.4.3.20 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.3.20`

#### Doel

> Aanduiding van het gerelateerde objecttype die het eindpunt van de relatie aangeeft. Naar objecten van dit objecttype wordt verwezen.
>
> — MIM 1.2, §2.4.3.21 (normatief)

> Toepassing: Relatiesoort en Externe koppeling.
>
> — MIM 1.2, §2.4.3.21 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.3.21`

#### Unidirectioneel

> De richting van een relatie, welke betekenis geeft aan de relatie vanuit het perspectief van de eigenaar van de relatie.
>
> — MIM 1.2, §2.4.3.22 (normatief)

> Toepassing: Relatiesoort en Externe koppeling.
>
> — MIM 1.2, §2.4.3.22 (normatief)

Waardebereik: default `Ja` (§2.4.5.2).

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.3.22`

#### Aggregatietype

> Aanduiding of het objecttype die de eigenaar is van een relatie het doel van relatie ziet als een samenstellend deel dat bij het objecttype hoort en wat de type van die samenstellingsrelatie is.
>
> — MIM 1.2, §2.4.3.23 (normatief)

> Toepassing: Relatiesoort en Externe koppeling.
>
> — MIM 1.2, §2.4.3.23 (normatief)

Waardebereik: waarden `Compositie`, `Gedeeld`, `Geen` (§2.4.5.1); default `Geen` (§2.4.5.2).

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.3.23`

#### Locatie

> Als het type van het attribuutsoort een waardelijst is, dan wordt hier de plek waar deze te vinden is opgegeven.
>
> — MIM 1.2, §2.4.3.24 (normatief)

> Toepassing: Codelijst en Referentielijst.
>
> — MIM 1.2, §2.4.3.24 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.3.24`

#### Doelformaat

> Het formaat waarin een waardelijst is gepubliceerd.
>
> — MIM 1.2, §2.4.3.25 (normatief)

> Toepassing: Codelijst en Referentielijst.
>
> — MIM 1.2, §2.4.3.25 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.3.25`

#### Waarde-item

> Het item (of element) van de lijst dat de waarde representeert.
>
> — MIM 1.2, §2.4.3.26 (normatief)

> Toepassing: Codelijst
>
> — MIM 1.2, §2.4.3.26 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.3.26`

#### Profielspecificatie

> Referentie naar het profiel dat de technische implementatie van de codelijst beschrijft.
>
> — MIM 1.2, §2.4.3.27 (normatief)

> Toepassing: Codelijst
>
> — MIM 1.2, §2.4.3.27 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.3.27`

#### Type

> Het datatype waarmee waarden van dit modelelement worden vastgelegd.
>
> — MIM 1.2, §2.4.3.28 (normatief)

> Toepassing: Alle informatie elementen die een attribuut modelleren: Attribuutsoort, Data-element, Referentie-element, Datatypekeuze, Doelkeuze.
>
> — MIM 1.2, §2.4.3.28 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.3.28`

#### Lengte

> De aanduiding van de lengte van een gegeven, volgens de aangegeven notatiewijze.
>
> — MIM 1.2, §2.4.3.29 (normatief)

> Toepassing: Attribuutsoort, Primitief datatype (alleen als dit datatype in het IM zelf-gedefinieerd is), Data-element, Referentie-element.
>
> — MIM 1.2, §2.4.3.29 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.3.29`

#### Patroon

> De verzameling van waarden die gegevens van deze attribuutsoort kunnen hebben, oftewel het waardenbereik, uitgedrukt in een specifieke structuur.
>
> — MIM 1.2, §2.4.3.30 (normatief)

> Toepassing: De modelelementen uit de groep Datatype en Attribuutsoort.
>
> — MIM 1.2, §2.4.3.30 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.3.30`

#### Formeel patroon

> Zoals patroon, formeel vastgelegd, uitgedrukt in een formele taal die door de computer wordt herkend.
>
> — MIM 1.2, §2.4.3.31 (normatief)

> Toepassing: De modelelementen uit de groep Datatype en Attribuutsoort.
>
> — MIM 1.2, §2.4.3.31 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.3.31`

#### Code

> De in een registratie of informatiemodel aan de enumeratiewaarde toegekend unieke code.
>
> — MIM 1.2, §2.4.3.32 (normatief)

> Toepassing: Enumeratiewaarde.
>
> — MIM 1.2, §2.4.3.32 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.3.32`

#### Indicatie abstract object

> Een indicatie die aangeeft of er objecten kunnen bestaan die getypeerd worden als zijnde objecten (instanties) van alleen dit objecttype.
>
> — MIM 1.2, §2.4.3.33 (normatief)

> Toepassing: Objecttype
>
> — MIM 1.2, §2.4.3.33 (normatief)

Waardebereik: waarden `Ja`, `Nee` (§2.4.5.1); default `Nee` (§2.4.5.2).

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.3.33`

#### Populatie

> Voor objecttypen die deel uitmaken van een (basis)registratie betreft dit de beschrijving van de exemplaren van het gedefinieerde objecttype die in de desbetreffende (basis)registratie voorhanden zijn.
>
> — MIM 1.2, §2.4.3.34 (normatief)

> Toepassing: Objecttype
>
> — MIM 1.2, §2.4.3.34 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.3.34`

#### Kwaliteit

> Beschrijving van de mate waarin in de registratie opgenomen objecten van het desbetreffende type volledig, juist, actueel, nauwkeurig en betrouwbaar zijn.
>
> — MIM 1.2, §2.4.3.35 (normatief)

> Toepassing: Objecttype
>
> — MIM 1.2, §2.4.3.35 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.3.35`

#### Eenheid

> Aanduiding van de eenheid die bij een meting of waarneming hoort.
>
> — MIM 1.2, §2.4.3.36 (normatief)

> Toepassing: Attribuutsoort, Referentie-element.
>
> — MIM 1.2, §2.4.3.36 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.3.36`

#### Minimumwaarde inclusief

> Minimumwaarde inclusief (`>=`) is de ondergrens van het waardebereik voor een attribuutsoort of data element getypeerd met een primitief datatype, inclusief die waarde zelf. De minimumwaarde moet van hetzelfde primitieve datatype zijn als het datatype van het modelelement waar het voor geldt.
>
> — MIM 1.2, §2.4.3.37 (normatief)

> Gebruik op attribuutsoorten, data elementen en referentie-elementen met een primitief datatype van het type:
> - Integer
> - Decimal
> - Float
> - Real
> - DateTime
> - Date
>
> — MIM 1.2, §2.4.3.37 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.3.37`

#### Minimumwaarde exclusief

> Minimumwaarde exclusief (`>`) is de ondergrens van het waardebereik voor een attribuutsoort of data element getypeerd met een primitief datatype, exclusief die waarde zelf. De minimumwaarde moet van hetzelfde primitieve datatype zijn als het datatype van het modelelement waar het voor geldt.
>
> — MIM 1.2, §2.4.3.38 (normatief)

> Gebruik op attribuutsoorten, data elementen en referentie-elementen met een primitief datatype van het type:
> - Integer
> - Decimal
> - Float
> - Real
> - DateTime
> - Date
>
> — MIM 1.2, §2.4.3.38 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.3.38`

#### Maximumwaarde inclusief

> Maximumwaarde inclusief (`<=`) is de bovengrens van het waardebereik voor een attribuutsoort of data element getypeerd met een primitief datatype, inclusief die waarde zelf. De maximumwaarde moet van hetzelfde primitieve datatype zijn als het datatype van het modelelement waar het voor geldt.
>
> — MIM 1.2, §2.4.3.39 (normatief)

> Gebruik op attribuutsoorten, data elementen en referentie-elementen met een primitief datatype van het type:
> - Integer
> - Decimal
> - Float
> - Real
> - DateTime
> - Date
>
> — MIM 1.2, §2.4.3.39 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.3.39`

#### Maximumwaarde exclusief

> Maximumwaarde exclusief (`<`) is de bovengrens van het waardebereik voor een attribuutsoort of data element getypeerd met een primitief datatype, exclusief die waarde zelf. De maximumwaarde moet van hetzelfde primitieve datatype zijn als het datatype van het modelelement waar het voor geldt.
>
> — MIM 1.2, §2.4.3.40 (normatief)

> Gebruik op attribuutsoorten, data elementen en referentie-elementen met een primitief datatype van het type:
> - Integer
> - Decimal
> - Float
> - Real
> - DateTime
> - Date
>
> — MIM 1.2, §2.4.3.40 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.3.40`

#### Mixin

> Metagegeven om bij een generalisatie aan te geven dat bij een implementatie die geen multiple inheritance ondersteunt de eigenschappen van de superklasse worden overgenomen door de subklasse. De superklasse zelf komt niet in de implementatie voor.
>
> — MIM 1.2, §2.4.3.41 (normatief)

> Toepassing: Generalisatie en alleen bij MIM niveau 3. Niet gebruiken bij generalisaties tussen datatypen.
>
> — MIM 1.2, §2.4.3.41 (normatief)

Waardebereik: waarden `Ja`, `Nee` (§2.4.5.1); default `Nee` (§2.4.5.2).

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.3.41`

### Bindingen tussen modelelementen (§2.4.4)

#### heeft attribuut

> De binding van een attribuutsoort als eigenschap aan een objecttype.
>
> — MIM 1.2, §2.4.4.1 (normatief)

Verkorte schrijfwijze: `attribuut`.

> Toepassing: Objecttype, Gegevensgroeptype en Relatieklasse.
>
> — MIM 1.2, §2.4.4.1 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.4.1`

#### heeft gegevensgroep

> De binding van een gegevensgroep als groep van eigenschappen aan een objecttype of gegevensgroeptype.
>
> — MIM 1.2, §2.4.4.2 (normatief)

Verkorte schrijfwijze: `gegevensgroep`.

> Toepassing: Objecttypen met Gegevensgroepen of een Gegevensgroeptype dat zelf ook weer een Gegevensgroeptype bevat.
>
> — MIM 1.2, §2.4.4.2 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.4.2`

#### heeft gegevensgroeptype

> De binding van een gegevensgroeptype als waardetype aan een gegevensgroep.
>
> — MIM 1.2, §2.4.4.3 (normatief)

Verkorte schrijfwijze: `gegevensgroeptype`.

> Toepassing: Gegevensgroep.
>
> — MIM 1.2, §2.4.4.3 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.4.3`

#### verwijst naar supertype

> De binding van een supertype aan een subtype middels een generalisatie.
>
> — MIM 1.2, §2.4.4.4 (normatief)

Verkorte schrijfwijze: `supertype`.

> Toepassing: Objecttype en Datatype.
>
> — MIM 1.2, §2.4.4.4 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.4.4`

#### heeft datatype

> De binding van een datatype aan een eigenschap.
>
> — MIM 1.2, §2.4.4.5 (normatief)

Verkorte schrijfwijze: `type`.

> Toepassing: Attribuutsoort, Keuze, Referentie-element, Data-element
>
> — MIM 1.2, §2.4.4.5 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.4.5`

#### heeft relatiesoort

> De binding van een objecttype aan een objecttype middels een relatiesoort.
>
> — MIM 1.2, §2.4.4.6 (normatief)

Verkorte schrijfwijze: `relatiesoort`.

> Toepassing: Objecttype, Gegevensgroeptype.
>
> — MIM 1.2, §2.4.4.6 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.4.6`

#### heeft externe koppeling

> De binding van een objecttype uit een extern package aan een objecttype.
>
> — MIM 1.2, §2.4.4.7 (normatief)

Verkorte schrijfwijze: `externe koppeling`.

> Toepassing: Objecttype, Gegevensgroeptype.
>
> — MIM 1.2, §2.4.4.7 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.4.7`

#### heeft data-element

> De binding van een data-element aan een gestructureerd datatype.
>
> — MIM 1.2, §2.4.4.8 (normatief)

Verkorte schrijfwijze: `data-element`.

> Toepassing: Gestructureerd datatype.
>
> — MIM 1.2, §2.4.4.8 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.4.8`

#### bevat modelelement

> De binding tussen een package en een modelelement dat zich in dat package bevindt.
>
> — MIM 1.2, §2.4.4.9 (normatief)

Verkorte schrijfwijze: `modelelement`.

> Toepassing: Package, Informatiemodel, Domein, Extern, View.
>
> — MIM 1.2, §2.4.4.9 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.4.9`

#### bevat enumeratiewaarde

> De binding van een enumeratiewaarde aan een enumeratie.
>
> — MIM 1.2, §2.4.4.10 (normatief)

Verkorte schrijfwijze: `waarde`.

> Toepassing: Enumeratie.
>
> — MIM 1.2, §2.4.4.10 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.4.10`

#### bevat referentie-element

> De binding van een referentie-element aan een referentielijst.
>
> — MIM 1.2, §2.4.4.11 (normatief)

Verkorte schrijfwijze: `referentie-element`.

> Toepassing: Referentielijst.
>
> — MIM 1.2, §2.4.4.11 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.4.11`

#### heeft datatypekeuze

> De binding van een keuze uit datatypen aan een attribuutsoort.
>
> — MIM 1.2, §2.4.4.12 (normatief)

Verkorte schrijfwijze: `datatypekeuze`.

> Toepassing: Attribuutsoort.
>
> — MIM 1.2, §2.4.4.12 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.4.12`

#### heeft attribuutkeuze

> De binding van een keuze uit attributen aan een attribuutsoort.
>
> — MIM 1.2, §2.4.4.13 (normatief)

Verkorte schrijfwijze: `attribuutkeuze`.

> Toepassing: Objecttype, Gegevensgroeptype, Relatieklasse, Attribuutsoort.
>
> — MIM 1.2, §2.4.4.13 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.4.13`

#### heeft keuzeattribuut

> De binding van een attribuutsoort aan een Keuze.
>
> — MIM 1.2, §2.4.4.14 (normatief)

Verkorte schrijfwijze: `keuzeattribuut`.

> Toepassing: Keuze.
>
> — MIM 1.2, §2.4.4.14 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.4.14`

#### heeft relatiedoelkeuze

> De binding van een keuze uit relatiedoelen aan een objecttype.
>
> — MIM 1.2, §2.4.4.15 (normatief)

Verkorte schrijfwijze: `relatiedoelkeuze`.

> Toepassing: Objecttype, Gegevensgroeptype, Keuze.
>
> — MIM 1.2, §2.4.4.15 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.4.15`

#### heeft relatiesoortkeuze

> De binding van een keuze uit relatiesoorten aan een objecttype.
>
> — MIM 1.2, §2.4.4.16 (normatief)

Verkorte schrijfwijze: `relatiesoortkeuze`.

> Toepassing: Objecttype, Gegevensgroeptype, Keuze.
>
> — MIM 1.2, §2.4.4.16 (normatief)

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.4.16`

#### heeft constraint

> De binding van een constraint aan een modelelement.
>
> — MIM 1.2, §2.4.4.17 (normatief)

Verkorte schrijfwijze: `constraint`.

Volledige tekst: `python3 scripts/mim.py paragraaf 2.4.4.17`

<!-- EINDE GEGENEREERD -->
