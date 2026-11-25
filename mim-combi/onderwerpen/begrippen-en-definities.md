---
id: begrippen-en-definities
titel: Begrippen, definities en de stelselcatalogus
bron: ["5.16", "5.16.1", "5.16.2", "5.16.3", "1.6.1", "2.4.3.3", "2.4.3.5", "5.14", "1.13"]
mim-versie: "1.2"
status: normatief
---

# Begrippen en definities

**In het kort.** Een begrip (niveau 1) en een modelelement (niveau 2 of 3) zijn niet hetzelfde. Met het metagegeven Begrip verwijs je vanuit een modelelement naar het begrip waar het een invulling van is, met een term of een URI. De definitie van het modelelement kan preciezer zijn dan die van het begrip.

## Metagegeven Begrip

> Verwijzing naar een begrip, vanuit een modelelement, waarmee wordt aangegeven op welk begrip, of begrippen, het informatiemodel element is gebaseerd. De verwijzing heeft de vorm van een term of een URI.
>
> — MIM 1.2, §2.4.3.3 (normatief)

Eigen uitleg. De verwijzing betekent dat het modelelement een invulling op informatiemodelniveau is van het begrip, niet dat ze "iets met elkaar te maken hebben" (§5.16). Een URI verwijst naar een `skos:Concept` (§5.16.1). Begrip mag later worden toegevoegd; leeg betekent "niet bekend of er een begrip is" (§5.16).

**Nul, één of meer begrippen.** Niet elk modelelement is een begrip; bij datatypen is het vaak niet zinvol (§5.16.2). Wees precies: als het begrippenkader Natuurlijk persoon en Niet natuurlijk persoon kent en het model alleen Persoon met een attribuutsoort "type persoon", dan hoort de verwijzing naar Natuurlijk persoon bij die attribuutsoort, of nog preciezer bij de waarde ‘NP’ (§5.16.2).

## Definitie van modelelement en begrip

> De definitie van het modelelement is niet hetzelfde bedoeld als de definitie van een begrip.
>
> — MIM 1.2, §5.16.3 (normatief)

Bij een één-op-één relatie is het wel verstandig de definities op elkaar af te stemmen (§5.16.3). Een definitie mag een URI naar een gepubliceerde definitie bevatten, maar let op: verandert die externe definitie, dan klopt je model misschien niet meer (§5.16.3).

Zie ook §1.6.5: de definitie in het informatiemodel moet soms preciezer zijn dan die van het begrip.

## Stelselcatalogus (basisregistraties)

MIM ondersteunt de metadata voor de stelselcatalogus en de stelselafspraken. Voor basisregistraties zijn ze verplicht; andere modellen mogen ze in een eigen extensie buiten scope plaatsen (§5.14). In de UML-tabellen staat `√` bij metagegevens volgens de stelselafspraken en `*` bij die volgens de stelselcatalogus (§3.2).

| Stelselcatalogus | In MIM? | Waardebereik gelijk? |
|---|---|---|
| Naam, Definitie, Toelichting, Populatie, Kwaliteit | ja | ja |
| Herkomst | ja | ja, met aanvullende afspraken |
| Authentiek | ja | nee, met vertaling: `Authentiek` → Ja, anders Nee |
| Relatie, Wetgeving, Eigenaar, Toegankelijkheid, Gebruiksvoorwaarden | nee | n.v.t. |

Bron: §5.14 en §5.14.1.

Bij tegenstrijdige afspraken in de normreferenties geldt: eerst de Stelselcatalogus, dan het GAB, dan de NORA-handreiking (§1.13).

## Zie ook

- `onderwerpen/beschouwingsniveaus.md`, `onderwerpen/naamgeving.md`
- Letterlijke tekst: `python3 scripts/mim.py paragraaf 5.16 --met-sub`
