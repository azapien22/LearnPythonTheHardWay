# Exercise 19. Functions and Variables

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # Function to display cheese and cracker counts
    
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man, that's enough for a party!")
    print("Get a blanket.\n")

# Calling the function with numbers directly
print("We can give the function numbers directly:")
cheese_and_crackers(20, 30)

# Calling the function with variables from our script
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Calling the function with math expressions
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# Calling the function with variables and math expressions
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

"""In this code snippet, we have a function named cheese_and_crackers that takes two parameters: cheese_count and boxes_of_crackers. 
The purpose of the function is to display the count of cheeses and boxes of crackers. Inside the function, there are several print() 
statements that output messages to the console, including the counts of cheeses and boxes of crackers. These statements use f-strings 
to insert the parameter values into the printed messages. After defining the function, we proceed to call it in various ways:
We call the function directly with numbers: cheese_and_crackers(20, 30). We call the function with variables defined in the script: 
cheese_and_crackers(amount_of_cheese, amount_of_crackers). Here, amount_of_cheese is assigned the value of 10 and amount_of_crackers
is assigned the value of 50.We call the function with math expressions: cheese_and_crackers(10 + 20, 5 + 6). We call the function with
a combination of variables and math expressions: cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000). Each call to the
function displays the cheese and cracker counts based on the provided arguments or expressions. The purpose of this code snippet is to 
demonstrate different ways of calling the cheese_and_crackers function with different inputs."""