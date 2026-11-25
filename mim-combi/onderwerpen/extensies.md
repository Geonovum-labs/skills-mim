---
id: extensies
titel: Extensies op MIM
bron: ["1.10", "2.1", "2.4.1.5", "3.3.2", "5.14"]
mim-versie: "1.2"
status: normatief
---

# Extensies

**In het kort.** Een organisatie mag MIM uitbreiden met een eigen extensie, bijvoorbeeld met extra metagegevens of een extra modelelement. Een extensie mag niets in MIM vervangen of anders laten werken: uitbreiden mag, afwijken niet. Een extensie mag wel zeggen welke MIM-onderdelen het eigen model níet gebruikt.

## Wat MIM zegt

> De spelregel bij een extensie is dat deze geen onderwerpen vervangt die in dit metamodel beschreven zijn, maar alleen echte uitbreidingen omvat.
>
> — MIM 1.2, §1.10 (normatief)

> Het is ook mogelijk om in de extensie aan te geven welke elementen uit dit metamodel _niet_ ingezet worden in een informatiemodel.
>
> — MIM 1.2, §1.10 (normatief)

> Een extensie wordt door een domein zelf en dus buiten MIM beheerd.
>
> — MIM 1.2, §1.10 (normatief)

> Een metamodelextensie is expliciet niet bedoeld voor aanvullende constructies die alleen spelen op het niveau van implementatie, of op het niveau van afgeleide technische modellen t.b.v. specifieke interfaces.
>
> — MIM 1.2, §1.10 (niet-normatief, noot)

## Wat je in een extensie vastlegt (eigen samenvatting, met vindplaats)

- extra modelelementen of metagegevens (§1.10);
- welke MIM-elementen of -metagegevens buiten scope zijn, bijvoorbeeld stelselcatalogus-metadata als het model geen basisregistratie is (§1.10, §5.14);
- extra primitieve datatypen (§5.1.1);
- eigen naamgevingsconventies (§5.15.5, §6.2);
- conventies voor historie-metagegevens, zoals "zie modelelement naam" (§5.8.4);
- een relatieklasse tussen drie of meer objecttypen (§5.6).

Het metagegeven MIM-extensie van het informatiemodel noemt de gebruikte extensie, bijvoorbeeld `Kadaster` of `NEN3610:2022` (§2.4.1.5).

In UML: het MIM-profiel in Enterprise Architect mag je uitbreiden, niet wijzigen (§3.3.2).

## Buiten de scope van deze kennisbank

Versie 1 van mim-kennis beschrijft alleen de kern van MIM 1.2. Bestaande extensies, zoals die van het Kadaster en NEN 3610, staan hier niet in. Vraagt iemand naar de inhoud van een extensie, meld dan dat de kennisbank die niet bevat.

## Zie ook

- `modelelementen/modelelement.md` (uitgangspunt "uitbreiden mag, afwijken niet")
- Letterlijke tekst: `python3 scripts/mim.py paragraaf 1.10`
