# Exercise 34 Accessing Elements of Lists Study drills:

# 1. Can you explain why the year 2010 in 'January 1, 2010," really is  2010 and not 2009? (hint: you can't pick years at random)

# The difference between how we count years in a calendar and how we count elements in a Python list. In Python lists, the index 
# is zero-based, which means that the first element is accessed with the index 0, the second element with index 1, and so on.
# On the other hand, our calendar years start at 1 (There's no year 0). So the year 2010 is indeed the 2010th year.
# However, if you were to create a Python list representing each year by its index position, the year 2010 would be at position 
# 2009 because of the zero-based indexing system.
# To Illustrate:

# Let's pretend this list represents years from year 1 to 2010.
years = list(range(1, 2011))

# If we want to find the position of year 2010, we would do:
position = years.index(2010)
print(position)  # This would print 2009

# In this example, the list years represents years 1 to 2010. But due to zero-based indexing, the year 2010 is actually at index 2009
# in the list. In conclusion, it's important to remember the context: Python list indices start at 0, but our calendar years start at 1.

# 2. Write some more lists and work out similar indexes until you can translate them.
# 3. Use Python to check your answers.

# Suppose you have a list of names:
names = ["Alice", "Bob", "Charlie", "Dave"]
#If you were to translate English-based positioning to Python list indices:

#First person: names[0] # Alice
#Second person: names[1] # Bob
#Third person: names[2] # Charlie
#Fourth person: names[3] # Dave

# Suppose you have a list of fruits:
fruits = ["apple", "banana", "cherry", "dragonfruit"]
#If you were to translate English-based positioning to Python list indices:

#First fruit: fruits[0] # apple
#Second fruit: fruits[1] # banana
#Third fruit: fruits[2] # cherry
#Fourth fruit: fruits[3] # dragonfruit

# Let's check these in Python:

names = ["Alice", "Bob", "Charlie", "Dave"]
print(names[0])  # Output: Alice
print(names[1])  # Output: Bob
print(names[2])  # Output: Charlie
print(names[3])  # Output: Dave

fruits = ["apple", "banana", "cherry", "dragonfruit"]
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
print(fruits[2])  # Output: cherry
print(fruits[3])  # Output: dragonfruit