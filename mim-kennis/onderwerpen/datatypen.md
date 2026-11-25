---
id: datatypen
titel: Datatypen in de praktijk
bron: ["5.1", "5.1.1", "5.1.1.1", "5.1.1.2", "5.1.2", "5.1.3", "5.1.4", "6.4.4.3", "2.4.3.29"]
mim-versie: "1.2"
status: normatief
---

# Datatypen in de praktijk

**In het kort.** MIM kent vier categorieën datatypen: primitieve datatypen uit internationale standaarden (CharacterString, Integer, …), landelijke datatypen (zoals Postcode), zelfgedefinieerde datatypen en gestructureerde datatypen. Beperkingen zoals lengte en patroon zet je als metagegeven bij de attribuutsoort, niet in het datatype.

## Vier categorieën

> 1. **Primitief datatype**: data zoals `"Amersfoort"` of `"10"` worden vastgelegd als `CharacterString` en `Integer`. Dit volgt de internationale standaarden voor datatypen.
> 2. **Landelijk datatype** (volgens het GAB): datatypen zoals: `Postcode`, `DMO` en `DTMO` (zie ook: 5.1.3 Landelijk Datatype).
> 3. **Zelfgedefinieerd datatype**: data zoals `NietNegatieveInteger`, `AN` (Alfanumerieke waarde) of een `Vlak`.
> 4. **Gestructureerd datatype**: een combinatie van data, zoals een `bedrag`: `"5 euro"`, opgebouwd uit `waarde` = `"5"` en `munteenheid` = `"euro"`), of een `GM_Surface`. Deze volgen ook internationale of nationale standaarden.
>
> — MIM 1.2, §5.1 (normatief)

> De primitieve datatypen uit onderstaande lijst moeten gebruikt worden. De landelijke en de Gestructureerde datatypen hoeven niet per sé gebruikt te worden, maar het gebruik hiervan wordt wel aanbevolen.
>
> — MIM 1.2, §5.1 (normatief)

## De primitieve datatypen van MIM 1.2

Eigen samenvatting van de tabel in §5.1.1; het LD-type komt uit §6.4.4.3.

| Datatype | Betekenis (kort) | In LD |
|---|---|---|
| CharacterString | alle tekens van de tekenset (standaard UTF-8); getallen met voorloopnullen ook | `xsd:string` |
| Integer | geheel getal, zonder voorloopnullen | `xsd:integer` |
| Real | zwevendekommagetal, geschatte waarde | `xsd:float` |
| Decimal | decimaal getal, exacte waarde | `xsd:decimal` |
| Boolean | True/false of 1/0 | `xsd:boolean` |
| Date | yyyy-mm-dd (ISO 8601) | `xsd:date` |
| DateTime | yyyy-mm-ddThh:mm:ss (ISO 8601) | `xsd:dateTime` |
| Year | yyyy | `xsd:gYear` |
| Day | dd | `xsd:gDay` |
| Month | mm | `xsd:gMonth` |
| URI | unieke identificatie volgens RFC 3986 | `xsd:anyURI` |

Extra primitieve datatypen kunnen in een eigen extensie (§5.1.1). Let op: Boolean kent alleen true/false; wil je "Ja"/"Nee", gebruik dan een enumeratie of AN met patroon (§5.1.1).

## Getallen, lengte en patroon (eigen samenvatting)

- Kun je er niet mee rekenen (bankrekeningnummer, gemeentecode `0060`)? Gebruik CharacterString met een patroon (§5.1.1.1, §5.1.1.2).
- Het - of + teken telt niet mee in de lengte (§5.1.1.1).
- Patroon is een beschrijving in tekst; Formeel patroon een reguliere expressie (§5.1.1.2).
- Notatie van Lengte: `"2..80"` voor tekens, `"3,2"` voor getallen met decimalen (§2.4.3.29).

## Landelijke en zelfgedefinieerde datatypen

Landelijke datatypen zoals Postcode, DMO (datum mogelijk onvolledig) en DTMO zijn geen onderdeel van MIM; MIM beschrijft alleen hoe je ze modelleert (§5.1.3). Zelfgedefinieerde datatypen zijn primitieve datatypen, codelijsten of referentielijsten in het eigen model, met een eigen definitie (§5.1.2). Het soort modelelement verandert niet door generalisatie (§5.1.2).

## Zie ook

- `modelelementen/datatype.md`, `modelelementen/primitief-datatype.md`, `modelelementen/gestructureerd-datatype.md`
- Letterlijke tekst: `python3 scripts/mim.py paragraaf 5.1 --met-sub`
