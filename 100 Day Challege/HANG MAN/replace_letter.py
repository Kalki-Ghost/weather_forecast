import random

names = ["Venkatesh", "Arun", "Ranjitha", "Rashmi", "Rudramma", "Kubendrappa"]
randomly_choice = random.choice(names).upper()
guessed_letter = input("Enter the letter:").upper()
answer = ['_'] * len(randomly_choice)
print(answer)
for i in range(len(randomly_choice)):
    if guessed_letter == randomly_choice[i]:
        answer[i] = guessed_letter
answer1 = ''.join(answer)
print(answer1)
print(randomly_choice)
