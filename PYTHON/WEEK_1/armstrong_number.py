import sys

num = input("Enter the number:")
length = len(num)
number = num
try:
    number = int(num)
except ValueError:
    print("Entered number is not digits")
    sys.exit()

answer = 0
num1 = number
while num1 != 0:
    temp = num1 % 10
    answer += pow(temp, length)
    num1 //= 10

if str(answer) == num:
    print("Entered number is armstrong number")
else:
    print("Entered number is not armstrong number")
