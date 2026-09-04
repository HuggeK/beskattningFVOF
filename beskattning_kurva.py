"""Ritar beskattningskurvan for ett FVOF och markerar arets faktiska resultat.

Samma simuleringslogik som i beskattning.ipynb, men med arets resultat som
indata: kurvan ritas upp till och med det resultatet och brytpunkten for
resultatet markeras.

Kor: python3 beskattning_kurva.py [arets_resultat]
"""

import csv
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# CHANGE Input parameters if you need!
nameOfFVOF = "Törn och Törngöls Fiskevårdsområdesförening"
aretsResultat = 124448  # Årets faktiska resultat i kronor.
undantag = 1500  # Undantag ifrån Skatteverket.
fileNameOfTheShares = "Beskattning.csv"
outputFileName = "beskattning_kurva.png"


# Reads the csv file with the shares of the entire Fiskevårdsområdesförening.
def readCSV(filename):
    andelar = []
    with open(filename, newline="") as csvfile:
        shareReader = csv.reader(csvfile, delimiter=" ")
        for row in shareReader:
            andelar.append(row)
    return andelar


def simulate(andelar, maxResult):
    # Simulation values/lists:
    totalDeclaredEveryone = []
    howManyDeclares = []
    tickListSharpIncreaseXAxis = []
    tickListSharpIncreaseCountYAxis = []
    currentSimulatedResultat = 0
    while currentSimulatedResultat <= maxResult:
        sumOfAllFractionsToTax = 0
        howManyDeclaresOnSpecificResult = 0
        for propertiesFractions in andelar:
            # replace comma with dot for decimal in python.
            fraction = float(propertiesFractions[0].replace(",", "."))
            # Antar att man får avrunda ner för skatteverket.
            taxForOneProperty = int(fraction * currentSimulatedResultat)

            if taxForOneProperty > undantag:
                howManyDeclaresOnSpecificResult += 1
                sumOfAllFractionsToTax += taxForOneProperty
        totalDeclaredEveryone.append(sumOfAllFractionsToTax)
        howManyDeclares.append(howManyDeclaresOnSpecificResult)

        # Checks if the amount who needs to tax is not the same as the last pass
        # and adds it to be able to add ticks on the X-Axis on crucial breakpoints.
        if (
            currentSimulatedResultat > 0
            and howManyDeclares[currentSimulatedResultat - 1]
            != howManyDeclares[currentSimulatedResultat]
        ):
            tickListSharpIncreaseXAxis.append(currentSimulatedResultat)
            tickListSharpIncreaseCountYAxis.append(howManyDeclaresOnSpecificResult)

        currentSimulatedResultat += 1  # Increments counter for while loop.
    return (
        tickListSharpIncreaseXAxis,
        tickListSharpIncreaseCountYAxis,
        totalDeclaredEveryone,
        howManyDeclares,
    )


if len(sys.argv) > 1:
    aretsResultat = int(sys.argv[1].replace(" ", "").replace("kr", ""))

andelar = readCSV(fileNameOfTheShares)
(
    tickListSharpIncreaseXAxis,
    tickListSharpIncreaseCountYAxis,
    totalDeclaredEveryone,
    howManyDeclares,
) = simulate(andelar, aretsResultat)

antalVidResultat = howManyDeclares[aretsResultat]
summaVidResultat = totalDeclaredEveryone[aretsResultat]
senasteBrytpunkt = max(
    [x for x in tickListSharpIncreaseXAxis if x <= aretsResultat], default=0
)
nastaBrytpunkt = None
kollaResultat = aretsResultat + 1
while nastaBrytpunkt is None and kollaResultat < aretsResultat + 100000:
    antal = sum(
        1
        for f in andelar
        if int(float(f[0].replace(",", ".")) * kollaResultat) > undantag
    )
    if antal != antalVidResultat:
        nastaBrytpunkt = kollaResultat
    kollaResultat += 1

print(
    "Crucial points to keep under, when the amount of members who need to "
    "include it in their tax return increases: " + str(tickListSharpIncreaseXAxis)
)
print(
    "Changes in amount of people who need to tax: "
    + str(tickListSharpIncreaseCountYAxis)
)
print()
print("Årets resultat: " + str(aretsResultat) + " kr")
print("Antal medlemsfastigheter som måste deklarera: " + str(antalVidResultat) + " st")
print("Summa att ta upp i deklarationerna: " + str(summaVidResultat) + " kr")
print("Närmast föregående brytpunkt: " + str(senasteBrytpunkt) + " kr")
print("Nästa brytpunkt (fler deklaranter): " + str(nastaBrytpunkt) + " kr")
print(
    "Marginal ned till föregående brytpunkt: "
    + str(aretsResultat - senasteBrytpunkt)
    + " kr"
)

# Initalizes two plots:
fig, ax1 = plt.subplots()

# Stairs with the total sum of all the money to bring into your tax return:
ax1.set_xlabel("Årets resultat i kronor (kr)")
plt.grid()  # Draws grid lines on x-axis.

ax1.set_ylabel("Summerat för alla att ta upp i sina deklrationer (kr)", color="orange")
ax1.tick_params(axis="y", labelcolor="orange")

ax1.stairs(
    totalDeclaredEveryone,
    hatch="//",
    label="Totalt att skatta för medlemmar",
    color="orange",
)

# Second plot for the amount of people which is over the undantagstillstånd:
ax2 = ax1.twinx()  # instantiate a second Axes that shares the same x-axis
ax2.set_ylabel(
    "Antal medlemsfastigheter som får uppta resultet i sin deklaration.", color="red"
)
ax2.tick_params(axis="y", labelcolor="red")

ax2.plot(howManyDeclares, label="Antal som skattar", color="red")

# Marks this years actual result:
ax1.axvline(
    aretsResultat,
    color="blue",
    linestyle="--",
    linewidth=2,
    label="Årets resultat (" + str(aretsResultat) + " kr)",
)
ax2.annotate(
    str(antalVidResultat) + " deklaranter\n" + str(summaVidResultat) + " kr totalt",
    xy=(aretsResultat, antalVidResultat),
    xytext=(-160, -30),
    textcoords="offset points",
    color="blue",
    bbox=dict(boxstyle="round", facecolor="white", edgecolor="blue"),
)

# Configuring matplotlib:
ax2.legend(
    handles=ax1.get_legend_handles_labels()[0] + ax2.get_legend_handles_labels()[0],
    labels=ax1.get_legend_handles_labels()[1] + ax2.get_legend_handles_labels()[1],
    loc="upper left",
    framealpha=0.9,
)
plt.title(
    "Summering av alla medlemmars delägarbeskattning om dessa uppgår till över "
    "undantagsgränsen på (" + str(undantag) + " kr)\nför föreningen: " + nameOfFVOF
    + " (utgår ifrån att en person äger en fastighet).",
    fontsize=12,
)
plt.grid()  # Draws grid lines on both y-axis.
fig.tight_layout()  # otherwise the right y-label is slightly clipped

fig.set_size_inches(18.5, 10.5, forward=True)
fig.set_dpi(300)

# Adjust ticks for total result:
xticks = sorted(set(tickListSharpIncreaseXAxis + [aretsResultat]))
fig.get_axes()[0].set_xticks(xticks, xticks, rotation="vertical")

fig.savefig(outputFileName, dpi=150, bbox_inches="tight")
print("\nSparade kurvan till " + outputFileName)
