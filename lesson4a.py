# DICTIONARIES: collection {}
# Properties: Unoredered, No duplicates, mutable(changeable) -> keys
# Key - Value pair


student1 = ["Joseph", 34, "Male", False, ["Programming", "SQL"]]
# With Lists data is accessed using indexing

student2 = {
    "name": "Joseph",
    "age": 34, 
    "gender": "Male",
    "isPresent": False,
    "subjects": ["Programming", "SQL"],
    "scores" : {
        "programming": 100,
        "sql": 87
    }
}

print(type(student2))

# Operations
# 1. printing dictionary
print(student2)
# 2. Accessing items from a dictionary
# We use key to access a value
print(student2["gender"])
# Access subjects from the dictionary
# 3.Updating values -> we use the key
student2["age"] = 35
print(student2)
# Update value "Programming" to "Programming in Python

student2["subjects"][0] = "Programming in Python"
print(student2)

# 4. Adding items to a dictionary
student2["email"] = "joe@gmail.com"
print(student2)

# Nested Dictionary
# Access the student2 sql score
print(student2["scores"]["sql"])

# Methods - functions
print(student2.keys())
print(student2.values())

student2.clear()
print(student2)

# API - Application Programming Interface
# JSON - JavaScript Object Notation(Standard Data Format)





