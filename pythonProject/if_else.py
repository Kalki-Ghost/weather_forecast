print("Hello")
i = 0
while i < 5:
    i += 1
    # if i == 3:
    #    continue
    print(i)
    if i == 3:
        break


def spam():
    global eggs
    eggs = 42
    print(eggs)


eggs = 30
print(eggs)
spam()
print(eggs)
