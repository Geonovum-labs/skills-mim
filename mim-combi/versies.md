---
id: versies
titel: Versieverschillen MIM 1.1.1 naar MIM 1.2
bron: ["6.5", "6.3", "2.4.3.11", "2.4.3.13", "3.2.4.4", "5.8"]
mim-versie: "1.2"
status: toelichtend
---

# Wat is er veranderd van MIM 1.1.1 naar MIM 1.2?

**In het kort.** MIM 1.2 (vastgesteld 13 juni 2024) voegt vooral metagegevens en verduidelijkingen toe: twee nieuwe historie-metagegevens (heeft tijdlijn geldigheid, heeft tijdlijn registratie), Eenheid, minimum- en maximumwaarden, Mixin, URI's voor modelelementen, een vijfde keuze-use case en constraints op alle modelelementen. Als verwijdering noemt de versielog alleen de historie-metagegevens bij een gegevensgroep (issue 224).

Deze kennisbank geldt alleen voor MIM 1.2. De versielog in MIM 1.2 (§6.5) is de bron; de indeling hieronder is eigen uitleg. Issuenummers verwijzen naar GitHub Geonovum/MIM-Werkomgeving.

## Inhoudelijke wijzigingen

| Onderwerp | Wijziging in 1.2 | Issue | Zie |
|---|---|---|---|
| Historie | nieuwe metagegevens heeft tijdlijn geldigheid en heeft tijdlijn registratie; gelijkwaardig aan Indicatie materiële/formele historie, die vervallen in MIM 2.x | 151 | `onderwerpen/historie.md` |
| Historie | historie-metagegevens bij Gegevensgroep verwijderd | 224 | `modelelementen/gegevensgroep.md` |
| Eenheid | nieuw metagegeven Eenheid (SI-stelsel) | 015 | `metagegevens.md` |
| Waardebereik | nieuwe metagegevens minimum- en maximumwaarde, inclusief en exclusief | 109 | `metagegevens.md` |
| Generalisatie | nieuw metagegeven Mixin, voor multiple inheritance op niveau 3 | 195 | `modelelementen/generalisatie.md` |
| Identificatie | URI van model en modelelementen (Basis-URI, Identificatie) | 188 | `metagegevens.md` |
| Packages | eenduidige beschrijving van packagetypen; nieuw metagegeven bevat modelelement | 431, 450 | `modelelementen/package.md` |
| Keuze | structuur van tekst en figuren aangepast; use case 5 (keuze tussen relatiesoorten) toegevoegd | 171, 190 | `onderwerpen/keuze.md` |
| Keuze | consistente namen keuzeattribuut en keuzerelatiedoel | 286 | `modelelementen/keuze.md` |
| Constraint | constraint toegestaan op alle modelelementen | 317 | `modelelementen/constraint.md` |
| Relatieklasse | beschrijving wanneer een relatieklasse een objecttype wordt; binding heeft gegevensgroep toegevoegd | 148, 305 | `onderscheidingen/relatieklasse-vs-objecttype.md` |
| Codelijst | definitie en toelichting aangepast; tekst Profielspecificatie aangepast | 253, 446 | `modelelementen/codelijst.md` |
| Definitie en toelichting | mogen rijke tekst bevatten (metagegeven Tekstopmaak) | 245 | `metagegevens.md` |
| Gestructureerd datatype | toelichting voor een gegeven uit meerdere "data-delen" (één gegevenselement) | 238 | `modelelementen/gestructureerd-datatype.md` |
| Definities | definities van Modelelement, Object en Gegeven aangepast | 425, 427, 428 | `modelelementen/modelelement.md` |
| Indicatie abstract object | toelichting, toepassing en transformatie aangepast | 288, 377, 378 | `onderwerpen/abstracte-objecttypen.md` |
| Populatie en Kwaliteit | beschrijving aangepast, voorbeelden toegevoegd | 201 | `metagegevens.md` |
| Linked Data | namespace `http://modellen.mim-standaard.nl/def/mim` overal doorgevoerd; betekenis `mim:locatie` consistent | 451, 289 | `uitdrukkingen/linked-data.md` |

## Redactionele wijzigingen (selectie)

Consistente schrijfwijze "datatypen" (314) en "waardelijst" (333), waarden van metagegevens (391), alle definities met een vaste opmaak (322), figuren met bijschriften (318), paragrafen over waardelijsten samengevoegd (310), naam en verwijzing van Alias in de LD-tabel (336). Bron: §6.5.

## Oude namen die je nog tegenkomt

| Oude naam | Naam in MIM 1.2 | Bron |
|---|---|---|
| Indicatie materiële historie | heeft tijdlijn geldigheid (beide bestaan in 1.x) | §2.4.3.11 |
| Indicatie formele historie | heeft tijdlijn registratie (beide bestaan in 1.x) | §2.4.3.13 |
| Keuze-element | vervallen sinds MIM 1.1; de opties van een keuze zijn gewoon datatypen, attribuutsoorten of relatiedoelen | §3.2.4.4 |
| Complex datatype | Gestructureerd datatype | §6.3 (kolom "MIM 1.1") |
| Gemeentelijk kerngegeven (waarde van Authentiek) | niet in het waardebereik van MIM 1.2; wel `Wettelijk gegeven` | §6.3, §2.4.5.1 |
| Indicatie authentiek | Authentiek | §6.3 |

## Vragen over andere versies

Vragen over MIM 1.0, 1.1, 1.1.1 in detail, of over MIM 2.x, kan deze kennisbank niet betrouwbaar beantwoorden. Zeg dat, en verwijs naar de publicaties op docs.geostandaarden.nl. De kennisbank weet alleen wat MIM 1.2 zelf over eerdere en latere versies zegt (de versielog, §6.3, en de noten over MIM 2.x bij §2.4.3.11 en §2.4.3.13).

## Zie ook

- Letterlijke tekst: `python3 scripts/mim.py paragraaf 6.5`
