import pprint

message = "Venkatesh K"
letters = {}
for ch in message:
    # setdefault function take key and value pair. ch is key and "0" is value
    letters.setdefault(ch, 0)
    letters[ch] = letters[ch] + 1
print(letters)
pprint.pprint(letters)
# letters.pop("K")
# print(letters)
# list1 = [1, 2, 3, 4]
# list1.append(letters)

# print(list1)
