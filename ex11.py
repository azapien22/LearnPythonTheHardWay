# Exercise 11. Asking Questions:

# Using the print() function to ask the user a question and ending the output with a space character
print("How old are you?", end=' ')

# Using the input() function to read the user's response to the previous question and assigning it to the variable 'age'
age = input()

# Using the print() function to ask the user another question and ending the output with a space character
print('How tall are you?', end=' ')

# Using the input() function to read the user's response to the previous question and assigning it to the variable 'height'
height = input()

# Using the print() function to ask the user a final question and ending the output with a space character
print("How much do you weigh?", end =' ')

# Using the input() function to read the user's response to the previous question and assigning it to the variable 'weight'
weight = input()

# Using an f-string to format a message using the values of the 'age', 'height', and 'weight' variables, and printing the resulting string to the console
print(f"So, you're {age} old, {height} tall and {weight} heavy.")