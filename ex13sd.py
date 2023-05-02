# Exercise 13 Study drills

"""1. Try giving a fewer than three arguments to your script. See that error you get? See if you can explain?"""

"""2. Write a script that has fewer arguments and one that has more. Make sure you give the unpacked variables a good name."""
 
"""3. Combine input with argv to make a script that gets more input from a user. Just use argv to get something, and input to get
 something else from the user."""

"""4. Remember that modules give you features. Modules. Modules. Remember this because we'll need it later."""

# Study drill 1

#from sys import argv

#script, first, second, third = argv

# print("The script is called:", script)
# print("Your first variable is:", first)
# print("Your second variable is:", second)
# print("Your third variable is:", third)

# Called the script in linux terminal: python ex13sd.py Apples Oranges
# The output: ValueError: not enough values to unpack (expected 4, got 3)
# The output indicates that I am trying to unpack too few values from an Iterable object to a set of variables.
# To fix this value error is to assign 4 arguments instead of 3.

# Study drill 2. 
# script_fewer_args.py

# import sys

# script_name, arg1, arg2 = sys.argv
 
# print(f"The script name is {script_name}")
# print(f"Arg1 is {arg1}")
# print(f"Arg2 is {arg2}")
 
 
# script_more_args.py
 
# import sys
 
# script_name, arg1, arg2, arg3, arg4 = sys.argv
 
# print(f"The script name is {script_name}")
# print(f"Arg1 is {arg1}")
# print(f"Arg2 is {arg2}")
# print(f"Arg3 is {arg3}")
# print(f"Arg4 is {arg4}")


# Study Drill 3.

# script_argv_input.py

# import sys

# script_name, arg1 = sys.argv

# print(f"The script name is {script_name}")
# print(f"Arg1 is {arg1}")

# user_input = input("Enter some input: ")
# print(f"You entered: {user_input}")

"""In this script, the first argument is obtained from argv, and the second argument is obtained from the user via input. 
When the script is run, the user will be prompted to enter some input after the second argument is printed to the console. 
Note that the input function always returns a string, so if you want to perform numerical calculations with the user input, 
you may need to convert the string to a number using the int or float functions, for example:"""

# script_argv_input_numbers.py

# import sys

# script_name, arg1 = sys.argv

# print(f"The script name is {script_name}")
# print(f"Arg1 is {arg1}")

# user_input = input("Enter a number: ")
# number = float(user_input)# convert the string input to a floating number

# result = number * 2
# print(f"{number} multiplied by 2 is {result}")

"""In this modified version of the script, the user is prompted to enter a number, which is converted from a string to a floating number 
using the float function. The float is then multiplied by 2 and the result is printed to the console."""

# Call the Script on linux terminal:

# Python3 ex13sd.py 'Jesus Christ'

# The output is the following:

# The script name is ex13sd.py
# Arg1 is Jesus Christ
# Enter some input: 35
# You entered: 35
# The script name is ex13sd.py
# Arg1 is Jesus Christ
# Enter a number: 35
# 35.0 multiplied by 2 is 70.0