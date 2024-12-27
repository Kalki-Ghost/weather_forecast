"""The program to calculate the bill pay by each person in the group."""

print("Welcome to tip calculater.")
total_bill = float(input("Enter the total bill?$"))
tips = int(input("How much tip would you like to give?10, 12, or 15? "))
persons = int(input("How many people to split the bills?"))
print(f"Each person should pay: ${round((total_bill * (1+tips / 100)) / persons, 2)}")
