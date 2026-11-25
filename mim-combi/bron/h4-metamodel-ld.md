<!--
Bron: MIM - Metamodel Informatie Modellering, versie 1.2, vastgestelde versie 13 juni 2024 (Geonovum).
https://docs.geostandaarden.nl/mim/def-st-mim-20240613/
Licentie: CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/).
Bewerking: automatisch omgezet van HTML naar markdown door de kennisbank mim-kennis (build/extract_def.py).
Figuren zijn niet overgenomen; alleen hun bijschrift staat er. De tekst is verder ongewijzigd.
-->

# Hoofdstuk 4 — Metamodel in Linked Data

Letterlijke tekst van MIM 1.2 (DEF, 13 juni 2024). Elke kop begint met het paragraafnummer uit de vastgestelde versie.

## §4 Metamodel in Linked Data (LD)

### §4.1 Ontologisch metamodel in LD

Het MIM uitgedrukt in LD houdt onder ander een ontologisch metamodel in. Dit betekent dat er voor elk van de modelelementen van het MIM een klasse en/of eigenschap gedefinieerd is in termen van RDF, RDFS en OWL. In de hierop volgende paragrafen wordt deze uitwerking geven.

Het MIM is een _metamodel_. Dit betekent dat in termen van het MIM een concreet informatiemodel kan worden uitgewerkt, bijvoorbeeld het informatiemodel Basisregistratie Adressen en Gebouwen. Het MIM is niet bedoeld om vervolgens in termen van dit informatiemodel een concrete dataset te vormen. Zie ook 1.6 Typering van modellen gekoppeld aan beschouwingsniveaus: het MIM is niet beoogd voor een informatiemodel op niveau 4. Hiervoor is een transformatie nodig naar een (technisch) uitwisselings- of opslagmodel nodig.

Op diezelfde manier levert het toepassen van het MIM in RDF geen ontologie of vocabulaire waarin RDF kan worden uitgedrukt: slechts het informatiemodel zelf is op deze manier in RDF uitgedrukt. Voor de vertaalslag naar een ontologie is een afzonderlijke transformatie nodig.

Vanuit een Linked Data perspectief is dit bijzonder. Een kernmerk van Linked Data is namelijk dat een informatiemodel op niveau 3 _ook_ direct, zonder aanpassingen, bruikbaar is als informatiemodel op niveau 4. Sterker nog: Linked Data modellen zijn ook bruikbaar op niveau 1 en 2. Dit is vanuit het MIM zelf niet mogelijk. Hiervoor is een vertaalslag nodig naar een "echte" Linked Data ontologie.

Zo leidt een MIM objecttype "Schip" tot de volgende weergave in RDF:

```
@prefix vb: <http://modellen.mim-standaard.nl/voorbeeld/> .
@prefix mim: <http://modellen.mim-standaard.nl/def/mim#> .

vb:Schip a mim:Objecttype;
  rdfs:label "Schip"@nl;
.
```

`vb:Schip` is in dit voorbeeld een voorkomen van de klasse `mim:Objecttype`. dit voorkomen kent zelf geen voorkomens. Hiervoor is een vertaling nodig naar een `rdfs:Class`, bijvoorbeeld door:

```
@prefix vbo: <http://modellen.mim-standaard.nl/voorbeeld/def#>.

vbo:Schip a rdfs:Class;
  mim:equivalent vb:Schip;
.
vb:Pakjesboot12 a vbo:Schip.
```

De transformatie van het MIM model naar deze RDF ontologie is opgenomen in 6.4 Transformatie MIM - RDFS/OWL/SHACL.

### §4.2 Structuur metamodel in LD

Het RDF model is opgesplitst in twee delen. Zoals gebruikelijk in RDF zijn deze modeldelen via hun URL op het internet te benaderen:

1. de RDF vocabulaire, met de (meta)klassen en (meta)eigenschappen;
2. de RDF Shapesgraph, met "shapes", de structuur die gelden op het gebruik van de klassen en eigenschappen.

In onderstaande paragrafen wordt zowel de vocabulaire als de structuur gezamenlijk per modelelement besproken. Een RDF representatie in turtle wordt gegeven en daarnaast ook een grafische representatie. Hiervoor wordt de verbeelding gebruikt zoals beschreven in het document: Best Practises for meaningful connected computing.

Met behulp van bovenstaande twee - machine leesbare - bestanden kan een geserialiseerd MIM model uitgedrukt in RDF (bijvoorbeeld een XML, JSON of Turtle bestand) gevalideerd worden of deze correct conform MIM is opgesteld. Hiervoor kan bijvoorbeeld dit open source java tool gebruikt worden.

Bij het opstellen van het MIM in RDF is gebruik gemaakt van de algemene, tekstuele beschrijving van het MIM uit het hoofdstuk Metamodel Algemeen. Er is een 1-op-1 omzetting gedaan, zonder enige aanpassing van de beschrijvingen. Dit maakt het mogelijk om een MIM informatiemodel om te zetten van de ene representatie (bijvoorbeeld in UML) naar de andere en weer terug, zonder verlies van informatie.

De volgende regels zijn gebruikt bij de omzetting van de MIM tekst naar RDF:

1. Elk voorkomen van een MIM «metaclass» is omgezet naar een voorkomen van een `owl:Class`;
2. Elk metagegeven van een MIM «metaclass» is omgezet naar een voorkomen van een `owl:DatatypeProperty`, voor zover sprake is van een metagegeven dat een waarde heeft die met een datatype is uit te drukken (zoals tekstuele, numerieke of boolean metagegevens);
3. Elk metagegeven van een MIM «metaclass» is omgezet naar een voorkomen van een `owl:ObjectProperty`, voor zover sprake is van een metagegeven waarbij de waarde verwijst naar een voorkomen van een andere MIM «metaclass»;
4. Een `rdfs:label` is opgenomen met de naam van de MIM «metaclass» c.q. het metagegeven;
5. Een `rdfs:comment` is opgenomen met de definitie van de MIM «metaclass» c.q. het metagegeven.

Voor de omzetting van de gegevensconstraints (zoals cardinaliteiten, datatypen en properties per klasse), is op de volgende manier een SHACL shape graph gemaakt:

1. Elk voorkomen van een MIM «metaclass» kent ook een `sh:NodeShape` met een `sh:name` die overeen komt de originele technische naam (UpperCamelCase);
2. Voor elk voorkomen van een MIM «metaclass» zijn `sh:PropertyShapes` aangemaakt om aan te geven welke metagegevens zijn toegestaan voor een MIM «metaclass», de kardinaliteiten en het datatype c.q. de geassocieerde MIM «metaclass».

Ten opzichte van de UML weergave van het MIM metamodel kent het MIM in RDF alleen het gebruik van de namen van de metagegevens en niet de namen van de bindingen die bij deze metagegevens horen. Zo kent het UML metamodel voor de binding tussen Objecttype en Attribuutsoort de bindingsnaam "heeft attribuut" en de rolnaam "attribuut". Het MIM in RDF gebruikt alleen de rolnaam "attribuut" in dit geval.

#### §4.2.1 Kern

[Figuur: Figuur 27 Diagram: Kern metamodel in LD] (media/rdf-kern.png)

Als prefix wordt voor de vocabulaire gebruik gemaakt van `mim`, met de namespace `http://modellen.mim-standaard.nl/def/mim#`. Voor de shapes wordt als prefix gebruik gemaakt van `shape`, met als namespace `http://modellen.mim-standaard.nl/def/mim-shapes#`.

