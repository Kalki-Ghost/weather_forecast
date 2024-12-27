# It is the game of the rock paper scissors
import random


def game():
    print("Start the game of the Rock Paper Scissor:")
    choices = ['rock', 'paper', 'scissor']
    computer = random.choice(choices)
    user_choice = input("Enter your choice('rock','paper','scissor'):").lower()
    if user_choice == computer:
        print("Match tie")
    elif (user_choice == "rock" and computer == 'scissor') or \
            (user_choice == 'paper' and computer == 'rock') or \
            (user_choice == 'scissor' and computer == 'paper'):
        print("You won")
    else:
        print(f"Computer choice is {computer}")
        print("You lose")


while True:
    game()
    flag = int(input("Enter the choice:1.Continue the game 2.End the game:"))
    if flag == 2:
        print("Good bye!")
        break
