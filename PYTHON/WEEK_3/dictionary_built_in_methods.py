capitals = {'Karnataka': 'Bangalore', 'Maharashtra': 'Mumbai', 'Tamil Nadu': 'Chennai'}
print(capitals.keys())
print(capitals.values())
print(capitals.items())
print("All keys:", capitals.keys())
print("All values:", capitals.values())
print("All items:", capitals.items())
print("Capital of Karnataka:", capitals.get('Karnataka'))
print("Print Dictionary:", capitals)
other_capitals = {'Gujarat': 'Ahmedabad'}
capitals.update(other_capitals)
print("Capitals:", capitals)
print("Other_capitals:", other_capitals)
