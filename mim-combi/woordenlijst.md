---
id: woordenlijst
titel: Woordenlijst
bron: ["6.3"]
mim-versie: "1.2"
status: toelichtend
---

# Woordenlijst

Gegenereerd uit `data/woordenlijst.json` door `beheer/bouw/maak_woordenlijst.py`. Niet met de hand wijzigen.

Gebruik: zoek de term, een synoniem of de Engelse term op en open het genoemde bestand. Met Python: `python3 scripts/mim.py zoek <term>`.

Engelse termen staan alleen in deze lijst. Ze komen uit MIM 1.2 §6.3. Die tabel gebruikt nog de namen uit MIM 1.1 (zie bekende-onduidelijkheden.md).

## Modelelementen

| Term | Ook genoemd | Engels | MIM 1.2 | Bestand |
|---|---|---|---|---|
| Attribuutsoort | attribuut, kenmerk, eigenschap | AttributeType, GF_AttributeType | §2.3.2.2, §3.2.1.2, §4.3.1.2 | `modelelementen/attribuutsoort.md` |
| Codelijst | codeList, CodeList | CodeList | §2.3.4.5, §3.2.3.1, §4.3.3.3 | `modelelementen/codelijst.md` |
| Constraint |  |  | §2.3.7.1, §3.1.3.1, §4.3.6.3 | `modelelementen/constraint.md` |
| Data-element | data element | DataElement | §2.3.5.4, §3.2.4.3, §4.3.4.3 | `modelelementen/data-element.md` |
| Datatype |  |  | §2.3.5.1, §4.2.2 | `modelelementen/datatype.md` — Abstract; in UML geen eigen stereotype. In §6.3 (MIM 1.1-namen) staat 'Datatype' → SimpleType. |
| Domein |  |  | §2.3.6.2, §3.2.5.1, §4.3.5.2 | `modelelementen/domein.md` |
| Enumeratie |  | Enumeration | §2.3.4.3, §3.2.3.2, §4.3.6.1 | `modelelementen/enumeratie.md` — In UML zonder stereotype: een UML-Enumeration (§3.1.2). |
| Enumeratiewaarde |  | Enum | §2.3.4.4, §3.2.3.3, §4.3.6.2 | `modelelementen/enumeratiewaarde.md` |
| Extern |  | External | §2.3.6.3, §3.2.5.2, §4.3.5.3 | `modelelementen/extern.md` |
| Externe koppeling |  | ExternalLink | §2.3.3.4, §3.1.3.4, §4.3.2.8 | `modelelementen/externe-koppeling.md` |
| Gegevensgroep |  | AttributeGroup | §2.3.2.3, §3.2.1.3, §4.3.1.3 | `modelelementen/gegevensgroep.md` |
| Gegevensgroeptype |  | AttributeGroupType | §2.3.2.4, §3.2.1.4, §4.3.1.4 | `modelelementen/gegevensgroeptype.md` |
| Generalisatie | overerving, specialisatie, supertype, subtype |  | §2.3.3.1, §3.2.2.5, §4.3.2.6 | `modelelementen/generalisatie.md` |
| Gestructureerd datatype | complex datatype, Gestructuurd datatype | ComplexType | §2.3.5.3, §3.1.2, §4.3.4.2 | `modelelementen/gestructureerd-datatype.md` — Heette in MIM 1.1 'Complex datatype' (§6.3). Stereotype en LD-klasse worden in de bron ook 'Gestructuurd' gespeld (I4). |
| Informatiemodel |  |  | §2.3.6.1, §3.2.5.3, §4.3.5.1 | `modelelementen/informatiemodel.md` |
| Keuze |  | Union | §2.3.7.2, §3.1.3.2, §4.2.3.2 | `modelelementen/keuze.md` — De keuzemogelijkheden heten sinds MIM 1.1 geen 'keuze-elementen' meer (§3.2.4.4). |
| Modelelement |  |  | §2.2.1 | `modelelementen/modelelement.md` |
| Objecttype |  | FeatureType, GF_FeatureType | §2.3.2.1, §3.2.1.1, §4.3.1.1 | `modelelementen/objecttype.md` |
| Package |  |  | §2.3.6, §4.2.3.5 | `modelelementen/package.md` |
| Primitief datatype | simpel datatype |  | §2.3.5.2, §3.2.4.1, §4.3.4.1 | `modelelementen/primitief-datatype.md` |
| Referentie-element |  | ReferenceElement | §2.3.4.2, §3.2.3.5, §4.3.3.2 | `modelelementen/referentie-element.md` |
| Referentielijst |  | ReferenceList | §2.3.4.1, §3.2.3.4, §4.3.3.1 | `modelelementen/referentielijst.md` |
| Relatieklasse |  | AssociationClass | §2.3.3.3, §3.2.2.7, §4.3.2.7 | `modelelementen/relatieklasse.md` |
| Relatierol | relatierol bron, relatierol doel, rol | AssociationRole, GF_AssociationRole | §2.3.3.5, §3.1.3.3, §4.3.2.4 | `modelelementen/relatierol.md` |
| Relatierol bron | bronrol, source |  | §2.3.3.5, §4.2.3.3 | `modelelementen/relatierol.md` |
| Relatierol doel | doelrol, target, relatiedoel |  | §2.3.3.5, §4.2.3.3 | `modelelementen/relatierol.md` — 'Relatiedoel' wordt in de Keuze-teksten gebruikt voor het doel van een relatie (§2.3.7.2). |
| Relatiesoort | relatie, associatie | AssociationType, GF_AssociationType | §2.3.3.2, §3.2.2, §4.3.2.2 | `modelelementen/relatiesoort.md` |
| View |  | View | §2.3.6.4, §3.2.5.4, §4.3.5.4 | `modelelementen/view.md` |

