---
id: gegevensgroeptype
titel: Gegevensgroeptype
metaclass: Gegevensgroeptype
bron: ["2.3.2.4", "3.2.1.4", "4.3.1.4", "6.4.5.4", "5.2", "5.2.1", "5.2.2"]
mim-versie: "1.2"
status: normatief
---

# Gegevensgroeptype

**In het kort.** Een gegevensgroeptype bundelt attribuutsoorten die bij elkaar horen, bijvoorbeeld omdat ze samen veranderen. De attribuutsoorten blijven kenmerken van het object; het groeperen is een modelleerkeuze. Een gegevensgroeptype is altijd het type van een gegevensgroep.

## 1. Definitie

> Een groep van met elkaar samenhangende attribuutsoorten. Een gegevensgroeptype is altijd een type van een gegevensgroep.
>
> — MIM 1.2, §2.3.2.4 (normatief)

## 2. Uitleg

> Een `«Attribuutsoort»` van een `«Gegevensgroeptype»` is semantisch gezien een eigenschap van een `«Objecttype»`. Echter, vanwege samenhangend gedrag (ze horen semantisch bij elkaar, ze wijzigen bijvoorbeeld gelijktijdig e.d.) zijn deze ondergebracht in een apart modelelement. Het onderbrengen van attribuutsoorten in een groep c.q. in het modelelement gegevensgroeptype, is een modelleerkeuze, het is niet perse noodzakelijk.
>
> — MIM 1.2, §2.3.2.4 (normatief)

> De gegevensgroep als geheel wordt daarom expliciet niet gezien als zijnde één attribuutsoort van een object.
>
> — MIM 1.2, §2.3.2.4 (normatief)

**Hergebruik.** Meestal hoort een gegevensgroeptype bij één objecttype. Hergebruik door meerdere objecttypen mag, maar alleen als de definitie voor al die objecttypen gelijk is (§2.3.2.4, §5.2.1). Op conceptueel niveau noemt MIM dat ongebruikelijk maar toegestaan.

**Wat mag een gegevensgroeptype bevatten?** Hier spreekt MIM 1.2 zichzelf tegen (onduidelijkheid I1):

> Een gegevensgroeptype kan, naast attribuutsoorten en relatiesoorten, ook zelf weer gegevensgroeptypen bevatten.
>
> — MIM 1.2, §2.3.2.4 (normatief)

> Richtlijn: een gegevensgroeptype bevat alleen «Attribuutsoort»en en geen «Relatiesoort»en. Als er wel een relatie aan de orde is, dan wordt de gegevensgroep gezien als een apart te beheren object. Er wordt dan een apart «Objecttype» gemaakt.
>
> — MIM 1.2, §5.2 (normatief)

Eigen uitleg. De metagegevenstabellen (§3.2.1.4) en de bindingen (§2.4.4.6, §2.4.4.7) staan een relatiesoort en externe koppeling vanuit een gegevensgroeptype wél toe. Noem bij een antwoord beide passages en verwijs naar `bekende-onduidelijkheden.md` (I1). Kies niet zelf.

Een gegevensgroeptype kan geen doel van een relatie zijn; inkomende relaties gaan altijd naar een objecttype (§4.2.1, en de Keuze-teksten in §2.2.4.1).

## 3. Uitdrukking in UML en Linked Data

| | UML | Linked Data |
|---|---|---|
| Uitdrukking | stereotype «Gegevensgroeptype» op een (UML) Class; in EA: Class (§3.1.1) | `mim:Gegevensgroeptype` (§4.2.1) |
| Metagegevens | §3.2.1.4 | §4.3.1.4 |
| Transformatie naar RDFS/OWL/SHACL | | `owl:Class` en `sh:NodeShape` (§6.4.4.1, §6.4.5.4) |

## 4. Metagegevens en bindingen

Lees de tabel zoals beschreven in `metagegevens.md` (paragraaf "Zo lees je de tabellen").

