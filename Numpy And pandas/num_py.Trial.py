import numpy as np

# arr = np.array(42)
# print(np.ndim(arr))
# arr1 = np.array([1, 2, 3, 4, 5])
# # print(arr1[0])
# arr2 = np.array([[1, 2, 3, 4, 5], [3, 6, 8, 4, 5]])
# # print(np.ndim(arr2))
# print(arr2[1, 1])
# arr3 = np.array([[[1, 2, 3], [6, 7, 8]], [[23, 5, 30], [5, 4, 2]]])
# # print(arr3[1, 1, 2])

# 1D array slicing
# arr = np.array([1, 2, 3, 4, 4, 5, 7, 8, 9])
# print(arr[1:5])
# print(arr[4:])
# print(arr[:4])
# print(arr[-3:-1])
# print(arr[1:5:2])
# print(arr[::2])


# 2D array slicing
arr1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr1)
print(arr1[1, 1:4])
print(arr1[0:2, 2])
print(arr1[0:2, 1:4])
print(arr1.shape)