---
id: primitief-datatype
titel: Primitief datatype
metaclass: Primitief datatype
bron: ["2.3.5.2", "3.2.4.1", "4.3.4.1", "6.4.6.1", "6.4.6.2", "5.1.1", "5.1.2"]
mim-versie: "1.2"
status: normatief
---

# Primitief datatype

**In het kort.** Een primitief datatype is een enkelvoudig datatype zonder onderdelen, zoals tekst (CharacterString), een geheel getal (Integer) of een datum (Date). Een model kan ook eigen primitieve datatypen maken, zoals Postcode, gebaseerd op een standaard datatype.

## 1. Definitie

> Een datatype met een eenvoudige basisstructuur, oftewel enkelvoudig en zonder gelaagdheid.
>
> — MIM 1.2, §2.3.5.2 (normatief)

## 2. Uitleg

> Een primitief datatype is een datatype zonder verdere specificatie over de structuur. Dit datatype is enkelvoudig, oftewel niet samengesteld en wordt ook wel simpel datatype genoemd. Dit datatype kent daarom zelf geen eigen modelelementen zoals een «Data element».
>
> — MIM 1.2, §2.3.5.2 (normatief)

Eigen uitleg. MIM onderscheidt twee gevallen (§2.3.5.2):

1. **Standaard datatypen** zoals CharacterString en Integer. Ze hebben hun naam en definitie uit ISO-standaarden en hebben **geen** MIM-metaclass. MIM 1.2 noemt CharacterString, Integer, Real, Decimal, Boolean, Date, DateTime, Year, Day, Month en URI (§5.1.1). Zie `onderwerpen/datatypen.md`.
2. **Zelfgedefinieerde primitieve datatypen** in het eigen model, zoals AN of Postcode. Die krijgen wel de MIM-metaclass Primitief datatype en hebben een eenduidig aangegeven standaard datatype als basis (via generalisatie of via een extensie).

Een primitief datatype kan een patroon of formeel patroon hebben dat de waarden verder beperkt. Lengte geldt alleen voor zelfgedefinieerde primitieve datatypen (§2.4.3.29).

## 3. Uitdrukking in UML en Linked Data

| | UML | Linked Data |
|---|---|---|
| Uitdrukking | stereotype «Primitief datatype» op een (UML) Primitive Type; in EA: Datatype (§3.1.2) | `mim:PrimitiefDatatype` (§4.2.2) |
| Metagegevens | §3.2.4.1 | §4.3.4.1 |
| Transformatie naar RDFS/OWL/SHACL | | `rdfs:Datatype` (§6.4.6.1); standaard datatypen naar `xsd:`-typen, bv. CharacterString → `xsd:string` (§6.4.4.3, §6.4.6.2) |

## 4. Metagegevens en bindingen

Lees de tabel zoals beschreven in `metagegevens.md` (paragraaf "Zo lees je de tabellen").

<!-- BEGIN GEGENEREERD: metagegevens primitief-datatype -->
| Metagegeven | Betekenis | UML | LD | Verplicht | Verschil UML/LD |
|---|---|---|---|---|---|
| Identificatie | §2.4.2.2 | `1` (§3.2.4.1) | `1` (§4.3.4.1) | verplicht |  |
| Naam | §2.4.3.1 | `1` (§3.2.4.1) | `1` (§4.3.4.1) | verplicht |  |
| Alias | §2.4.3.2 | `0..1` (§3.2.4.1) | `0..1` (§4.3.4.1) | optioneel |  |
| Herkomst | §2.4.3.4 | `0..1` (§3.2.4.1) | `1` (§4.3.4.1) | afwijkend tussen UML en LD | ja |
| Begrip | §2.4.3.3 | `0..*` (§3.2.4.1) | `0..*` (§4.3.4.1) | optioneel |  |
| Definitie | §2.4.3.5 | `0..1` (§3.2.4.1) | `1` (§4.3.4.1) | afwijkend tussen UML en LD | ja |
| Herkomst definitie | §2.4.3.6 | `0..1` (§3.2.4.1) | - | optioneel | ja |
| Toelichting | §2.4.3.7 | `0..1` (§3.2.4.1) | `0..1` (§4.3.4.1) | optioneel |  |
| Datum opname | §2.4.3.8 | `1` (§3.2.4.1) | `1` (§4.3.4.1) | verplicht |  |
| Lengte | §2.4.3.29 | `0..1` (§3.2.4.1) | `0..1` (§4.3.4.1) | optioneel |  |
| Patroon | §2.4.3.30 | `0..1` (§3.2.4.1) | `0..1` (§4.3.4.1) | optioneel |  |
| Formeel patroon | §2.4.3.31 | `0..1` (§3.2.4.1) | `0..1` (§4.3.4.1) | optioneel |  |
| heeft constraint | §2.4.4.17 | `0..*` (§3.2.4.1) | `0..*` (§4.3.4.1) | optioneel |  |
| Begripsterm | - | - | `0..*` (§4.3.4.1) | optioneel | ja |
| Type (heeft datatype) | §2.4.3.28 / §2.4.4.5 | - | `1` (§4.3.4.1) | verplicht | ja |
<!-- EINDE GEGENEREERD -->

Eigen uitleg bij de tabel: de metagegevens gelden voor primitieve datatypen die in het model zelf worden gedefinieerd, niet voor datatypen die al buiten het model bestaan, zoals Integer (§3.2.4). Definitie en Herkomst zijn in de UML-tabel optioneel en in de LD-tabel verplicht; meld dat verschil.

## 5. Voorbeeld en tegenvoorbeeld

**Voorbeeld uit MIM.**

> Een voorbeeld waar een patroon nodig is, is een attribuut waarvan het waardenbereik altijd een getal is met precies de lengte 4, zoals bijvoorbeeld 0001 tot en met 9999, en dus voorloopnullen heeft. Een datatype zoals `Integer` kan hiervoor niet gebruikt worden, omdat 0001 geen getal is.
>
> — MIM 1.2, §5.1.1.2 (normatief)

**Tegenvoorbeeld uit MIM.** Een bedrag (som en valuta) is niet enkelvoudig en dus geen primitief datatype, maar een gestructureerd datatype (§2.3.5.3).

## 6. Wordt vaak verward met

- **Gestructureerd datatype.** Zie `modelelementen/gestructureerd-datatype.md`.
- **Landelijk datatype** (zoals Postcode, DMO). Dat is geen aparte metaclass maar een afspraak op landelijk niveau; zie `onderwerpen/datatypen.md`.

## Zie ook

- `onderwerpen/datatypen.md`
- Letterlijke tekst: `python3 scripts/mim.py paragraaf 2.3.5.2`
