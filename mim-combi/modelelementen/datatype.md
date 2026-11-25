---
id: datatype
titel: Datatype
metaclass: Datatype
bron: ["2.3.5.1", "2.1", "2.2.3", "3.1.1", "4.2.2", "5.1"]
mim-versie: "1.2"
status: normatief
---

# Datatype

**In het kort.** Een datatype beschrijft de vorm waaraan een waarde moet voldoen, bijvoorbeeld "een geheel getal" of "een bedrag met som en valuta". Een datatype zegt niets over betekenis: die staat in de attribuutsoort.

## 1. Definitie

> Een beschrijving van de structuur waaraan een waarde, oftewel de data zelf, aan moet voldoen.
>
> — MIM 1.2, §2.3.5.1 (normatief)

## 2. Uitleg

Een van de uitgangspunten van MIM:

> Datatypen zijn onderdeel van het metamodel en beschrijven de structuur van de data, maar niet de semantiek/betekenis. De aanbeveling is dan ook om eerst een informatiemodel te maken zonder datatypen. De regel is dat als alle datatypen uit het model worden weggelaten, er geen semantische betekenis verloren mag gaan.
>
> — MIM 1.2, §2.1 (normatief)

Eigen uitleg. Datatype is een abstract modelelement: in een model gebruik je altijd een concrete soort. MIM kent:

| Soort | Bestand |
|---|---|
| Primitief datatype | `modelelementen/primitief-datatype.md` |
| Gestructureerd datatype (met data-elementen) | `modelelementen/gestructureerd-datatype.md` |
| Enumeratie (met enumeratiewaarden) | `modelelementen/enumeratie.md` |
| Referentielijst (met referentie-elementen) | `modelelementen/referentielijst.md` |
| Codelijst | `modelelementen/codelijst.md` |
| Keuze tussen datatypen | `modelelementen/keuze.md` |

Een datatype wordt gebruikt als type van een attribuutsoort, data-element, referentie-element of keuze (binding "heeft datatype", §2.4.4.5). Datatypen zijn herbruikbaar op veel plekken (§2.3.5.1).

Extra beperkingen zoals lengte horen niet in het datatype zelf, maar in metagegevens van de attribuutsoort (§5.1). Welke primitieve datatypen MIM kent, staat in `onderwerpen/datatypen.md`.

## 3. Uitdrukking in UML en Linked Data

| | UML | Linked Data |
|---|---|---|
| Uitdrukking | geen eigen stereotype: Datatype is abstract en komt alleen voor in zijn concrete soorten (noot bij §3.1.1) | `mim:Datatype` (§4.2.2) |
| Transformatie naar RDFS/OWL/SHACL | | abstracte klasse, niet getransformeerd (§6.4.4.1) |

## 4. Metagegevens en bindingen

Datatype heeft geen eigen metagegevenstabel in §3.2 of §4.3. Zie de tabellen van de concrete soorten.

Let op: metagegevens erven niet over van Datatype naar de soorten. Een referentielijst heeft bijvoorbeeld geen Patroon (§2.4.3, inleiding).

## 5. Voorbeeld en tegenvoorbeeld

**Voorbeeld uit MIM.**

> Bijvoorbeeld: het `Type` van het kenmerk `geometrie` is het `«Datatype»` `VlakOfMultivlak`;
>
> — MIM 1.2, §2.4.3.28 (normatief)

**Tegenvoorbeeld (eigen voorbeeld).** Een datatype "Woonadres" met de betekenis "het adres waar iemand woont" is geen goed datatype: de betekenis hoort in de attribuutsoort of relatiesoort `woonadres`; het datatype beschrijft hooguit de structuur van een adres.

## 6. Wordt vaak verward met

- **Attribuutsoort.** Betekenis tegenover structuur.
- **Gegevensgroeptype.** Zie `onderscheidingen/gegevensgroep-vs-gestructureerd-datatype.md`.

## Zie ook

- `onderwerpen/datatypen.md`
- Letterlijke tekst: `python3 scripts/mim.py paragraaf 2.3.5.1`
