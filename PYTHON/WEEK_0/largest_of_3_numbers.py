def largestof3numbers(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print(num1, "is greater")
        return
    elif num2 > num1 and num2 > num3:
        print(num2, "is greater")
        return
    else:
        print(num3, "is greater")


print("Enter the three numbers:")
num1 = int(input(">"))
num2 = int(input(">"))
num3 = int(input(">"))
largestof3numbers(num1, num2, num3)
