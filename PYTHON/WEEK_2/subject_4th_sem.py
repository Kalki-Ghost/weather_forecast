list = ["MATHS", "MC&IOT", "DAA", "DCN", "FAIL", "DAA LAB", "DCN LAB", "Python Programming Lab", "DATA ANALYSIS R"]
print("Print list using for loop")
for item in list:
    print(item,',',end='')

print()
print("2nd element", list[1])
print("5th element", list[4])
print()
print("First 4 elements of the list")
for item in range(4):
    print(list[item])
print()
print("Last 4 elements of the list")
for item in range(-4,0,1):
    print(list[item])
print()
print("'Python Programming Lab' in list:", 'Python Programming Lab' in list)
print()
list.append("Intra Internship")
print("Append:", list)
list.insert(2, "DCN LAB")
print("Insert:", list)
print()
list.remove("DCN LAB")
print("Remove:", list)
print("Pop:", list.pop())
print()
list.sort()
print("Ascending order:", list)
list.reverse()
print("Descending order:", list)

print()
subject = ["python"]
list.extend(subject)
print(list)
