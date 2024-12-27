num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
print('''Enter
1.addition
2.subtraction
3.multiplication
4.division''')
choice = int(input(">"))
if choice == 1:
    print("Addition of number is", num1 + num2)
elif choice == 2:
    print("Subtraction of number is", num1 - num2)
elif choice == 3:
    print("Multiplication of number is", num1 * num2)
elif choice == 4:
    print("Division  of number is", num1 / num2)
else:
    print("You enter the wrong choice")
