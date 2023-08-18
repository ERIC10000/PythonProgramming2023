# Triangle

side1 = int(input("Enter First Side in cm : "))
side2 = int(input("Enter the Second Side in cm: "))
side3 = int(input("Enter the Third Side in cm: "))

# Equalateral 
if side1 == side2 and side2 == side3:
    print("Equalateral")

# Isoscles 
elif (side1 == side2 and side2 !=side3) or (side2 == side3 and side3 !=side1) or (side3 == side1 and side1 != side2):
    print("Isosceles")

# Scalene
elif (side1 != side2) and (side2 !=side3) and (side3 !=side1):
    print("Scalene")

else:
    print("Invalid Inputs")