## Metagegevens

| Term | Ook genoemd | Engels | MIM 1.2 | Bestand |
|---|---|---|---|---|
| Aggregatietype |  |  | §2.4.3.23 | `metagegevens.md` — Hoort bij relaties, niet bij een attribuutsoort; onduidelijkheid I3. |
| Alias |  |  | §2.4.3.2 | `metagegevens.md` |
| Authentiek | Indicatie authentiek | Indication authentic | §2.4.3.16 | `metagegevens.md` — Waardebereik: zie data/waardebereik.json; onduidelijkheid I2. |
| Basis-URI |  |  | §2.4.2.1 | `metagegevens.md` |
| Begrip |  |  | §2.4.3.3 | `metagegevens.md` |
| Begripsterm |  |  | - | `metagegevens.md` — Staat alleen in de LD-tabellen (§4.3) en de transformatie (§6.4.9.5), niet in §2.4. |
| bevat enumeratiewaarde | waarde, heeft enumeratiewaarde |  | §2.4.4.10 | `metagegevens.md` |
| bevat modelelement |  |  | §2.4.4.9 | `metagegevens.md` |
| bevat referentie-element |  |  | §2.4.4.11 | `metagegevens.md` |
| Bron |  |  | §2.4.3.20 | `metagegevens.md` |
| Code |  |  | §2.4.3.32 | `metagegevens.md` |
| Datum opname |  | Date recorded | §2.4.3.8 | `metagegevens.md` |
| Definitie |  |  | §2.4.3.5 | `metagegevens.md` |
| Doel |  |  | §2.4.3.21 | `metagegevens.md` |
| Doelformaat |  |  | §2.4.3.25 | `metagegevens.md` |
| Eenheid |  |  | §2.4.3.36 | `metagegevens.md` |
| Formeel patroon |  | Formal pattern | §2.4.3.31 | `metagegevens.md` |
| heeft attribuut | attribuut |  | §2.4.4.1 | `metagegevens.md` |
| heeft attribuutkeuze |  |  | §2.4.4.13 | `metagegevens.md` |
| heeft constraint |  |  | §2.4.4.17 | `metagegevens.md` |
| heeft data-element |  |  | §2.4.4.8 | `metagegevens.md` |
| heeft datatypekeuze |  |  | §2.4.4.12 | `metagegevens.md` |
| heeft externe koppeling |  |  | §2.4.4.7 | `metagegevens.md` |
| heeft gegevensgroep |  |  | §2.4.4.2 | `metagegevens.md` |
| heeft gegevensgroeptype |  |  | §2.4.4.3 | `metagegevens.md` |
| heeft keuzeattribuut |  |  | §2.4.4.14 | `metagegevens.md` |
| heeft keuzerelatiedoel |  |  | - | `metagegevens.md` |
| heeft relatiedoelkeuze |  |  | §2.4.4.15 | `metagegevens.md` |
| heeft relatiesoort |  |  | §2.4.4.6 | `metagegevens.md` |
| heeft relatiesoortkeuze |  |  | §2.4.4.16 | `metagegevens.md` |
| heeft tijdlijn geldigheid | materiële historie, tijdlijn geldigheid, geldigheid |  | §2.4.3.10 | `metagegevens.md` |
| heeft tijdlijn registratie | formele historie, tijdlijn registratie, registratietijdlijn |  | §2.4.3.12 | `metagegevens.md` |
| Herkomst |  | Source | §2.4.3.4 | `metagegevens.md` |
| Herkomst definitie |  | Origin of definition | §2.4.3.6 | `metagegevens.md` |
| Identificatie |  |  | §2.4.2.2 | `metagegevens.md` |
| Identificerend | isId, «id», «isId» |  | §2.4.3.9 | `metagegevens.md` |
| Indicatie abstract object | abstract, indAbstract, isAbstract |  | §2.4.3.33 | `metagegevens.md` |
| Indicatie afleidbaar | afleidbaar, afgeleid gegeven, isDerived |  | §2.4.3.17 | `metagegevens.md` |
| Indicatie classificerend |  |  | §2.4.3.18 | `metagegevens.md` |
| Indicatie formele historie |  | Indication formal history | §2.4.3.13 | `metagegevens.md` — Gelijkwaardig aan 'heeft tijdlijn registratie'; vervalt in MIM 2.x (noot bij §2.4.3.13). |
| Indicatie materiële historie |  | Indication material history | §2.4.3.11 | `metagegevens.md` — Gelijkwaardig aan 'heeft tijdlijn geldigheid'; vervalt in MIM 2.x (noot bij §2.4.3.11). |
| Informatiedomein |  |  | §2.4.1.1 | `metagegevens.md` |
| Informatiemodeltype |  |  | §2.4.1.2 | `metagegevens.md` |
| Kardinaliteit | multipliciteit, multiplicity |  | §2.4.3.14 | `metagegevens.md` |
| Kardinaliteit relatie bron |  |  | §2.4.3.15 | `metagegevens.md` |
| Kwaliteit |  | Quality | §2.4.3.35 | `metagegevens.md` |
| Lengte |  | Length | §2.4.3.29 | `metagegevens.md` |
| Locatie |  | Location | §2.4.3.24 | `metagegevens.md` |
| Maximumwaarde exclusief |  |  | §2.4.3.40 | `metagegevens.md` |
| Maximumwaarde inclusief |  |  | §2.4.3.39 | `metagegevens.md` |
| MIM-extensie |  |  | §2.4.1.5 | `metagegevens.md` |
| MIM-taal |  |  | §2.4.1.6 | `metagegevens.md` |
| MIM-versie |  |  | §2.4.1.4 | `metagegevens.md` |
| Minimumwaarde exclusief |  |  | §2.4.3.38 | `metagegevens.md` |
| Minimumwaarde inclusief |  |  | §2.4.3.37 | `metagegevens.md` |
| Mixin |  |  | §2.4.3.41 | `metagegevens.md` |
| Mogelijk geen waarde | onbekende waarde | Voidable | §2.4.3.19 | `metagegevens.md` |
| Naam |  |  | §2.4.3.1 | `metagegevens.md` |
| Patroon |  | Pattern | §2.4.3.30 | `metagegevens.md` |
| Populatie |  | Population | §2.4.3.34 | `metagegevens.md` |
| Profielspecificatie |  |  | §2.4.3.27 | `metagegevens.md` |
| Relatiemodelleringstype |  |  | §2.4.1.3 | `metagegevens.md` |
| Relatierol |  |  | - | `metagegevens.md` |
| Specificatie formeel |  |  | - | `metagegevens.md` |
| Specificatie tekst |  |  | - | `metagegevens.md` |
| Subtype |  |  | - | `metagegevens.md` |
| Tekstopmaak |  |  | §2.4.1.7 | `metagegevens.md` |
| Toelichting |  | Description | §2.4.3.7 | `metagegevens.md` |
| Type (heeft datatype) | Type, heeft datatype, datatype van een attribuutsoort |  | §2.4.3.28, §2.4.4.5 | `metagegevens.md` |
| Unidirectioneel |  |  | §2.4.3.22 | `metagegevens.md` |
| Unieke aanduiding | unieke identificatie |  | - | `metagegevens.md` — Staat in de UML-tabel van Objecttype (§3.2.1.1) en in §6.4.9.24, niet in §2.4. |
| verwijst naar relatiedoel |  |  | - | `metagegevens.md` |
| verwijst naar supertype | supertype |  | §2.4.4.4 | `metagegevens.md` |
| Waarde-item |  |  | §2.4.3.26 | `metagegevens.md` |

