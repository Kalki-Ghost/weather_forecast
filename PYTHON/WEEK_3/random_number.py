import random
import sys

# question in 7(A)
num = 0
try:
    print("Enter the range:")
    num = int(input(">"))
    print('Enter the number of random number generate')
    n = int(input(">"))
except ValueError:
    print("You given wrong input")
    sys.exit()

i = 0
print("Even random numbers are: ", end='')
while i < n:
    random_number = random.randint(0, num)
    if random_number % 2 == 0:
        print(random_number, end=' ')
        i += 1