| **MIM metaclass** | **Metaclass in RDF** | **Shape in RDF** | **Grondslag** |
|---|---|---|---|
| Objecttype | `mim:Objecttype` | shape:Objecttype | grondslag |
| Attribuutsoort | `mim:Attribuutsoort` | shape:Attribuutsoort | grondslag |
| Gegevensgroep | `mim:Gegevensgroep` | shape:Gegevensgroep | grondslag |
| Gegevensgroeptype | `mim:Gegevensgroeptype` | shape:Gegevensgroeptype | grondslag |
| Generalisatie | `mim:Generalisatie` | shape:Generalisatie | grondslag |
| Relatiesoort | `mim:Relatiesoort` | shape:Relatiesoort | grondslag |
| Relatieklasse | `mim:Relatieklasse` | shape:Relatieklasse | grondslag |

In bovenstaand figuur zijn niet alle bindingen getekend rondom `mim:Relatiesoort`: dit zou het figuur onnodig complex maken. De bindingen met `mim:Gegevensgroeptype` zijn niet getekend. Dit is afgebeeld in onderstaand figuur. Daarbij is zichtbaar dat een `mim:Gegevensgroeptype` wel uitgaande relaties kan hebben, maar geen inkomende relaties: dat is altijd een `mim:Objecttype`.

[Figuur: Figuur 28 Diagram: Bindingen met mim:Gegevensgroeptype in LD] (media/rdf-relatiekern.png)

#### §4.2.2 Datatypen

[Figuur: Figuur 29 Diagram: Datatypen in LD] (media/rdf-datatype.png)

| **MIM metaclass** | **Metaclass in RDF** | **Shape in RDF** | **Grondslag** |
|---|---|---|---|
| Datatype | `mim:Datatype` | shape:Datatype | grondslag |
| Primitief datatype | `mim:PrimitiefDatatype` | shape:PrimitiefDatatype | grondslag |
| Gestructureerd datatype | `mim:GestructuurdDatatype` | shape:GestructuurdDatatype | grondslag |
| Data element | `mim:DataElement` | shape:DataElement | grondslag |
| Enumeratie | `mim:Enumeratie` | shape:Enumeratie | grondslag |
| Enumeratiewaarde | `mim:Enumeratiewaarde` | shape:Enumeratiewaarde | grondslag |
| Referentielijst | `mim:Referentielijst` | shape:Referentielijst | grondslag |
| Referentie element | `mim:ReferentieElement` | shape:ReferentieElement | grondslag |
| Codelijst | `mim:Codelijst` | shape:Codelijst | grondslag |

#### §4.2.3 Overige

##### §4.2.3.1 Constraint

[Figuur: Figuur 30 Diagram: Constraint in LD] (media/rdf-constraint.png)

| **MIM metaclass** | **Metaclass in RDF** | **Shape in RDF** | **Grondslag** |
|---|---|---|---|
| Constraint | `mim:Constraint` | shape:Constraint | grondslag |
| Keuzeconstraint | `mim:Keuzeconstraint` | shape:Keuze | grondslag |

##### §4.2.3.2 Keuze

De "keuze constructie" maakt een keuze mogelijk tussen meerdere attribuutsoorten, datatypen en relatiedoelen (objecttypen). Er mag aan één specifieke keuze maar één soort van deze drie worden verbonden. Indien dit datatype gekozen wordt voor een attribuutsoort of relatiedoel, dan heeft dit de volgende betekenis, afhankelijk van de verbonden soort:

- Attribuutsoort: een keuze tussen attribuutsoorten **in plaats van** de attribuutsoort die deze keuze als datatype heeft;
- Datatype: een keuze tussen datatypen **in plaats van** dit keuze datatype;
- Relatiedoel: een keuze tussen objecttypen als relatiedoel **in plaats van** het doel van de relatieroldoel

| **MIM metaclass** | **Metaclass in RDF** | **Shape in RDF** | **Grondslag** |
|---|---|---|---|
| Keuze | `mim:Keuze` | shape:Keuze | grondslag |
| Datatype | `mim:Datatype` | shape:Datatype | grondslag |
| Objecttype | `mim:Objecttype` | shape:Objecttype | grondslag |
| Attribuutsoort | `mim:Attribuutsoort` | shape:Attribuutsoort | grondslag |

_Datatypekeuze_

[Figuur: Figuur 31 Diagram: Datatypekeuze in LD] (media/rdf-keuze-datatype.png)

Aangezien een `mim:Keuze` een specialisatie is van een `mim:Datatype`, mag een attribuutsoort via een `mim:type` een verwijzen naar een Keuze. Een dergelijk keuze heeft in dit geval zelf minimaal twee `mim:type` verwijzingen naar de 2 (of meer) datatypen waaruit gekozen wordt.

_Attribuutkeuze_

[Figuur: Figuur 32 Diagram: Attribuutkeuze in LD] (media/rdf-keuze-attribuut.png)

Indien een `mim:Keuze` wordt gebruikt voor een keuze tussen attribuutsoorten, dan wordt vanuit een objecttype via een `mim:attribuut` niet verwezen naar een attribuutsoort, maar naar de keuze. De keuze zelf verwijst op zijn beurt naar de attribuutsoorten waartussen gekozen wordt.

_Relatiedoelkeuze_

[Figuur: Figuur 33 Diagram: Relatiedoelkeuze in LD] (media/rdf-keuze-relatiedoel.png)

Indien een `mim:Keuze` wordt gebruikt voor een keuze tussen objecttypen die de relatiedoelen zijn voor een relatiesoort, dan wordt vanuit een relatiesoort via een `mim:doel` niet verwezen naar een objecttype, maar naar de keuze. De keuze zelf verwijst op zijn beurt naar de objecttypen waartussen gekozen wordt.

_Relatiesoortkeuze_

[Figuur: Figuur 34 Diagram: Relatiesoortkeuze in LD] (media/rdf-keuze-relatiesoort.png)

Een keuze tussen relatiesoorten wordt gedaan op basis van een keuzeconstraint. Een keuzeconstraint is geen datatype, maar juist een constraint die in dit geval aangeeft dat er een keuze gemaakt moet worden tussen twee relatiesoorten.

##### §4.2.3.3 Relatierol

[Figuur: Figuur 35 Diagram: Relatierol in LD] (media/rdf-relatie.png)

| **MIM metaclass** | **Metaclass in RDF** | **Shape in RDF** | **Grondslag** |
|---|---|---|---|
| Relatierol (abstract) | `Relatierol` | shape:Relatierol | grondslag |
| Relatierol bron | `RelatierolBron` | shape:RelatierolBron | grondslag |
| Relatierol doel | `RelatierolDoel` | shape:RelatierolDoel | grondslag |

##### §4.2.3.4 Externe koppeling

| **MIM metaclass** | **Metaclass in RDF** | **Shape in RDF** | **Grondslag** |
|---|---|---|---|
| Externe koppeling | `mim:ExterneKoppeling` | shape:ExterneKoppeling | grondslag |

##### §4.2.3.5 Packages

[Figuur: Figuur 36 Diagram: Packages in LD] (media/rdf-packages.png)

Het metagegeven bevat modelelement geeft aan dat packages modelelementen kunnen bevatten. Dit metagegeven wordt in het Linked Data metamodel opgenomen als relatie. Welke modelelementen precies toegestaan zijn, wordt in het plaatje niet tot uitdrukking gebracht. Zie hiervoor sectie 2.6.

