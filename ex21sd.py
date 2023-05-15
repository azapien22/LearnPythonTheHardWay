# Exercise 21. Functions can Return Something

# Defines a function called 'add' that takes two parameters 'a' and 'b'
def add(a,b):
    print(f"ADDING {a} + {b}")  # Prints a string showing the addition operation
    return a + b  # Returns the result of adding 'a' and 'b'

# Defines a function called 'subtract' that takes two parameters 'a' and 'b'
def subtract(a,b):
    print(f"SUBTRACTING {a} - {b}")  # Prints a string showing the subtraction operation
    return a - b  # Returns the result of subtracting 'b' from 'a'

# Defines a function called 'multiply' that takes two parameters 'a' and 'b'
def multiply(a,b):
    print(f"MULTIPLYING {a} * {b}")  # Prints a string showing the multiplication operation
    return a * b  # Returns the result of multiplying 'a' and 'b'

# Defines a function called 'divide' that takes two parameters 'a' and 'b'
def divide(a,b):
    print(f"DIVIDING {a} / {b}")  # Prints a string showing the division operation
    return a / b  # Returns the result of dividing 'a' by 'b'

print("let's do some math with just functions!")  # Prints a string

# Calls the 'add' function with arguments 30 and 5, and assigns the result to 'age'
age = add(30,5)

# Calls the 'subtract' function with arguments 78 and 4, and assigns the result to 'height'
height = subtract(78,4)

# Calls the 'multiply' function with arguments 90 and 2, and assigns the result to 'weight'
weight = multiply(90,2)

# Calls the 'divide' function with arguments 100 and 2, and assigns the result to 'iq'
iq = divide(100,2)

# Prints a formatted string showing the calculated 'age', 'height', 'weight', and 'iq'
print(f"Age: {age}, height: {height}, Weight: {weight}, IQ: {iq}")

print("Here is a puzzle.")  # Prints a string

# Calls the four functions in a nested way and assigns the result to 'what'
what = add(age, subtract(height, multiply(weight, divide(iq, 2)))) #Study drill 2

# Prints a string and the value of 'what', asking if you can do the calculation by hand
print("That becomes: ", what, "Can you do it by hand?")
# The output: That becomes:  -4391.0 Can you do it by hand?

# Study drill 1: 
# Return is commented in the lines of code.

#Study Drill 2: 
# The following is the normal math formula that would recreate this same set of operations:
# 30 + 5 + 78 - 4 -(90 * 2) * (100/2) / 2  

# Define the functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# Calculate the equation
result = subtract(
    add(
        add(30, 5),
        subtract(78, 4)
    ),
    divide(
        multiply(
            multiply(90, 2),
            divide(100, 2)
        ),
        2
    )
)

# Print the result
print("The result is: ", result)
# The result is:  -4391.0  


# Study Drill 3:
# Once you have the formula worked out modify the parts of the function. 
# Change it on purpose to create another value:

# Define the functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# Calculate the equation
result = subtract(
    add(
        add(30**9, 5),
        subtract(78, 4)
    ),
    divide(
        multiply(
            multiply(90, 2**2), # pow(2,2) or 2^2
            divide(100, 2**4)   # pow(2,4) or 2^4
        ),
        2
    )
)

# Print the result
print("The result is: ", result)
# the output: The result is:  19682999998954.0

# Study Drill 4:
# 24 + 34 / 100 - 1023

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def divide(a,b):
    return a / b

result = subtract(add(24,divide(34,100)), 1023)

print(f"The result is {result}. ")
print("The result is: ", result)

