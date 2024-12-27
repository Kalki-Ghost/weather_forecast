import pyperclip
import re

import pyperclip

message = pyperclip.paste()
code = re.compile(r'([a-zA-Z]+[0-9]+)+')
print(code.findall(message))
