from calucater_logo import logo


def addition(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def division(n1, n2):
    if n2 == 0:
        return 'Error! division by zero'
    return n1 / n2


operator = {'+': addition, '-': subtract, '*': multiply, '/': division}


def calculation():
    print(logo)
    num1 = float(input('Enter the first number:'))

    for op in operator:
        print(op)
    continue_calculation = True
    while continue_calculation:
        operation = input("Choose the operator:")
        if operation not in operator:
            print("Invalid operator! Please choose a valid operator.")
            continue
        num2 = float(input("Enter the second number:"))
        answer = operator[operation](num1, num2)
        if isinstance(answer, str):
            print("Division by zero error.")
        else:
            print(f'{num1} {operation} {num2} = {answer}')
            num1 = answer
        flag = input(
            f"To continue with {num1}, enter 'y'. To input a new number, enter 'n'. To exit, enter any other key.\n").lower()
        if flag == 'n':
            num1 = float(input('Enter the first number:'))
        elif flag != 'y':
            continue_calculation = False
            print("Good bye!")


calculation()
