---
id: gegevensgroep
titel: Gegevensgroep
metaclass: Gegevensgroep
bron: ["2.3.2.3", "3.2.1.3", "4.3.1.3", "6.4.5.3", "5.2"]
mim-versie: "1.2"
status: normatief
---

# Gegevensgroep

**In het kort.** Een gegevensgroep is het kenmerk van een objecttype dat een groep samenhangende gegevens aan dat objecttype koppelt. De inhoud van de groep staat in een gegevensgroeptype; de gegevensgroep is de "aansluiting" op het objecttype.

## 1. Definitie

> Een typering van een groep van gelijksoortige gegevens die voor een objecttype van toepassing is.
>
> — MIM 1.2, §2.3.2.3 (normatief)

## 2. Uitleg

> Dit modelelement verzorgt de modelmatige aankoppeling van een `«Gegevensgroeptype»` aan het `«Objecttype»` waartoe een `«Gegevensgroeptype»` onlosmakelijk behoort. De groep van gegevens is een kenmerk van een object. De `«Gegevensgroep»` is een betekenisvol kenmerk van een `«Objecttype»`. De `«Gegevensgroep»` heeft altijd als type een `«Gegevensgroeptype»`.
>
> — MIM 1.2, §2.3.2.3 (normatief)

Eigen uitleg. Gegevensgroep en gegevensgroeptype horen altijd bij elkaar, vergelijkbaar met een attribuutsoort en zijn datatype:

| | Attribuutsoort | Gegevensgroep |
|---|---|---|
| Is een kenmerk van | objecttype | objecttype |
| Heeft als type | datatype | gegevensgroeptype |

Het verschil: een datatype beschrijft alleen structuur, een gegevensgroeptype bevat attribuutsoorten die elk zelf betekenis hebben (§5.2.2). Een objecttype kan niet rechtstreeks een gegevensgroeptype hebben; dat loopt altijd via een gegevensgroep (§2.2.2).

## 3. Uitdrukking in UML en Linked Data

| | UML | Linked Data |
|---|---|---|
| Uitdrukking | stereotype «Gegevensgroep» op een (UML) Property; in EA: Attribute (§3.1.1) | `mim:Gegevensgroep` (§4.2.1) |
| Metagegevens | §3.2.1.3 | §4.3.1.3 |
| Transformatie naar RDFS/OWL/SHACL | | `sh:PropertyShape` en `owl:ObjectProperty` (§6.4.4.1, §6.4.5.3) |

## 4. Metagegevens en bindingen

Lees de tabel zoals beschreven in `metagegevens.md` (paragraaf "Zo lees je de tabellen").

<!-- BEGIN GEGENEREERD: metagegevens gegevensgroep -->
| Metagegeven | Betekenis | UML | LD | Verplicht | Verschil UML/LD |
|---|---|---|---|---|---|
| Identificatie | §2.4.2.2 | `1` (§3.2.1.3) | `1` (§4.3.1.3) | verplicht |  |
| Naam | §2.4.3.1 | `1` (§3.2.1.3) | `1` (§4.3.1.3) | verplicht |  |
| Alias | §2.4.3.2 | `0..1` (§3.2.1.3) | `0..1` (§4.3.1.3) | optioneel |  |
| Herkomst | §2.4.3.4 | `0..1` (§3.2.1.3) | `1` (§4.3.1.3) | afwijkend tussen UML en LD | ja |
| Begrip | §2.4.3.3 | `0..*` (§3.2.1.3) | `0..*` (§4.3.1.3) | optioneel |  |
| Definitie | §2.4.3.5 | `1` (§3.2.1.3) | `1` (§4.3.1.3) | verplicht |  |
| Herkomst definitie | §2.4.3.6 | `1` (§3.2.1.3) | `1` (§4.3.1.3) | verplicht |  |
| Toelichting | §2.4.3.7 | `0..1` (§3.2.1.3) | `0..1` (§4.3.1.3) | optioneel |  |
| Datum opname | §2.4.3.8 | `1` (§3.2.1.3) | `1` (§4.3.1.3) | verplicht |  |
| Kardinaliteit | §2.4.3.14 | `1` (§3.2.1.3) | `1` (§4.3.1.3) | verplicht |  |
| Authentiek | §2.4.3.16 | `1` (§3.2.1.3) | `1` (§4.3.1.3) | verplicht |  |
| heeft gegevensgroeptype | §2.4.4.3 | `1` (§3.2.1.3) | `1` (§4.3.1.3) | verplicht |  |
| heeft constraint | §2.4.4.17 | `0..*` (§3.2.1.3) | `0..*` (§4.3.1.3) | optioneel |  |
| Begripsterm | - | - | `0..*` (§4.3.1.3) | optioneel | ja |
<!-- EINDE GEGENEREERD -->

Eigen uitleg bij de tabel:

- Historie-metagegevens horen in MIM 1.2 niet meer bij een gegevensgroep: ze zijn verwijderd (versielog, issue 224, §6.5). Historie geef je aan bij de afzonderlijke attribuutsoorten in het gegevensgroeptype.
- **Kardinaliteit** van de gegevensgroep telt mee bij hoe vaak een gegeven bij het object voorkomt (§2.4.3.14): de kardinaliteit van de attribuutsoort binnen het gegevensgroeptype én die van de gegevensgroep.
- **Herkomst** is in de UML-tabel optioneel en in de LD-tabel verplicht. MIM 1.2 lost dat niet op; meld het verschil.

## 5. Voorbeeld en tegenvoorbeeld

**Voorbeeld uit MIM.** In de BRK heeft een schip een motor met eigen eigenschappen. De motor is geen zelfstandig object (er kan geen aparte eigenaar van zijn), dus de eigenschappen van de motor komen in een gegevensgroeptype, en het schip krijgt een gegevensgroep "motor" (§2.3.2.4).

**Tegenvoorbeeld (eigen voorbeeld).** "Bedrag" (som en valuta) is geen gegevensgroep: som en valuta hebben los van elkaar geen betekenis voor het object. Dat is een gestructureerd datatype. Zie `onderscheidingen/gegevensgroep-vs-gestructureerd-datatype.md`.

## 6. Wordt vaak verward met

- **Gegevensgroeptype.** De gegevensgroep is het kenmerk, het gegevensgroeptype is de inhoud. Zie `modelelementen/gegevensgroeptype.md`.
- **Gestructureerd datatype.** Zie `onderscheidingen/gegevensgroep-vs-gestructureerd-datatype.md`.
- **Attribuutsoort.** De gegevensgroep als geheel is géén attribuutsoort van het object (§2.3.2.4).

## Zie ook

- Letterlijke tekst: `python3 scripts/mim.py paragraaf 2.3.2.3`
