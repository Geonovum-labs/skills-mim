---
id: mogelijk-geen-waarde
titel: Mogelijk geen waarde en kardinaliteit
bron: ["5.11", "2.4.3.19", "2.4.3.14"]
mim-versie: "1.2"
status: normatief
---

# Mogelijk geen waarde

**In het kort.** Of een kenmerk verplicht is (kardinaliteit) en of de waarde onbekend mag zijn (mogelijk geen waarde) zijn twee aparte vragen. Een geboortedatum is altijd verplicht, maar kan onbekend zijn: dan blijft de kardinaliteit `1` en wordt Mogelijk geen waarde `Ja`. Je maakt een verplicht kenmerk nooit optioneel omdat de waarde soms onbekend is.

## Definitie

> Aanduiding dat van een aspect geen waarde is geregistreerd, maar dat onduidelijk is of de waarde er werkelijk ook niet is.
>
> — MIM 1.2, §2.4.3.19 (normatief)

## Niet optioneel maken

> Verder, wanneer er sprake is van mogelijk geen waarde dan het is expliciet niet de bedoeling om een verplicht veld optioneel maken. Dit is niet de juiste oplossing en kan bovendien de indruk geven dat het veld niet relevant is.
>
> — MIM 1.2, §5.11 (normatief)

> Het ontbreken van een optionele waarde heeft daarom de betekenis dat het bekend is dat er in de betreffende situatie in de werkelijkheid geen waarde bestaat.
>
> — MIM 1.2, §5.11 (normatief)

## De vier combinaties

> - Het attribuut heeft in de werkelijkheid altijd een waarde en die waarde moet zijn gevuld, zoals de identificatie. Waarde is verplicht, mogelijk geen waarde: Nee;
> - Het attribuut heeft in de werkelijkheid altijd een waarde, maar die waarde is mogelijk onbekend, bijvoorbeeld de geboortedatum. Waarde is verplicht, mogelijk geen waarde: Ja;
> - Het attribuut heeft in de werkelijkheid soms een waarde en die waarde moet dan zijn gevuld, bijvoorbeeld de officiële straatnaam. Waarde is optioneel, mogelijk geen waarde: Nee;
> - Het attribuut heeft in de werkelijkheid soms een waarde, maar die waarde en zelfs het bestaan ervan hoeven niet bekend te zijn, zoals de overlijdensdatum van een persoon. Waarde is optioneel, mogelijk geen waarde: ja.
>
> — MIM 1.2, §5.11 (normatief)

Als tabel (eigen weergave van hetzelfde):

| | Mogelijk geen waarde: Nee | Mogelijk geen waarde: Ja |
|---|---|---|
| **Verplicht** (min. kardinaliteit 1) | identificatie | geboortedatum |
| **Optioneel** (min. kardinaliteit 0) | officiële straatnaam | overlijdensdatum |

## Verder (eigen samenvatting van §5.11)

- De beheerder van het model bepaalt welke redenen voor een ontbrekende waarde zijn toegestaan; die kun je in de toelichting vastleggen.
- Een enumeratiewaarde "onbekend" in een eigen model is niet de bedoeling, behalve bij één-op-één overgenomen gegevens uit een registratie die "onbekend" wél gebruikt.
- Mogelijk geen waarde kan ook bij een element van een datatype, zoals de dag in een datum mogelijk onvolledig (DMO).
- Het metagegeven geldt voor attribuutsoorten en relatiesoorten (§2.4.3.19); de tabellen noemen het ook bij relatieklasse, externe koppeling en (bij relatierol leidend) relatierol.

## Zie ook

- `metagegevens.md` (Kardinaliteit, Mogelijk geen waarde)
- Letterlijke tekst: `python3 scripts/mim.py paragraaf 5.11`
