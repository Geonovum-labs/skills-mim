---
id: informatiemodel
titel: Informatiemodel
metaclass: Informatiemodel
bron: ["2.3.6.1", "2.4.1", "2.4.2.1", "3.2.5.3", "4.3.5.1", "1.5", "1.6"]
mim-versie: "1.2"
status: normatief
---

# Informatiemodel

**In het kort.** Het modelelement Informatiemodel is het hoofdpackage: het model als geheel. Hier staan de metagegevens die voor het hele model gelden, zoals of het model conceptueel of logisch is en welke MIM-versie het volgt.

## 1. Definitie

> De groepering van alle modelelementen waaruit het informatiemodel is opgebouwd. Het informatiemodel als geheel.
>
> — MIM 1.2, §2.3.6.1 (normatief)

## 2. Uitleg

> Het informatiemodel is een package, te weten het hoofdpackage van het informatiemodel, waar alle subpackages die een informatiemodel beschrijven onder vallen, zoals Domein en View en extern.
>
> — MIM 1.2, §2.3.6.1 (normatief)

Eigen uitleg. Dit bestand gaat over het **modelelement** Informatiemodel. Wat een informatiemodel als begrip is (en wat beschouwingsniveaus zijn) staat in `onderwerpen/beschouwingsniveaus.md` (§1.5, §1.6).

Specifieke metagegevens van het informatiemodel (§2.4.1, §2.4.2):

| Metagegeven | Verplicht | Waarden of voorbeeld |
|---|---|---|
| Informatiedomein | ja | bijvoorbeeld BRK |
| Informatiemodeltype | ja | `Conceptueel` of `Logisch` |
| Relatiemodelleringstype | ja | `Relatiesoort leidend` of `Relatierol leidend` |
| MIM-versie | ja | bijvoorbeeld `1.2` |
| MIM-extensie | nee | bijvoorbeeld `Kadaster` of `NEN3610:2022` |
| MIM-taal | nee | bijvoorbeeld `NL` |
| Tekstopmaak | nee | bijvoorbeeld `html`; geldt voor definities en toelichtingen |
| Basis-URI | volgens §2.4.2.1 verplicht; in de tabellen `0..1` | bij ontbreken een default `urn:modelelement:` + naam |

Informatiemodeltype is belangrijk: een model is altijd óf conceptueel óf logisch, nooit een mengvorm (§1.6.5).

## 3. Uitdrukking in UML en Linked Data

| | UML | Linked Data |
|---|---|---|
| Uitdrukking | stereotype «Informatiemodel» op een (UML) Package (§3.1.3.5) | `mim:Informatiemodel` (§4.2.3.5) |
| Metagegevens | §3.2.5.3 | §4.3.5.1 |

## 4. Metagegevens en bindingen

Lees de tabel zoals beschreven in `metagegevens.md` (paragraaf "Zo lees je de tabellen").

<!-- BEGIN GEGENEREERD: metagegevens informatiemodel -->
| Metagegeven | Betekenis | UML | LD | Verplicht | Verschil UML/LD |
|---|---|---|---|---|---|
| Identificatie | §2.4.2.2 | `1` (§3.2.5.3) | `1` (§4.3.5.1) | verplicht |  |
| Naam | §2.4.3.1 | `1` (§3.2.5.3) | `1` (§4.3.5.1) | verplicht |  |
| Alias | §2.4.3.2 | `0..1` (§3.2.5.3) | `0..1` (§4.3.5.1) | optioneel |  |
| Herkomst | §2.4.3.4 | `1` (§3.2.5.3) | `1` (§4.3.5.1) | verplicht |  |
| Definitie | §2.4.3.5 | `1` (§3.2.5.3) | `1` (§4.3.5.1) | verplicht |  |
| Herkomst definitie | §2.4.3.6 | `1` (§3.2.5.3) | - | verplicht | ja |
| Toelichting | §2.4.3.7 | `0..1` (§3.2.5.3) | - | optioneel | ja |
| Datum opname | §2.4.3.8 | `1` (§3.2.5.3) | `1` (§4.3.5.1) | verplicht |  |
| Informatiemodeltype | §2.4.1.2 | `1` (§3.2.5.3) | `1..1` (§4.3.5.1) | verplicht |  |
| Informatiedomein | §2.4.1.1 | `1` (§3.2.5.3) | `1..1` (§4.3.5.1) | verplicht |  |
| MIM-versie | §2.4.1.4 | `1` (§3.2.5.3) | `1` (§4.3.5.1) | verplicht |  |
| MIM-extensie | §2.4.1.5 | `0..1` (§3.2.5.3) | `0..1` (§4.3.5.1) | optioneel |  |
| MIM-taal | §2.4.1.6 | `0..1` (§3.2.5.3) | `0..1` (§4.3.5.1) | optioneel |  |
| Relatiemodelleringstype | §2.4.1.3 | `1` (§3.2.5.3) | `1..1` (§4.3.5.1) | verplicht |  |
| Tekstopmaak | §2.4.1.7 | `0..1` (§3.2.5.3) | `0..1` (§4.3.5.1) | optioneel |  |
| heeft constraint | §2.4.4.17 | `0..*` (§3.2.5.3) | `0..*` (§4.3.5.1) | optioneel |  |
| Basis-URI | §2.4.2.1 | `0..1` (§3.2.5.3) | `0..1` (§4.3.5.1) | optioneel |  |
| bevat modelelement | §2.4.4.9 | `0..*` (§3.2.5.3) | - | optioneel | ja |
<!-- EINDE GEGENEREERD -->

Eigen uitleg bij de tabel: de LD-tabel (§4.3.5.1) gebruikt voor MIM-versie, -extensie en -taal de eigenschappen `mim:mimversie`, `mim:mimextensie` en `mim:mimtaal` (zoals de vocabulaire). De overzichtstabel in §4.3 noemt `mim:versie`, `mim:extensie` en `mim:taal`. Zie `bekende-onduidelijkheden.md`.

## 5. Voorbeeld en tegenvoorbeeld

**Voorbeeld uit MIM.**

> Voorbeeld: IMKAD, of IMBAGLV. Elk van deze is een naam van een informatiemodel.
>
> — MIM 1.2, §2.3.6.1 (niet-normatief, voorbeeld)

Het is gangbaar, maar niet verplicht, om de naam met IM te laten beginnen (§2.3.6.1).

**Tegenvoorbeeld (eigen voorbeeld).** Een model met het Informatiemodeltype `Conceptueel` dat begin- en einddatum-attributen voor historie bevat, mengt niveaus: tijdlijnattributen horen op logisch niveau (§5.8.2).

## Zie ook

- `onderwerpen/beschouwingsniveaus.md`, `onderwerpen/relatiemodellering.md`
- Letterlijke tekst: `python3 scripts/mim.py paragraaf 2.4.1 --met-sub`
