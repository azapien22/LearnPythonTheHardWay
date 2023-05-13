# Exercise 20. Functions and files

from sys import argv 
# This line imports the argv module from the sys package. The argv module allows command-line arguments to be passed to the script.

script, input_file = argv
# Here, the script expects two command-line arguments: the script name itself (script) and an input_file to be provided. 
# The argv module returns a list of command-line arguments, and this line assigns the values to the variables script and input_file.
def print_all(f):
    print(f.read())
# This function, print_all, takes a file object (f) as a parameter and reads and prints the entire contents of the file using the read() method.   
def rewind(f):
    f.seek(0)
# The rewind function takes a file object (f) as a parameter and uses the seek() method to move the file pointer to the beginning of the file (offset 0).
def print_a_line(line_count, f):
    print(line_count, f.readline())
# The print_a_line function takes a line count and a file object as parameters. It prints the line count and reads and prints a single line from the file using the readline() method.
current_file = open(input_file)
# This line opens the input_file provided as a command-line argument and assigns the resulting file object to the variable current_file.
print("First let's print the whole file:\n")
print_all(current_file)
# This code prints a message and then calls the print_all function, passing the current_file object as an argument. It prints the entire contents of the file.
print("Now let's rewind, kind of like a tape.")
rewind(current_file)
# Similar to the previous lines, this code prints a message and then calls the rewind function, passing the current_file object as an argument. It moves the file pointer back to the beginning of the file.
print("let's print three lines:")
current_line = 1
print_a_line(current_line, current_file)
# Again, a message is printed, and the print_a_line function is called, passing current_line (set to 1) and current_file as arguments. It prints the first line of the file. ***
current_line = current_line + 1
print_a_line(current_line, current_file)
# The current_line variable is incremented by 1, and the print_a_line function is called again with the updated current_line value. It prints the second line of the file.
current_line =  current_line + 1
print_a_line(current_line, current_file)
# The current_line variable is incremented once more, and the print_a_line function is called. It prints the third line of the file.
# This sequence of code reads a file, prints its contents, rewinds the file pointer, and then prints three lines from the file with their respective line numbers.