<!-- BEGIN GEGENEREERD: metagegevens gegevensgroeptype -->
| Metagegeven | Betekenis | UML | LD | Verplicht | Verschil UML/LD |
|---|---|---|---|---|---|
| Identificatie | §2.4.2.2 | `1` (§3.2.1.4) | `1` (§4.3.1.4) | verplicht |  |
| Naam | §2.4.3.1 | `1` (§3.2.1.4) | `1` (§4.3.1.4) | verplicht |  |
| Alias | §2.4.3.2 | `0..1` (§3.2.1.4) | `0..1` (§4.3.1.4) | optioneel |  |
| Herkomst | §2.4.3.4 | `1` (§3.2.1.4) | - | verplicht | ja |
| Begrip | §2.4.3.3 | `0..*` (§3.2.1.4) | `0..*` (§4.3.1.4) | optioneel |  |
| Definitie | §2.4.3.5 | `1` (§3.2.1.4) | `0..1` (§4.3.1.4) | afwijkend tussen UML en LD | ja |
| Herkomst definitie | §2.4.3.6 | `1` (§3.2.1.4) | `0..1` (§4.3.1.4) | afwijkend tussen UML en LD | ja |
| Toelichting | §2.4.3.7 | `0..1` (§3.2.1.4) | `0..1` (§4.3.1.4) | optioneel |  |
| Datum opname | §2.4.3.8 | `1` (§3.2.1.4) | `1` (§4.3.1.4) | verplicht |  |
| Kardinaliteit | §2.4.3.14 | `1` (§3.2.1.4) | - | verplicht | ja |
| Authentiek | §2.4.3.16 | `1` (§3.2.1.4) | - | verplicht | ja |
| heeft attribuut | §2.4.4.1 | `0..*` (§3.2.1.4) | `0..*` (§4.3.1.4) | optioneel |  |
| heeft gegevensgroep | §2.4.4.2 | `0..*` (§3.2.1.4) | `0..*` (§4.3.1.4) | optioneel |  |
| heeft relatiesoort | §2.4.4.6 | `0..*` (§3.2.1.4) | - | optioneel | ja |
| heeft externe koppeling | §2.4.4.7 | `0..*` (§3.2.1.4) | - | optioneel | ja |
| verwijst naar supertype | §2.4.4.4 | `0..*` (§3.2.1.4) | - | optioneel | ja |
| heeft constraint | §2.4.4.17 | `0..*` (§3.2.1.4) | `0..*` (§4.3.1.4) | optioneel |  |
| Begripsterm | - | - | `0..*` (§4.3.1.4) | optioneel | ja |
<!-- EINDE GEGENEREERD -->

Eigen uitleg bij de tabel: de UML-tabel noemt voor het gegevensgroeptype ook Kardinaliteit, Authentiek en "verwijst naar supertype". Die staan niet in de LD-tabel. Generalisatie is volgens de definitie alleen gedefinieerd voor objecttypen en datatypen (§2.3.3.1). Ook dit is een verschil in de bron; zie `bekende-onduidelijkheden.md`.

## 5. Voorbeeld en tegenvoorbeeld

**Voorbeeld uit MIM.**

> Een voorbeeld van het hergebruik van een gegevensgroeptype door meerdere objecttypen is de specificatie voor het Brondocument in de basisregistratie BAG. Het gegevensgroeptype Brondocument is qua betekenis en structuur voor alle objecttypes gelijk.
>
> — MIM 1.2, §5.2.1 (niet-normatief, voorbeeld)

**Tegenvoorbeeld uit MIM.** Jan Jansen (voornaam en achternaam) is een gegevensgroeptype Naam, geen gestructureerd datatype: er zijn meerdere personen met die naam, dus de waarde "identificeert zichzelf" niet (§2.3.5.3).

## 6. Wordt vaak verward met

- **Objecttype.** Heeft het "ding" een eigen bestaan, eigen eigenaar of eigen relaties? Dan is het een objecttype. Zie het motorvoorbeeld in `modelelementen/gegevensgroep.md`.
- **Gestructureerd datatype.** Zie `onderscheidingen/gegevensgroep-vs-gestructureerd-datatype.md`.

## Zie ook

- `modelelementen/gegevensgroep.md`
- `bekende-onduidelijkheden.md` (I1)
- Letterlijke tekst: `python3 scripts/mim.py paragraaf 2.3.2.4`
