# Exercise 13. Parameters, Unpacking, variables

# from sys import argv
"""Read the wyss section for how to run this"""

"""The WYSS (What You Should See) section is typically used in Python code examples to show the expected output of the code. 

In the case of the sys.argv example, the WYSS section would show the expected output based on the command-line arguments passed 

to the script. To run the WYSS section for the from sys import argv example, you would need to create a Python script that uses the 

sys.argv variable to read command-line arguments, and then run the script from the command line with some arguments.

Here's an example Python script that uses sys.argv to read two command-line arguments and prints them out:"""
# from sys import argv

""" Unpack the command-line arguments into two separate variables """
# script, arg1, arg2 = argv

# Print out the values of the arguments
# print("The script is called:", script)
# print("The first argument is:", arg1)
# print("The second argument is:", arg2)

"""Assuming that you save this code in a file called script.py, you can run it from the command line with two arguments like this:"""
# $ python script.py foo bar
"""This will run the script with the command-line arguments "foo" and "bar". The expected output of this script according to the WYSS 
section would be:"""

# The script is called: script.py
# The first argument is: foo
# The second argument is: bar


from sys import argv

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# python ex.13.py Apples Oranges "Grape Fruit"
"""The output should render the following """
# The script is called: ex13.py
# The first argument is: Apples
# The second argument is: Oranges
# The third argument is: Grape Fruit 