import random
import sys

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
            'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
symbol = ['@', '#', '&', '(', ')']
print("Welcome to password generate.")
number_letter = int(input("Enter the number of letters in password:"))
number_alphabet = int(input("Enter the number of alphabet in password:"))
number_digits = int(input("Enter the number of digits in password:"))
number_symbol = int(input("Enter the number of symbol in password:"))
password_list = []
if number_letter<(number_symbol+number_digits+number_alphabet):
    print("Alphabet, digits, symbols more than letters in password.")
    sys.exit()
for i in range(number_alphabet):
    password_list.append(random.choice(alphabet))
for i in range(number_digits):
    password_list.append(random.choice(number))
for i in range(number_symbol):
    password_list.append(random.choice(symbol))
random.shuffle(password_list)
password = ""
for i in range(number_letter):
    password += str(password_list[i])
print(f"Your password is:{password}")
