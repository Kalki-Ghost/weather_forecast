import random


class BankAccount:
    def __init__(self, cust_name, balance, typeof_account, address):
        self.cust_name = cust_name
        self.account_number = random.randint(1000, 10000)
        self.balance = balance
        self.typeof_account = typeof_account
        self.address = address

    def deposit(self, amount):
        self.balance += amount
        print("Deposit is successful")
        print()

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            print("Withdraw is successful")
        else:
            print("Balance is less amount withdraw so unable to withdraw.")

        print()

    def display_details(self):
        print(f"""Customer name:{self.cust_name}
Account number:{self.account_number}
Balance:{self.balance}
Type of account:{self.typeof_account}
Address:{self.address}\n""")


person1 = BankAccount("Venkatesh", 5000, "SA", "Holalkere(tq),Chitardurga")
person1.deposit(10000)
person1.withdraw(5000)
person1.display_details()

person1 = BankAccount("Suhas", 8000, "CA", "Bangalore,Karnataka")
person1.deposit(2000)
person1.withdraw(5000)
person1.display_details()
