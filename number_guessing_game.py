import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = random.choice (range(1,101))  

print("Please select the difficulty level:\n 1. Easy (10 chances) \n 2. Medium (5 chances) \n 3. Hard (3 chances)")

difficulty =  input("Enter your choice:").lower()

if difficulty == "1" or difficulty == "easy" :
    print("Great! You have selected the Easy difficulty level.\n Let's start the game!")
    attempts = 10

elif difficulty == "2" or difficulty == "medium":
    print("Great! You have selected the Medium difficulty level.\n Let's start the game!")
    attempts = 5

elif difficulty == "3" or difficulty == "hard" :
    print("Great! You have selected the Hard difficulty level.\n Let's start the game!")
    attempts = 3

else :
    print("Please enter a valid difficulty")
    exit()

print(f"You have {attempts} attempts to guess the number ")

for i in range (attempts):
    guess  = int(input(f"{i+1} Enter your guess: "))
    
    if guess > number :
        print(f"Incorrect! The number is less than {guess}")

    elif guess < number :
        print(f"Incorrect! The number is greater than {guess}") 

    else :
        print(f"Congratulations! You guessed the correct number in {i+1} attempts.")
        exit()