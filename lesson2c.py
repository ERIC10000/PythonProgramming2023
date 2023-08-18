# BOOLEANS (bool)

isApproved = False
print(type(isApproved))

isAbsent = True

# Booleans with Comparison Operators
# We have the following: >, <, ==, >=, <=, !=
# Comparison Operators : used to compare one variable and another

print(10 > 6)

# passwordSaved = '12345678'
# passwordRequested = input(" Enbter Your Password:  ")

# print(passwordSaved != passwordRequested)

# Logical Operators: Compare relationship btn one condition and another
# and : returns True when BOTH conditions are true
# or : ATLEAST ONE condition is True
# not : NEGATES(opposite) a condition

username = 'admin'
password = '12345678'

usernameRequested = input("Enter Username: ")
passwordRequested = input("Enter Your Password: ")

print(not(username == usernameRequested  and  password == passwordRequested) )

