# Exercise 10. What was that... Study Drill
# Combine escape sequences and format strings to create a more complex format

# Assigning values to variables
name = "Leo"
age = 30
city = "New York"
message = "Hello, {}! You are {} years old and you live in {}."

# Using escape sequence '\n' to add a new line and formatting the message string with variables
print(message.format(name, age, city))

# Using escape sequence '\t' to add a tab character and formatting the message string with variables
print("Here's another message:\n\t{}".format(message.format(name, age, city)))