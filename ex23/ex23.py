"""This script reads a file "languages.txt" and then encodes and decodes each line using the 
given encoding and error handling method. Here is the line-by-line explanation of your script:"""

"""The sys module provides access to some variables used or maintained by the Python interpreter and to functions that 
interact strongly with the interpreter. In this case, it's used to get command-line arguments."""
import sys

"""sys.argv is a list in Python, which contains the command-line arguments passed to the script. 
Here, the script expects three command-line arguments: the script name, the encoding type, and the error handling method."""
script, encoding, error = sys.argv
"""This is the definition of the function main which expects three parameters: the file to read, 
the encoding type, and the error handling method."""
def main(language_file, encoding, errors):
    
    # This reads one line from the file language_file.
    line = language_file.readline()
    """This checks if the line read is not empty (not the end of the file). If it's not empty, it passes this line to the print_line 
    function (which encodes and decodes the line), then calls itself (recursively) to process the next line."""
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
# This is the definition of the function print_line which takes a line of text, an encoding, and an error handling method as parameters.    
def print_line(line, encoding, errors):
    next_lang = line.strip() # This removes the leading and trailing whitespaces from the line.
    raw_bytes = next_lang.encode(encoding, errors = errors) # This encodes the string next_lang into bytes using the specified encoding and error handling method.
    cooked_string = raw_bytes.decode(encoding, errors = errors) # This decodes the bytes raw_bytes back into a string using the same encoding and error handling method.
    print(raw_bytes, "<===>", cooked_string) # This prints the encoded bytes, a separator string, and the decoded string.
# This opens the file "languages.txt" with UTF-8 encoding and assigns the file object to languages.
languages = open("languages.txt", encoding="utf-8")

"""This calls the main function with the languages file object, the encoding type, and the error handling method to start processing 
the lines of the file. The purpose of this script is to demonstrate how encoding and decoding works in Python, and how the same string 
can be represented in different forms (raw bytes and cooked string)."""

main(languages, encoding, error)