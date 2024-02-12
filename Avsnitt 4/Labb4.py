# Namn
# Datum
# Kurskod

# En kort beskrivning av programmet.

# För att rita ut spelplanen används Box Drawing Characters": https://en.wikipedia.org/wiki/Box-drawing_character


def skrivUtSpelplan(spelplan):
    print("    A   B   C  ")
    print("  ┏━━━┳━━━┳━━━┓")
    radRäknare = 0
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


def kontrolleraRader():
    """Kontrollerar om det finns tre likadana tecken på någon rad och returnerar då True, annars False
    Inparameter: spelplan (matris)
    Returvärde: True om det finns vinnare annars False (booleskt värde)
    """


def kontrolleraKolumner(spelplan):
    for i in range(3):
        if " " not in [spelplan[0][i], spelplan[1][i], spelplan[2][i]]:
            if spelplan[0][i] == spelplan[1][i] == spelplan[2][i]:
                return True
            else:
                return False

    return False


def kontrolleraDiagonaler(spelplan):
    # första diagonalen, uppe till vänster till nere till höger
    if (
        " " not in [spelplan[0][0], spelplan[1][1], spelplan[2][2]]
        and spelplan[0][0] == spelplan[1][1] == spelplan[2][2]
    ):
        return True
    else:
        return False


def finnsVinnare(spelplan):
    if kontrolleraKolumner(spelplan) or kontrolleraDiagonaler(spelplan):
        return True
    else:
        return False


def oavgjort(spelplan):
    for rad in spelplan:
        for element in rad:
            if element == " ":
                return False
    return False


def tolkaInmatning(inmatning):
    bokstav = inmatning[
        0
    ].upper()  # Använder .upper() för att göra om alla inmatade bokstäver till versaler
    rad = int(inmatning[1]) - 1
    if bokstav == "A":
        kolumn = 0
    elif bokstav == "B":
        kolumn = 1
    else:
        kolumn = 2
    return rad, kolumn


def spela(spelarNamn1, spelarNamn2):
    print("Då kör vi!")
    print("Ange de koordinater du vill lägga på på formatet A1, B3 osv.")
    spelplan = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    # spelplan = [["X", "X", "O"], ["O", "O", "X"], ["X", " ", "O"]]
    # spelplan = [["X", "X", "O"], ["O", "X", "O"], ["X", "O", " "]]

    spelarLista = [spelarNamn1, spelarNamn2]
    vemsTur = 1
    while finnsVinnare(spelplan) == False:
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
        spelplan[rad][kolumn] = markör
        if oavgjort(spelplan) == True:
            skrivUtSpelplan(spelplan)
            print("Det blev oavgjort!")
            break

    if not oavgjort(spelplan):
        skrivUtSpelplan(spelplan)
        print("Grattis " + str(spelarLista[vemsTur]) + " du vann!")


def huvudfunktion():
    print("Hej och väkommen till Tre-i-rad!")
    spelarNamn1 = input("Vad heter spelare 1? ")
    spelarNamn2 = input("Vad heter spelare 2? ")
    spela(spelarNamn1, spelarNamn2)