| **MIM metaclass** | **Metaclass in RDF** | **Shape in RDF** | **Grondslag** |
|---|---|---|---|
| Package | `mim:Package` | shape:Package | grondslag |
| Informatiemodel | `mim:Informatiemodel` | shape:Informatiemodel | grondslag |
| Domein (het eigen IM) | `mim:Domein` | shape:Domein | grondslag |
| Extern | `mim:Extern` | shape:Extern | grondslag |
| View | `mim:View` | shape:View | grondslag |

### §4.3 Specificatie metagegevens in LD

Deze paragraaf is een aanvulling op de paragraaf 2.4 Specificatie metagegevens. De betekenis van de metagegevens worden in LD gespecificeerd los van de klasse waartoe deze metagegevens behoren. Hieronder is een opsomming gegeven van alle metagegevens en de overeenkomstige meta-eigenschap in RDF. De gegevensregels (structuur) voor de metagegevens zijn wel specifiek per klasse, en worden in de betreffende paragraaf behandeld.

| **MIM metagegeven** | **Meta-eigenschap in RDF** | **RDF type** | **Grondslag** |
|---|---|---|---|
| aggregatietype | `mim:aggregatietype` | owl:ObjectProperty | grondslag |
| alias | `mim:alias` | owl:DatatypeProperty | grondslag |
| attribuut | `mim:attribuut` | owl:ObjectProperty | grondslag |
| authentiek | `mim:authentiek` | owl:ObjectProperty | grondslag |
| basis-URI | `mim:basisUri` | owl:DatatypeProperty | grondslag |
| begrip | `mim:begrip` | owl:ObjectProperty | grondslag |
| begripsterm | `mim:begripsterm` | owl:DatatypeProperty | grondslag |
| bron | `mim:bron` | owl:ObjectProperty | grondslag |
| code | `mim:code` | owl:DatatypeProperty | grondslag |
| constraint | `mim:constraint` | owl:ObjectProperty | grondslag |
| data-element | `mim:dataElement` | owl:ObjectProperty | grondslag |
| datum opname | `mim:datumOpname` | owl:DatatypeProperty | grondslag |
| definitie | `mim:definitie` | owl:DatatypeProperty | grondslag |
| doel | `mim:doel` | owl:ObjectProperty | grondslag |
| formeel patroon | `mim:formeelPatroon` | owl:DatatypeProperty | grondslag |
| gegevensgroep | `mim:gegevensgroep` | owl:ObjectProperty | grondslag |
| groeptype | `mim:groeptype` | owl:ObjectProperty | grondslag |
| herkomst | `mim:herkomst` | owl:DatatypeProperty | grondslag |
| herkomst definitie | `mim:herkomstDefinitie` | owl:DatatypeProperty | grondslag |
| identificerend | `mim:identificerend` | owl:DatatypeProperty | grondslag |
| indicatie abstract object | `mim:indicatieAbstractObject` | owl:DatatypeProperty | grondslag |
| indicatie afleidbaar | `mim:indicatieAfleidbaar` | owl:DatatypeProperty | grondslag |
| indicatie classificerend | `mim:indicatieClassificerend` | owl:DatatypeProperty | grondslag |
| heeft tijdlijn geldigheid | `mim:heeftTijdlijnGeldigheid` | owl:DatatypeProperty | grondslag |
| indicatie materiële historie | `mim:indicatieMaterieleHistorie` | owl:DatatypeProperty | grondslag |
| heeft tijdlijn registratie | `mim:heeftTijdlijnRegistratie` | owl:DatatypeProperty | grondslag |
| indicatie formele historie | `mim:indicatieFormeleHistorie` | owl:DatatypeProperty | grondslag |
| informatiedomein | `mim:informatiedomein` | owl:DatatypeProperty | grondslag |
| informatiemodeltype | `mim:informatiemodeltype` | owl:ObjectProperty | grondslag |
| kardinaliteit | `mim:kardinaliteit` | owl:DatatypeProperty | grondslag |
| kwaliteit | `mim:kwaliteit` | owl:DatatypeProperty |  |
| lengte | `mim:lengte` | owl:DatatypeProperty | grondslag |
| locatie | `mim:locatie` | owl:DatatypeProperty | grondslag |
| identificatie | `mim:identificatie` | owl:DatatypeProperty | grondslag |
| mim extensie | `mim:extensie` | owl:DatatypeProperty | grondslag |
| mim taal | `mim:taal` | owl:DatatypeProperty | grondslag |
| mim tekstopmaak | `mim:tekstopmaak` | owl:DatatypeProperty | grondslag |
| mim versie | `mim:versie` | owl:DatatypeProperty | grondslag |
| mogelijk geen waarde | `mim:mogelijkGeenWaarde` | owl:DatatypeProperty | grondslag |
| naam | `mim:naam` | owl:DatatypeProperty | grondslag |
| patroon | `mim:patroon` | owl:DatatypeProperty | grondslag |
| populatie | `mim:populatie` | owl:DatatypeProperty |  |
| referentie-element | `mim:referentieElement` | owl:ObjectProperty | grondslag |
| relatiemodelleringstype | `mim:relatiemodelleringstype` | owl:ObjectProperty | grondslag |
| relatierol | `mim:relatierol` | owl:ObjectProperty |  |
| specificatie formeel | `mim:specificatieFormeel` | owl:DatatypeProperty |  |
| specificatie tekst | `mim:specificatieTekst` | owl:DatatypeProperty |  |
| subtype | `mim:subtype` | owl:ObjectProperty |  |
| supertype | `mim:supertype` | owl:ObjectProperty |  |
| toelichting | `mim:toelichting` | owl:DatatypeProperty | grondslag |
| type | `mim:type` | owl:ObjectProperty | grondslag |
| unidirectioneel | `mim:unidirectioneel` | owl:DatatypeProperty | grondslag |
| waarde | `mim:waarde` | owl:ObjectProperty | grondslag |
| minimumwaarde inclusief | `mim:minimumwaardeInclusief` | owl:DatatypeProperty | grondslag |
| minimumwaarde exclusief | `mim:minimumwaardeExclusief` | owl:DatatypeProperty | grondslag |
| maximumwaarde inclusief | `mim:maximumwaardeInclusief` | owl:DatatypeProperty | grondslag |
| maximumwaarde exclusief | `mim:maximumwaardeExclusief` | owl:DatatypeProperty | grondslag |
| mixin | `mim:mixin` | owl:DatatypeProperty | grondslag |

#### §4.3.1 Objecten en attributen in LD

##### §4.3.1.1 mim:Objecttype

De objecttypen worden naar de volgende aspecten gespecificeerd:

| **Aspect** | **Eigenschap** | **Kardinaliteit** | **Datatype of klasse** |
|---|---|---|---|
| Identificatie | `mim:identificatie` | 1 | `xsd:anyURI` |
| Naam | `mim:naam` | 1 | tekst |
| Alias | `mim:alias` | 0..1 | tekst |
| Begrip | `mim:begrip` | 0..* | `skos:Concept` |
| Begripsterm | `mim:begripsterm` | 0..* | tekst |
| Herkomst | `mim:herkomst` | 1 | tekst |
| Definitie | `mim:definitie` | 1 | tekst |
| Herkomst definitie | `mim:herkomstDefinitie` | 1 | tekst |
| Datum opname | `mim:datumOpname` | 1 | datum |
| Populatie | `mim:populatie` | 0..1 | tekst |
| Kwaliteit | `mim:kwaliteit` | 0..1 | tekst |
| Toelichting | `mim:toelichting` | 0..1 | tekst |
| Indicatie abstract object | `mim:indicatieAbstractObject` | 1 | boolean |
| Attribuut | `mim:attribuut` | 0..* | `mim:Attribuutsoort` |
| Gegevensgroep | `mim:gegevensgroep` | 0..* | `mim:Gegevensgroep` |
| Constraint | `mim:constraint` | 0..* | `mim:Constraint` |

