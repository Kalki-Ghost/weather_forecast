import re

number = re.compile(r'\d\d\d-?\d\d\d-\d\d\d\d')
print(number)
print(number.findall("123 456 Number 123-345-6789 is found 109-833-2142 to 1234567890"))

pattern = re.compile(r'ba(wo)?man', re.IGNORECASE)
print(pattern.findall("this wo men are bawoman"))
