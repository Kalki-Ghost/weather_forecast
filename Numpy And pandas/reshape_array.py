import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
arr1 = arr.reshape(2, 6)
print(type(arr1))
print(arr1)
arr2 = arr.reshape(2, 3, 2)
print(arr2)
arr3 = arr.reshape(4, 3)
print(arr3)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
print(arr.reshape(2, 2, 2, 2))

arrr = arr.resize(2, 8)
print(arr)

# More D array to 1D Array
print(arr3.reshape(-1))

arr = np.array([1, 2, 3, 4, 5, 6])
for x in arr:
    print(x)

arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
    for y in x:
        print(y)
