# Exercise 16. Reading & Writing Files

# Importing argv from the sys module
from sys import argv

# Unpacking the command-line arguments and assigning to variables
script, filename, = argv

# Printing a message indicating the name of the file that will be erased
print(f"We're going to erase {filename}.")

# Printing instructions for the user to cancel the operation
print("If you don't want that, hit CTRL-C (^C).")

# Printing instructions for the user to proceed with the operation
print("If you do want that, hit RETURN.")

# Prompting the user to enter input to proceed or cancel the operation
input("?")

# Printing a message indicating that the file is being opened
print("Opening the file...")

# Opening the file in write mode
target = open(filename, 'w')

# Printing a message indicating that the file is being truncated
print("Truncating the file. Goodbye!")

# Truncating the file to remove all its contents
target.truncate()

# Printing a message indicating that the user will be prompted for three lines
print("Now I am going to ask you for three lines.")

# Prompting the user to enter three lines of input
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

# Printing a message indicating that the lines will be written to the file
print("I'm going to write these to the file.")

# Writing the three lines of input to the file
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# Printing a message indicating that the file is being closed
print("And finally, we close it.")

# Closing the file
target.close()
