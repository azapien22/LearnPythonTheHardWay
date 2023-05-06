# Exercise 15. Reading Files

# Importing argv from the sys module
from sys import argv

# Unpacking the command-line arguments and assigning to variables
script, filename = argv

# Opening the file with the name passed as an argument
txt = open(filename)

# Printing a message that indicates the name of the file being read
print(f"Here's your file {filename}:")

# Reading the contents of the file and printing it to the console
print(txt.read())

# Asking the user to enter the filename again
print("Type the filename again:")
file_again = input("> ")

# Opening the file with the name entered by the user
txt_again = open(file_again)

# Reading the contents of the file and printing it to the console
print(txt_again.read())