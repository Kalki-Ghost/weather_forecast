def binary_search(arr, low, high, key):
    arr.sort()
    while low < high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return -1


list1 = [9, 7, 4, 6, 1, 3, 5]
ele = 9
size = len(list1)
flag = binary_search(list1, 0, size, ele)
if flag == -1:
    print("Element is not found")
else:
    print("Element", ele, "found at index", flag)
