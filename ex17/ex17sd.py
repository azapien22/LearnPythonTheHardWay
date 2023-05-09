# Study Drill 1: Remove features to make the script more friendly.

from sys import argv
from shutil import copyfile

script, from_file, to_file = argv

copyfile(from_file, to_file)

print(f"{from_file} has been copied to {to_file}.")

"""n this version, we've imported the copyfile() function from the shutil library, which provides a higher-level interface for copying files. 
We then use this function to copy the contents of the from_file to the to_file, without prompting the user for confirmation.
Finally, we print a message to the console indicating that the copy operation was successful."""

# Study Drill 2: Shorten code to one line

import shutil
shutil.copy('/home/subdeus369/Coding Practice/LearnPythontheHardWay/ex17/romans.txt', '/home/subdeus369/Coding Practice/LearnPythontheHardWay/ex17/new_file.txt')

"""Yes, you can copy a file in Python using a single line of code using the shutil.copy() function.
Replace /path/to/source/file with the path to the file you want to copy, and /path/to/destination/file 
with the path to where you want to copy the file."""

# Study Drill 3: Type Man cat to read about it.

"""Concatenate files and print on the standard output"""

# Study Drill 4: Find out why you had to write out_file.close() in the code.

"""Because the out_file was opened in order to be written "w" and thus needs to be closed.
In order to avoid closing files after opening it is better to use a with statement such as 'with open(filename) as f:'
as it is self closing. """

# Study Drill 5: Read about pythons import statement and start python3.6 and try it out. Try importing some things

# Importing the math module
import math

# Using the sqrt() function from the math module
x = math.sqrt(25)
print(x)

