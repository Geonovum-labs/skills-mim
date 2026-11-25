---
id: historie
titel: Historie
bron: ["5.8", "5.8.1", "5.8.2", "5.8.3", "5.8.4", "2.4.3.10", "2.4.3.11", "2.4.3.12", "2.4.3.13"]
mim-versie: "1.2"
status: normatief
---

# Historie

**In het kort.** MIM kent twee tijdlijnen. De **tijdlijn geldigheid** zegt wanneer iets in de werkelijkheid zo was. De **tijdlijn registratie** zegt wanneer het in de administratie is vastgelegd. In een conceptueel model geef je per attribuutsoort of relatie alleen aan óf die tijdlijnen gelden (Ja/Nee). Hoe je ze implementeert, schrijft MIM niet voor.

## Twee tijdlijnen

> - Wanneer is iets gebeurd, in de werkelijkheid of volgens opgave (wanneer zijn de opgenomen gegevens geldig)? Dit valt binnen de tijdlijn van de aangehouden werkelijkheid, zoals bepaald door een bevoegd gezag (een partij die erover gaat).
> - Vanaf wanneer wist de overheid (als collectief van organisaties) dat de gegevens bekend waren? Dit valt binnen de tijdlijn van het administratieproces of de administratieve werkelijkheid. Op welke moment zijn de gegevens registreerd.
>
> — MIM 1.2, §5.8.1 (normatief)

## Metagegevens (nieuw en oud)

| MIM 1.2 | Gelijkwaardig aan (oude naam) | Waarden | Default |
|---|---|---|---|
| heeft tijdlijn geldigheid (§2.4.3.10) | Indicatie materiële historie (§2.4.3.11) | `Ja`, `Nee` | `Nee` |
| heeft tijdlijn registratie (§2.4.3.12) | Indicatie formele historie (§2.4.3.13) | `Ja`, `Nee` | `Nee` |

De oude namen blijven in MIM 1.x bestaan voor compatibiliteit en vervallen vanaf MIM 2.x (noten bij §2.4.3.11 en §2.4.3.13). Ze gelden voor attribuutsoorten en relaties (relatiesoort, relatieklasse, externe koppeling); niet meer voor een gegevensgroep (versielog, issue 224).

## Conceptueel niveau

> Merk op: de _heeft tijdlijn geldigheid_ geeft op conceptueel niveau niet aan dat er voor het gegeven een tijdlijn geldigheid wordt bijgehouden in de administratie. Het geeft aan _dat een eigenschap_ kan veranderen en er op de tijdlijn geldigheid verschillende waarden kunnen bestaan (op verschillende momenten).
>
> — MIM 1.2, §5.8.2 (normatief)

> Richtlijn: op conceptueel niveau worden voor historie alléén heeft tijdlijn geldigheid en heeft tijdlijn registratie bij een attribuut of relatie vastgelegd. De attributen waaruit de tijdlijnen zelf bestaan (zoals bijvoorbeeld: 'begin geldigheid' en 'eind geldigheid' en 'begin registratie' en 'eind registratie') worden niet gemodelleerd in een conceptueel informatiemodel.
>
> — MIM 1.2, §5.8.2 (normatief)

Voorbeelden uit MIM (§5.8.2, voorbeeld): bouwjaar van een pand en geboortedatum van een mens kunnen in de werkelijkheid niet veranderen, dus heeft tijdlijn geldigheid = `Nee`. Achternaam en woonadres kunnen veranderen, dus `Ja`. Tijdlijn registratie staat "vrijwel altijd op Ja", behalve als alleen de actuele situatie nodig is.

## Logisch niveau

> MIM schrijft geen implementatie van het logische niveau voor.
>
> — MIM 1.2, §5.8.3 (normatief)

Eigen samenvatting van de aandachtspunten in §5.8.3 (niet bindend): specifieke of generieke tijdlijnattributen; historie per attribuut of per versie van een object; statusovergangen; statusattributen over gegevens. Een correctie van een gegeven dat in werkelijkheid niet kan veranderen (zoals een foute geboortedatum) geldt met terugwerkende kracht op de tijdlijn geldigheid en krijgt een nieuw moment op de tijdlijn registratie.

> Opmerking: de metagegevens heeft tijdlijn geldigheid en heeft tijdlijn geldigheid mogen worden opgenomen in een logisch model (mogen worden overgenomen van het conceptuele naar het logische informatiemodel).
>
> — MIM 1.2, §5.8.3 (normatief)

(In dit citaat staat twee keer "geldigheid"; bedoeld is waarschijnlijk geldigheid en registratie. Zie `bekende-onduidelijkheden.md`.)

## Veelgemaakte fouten (eigen uitleg)

- "heeft tijdlijn geldigheid = Ja" lezen als "de registratie houdt begin- en einddatum bij". Op conceptueel niveau betekent het alleen dat het kenmerk kan veranderen (§5.8.2).
- Begin- en einddatum-attributen in een conceptueel model opnemen (§5.8.2).
- Historie per data-element van een gestructureerd datatype willen bijhouden; dat is meestal niet zinvol (§2.3.1.2).

## Zie ook

- `metagegevens.md`
- Letterlijke tekst: `python3 scripts/mim.py paragraaf 5.8 --met-sub`
