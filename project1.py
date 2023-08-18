# USSD: Accessible by short codes e,g *444#

# Withdraw Function:

customer = {
    "pin": 2023,
    "name": "Derrick  Clerkson",
    "balance": 15000,
    "status": "active",
    "phone": "+254740922861"
}

# Withdraw
def withdraw(pin, amount, agent_no):
    print("====WELCOME====")
    if pin == customer['pin']:
        print("===ACCESS GRANTED====")
        if amount <= customer["balance"]:
            print(f"Confirmed. Successfully withdrawn Kshs {amount} from Agent No. {agent_no}")
            balance = customer["balance"] - amount
            print(f"Your Balance is {balance}")
            print("Thank You!!!")
        else:
            print("Insuffient Account Balance")
            print("Try Again!!!")

    else:
        print("====ACCESS DENIED===")
        print("Wrong PIN!!!")

# Deposit
def deposit(pin, amount, agent_no):
    print("====WELCOME TO DEPOSIT====")
    if customer["status"] == "active":
        if pin == customer["pin"]:
             print("===ACCESS GRANTED====")
             print("PLEASE WAIT.......")
             current_balance = amount + customer["balance"]
             print(f"Thank You for Depositing At Agent no. {agent_no}")
             print(f"Your Current  Balance is {current_balance}")

        else:
            print("====ACCESS DENIED===")
            print("Wrong PIN!!!")

    else:
        print("===Sorry!, Please Activate Your Account====")

# check balance
def check_balance(pin):
    if customer["status"] == "active":
        if pin == customer["pin"]:
            print(f"Confirmed Your Current Balance is {customer['balance']}")

        else:
            print("====ACCESS DENIED===")
            print("Wrong PIN!!!")

    else:
        print("===Sorry!, Please Activate Your Account====")


# Change PIN

# current pin
# new pin
# confirm pin

def check_pin(current, new, confirm):
    if customer["status"] == "active":
        if current == customer["pin"]:
            if new == confirm:
                customer["pin"] = new
                print("PIN updated succesfully")
                print(f"Your new PIN is {customer['pin']}")

            else:
                print("Failed, PIN Dont Match!!!")

        else:
            print("Wrong, PIN")

    else:
        print("Please Activate Your Account")



def menu():
    print("SIMPLE MPESA USSD APP")
    print("====WELCOME====")
    print("\n")

    print("1. Withdraw")
    print("2. Deposit")
    print("3. Check Balance ")
    print("4. Change PIN")
    print("5. Loans and Saving")
    print("6. Fuliza Mpesa")
    print("0. Exit")
    print("")

    while True:
        option = int(input(" Please Enter Your Choice?:  "))
        if option == 1:
            withdraw(  int(input(" Enter Your PIN: ")), int(input(" Enter the Amount: ")), int(input(" Enter Agent No.: "))  )

        elif option == 2:
            deposit( int(input(" Enter Your PIN: ")),  int(input(" Enter the Amount: ")), int(input(" Enter Agent No.: ")))

        elif option == 3:
            check_balance( int(input(" Enter Your PIN?: ")) )

        elif option == 4:
            check_pin( int(input("Enter Your Current PIN?: ")), int(input("Enter Your New PIN?: ")), int(input("Confirm Your PIN?: ")) )

        elif option == 0:
            break

        else:
            print("Other options on Development")

menu()


