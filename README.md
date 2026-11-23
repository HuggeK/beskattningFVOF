# beskattningFVOF

Underlag för delägarnas deklarationer i **Törn och Törngöls Fiskevårdsområdesförening (FVOF)**.

> [!WARNING]
> **Detta är inte skatterådgivning.** Texten är en **sammanfattning skriven av en
> språkmodell (AI)** och ska bara ses som upplysning om hur reglerna ser ut i
> november 2026. Regler och beloppsgränser ändras. **Se alltid
> [Skatteverket](https://www.skatteverket.se) för aktuella skatteregler.** Varje
> delägare ansvarar själv för sin deklaration.

## Kort om hur det fungerar

Föreningen betalar ingen inkomstskatt själv. I stället äger varje delägarfastighet
en **andel** av föreningen, och fastighetens ägare ska ta upp den andelen av
föreningens intäkter och kostnader i sin egen deklaration. Oftast blir det så små
belopp att ingen behöver deklarera något alls. Den som äger skog eller jordbruk
(en *näringsfastighet*) ska deklarera om fastighetens andel av överskottet är minst
1 500 kr. Ett år med förlust *får* den ägaren välja att ta upp förlusten och minska
sin skatt. Den som bara har ett bostadshus (en *privatbostad*) behöver i praktiken
nästan aldrig göra något. Föreningens uppgift är bara att tala om för varje
fastighet hur stor dess andel av intäkterna och kostnaderna är. Det är vad det här
verktyget räknar ut.

## Beskattningskurvan

Verktygets kärna är **beskattningskurvan**. Den visar vid vilket resultat för
föreningen delägare med näringsfastighet måste börja deklarera, och hur mycket som
då tas upp totalt. Kurvan bygger bara på andelarna, så den kan användas för att
planera: inför en stor utgift, vid budgetering eller när man sätter priset på
fiskekort.

![Beskattningskurvan](docs/beskattningskurva.png)

- **Övre diagrammet:** den röda trappan visar hur många som *ska* deklarera vid ett
  visst resultat. Den blå linjen visar hur mycket som tas upp totalt.
  - I det **gröna fältet** behöver ingen deklarera. Med våra andelar gäller det så
    länge resultatet är under 8 931 kr.
  - I det **orange fältet** har föreningen underskott, och alla med näringsfastighet
    *får* ta upp sin andel.
- **Nedre diagrammet:** för varje fastighet visas från vilket resultat just den
  måste deklarera (rött) och var den ligger under gränsen (grått).
- **Scenarier:** i notebooken jämför du egna resultat med listan `SCENARIER`.
  Där finns också ett **reglage** för att prova olika resultat (kräver `ipywidgets`).
- **I utskicket** får varje fastighet kolumnen `naring_deklarera_fran_resultat`.
  Den visar från vilket resultat för föreningen ägaren måste deklarera.

### Årets gång

```mermaid
flowchart LR
    A["Räkenskapsåret<br/>jan–dec"] --> B["Bokslut"]
    B --> C["Årsmöte i mars<br/>fastställer resultatet"]
    C --> D["Notebooken räknar<br/>andel per fastighet"]
    D --> E["Utskick till<br/>delägarna"]
    E --> F["Delägarna deklarerar<br/>i maj"]
```

Årsmötet i mars flyttar inte inkomsten till ett annat år. Verksamhetsåret 2026
deklareras i maj 2027, och en utgift i januari 2027 hör till 2027.

### Behöver jag som delägare deklarera?

```mermaid
flowchart TD
    S["Min fastighets andel<br/>(från föreningens utskick)"] --> T{"Vilken typ av fastighet?<br/>Se typkoden på<br/>fastighetstaxeringen"}
    T -->|"Lantbruk/skog (typkod 1xx)<br/>eller ägd av bolag"| N{"Andelens netto<br/>= intäkter − kostnader"}
    T -->|"Småhus där jag eller en<br/>närstående bor (typkod 2xx)"| P{"Andel av intäkterna<br/>över 50 000 kr?"}
    N -->|"1 500 kr eller mer"| N1["SKA deklarera<br/>i NE-bilagan eller INK2"]
    N -->|"0–1 499 kr"| N2["Behöver inte"]
    N -->|"Negativt"| N3["FÅR deklarera<br/>underskottet i NE"]
    P -->|"Nej (nästan alltid)"| P1["Inget att deklarera"]
    P -->|"Ja"| P2["Deklarera i ruta 7.3<br/>efter schablonavdrag"]
```

| | Näringsfastighet | Privatbostad |
|---|---|---|
| Föreningens kostnader | Ger avdrag | Ger inget avdrag |
| Gräns för att deklarera | Netto ≥ 1 500 kr | Andel av intäkterna > 50 000 kr (schablon 40 000 kr + 20 %) |
| Förlustår | Kan minska skatten på gårdens överskott | Ingen effekt |
| Blankett | NE-bilagan eller INK2 | Ruta 7.3 (ränta i 7.2) |

## Så använder du verktyget

Du behöver **bara några summor ur bokslutets resultaträkning**, inga enskilda
transaktioner.

1. **`data/andelar.csv`**: ett andelstal per rad, med komma eller punkt som decimaltecken.
   Du kan också använda en tabell med semikolon och kolumnerna
   `fastighet;andel;agare;antal_agare`, där bara `andel` krävs.
2. **`data/bokslut.csv`**: en rad per år med summorna från resultaträkningen:

   | Kolumn | Ta från resultaträkningen | Krävs |
   |---|---|---|
   | `ar` | Räkenskapsåret | Ja |
   | `intakter` | Summa rörelseintäkter (fiskekort, bidrag m.m.) | Ja |
   | `kostnader` | Summa rörelsekostnader, **inklusive avskrivningar** | Ja |
   | `ranteintakter` | Finansiella intäkter (ränta, utdelning) | Nej |
   | `ranteutgifter` | Finansiella kostnader | Nej |
   | `varav_uttaxering` | Uttaxering eller medlemsavgifter från delägarna, om den ingår i `intakter`. Räknas bort | Nej |

3. Ange året och eventuella scenarier i notebookens första kodcell och kör alla
   celler. Beskattningskurvan sparas i `utdata/beskattningskurva.png` och
   underlaget i `utdata/underlag_<år>.csv`, som kan skickas ut till delägarna.

Kräver Python 3 och `matplotlib`. `ipywidgets` behövs bara för reglaget.

**Moms:** ta beloppen direkt från resultaträkningen. Där är de redan rätt. Hos en
momsregistrerad förening, som vår, är de utan moms. Hos en förening som inte är
momsregistrerad ingår momsen i kostnaderna, och så ska det vara.

**Vad blir förenklat?** Alla intäkter behandlas lika, och bokslutets avskrivningar
används. För näringsfastigheter blir det rätt. Den som vill göra något annat,
till exempel en egen avskrivningsplan, får räkna själv utifrån sin andel. För
privatbostäder räknas alla intäkter som upplåtelseintäkter. Det kan ge något för
höga siffror, men med föreningens storlek hamnar de ändå långt under gränsen.

## Bra att veta

- **Driftsbidrag och utdelning.** Avgifter som delägarna betalar till föreningen är
  inte avdragsgilla för dem. Utdelning från föreningen är skattefri. Ingen av dem
  ska därför räknas med.
- **Avskrivningar.** Huvudregeln är att köpta tjänster och undersökningar dras av
  direkt det år de görs, till exempel en fiskevårdsplan från en konsult eller ett
  provfiske. Det finns ingen regel om 10 eller 5 år för sådana utgifter. Inventarier
  som båt, motor och redskap skrivs ofta av på 5 år. De får dras av direkt om de
  kostar mindre än ett halvt prisbasbelopp, alltså 29 800 kr år 2027 utan moms.
  Stäm av med revisorn om ni vill fördela en tjänst över flera år.
- **Moms.** Fiskekort är momspliktiga med 25 % moms när föreningen är
  momsregistrerad, vilket krävs över 120 000 kr i omsättning per år. Momsen är då
  föreningens och syns inte i delägarnas underlag.
- **Bolag med brutet räkenskapsår.** Föreningen lämnar siffror för sitt eget år.
  Bolagets revisor avgör vilket år bolaget tar upp dem.
- **KU73** gäller bara **föreningens ränteintäkter**, inte fiskekort och inte
  utdelning till medlemmarna. Den behövs bara om en privatbostads andel av räntan
  överstiger 1 500 kr. Notebooken kontrollerar det. KU73 lämnas digitalt senast
  31 januari, med ägarens personnummer.
- **Fastighetstyp.** Föreningen behöver inte hålla reda på vilken typ av fastighet
  varje delägare har. Underlaget visar utfallet för båda typerna, och delägaren
  läser det som gäller för hen.

## Källor

- [Skatteverket: Så deklarerar du som delägare i en samfällighet](https://skatteverket.se/foreningar/deklarera/sadeklarerarduatensamfallighet/sadeklarerardusomdelagareiensamfallighet.4.1c68351d170ce5545273d9b.html)
- [Skatteverket: Så deklarerar du åt en samfällighet](https://skatteverket.se/foreningar/deklarera/sadeklarerarduatensamfallighet.4.70ac421612e2a997f85800044871.html)
- [Skatteverket: Kontrolluppgift KU73](https://www.skatteverket.se/foretag/skatterochavdrag/kontrolluppgifter/kontrolluppgiftomutdelningmmtilldelagareiensamfallighetku73.4.339cd9fe17d1714c07713c1.html)
- [Skatteverket: Typkoder för fastigheter](https://skatteverket.se/foretag/skatterochavdrag/fastighet/fastighetstaxering/typkoder.4.3f4496fd14864cc5ac9126d.html)
- [Vattenägarna: Momsplikten](https://www.vattenagarna.se/momsplikten/)
- Inkomstskattelagen (1999:1229) 15 kap. 10 §, mervärdesskattelagen (2023:200) 10 kap.

Licens: GPL-3.0, se `LICENSE`.
