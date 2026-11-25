---
id: modelelement
titel: Modelelement
metaclass: Modelelement
bron: ["2.2.1", "2.1", "2.2", "2.4.3"]
mim-versie: "1.2"
status: normatief
---

# Modelelement

**In het kort.** "Modelelement" is de verzamelnaam voor alle bouwstenen van MIM: objecttype, attribuutsoort, relatiesoort, datatype, package enzovoort. Elk modelelement heeft een eigen MIM-metaclass waaraan je het herkent.

## 1. Definitie

> Elk element uit een model met een op zichzelf staande identiteit, inclusief het model zelf.
>
> — MIM 1.2, §2.2.1 (normatief)

## 2. Uitleg

> De klasse modelelement is de superklasse van alle metaklassen in het MIM-metamodel.
>
> — MIM 1.2, §2.2.1 (normatief)

> De metagegevens van de metaklassen worden niet gezien als modelelementen.
>
> — MIM 1.2, §2.2.1 (normatief)

Eigen uitleg. Twee uitgangspunten van MIM gaan direct over modelelementen (§2.1):

> Elk modelelement heeft een naam en een eigen MIM-metaclass, waaraan je het modelelement overal kan herkennen.
>
> — MIM 1.2, §2.1 (normatief)

> Uniforme toepassing van het metamodel in informatiemodellen. Anders gezegd, uitbreiden mag, afwijken niet. Maak voor hetzelfde doel geen alternatieve constructies.
>
> — MIM 1.2, §2.1 (normatief)

**De modelelementen van MIM 1.2** (eigen indeling naar §2.2):

| Groep | Modelelementen |
|---|---|
| Kern | Objecttype, Attribuutsoort, Gegevensgroep, Gegevensgroeptype, Generalisatie, Relatiesoort, Relatieklasse, Relatierol, Datatype |
| Datatypen | Primitief datatype, Gestructureerd datatype, Data-element, Enumeratie, Enumeratiewaarde, Referentielijst, Referentie-element, Codelijst |
| Overig | Constraint, Keuze, Relatierol (bron, doel), Externe koppeling |
| Packages | Package, Informatiemodel, Domein, Extern, View |

Elk heeft een eigen bestand in `modelelementen/`. Objecten en gegevens zijn **geen** modelelementen (noten bij §2.3.1.1 en §2.3.1.2).

Metagegevens erven niet over via generalisatie; ze horen bij elk modelelement apart (§2.4.3, inleiding). Het metagegeven Identificatie geldt voor alle modelelementen (§2.4.2.2).

## 3. Uitdrukking in UML en Linked Data

| | UML | Linked Data |
|---|---|---|
| Uitdrukking | geen eigen stereotype; elk concreet modelelement heeft een stereotype op een UML-metaclass (§3.1) | `mim:Modelelement` (abstracte klasse, §6.4.4.1) |

## 4. Metagegevens en bindingen

Modelelement heeft geen eigen metagegevenstabel. Zie `metagegevens.md`.

## Zie ook

- `metagegevens.md`, `woordenlijst.md`
- Letterlijke tekst: `python3 scripts/mim.py paragraaf 2.2 --met-sub`
