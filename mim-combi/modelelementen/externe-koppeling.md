---
id: externe-koppeling
titel: Externe koppeling
metaclass: Externe koppeling
bron: ["2.3.3.4", "3.1.3.4", "3.2.2.8", "4.3.2.8", "6.4.5.8", "5.13"]
mim-versie: "1.2"
status: normatief
---

# Externe koppeling

**In het kort.** Een externe koppeling is een relatie van een objecttype in het eigen informatiemodel naar een objecttype dat in een ander informatiemodel is gedefinieerd. De relatie hoort bij het eigen objecttype.

## 1. Definitie

> Een associatie waarmee vanuit het perspectief van het eigen informatiemodel een objecttype uit het ‘eigen’ informatiemodel gekoppeld wordt aan een objecttype van een extern informatiemodel. De relatie zelf hoort bij het ‘eigen’ objecttype.
>
> — MIM 1.2, §2.3.3.4 (normatief)

## 2. Uitleg

Eigen uitleg. Het woord "associatie" in de definitie betekent hier "verband"; het is niet de UML-betekenis van association (U15). Een externe koppeling wordt gebruikt samen met een view of extern package waarin het externe objecttype staat.

> Bij registraties is het regelmatig noodzakelijk om te verwijzen vanuit het eigen model naar gegevens uit een andere informatiemodel. Denk aan het opnemen van de identificatie van een object uit een andere registratie, of aan het overnemen van een subset van gegevens van een object uit een ander model. Hiervoor zijn de stereotypes «view» en «externe koppeling» bedoeld.
>
> — MIM 1.2, §5.13 (normatief)

Wanneer is het **geen** externe koppeling? Als je alleen de unieke aanduiding van het externe object opneemt (bijvoorbeeld het BSN), zonder gegevens over te nemen. Dat noemt MIM een referentie (§5.13, voorbeeld).

Het aggregatietype van de externe koppeling in het IMKAD-voorbeeld is volgens MIM "altijd Composite" (§5.13). Het waardebereik van Aggregatietype heet in MIM 1.2 `Compositie` (§2.4.5.1).

## 3. Uitdrukking in UML en Linked Data

| | UML | Linked Data |
|---|---|---|
| Uitdrukking | stereotype «Externe koppeling» op een (UML) Association; in EA: Association (§3.1.3.4) | `mim:ExterneKoppeling` (§4.2.3.4) |
| Metagegevens | §3.2.2.8 | §4.3.2.8 |
| Transformatie naar RDFS/OWL/SHACL | | `sh:PropertyShape` en `owl:ObjectProperty` (§6.4.4.1, §6.4.5.8) |

## 4. Metagegevens en bindingen

Lees de tabel zoals beschreven in `metagegevens.md` (paragraaf "Zo lees je de tabellen").

