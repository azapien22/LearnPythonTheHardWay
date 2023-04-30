# Exercise 10. What was that... Study Drill
# Combine escape sequences and format strings to create a more complex format

# Assigning values to variables
# Assigning a string value to the variable 'name'
name = "Leo"

# Assigning an integer value to the variable 'age'
age = 30

# Assigning a string value to the variable 'city'
city = "New York"

# Assigning a string with curly braces to indicate where dynamic values will be inserted to the variable 'message'
message = "Hello, {}! You are {} years old and you live in {}."

# Using the format() method to insert dynamic values into the message string and printing the resulting string
print(message.format(name, age, city))


# Printing the string literal and using escape sequence '\n' to add a new line
# Using escape sequence '\t' to add a tab character and formatting the message string with variables
print("Here's another message:\n\t{}".format(message.format(name, age, city)))