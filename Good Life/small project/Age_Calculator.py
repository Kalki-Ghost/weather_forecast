# Calculate the age of the person by date of birth
from datetime import datetime


def age_calculator():
    print("Enter the date of birth(YYYY-MM-DD):")
    date_birth = input()
    date_birth = datetime.strptime(date_birth, "%Y-%m-%d")
    current_date = datetime.now()
    age = current_date.year - date_birth.year - (
            (current_date.month, current_date.day) < (date_birth.month, date_birth.day))
    print(f"Your are {age} year old")


age_calculator()
