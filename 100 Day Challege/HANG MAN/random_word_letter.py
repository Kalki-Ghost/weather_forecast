import random

names = ["Venkatesh", "Arun", "Ranjitha", "Rashmi", "Rudramma", "Kubendrappa"]
randomly_choice = random.choice(names)
guessed_letter = input("Enter the letter:")
for i in range(len(randomly_choice)):
    if guessed_letter == randomly_choice[i]:
        print("Right")
    else:
        print("Wrong")
print(randomly_choice)
