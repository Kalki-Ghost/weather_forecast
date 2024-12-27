# create a list
import copy

spam = []
for i in range(5):
    spam.append(i)
print(spam)

# remove
for item in spam:
    spam.remove(item)
print(spam)

# Append
for i in range(10, 15):
    spam.append(i)
print(spam)

# pop
for item in spam:
    spam.pop()
print(spam)

spam1 = []
for i in range(21, 25):
    spam1.append(i)

# Extend
spam.extend(spam1)
print(spam)

spam.reverse()
print(spam)
spam.sort()
print(spam * 3)
print(spam + [78])

# delete
del spam[len(spam) - 1]
print(spam)

print(spam.index(10))

spam1 = spam
print("spam1:", spam1)
print("spam:", spam)

spam[0] = 100
print("spam1:", spam1)
print("spam:", spam)

spam2 = copy.deepcopy(spam)
spam[1] = 450
print("spam:", spam)
print("spam1:", spam1)
print("spam2:", spam2)


