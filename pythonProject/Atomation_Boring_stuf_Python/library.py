import pprint

import pyperclip
import sys
import random

pyperclip.copy("Hello world!")
pprint.pprint("Hello world")
print(pyperclip.paste())
a = random.randint(10, 20)
print(a)
if 10 <= a < 15:
    sys.exit()
elif 15 <= a <= 20:
    print("Hello world!")

print("Continue")
