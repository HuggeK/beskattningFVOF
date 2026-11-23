# beskattningFVOF

Underlag för delägarbeskattning i **Törn och Törngöls Fiskevårdsområdesförening (FVOF)**.
Notebooken `beskattning.ipynb` fördelar föreningens intäkter och kostnader på
delägarfastigheterna. För varje fastighet visar den vad som ska, får eller inte
behöver tas upp i deklarationen.

> [!WARNING]
> **Viktigt: detta är inte skatterådgivning.**
>
> Texten i den här README:n och i notebooken är en **sammanfattning skriven av en
> språkmodell (AI)**. Den ska bara ses som **upplysning om hur reglerna ser ut i
> skrivande stund (november 2026)**. Regler, beloppsgränser och Skatteverkets
> tolkningar ändras.
>
> **Se alltid [Skatteverket](https://www.skatteverket.se) för aktuella skatteregler.**
> Allt här är enbart råd. Varje delägare ansvarar själv för sin deklaration. Fråga
> Skatteverket, föreningens revisor eller en redovisningskonsult vid minsta tvekan.
> Belopp och regler nedan gäller inkomstår 2024 och framåt om inget annat anges.

---

## Snabbstart

1. Fyll i `data/andelar.csv`. Det räcker med en lista med ett andelstal per rad.
2. Fyll i en resultatfil för året, se `data/resultat_exempel.csv`. Använd **bokslutets
   periodiserade belopp**, inte kontoutdragen.
3. Fyll i `data/investeringar.csv` med föreningens investeringar, alla år.
4. Ställ in år, filnamn och om föreningen är momsregistrerad i notebookens första kodcell.
5. Kör alla celler. Resultatet visas i notebooken och sparas i `utdata/underlag_<år>.csv`.

Kräver Python 3 och `matplotlib`, för diagrammet.

---

## Sammanfattning av reglerna

### 1. Föreningen är delägarbeskattad

Fiskevårdsområden är i regel **delägarbeskattade**. Föreningen betalar ingen
inkomstskatt. Varje delägare deklarerar i stället sin fastighets andel av
föreningens intäkter och kostnader.

Utdelning från föreningen och driftsbidrag till föreningen räknas inte med:

- **Driftsbidrag/uttaxering** från delägarna är inte avdragsgilla för delägaren och
  är ingen intäkt i beräkningen.
- **Utdelning** till delägarna är skattefri för delägaren och ingen kostnad i beräkningen.

### 2. Vilket år?

- Delägare som är **fysiska personer och dödsbon** har kalenderår som beskattningsår.
- Med kalenderår som räkenskapsår gäller: verksamhetsåret 2026 fastställs på
  årsmötet i mars 2027 och deklareras i maj 2027 (inkomstår 2026). **Årsmötets
  datum flyttar inte inkomsten till ett annat år.**
- En utgift som uppkommer i januari 2027 hör till 2027 års resultat. Undantag är om
  den gäller 2026 och bokas som skuld i bokslutet för 2026 (bokföringsmässiga grunder).
- **Aktiebolag och ekonomiska föreningar** som äger delägarfastigheter kan ha
  **brutet räkenskapsår**. Skatteverket anger ingen uttrycklig regel för vilket av
  föreningens år de ska ta upp. Det avgör bolagets revisor eller redovisningskonsult.
  Föreningen lämnar siffror för sitt eget räkenskapsår.

### Näring eller privat: därför spelar fastighetstypen roll

| | Näring | Privat |
|---|---|---|
| Föreningens kostnader | Ger avdrag | Ger inget avdrag |
| Gräns för att deklarera | Netto ≥ 1 500 kr | Andelen av upplåtelseintäkten överstiger 50 000 kr (schablon 40 000 kr + 20 % av intäkten) |
| Förlustår (till exempel 2027) | Kan minska skatten på gårdens överskott | Ingen effekt |
| Blankett | NE-bilagan eller INK2 | Ruta 7.2 och 7.3 (ränteutgifter i 8.1) |

### 3. Näringsfastighet (lantbruk, skog, fastigheter ägda av bolag)

- Andelen av intäkter och **faktiska kostnader** redovisas i näringsverksamhet:
  NE-bilagan för fysiska personer, INK2 för aktiebolag.
- Andelen **behöver inte tas upp om intäkterna överstiger kostnaderna med mindre än
  1 500 kr** (15 kap. 10 § IL, 600 kr till och med inkomstår 2023).
  Gränsen gäller **nettot**. Är nettot exakt 1 500 kr eller mer ska andelen tas upp.
- Undantaget gäller **intäkter och kostnader tillsammans**. Det går inte att ta upp
  bara kostnaderna.
- **Underskott:** lagtexten säger "behöver inte". Det tyder på att en delägare får
  välja att ta upp en negativ andel, till exempel ett år med en stor utgift, och
  minska sitt överskott från jord- eller skogsbruket. Skatteverket säger inget
  uttryckligt om detta. **Kontrollera med Skatteverket innan det används.**
- För en fysisk person räknas all näringsverksamhet som en. Andelen ingår alltså i
  samma NE som skogsgården. Gårdens egna kostnader, till exempel maskiner, får dras
  av oavsett föreningen. Utjämning mellan år görs med periodiseringsfond,
  expansionsfond och räntefördelning. **Skogskonto** gäller bara intäkter från
  skogen och inte fiskeintäkter.
- Värdeminskningsavdrag på föreningens tillgångar görs som om de vore fastighetens egna.

### 4. Privatbostadsfastighet (småhus ägt av en fysisk person)

- Andelen av upplåtelseintäkterna, till exempel fiskekort och arrende, deklareras
  som **kapital, ruta 7.3**.
- **Faktiska kostnader får inte dras av.** I stället gäller ett **schablonavdrag på
  40 000 kr per år och fastighet plus 20 % av intäkten**. Avdraget får inte bli större
  än intäkten. Schablonen gäller fastighetens **alla** upplåtelser tillsammans, så
  annan uthyrning på samma fastighet påverkar resultatet.
- **Ränta och utdelning** deklareras i ruta 7.2. Bara den del av andelen som
  **överstiger 1 500 kr** per samfällighet ska tas upp.
- **Ränteutgifter:** andelen får dras av i ruta 8.1.
- Ingen förlust kan uppstå, och föreningens kostnader påverkar inte delägarens skatt.

### 5. Kontrolluppgift KU73

För en **delägarbeskattad** förening gäller KU73 inte utdelning från föreningen
till medlemmarna. Den gäller **föreningens egna ränteintäkter och utdelningar på
kapital**, till exempel ränta på bankkontot.

- **Vilka:** privatpersoner och dödsbon som äger en **privatbostadsfastighet**.
  Näringsfastigheter ingår inte.
- **Belopp:** fält 732, "Skattepliktig del kapital". Det är fastighetens andel av
  räntan och utdelningen **minus 1 500 kr**. Upplåtelse, till exempel fiskekort,
  ska **inte** med. Ränteutgifter dras inte av.
- **Flera ägare:** en KU73 per ägare, där beloppet delas. Exempel: 2 000 kr − 1 500 kr
  = 500 kr ger 250 kr var för två ägare.
- **Under gränsen:** är andelen högst 1 500 kr lämnas ingen KU73.
- **Uppgifter som krävs:** föreningens organisationsnummer och namn, inkomstår,
  specifikationsnummer, samt mottagarens personnummer (eller dödsbonummer),
  namn och adress.
- **När och hur:** senast **31 januari** året efter. Bara digitalt, via
  e-tjänsten *Lämna kontrolluppgifter* eller som XML-fil. Rättelser görs med samma
  specifikationsnummer.

Notebooken behöver inte veta fastighetstypen för att avgöra om KU73 **kan** behövas.
Om ingen fastighets andel av räntan är över 1 500 kr behövs ingen KU73 alls.
Annars listas de fastigheter där det krävs **om** de är privatbostäder.

### 6. Moms (vår förening är momsregistrerad)

- Upplåtelse av **rätt till fiske** är undantagen från fastighetsundantaget i
  mervärdesskattelagen (2023:200) och är därför **momspliktig**. Fiskekort säljs
  med **25 % moms**. Livsmedel, till exempel fisk, har 12 % och böcker 6 %.
- Momsplikt gäller när omsättningen överstiger **120 000 kr per år**. En förening
  under gränsen kan ansöka om momsbefrielse men förlorar då avdragsrätten för
  ingående moms.
- **Momsen är föreningens.** Delägarna redovisar ingen moms. Den ingår inte heller i
  deras inkomster eller kostnader.
- Är föreningen momsregistrerad ska **alla belopp i delägarunderlaget vara exklusive
  moms**: intäkter utan utgående moms och kostnader utan avdragsgill ingående moms.
  Notebooken räknar om belopp som anges inklusive moms.
- Är föreningen inte momsregistrerad är kostnaderna **inklusive moms**, eftersom
  momsen då är en kostnad.
- Bidrag är normalt ingen momspliktig omsättning (moms 0 %).

### 7. Avskrivningar och investeringar

**Huvudregeln är direkt avdrag.** Löpande kostnader och köpta tjänster dras av det
år de uppkommer. Avskrivning (värdeminskningsavdrag) gäller **inventarier**, till
exempel båt, motor, nät, fiskräknare och mätstation, samt vissa förvärvade
rättigheter.

| Exempel | Vanlig hantering | Kommentar |
|---|---|---|
| **Fiskevårdsplan** köpt av konsult | **Direkt avdrag** (löpande kostnad/tjänst) | Det finns ingen regel om 10 år. En plan är en köpt tjänst, inte ett inventarium eller en förvärvad rättighet. Att fördela den över 10 år kräver stöd i god redovisningssed (aktivering som immateriell tillgång) och bör stämmas av med revisor eller Skatteverket först. |
| **Provfiske** | **Direkt avdrag** | En undersökning av beståndet är en driftkostnad. Att fördela den över 5 år har normalt inget stöd. |
| Båt, motor, redskap | Avskrivning, ofta **5 år** (20 % per år) | Inventarieregler: räkenskapsenlig avskrivning (30- eller 20-regeln) eller restvärdesavskrivning. |
| Inventarie med livslängd ≤ 3 år | Direkt avdrag | Korttidsinventarier |
| Inventarie under ett **halvt prisbasbelopp** | Direkt avdrag | Inventarier av mindre värde. 29 600 kr år 2026 och 29 800 kr år 2027, exklusive moms vid avdragsrätt. |

Notebooken låter dig ange avskrivningstid per post (`0` betyder direkt avdrag) och
använder rak avskrivning med helårsavskrivning från anskaffningsåret som underlag.
Poster av typen `tjanst` med avskrivningstid över 0 flaggas, eftersom huvudregeln
är direkt avdrag. Varje delägare med näringsfastighet får göra
värdeminskningsavdrag som om tillgången vore hans eller hennes egen. Föreningens
plan är därför ett förslag och inget tvång.

---

## Indatafiler

Alla filer använder semikolon `;` som avgränsare. Decimaler kan skrivas med komma
eller punkt, och andelar kan skrivas som bråk (`5/64`).

### `data/andelar.csv`

Det enklaste formatet är **en lista med ett andelstal per rad**. Decimaltecknet
kan vara komma eller punkt, citattecken runt talen går bra, och en rubrikrad
som `andel` hoppas över:

```
0,167971461
0.001761027
"0,009030724"
5/64
```

Fastigheterna får då namnen *Fastighet 01*, *Fastighet 02* och så vidare i radordning.

Vill du ha med fler uppgifter använder du en tabell med **semikolon** (eller tab)
som avgränsare. Kommatecken går inte, eftersom det kan vara decimaltecken. Bara
`andel` krävs, alla andra kolumner är frivilliga:

| Kolumn | Beskrivning |
|---|---|
| `andel` | Andelstal: decimaltal, bråk (`5/64`) eller mantal, se `ANDELSTYP` i notebooken |
| `fastighet` | Fastighetsbeteckning |
| `agare` | Ägare, fritext |
| `antal_agare` | Antal ägare som delar fastigheten lika (standard 1). Används för belopp per ägare och KU73 |

`fastighet;andel` utan rubrikrad fungerar också.

Ingen kolumn för fastighetstyp behövs. Notebooken visar utfallet både för
näringsfastighet och för privatbostad, och varje delägare läser den kolumn som
gäller för hen.

### `data/resultat_<år>.csv`

| Kolumn | Beskrivning |
|---|---|
| `post` | Beskrivning, till exempel "Fiskekort Iceberg" |
| `kategori` | Se tabellen nedan |
| `belopp` | Belopp i kr. Positivt för både intäkter och kostnader. Negativt bara för rättelser |
| `moms_sats` | 0, 6, 12 eller 25 |
| `inkl_moms` | `ja` om beloppet är inklusive moms, annars `nej` |

| Kategori | Betyder | Med i underlaget? |
|---|---|---|
| `upplatelse` | Fiskekort, upplåtelse eller arrende av fiskerätt | Intäkt |
| `ranta` | Ränteintäkter och utdelning | Intäkt (egen regel för privatbostad) |
| `bidrag` | Bidrag, till exempel fiskevårdsbidrag | Intäkt |
| `ovrig_intakt` | Övriga intäkter | Intäkt |
| `drift` | Direkt avdragsgilla kostnader: utsättning, provfiske, fiskevårdsplan, tillsyn, försäkring, möten | Kostnad |
| `ranteutgift` | Ränteutgifter | Kostnad (ruta 8.1 för privatbostad) |
| `driftsbidrag` | Uttaxering eller avgifter från delägarna | **Nej**, räknas bort |
| `utdelning` | Utdelning till delägarna | **Nej**, räknas bort |

### `data/investeringar.csv`

| Kolumn | Beskrivning |
|---|---|
| `post` | Beskrivning |
| `typ` | `inventarie` eller `tjanst` |
| `anskaffningsar` | År |
| `anskaffningsvarde` | Belopp i kr |
| `moms_sats`, `inkl_moms` | Som ovan |
| `avskrivningstid_ar` | Antal år. `0` betyder direkt avdrag anskaffningsåret |

### Utdata per fastighet

Andel av upplåtelse, ränta, övriga intäkter, driftkostnader, ränteutgifter och
avskrivning, samt netto. Utfallet visas för **båda** fastighetstyperna:

- **Om näringsfastighet:** `SKA deklarera` (netto ≥ 1 500 kr), `FÅR välja (underskott)`
  (netto < 0) eller `Behöver inte` (0–1 499 kr).
- **Om privatbostad:** belopp att ta upp i ruta 7.3 efter schablonavdrag, ränta över
  1 500 kr för ruta 7.2, avdrag i ruta 8.1, och KU73-belopp per ägare.

---

## Källor (Skatteverket m.fl.)

- [Så deklarerar du som delägare i en samfällighet](https://skatteverket.se/foreningar/deklarera/sadeklarerarduatensamfallighet/sadeklarerardusomdelagareiensamfallighet.4.1c68351d170ce5545273d9b.html)
- [Så deklarerar du åt en samfällighet](https://skatteverket.se/foreningar/deklarera/sadeklarerarduatensamfallighet.4.70ac421612e2a997f85800044871.html)
- [Kontrolluppgift KU73](https://www.skatteverket.se/foretag/skatterochavdrag/kontrolluppgifter/kontrolluppgiftomutdelningmmtilldelagareiensamfallighetku73.4.339cd9fe17d1714c07713c1.html)
- [Momssatser och undantag från moms](https://www.skatteverket.se/foretag/moms/saljavarorochtjanster/momssatserochundantagfranmoms.4.58d555751259e4d66168000409.html)
- [Mervärdesskattelag (2023:200)](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/mervardesskattelag-2023200_sfs-2023-200/), 10 kap. undantag inom fastighetsområdet
- [Vattenägarna – Momsplikten](https://www.vattenagarna.se/momsplikten/)
- [Prisbasbeloppet för år 2027 (SCB)](https://www.scb.se/hitta-statistik/statistik-efter-amne/priser-och-ekonomiska-tendenser/priser/konsumentprisindex-kpi/pong/statistiknyhet/prisbasbeloppet-for-ar-2027/)
- Inkomstskattelagen (1999:1229): 6 kap. 6 §, 15 kap. 10 §, 42 kap. 29–30 §§

## Licens

GPL-3.0, se `LICENSE`.
