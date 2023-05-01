# Can you find other ways to use Python's input()? Try some of the samples you find. 

# Ask the user for their name and store it in a variable
name = input("What is your name? ")

# Print a personalized message to the user using their name
print(f"Hello, {name}! Welcome to my program.")

""" In this example, the input() function is used to ask the user for their name and store the input in the name variable. 
The function takes an optional string argument that is used as the prompt to display to the user. 
In this case, the prompt is "What is your name?". The input from the user is then used to create a personalized greeting message
 using an f-string. Finally, the message is printed to the console using the print() function."""

# Write another "form" like this to ask some other questions.

# Ask the user for their name and store it in a variable
name = input("What is your name? ")

# Ask the user for their age and store it in a variable
age = input("How old are you? ")

# Ask the user for their city of residence and store it in a variable
city = input("What city do you live in? ")

# Print a personalized message to the user using their input
print(f"Hello, {name}! You are {age} years old and you live in {city}.")

"""In this example, we use input() three times to ask the user for their name, age, and city of residence, and store the responses 
in the name, age, and city variables. We then use these variables to create a personalized message using an f-string, and print the
 message to the console using the print() function."""