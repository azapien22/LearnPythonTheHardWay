# Study Drills

#4. Get rid of lines 10-15

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
#7. For file objects it is important to close files when done. 
txt.close()

# Calling the script:
# python3 ex15sd.py scripture.txt
# Output is the following:
#Here's your file scripture.txt:
#Philippians 4:11–13
#12 I know both how to be abased, and I know how to abound: every where and in all things am instructed both to be full and to be hungry, 
# both to abound and to suffer need. 13 I can do all things through Christ which strengtheneth me.


#5. Use only input and try the script. Why is one way of getting the filename better than another?
# Prompting the user for the filename
filename = input("Enter the filename: ")

# Opening the file with the name entered by the user
with open(filename) as f:
    # Printing a message that indicates the name of the file being read
    print(f"Here's your file {filename}:")
    
    # Reading the contents of the file and printing it to the console
    print(f.read())

# In this modified version of the script, the argv module is no longer needed. Instead, the input() function is used to prompt the user for
#  the filename of the file to be read. The with statement is used to open the file and ensure that it is properly closed, even if an 
# exception is raised. The rest of the script is the same as before, with a message being printed to the console indicating the name of the
#  file being read, and the contents of the file being printed to the console using the read() method of the file object f.
