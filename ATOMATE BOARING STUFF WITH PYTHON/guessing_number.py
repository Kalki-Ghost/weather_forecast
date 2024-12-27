import random

print("Hello,What is your name.")
name = input()
number = random.randint(1, 20)
lives = 1
while lives <= 6:
    guess = int(input("Enter the number between 1 to 20:"))
    if guess > number:
        print("Your guess is too high")
    elif guess < number:
        print("Your guess is too low")
    else:
        print(f"You guessed number.{name}! You guessed the number in {lives} guesses!.")
        break
    lives = lives + 1

if guess != number:
    print(f"{name} lives are over.Number is {number}.")
