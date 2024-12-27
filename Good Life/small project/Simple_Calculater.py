# It is simple calculater to make operation on two numbers
def calculation(num1, num2, symbol):

    if num1.is_integer() or num2.is_integer():
        if symbol == '+':
            print(f"Result:{num1 + num2}")
        elif symbol == '*':
            print(f"Result:{num1 * num2}")
        elif symbol == '-':
            print(f"Result:{num1 - num2}")
        elif symbol == '/':
            print(f"Result:{num1 / num2}")
        else:
            print("Invalid symbol")
    else:
        print("Invalid numbers")


number1 = float(input("Enter the first number:"))
number2 = float(input("Enter the second number:"))
symbol = input("Enter the symbol{+,-,*,/}:")
calculation(number1, number2, symbol)
