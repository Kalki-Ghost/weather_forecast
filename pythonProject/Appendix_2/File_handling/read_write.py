import os

read = open(r'C:\Users\peddu\PycharmProjects\pythonProject\hello.py', 'w+')
read.write("Venkatesh is a good friend")
read.seek(0)
print(read.readlines())
read.close()

hello = open(r'hello.txt', 'w')
hello.write(r'''Hello,Venkatesh
How are you?
This is good day''')
hello.close()

print(os.path.isabs(r'C:\Users\peddu\PycharmProjects\pythonProject\Appendix_2\File_handling\hello.txt'))
print(os.getcwd())
print(os.path.basename(r'C:\Users\peddu\PycharmProjects\pythonProject\Appendix_2\File_handling\hello.txt'))
print(os.sep)
