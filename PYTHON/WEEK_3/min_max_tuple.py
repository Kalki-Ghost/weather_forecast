import random
import sys


def max_min_k_elements(arr, i):
    arr1 = sorted(arr)
    if len(arr1) < i * i:
        return arr1
    else:
        minimum = arr1[:i]
        maximum = arr1[-i:]
        arr1 = minimum + maximum
        return arr1


array = ()
size = 0
try:
    size = int(input("Enter the size of tuple:"))
except ValueError:
    print("You not give correct input.")
    sys.exit()
for j in range(size):
    temp = random.randint(1, 100)
    array += (temp,)
print(array)
print(max_min_k_elements(array, 2))
