import sys

from logo_of_game import logo
import random

print(logo)

random_number = random.randint(1, 100)
turn = 0


def number_guess(remaining_guess):
    guess = int(input("Guess the number:"))

    if random_number == guess:
        return 1
    remaining_guess -= 1
    if remaining_guess <= 0:
        return 0
    if random_number > guess:
        print("You guessed to low.")
    elif random_number < guess:
        print('You guessed to high.')
    print("Guess again.")
    print(f"Remaining {remaining_guess} attempts.")
    print()
    return number_guess(remaining_guess)


print("Welcome to number guessing game.")
print("I'a guessing number between 1 to 100.")
level = input("Choose of difficulty.Type 'easy' or 'hard':").lower()
if level == 'easy':
    turn = 10
elif level == 'hard':
    turn = 5
else:
    print("You given wrong input.")
    sys.exit()

print(f"You have {turn} attempts to guess the number.")
result = number_guess(turn)
if result:
    print("You guessed the number. You won")
else:
    print(f"Number is {random_number}")
    print("Attempts are over.You loss the game")
