# For Loop in a Sequence(Collection)
# collection: string, list, tuples, dictionaries

# String Sequence
language = "Python"
for letter in language:
    print(letter)

print("=============")
# List Sequence
# loops with conditions

proLanguages = ["Python", "C", "Java", "JavaScript", "C#"]
for language in proLanguages:
    if language == "Java":
        print("Java Exists")


# Assumption:
# 1. create a list of 8 counties in Kenya
# 2. create 2 empty lists namely: single, double

# Task: loop and conditions
# Iterate through the list of 8 counties checking wether it has either single name or double name
# if it has single name append to single empty list, otherwise append to double empty lists

counties = ["Nairobi", "Taita Taveta", "Garissa", "Nakuru", "Uasin Gishu", "Homa Bay", "Muranga", "Kakamega"]

double = []
single = []

for county in counties:
    if " " in county:
        double.append(county)
    else:
        single.append(county)

print(single)
print(double)

# others methods



    
   

    