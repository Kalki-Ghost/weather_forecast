import sys


def list_tuple(arr, string):
    length = len(string)
    temp = (string, length)
    arr.append(temp)


def sort(arr):
    i = 0
    while i < len(arr) - 1:
        minimum = i
        k = i + 1
        while k < len(arr):
            if arr[minimum][1] > arr[k][1]:
                minimum = k
            k += 1
        arr[i], arr[minimum] = arr[minimum], arr[i]
        i += 1


array = []
try:
    number = int(input("Enter the number of strings:"))
except ValueError:
    print("Enter the wrong input. Program is terminated")
    sys.exit()
for num in range(number):
    names = input(str(num+1) + ".Enter the String:")
    list_tuple(array, names)

print(array)
sort(array)
print("Sorted list of tuple is:", array)
