from logo_art import logo
import os


def bid():
    name = input("What is your name? ")
    biding = int(input("What is your bid? $"))
    info = {name: biding}
    return info


def clear_screen():
    # Clear command for Windows
    if os.name == 'nt':
        os.system('cls')
    # Clear command for Unix-based systems
    else:
        os.system('clear')


def winner(dictionary):
    if not dictionary:
        return None
    temp = max(dictionary, key=dictionary.get)
    return temp


print(logo)
print("Welcome to biding.")
bids = {}

while True:
    bids.update(bid())
    flag = input("Are there any bidders? Type 'yes' or 'no.").lower()
    if flag == 'no':
        key = winner(bids)
        if key:
            print(f"Winner is {key} and bidding amount is ${bids[key]}.")
        else:
            print("No bid's are placed")
        break
