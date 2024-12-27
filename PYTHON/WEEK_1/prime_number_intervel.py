num = int(input("Enter the number:"))
flag = False
print("Prime Numbers:", end='')
for i in range(2, num + 1):
    flag1 = False
    for j in range(2, i):
        if i % j == 0:
            flag1 = True
            break
    if not flag1:
        flag = True
        print(i, " ", end='')
if not flag:
    print("None")