## Begrippen en onderwerpen

| Term | Ook genoemd | Engels | MIM 1.2 | Bestand |
|---|---|---|---|---|
| Abstract objecttype | abstract, concreet objecttype, specialisatie |  | §5.5, §2.4.3.33 | `onderwerpen/abstracte-objecttypen.md` |
| Alternatief (relatiemodellering) | relatiesoort leidend, relatierol leidend, alternatief 1, alternatief 2 |  | §1.11, §3.2.2 | `onderwerpen/relatiemodellering.md` |
| Begrip | concept | concept | §1.6.1, §5.16 | `onderwerpen/begrippen-en-definities.md` |
| Beschouwingsniveau | niveau 1, niveau 2, niveau 3, niveau 4 |  | §1.6 | `onderwerpen/beschouwingsniveaus.md` |
| Conceptueel informatiemodel | conceptueel, niveau 2, CIM |  | §1.6.2 | `onderwerpen/beschouwingsniveaus.md` |
| Extensie | MIM-extensie, eigen extensie, uitbreiding |  | §1.10 | `onderwerpen/extensies.md` |
| Fysiek of technisch datamodel | technisch model, fysiek model, niveau 4 |  | §1.6.4 | `onderwerpen/beschouwingsniveaus.md` — Buiten de scope van MIM. |
| Gegeven |  |  | §2.3.1.2 | `onderscheidingen/object-objecttype-gegeven.md` — Geen modelelement (noot bij §2.3.1.2). |
| Historie | tijdlijnen, materiële historie, formele historie |  | §5.8 | `onderwerpen/historie.md` |
| Informatiemodel (begrip) | IM |  | §1.5 | `onderwerpen/beschouwingsniveaus.md` |
| Landelijk datatype | Postcode, DMO, DTMO, Datum mogelijk onvolledig |  | §5.1.3 | `onderwerpen/datatypen.md` |
| Logisch informatiemodel | logisch, gegevensmodel, niveau 3, LIM |  | §1.6.3 | `onderwerpen/beschouwingsniveaus.md` |
| Metamodel | modelleertaal, metataal |  | §1.7 | `onderwerpen/beschouwingsniveaus.md` |
| MIM metaclass | metaclass, metaklasse, MIM-metaclass |  | §2.2, §2.1 | `modelelementen/modelelement.md` |
| Model van begrippen | begrippenmodel, begrippenkader, niveau 1 |  | §1.6.1 | `onderwerpen/beschouwingsniveaus.md` |
| Mogelijk geen waarde (onderwerp) | onbekend, onbekende waarde | Voidable | §2.4.3.19, §5.11 | `onderwerpen/mogelijk-geen-waarde.md` |
| Multiple inheritance | meervoudige overerving | multiple inheritance | §2.3.3.1, §2.4.3.41 | `modelelementen/generalisatie.md` |
| Naamgevingsconventie | naamgeving, CamelCase, UpperCamelCase, lowerCamelCase |  | §5.15, §6.2 | `onderwerpen/naamgeving.md` |
| Normatief | niet-normatief, conformiteit |  | §7 | `SKILL.md` |
| Object | exemplaar, instantie |  | §2.3.1.1 | `onderscheidingen/object-objecttype-gegeven.md` — Geen modelelement (noot bij §2.3.1.1). |
| Primitieve datatypen (lijst) | CharacterString, Integer, Real, Decimal, Boolean, Date, DateTime, Year, Day, Month, URI |  | §5.1.1 | `onderwerpen/datatypen.md` |
| Stelselcatalogus | SCAT, stelselafspraken |  | §5.14 | `onderwerpen/begrippen-en-definities.md` |
| Uniform toepassen | uitbreiden mag, afwijken niet |  | §2.1 | `SKILL.md` |
| Waardelijst | domeinwaarden, codetabel, lijst |  | §2.3.4, §5.4 | `onderwerpen/waardelijsten.md` |
| Zelfgedefinieerd datatype | eigen datatype, AN, NietNegatieveInteger |  | §5.1.2 | `onderwerpen/datatypen.md` |

