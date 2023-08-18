# Control Flow : A way to control program execution
# Three Categories:

# 1. Sequential control flow : Default codes executed line by line (no indentation)
# 2. Conditional control flow: Codes are executed based on some conditions

# 3. Iterative Control Flow: Codes are executed a number of times based on some condtions


# CONDITIONAL:
# We have 3 conditions, if, else, else if (elif), nested if

# IF: 
# condition/expression: checked return boolean (True, Fasle)
# Statements: Code that is executed when condition is either True or False


age = 15 
if age > 18:
    print(" ISSUED WITH ID ")

else:
    print("PLEASE TRY NEXT TIME!")

# IF ELSE: One condition is checked, if condition return True if statement is executed, otherwise else statement is executed.


# Request the number from the user
# Applying the idea of modulus(%) and conditions
# Write a program to test whether a number is even(divisible by 2) or odd

number = int(input(" Enter the Number:  "))
if number % 2 == 0:
    print("EVEN NUMBER!!!")
else:
    print("ODD NUMBER!!!")


