import re

message = """.FLUID
Loop Component
.SMF
StarMath Formula File
.DAT
Geometry Dash Saved Data
.DOC
Microsoft Word D"""
code = re.compile(r"(\.[A-Za-z]*)+")
code1 = re.compile(r'\b(?<!\.)\w+\b')
print(code.findall(message))
print(code1.findall(message))
