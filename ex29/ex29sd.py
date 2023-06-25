# Exercise 29 Study drills

people = 20
cats = 30
dogs = 15

if people < cats:
    print("Too many cats! The world is doomed!")
    
if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")
    
if people > dogs:
    print("The world is dry!")
    
dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")
    
if people <= dogs:
    print("People are less than or equal to dogs.")
        
if people == dogs:
    print("People are dogs.")  
    
 
"""The if statements in the code are conditional statements that evaluate a Boolean expression. If the expression is true, the code block
indented under the if statement is executed. Let's go through the questions one by one:"""

#1.What do you think the if does to the code under it?
#The if statement checks the condition specified in the Boolean expression and executes the code block underneath it only if the condition 
# is true. If the condition is false, the code block is skipped.

#2.Why does the code under the if need to be indented four spaces?
#In Python, indentation is used to define the scope or block of code. Indenting the code under the if statement by four spaces (or any 
#consistent indentation) indicates that it belongs to the code block controlled by the if statement. It helps Python distinguish which code
# should be executed conditionally.

#3.What happens if it isn't indented?
#If the code under the if statement is not indented properly, it will result in a IndentationError because Python expects the code block to 
# be indented. Indentation is crucial in Python as it is used to determine the structure and hierarchy of the code.

#4.Can you put other Boolean expressions in the if statement? Try it.
#Yes, you can use other Boolean expressions in the if statement. The if statement evaluates any valid Boolean expression, which can include
# comparison operators (<, >, <=, >=, ==, !=), logical operators (and, or, not), and other conditions.

#For example, you can modify the code as follows:
#if people != cats:
#    print("The number of people is not equal to the number of cats.")

#5. What happens if you change the initial values for people, cats, and dogs?
#Changing the initial values for people, cats, and dogs would affect the conditions in the if statements and consequently the output when 
#running the code. The output would change depending on how the new values compare to each other in the conditions. The code is designed 
#to print different statements based on the comparisons between people, cats, and dogs.