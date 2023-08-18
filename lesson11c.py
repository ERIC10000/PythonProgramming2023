# Banking System
# Account

# Parent Class
class Bank:

    def usd_exchange_rate(self, currency, rate):
        rate = rate / currency
        print(f"Your New rate is {rate}")


class Account(Bank):
    def __init__(self, name, pin, balance, accno, branch, status):
        if balance <= 0:
            print("Account bance cannot be zero!")
        elif len(name) == 0:
            print("Please Enter Account Name!")
        elif len(accno) != 6:
            print("Invalid Account Number")
        else:
            self.name = name
            self.pin = pin
            self.balance = balance
            self.accno = accno
            self.branch = branch
            self.status = status

    def withdraw(self):
        print("===WELCOME TO WITHDRAW====== \n")
        pin = int(input("Please Enter PIN: "))
        if pin == self.pin:
            print("===ACCESS GRANTED====")
            amount = int(input("Enter the Amount?: "))
            if amount <= self.balance:
                print("Sucess!")
                print(f"You have withdrawn Kshs. {amount}")
                newBalance = self.balance - amount
                print(f"Your New Balance is : {newBalance}")

            else:
                print("Insufficient Account Balance!")
        else:
            print("Wrong PIN!!!")

    # check_balance()
    def check_balance(self):
        print("===WELCOME TO CHECK BALANCE====== \n")
        pin = int(input("Please Enter PIN: "))
        if pin == self.pin:
            print("===ACCESS GRANTED====")
            print(f"Your current Balance is : {self.balance}")
        else:
            print("Wrong PIN!!!")


account1 = Account("Modcom Institute", 1234, 10000,
                   "123456", "Westlands", "active")
# account1.withdraw()
# account1.check_balance()
account1.usd_exchange_rate(10000, 140)


# In OOP Paradigm we follow some of its concepts:
# We have four concepts:
# 1.Inheritance: Child class can inherit states and behavoirs of a Parent Class

# 2.Abstraction: It hides complexities of a the program by implementing Interfaces
# 3.Encapsulation: Classes can hide their information from other classes
# 4.Polymorphism: An class can generates different instances

# Method Overloading
# Method Ovverriding
