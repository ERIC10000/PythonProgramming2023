# Tuples: ()
# Properties: Ordered, duplicates allowed, immutable(unchangeable)
# Data from database to/from an application are enclosed on a tuple

counties = ("Nairobi", "Baringo", "Siaya", "Nairobi")
print(type(counties))

# Create a tuple of one item
# Print the type

county = ("Kisumu",)
print(type(county))

newCounty = tuple("Nakuru")
print(type(newCounty))

print(counties[0])

# Methods:
print(counties.index("Nairobi"))

newCounties = list(counties)
newCounties.append("Muranga")

counties = tuple(newCounties)
print(counties)


