---
id: keuze
titel: Keuze
metaclass: Keuze
bron: ["2.3.7.2", "2.2.4.1", "3.1.3.2", "3.2.4.4", "4.2.3.2", "6.4.6.5", "5.3"]
mim-versie: "1.2"
status: normatief
---

# Keuze

**In het kort.** Een keuze somt een aantal modelelementen op waarvan er in een concreet geval precies één geldt, zoals "de geometrie is óf een lijn óf een vlak". MIM kent vijf situaties (use cases) waarin een keuze wordt gebruikt.

## 1. Definitie

> Een opsomming van meerdere modelelementen, waarbij er maar van één tegelijkertijd sprake kan zijn.
>
> — MIM 1.2, §2.3.7.2 (normatief)

## 2. Uitleg

> Een belangrijk voordeel van het gebruik van de `Keuze` ten opzichte van een constraint is dat de kardinaliteiten zuiver gehouden kunnen worden.
>
> — MIM 1.2, §2.3.7.2 (normatief)

> Hierbij is het vooral van belang dat er als gevolg van de modellering van een keuze in plaats van constraint er geen nieuwe kenmerken mogen ontstaan en ook geen kenmerken mogen wegvallen. De kenmerken van het object blijven gelijk.
>
> — MIM 1.2, §2.3.7.2 (normatief)

De vijf use cases, in het kort (eigen samenvatting van §2.3.7.2; uitgebreid in `onderwerpen/keuze.md`):

| # | Keuze tussen | Gekoppeld aan | Voorbeeld uit MIM |
|---|---|---|---|
| 1 | datatypen | een attribuutsoort (de keuze is het type) | geometrie van Weg: `GM_Curve` of `GM_Surface` (keuze `LijnOfVlak`) |
| 2 | twee of meer attribuutsoorten | het objecttype | Betalingsopdracht: `betalingskenmerk` of `omschrijving` |
| 3 | attribuutsoorten als invulling van één betekenisvolle attribuutsoort | die attribuutsoort | `beschrijving` als betalingskenmerk of omschrijving |
| 4 | relatiedoelen van één betekenisvolle relatiesoort | de relatiesoort | `eigenaar` van Vervoermiddel: Persoon of Bedrijf |
| 5 | twee of meer relatiesoorten, elk betekenisvol | het objecttype | Vervoermiddel: `eigenaar` of `wordt verhuurd door` |

De keuze zelf heeft geen eigen betekenis als kenmerk; de naam is arbitrair (§2.3.7.2, use case 2). De opties blijven wat ze zijn: een datatype blijft een datatype, een attribuutsoort een attribuutsoort (§3.1.3.2).

**Regel.** Opties binnen één keuze mogen niet identiek zijn: andere naam én een ander datatype, of hetzelfde datatype met een ander (formeel) patroon (§5.3).

**Terminologie.** De opties heten sinds MIM 1.1 geen "keuze-elementen" meer (§3.2.4.4). §5.3 gebruikt die term nog wel; zie `bekende-onduidelijkheden.md`.

## 3. Uitdrukking in UML en Linked Data

| | UML | Linked Data |
|---|---|---|
| Uitdrukking | stereotype «Keuze» op een (UML) Class, (UML) Datatype of (UML) Property, afhankelijk van de use case (§3.1.3.2) | `mim:Keuze` (§4.2.3.2); voor een keuze tussen relatiesoorten `mim:Keuzeconstraint` (§4.2.3.1) |
| Metagegevens | §3.2.4.4 | geen eigen tabel in §4.3 |
| Transformatie naar RDFS/OWL/SHACL | | `sh:xone` met een `rdf:List` (§6.4.4.1, §6.4.6.5) |

In UML (§3.1.3.2):

- UML-Datatype met stereotype keuze: bevat alleen de datatypen waaruit gekozen wordt (use case 1);
- UML-Class met stereotype keuze: bevat de attribuutsoorten of relatiedoelen waaruit gekozen wordt (use case 2 tot en met 5);
- UML-Property met stereotype keuze: hulpconstructie om de keuze aan het objecttype of de attribuutsoort te koppelen. Zo'n property is zelf géén attribuutsoort.

