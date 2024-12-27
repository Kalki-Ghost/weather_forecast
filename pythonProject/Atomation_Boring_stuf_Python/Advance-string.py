
alp = "abc"
num = '123'
alp123 = 'abc123'
space = "  "
tit = "Arun Is Good Friend"
print(alp.isalpha())
print(num.isdecimal())
print(alp123.isalnum())
print(space.isspace())
print(tit.istitle())
print("*" * 20)
print(alp.istitle())
print(alp123.isalpha())
print(alp.isascii())
print(alp.startswith('c'))
print(alp.startswith('a'))
print(alp.encode())
print(alp.split(' '))
print(alp.center(10,'*'))
alp = alp.rjust(20, '*')
print(alp)
alp = alp.lstrip('*')
print(alp)
alp = alp.ljust(20, '*')
print(alp)
alp = alp.strip('*')
print(alp)
