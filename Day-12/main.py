# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo

import random

print(lobo)
my_number = random.randint(1, 100)
attempts = {"hard": 5, "easy": 10}

print("I'm thinking of a number between 1 and 100")
total_attempts = attempts[input("chose a difficulty: easy or hard ")]


def check_choice():
    global total_attempts
    guess = int(input("Make a guess! "))
    if guess == my_number:
        print("You got it right")
        return 1
    elif guess > my_number:
        print("Too high")

        total_attempts -= 1
        print(f"You have {total_attempts} attempts remaining")

    else:
        print("Too low")

        total_attempts -= 1
        print(f"You have {total_attempts} attempts remaining")


play_again = True
while total_attempts > 0 and play_again:
    x = check_choice()
    if x == 1:
        play_again = input("Do you want to play again? y or n") == "y"
        my_number = random.randint(1, 100)
        total_attempts = attempts[input("chose a difficulty: easy or hard ")]
    else:
        pass

    if total_attempts == 0:
        print("You Lost")
        play_again = input("Do you want to play again? y or n") == "y"
        my_number = random.randint(1, 100)
        total_attempts = attempts[input("chose a difficulty: easy or hard ")]
