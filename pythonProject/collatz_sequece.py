def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return number * 3 + 1


num = 0
flag = True
while flag:
    try:
        num = int(input("Enter the number:"))
    except KeyboardInterrupt:
        print("You enter wrong value.\nPlease enter the digits.")
        continue
    if collatz(num) == 1:
        flag = False
    print(collatz(num))
