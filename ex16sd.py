# Study Drill 1. Comment each line of code.

filename = input("Enter the filename: ")

print(f"We're going to erase {filename}.")

print("If you don't want that, hit CTRL-C (^C).")

print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")

with open(filename, "w+") as f:

    print("Truncating the file. Goodbye!")

    f.truncate()

    print("Now I am going to ask you for three lines.")

    line1 = input("Line 1: ")

    line2 = input("Line 2: ")

    line3 = input("Line 3: ")

    print("I'm going to write these to the file.")

    f.write(line1)

    f.write("\n")

    f.write(line2)

    f.write("\n")

    f.write(line3)

    f.write("\n")

    f.seek(0)

    newfile = f.read()

    print(newfile)

#Study Drill 2

from sys import argv

script, filename = argv

print(f"May I read the {filename} you just created?")

input("> ")

print("opening file...")

with open(filename) as f:

    print(f.read())
    
# Study Drill 3 Remove the redundancy using stings, formats, and escapes to print the lines with just one target.write()

filename = input("Enter the filename: ")

print(f"We're going to erase {filename}.")

print("If you don't want that, hit CTRL-C (^C).")

print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")

with open(filename, "w+") as f:

    print("Truncating the file. Goodbye!")

    f.truncate()

    print("Now I am going to ask you for three lines.")

    line1 = input("Line 1: ")

    line2 = input("Line 2: ")

    line3 = input("Line 3: ")

    print("I'm going to write these to the file.")

    f.write(f"{line1}\n{line2}\n{line3}\n")

    f.seek(0)

    newfile = f.read()

    print(newfile)

#Study Drill 4. Find out why we had to pass a "w" as an extra parameter to open.
"""In Python, the open() function is used to open files for reading, writing, or appending data. The first argument to the open() function 

is the filename, which is the name of the file that you want to open. The second argument is the mode in which you want to open the file, 

which can be "r" for reading, "w" for writing, or "a" for appending. In the code you provided, the second argument to open() is "w", which 

stands for write mode. When a file is opened in write mode, you can write new data to the file, which will overwrite any existing data in the file. 

If the file does not exist, it will be created. The "w" mode is used here because the code is likely intending to write some data to the file. 

By passing "w" as the mode argument, the code ensures that any existing data in the file is erased and replaced with the new data. 

Additionally, the with statement is used in conjunction with open() to ensure that the file is properly closed when the block of code is 

finished executing. This is important because leaving files open can cause issues with data consistency and memory usage. By using the with 

statement, the file will be closed automatically when the block of code is finished executing, regardless of any errors that may occur.."""


# Study Drill 5. If you open the file with "w" mode, then do you really need the truncate() function?
"""
No, if you open a file in "w" mode (write mode), it will automatically truncate the file to zero length if it already exists, or create a 

new file if it doesn't exist. Therefore, using truncate() function after opening the file in "w+" mode is not necessary. Here's the updated

 code with the unnecessary truncate() function removed:"""

filename = input("Enter the filename: ")

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
input("?")

print("Opening the file...")
with open(filename, "w+") as f:

    print("Now I am going to ask you for three lines.")
    line1 = input("Line 1: ")
    line2 = input("Line 2: ")
    line3 = input("Line 3: ")

    print("I'm going to write these to the file.")
    f.write(f"{line1}\n{line2}\n{line3}\n")

    f.seek(0)
    newfile = f.read()

    print(newfile)

"""In this code, we have removed the truncate() function call and opened the file in "w" mode instead of "w+" mode. The rest of the code

 remains the same."""