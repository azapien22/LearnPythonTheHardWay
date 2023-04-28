# Exercise 2. Comments and Pound characters
# A comment, this is so you can read your program later.
# Anything after the # is ignored by python
print("I could have code like this.") # and the comment after is ignored.
# You can also use a comment to 'disable' or comment out code:
# print("This wont run.")
print("This # will run.")
# Why does the # in: print("This # will run") not get ignored?
# the # symbol is inside a string literal. A string literal is a sequence of characters enclosed in quotes. In this case, the string is "This # will run", and the # symbol is just one of the characters in that string.
# So when this line of code is executed, the entire string "This # will run" will be passed to the print() function, and it will be printed to the console exactly as it appears, including the # symbol.