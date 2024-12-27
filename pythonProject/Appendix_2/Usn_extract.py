import pyperclip
import re

# USN = re.compile(r'[0-9A-Z-]{10,12}')
# usn=USN.findall(pyperclip.paste())
# for us in usn:
#    print(us)

name=re.compile(r'[A-Za-z.]\D{2,}')
names=name.findall(pyperclip.paste())
for na in names:
    print(na)