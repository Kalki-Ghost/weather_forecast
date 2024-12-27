import math


def find_quadratic_eq(a, b, c):
    print("d=b*b-4ac")
    d = b * b - 4 * a * c
    if d == 0:
        print("Two roots are equal")
        print("Roots:", -b / (2 * a))
    elif d > 0:
        print("Two are distinct roots")
        print("Roots:", (-b + math.sqrt(d)) / 2 * a, (-b - math.sqrt(d)) / 2 * a)
    else:
        r = -b / (2 * a)

        print("Two are imaginary roots")
        print("Roots:")
        print(r, '+(i(', abs(d), ')/', 2 * a, ')')
        print(r, '-(i(', abs(d), ')/', 2 * a, ')')


print("Enter the value of a,b,c:")
num1 = int(input(">"))
num2 = int(input(">"))
num3 = int(input(">"))
find_quadratic_eq(num1, num2, num3)
