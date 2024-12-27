age = int(input("Enter your age:"))
if 0 <= age < 18:
    print("Your are not eligible to vote")
elif age >= 18:
    print("Your are eligible to vote")
elif age < 0:
    print("You enter the wrong age")
