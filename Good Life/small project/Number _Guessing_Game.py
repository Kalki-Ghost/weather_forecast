# It is simple program of to guess the random number
import random


def guess_number(start, end):
    if start == end:
        print("Starting and ending number not same.")
    number = random.randint(start, end)
    attempts = 0
    while True:
        guess = int(input("Enter the number:"))
        if number == guess:
            attempts += 1
            print("You find the number in", attempts)
            break
        elif guess < start or guess > end:
            print(f"Please enter the number in between {start} to {end}")
        else:
            if number > guess:
                print("To low")
            else:
                print("To high")
            attempts += 1


start_num = int(input("Enter the starting range of number:"))
end_num = int(input("Enter the ending range of number:"))

guess_number(start_num, end_num)
