# SIMPLE LOGIN SYSTEM

user = {
    "username": "user123",

    "password": "1234",

    "timeline1": {
        "username": "BigBuzz",
        "posted": "LIVE IN NAIVASHA"
    },


    "timeline2": {
        "username": "Coderz",
        "posted": "Working on my Bootstrap"
    }

}

# user authentication
username = input("Enter Your Username: ")
password = input("Enter Your Password: ")
if not(username == user["username"] and password == user["password"]):
    print("======WELCOME TO FACEBOOK=======")
    print(user["timeline1"])
    print("================================")
    print(user["timeline2"])

else:
    print("=========ACCESS DENIED===========")
    print("==========TRY AGAIN!!!===========")

# Task1:
# Attack(Hack) the system to grant access with only your username
# Task2:
# Granted Access with both wrong credential


# Mpesa Application
# Deposit
# Withdraw
# Check Balance
# Change Pin
# Send Money


