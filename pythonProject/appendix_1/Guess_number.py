import random
print("Welcome,to the game")
secret_num=random.randint(1,20)
print("Enter the number between 1 to 20")
i=1
while(i<=6):
    print("Enter the number")
    try:
        num=int(input(">"))
        if(num>secret_num):
            print("You enter to high number")
        elif num<secret_num:
            print("You enter to low number")
        else:
            break
        i+=1

    except ValueError:{
        print("Please enter the number in digit")
    }
if(i==6+1):
    print(f"Nope! you not guess the correct number.Secret number is {secret_num}")
else:
    print(f"You guessed the secret number in {i} attempts")
