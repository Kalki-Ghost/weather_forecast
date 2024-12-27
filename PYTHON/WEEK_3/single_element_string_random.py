import random
import sys

# question 7(B)
string = input("Enter the String:")
length = len(string)
value = random.randint(0, length - 1)
print("Random element in string is:", string[value])


# question 7(c)
number = 0
try:
    range_num = int(input("Enter the range of random number:"))
    value = int(input("Enter the number of unique random element to generate(>range):"))

except ValueError:
    print("You given wrong input.")
    sys.exit()

list1 = []
if range_num < value:
    for i in range(range_num+1):
        list1.append(i)

else:
    i = 0
    while i < value:
        random_number = random.randint(0, range_num)
        if random_number not in list1:
            list1.append(random_number)
            i += 1

print("Unique random number:", list1)
