import random

list1 = [10, 20, 30, 40, 25]
for index, item in enumerate(list1):
    print("Index " + str(index) + " value is " + str(item))

print(random.choice(list1))
random.shuffle(list1)
print(list1)
random.shuffle(list1)
print(list1)
