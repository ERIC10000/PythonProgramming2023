# Functions: A block of code that performs a specific task on the system, that only executes when it is called(referenced)
# Mpesa USSD Applications, eg Send Money, Deposit, Withdraw, Check Balance, Change PIN

# Types of function:
# Inbuilt Functions: Already existing on the project, e,g print(), input(), range()
# User-Specific(Defined): Created by a developer, then call them when needed.e,g send_sms(), encrypt(), mpesa()

# Defining a function:
# def function_name():
#      code block

def greet():
    print("Hello, Welcome to Functions")


# Calling a function
# function_name(): Exit the function and call

# greet()

def add():
    number1 = int(input("Enter First Number: "))
    number2 = int(input("Enter Second Number:  "))
    sum = number1 + number2
    print(sum)

# add()

# create a function to perform simple interest
# call the function 

def calculate_interest():
    principal = int(input("Enter the Amount Deposited?: "))
    rate = int(input("Enter the Rate?: "))
    time = int(input("Enter the Time?: "))

    interest = (principal * rate * time)/100
    print(f" Your interest is {interest}")


calculate_interest()


