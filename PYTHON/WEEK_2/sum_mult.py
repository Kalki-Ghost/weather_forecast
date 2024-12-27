def sum(list):
    add = 0
    for item in list:
        add += item
    return add


def multiply(list):
    mul = 1
    for item in list:
        mul *= item
    return mul


num = int(input('Enter the number of item:'))
print("Enter the elements:")
list = []
for i in range(0, num):
    list.append(int(input(">")))

print("Addition:", sum(list))
print("Multiplication:", multiply(list))
