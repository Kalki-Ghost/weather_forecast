row = int(input("Enter the number of row:"))
for i in range(row + row):
    sum = row-1 - i
    if sum > 0:
        for j in range(i + 1):
            print("* ", end='')
    else:
        for z in range(row - abs(sum)):
            print("* ", end='')
    print()
