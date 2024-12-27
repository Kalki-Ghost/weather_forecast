import copy

spam=[1,2,3,4,5,6]
print(spam[1:])
del spam[1]
print(spam)
print(spam.pop())
print(spam)
list=[10,20,30]
spam=spam+list
print(spam)
one,two,three=list
print(one,two,three)
spam.sort(reverse=True)
print(spam)
venk=copy.deepcopy(spam)
print("Before modification")
print(venk)
print(spam)
print("After modification")
venk.append(100)
print(venk)
print(spam)


#####@@@@String@@@@#####
spam="Hello World!"
print(spam.replace('l','a'))


print("Hello "+\
"World"+\
      "!")