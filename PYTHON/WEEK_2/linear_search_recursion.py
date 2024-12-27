def linear_search(list2, j, key):
    if j >= len(list2):
        return -1
    if list2[j] == key:
        return j
    j += 1
    return linear_search(list2, j, key)


list1 = []
num = int(input("Enter the number of elements in array:"))
print("Enter the elements of array:")
for i in range(num):
    list1.append(int(input(">")))

ele = int(input("Enter the element to find:"))
flag = linear_search(list1, 0, ele)
if flag == -1:
    print("Element is not found in list")
else:
    print("Element", ele, "found at index", flag)