##### §4.3.1.2 mim:Attribuutsoort

De attribuutsoorten worden naar de volgende aspecten gespecificeerd:

| **Aspect** | **Eigenschap** | **Kardinaliteit** | **Datatype of klasse** |
|---|---|---|---|
| Identificatie | `mim:identificatie` | 1 | `xsd:anyURI` |
| Naam | `mim:naam` | 1 | tekst |
| Alias | `mim:alias` | 0..1 | tekst |
| Begrip | `mim:begrip` | 0..* | `skos:Concept` |
| Begripsterm | `mim:begripsterm` | 0..* | tekst |
| Herkomst | `mim:herkomst` | 1 | tekst |
| Definitie | `mim:definitie` | 1 | tekst |
| Herkomst definitie | `mim:herkomstDefinitie` | 1 | tekst |
| Datum opname | `mim:datumOpname` | 1 | datum |
| Type | `mim:type` | 1 | `mim:Datatype` |
| Lengte | `mim:lengte` | 0..1 | tekst |
| Patroon | `mim:patroon` | 0..1 | tekst |
| Formeel patroon | `mim:formeelPatroon` | 0..1 | tekst |
| Heeft tijdlijn geldigheid | `mim:heeftTijdlijnGeldigheid` | 1 | boolean |
| Indicatie materiële historie | `mim:indicatieMaterieleHistorie` | 1 | boolean |
| Heeft tijdlijn registratie | `mim:heeftTijdlijnRegistratie` | 1 | boolean |
| Indicatie formele historie | `mim:indicatieFormeleHistorie` | 1 | boolean |
| Kardinaliteit | `mim:kardinaliteit` | 1 | tekst |
| Authentiek | `mim:authentiek` | 1 | Authenticiteit |
| Toelichting | `mim:toelichting` | 0..1 | tekst |
| Indicatie afleidbaar | `mim:indicatieAfleidbaar` | 1 | boolean |
| Indicatie classificerend | `mim:indicatieAfleidbaar` | 1 | boolean |
| Mogelijk geen waarde | `mim:mogelijkGeenWaarde` | 1 | boolean |
| Identificerend | `mim:identificerend` | 0..1 | boolean |
| Eenheid | `mim:eenheid` | 0..1 | `si:MeasurementUnit` |
| Constraint | `mim:constraint` | 0..* | `mim:Constraint` |
| Minimumwaarde inclusief | `mim:minimumwaardeInclusief` | 0..1 | integer, decimal, float, real, dateTime, date |
| Minimumwaarde exclusief | `mim:minimumwaardeExclusief` | 0..1 | integer, decimal, float, real, dateTime, date |
| Maximumwaarde inclusief | `mim:maximumwaardeInclusief` | 0..1 | integer, decimal, float, real, dateTime, date |
| Maximumwaarde exclusief | `mim:maximumwaardeExclusief` | 0..1 | integer, decimal, float, real, dateTime, date |

Het veld `mim:authentiek` verwijst naar één van de volgende mogelijke waarden:

| **Authenticiteit** | **Definitie** |
|---|---|
| `mim:Authentiek` | In een basisregistratie opgenomen gegeven dat bij wettelijk voorschrift als authentiek is aangemerkt. |
| `mim:Basisgegeven` | Een in een basisregistratie opgenomen gegeven. |
| `mim:WettelijkGegeven` | Gegeven behorende bij een wettelijke registratie, niet zijnde een basisregistratie |
| `mim:LandelijkKerngegeven` | Indien het een gegeven of een als relatiesoort gemodelleerd gegeven is in een landelijk sector- en domein-overstijgend informatiemodel en geen authentiek gegeven en geen basisgegeven is. |
| `mim:OverigeAuthenticiteit` | Indien het géén van de voorgaande categorieën betreft. Veelal gaat het dan om proces-, taakveld- of domeinspecifieke gegevens. |

Het veld `mim:eenheid` verwijst naar een waarde afkomstig uit SI Digital framework.

##### §4.3.1.3 mim:Gegevensgroep

De gegevensgroepen worden naar de volgende aspecten gespecificeerd:

| **Aspect** | **Eigenschap** | **Kardinaliteit** | **Datatype of klasse** |
|---|---|---|---|
| Identificatie | `mim:identificatie` | 1 | `xsd:anyURI` |
| Naam | `mim:naam` | 1 | tekst |
| Alias | `mim:alias` | 0..1 | tekst |
| Begrip | `mim:begrip` | 0..* | `skos:Concept` |
| Begripsterm | `mim:begripsterm` | 0..* | tekst |
| Definitie | `mim:definitie` | 1 | tekst |
| Toelichting | `mim:toelichting` | 0..1 | tekst |
| Gegevensgroeptype | `mim:gegevensgroeptype` | 1 | `mim:Gegevensgroeptype` |
| Herkomst | `mim:herkomst` | 1 | tekst |
| Herkomst definitie | `mim:herkomstDefinitie` | 1 | tekst |
| Datum opname | `mim:datumOpname` | 1 | datum |
| Kardinaliteit | `mim:kardinaliteit` | 1 | tekst |
| Authentiek | `mim:authentiek` | 1 | Authenticiteit |
| Constraint | `mim:constraint` | 0..* | `mim:Constraint` |

##### §4.3.1.4 mim:Gegevensgroeptype

De gegevensgroeptypen worden naar de volgende aspecten gespecificeerd:

| **Aspect** | **Eigenschap** | **Kardinaliteit** | **Datatype of klasse** |
|---|---|---|---|
| Identificatie | `mim:identificatie` | 1 | `xsd:anyURI` |
| Naam | `mim:naam` | 1 | tekst |
| Alias | `mim:alias` | 0..1 | tekst |
| Begrip | `mim:begrip` | 0..* | `skos:Concept` |
| Begripsterm | `mim:begripsterm` | 0..* | tekst |
| Definitie | `mim:definitie` | 0..1 | tekst |
| Herkomst definitie | `mim:herkomstDefinitie` | 0..1 | tekst |
| Toelichting | `mim:toelichting` | 0..1 | tekst |
| Datum opname | `mim:datumOpname` | 1 | datum |
| Attribuut | `mim:attribuut` | 0..* | `mim:Attribuutsoort` |
| Gegevensgroep | `mim:gegevensgroep` | 0..* | `mim:Gegevensgroep` |
| Constraint | `mim:constraint` | 0..* | `mim:Constraint` |

#### §4.3.2 Relaties in LD

Het metamodel heeft twee manieren om een relatie tussen twee objecttypen te beschrijven. Deze keuze wordt aangegeven in de eigen extensie, zoals beschreven in 1.9 Uitdrukken in Linked Data. Alleen het gekozen alternatief is relevant voor de modellering in uw informatiemodel.

