# Exercise 24 More Practice:
#This line prints the string "Let's practice everything" to the console.
print("Let's practice everything")
#This line prints the string "You'd need to know 'bout escapes with \ that do:" to the console. The backslash \\ is used 
# as an escape character to indicate that the following character should be treated differently, in this case, escaping the single quote.
print("You'd need to know \ 'bout escapes with \\ that do:")
# This line prints the string "\n newlines and \t tabs." to the console. The "\n" represents a newline character, and "\t" represents a 
# tab character. When printed, these special characters will be interpreted as a newline and a tab respectively.
print("\n newlines and \t tabs.")
# This block of code assigns a multi-line string to the variable poem. The string contains newlines ("\n") and tabs ("\t") that will be 
# interpreted when the string is printed. The leading "\t" before each line adds an indentation effect.
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""
# These three lines print a series of dashes, then the poem variable, and another series of dashes. This creates a visual separation
# before and after printing the poem.
print("-------------")
print(poem)
print("-------------")
# This line performs a series of arithmetic operations and assigns the result (which is 5) to the variable five.
five = 10 - 2 + 3 - 6
# This line uses an f-string to format the string "This should be five: {five}" and print it to the console. 
# The curly braces {} are used to embed the value of the five variable within the string.
print(f"This should be five: {five}")
# This block of code defines a function called secret_formula that takes one parameter called started.
# Inside the function, it performs some calculations based on the started parameter and assigns the results to local 
# variables jelly_beans, jars, and crates. It then returns a tuple containing these three values.
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates
# These two lines assign the value 10000 to the variable start_point. Then, the secret_formula function is called 
# with start_point as an argument, and the returned tuple is unpacked into the variables beans, jars, and crates.
start_point = 10000

beans, jars, crates = secret_formula(start_point)
# This line uses the format() method to insert the value of start_point into the string "With a starting point 
# of: {}". The formatted string is then printed to the console.
# Remember that this is another way to format a string:
print("With a starting point of: {}" .format(start_point))
# This line uses an f-string to format the string "we'd have {beans} beans, {jars} jars, and {crates} crates." 
# The values of beans, jars, and crates are inserted into the respective curly braces, and the resulting string is printed to the console.
# It's just like with an f"" string
print(f"we'd have {beans} beans, {jars} jars, and {crates} crates.")
# This line divides the value of start_point by 10 and assigns the result back to start_point.
start_point = start_point / 10

# These lines print the string "We can also do that this way:", then call the secret_formula function with the updated start_point value. 
# The returned tuple is unpacked into the formula variable. Finally, the values of formula are inserted into the string using the format() 
# method, and the resulting string is printed to the console.
#Overall, this code demonstrates the usage of string formatting, escape characters, multi-line strings, function definition, arithmetic
# operations, and function calling in Python.
print("We can also do that this way:")

formula = secret_formula(start_point)

# This is an easy way to apply a list to a format string

print("We'd have {} beans, {} jars, and {} crates.".format(*formula)) 