---
id: abstracte-objecttypen
titel: Abstracte objecttypen en concrete objecten
bron: ["5.5", "5.5.1", "5.5.2", "5.5.3", "2.4.3.33", "2.3.2.1"]
mim-versie: "1.2"
status: normatief
---

# Abstracte objecttypen

**In het kort.** Een abstract objecttype is een algemene soort waarvan geen objecten bestaan die alleen tot die soort horen. Elk object hoort bij een concreet subtype. Voorbeeld: als een persoon altijd óf docent óf leerling is, is Persoon abstract en zijn Docent en Leerling concreet.

## Wat MIM zegt

> Wanneer een `«Objecttype»` wel abstract is, dan kunnen er geen objecten bestaan die een instantie van dit `«Objecttype»` zijn. Er moet dan altijd sprake zijn van een concreet (niet abstract) `«Objecttype»` die het abstracte `«Objecttype»` als `«Generalisatie»` heeft.
>
> — MIM 1.2, §2.4.3.33 (normatief)

> De enige regel die geldt is dat een abstract objecttype niet geïnstantieerd kan worden. Elk object is altijd een instantie van een concreet objecttype.
>
> — MIM 1.2, §5.5.2 (normatief)

## Richtlijnen (§5.5.1 en §5.5.3, eigen samenvatting)

- Een abstract objecttype is een echt onderwerp van gesprek in het domein, met een eigen betekenis.
- Elke definitie, ook van een abstract objecttype, maakt ondubbelzinnig duidelijk of een object wel of niet tot het type hoort. Dus geen definitie als "De gemeenschappelijke eigenschappen van een object…".
- Wat in het ene model abstract is, kan in een ander model concreet zijn.
- Modelleer een abstract objecttype pas bij twee of meer specialisaties.
- De onderste specialisaties zijn altijd concreet.
- Een unieke aanduiding op het abstracte objecttype geldt voor alle concrete subtypen samen.

> - Modelleer een abstract objecttype pas wanneer er sprake is van twee of meer specialisaties
>
> — MIM 1.2, §5.5.3 (normatief)

## Conceptueel en logisch

Op logisch niveau gelden dezelfde regels, maar er kunnen ook implementatieredenen zijn om een abstract objecttype te maken, zoals extra hiërarchie (§5.5.2).

## In het model

- Metagegeven: Indicatie abstract object, `Ja` of `Nee`, default `Nee` (§2.4.3.33, §2.4.5).
- UML: `isAbstract`; de naam wordt cursief geschreven (§5.5.3, tabel §3.2.1.1).
- Een model mag een abstract objecttype bevatten zonder concreet subtype in hetzelfde model; de concrete typen kunnen in een ander model staan (noot bij §2.4.3.33).

## Voorbeeld uit MIM

> Wanneer ervan uit wordt gegaan dat binnen het te beschouwen gebied een persoon altijd ofwel een docent ofwel leerling kan zijn (en nooit beide tegelijk) dan definiëren we een Persoon als een abstract objecttype. Docent en Leerling zijn dan concrete objecttypen in het conceptueel informatiemodel.
>
> — MIM 1.2, §5.5.1 (niet-normatief, voorbeeld)

## Zie ook

- `modelelementen/objecttype.md`, `modelelementen/generalisatie.md`
- Letterlijke tekst: `python3 scripts/mim.py paragraaf 5.5 --met-sub`
