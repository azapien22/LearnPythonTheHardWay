# Exercise 6. Strings and Text
# Set the number of types of people
types_of_people = 10

# Use an f-string to create a string containing the number of types of people
x = f"There are {types_of_people} types of people."

# Define two string variables
binary = "binary"
do_not = "don't"

# Use an f-string to create a string containing the two string variables
y = f"Those who know {binary} and those who {do_not}"

# Print the string containing the number of types of people
print(x)

# Print the string containing the two string variables
print(y)

# Use an f-string to include the string containing the number of types of people in a sentence
print(f"I said: {x}")

# Use an f-string to include the string containing the two string variables in a sentence
print(f"I also said: '{y}'")

# Define a boolean variable
hilarious = False

# Define a string variable with a placeholder for a value
joke_evaluation = "Isn't that joke so funny?! {}"

# Use the .format() method to insert the value of the hilarious variable into the joke_evaluation string
print(joke_evaluation.format(hilarious))

# Define two string variables
w = "This is the left side of..."
e = "a string with a right side."

# Concatenate the two strings using the + operator
print(w + e)

# The following code illustrates a string within a string:
# x = f"There are {types_of_people} types of people."
# y = f"Those who know {binary} and those who {do_not}"
# print(f"I said: {x}")
# print(f"I also said: '{y}'")
# joke_evaluation = "Isn't that joke so funny?! {}"
# print(joke_evaluation.format(hilarious))

# Explain why adding the two strings w and e with "+" makes a longer string
# Adding variable w and variable e concatenates the 2 strings which means it combines
# the 2 string making it one full sentence.