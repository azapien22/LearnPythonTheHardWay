
# Define a variable with a string that has four placeholders
formatter = "{} {} {} {}"

# Use the .format() method to insert the values 1, 2, 3, and 4 into the placeholders and print the resulting string
print(formatter.format(1,2,3,4))

# Use the .format() method to insert the strings "one", "two", "three", and "four" into the placeholders and print the resulting string
print(formatter.format("one", "two", "three", "four"))

# Use the .format() method to insert the boolean values True, False, False, and True into the placeholders and print the resulting string
print(formatter.format(True, False, False, True))

# Use the .format() method to insert the formatter variable into each placeholder and print the resulting string
print(formatter.format(formatter, formatter, formatter, formatter,))

# Use the .format() method to insert the given strings into the placeholders and print the resulting string
print(formatter.format("Try your", "Own text here", "Maybe a poem", "or a song about fear"))