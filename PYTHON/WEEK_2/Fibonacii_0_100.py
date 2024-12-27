def fibonacci(n):
    a = 0
    b = 1
    list1 = []
    while a <= n:
        list1.append(a)
        a = a + b
        a, b = b, a
    return list1


num = int(input("Enter the number:"))
print("Fibonacci series:", fibonacci(num))
