import random

print("Guess you lucky number between 1 to 10 in 5 choice")
guess = random.randint(1, 10)
i = 0
flag = False
while i < 5:
    choice = int(input("Enter the number:"))
    if choice == guess:
        flag = True
        print("Good guess!")
        break
    else:
        print("Try again!")
    i+=1
if not flag:
    print("Game over")
