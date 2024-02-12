# Ett program för ett luffarschacksspel
# Kasiem Saeed Al-Mshabbak
# 2024-02-12
# DD100N

# För att rita ut spelplanen används Box Drawing Characters": https://en.wikipedia.org/wiki/Box-drawing_character

from random import *


def skrivUtSpelplan(spelplan):
    # Skriver ut spelplanen varje gång ett drag ska göras
    # Inparameterar: spelplan (matris)

    print("    A   B   C  ")
    print("  ┏━━━┳━━━┳━━━┓")

    radRäknare = 0  # Räknar antalet rader som har skrivits ut
    for rad in spelplan:
        radRäknare += 1
        print(str(radRäknare) + " ┃", end=" ")

        for ruta in rad:
            print("" + ruta, end=" ")
            print("┃", end=" ")

        print()
        if radRäknare < 3:  # Efter sista raden vill vi inte göra detta
            print("  ┣━━━╋━━━╋━━━┫")
    print("  ┗━━━┻━━━┻━━━┛")  # Utan istället detta


def kontrolleraRader(spelplan):
    # Kontrollerar om alla tre värden i en rad är tomma och om de är samma, alltså om en spelare har vunnit eller ej
    # Inparameterar: spelplan (matris)
    # Returvärde: True om någon har vunnit, annars False (bool)

    for i in range(3):
        if " " not in [
            spelplan[i][0],
            spelplan[i][1],
            spelplan[i][2],
        ]:  # Om inget värde i raden är tomt
            if (
                spelplan[i][0] == spelplan[i][1] == spelplan[i][2]
            ):  # Om alla tre värden i raden är samma
                return True

    return False


def kontrolleraKolumner(spelplan):
    # Kontrollerar om alla tre värden i en kolumn är tomma och om de är samma, alltså om en spelare har vunnit eller ej
    # Inparameterar: spelplan (matris)
    # Returvärde: True om någon har vunnit, annars False (bool)

    for i in range(3):
        if " " not in [
            spelplan[0][i],
            spelplan[1][i],
            spelplan[2][i],
        ]:  # Om inget värde i kolumnen är tomt
            if (
                spelplan[0][i] == spelplan[1][i] == spelplan[2][i]
            ):  # Om alla tre värden i kolummnen är samma
                return True

    return False


def kontrolleraDiagonaler(spelplan):
    # Kontrollerar om värdena i de två diagonalerna är tomma och om de är samma
    # Alltså om en spelare har vunnit eller ej
    # Inparameterar: spelplan (matris)
    # Returvärde: True om någon har vunnit, annars False (bool)

    if (  # Om inget värde i diagonalen från vänster topp till höger botten är tomt och alla tre värden är samma
        " " not in [spelplan[0][0], spelplan[1][1], spelplan[2][2]]
        and spelplan[0][0] == spelplan[1][1] == spelplan[2][2]
    ):
        return True
    elif (  # Om inget värde i diagonalen från höger topp till vänster botten är tomt och alla tre värden är samma
        " " not in [spelplan[2][0], spelplan[1][1], spelplan[0][2]]
        and spelplan[2][0] == spelplan[1][1] == spelplan[0][2]
    ):
        return True
    else:
        return False


def finnsVinnare(spelplan):
    # Kallar på funktioner som kontrollerar om någon har vunnit eller inte
    # Inparameterar: spelplan (matris)
    # Returvärde: True om någon har vunnit, annars False (bool)

    if (
        kontrolleraKolumner(spelplan)
        or kontrolleraDiagonaler(spelplan)
        or kontrolleraRader(spelplan)
    ):
        return True
    else:
        return False


def oavgjort(spelplan):
    # Kontrollerar om spelet är oavgjort genom att kolla om det finns en tom cell i spelplanen
    # Inparameterar: spelplan (matris)
    # Returvärde: True om spelplanen är full, annars False (bool)

    for rad in spelplan:
        for element in rad:
            if element == " ":
                return False
    return True


def slumpaVemBörjar():
    # Slumpar vilken spelare som gör det första draget
    # Returvärde: Slumpmässigt tal, 0 eller 1 (int)
    return randrange(0, 1)


def tolkaInmatning(inmatning):
    # Tar in vart spelaren vill spela och tolkar det till något programmet kommer förstå
    # Alltså retunerar funktionen koordinaterna som enbart nummer
    # Inparameterar: inmatning (string)
    # Returvärde: rad (int)
    #             kolumn (int)

    bokstav = inmatning[
        0
    ].upper()  # Använder .upper() för att göra om alla inmatade bokstäver till versaler
    rad = int(inmatning[1]) - 1
    if bokstav == "A":
        kolumn = 0
    elif bokstav == "B":
        kolumn = 1
    elif bokstav == "C":
        kolumn = 2
    return rad, kolumn


def spela(spelarNamn1, spelarNamn2):
    # Innehåller loopen som faktiskt kör spelet och kallar på alla andra funktioner
    # Håller koll på vems tur det är och om spelet är klart
    # Inparameterar: spelarNamn1 (string)
    #                spelarNamn2 (string)

    print("Då kör vi!")
    print("Ange de koordinater du vill lägga på på formatet A1, B3 osv.")
    spelplan = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    spelarLista = [spelarNamn1, spelarNamn2]
    vemsTur = slumpaVemBörjar()

    while oavgjort(spelplan) == False:
        vemsTur = (
            vemsTur + 1
        ) % 2  # vemsTur ska aldrig bli 2, utan börja om igen på 0, %-är modul dvs resten vid heltals division.
        skrivUtSpelplan(spelplan)

        if vemsTur == 0:
            markör = "X"
        else:
            markör = "O"

        inmatning = input(str(spelarLista[vemsTur]) + "s tur att spela: ")
        rad, kolumn = tolkaInmatning(inmatning)

        while spelplan[rad][kolumn] != " ":
            # Om spelaren lägger sin markör på en icke tom ruta får den spela igen tills den gör rätt
            print("Den rutan är redan uptagen, välj en tom ruta!")
            skrivUtSpelplan(spelplan)
            inmatning = input(str(spelarLista[vemsTur]) + "s tur att spela: ")
            rad, kolumn = tolkaInmatning(inmatning)

        spelplan[rad][kolumn] = markör

        if finnsVinnare(spelplan) == True:
            skrivUtSpelplan(spelplan)
            print("Grattis " + str(spelarLista[vemsTur]) + " du vann!")
            break

    if oavgjort(spelplan) and finnsVinnare(spelplan) == False:
        skrivUtSpelplan(spelplan)
        print("Det blev oavgjort!")


def huvudfunktion():
    # Här börjar programmet, frågar om spelarnas namn och kallar på funktionen som kör spelet

    print("Hej och väkommen till Tre-i-rad!")
    spelarNamn1 = input("Vad heter spelare 1? ")
    spelarNamn2 = input("Vad heter spelare 2? ")
    spela(spelarNamn1, spelarNamn2)


huvudfunktion()
