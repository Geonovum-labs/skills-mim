---
id: keuze
titel: Keuze in vijf use cases
bron: ["2.3.7.2", "2.2.4.1", "3.1.3.2", "4.2.3.2", "5.3"]
mim-versie: "1.2"
status: normatief
---

# Keuze: de vijf use cases

**In het kort.** MIM gebruikt een keuze wanneer er precies één van meerdere mogelijkheden geldt. Er zijn vijf situaties, elk met een eigen patroon. Het verschil zit in waartussen gekozen wordt en waaraan de keuze vastzit. In alle gevallen blijven de kenmerken van het object hetzelfde: er komen er geen bij en er vallen er geen weg.

De definitie en de uitdrukking in UML en LD staan in `modelelementen/keuze.md`. Dit bestand werkt de use cases uit.

## Use case 1: keuze tussen datatypen

> Een objecttype heeft een attribuutsoort en het datatype hiervan is ofwel datatype D1 ofwel datatype D2. In MIM modelleren we daarom 1 attribuutsoort met als datatype een keuze tussen het datatype D1 en het datatype D2. Het maken van deze keuze is verplicht.
>
> — MIM 1.2, §2.3.7.2 (normatief)

Voorbeeld: `geometrie` van `Weg` met keuze `LijnOfVlak` tussen `GM_Curve` en `GM_Surface`. Zonder keuze zou je twee attribuutsoorten met kardinaliteit `0..1` krijgen, terwijl de werkelijke kardinaliteit `1..1` is (§2.3.7.2). Ook in §5.3: `PuntOfVlak`, `BereikOfWaarde`.

## Use case 2: keuze tussen twee of meer attribuutsoorten

> Er is sprake van ofwel attribuutsoort A1 ofwel attribuutsoort A2. In MIM modelleren we daarom een keuze tussen de 2 attribuutsoorten A1 en A2. Het maken van deze keuze is verplicht.
>
> — MIM 1.2, §2.3.7.2 (normatief)

Voorbeeld: `Betalingsopdracht` heeft `betalingskenmerk` óf `omschrijving`, keuze `BetalingskenmerkOfOmschrijving`. De keuze is gebonden aan het **objecttype**. De naam van de keuze is arbitrair: het is geen attribuutsoort en komt in de data niet voor (§2.3.7.2).

## Use case 3: keuze als invulling van één betekenisvolle attribuutsoort

> Er is sprake van ofwel attribuutsoort A0 en aanvullend hierbij een keuze tussen ofwel attribuutsoort A1 ofwel attribuutsoort A2. In MIM modelleren we daarom voor A1 en A2 een keuze tussen de 2 attribuutsoorten. Het maken van deze keuze is verplicht.
>
> — MIM 1.2, §2.3.7.2 (normatief)

Voorbeeld: `Betalingsopdracht` heeft een `beschrijving` (betekenisvol kenmerk), ingevuld als betalingskenmerk óf omschrijving. De keuze is gebonden aan de **attribuutsoort** `beschrijving`: de keuze is het type ervan.

Verschil met use case 2 (MIM, §2.3.7.2): de keuze zelf is hetzelfde, alleen de binding verschilt (objecttype of attribuutsoort).

## Use case 4: keuze tussen relatiedoelen

> Er is sprake van een relatiesoort R0 en aanvullend hierbij een keuze tussen relatiedoel D1 of relatiedoel D2. In MIM modelleren we daarom een keuze tussen de 2 relatiedoelen D1 en D2. Het maken van deze keuze is verplicht.
>
> — MIM 1.2, §2.3.7.2 (normatief)

Voorbeeld: `Vervoermiddel` heeft één `eigenaar`: een `Persoon` of een `Bedrijf`, met keuze `EigenaarKeuze`. De betekenis van de relatie is hetzelfde, ongeacht het doel. Niet de bedoeling: twee relatiesoorten `eigenaar_persoon` en `eigenaar_bedrijf` (§2.3.7.2). Een gegevensgroeptype kan geen doel zijn (§2.2.4.1).

## Use case 5: keuze tussen relatiesoorten die elk betekenis hebben

> Er is sprake van een relatiesoort R1 en een relatiesoort R2. R1 heeft als doel een object van objecttype D1 en R2 heeft als doel een object van objecttype 2. In MIM modelleren we daarom een keuze met als uitgaande relatiesoorten R1 en R2. Het maken van deze keuze is verplicht.
>
> — MIM 1.2, §2.3.7.2 (normatief)

Voorbeeld: `Vervoermiddel` heeft een `eigenaar` of `wordt verhuurd door` een verhuurbedrijf: keuze `VerhuurbedrijfOfEigenaar`. Elke relatiesoort of rol heeft een eigen naam (§2.2.4.1). Use case 5 is nieuw in MIM 1.2 (versielog, issue 190).

## Overzicht (eigen samenvatting)

| # | Kiezen tussen | Keuze gebonden aan | UML-vorm van de keuze (§3.1.3.2) |
|---|---|---|---|
| 1 | datatypen | attribuutsoort (als type) | UML-Datatype «Keuze» |
| 2 | attribuutsoorten | objecttype | UML-Class «Keuze», gekoppeld via UML-Property «Keuze» |
| 3 | attribuutsoorten | attribuutsoort (als type) | UML-Class «Keuze» |
| 4 | relatiedoelen | relatiesoort | UML-Class «Keuze» met uitgaande associations «Keuze» |
| 5 | relatiesoorten | objecttype | UML-Class «Keuze», gekoppeld via UML-Association «Keuze» |

In LD: use case 1 via `mim:type`, use case 2 via `mim:attribuut`, use case 4 via `mim:doel`, use case 5 via een keuzeconstraint (§4.2.3.2). §4.2.3.2 beschrijft use case 3 niet apart.

## Regels

> Regel: het is niet toegestaan dat keuze elementen binnen één en dezelfde keuze identiek zijn. De naam van elk keuze element moet verschillend zijn én de datatypen moeten op zijn minst verschillend zijn.
>
> — MIM 1.2, §5.3 (normatief)

## Zie ook

- `modelelementen/keuze.md`, `onderscheidingen/keuze-vs-constraint.md`
- Letterlijke tekst: `python3 scripts/mim.py paragraaf 2.3.7.2`
