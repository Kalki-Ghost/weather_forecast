def add(a, b):
    """Add to number"""
    return a + b


print(add.__class__)
l = [1, 2, 34, 5, 6]
i = -1
while (i := (i + 1)) < len(l):
    print(l[i])

print([x * x if x % 2 != 0 else x for x in l])
