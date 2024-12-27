# This shebang-like line is for Unix-like systems; it has no effect on Windows.
# !/usr/bin/env python


# Strings = "HelloVenkatesh"
# print(Strings.upper().isupper()
# print(Strings.isalpha())
# print(Strings.isalnum())
# print(Strings.isdecimal())
# Strings="123A"
# print(Strings.isspace())
# print(Strings.isalpha())
# print(Strings.isa#lnum())


Strings = "hello World"
print(Strings.rjust(30, '#').ljust(40, '@'))
print(Strings.ljust(10, '!'))
print(Strings.center(20, '*'))
Strings = Strings.center(20, '$')
print(Strings)
print(Strings.rstrip('$'))
print(Strings.strip('$'))
print("%s" % Strings)
