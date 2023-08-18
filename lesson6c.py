# Nested if Conditions
# Money Withdrawal Application

account = {
    "PIN": "1234",
    "name": "Derrick",
    "balance": 10000
}

print("===WELCOME TO ABC BANK=====")

while True:
    pin = input("Enter Your PIN: ")
    if pin == account["PIN"]:
        print(f"===KARIBU {account['name']} ====")
        amount = int(input(" Enter the Amount to Withdraw:  "))
        if amount <= account["balance"]:
            print(f" Confirmed. Withdrawn Kshs  {amount}")
            newBalance = account["balance"] - amount
            print(f"Your Balance is {newBalance}")
            print("======CONTINUE WITH TRANSACTION=====")
            

        else:
            print("Insufficient Account Balance...")
            print(f" Your Balance is {account['balance']}")

    else:
        print("Wrong PIN, Try Again!!!")