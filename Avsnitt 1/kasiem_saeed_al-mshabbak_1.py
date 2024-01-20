# A program that counts amount of letters in a name and age in days
# Kasiem Saeed Al-Mshabbak
# 2024-01-19
# DD100N

SURNAME = "Kasiem"
LASTNAME = "Saeed"

counter = 0
for letter in SURNAME:
    counter += 1  # Increments by 1 for each character in the string

lettersInSurname = counter

counter = 0  # Resetting counter
for letter in LASTNAME:
    counter += 1

lettersInLastname = counter

totalLettersInName = lettersInSurname + lettersInLastname

print(
    "Hello!\nMy name is " + SURNAME,
    LASTNAME + ". There are",
    totalLettersInName,
    "Letters in my name.",
)

age = 21.8
DAYS_IN_YEAR = 365
ageInDays = age * DAYS_IN_YEAR

print(
    "I am",
    age,
    "years old. If you change that into days then I've lived for about",
    ageInDays,
    "days",
)
