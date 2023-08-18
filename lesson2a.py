# Data Types
# Specify the format(type) of data stored on a variable e,g number, letter, colletion....
# Specify the operations done on that variable
# In python :
# Integers (int): Numbers without decimal, e,g age, month...
# Floating Points (floats): Numbers with decimal places e,g distance, height, speed..
# Strings (str): Sequence of characters enclosed inside either a double or single quotes e,g name, course
# Booleans (bool): A value having only two instances, e,g True, False,

# Collections(Arrays): list, tuple, dictionary, sets

# Strings
# type()
# Escape Sequence: used to introduce spewcial characters inside a strings \', \n

message = "I love programming"
print(type(message))

weather = 'It\'s a Chilly Morning'
print(weather)

paragraph = 'This is the first line,\n This is the second line'
print(paragraph)

firstMessage = "I love "
secondMessage = "Python"

# Concatenation - merge strings (+)

wholeMessage = firstMessage + secondMessage
print(wholeMessage)

# len(): Returns the number of characters in a String
password = input("Enter Your Password: ")
print(len(password))
