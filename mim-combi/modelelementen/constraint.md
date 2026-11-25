---
id: constraint
titel: Constraint
metaclass: Constraint
bron: ["2.3.7.1", "2.2.4.1", "3.1.3.1", "3.2.6.1", "4.3.6.3", "6.4.8.1", "5.7", "2.4.4.17"]
mim-versie: "1.2"
status: normatief
---

# Constraint

**In het kort.** Een constraint is een extra regel die je niet met de gewone modelelementen kunt uitdrukken, bijvoorbeeld "minstens één van deze twee velden is gevuld". Een constraint staat altijd in gewone tekst en kan daarnaast formeel (in OCL) worden vastgelegd.

## 1. Definitie

> Een conditie of een beperking, die voor één of meerdere modelelementen uit het informatiemodel geldt.
>
> — MIM 1.2, §2.3.7.1 (normatief)

## 2. Uitleg

> Een `Constraint` wordt opgenomen om een constructie uit te drukken die niet via bestaande modelelementen is uit te drukken.
>
> — MIM 1.2, §2.3.7.1 (normatief)

> Een `Constraint` wordt altijd in _gewone tekst_ omschreven en kan _optioneel als formele specificatie_ worden aangegeven.
>
> — MIM 1.2, §2.3.7.1 (normatief)

**Betrekken en vastleggen.** Een constraint kan gaan over het ene element (betrekken) en worden vastgelegd bij een ander (vastleggen):

> Zo kan een constraint die van toepassing is op toegestane waarden van een attribuutsoort vastgelegd worden bij het objecttype dat de attribuutsoort gebruikt.
>
> — MIM 1.2, §2.3.7.1 (normatief)

In MIM 1.2 mag een constraint op alle modelelementen worden toegepast (§2.2.4.1; versielog, issue 317). Twee constraints op hetzelfde modelelement mogen niet dezelfde naam hebben (§5.7).

**Aanbevelingen** (§5.7, eigen samenvatting):

1. Kan het met een patroon, lengte of kardinaliteit, gebruik dat en geen constraint.
2. Wees terughoudend met regels die vaak wijzigen of niet over semantiek, structuur of syntax gaan (zoals "wie 65 of ouder is, mag geen uitkering aanvragen"). Leg die buiten het model vast, bijvoorbeeld als validatieregel.

**Constraint of keuze?** Voor een aantal situaties is een keuze een betere manier dan een constraint, omdat de kardinaliteiten dan zuiver blijven (§2.3.7.2). Zie `onderscheidingen/keuze-vs-constraint.md`.

## 3. Uitdrukking in UML en Linked Data

| | UML | Linked Data |
|---|---|---|
| Uitdrukking | een (UML) Constraint zonder stereotype (tabel §3.1.3.1); in EA: Constraint | `mim:Constraint` (§4.2.3.1) |
| Metagegevens | §3.2.6.1 | §4.3.6.3 |
| Transformatie naar RDFS/OWL/SHACL | | blijft `mim:Constraint` (§6.4.4.1, §6.4.8.1) |

In UML: naam, "specificatie in tekst" (UML-Constraint Notes, type invariant) en optioneel "specificatie formeel" in OCL. In Enterprise Architect kunnen tekst en OCL niet in één constraint; dan worden het twee constraints met een andere naam, of OCL met de tekst als commentaar `/* … */` (§5.7).

## 4. Metagegevens en bindingen

Lees de tabel zoals beschreven in `metagegevens.md` (paragraaf "Zo lees je de tabellen").

<!-- BEGIN GEGENEREERD: metagegevens constraint -->
| Metagegeven | Betekenis | UML | LD | Verplicht | Verschil UML/LD |
|---|---|---|---|---|---|
| Naam | §2.4.3.1 | `1` (§3.2.6.1) | `1` (§4.3.6.3) | verplicht |  |
| Specificatie tekst | - | `0..1` (§3.2.6.1) | `0..1` (§4.3.6.3) | optioneel |  |
| Specificatie formeel | - | `0..1` (§3.2.6.1) | `0..1` (§4.3.6.3) | optioneel |  |
| Datum opname | §2.4.3.8 | `1` (§3.2.6.1) | - | verplicht | ja |
| van toepassing op (constraint) | - | `0..1` (§3.2.6.1) | - | optioneel | ja |
<!-- EINDE GEGENEREERD -->

Eigen uitleg bij de tabel: Specificatie tekst heeft in beide tabellen kardinaliteit `0..1`, terwijl §2.3.7.1 zegt dat een constraint "altijd in gewone tekst" wordt omschreven. Meld dit verschil als het ertoe doet.

## 5. Voorbeeld en tegenvoorbeeld

**Voorbeeld uit MIM.** Een elfproef op het datatype van een attribuutsoort (§2.3.7.1). En de constraint `idNummeraanduidingBAGEnOfLocatieomschrijving`: het adres via idNummeraanduidingBAG en/of de locatieomschrijving moet gevuld zijn (§5.7).

**Tegenvoorbeeld uit MIM.** "Precies één van betalingskenmerk of omschrijving" kun je met een constraint modelleren, maar MIM vindt een keuze daarvoor duidelijker (§2.3.7.2, use case 2).

## Zie ook

- `modelelementen/keuze.md`
- Letterlijke tekst: `python3 scripts/mim.py paragraaf 5.7`
