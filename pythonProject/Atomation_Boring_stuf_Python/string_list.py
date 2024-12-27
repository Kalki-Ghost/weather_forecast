message = "Hello"
print(message[1:4])

spam = list(message)
print(''.join(spam))
print("%%%%%%%")
# spam.sort(key=str.lower,reverse=True)
print(spam)
temp = list(range(4))
print(temp)

message1 = "Arun"
spam1 = list(message1)
spam.extend(spam1)
print(spam)
print(spam1)

print("-" * 30)
spam = "Venkatesh K"
spam=list(spam)
print(spam)
spam.sort(key=str.lower,reverse=True)
print(spam)
