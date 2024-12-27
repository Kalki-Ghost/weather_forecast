def display_minmax(list):
    minimum = list[0]
    maximum = list[0]
    for j in list:
        if minimum > j:
            minimum = j
        if maximum < j:
            maximum = j
    print("Minimum item in array is", minimum)
    print("Maximum item in array is", maximum)
    return min

def displaySecondMax(list):
    first = display_minmax(list)
    min = list[0]
    for i in list:
        if min > i and first != i:
            min = i
    print("Second minimum element is", min)


num = int(input('Enter the number of item:'))
print("Enter the elements:")
list = []
for i in range(0, num):
    list.append(int(input(">")))
displaySecondMax(list)

