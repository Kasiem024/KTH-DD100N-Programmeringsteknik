# A program that converts measurements
# Kasiem Saeed Al-Mshabbak
# 2024-01-20
# DD100N

print("Welcome to a small and simple unit conversion program!")

userChoice = 0

while userChoice != 5:
    userChoice = int(
        input(
            "Choose on of the following options:\n "
            "1. Degrees in Celsius to degrees in Fahrenheit\n "
            "2. Distance in meters to distance in american miles\n "
            "3. Volume in liters to volume in gallons\n "
            "4. Weight in kilograms to weight in pounds\n "
            "5. Exit the program "
        )
    )

    if userChoice == 1:
        tempInCelsius = float(input("What is the temperature in Celsius? "))
        tempInFahrenheit = (tempInCelsius * 1.8) + 32

        print(tempInFahrenheit)

    elif userChoice == 2:
        distanceInMeters = float(input("What is the distance in meters? "))
        distanceInMiles = distanceInMeters / 1609.3

        print(distanceInMiles)

    elif userChoice == 3:
        volumeInLiter = float(input("What is the volume in liters? "))
        volumeInGallons = volumeInLiter / 3.785

        print(volumeInGallons)

    elif userChoice == 4:
        weightInKG = float(input("What is the weight in kilograms? "))
        weightInPounds = weightInKG * 2.2046

        print(weightInPounds)

    else:  # If user input does not match the the available choices
        print("Sorry it seems something went wrong there, please try again!")

print("Thanks for your time!")
