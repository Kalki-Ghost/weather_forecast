import numpy as np

arr1 = np.array([[1, 2, 3], [2, 5, 6]])
arr2 = np.array([[5, 6, 7], [10, 5, 2]])
arr3 = np.concatenate((arr1, arr2), axis=1)
print(arr3)
arr4 = np.hstack((arr1, arr2))
print(arr4)
