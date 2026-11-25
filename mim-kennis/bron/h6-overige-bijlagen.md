<!--
Bron: MIM - Metamodel Informatie Modellering, versie 1.2, vastgestelde versie 13 juni 2024 (Geonovum).
https://docs.geostandaarden.nl/mim/def-st-mim-20240613/
Licentie: CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/).
Bewerking: automatisch omgezet van HTML naar markdown door de kennisbank mim-kennis (build/extract_def.py).
Figuren zijn niet overgenomen; alleen hun bijschrift staat er. De tekst is verder ongewijzigd.
-->

# Hoofdstuk 6 (zonder 6.4) en hoofdstuk 7

Letterlijke tekst van MIM 1.2 (DEF, 13 juni 2024). Elke kop begint met het paragraafnummer uit de vastgestelde versie.

## §6 Bijlagen

### §6.1 Diagrammen

#### §6.1.1 Overzicht toegepaste UML metaclasses

[Figuur: Figuur 38 Diagram: toegepaste UML metaclasses] (media/OverzichtToegepasteUMLmetaclasses.png)

#### §6.1.2 Modelelementen en metagegevens als diagram

Deze bijlage bevat alle modelelementen en metagegevens in één diagram.

_Kern - Relatiesoort is leidend_

[Figuur: Figuur 39 Diagram: Kern met metagegevens - relatiesoort leidend (alt 1)] (media/KernMetMetagegevens_Alt1.png)

_Kern - Relatierol is leidend_

[Figuur: Figuur 40 Diagram: Kern met metagegevens - relatierol leidend (alt 2)] (media/KernMetMetagegevens_Alt2.png)

_Datatypen_

[Figuur: Figuur 41 Diagram: Datatypen met metagegevens] (media/DatatypenMetMetagegevens.png)

_Constraints_

[Figuur: Figuur 42 Diagram: Constraints met metagegevens] (media/ConstraintsMetMetagegevens.png)

_Keuze_

_Keuze tussen datatypen_

Dit UML is uitgewerkt voor Objecttype. Voor Gegevensgroeptype en Relatieklasse geldt hetzelfde patroon.

[Figuur: Figuur 43 Diagram: Keuze tussen datatypen met metagegevens] (media/KeuzeDatatype1metMeta.png)

_Keuze tussen attribuutsoorten_

Dit UML is uitgewerkt voor Objecttype. Voor Gegevensgroeptype en Relatieklasse geldt hetzelfde patroon.

[Figuur: Figuur 44 Diagram: Keuze tussen attribuutsoorten met metagegevens] (media/KeuzeAttribuutsoort2metMetaUML.png)

_Keuze tussen attribuutsoorten binnen de context van een attribuutsoort_

Dit UML is uitgewerkt voor Objecttype. Voor Gegevensgroeptype en Relatieklasse geldt hetzelfde patroon.

[Figuur: Figuur 45 Diagram: Keuze tussen attribuutsoorten binnen de context van een attribuutsoort met metagegevens] (media/KeuzeAttribuutsoort3metMetaUML.png)

_Keuze tussen relatiedoelen, als nadere invulling van 1 betekenisvolle relatiesoort_

Dit UML is uitgewerkt voor Objecttype. Voor Gegevensgroeptype geldt hetzelfde patroon, behalve dat een Gegevensgroeptype geen doel mag zijn voor een Relatiesoort.

[Figuur: Figuur 46 Diagram: Keuze tussen relatiedoelen met metagegevens] (media/KeuzeRelatiedoel4metMetaUML.png)

_Keuze tussen relatiesoorten/relatierollen (elk afzonderlijk betekenisvol)_

Dit UML is uitgewerkt voor Objecttype. Voor Gegevensgroeptype geldt hetzelfde patroon, behalve dat een Gegevensgroeptype geen doel mag zijn voor een Relatiesoort.

[Figuur: Figuur 47 Diagram: Keuze tussen relatiesoorten/relatierollen met metagegevens] (media/KeuzeRelatiedoel5MetaUML.png)

_Packages_

[Figuur: Figuur 48 Diagram: Packages met metagegevens] (media/PackagesMetMetagegevens.png)

### §6.2 Template Naamgevingsconventies

| **Modelelement** | **Naamgevingsconventie** | **Voorbeeld** |
|---|---|---|
| «Objecttype» | ... | ... |
| «Attribuutsoort» | ... | ... |
| «Gegevensgroep» | ... | ... |
| «Gegevensgroeptype» | ... | ... |
| «Relatiesoort» | ... | ... |
| «Relatieklasse» | ... | ... |
| «Externe Koppeling» | ... | ... |
| «Relatierol» | ... | ... |
| «Referentielijst» | ... | ... |
| «Referentie-element» | ... | ... |
| «Enumeratie» | ... | ... |
| «Enumeratiewaarde» | ... | ... |
| «Codelijst» | ... | ... |
| «Gestructureerd datatype» | ... | ... |
| «Data-element» | ... | ... |
| «Informatiemodel» | ... | ... |
| «Domein» | ... | ... |
| «Extern» | ... | ... |
| «View» | ... | ... |
| «Keuze» | ... | ... |

