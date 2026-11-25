---
id: object-objecttype-gegeven
titel: Object, objecttype en gegeven
bron: ["2.3.1", "2.3.1.1", "2.3.1.2", "2.3.2.1", "1.5.1"]
mim-versie: "1.2"
status: toelichtend
---

# Object, objecttype en gegeven

**In het kort.** Een **object** is een ding in de werkelijkheid (Jan, de Domtoren). Een **objecttype** is de soort (Persoon, Gebouw) en staat in het informatiemodel. Een **gegeven** is een vastgelegde waarneming of bewering over een kenmerk van een object ("de geboortedatum van Jan is 1-1-1970"). Objecten en gegevens staan niet in het model.

## Wat MIM zegt

> Een object is een onderscheidbaar iets in het beschouwde domein.
>
> — MIM 1.2, §2.3.1.1 (normatief)

> Een **object is geen modelelement** in een informatiemodel. Een objecttype is wel een modelelement in een informatiemodel.
>
> — MIM 1.2, §2.3.1.1 (niet-normatief, noot)

> Een gegeven is een vastgelegde waarneming of bewering over een getypeerde eigenschap van een object.
>
> — MIM 1.2, §2.3.1.2 (normatief)

> Een **gegeven is geen modelelement** in een informatiemodel.
>
> — MIM 1.2, §2.3.1.2 (niet-normatief, noot)

## Samenhang (eigen uitleg)

| Laag | In de werkelijkheid of registratie | In het informatiemodel |
|---|---|---|
| Ding | object: Jan | objecttype: Persoon |
| Kenmerk | Jan heeft een geboortedatum | attribuutsoort: geboortedatum |
| Waarde | gegeven: geboortedatum van Jan is 1-1-1970 | datatype: Date |
| Verband | Jan woont in Paleis Het Loo | relatiesoort: woont in (Persoon → Gebouw) |

Een object heet ook wel een exemplaar of instantie van een objecttype (§2.3.1.1). Objecten zijn nooit abstract; een objecttype kan dat wel zijn (§2.3.2.1).

Een gegeven heeft vier kanten (§2.3.1.2): het is een **waarneming of bewering**, het is **vastgelegd**, het is **getypeerd** (het hoort bij een attribuutsoort, relatiesoort of externe koppeling) en het heeft een **waarde** die aan het datatype moet voldoen.

In termen van de vier lagen van OMG (§1.8): het informatiemodel zit op M1, objecten en gegevens op M0, MIM zelf op M2.

## Zie ook

- `modelelementen/objecttype.md`, `onderwerpen/beschouwingsniveaus.md`
- Letterlijke tekst: `python3 scripts/mim.py paragraaf 2.3.1 --met-sub`
