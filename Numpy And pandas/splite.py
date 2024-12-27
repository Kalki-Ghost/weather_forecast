import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
new_arr = np.array_split(arr, 4)
print(new_arr)

arr1 = np.where(arr % 2 == 0)
print(arr1)
