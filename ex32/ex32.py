# Exercise 32. Loops and Lists

the_count = [1,2,3,4,5]
fruits = ['apple', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# This first kind of for-loop goes through a list
for number in the_count:
    print(f'This is count {number}.')
    
# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")
    
# also we can go through mixed lists too
# Notice we have to use {} since we don't know whats in it

for i in change:
    print(f"I got {i}")
    
#We can also build lists, first start with an empty one

elements = []

# Then use the range function to do 0 t 5 counts

for i in range(0,6):
    print(f"Adding {i} to the lists.")
    #Append is a function that lists understand
    elements.append(i)
    print(elements)
    
# Now we can print them out too
for i in elements:
    print(f"Element was: {i}") 
    
# The following is the output:
# This is count 1.
# This is count 2.
# This is count 3.
# This is count 4.
# This is count 5.
# A fruit of type: apple
# A fruit of type: oranges
# A fruit of type: pears
# A fruit of type: apricots
# I got 1
# I got pennies
# I got 2
# I got dimes
# I got 3
# I got quarters
# Adding 0 to the lists.
# [0]
# Adding 1 to the lists.
# [0, 1]
# Adding 2 to the lists.
# [0, 1, 2]
# Adding 3 to the lists.
# [0, 1, 2, 3]
# Adding 4 to the lists.
# [0, 1, 2, 3, 4]
# Adding 5 to the lists.
# [0, 1, 2, 3, 4, 5]
# Element was: 0
# Element was: 1
# Element was: 2
# Element was: 3
# Element was: 4
# Element was: 5