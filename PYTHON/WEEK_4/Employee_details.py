import random


class Employee:
    def __init__(self, emp_name, emp_designation, emp_experience, age):
        self.emp_name = emp_name
        self.emp_designation = emp_designation
        self.emp_experience = emp_experience
        self.age = age
        self.emp_id = random.randint(100, 1000)
        self.salary = 0.0

    def add_employee(self, name, age, emp_designation, emp_experience):
        self.emp_name = name
        self.age = age
        self.emp_experience = emp_experience
        self.emp_designation = emp_designation

    def display_details(self):
        print(f"""Employee name:{self.emp_name}
Employee designation:{self.emp_designation}
Employee experience:{self.emp_experience}
Employee age:{self.age}
Employee id:{self.emp_id}
Employee salary={self.salary}""")

    def calculate_salary(self, basic):
        if self.age < 30 and self.emp_experience > 5:
            self.salary = basic * 1.5
        elif self.age < 40 and 5 < self.emp_experience < 10:
            self.salary = basic * 1.75
        elif self.age < 40 and self.emp_experience > 10:
            self.salary = basic * 2
        elif self.age < 50 and 20 < self.emp_experience < 25:
            self.salary = basic * 2.25
        elif self.age < 50 and self.emp_experience > 25:
            self.salary = basic * 2.5
        elif self.age < 58 and self.emp_experience > 30:
            self.salary = 3 * basic
        self.salary = round(self.salary, 2)


emp1 = Employee("Venkatesh", "Software Engineering", 6, 30)
emp1.calculate_salary(10_000)
emp1.display_details()