- Alternatief 1: Verplichte benoeming van de naam van de relatie met de bijbehorende metagegevens
- Alternatief 2: Verplichte benoeming van de rol van het doel in een relatie met de bijbehorende metagegevens en optioneel de benoeming van de naam van de relatie.

Beide alternatieven gebruiken relatiesoort en relatierol, maar met andere regels voor gebruik.

##### §4.3.2.1 mim:Relatiesoort (alt 1: soort leidend)

De relatiesoorten worden naar de volgende aspecten gespecificeerd.

| **Aspect** | **Eigenschap** | **Kardinaliteit** | **Datatype of klasse** |
|---|---|---|---|
| Identificatie | `mim:identificatie` | 1 | `xsd:anyURI` |
| Naam | `mim:naam` | 1 | tekst |
| Alias | `mim:alias` | 0..1 | tekst |
| Begrip | `mim:begrip` | 0..* | `skos:Concept` |
| Begripsterm | `mim:begripsterm` | 0..* | tekst |
| Unidirectioneel | `mim:unidirectioneel` | 1 | boolean |
| Bron | `mim:bron` | 1 | `mim:Objecttype` |
| Doel | `mim:doel` | 1 | `mim:Objecttype` |
| Aggregatietype | `mim:aggregatietype` | 1 | Aggregatietype |
| Kardinaliteit | `mim:kardinaliteit` | 1 | tekst |
| Kardinaliteit relatie bron | `mim:kardinaliteitRelatieBron` | 0..1 | tekst |
| Herkomst | `mim:herkomst` | 1 | tekst |
| Definitie | `mim:definitie` | 1 | tekst |
| Toelichting | `mim:toelichting` | 0..1 | tekst |
| Herkomst definitie | `mim:herkomstDefinitie` | 1 | tekst |
| Datum opname | `mim:datumOpname` | 1 | datum |
| Identificerend | `mim:identificerend` | 0..1 | boolean |
| Heeft tijdlijn geldigheid | `mim:heeftTijdlijnGeldigheid` | 1 | boolean |
| Indicatie materiële historie | `mim:indicatieMaterieleHistorie` | 1 | boolean |
| Heeft tijdlijn registratie | `mim:heeftTijdlijnRegistratie` | 1 | boolean |
| Indicatie formele historie | `mim:indicatieFormeleHistorie` | 1 | boolean |
| Authentiek | `mim:authentiek` | 1 | Authenticiteit |
| Indicatie afleidbaar | `mim:indicatieAfleidbaar` | 1 | boolean |
| Mogelijk geen waarde | `mim:mogelijkGeenWaarde` | 1 | boolean |
| Constraint | `mim:constraint` | 0..* | `mim:Constraint` |

Het veld `mim:aggregatietype` verwijst naar één van de volgende mogelijke waarden:

| **Aggregatietype** | **Definitie** |
|---|---|
| `mim:Geen` | Er is geen sprake van een aggregatie |
| `mim:Compositie` | Compositie (gesloten wiebertje) |
| `mim:Gedeeld` | Gedeelde aggregatie (open wiebertje) |

##### §4.3.2.2 mim:Relatiesoort (alt 2: rol leidend)

De relatiesoorten worden naar de volgende aspecten gespecificeerd.

| **Aspect** | **Eigenschap** | **Kardinaliteit** | **Datatype of klasse** |
|---|---|---|---|
| Identificatie | `mim:identificatie` | 1 | `xsd:anyURI` |
| Naam | `mim:naam` | 0..1 | tekst |
| Alias | `mim:alias` | 0..1 | tekst |
| Begrip | `mim:begrip` | 0..* | `skos:Concept` |
| Begripsterm | `mim:begripsterm` | 0..* | tekst |
| Definitie | `mim:definitie` | 0..1 | tekst |
| Relatierol | `mim:relatierol` | 1..2 | `Relatierol` |
| Constraint | `mim:constraint` | 0..* | `mim:Constraint` |

##### §4.3.2.3 mim:Relatierol (alt 1: soort leidend)

Voor relatierollen worden naar de volgende aspecten gespecificeerd.

| **Aspect** | **Eigenschap** | **Kardinaliteit** | **Datatype of klasse** |
|---|---|---|---|
| Identificatie | `mim:identificatie` | 1 | `xsd:anyURI` |
| Naam | `mim:naam` | 0..1 | tekst |
| Alias | `mim:alias` | 0..1 | tekst |
| Begrip | `mim:begrip` | 0..* | `skos:Concept` |
| Begripsterm | `mim:begripsterm` | 0..* | tekst |
| Definitie | `mim:definitie` | 0..1 | tekst |
| Constraint | `mim:constraint` | 0..* | `mim:Constraint` |

##### §4.3.2.4 mim:Relatierol (alt 2: rol leidend)

Voor relatierol worden bij het doel rol van een relatiesoort de volgende aspecten gespecificeerd.

| **Aspect** | **Eigenschap** | **Kardinaliteit** | **Datatype of klasse** |
|---|---|---|---|
| Identificatie | `mim:identificatie` | 1 | `xsd:anyURI` |
| Naam | `mim:naam` | 1 | tekst |
| Alias | `mim:alias` | 0..1 | tekst |
| Begrip | `mim:begrip` | 0..* | `skos:Concept` |
| Begripsterm | `mim:begripsterm` | 0..* | tekst |
| Kardinaliteit | `mim:kardinaliteit` | 1 | tekst |
| Herkomst | `mim:herkomst` | 1 | tekst |
| Definitie | `mim:definitie` | 1 | tekst |
| Toelichting | `mim:toelichting` | 0..1 | tekst |
| Herkomst definitie | `mim:herkomstDefinitie` | 1 | tekst |
| Datum opname | `mim:datumOpname` | 1 | datum |
| Identificerend | `mim:identificerend` | 0..1 | boolean |
| Heeft tijdlijn geldigheid | `mim:heeftTijdlijnGeldigheid` | 1 | boolean |
| Indicatie materiële historie | `mim:indicatieMaterieleHistorie` | 1 | boolean |
| Heeft tijdlijn registratie | `mim:heeftTijdlijnRegistratie` | 1 | boolean |
| Indicatie formele historie | `mim:indicatieFormeleHistorie` | 1 | boolean |
| Authentiek | `mim:authentiek` | 1 | Authenticiteit |
| Mogelijk geen waarde | `mim:mogelijkGeenWaarde` | 1 | boolean |
| Constraint | `mim:constraint` | 0..* | `mim:Constraint` |

##### §4.3.2.5 mim:Generalisatie bij objecttypen

De generalisaties worden naar het volgende aspect gespecificeerd:

| **Aspect** | **Eigenschap** | **Kardinaliteit** | **Datatype of klasse** |
|---|---|---|---|
| Identificatie | `mim:identificatie` | 1 | `xsd:anyURI` |
| Subtype | `mim:definitie` | 1 | `mim:Objecttype` |
| Supertype | `mim:definitie` | 1 | `mim:Objecttype` |
| Datum opname | `mim:datumOpname` | 1 | datum |
| Mixin | `mim:mixin` | 1 | boolean |

##### §4.3.2.6 mim:Generalisatie bij datatypen

De generalisaties worden naar het volgende aspect gespecificeerd:

| **Aspect** | **Eigenschap** | **Kardinaliteit** | **Datatype of klasse** |
|---|---|---|---|
| Identificatie | `mim:identificatie` | 1 | `xsd:anyURI` |
| Subtype | `mim:definitie` | 1 | `mim:Datatype` |
| Supertype | `mim:definitie` | 1 | `mim:Datatype` |

