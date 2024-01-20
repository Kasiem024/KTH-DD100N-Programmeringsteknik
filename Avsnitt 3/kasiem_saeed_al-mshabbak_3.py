# A program that keeps track of how far students have jumped
# Kasiem Saeed Al-Mshabbak
# 2024-01-20
# DD100N

print(
    "Welcome to the program that keeps track of who jumped how far!\n"
    "This program will assume that you have 3 students that have jumped 3 times each"
)

AMOUNT_OF_JUMPS = 3
AMOUNT_OF_STUDENTS = 3
allStudentStats = {}
studentCounter = 0

while studentCounter < AMOUNT_OF_STUDENTS:
    studentName = str(input("What is the name of the student? "))

    jumpCounter = 1
    studentJumpStats = []

    while jumpCounter <= AMOUNT_OF_JUMPS:
        jumpLength = float(input("Length of jump nr " + str(jumpCounter) + ": "))
        studentJumpStats.append([jumpLength])

        jumpCounter += 1

    allStudentStats.update({studentName: studentJumpStats})

    studentCounter += 1

userChoice = 0

while userChoice != 3:
    userChoice = int(
        input(
            "Choose one of the following options:\n "
            "1. View all the stats for all of the students\n "
            "2. View the longest jump for each student\n "
            "3. Exit the program "
        )
    )

    if userChoice == 1:
        for student in allStudentStats:
            text = student + " jumped"
            for jump in allStudentStats[str(student)]:
                text += " " + str(jump)

            text += " meter."
            print(text)

    elif userChoice == 2:
        for student in allStudentStats:
            jumpList = []

            for jump in allStudentStats[str(student)]:
                jumpList.append(jump)

            longestJump = jumpList[0]

            for jump in jumpList:
                if jump > longestJump:
                    longestJump = jump

            print("The longest jump for " + student + " is " + str(longestJump))

    else:  # If user input does not match the the available choices
        print("Sorry it seems something went wrong there, please try again!")

print("Thanks for your time!")
