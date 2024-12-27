import copy

info = {"name": "Venkatesh", "age": 20, "College": "MSRIT"}
print(info.get("nam", "Not present"))
print(info.pop("age"))
print(info.values())
dict = copy.deepcopy(info)
dict["name"] = "arun"
print(info)
print(dict)
print(dict.items())
print(list(info.items()))
print(list(dict.values()))
print(list(dict.keys()))
info.setdefault("name", "arun")
print(info)
info.setdefault("Color", "Red")
print(info)
list=[]
for i in dict.items():
    list.append(i)
print(list)