> **Voorbeeld:**
> Het invullen van de tabel, kan er bijvoorbeeld als volgt uitzien:
>
> | Modelelement | Naamgevingsconventie | Voorbeeld |
> |---|---|---|
> | «Objecttype» | UpperCamelCase | `BestuurlijkGebied` |
> | «Attribuutsoort» | lowerCamelCase | `geometrieReferentiepunt` |
> | etc. | etc. | etc. |

### §6.3 Vertaling naar engels

MIM is een specificatie die is ontstaan vanuit de behoeften van enkele basisregistraties en afnemers daarvan. Daarbij is de aansluiting bij internationale (geo)normen gewaarborgd. Echter de precieze aansluiting bij die normen is niet altijd expliciet gemaakt in MIM. Met name de relatie met de modelleertechnieken van de ISO 19100 serie is van belang. Deze ISO standaarden vormen de ondergrond voor o.a. Inspire en NEN 3610.

In het volgende overzicht geldt het volgende

Kolom Aard waarden:

- ST = Stereotype
- TV = Tagged value naam
- VAL = Tagged value waarde

Kolom MIM benaming ISO waarden:

- Als _schuin gedrukt_, dan is de naam overgenomen voor dezelfde constructie uit het General Feature Model [ISO 19109].

Kolom Reden waarden:

- Vertaling = Hetzelfde ding, vertaald in het Engels. De aansluiting bij ISO 19100 serie wordt daarbij expliciet gezocht.
- Precisering = De naam maakt de aard van het stereotype preciezer.

| **Aard** | **MIM 1.1** | **MIM benaming ISO** | **Reden** |
|---|---|---|---|
| ST | Objecttype | _FeatureType_ (ISO 19109) GF_FeatureType | Vertaling |
| ST | Attribuutsoort | _AttributeType_ (ISO 19109) GF_AttributeType | Vertaling |
| ST | Gegevensgroeptype | AttributeGroupType | Vertaling en precisering |
| ST | Gegevensgroep | AttributeGroup | Vertaling en precisering |
| ST | Relatiesoort | _AssociationType_ (ISO 19109) GF_AssociationType | Vertaling |
| ST | Relatieklasse | AssociationClass | Vertaling |
| ST | Externe koppeling | ExternalLink | Vertaling |
| ST | Relatierol | _AssociationRole_ (ISO 19109) GF_AssociationRole | Vertaling |
| ST | Referentielijst | ReferenceList | Vertaling |
| ST | Referentie element | ReferenceElement | Vertaling |
| ST | Enumeratie | Enumeration | Vertaling |
| ST | Enumeratiewaarde | Enum | Vertaling |
| ST | CodeLijst | _CodeList_ (ISO 19103) | - |
| ST | Datatype | SimpleType | Vertaling en precisering |
| ST | Complex datatype | ComplexType | Vertaling |
| ST | Data element | DataElement | Vertaling |
| ST | Keuze | Union Defines a union data type. | - |
| ST | Keuze element | UnionElement | Vertaling |
| ST | Extern | External | Vertaling |
| ST | View | View | Vertaling |
| TV | Beheerder | Administrator | Vertaling |
| TV | Data locatie | Data location | Vertaling |
| TV | Datum opname | Date recorded | Vertaling |
| TV | Eigenaar | Owned by | Vertaling |
| TV | Formeel patroon | Formal pattern | Vertaling |
| TV | Herkomst | Source | Vertaling |
| TV | Herkomst definitie | Origin of definition | Vertaling |
| TV | Indicatie authentiek | Indication authentic | Vertaling |
| TV | Indicatie formele historie | Indication formal history | Vertaling |
| TV | Indicatie materiële historie | Indication material history | Vertaling |
| TV | Kwaliteit | Quality | Vertaling |
| TV | Lengte | Length | Vertaling |
| TV | Locatie | Location | Vertaling |
| TV | Mogelijk geen waarde | Voidable | Vertaling |
| TV | Patroon | Pattern | Vertaling |
| TV | Populatie | Population | Vertaling |
| TV | Regels | Rules | Vertaling |
| TV | Toelichting | Description | Vertaling |
| VAL | Ja | Yes | Vertaling |
| VAL | Nee | No | Vertaling |
| VAL | Zie groep | See group | Vertaling |
| VAL | Authentiek | Authentic | Vertaling |
| VAL | Basisgegeven | Base data | Vertaling |
| VAL | Landelijk kerngegeven | National base data | Vertaling |
| VAL | Gemeentelijk kerngegeven | Municipal base data | Vertaling |
| VAL | Overig | Other | Vertaling |