##### §4.3.2.7 mim:Relatieklasse

De relatieklassen worden naar de volgende aspecten gespecificeerd:

| **Aspect** | **Eigenschap** | **Kardinaliteit** | **Datatype of klasse** |
|---|---|---|---|
| Identificatie | `mim:identificatie` | 1 | `xsd:anyURI` |
| Naam | `mim:naam` | 0..1 | tekst |
| Alias | `mim:alias` | 0..1 | tekst |
| Herkomst | `mim:herkomst` | 1 | tekst |
| Begrip | `mim:begrip` | 0..* | `skos:Concept` |
| Begripsterm | `mim:begripsterm` | 0..* | tekst |
| Definitie | `mim:definitie` | 0..1 | tekst |
| Herkomst definitie | `mim:herkomstDefinitie` | 1 | tekst |
| Toelichting | `mim:toelichting` | 0..1 | tekst |
| Datum opname | `mim:datumOpname` | 1 | datum |
| Constraint | `mim:constraint` | 0..* | `mim:Constraint` |
| Unidirectioneel | `mim:unidirectioneel` | 1 | boolean |
| Aggregatietype | `mim:aggregatietype` | 1 | Aggregatietype |
| Kardinaliteit | `mim:kardinaliteit` | 1 | tekst |
| Heeft tijdlijn geldigheid | `mim:heeftTijdlijnGeldigheid` | 1 | boolean |
| Indicatie materiële historie | `mim:indicatieMaterieleHistorie` | 1 | boolean |
| Heeft tijdlijn registratie | `mim:heeftTijdlijnRegistratie` | 1 | boolean |
| Indicatie formele historie | `mim:indicatieFormeleHistorie` | 1 | boolean |
| Authentiek | `mim:authentiek` | 1 | Authenticiteit |
| Indicatie afleidbaar | `mim:indicatieAfleidbaar` | 1 | boolean |
| Mogelijk geen waarde | `mim:mogelijkGeenWaarde` | 1 | boolean |

##### §4.3.2.8 mim:ExterneKoppeling

Externe koppelingen worden naar de volgende aspecten gespecificeerd.

| **Aspect** | **Eigenschap** | **Kardinaliteit** | **Datatype of klasse** |
|---|---|---|---|
| Identificatie | `mim:identificatie` | 1 | `xsd:anyURI` |
| Naam | `mim:naam` | 1 | tekst |
| Alias | `mim:alias` | 0..1 | tekst |
| Begrip | `mim:begrip` | 0..* | `skos:Concept` |
| Begripsterm | `mim:begripsterm` | 0..* | tekst |
| Unidirectioneel | `mim:unidirectioneel` | 1 | boolean |
| Bron | `mim:bron` | 1 | `mim:Objecttype` |
| Doel | `mim:doel` | 1 | `mim:Objecttype` |
| Aggregatietype | `mim:aggregatietype` | 1 | Aggregatietype |
| Kardinaliteit | `mim:kardinaliteit` | 1 | tekst |
| Herkomst | `mim:herkomst` | 1 | tekst |
| Definitie | `mim:definitie` | 1 | tekst |
| Toelichting | `mim:toelichting` | 0..1 | tekst |
| Herkomst definitie | `mim:herkomstDefinitie` | 1 | tekst |
| Datum opname | `mim:datumOpname` | 1 | datum |
| Heeft tijdlijn geldigheid | `mim:heeftTijdlijnGeldigheid` | 1 | boolean |
| Indicatie materiële historie | `mim:indicatieMaterieleHistorie` | 1 | boolean |
| Heeft tijdlijn registratie | `mim:heeftTijdlijnRegistratie` | 1 | boolean |
| Indicatie formele historie | `mim:indicatieFormeleHistorie` | 1 | boolean |
| Authentiek | `mim:authentiek` | 1 | Authenticiteit |
| Indicatie afleidbaar | `mim:indicatieAfleidbaar` | 1 | boolean |
| Mogelijk geen waarde | `mim:mogelijkGeenWaarde` | 1 | boolean |
| Constraint | `mim:constraint` | 0..* | `mim:Constraint` |

#### §4.3.3 Waardelijsten in LD

Waar in onderstaande specificaties sprake is van een locatie, wordt in Linked Data termen veronderstelt dat op deze locatie de waardelijst te vinden is. Concreet betekent dit dat via content negotiation de waardelijst in een specifieke serialisatie van Linked Data is op te halen (zoals: JSON-LD, RDF/XML, Turtle). Vervolgens wordt verondersteld dat de resources in dit bestand de afzonderlijke waarden van de waardelijst zijn, of andere metagegevens van de waardelijst. Zo ligt voor de hand dat het bestand een resource bevat met dezelfde URL als opgegeven in de locatie, waarmee nadere informatie kan worden aangegeven.

##### §4.3.3.1 mim:Referentielijst

Voor referentielijsten worden de volgende aspecten gespecificeerd:

| **Aspect** | **Eigenschap** | **Kardinaliteit** | **Datatype of klasse** |
|---|---|---|---|
| Identificatie | `mim:identificatie` | 1 | `xsd:anyURI` |
| Naam | `mim:naam` | 1 | tekst |
| Alias | `mim:alias` | 0..1 | tekst |
| Begrip | `mim:begrip` | 0..* | `skos:Concept` |
| Begripsterm | `mim:begripsterm` | 0..* | tekst |
| Herkomst | `mim:herkomst` | 1 | tekst |
| Definitie | `mim:definitie` | 1 | tekst |
| Herkomst definitie | `mim:herkomstDefinitie` | 1 | tekst |
| Datum opname | `mim:datumOpname` | 1 | datum |
| Toelichting | `mim:toelichting` | 0..1 | tekst |
| Locatie | `mim:locatie` | 1 | tekst |
| Referentie-element | `mim:referentieElement` | 1..* | `mim:ReferentieElement` |
| Constraint | `mim:constraint` | 0..* | `mim:Constraint` |

##### §4.3.3.2 mim:ReferentieElement

De referentie-elementen worden naar de volgende aspecten gespecificeerd:

| **Aspect** | **Eigenschap** | **Kardinaliteit** | **Datatype of klasse** |
|---|---|---|---|
| Identificatie | `mim:identificatie` | 1 | `xsd:anyURI` |
| Naam | `mim:naam` | 1 | tekst |
| Alias | `mim:alias` | 0..1 | tekst |
| Begrip | `mim:begrip` | 0..* | `skos:Concept` |
| Begripsterm | `mim:begripsterm` | 0..* | tekst |
| Definitie | `mim:definitie` | 1 | tekst |
| Datum opname | `mim:datumOpname` | 1 | datum |
| Type | `mim:type` | 1 | `mim:Datatype` |
| Lengte | `mim:lengte` | 0..1 | tekst |
| Patroon | `mim:patroon` | 0..1 | tekst |
| Formeel patroon | `mim:formeelPatroon` | 0..1 | tekst |
| Kardinaliteit | `mim:kardinaliteit` | 1 | tekst |
| Identificerend | `mim:identificerend` | 0..1 | tekst |
| Toelichting | `mim:toelichting` | 0..1 | tekst |
| Constraint | `mim:constraint` | 0..* | `mim:Constraint` |
| Eenheid | `mim:eenheid` | 0..1 | `si:MeasurementUnit` |
| Constraint | `mim:constraint` | 0..* | `mim:Constraint` |
| Minimumwaarde inclusief | `mim:minimumwaardeInclusief` | 0..1 | integer, decimal, float, real, dateTime, date |
| Minimumwaarde exclusief | `mim:minimumwaardeExclusief` | 0..1 | integer, decimal, float, real, dateTime, date |
| Maximumwaarde inclusief | `mim:maximumwaardeInclusief` | 0..1 | integer, decimal, float, real, dateTime, date |
| Maximumwaarde exclusief | `mim:maximumwaardeExclusief` | 0..1 | integer, decimal, float, real, dateTime, date |