## Oude of vervallen termen

| Term | Ook genoemd | Engels | MIM 1.2 | Bestand |
|---|---|---|---|---|
| Complex datatype |  | ComplexType | §6.3 | `modelelementen/gestructureerd-datatype.md` — MIM 1.1-naam; in MIM 1.2 heet dit Gestructureerd datatype. |
| Keuze-element | keuze element | UnionElement | §3.2.4.4, §5.3 | `onderwerpen/keuze.md` — Vervallen sinds MIM 1.1 (§3.2.4.4), maar §5.3 gebruikt de term nog; zie bekende-onduidelijkheden.md. |

## UML-termen

| Term | Ook genoemd | Engels | MIM 1.2 | Bestand |
|---|---|---|---|---|
| Stereotype | UML-stereotype | stereotype | §1.8, §3.1 | `uitdrukkingen/uml.md` |
| Tagged value | tagged values | tagged value | §1.8, §2.4.3 | `uitdrukkingen/uml.md` |
| UML-profiel | MIM-profiel, MIM-toolbox, profiel | UML profile | §1.8, §3.3.1 | `uitdrukkingen/uml.md` |
| Vier lagen metamodel architectuur | M0, M1, M2, M3, MOF |  | §1.8 | `uitdrukkingen/uml.md` |

