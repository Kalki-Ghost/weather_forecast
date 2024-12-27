import re

gmailregex = re.compile(r'[a-zA-Z0-9_.]*@[a-zA-Z0-9_.]*')
numberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
message = "peddu2004@gmail.com is the email id of 903-561-5310"
print(gmailregex.findall(message))
print(numberRegex.findall(message))
