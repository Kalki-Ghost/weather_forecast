# dictionaries function trial
profile = {"Name": "Venkatesh K", "Age": 20, "Course": "Cse", "Father Name": "Kubendrappa", "Mother Name": "Rudramma"}
print("name" not in profile)
print(profile.values())
print(profile.keys())
print(profile.items())
print(profile.get("Name", "Not present"))
print(profile.get("class", "Not present"))
profile.setdefault("Friend", "Arun")
print(profile)
print(profile.setdefault("Name", "Arun"))
print(profile)
