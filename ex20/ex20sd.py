# Study Drills:

#2:
"""Each time print_a_line is run, you are passing in a variable, current_line. Write out what current_line 
is equal to on each function call, and trace how it becomes line_count in print_a_line."""

from sys import argv 

script, input_file = argv

def print_all(f): # 3: Correct argument
    print(f.read())
    
def rewind(f): # 3: Correct argument
    f.seek(0)
    
def print_a_line(line_count, f): # 3: Correct argument
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)


print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("let's print three lines:")

current_line = 1 #2 Answer: Current line is set to 1
print_a_line(current_line, current_file)

current_line += current_line #2 & #5 Answer: current line is set to 1 + 1 = 2
print_a_line(current_line, current_file)

current_line += 1 #2 & # 5 Answer: current line is set to 2 + 1 = 3
print_a_line(current_line, current_file)

# 3: Find each place a function is used, and check its def to ensure accurate arguments. 

#4:
# Research the seek function for file:
"""The seek() function in Python is used to change the position of the file handle within a file. In the context of the code snippet you
provided, the rewind() function takes a file object f as a parameter and uses f.seek(0) to move the file handle or pointer to the beginning 
of the file. """
# Here's an explanation of how seek(0) works:
# 1. The seek() function is called on the file object f.
# 2. The parameter 0 passed to seek() indicates that we want to move the file handle to the beginning of the file. 
# In Python, the offset 0 represents the start of the file.
# 3.After executing f.seek(0), the file handle is positioned at the beginning of the file, ready to read from the start again.
"""This function is commonly used to "rewind" or reset the file handle to the beginning of a file so that subsequent 
read operations start from the beginning rather than continuing from the current position.
In the code snippet you provided, the rewind() function is used to reset the file handle f to the beginning of 
the file before performing subsequent read operations."""

# 5: Research the shorthand notation +=, and rewrite the script to use += instead.