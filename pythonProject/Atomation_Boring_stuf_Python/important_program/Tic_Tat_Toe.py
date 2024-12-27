import random

flag = 1
dictionary = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}


def display():
    a = 0
    for values in dictionary.values():
        print(values, "|", end='')
        a += 1
        if a % 3 == 0:
            print()
            print("-+-+-+-+-+")


display()
while flag == 1:
    print("Start the game")
    i = 0
    print('Enter your choice(* or #):')
    char = input('>')
    print('You Enter the different value it takes "*" as input value')
    comp='#'
    if char != '*' or char != '#':
        char = '*'
        comp='#'
    if char =='*':
        comp='#'
    else:
        comp='*'

    print("Choice is yours")
    while i < 9:
        choice = 1
        try:
            choice = input('Enter the block number')
        except ValueError:
            print("Please enter the digit")
            continue
        if dictionary.get(choice) != ' ':
            print('Enter the wrong block')
            continue
        else:
            dictionary[choice]=char
        display()

    computer=1
    while computer:
        temp=random.randint(1,9)
        if dictionary[temp]!=' ':
            computer=0
            dictionary[temp]=comp


