# Exercise 30 Else and If Study Drills

people = 30 
cars = 40 
trucks = 15

if cars > people:
    print("We Should take the cars.")

elif cars < people:
    print("We should not take the cars.")
    
else:
    print("We cant decide.")
    
if trucks > cars:
    print("Thats too many")
    
elif trucks < cars:
    print("Maybe we could take the trucks.")
    
else:
    print("We still can't decide.")
    
if people > trucks:
    print("Alright, Let's just take the trucks.")

else: 
    print("Fine, Let's stay home then.")
    
# 1. Try to guess what elif and else are doing
#
#The elif and else keywords in Python are used in conditional statements to handle different situations. Here's what they do in your 
# provided code:

#if cars > people:: This line checks if the number of cars is greater than the number of people. If this is True, the code inside the if 
# statement is executed, and Python will print "We should take the cars."

#elif cars < people:: This line is only checked if the previous if condition was False. In this case, it checks if the number of cars is 
# less than the number of people. If this condition is True, it prints "We should not take the cars."

#else:: This keyword catches everything which isn't caught by the preceding conditions. In this case, it catches the situation where the 
# number of cars is exactly equal to the number of people. If that's the case, it prints "We can't decide."

#This process is then repeated for the number of trucks and cars, and again for the number of people and trucks.

#The elif keyword is short for "else if." It allows you to check multiple expressions for True and execute a block of code as soon as one 
# of the conditions evaluates to True.

#Similarly, the else keyword catches anything which isn't caught by the preceding conditions.

#In summary, this script is making a series of checks to decide whether the group should take cars, trucks, or stay at home based on the 
# numbers of people, cars, and trucks.

# 2. Change the numbers of cars, people, and trucks, and then trace through each if - statementto see what will be printed:

people = 35 
cars = 26
trucks = 55

if cars > people:
    print("We Should take the cars.")

elif cars < people:
    print("We should not take the cars.")
    
else:
    print("We cant decide.")
    
if trucks > cars:
    print("Thats too many")
    
elif trucks < cars:
    print("Maybe we could take the trucks.")
    
else:
    print("We still can't decide.")
    
if people > trucks:
    print("Alright, Let's just take the trucks.")

else: 
    print("Fine, Let's stay home then.")
    
# The following is the output:
#We should not take the cars.
#Thats too many
#Fine, Let's stay home then.

# 3 & 4: Try some more complex Boolean expressions and write a comment describing what the line does:
# Declare and initialize variables
x = 10
y = 20
z = 30

# Complex boolean expression with 'and', 'or'
# This checks if x is greater than y (which is False) and if y is less than z (which is True) or x is less than z (which is True)
# Due to precedence rules, the 'and' operation is performed first, followed by the 'or' operation
# The 'and' operation returns False (because one condition is False), but the 'or' operation returns True (because one condition is True)
if x > y and y < z or x < z:
    print("Expression 1 is True")
else:
    print("Expression 1 is False")

# Use of parentheses to control the order of operations
# This expression checks if x is greater than y (which is False) and if either y is less than z (which is True) or x is less than z 
# (which is True)
# The parentheses cause the 'or' operation to be performed first, followed by the 'and' operation
# Both 'or' conditions are True, so the 'or' operation returns True
# But the 'and' operation returns False (because one condition is False)
if x > y and (y < z or x < z):
    print("Expression 2 is True")
else:
    print("Expression 2 is False")

# Use of 'not' operator to invert the result
# This expression checks if x is not greater than y (which is True, because x is actually less than y)
if not x > y:
    print("Expression 3 is True")
else:
    print("Expression 3 is False")
