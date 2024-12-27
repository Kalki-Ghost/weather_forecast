print("Welcome to tip calculater!")
total_bill = input("What is the total bill?\n$ ")
tip = input("How much tip would you like to give?  10,12, or 15?\n")
number_people = input("How many people to split the bill?\n")
each_one = float(total_bill) / int(number_people)
tip = each_one * int(tip) / 100
print(f"Each person should pay:$%.2f" % round(each_one + tip, 2))
