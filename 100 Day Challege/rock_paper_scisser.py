import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Lets start the game")
choice = int(input("Enter 0>Rock 1>Paper 2>Scissor.>\n"))
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)

if 0 > choice or choice > 2:
    print("Wrong choice.")
else:
    print("Computer choice:")
    random_num = random.randint(0, 2)
    if random_num == 0:
        print(rock)
    elif random_num == 1:
        print(paper)
    else:
        print(scissors)

    if choice == random_num:
        print("Match draw.")
    elif choice == 0 and random_num == 1:
        print("You loss.")
    elif choice == 0 and random_num == 2:
        print("You won.")
    elif choice == 1 and random_num == 0:
        print("You won")
    elif choice == 1 and random_num == 2:
        print("You loss.")
    elif choice == 2 and random_num == 0:
        print("You loss.")
    elif choice == 2 and random_num == 1:
        print("You won")