### §6.5 Versielog

De onderstaande tabel geeft een overzicht van de wijzigingen die in MIM 1.2 zijn verwerkt met een verwijzging naar het bijbehorende issue op GitHub.

| Issue | Samenvatting |
|---|---|
| 015 | Toevoegen metagegeven `Eenheid` aan documentatie. |
| 109 | Toevoegen metagegevens `min-max inclusief` en `min-max exclusief`. |
| 111 | Aanpassen samenhang `«Relatiesoort»`, `«Objecttype»` en `«Relatierol»` in het diagram. |
| 148 | Toevoegen beschrijving wanneer `Relatieklasse` modelleren als `Objecttype`. |
| 151 | Toevoegen metagegevens `heeft tijdlijn geldigheid` en `heeft tijdlijn registratie`. |
| 156 | Afstemmen metaclasses tabellen en diagrammen. |
| 171 | Aanpassen structuur tekst en figuren m.b.t. `Keuze`. |
| 188 | Toevoegen van `URI` van model en modelelementen voor publicatie op het web. |
| 190 | Toevoegen Keuze tussen realtiesoorten (use case 5). |
| 195 | Toevoegen metagegeven `«Mixin»` voor `«Generalisatie»` bij _multiple inheritance_. |
| 201 | Aanpassen beschrijving `Populatie` en `Kwaliteit`, toevoegen voorbeelden. |
| 224 | Verwijderen metagegevens `formele historie` en `materiële historie` bij `Gegevensgroep`. |
| 238 | Opnemen toelichting hoe omgaan met een gegeven dat uit meerdere 'data-delen' bestaat. |
| 245 | Beschrijven dat `Definitie` en `Toelichting` rijke tekst mogen bevatten. |
| 253 | Aanpassen definitie en toelichtring `«Codelijst»`. |
| 283 | Toelichten betekenis `heeft Datatype`. |
| 285 | Aanpassen verkorte naam `heeft enumeratiewaarde`. |
| 286 | Consistente naamgeving `keuzeattribuut` en `keuzerelatiedoel`. |
| 288 | Aanpassen transformatie `Indicatie abstract object`. |
| 289 | Betekenis `mim:locatie` niet consistent doorgevoerd. |
| 305 | Toevoegen binding `heeft gegevensgroep` aan tabel metagegevens `«Relatieklasse»` |
| 310 | Samenvoegen paragrafen met waardelijsten. |
| 314 | Consistente schrijfwijze meervoud _datatype_ (uitgang `-n`: _datatypen_). |
| 317 | Toevoegen `«Constraint»` toestaan op alle modelelementen. |
| 318 | Alle figuren voorzien van `<figure>` tags en bijschriften. Nu vindbaar in ToF. |
| 321 | Verbeteren structuur document: tussenkoppen met tag, voor zichbaarheid in de index. |
| 322 | Alle definities voorzien van `<dfn>` tag en zichtbaar format. |
| 333 | Consistente schrijfwijze `Waardelijst` (zonder `-n`: _waarde_, i.p.v. _waarden_). |
| 336 | Aanpassen naamgeving en verwijzing van `Alias` in tabel specificatie metagegevens in LD. |
| 352 | Herstellen _broken links_ en toepassen _inner-document expansion references_. |
| 370 | Aanpassen figuur: Keuze tussen attribuutsoorten binnen een `«Attribuutsoort»`. |
| 377 | Aanpassen toelichting `Indidcatie abstract object`. |
| 378 | Corrigeren toepassing `Indicatie abstract object`. |
| 387 | Aanpassing toelichting `Identificatie` modelelement. |
| 391 | Consistente schrijfwijze waardes van metagegevens. |
| 425 | Aanpassen definitie `Modelelement`. |
| 427 | Aanpassen definitie `Object`. |
| 428 | Aanpassen definitie `Gegeven`. |
| 431 | Toevoegen eenduidige beschrijving van packagetypen. |
| 445 | Aanpassen metagegeven `Datatype`. |
| 446 | Aanpassen tekst metagegeven `Profielspecificatie`. |
| 450 | Toevoegen metagegeven `bevat modelelement`. |
| 451 | MIM namespace overal doorgevoerd http://modellen.mim-standaard.nl/def/mim. |

## §7 Conformiteit

Naast onderdelen die als niet normatief gemarkeerd zijn, zijn ook alle diagrammen, voorbeelden, en noten in dit document niet normatief. Verder is alles in dit document normatief.
