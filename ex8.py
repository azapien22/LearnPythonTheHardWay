# Assigning a string with four curly braces to a variable called formatter
formatter = "{} {} {} {}"

# Printing the output of formatter variable with four arguments - 1, 2, 3, and 4, in the respective places of the curly braces.
print(formatter.format(1,2,3,4))

# Printing the output of formatter variable with four arguments - "one", "two", "three", and "four", in the respective places of the curly braces.
print(formatter.format("one", "two", "three", "four"))

# Printing the output of formatter variable with four arguments - True, False, False, and True, in the respective places of the curly braces.
print(formatter.format(True, False, False, True))

# Printing the output of formatter variable with four arguments - formatter itself repeated four times, in the respective places of the curly braces.
print(formatter.format(formatter, formatter, formatter, formatter,))

# Printing the output of formatter variable with four arguments - "Try your", "Own text here", "Maybe a poem", and "or a song about fear", in the respective places of the curly braces.
print(formatter.format("Try your", "Own text here", "Maybe a poem", "or a song about fear"))