## Linked Data-termen

| Term | Ook genoemd | Engels | MIM 1.2 | Bestand |
|---|---|---|---|---|
| MIM-vocabulaire | mim.ttl, vocabulaire |  | §4.1, §4.2 | `uitdrukkingen/linked-data.md` |
| Shapes | mim-shapes.ttl, shapesgraph, SHACL-shapes |  | §4.2 | `uitdrukkingen/linked-data.md` |
| Transformatie naar RDFS/OWL/SHACL | promoveren, mim:equivalent, ontologie |  | §6.4 | `uitdrukkingen/linked-data.md` |

## Afkortingen

| Term | Ook genoemd | Engels | MIM 1.2 | Bestand |
|---|---|---|---|---|
| BAG | Basisregistratie Adressen en Gebouwen (voorbeeld in MIM) |  | - | `woordenlijst.md` |
| BRK | Basisregistratie Kadaster (voorbeeld in MIM) |  | - | `woordenlijst.md` |
| BRP | Basisregistratie Personen (voorbeeld in MIM) |  | - | `woordenlijst.md` |
| EA | Sparx Enterprise Architect |  | §2.1, §3.3.1 | `uitdrukkingen/uml.md` |
| GAB | Gegevensbeschrijving (normreferentie, zie §1.13) |  | §1.13, §5.1.1 | `onderwerpen/datatypen.md` |
| IM | informatiemodel (gangbaar voorvoegsel, bv. IMKAD) |  | §2.3.6.1 | `modelelementen/informatiemodel.md` |
| Imvertor | open source tool om te controleren of een model aan MIM voldoet |  | §3.3.3, §4.4 | `uitdrukkingen/uml.md` |
| LD | Linked Data |  | §1.9 | `uitdrukkingen/linked-data.md` |
| MIM | Metamodel Informatie Modellering |  | §1 | `SKILL.md` |
| MOF | Meta Object Facility |  | §1.8 | `uitdrukkingen/uml.md` |
| NEN3610 | Basismodel Geo-informatie (normreferentie; extensies buiten scope van versie 1) |  | §1.13 | `onderwerpen/extensies.md` |
| NORA | Nederlandse Overheid Referentie Architectuur (Handreiking gegevensbeschrijving) |  | §1.13 | `onderwerpen/begrippen-en-definities.md` |
| OCL | Object Constraint Language |  | §5.7 | `modelelementen/constraint.md` |
| OMG | Object Management Group |  | §1.8 | `uitdrukkingen/uml.md` |
| OWL | Web Ontology Language |  | §6.4 | `uitdrukkingen/linked-data.md` |
| RDF | Resource Description Framework |  | §1.9 | `uitdrukkingen/linked-data.md` |
| RDFS | RDF Schema |  | §6.4 | `uitdrukkingen/linked-data.md` |
| SCAT | Stelselcatalogus |  | §1.13, §5.14 | `onderwerpen/begrippen-en-definities.md` |
| SHACL | Shapes Constraint Language |  | §1.9.1, §4.2 | `uitdrukkingen/linked-data.md` |
| SKOS | Simple Knowledge Organization System |  | §1.9 | `uitdrukkingen/linked-data.md` |
| UML | Unified Modeling Language |  | §1.8 | `uitdrukkingen/uml.md` |
| URI | Uniform Resource Identifier |  | §2.4.2 | `metagegevens.md` |
| URN | Uniform Resource Name |  | §2.4.2.1 | `metagegevens.md` |
| XMI | XML Metadata Interchange (exportformaat van UML-tools) |  | - | `uitdrukkingen/uml.md` |
