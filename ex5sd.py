# Exercise 5. More Variables and Printing 
# Removed "my" from all variables
name = 'Zed A. Shaw'
age = 35 # Not a Lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}")
print(f"He's {height} inches tall")
print(f"He's {weight} pounds heavy")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right

total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

# Convert inches and pounds to centimeters and kilograms
# Define the conversion factors

INCHES_TO_CM = 2.54
POUNDS_TO_KG = 0.453592

# Get the input values from the user
inches = float(input("Enter the length in inches: "))
pounds = float(input("Enter the weight in pounds: "))

# Convert the inches to centimeters
centimeters = inches * INCHES_TO_CM

# Convert the pounds to kilograms
kilograms = pounds * POUNDS_TO_KG

# Print the converted values
print("The length in centimeters is:", centimeters, "cm")
print("The weight in kilograms is:", kilograms, "kg")