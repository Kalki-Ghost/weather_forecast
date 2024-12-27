def search(array, ke):
    for i in range(len(array)):
        if array[i] == ke:
            return i
    return -1


arr = [10, 30, 50, 20, 40, 60]
key = int(input("Enter the element to find:"))
ans = search(arr, key)
if ans == -1:
    print("Key is not found in list")
else:
    print("Key found at", ans)
