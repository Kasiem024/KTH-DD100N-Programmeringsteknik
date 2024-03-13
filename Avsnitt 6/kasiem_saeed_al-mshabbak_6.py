# A program to show status of pets and interact with them
# Kasiem Saeed Al-Mshabbak
# 2024-03-13
# DD100N


class Pet:
    # Describes a Pet, has attributes name (str), needsPetting (bool), hungry (bool)

    def __init__(self, name, needsPetting, hungry):
        # Constructor that gets called when creating a new pet
        # Parameters in: name (str)
        # Parameters in: needsPetting (bool)
        # Parameters in: hungry (bool)

        self.name = name  # str
        self.needsPetting = needsPetting  # bool
        self.hungry = hungry  # bool

    def __str__(self):
        # Returns a string that desribes the object

        return (
            self.name
            + ": Needs petting? "
            + str(self.needsPetting)
            + " Needs food? "
            + str(self.hungry)
        )

    def __lt__(self, other):
        # Sorts pets based on name

        if self.name < other.name:
            return True
        else:
            return False

    def petting(self):
        # Changes needsPetting attribute to false
        self.needsPetting = False

    def feed(self):
        # Changes hungry attribute to false
        self.hungry = False


def readPetsFile(petsFile):
    # Reads pets from file, puts them in a list and sorts the list
    # Parameters in: petsFile (list)
    # Parameters out: petList (list)

    petList = []

    for line in petsFile:
        line = line.strip()

        petName = str(line.split(",")[0])  # Splits the pets name
        petNeedsPetting = bool(line.split(",")[1])  # Splits the pets need for petting
        petHungry = bool(line.split(",")[2])  # Splits the pets hunger

        petList.append(
            Pet(petName, petNeedsPetting, petHungry)
        )  # Adds the values to the end of the list

    return petList


def interactWithPet(petList, chosenPet, petIndex):
    # Lets the user interact with chosen pet through a choice menu, returns updated petList
    # Parameters in: petList (list)
    # Parameters in: chosenPet (str)
    # Parameters in: petIndex (int)
    # Parameters out: petList (list)

    interactionChoice = 0

    while interactionChoice != 3:
        try:
            print(
                "What do you want to do with "
                + chosenPet
                + " ?\n1: Pet\n2: Feed \n3: Return to main menu\n"
            )

            interactionChoice = int(input("\nWhat is your choice? "))

            if interactionChoice == 1:
                # Using petIndex to know which pet to pet with
                print("\nPetting" + chosenPet)
                petList[petIndex].petting()

            elif interactionChoice == 2:
                # Using petIndex to know which pet to feed with
                print("\nFeeding" + chosenPet)
                petList[petIndex].feed()

            elif interactionChoice == 3:
                # Goes back to choiceMenu()
                pass

        except:
            print("\nSomething went wrong there!\n")
            continue

    return petList


def addNewPet(petList):
    # Adds a new pet with users input, handles errors
    # Parameters: petList (list)
    # Parameters out: petList (list)

    newPetAdded = False  # Used to keep user inside of loop in case of wrong input

    while newPetAdded == False:
        try:
            petName = str(input("What is the name of the pet? "))

            for pet in petList:
                if petName == pet.name:  # Checks if pet already exists
                    print("That pet already exists!")
                    raise Exception

            petNeedsPetting = str(input("Does the pet need petting, True or False "))

            if petNeedsPetting == "True":
                petNeedsPetting = True

            elif petNeedsPetting == "False":
                petNeedsPetting = False

            else:
                print("\nNeeds to be either True or False!\n")
                raise Exception

            petHungry = str(input("Is the pet hungry, True or False "))

            if petHungry == "True":
                petHungry = True

            elif petHungry == "False":
                petHungry = False

            else:
                print("\nNeeds to be either True or False!\n")
                raise Exception

            petList.append(
                Pet(petName, petNeedsPetting, petHungry)
            )  # Adds the values to the end of the list

            print("\nNew pet added!\n")

            newPetAdded = True  # If all of the user's inputs have been correct, return to main menu

        except:
            print("\nSomething went wrong there!\n")
            continue

    return petList


def removePet(petList):
    # Removes a pet with users input
    # Parameters: petList (list)
    # Parameters out: petList (list)

    petFound = False

    while petFound == False:
        try:

            chosenPet = str(
                input("\nName of pet you want to remove: ")
            )  # User chooses which pet to remove

            counter = 0  # Used to know index of chosen pet

            for pet in petList:

                if pet.name == chosenPet:
                    # If user's choice exists
                    del petList[counter]
                    print("\nPet has been removed!\n")
                    petFound = True

                counter += 1

            if petFound == False:
                # If user's choice doesn't exist
                print("\nNo pet matches that name!\n")

        except:
            print("\nSomething went wrong there!\n")
            continue

    return petList


def writeToPetsFile(petList, petsFile):
    # Formats each item in petList and writes it to petsFile
    # Parameters in: petList (list)
    # Parameters in: petsFile (list)

    petsFile.seek(0)  # Resets file pointer position to the first line

    counter = 0  # Being used to know if it's the last pet

    for pet in petList:
        lineToWrite = (
            pet.name + "," + str(pet.hungry) + "," + str(pet.needsPetting) + "\n"
        )  # Formats the line to be written

        if counter == (len(petList) - 1):
            # If it's the last line to be written

            lineToWrite = (
                pet.name + "," + str(pet.hungry) + "," + str(pet.needsPetting)
            )  # Don't include new line
            petsFile.truncate()  # Removes all lines after last line to be written

        petsFile.write("".join(lineToWrite))  # Writes to file

        counter += 1

    petsFile.close()


def choiceMenu(petList, petsFile):
    # Lets user choose what to do
    # Parameters in: petList (list)
    # Parameters in: petsFile (list)

    userChoice = 0

    while userChoice != 5:
        try:
            print(
                "Hello what do you want to do?\n1: See status of all pets\n2: Interact with a specific pet\n3: Add a new pet\n4: Remove pet\n5: Exit program\n"
            )

            userChoice = int(input("\nWhat is your choice? "))

            if userChoice == 1:
                print("\nAll pets sorted alphabetically by their name:\n")
                petList.sort()

                for pet in petList:
                    print(pet)

            elif userChoice == 2:
                chosenPet = str(
                    input("\nName of pet you want to interact with: ")
                )  # User chooses which pet to interact with

                counter = 0  # Used to know index of chosen pet
                petFound = False

                for pet in petList:

                    if pet.name == chosenPet:
                        # If user's choice exists
                        petList = interactWithPet(petList, chosenPet, counter)
                        petFound = True

                    counter += 1

                if petFound == False:
                    # If user's choice doesn't exist
                    print("\nNo pet matches that name!\n")

            elif userChoice == 3:
                # Lets user add a new pet
                petList = addNewPet(petList)

            elif userChoice == 4:
                petList = removePet(petList)

            elif userChoice == 5:
                # Writes to file and exits program

                writeToPetsFile(petList, petsFile)
                print("\nGoodbye!")

            else:
                # If user input is an int not between 1-3
                print("\nSomething went wrong therem try again!\n")

        except:
            print("\nSomething went wrong there!\n")
            continue


def main():
    # Program starts here, opens file, calls readPetsFile and choiceMenu

    petsFile = open("pets.txt", "r+")
    petList = readPetsFile(petsFile)
    choiceMenu(petList, petsFile)


main()
