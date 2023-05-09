# Exercise 17. More Files

# Importing argv from the sys module and exists from the os.path module
from sys import argv
from os.path import exists

# Unpacking the command-line arguments and assigning to variables
script, from_file, to_file = argv

# Printing a message indicating which files will be copied
print(f"Copying from {from_file} to {to_file}")

# Opening the input file in read mode and assigning it to the in_file variable
in_file = open(from_file)
# Reading the contents of the input file and assigning it to the indata variable
indata = in_file.read()

# Printing the size of the input file in bytes
print(f"The input file is {len(indata)} bytes long")

# Checking if the output file already exists and printing the result
print(f"Does the output file exist? {exists(to_file)}")

# Starting a loop that prompts the user to continue or abort the operation
while True:
    try:
        input("Ready, hit RETURN to continue, CTRL-C to abort...> ")
        break
    except KeyboardInterrupt:
        print("\nAborted by user.")
        exit()

# Opening the output file in write mode and assigning it to the out_file variable
out_file = open(to_file, "w")
# Writing the contents of the input file to the output file
out_file.write(indata)

# Printing a message indicating that the operation is complete
print("alright, all done.")

# Closing both the input and output files
out_file.close()
in_file.close()

"""In this code, the argv module is used to accept two filenames as command-line arguments: the input file and the output file.
 The contents of the input file are then copied to the output file.
 The script begins by importing the argv module from the sys library, as well as the exists() function from the os.path library. 
 The script, from_file, and to_file variables are then assigned to the command-line arguments using tuple unpacking.
 The script then prints a message indicating which files will be copied, and opens the input file in read mode using the open() function.
 The contents of the input file are read into memory using the read() method and assigned to the indata variable. The size of the input 
 file is printed to the console using the len() function. The script checks if the output file already exists using the exists() function, 
 and prints the result to the console. The script then enters a loop that prompts the user to either continue or abort the operation. 
 If the user chooses to continue, the output file is opened in write mode using the open() function, and the contents of the input file are
 written to the output file using the write() method. Finally, the script prints a message indicating that the operation is complete, and 
 closes both the input and output files using the close() method."""