<!-- BEGIN GEGENEREERD: metagegevens externe-koppeling -->
| Metagegeven | Betekenis | UML | LD | Verplicht | Verschil UML/LD |
|---|---|---|---|---|---|
| Identificatie | §2.4.2.2 | `1` (§3.2.2.8) | `1` (§4.3.2.8) | verplicht |  |
| Naam | §2.4.3.1 | `1` (§3.2.2.8) | `1` (§4.3.2.8) | verplicht |  |
| Alias | §2.4.3.2 | `0..1` (§3.2.2.8) | `0..1` (§4.3.2.8) | optioneel |  |
| Herkomst | §2.4.3.4 | `1` (§3.2.2.8) | `1` (§4.3.2.8) | verplicht |  |
| Begrip | §2.4.3.3 | `0..*` (§3.2.2.8) | `0..*` (§4.3.2.8) | optioneel |  |
| Definitie | §2.4.3.5 | `1` (§3.2.2.8) | `1` (§4.3.2.8) | verplicht |  |
| Herkomst definitie | §2.4.3.6 | `1` (§3.2.2.8) | `1` (§4.3.2.8) | verplicht |  |
| Toelichting | §2.4.3.7 | `0..1` (§3.2.2.8) | `0..1` (§4.3.2.8) | optioneel |  |
| Datum opname | §2.4.3.8 | `1` (§3.2.2.8) | `1` (§4.3.2.8) | verplicht |  |
| Unidirectioneel | §2.4.3.22 | `1` (§3.2.2.8) | `1` (§4.3.2.8) | verplicht |  |
| Bron | §2.4.3.20 | `1` (§3.2.2.8) | `1` (§4.3.2.8) | verplicht |  |
| Doel | §2.4.3.21 | `1` (§3.2.2.8) | `1` (§4.3.2.8) | verplicht |  |
| Aggregatietype | §2.4.3.23 | `1` (§3.2.2.8) | `1` (§4.3.2.8) | verplicht |  |
| Kardinaliteit | §2.4.3.14 | `1` (§3.2.2.8) | `1` (§4.3.2.8) | verplicht |  |
| Kardinaliteit relatie bron | §2.4.3.15 | `1` (§3.2.2.8) | - | verplicht | ja |
| Indicatie materiële historie | §2.4.3.11 | `1` (§3.2.2.8) | `1` (§4.3.2.8) | verplicht |  |
| Indicatie formele historie | §2.4.3.13 | `1` (§3.2.2.8) | `1` (§4.3.2.8) | verplicht |  |
| Authentiek | §2.4.3.16 | `1` (§3.2.2.8) | `1` (§4.3.2.8) | verplicht |  |
| Indicatie afleidbaar | §2.4.3.17 | `1` (§3.2.2.8) | `1` (§4.3.2.8) | verplicht |  |
| Mogelijk geen waarde | §2.4.3.19 | `1` (§3.2.2.8) | `1` (§4.3.2.8) | verplicht |  |
| verwijst naar relatiedoel | - | `0..*` (§3.2.2.8) | - | optioneel | ja |
| heeft constraint | §2.4.4.17 | `0..*` (§3.2.2.8) | `0..*` (§4.3.2.8) | optioneel |  |
| Begripsterm | - | - | `0..*` (§4.3.2.8) | optioneel | ja |
| heeft tijdlijn geldigheid | §2.4.3.10 | - | `1` (§4.3.2.8) | verplicht | ja |
| heeft tijdlijn registratie | §2.4.3.12 | - | `1` (§4.3.2.8) | verplicht | ja |
<!-- EINDE GEGENEREERD -->

Eigen uitleg bij de tabel: net als bij de relatieklasse noemt de UML-tabel alleen de oude historie-metagegevens en de LD-tabel ook de nieuwe. Het relatiemodelleringstype (relatiesoort of relatierol leidend) geldt in het verlengde ook voor de externe koppeling (§2.4.1.3).

## 5. Voorbeeld en tegenvoorbeeld

**Voorbeeld uit MIM.**

> In IMKAD zit het objecttype: «Objecttype» Persoon. Hierin zitten de attributen waarvan de basisregistratie Kadaster de gegevens zelf inwint. In IMKAD zit het package: «view» BRP en hierin zit het «Objecttype» GeregistreerdPersoon. Hierin zitten de attributen die de basisregistratie BRP inwint en die het Kadaster overneemt.
>
> — MIM 1.2, §5.13 (niet-normatief, voorbeeld)

De relatie van Persoon naar GeregistreerdPersoon is de externe koppeling.

**Tegenvoorbeeld uit MIM.** Alleen het BSN opnemen, zonder BRP-gegevens over te nemen, is geen externe koppeling maar een referentie (§5.13).

## 6. Wordt vaak verward met

- **Relatiesoort.** Binnen het eigen model. Zie `onderscheidingen/relatiesoort-externe-koppeling-view-extern.md`.
- **View** en **Extern.** Dat zijn packages, geen relaties. Zie hetzelfde bestand.

## Zie ook

- `modelelementen/view.md`, `modelelementen/extern.md`
- Letterlijke tekst: `python3 scripts/mim.py paragraaf 5.13`
