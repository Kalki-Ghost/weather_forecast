print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")
direction = input("You're at a cross road.Where do you want to go? Type 'left' or 'right'\n")
if direction.lower() == 'left':
    print("You come to lake.There is an island in the middle of the lake.")

    flag = input("Type 'wait' to wait for a boat.Type 'swim' across.")
    if flag.lower() == 'wait':
        print("You arrive at the island unharmed.There is a house with 3 doors.")
        room = input("One Yellow and one Red and one Blue.Which colour do you choice.")
        if room.lower() == "yellow":
            print("You won the game.You got the treasure.")
        elif room.lower() == 'red':
            print("It's a room full of fire.Game Over.")
        elif room.lower() == 'blue':
            print("It's a room full of beast.Game Over.")
        else:
            print("You enter the wrong choice.")

    elif flag.lower() == 'swim':
        print("You caught by angry whale.Game over.")
    else:
        print("You enter the wrong choice.")
elif direction.lower() == 'right':
    print("You fell into a hole.Game Over.")
else:
    print("You enter the wrong choice.")