In LD is `mim:Keuze` een specialisatie van `mim:Datatype` (§4.2.3.2). De vocabulaire spelt de klasse voor relatiesoortkeuze als `mim:KeuzeConstraint`.

## 4. Metagegevens en bindingen

Lees de tabel zoals beschreven in `metagegevens.md` (paragraaf "Zo lees je de tabellen").

<!-- BEGIN GEGENEREERD: metagegevens keuze -->
| Metagegeven | Betekenis | UML | LD | Verplicht | Verschil UML/LD |
|---|---|---|---|---|---|
| Identificatie | §2.4.2.2 | `1` (§3.2.4.4) | - | verplicht |  |
| Naam | §2.4.3.1 | `1` (§3.2.4.4) | - | verplicht |  |
| Alias | §2.4.3.2 | `0..1` (§3.2.4.4) | - | optioneel |  |
| Herkomst | §2.4.3.4 | `0..1` (§3.2.4.4) | - | optioneel |  |
| Begrip | §2.4.3.3 | `0..*` (§3.2.4.4) | - | optioneel |  |
| Definitie | §2.4.3.5 | `0..1` (§3.2.4.4) | - | optioneel |  |
| Herkomst definitie | §2.4.3.6 | `0..1` (§3.2.4.4) | - | optioneel |  |
| Toelichting | §2.4.3.7 | `0..1` (§3.2.4.4) | - | optioneel |  |
| Datum opname | §2.4.3.8 | `1` (§3.2.4.4) | - | verplicht |  |
| heeft datatypekeuze | §2.4.4.12 | `0..*` (§3.2.4.4) | - | optioneel |  |
| heeft keuzeattribuut | §2.4.4.14 | `0..*` (§3.2.4.4) | - | optioneel |  |
| heeft keuzerelatiedoel | - | `0..*` (§3.2.4.4) | - | optioneel |  |
| heeft constraint | §2.4.4.17 | `0..*` (§3.2.4.4) | - | optioneel |  |
<!-- EINDE GEGENEREERD -->

Eigen uitleg bij de tabel: de bindingen heten in §2.4.4 heeft datatypekeuze, heeft attribuutkeuze, heeft keuzeattribuut, heeft relatiedoelkeuze en heeft relatiesoortkeuze. De UML-tabel noemt daarnaast "heeft keuzerelatiedoel". MIM 1.2 maakte de namen keuzeattribuut en keuzerelatiedoel consistent (versielog, issue 286).

## 5. Voorbeeld en tegenvoorbeeld

**Voorbeeld uit MIM.**

> Voorbeeld: Attribuutsoort `geometrie` als kenmerk van een objecttype `Weg`. Dit is een keuze uit `Datatype` `GM_Curve` of `Datatype` `GM_Surface`. De opsomming van beide keuzemogelijkheden noemen we de `Keuze` `LijnOfVlak`. De binding aan het attribuutsoort `geometrie` gebeurt door aan te geven dat `LijnOfVlak` het type is van `geometrie`.
>
> — MIM 1.2, §2.3.7.2 (niet-normatief, voorbeeld)

**Tegenvoorbeeld uit MIM.** Twee optionele attribuutsoorten (`0..1`) met een constraint "één van beide is gevuld" geeft onzuivere kardinaliteiten: de werkelijke kardinaliteit is `1..1` (§2.3.7.2, use case 1 en 2).

## 6. Wordt vaak verward met

- **Constraint.** Zie `onderscheidingen/keuze-vs-constraint.md`.
- **Enumeratie.** Een enumeratie somt waarden op, een keuze modelelementen.

## Zie ook

- `onderwerpen/keuze.md`
- Letterlijke tekst: `python3 scripts/mim.py paragraaf 2.3.7.2`
