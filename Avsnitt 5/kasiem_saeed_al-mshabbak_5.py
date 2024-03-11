# A program to read and write new values to a file
# Kasiem Saeed Al-Mshabbak
# 2024-03-10
# DD100N


def readResults(resultsFile):
    # Reads results from file, puts them in a list and sorts the list
    # Parameters in: resultsfile (list)
    # Parameters out: resultsList (list)

    resultsList = []

    for line in resultsFile:
        line = line.strip()

        playerName = line.split(",")[0]  # Splits the player's name from their points
        playerPoints = line.split(",")[1]

        resultsList.append(
            [playerName, int(playerPoints)]
        )  # Adds the values to the end of the list

    resultsList.sort(
        key=lambda player: player[1], reverse=True
    )  # Sorts the list by amount of points

    return resultsList


def writeToFile(resultsList, resultsFile):
    # Formats each item in resultsList and writes it to resultsFile
    # Parameters: resultsList (list)
    #             resultsFile (list)
    # Parameters out: resultsList (list)

    resultsFile.seek(0)  # Resets file pointer position to the first line
    counter = 0

    for result in resultsList:
        lineToWrite = (
            result[0] + "," + str(result[1]) + "\n"
        )  # Formats the line to be written

        if counter == (len(resultsList) - 1):
            # If it's the last line to be written
            lineToWrite = result[0] + "," + str(result[1])  # Don't include new line

        resultsFile.write("".join(lineToWrite))  # Writes to file
        counter += 1

    resultsFile.close()
    return resultsList


def writeResult(resultsList):
    # Updates resultsList with users input, handles errors
    # Parameters: resultsList (list)
    # Parameters out: resultsList (list)

    try:
        playerName = str(input("What is the name of the player? "))

        for player in resultsList:
            if playerName == player[0]:  # Checks if playerName already exists
                print("That name already exists!")
                raise Exception

        playerPoints = int(
            input("How many points did " + playerName + " get? ")
        )  # Int here to make sure the input is a number

        if playerPoints < 51:  # Check if player has too many points
            resultsList.append(
                [playerName, playerPoints]
            )  # Adds new result to the end ofresultsList

        else:
            print("Too many points!")
            raise Exception

    except:
        print("\nSomething went wrong there!\n")
        pass

    return resultsList


def choiceMenu(resultsList, resultsFile):
    # Lets user choose what to do
    # Parameters: resultsList (list)
    #             resultsFile (list)

    userChoice = 0

    while userChoice != 3:
        try:

            print(
                "\nHello, what do you want do do?\n1: See results so far\n2: Add new result\n3: Save and exit\n"
            )

            userChoice = int(input("\nWhat is your choice? "))

            if userChoice == 1:
                # Shows resultsList
                print("\nThe results so far are:")

                for player in resultsList:
                    print(player[0], player[1], "points")

            elif userChoice == 2:
                # Lets user write a new result
                resultsList = writeResult(resultsList)

            elif userChoice == 3:
                # Writes to file and exits program
                writeToFile(resultsList, resultsFile)
                print("Goodbye!")

            else:
                # If user input is an int not between 1-3
                print("\nSomething went wrong there, try again!\n")

        except:
            print("\nSomething went wrong there!\n")
            continue


def main():
    # Program starts here, opens file calls readResults and choiceMenu

    resultsFile = open("results.txt", "r+")
    resultsList = readResults(resultsFile)
    choiceMenu(resultsList, resultsFile)


main()
