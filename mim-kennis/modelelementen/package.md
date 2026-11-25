---
id: package
titel: Package
metaclass: Package
bron: ["2.3.6", "2.2.4.4", "4.2.3.5", "2.4.4.9"]
mim-versie: "1.2"
status: normatief
---

# Package

**In het kort.** Een package is een map waarin modelelementen worden gegroepeerd. MIM kent vier soorten: Informatiemodel (de hoofdmap), Domein, Extern en View.

## 1. Definitie

> Een benoemde en begrensde verzameling/groepering van modelelementen.
>
> — MIM 1.2, §2.3.6 (normatief)

## 2. Uitleg

> In een informatiemodel package mogen alleen domein of view packages opgenomen worden. Beide kunnen meertallig voorkomen en de volgorde is hierbij niet van belang. Een extern package bevindt zich buiten het package informatiemodel.
>
> — MIM 1.2, §2.3.6 (normatief)

In een domein-, view- of extern-package mogen volgens §2.3.6 alleen deze elementen staan: Objecttype, Gegevensgroeptype, Datatype (alle varianten), Relatieklasse en Keuze. De volgorde is niet van belang.

Eigen uitleg. Package zelf is abstract; in een model gebruik je de vier soorten:

| Soort | Waarvoor | Bestand |
|---|---|---|
| Informatiemodel | het model als geheel, hoofdpackage | `modelelementen/informatiemodel.md` |
| Domein | een samenhangend deel van het eigen model | `modelelementen/domein.md` |
| Extern | ongewijzigd overgenomen elementen van een externe beheerder | `modelelementen/extern.md` |
| View | de voor het eigen model relevante deelverzameling uit een extern model | `modelelementen/view.md` |

De binding tussen een package en zijn inhoud heet "bevat modelelement" (§2.4.4.9); die is in MIM 1.2 toegevoegd (versielog, issue 450).

## 3. Uitdrukking in UML en Linked Data

| | UML | Linked Data |
|---|---|---|
| Uitdrukking | (UML) Package met het stereotype van de soort (§3.1.3.5) | `mim:Package` (abstract) en de vier soorten (§4.2.3.5) |
| Transformatie naar RDFS/OWL/SHACL | | abstracte klasse, niet getransformeerd (§6.4.4.1) |

## 4. Metagegevens en bindingen

Package heeft geen eigen metagegevenstabel. Zie de tabellen bij de vier soorten.

## 5. Voorbeeld en tegenvoorbeeld

**Eigen voorbeeld.** Informatiemodel IMBAGLV met de domeinpackages "Objecten" en "Waardelijsten", en een externe package NEN3610.

**Tegenvoorbeeld uit MIM.** Een attribuutsoort of relatiesoort staat niet los in een package, maar hoort bij een objecttype of gegevensgroeptype (zie de lijst hierboven).

## Zie ook

- Letterlijke tekst: `python3 scripts/mim.py paragraaf 2.3.6 --met-sub`