##### §4.3.3.3 mim:Codelijst

Voor codelijst worden de volgende aspecten gespecificeerd:

| **Aspect** | **Eigenschap** | **Kardinaliteit** | **Datatype of klasse** |
|---|---|---|---|
| Identificatie | `mim:identificatie` | 1 | `xsd:anyURI` |
| Naam | `mim:naam` | 1 | tekst |
| Alias | `mim:alias` | 0..1 | tekst |
| Begrip | `mim:begrip` | 0..* | `skos:Concept` |
| Begripsterm | `mim:begripsterm` | 0..* | tekst |
| Herkomst | `mim:herkomst` | 1 | tekst |
| Definitie | `mim:definitie` | 1 | tekst |
| Datum opname | `mim:datumOpname` | 1 | datum |
| Toelichting | `mim:toelichting` | 0..1 | tekst |
| Locatie | `mim:locatie` | 1 | tekst |
| Constraint | `mim:constraint` | 0..* | `mim:Constraint` |

#### §4.3.4 Datatypen in LD

Het betreft metagegevens voor in het informatiemodel gedefinieerde datatypen, oftewel exclusief datatypen die al buiten het model bestaan, zoals Integer, DateTime, Surface.

##### §4.3.4.1 mim:PrimitiefDatatype

De datatypen worden naar de volgende aspecten gespecificeerd:

| **Aspect** | **Eigenschap** | **Kardinaliteit** | **Datatype of klasse** |
|---|---|---|---|
| Identificatie | `mim:identificatie` | 1 | `xsd:anyURI` |
| Naam | `mim:naam` | 1 | tekst |
| Alias | `mim:alias` | 0..1 | tekst |
| Begrip | `mim:begrip` | 0..* | `skos:Concept` |
| Begripsterm | `mim:begripsterm` | 0..* | tekst |
| Definitie | `mim:definitie` | 1 | tekst |
| Toelichting | `mim:toelichting` | 0..1 | tekst |
| Type | `mim:type` | 1 | `mim:Datatype` |
| Lengte | `mim:lengte` | 0..1 | tekst |
| Patroon | `mim:patroon` | 0..1 | tekst |
| Formeel patroon | `mim:formeelPatroon` | 0..1 | tekst |
| Herkomst | `mim:herkomst` | 1 | tekst |
| Datum opname | `mim:datumOpname` | 1 | datum |
| Constraint | `mim:constraint` | 0..* | `mim:Constraint` |

##### §4.3.4.2 mim:GestructureerdDatatype

Voor Gestructureerde datatypen worden de volgende aspecten gespecificeerd:

| **Aspect** | **Eigenschap** | **Kardinaliteit** | **Datatype of klasse** |
|---|---|---|---|
| Identificatie | `mim:identificatie` | 1 | `xsd:anyURI` |
| Naam | `mim:naam` | 1 | tekst |
| Alias | `mim:alias` | 0..1 | tekst |
| Begrip | `mim:begrip` | 0..* | `skos:Concept` |
| Begripsterm | `mim:begripsterm` | 0..* | tekst |
| Herkomst | `mim:herkomst` | 1 | tekst |
| Definitie | `mim:definitie` | 1 | tekst |
| Toelichting | `mim:toelichting` | 0..1 | tekst |
| Patroon | `mim:patroon` | 0..1 | tekst |
| Formeel patroon | `mim:formeelPatroon` | 0..1 | tekst |
| Datum opname | `mim:datumOpname` | 1 | datum |
| Data-element | `mim:dataElement` | 0..* | `mim:DataElement` |
| Constraint | `mim:constraint` | 0..* | `mim:Constraint` |

##### §4.3.4.3 mim:DataElement

De data-elementen worden naar de volgende aspecten gespecificeerd:

| **Aspect** | **Eigenschap** | **Kardinaliteit** | **Datatype of klasse** |
|---|---|---|---|
| Identificatie | `mim:identificatie` | 1 | `xsd:anyURI` |
| Naam | `mim:naam` | 1 | tekst |
| Alias | `mim:alias` | 0..1 | tekst |
| Begrip | `mim:begrip` | 0..* | `skos:Concept` |
| Begripsterm | `mim:begripsterm` | 0..* | tekst |
| Definitie | `mim:definitie` | 1 | tekst |
| Toelichting | `mim:toelichting` | 0..1 | tekst |
| Datum opname | `mim:datumOpname` | 1 | datum |
| Type | `mim:type` | 1 | `mim:Datatype` |
| Lengte | `mim:lengte` | 0..1 | tekst |
| Patroon | `mim:patroon` | 0..1 | tekst |
| Formeel patroon | `mim:formeelPatroon` | 0..1 | tekst |
| Kardinaliteit | `mim:kardinaliteit` | 1 | tekst |
| Constraint | `mim:constraint` | 0..* | `mim:Constraint` |
| Minimumwaarde inclusief | `mim:minimumwaardeInclusief` | 0..1 | integer, decimal, float, real, dateTime, date |
| Minimumwaarde exclusief | `mim:minimumwaardeExclusief` | 0..1 | integer, decimal, float, real, dateTime, date |
| Maximumwaarde inclusief | `mim:maximumwaardeInclusief` | 0..1 | integer, decimal, float, real, dateTime, date |
| Maximumwaarde exclusief | `mim:maximumwaardeExclusief` | 0..1 | integer, decimal, float, real, dateTime, date |

#### §4.3.5 Packages in LD

##### §4.3.5.1 mim:Informatiemodel

Informatiemodel packages worden naar de volgende aspecten gespecificeerd:

| **Aspect** | **Eigenschap** | **Kardinaliteit** | **Datatype of klasse** |
|---|---|---|---|
| Identificatie | `mim:identificatie` | 1 | `xsd:anyURI` |
| Naam | `mim:naam` | 1 | tekst |
| Alias | `mim:alias` | 0..1 | tekst |
| Definitie | `mim:definitie` | 1 | tekst |
| Herkomst | `mim:herkomst` | 1 | tekst |
| Datum opname | `mim:datumOpname` | 1 | datum |
| MIM versie | `mim:mimversie` | 1 | tekst |
| MIM extensie | `mim:mimextensie` | 0..1 | tekst |
| MIM taal | `mim:mimtaal` | 0..1 | tekst |
| Informatiedomein | `mim:informatiedomein` | 1..1 | tekst |
| Informatiemodeltype | `mim:informatiemodeltype` | 1..1 | Informatiemodeltypen |
| Relatiemodelleringstype | `mim:relatiemodelleringstype` | 1..1 | Relatiemodelleringstypen |
| tekstopmaak | `mim:tekstopmaak` | 0..1 | tekst |
| Constraint | `mim:constraint` | 0..* | `mim:Constraint` |
| Basis-URI | `mim:basisUri` | 0..1 | `xsd:anyURI` |

