# mim-kennis — leesmij voor beheerders

Kennisbank over MIM 1.2 (vastgestelde versie 13 juni 2024), verpakt als Claude-skill. Agents beginnen bij `SKILL.md`; dit bestand is voor wie de kennisbank bijhoudt.

- Versie: 0.1.0, status **concept** (23 november 2026). Doelversie volgens U23: `mim-kennis 1.0 (MIM 1.2)`.
- Eigenaar: Mats Braster (Geonovum).
- Uitgangspunten, besluiten en voortgang: in het Claude-project "MIM kennis skills" (projectdocumenten uitgangspunten.md en overdracht.md) en het logboek (Claude Doc).

## Opbouw

```
mim-kennis/
├── SKILL.md                     instructies voor de agent (grondregels, leesroute, antwoordsjabloon)
├── modelelementen/   (26)       één bestand per MIM-metaclass
├── metagegevens.md              betekenis, waardebereik, defaults; definities per metagegeven
├── onderwerpen/      (11)       beschouwingsniveaus, historie, keuze, waardelijsten, naamgeving, …
├── onderscheidingen/ (7)        X of Y: vergelijkingen en beslisvragen
├── uitdrukkingen/               uml.md, linked-data.md
├── versies.md                   MIM 1.1.1 → 1.2
├── bekende-onduidelijkheden.md  I1–I19 en redactionele fouten, met voorlopige lezing
├── woordenlijst.md              gegenereerd uit data/woordenlijst.json
├── bron/                        letterlijke MIM 1.2-tekst per hoofdstuk + paragrafen.json
├── data/                        elementen, metagegevens (json + csv), waardebereik, woordenlijst
├── scripts/                     mim.py (opzoeken), check_kennisbank.py (controle)
├── assets/                      mim.ttl, mim-shapes.ttl (uit de werkbron)
└── beheer/                      schrijfwijzer, sjablonen, bouwscripts (niet in het skillpakket)
```

## Controleren

```bash
python3 scripts/check_kennisbank.py
```

Controleert onder meer of elk letterlijk citaat woordelijk in de genoemde MIM-paragraaf staat, of elke `§`-verwijzing bestaat, of links kloppen, of de gegenereerde tabellen gelijk zijn aan de data en of `SKILL.md` onder 500 regels blijft. Draai dit na elke wijziging.

## Herbouwen

Alles wat gegenereerd is (map `bron/`, de bestanden in `data/`, `woordenlijst.md` en de blokken `<!-- BEGIN GEGENEREERD … -->`) bouw je opnieuw met:

```bash
python3 beheer/bouw/bouw_alles.py <pad>/MIM-Werkomgeving/DEF-mim-20240613.html
```

Nodig: Python 3.8+ en `beautifulsoup4` (alleen voor het omzetten van de HTML). Het script eindigt met de controle. Herbouwen op dezelfde bron geeft geen verschillen.

## Verpakken

```bash
python3 beheer/verpak.py <uitvoermap>
```

Maakt `mim-kennis.skill` (een zip van deze map zonder `beheer/` en zonder caches) en draait eerst de controle.

## Bij een nieuwe MIM-versie

1. Haal de nieuwe vastgestelde HTML op en draai `bouw_alles.py`.
2. Lees de controle-uitvoer: citaten die niet meer kloppen wijzen naar gewijzigde tekst.
3. Pas `beheer/bouw/maak_elementen.py` en `maak_waardebereik.py` aan als paragraafnummers of waarden zijn veranderd.
4. Werk `versies.md` en `bekende-onduidelijkheden.md` bij.
5. Pas `mim-versie` in de frontmatter en de versie in `SKILL.md` aan.

## Schrijfregels

Zie `beheer/schrijfwijzer.md`. Kern: letterlijke tekst alleen in een blockquote die eindigt op `— MIM 1.2, §<nr> (normatief)` of `(niet-normatief, …)`; al het andere is eigen uitleg.

## Licenties

- MIM-tekst (map `bron/` en alle citaten): CC BY 4.0, © Geonovum. Bron: <https://docs.geostandaarden.nl/mim/def-st-mim-20240613/>.
- `assets/mim.ttl` en `assets/mim-shapes.ttl`: uit Geonovum/MIM-Werkomgeving.
- Eigen tekst en scripts: EUPL-1.2 (voorstel, in lijn met de Geonovum-skillrepo's; nog te bevestigen).
