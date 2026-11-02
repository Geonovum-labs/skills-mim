# Disclaimer

De skills in deze repository zijn hulpmiddelen van [Geonovum](https://www.geonovum.nl) bij de standaard MIM (Metamodel Informatiemodellering). Hun status is **informatief**: ze maken geen deel uit van de standaard en hebben geen normatieve status.

## De skills zijn niet de standaard

Een skill is een samenvatting en een werkinstructie, niet de regel zelf. De officiële publicatie is altijd leidend:

- de standaard MIM 1.2 op [docs.geostandaarden.nl/mim/mim/](https://docs.geostandaarden.nl/mim/mim/), met per versie een persistente URI (vastgesteld 13 juni 2024: [def-st-mim-20240613](https://docs.geostandaarden.nl/mim/def-st-mim-20240613/));
- gepubliceerde informatiemodellen, waaronder RDF-modellen op [modellen.geostandaarden.nl](http://modellen.geostandaarden.nl) en HTML/PDF-catalogi van de modelbeheerder;
- de broncode van de standaard in [Geonovum/MIM-Werkomgeving](https://github.com/Geonovum/MIM-Werkomgeving).

Waar de interpret-skill vereenvoudigt of extra-standaard werk toevoegt (met name de mapping van een dataproduct naar modelelementen), staat dat in `mim-interpret/references/conflicts.md`. Bij twijfel of tegenstrijdigheid geldt de officiële, gepubliceerde versie van de standaard en van het betreffende informatiemodel.

De mapping van velden in een API of bestand naar modelelementen is **geen** onderdeel van MIM (data en beschouwingsniveau 4 vallen buiten MIM). Die mapping is extra-standaard werk van `geonovum-mim-interpret`. Het implementeren van een model in software is extra-standaard werk van `geonovum-mim-implement` (nog niet gebouwd).

## Geen conformiteitsverklaring

Een antwoord of mapping van deze skills is geen goedkeuring, aanbeveling of conformiteitsverklaring van Geonovum, Kadaster of een andere beheerder. Of data of een model MIM-conform is, bepaalt de standaard (en voor toetsing: Imvertor), niet deze skills. Wie op grond van een antwoord een besluit neemt, blijft daar zelf verantwoordelijk voor.

## Gebruik van generatieve AI

De skills worden uitgevoerd door AI-assistenten. Een antwoord kan daardoor onvolledig of onjuist zijn, ook als de skill zelf klopt. Of bij het schrijven van een skill generatieve AI is gebruikt, staat in het veld `nl.gov.generated-with` van die skill. Overheidsorganisaties die generatieve AI inzetten, ook via deze skills, dienen te voldoen aan het [Overheidsbreed standpunt voor de inzet van generatieve AI](https://open.overheid.nl/documenten/bc03ce31-0cf1-4946-9c94-e934a62ebe73/file) en aan eigen beleid en kaders over AI.

## Status en onderhoud

De status van elke skill staat in het veld `nl.gov.status` in de frontmatter van `SKILL.md`, met een herzieningsdatum in `nl.gov.review-by`. Een skill met status `concept` is nog niet vastgesteld. `mim-implement/` heeft geen `SKILL.md` en is geen laadbare skill.

## Privacy

Deze skills zijn niet bedoeld om persoonsgegevens op te vragen of te verwerken. Gegevens over objecten mogen alleen worden geïnterpreteerd voor zover het geen persoonsgegevens zijn. Adressen of objecten niet koppelen aan personen.

## Geen garantie

De inhoud wordt aangeboden zonder garantie van volledigheid, juistheid of actualiteit. Fouten en verbeteringen graag als issue in de later te publiceren repository `Geonovum/skills-mim`.
