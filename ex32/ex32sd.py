# Exercise 32. Loops and Lists Study Drills

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
    
# Now we can print them out too
for i in elements:
    print(f"Element was: {i}") 
    
# 1. Take a look at how you used range. Look up the range function to understand it.
# The range() function generates a sequence of numbers starting from 0 (by default), and increments by 1 (by default), and stops
# before a specified number.

# 2. Could you have avoided that for-loop entirely on line 22 and just assigned range (0,6) directly to elements?
# Yes: elements = list(range(6))

# 3. Per the python documentation what other operands can be used for lists?

# Concatenation (+): This operation allows you to add together two lists, resulting in a new list that contains all elements from both.
# Example:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)  # Output: [1, 2, 3, 4, 5, 6]

# Repetition (*): This operation allows you to repeat the elements in a list a given number of times.
# Example:
list1 = [1, 2, 3]
print(list1 * 3)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Membership (in): This operation allows you to check if an item is in the list.
# Example:
list1 = [1, 2, 3]
print(2 in list1)  # Output: True

# Indexing ([]): This operation allows you to access an individual element in the list.
# Example:
list1 = [1, 2, 3]
print(list1[1])  # Output: 2

# Slicing ([:]): This operation allows you to access a subset of the list's elements.
# Example: 
list1 = [1, 2, 3, 4, 5]
print(list1[1:3])  # Output: [2, 3]

# Length (len()): This operation returns the number of elements in the list.
# Example:
list1 = [1, 2, 3]
print(len(list1))  # Output: 3

# Minimum (min()): This operation returns the smallest element in the list.
# Example:
list1 = [1, 2, 3]
print(min(list1))  # Output: 1

# Maximum (max()): This operation returns the largest element in the list.
# Example:
list1 = [1, 2, 3]
print(max(list1))  # Output: 3

# The following are examples of append() , remove(), and sort() in a code snippet:

# Initialize a list
my_list = [2, 1, 3]

# Use append() to add an element to the end of the list
my_list.append(4)
print(my_list)  # Output: [2, 1, 3, 4]

# Use remove() to remove the first occurrence of an element from the list
my_list.remove(2)
print(my_list)  # Output: [1, 3, 4]

# Use sort() to sort the elements in the list in ascending order
my_list.sort()
print(my_list)  # Output: [1, 3, 4]