Het veld `mim:informatiemodeltype` verwijst naar één van de volgende mogelijke waarden:

| **Informatiemodeltype** | **Definitie** |
|---|---|
| `mim:ConceptueelInformatiemodel` | Niveau-2 model, conform deze sectie |
| `mim:LogischInformatiemodel` | Niveau-3 model, conform deze sectie |
| `mim:TechnischInformatiemodel` | Niveau-4 model, conform deze sectie |

Het veld `mim:relatiemodelleringstype` verwijst naar één van de volgende mogelijke waarden:

| **Relatiemodelleringstype** | **Definitie** |
|---|---|
| `mim:RelatiesoortLeidend` | Relatiesoort leidend, conform deze en deze secties |
| `mim:RelatierolLeidend` | Relatierol leidend, conform deze en deze secties |

##### §4.3.5.2 mim:Domein

Domein packages worden naar de volgende aspecten gespecificeerd:

| **Aspect** | **Eigenschap** | **Kardinaliteit** | **Datatype of klasse** |
|---|---|---|---|
| Identificatie | `mim:identificatie` | 1 | `xsd:anyURI` |
| Naam | `mim:naam` | 1 | tekst |
| Alias | `mim:alias` | 0..1 | tekst |
| Datum opname | `mim:datumOpname` | 1 | datum |
| Constraint | `mim:constraint` | 0..* | `mim:Constraint` |
| Basis-URI | `mim:basisUri` | 0..1 | `xsd:anyURI` |

##### §4.3.5.3 mim:Extern

Externe packages worden naar de volgende aspecten gespecificeerd:

| **Aspect** | **Eigenschap** | **Kardinaliteit** | **Datatype of klasse** |
|---|---|---|---|
| Identificatie | `mim:identificatie` | 1 | `xsd:anyURI` |
| Naam | `mim:naam` | 1 | tekst |
| Alias | `mim:alias` | 0..1 | tekst |
| Locatie | `mim:locatie` | 1 | tekst |
| Definitie | `mim:definitie` | 1 | tekst |
| Toelichting | `mim:toelichting` | 0..1 | tekst |
| Herkomst | `mim:herkomst` | 1 | tekst |
| Datum opname | `mim:datumOpname` | 1 | datum |
| Constraint | `mim:constraint` | 0..* | `mim:Constraint` |
| Basis-URI | `mim:basisUri` | 0..1 | `xsd:anyURI` |

##### §4.3.5.4 mim:View

View packages worden naar de volgende aspecten gespecificeerd:

| **Aspect** | **Eigenschap** | **Kardinaliteit** | **Datatype of klasse** |
|---|---|---|---|
| Identificatie | `mim:identificatie` | 1 | `xsd:anyURI` |
| Naam | `mim:naam` | 1 | tekst |
| Alias | `mim:alias` | 0..1 | tekst |
| Locatie | `mim:locatie` | 1 | tekst |
| Definitie | `mim:definitie` | 1 | tekst |
| Toelichting | `mim:toelichting` | 0..1 | tekst |
| Herkomst | `mim:herkomst` | 1 | tekst |
| Datum opname | `mim:datumOpname` | 1 | datum |
| Constraint | `mim:constraint` | 0..* | `mim:Constraint` |
| Basis-URI | `mim:basisUri` | 0..1 | `xsd:anyURI` |

#### §4.3.6 Overige modelelementen in LD

##### §4.3.6.1 mim:Enumeratie

Enumeraties betreffen de metaclass Enumeration en worden naar de volgende aspecten gespecificeerd:

| **Aspect** | **Eigenschap** | **Kardinaliteit** | **Datatype of klasse** |
|---|---|---|---|
| Identificatie | `mim:identificatie` | 1 | `xsd:anyURI` |
| Naam | `mim:naam` | 1 | tekst |
| Alias | `mim:alias` | 0..1 | tekst |
| Begrip | `mim:begrip` | 0..* | `skos:Concept` |
| Begripsterm | `mim:begripsterm` | 0..* | tekst |
| Definitie | `mim:definitie` | 1 | tekst |
| Toelichting | `mim:toelichting` | 0..1 | tekst |
| Datum opname | `mim:datumOpname` | 1 | datum |
| Waarde | `mim:waarde` | 1..* | `mim:Waarde` |
| Constraint | `mim:constraint` | 0..* | `mim:Constraint` |

##### §4.3.6.2 mim:Enumeratiewaarde

De enumeratiewaarde zelf betreft de metaclass UML-EnumerationLiteral en kent volgende aspecten:

| **Aspect** | **Eigenschap** | **Kardinaliteit** | **Datatype of klasse** |
|---|---|---|---|
| Identificatie | `mim:identificatie` | 1 | `xsd:anyURI` |
| Naam | `mim:naam` | 1 | tekst |
| Definitie | `mim:definitie` | 0..1 | tekst |
| Toelichting | `mim:toelichting` | 0..1 | tekst |
| Code | `mim:code` | 0..1 | tekst |
| Begrip | `mim:begrip` | 0..* | `skos:Concept` |
| Begripsterm | `mim:begripsterm` | 0..* | tekst |
| Datum opname | `mim:datumOpname` | 1 | datum |
| Constraint | `mim:constraint` | 0..* | `mim:Constraint` |

Een enumeratiewaarde mag geen alias hebben, omdat in UML het alias-veld wordt gebruikt voor de mim:code. Mocht toch een `mim:alias` zijn opgegeven voor een enumeratiewaarde, dan dient deze gelezen te worden als een `mim:code`. In het RDF model is `mim:code` een subproperty van een `mim:alias`.

##### §4.3.6.3 mim:Constraint

De enumeratiewaarde zelf betreft de metaclass UML-EnumerationLiteral en kent volgende aspecten:

| **Aspect** | **Eigenschap** | **Kardinaliteit** | **Datatype of _klasse** |
|---|---|---|---|
| Naam | `mim:naam` | 1 | tekst |
| Specificatie-tekst | `mim:specificatieTekst` | 0..1 | tekst |
| Specificatie-formeel | `mim:specificatieFormeel` | 0..1 | tekst |

### §4.4 Linked Data Tooling

Het metamodel van MIM is specifiek voor het MIM opgesteld. Hiervoor zijn niet direct tools beschikbaar. Wel zijn er twee alternatieve opties die modelleurs kunnen volgen:

1. Modelleurs kunnen een MIM model met behulp van Enterprise Architect opstellen. Er is een tool Imvertor, waarmee het mogelijk is om een MIM Model opgesteld in Enterprise Architect te transformeren naar een Linked Data model. Deze tool is open source.
2. Modelleurs kunnen ook direct in een Linked Data model (in OWL en SHACL) opstellen. Een dergelijk model kan, indien het voldoet aan de transformatieregels, gezien worden als een MIM informatiemodel. Om expliciet de link naar het MIM duidelijk te maken, kan gebruik worden gemaakt van deze SPARQL constructieregels, die een RDF/RDFS/OWL/SHACL model "terugvertalen" naar een MIM model. De terugvertaalregels zijn beschreven in 6.4.10 Transformatie vanuit RDFS/OWL/SHACL. Er zijn diverse tools beschikbaar om een dergelijk model op te stellen. De meest bekende tools zijn Protege (open source)en Poolparty (commercieel product). Daarnaast zijn er ook veel modelleurs die gebruik maken van generieke IDE's voor het maken van Linked Data modellen, vaak op basis van de voor mensen leesbare Turtle syntax.
