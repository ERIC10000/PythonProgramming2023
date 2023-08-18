# Collections(Arrays): groups of data on the same variable
# We have: 
# List : []
# Tuple: ()
# Dictionary : {}
# Sets: {}

student1 = "Sally"
student2 = "Bob"
student3 = "Jane"

students = ["Sally", "Bob", "Jane"]

# List: Stores data in collection using a sqaure bracket, each comma separated
# Properties: Ordered, mutable(changeable), allow duplicate data

counties = ["Nakuru", "Kajiado", "Nyandarua", "Bomet", "Wajir", "Nairobi"]
student = ["Sally", 23, False, 3.57]
print(type(counties))

# List Operations
# 1. printing elements of a list
print(counties)
# 2. Accessing items on a list
# Ordered: Indexing -> Items are given numeric values starting from zero
print(counties[2])
# print the forth item from the list
print(counties[3])
# 3. range of values (:)
# the first index included, but the last index is excluded.
print(counties[1:])
print(counties[:3])
print(counties[1:3])
# print the 2nd, 3rd, 4th, 5th
print(counties[1:5])
# All the items
print(counties[0:6])
print(counties[:])

# 4. List methods
# a) Add a new item to the list -> append()
counties.append("Nyeri")
print(counties)

# counties.append("Kilifi")
# counties.append("Mombasa")

newCounties = ["Kilifi", "Mombasa"]
counties.extend(newCounties)
print(counties)

# append and extend, add items to end of the list
# insert(0, ""): 
counties.insert(1, "Kwale")
print(counties)

# b) Removing item from a list
counties.pop(3)
print(counties)

# counties.remove("Nyandarua")
print(counties)
print(len(counties))

counties[2:2] = ["Migori", "Kisumu"]
print(counties)

# counties.clear()
# print(counties)

print(counties.count("Kajiado"))


