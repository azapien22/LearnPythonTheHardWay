# Exercise 33 study drill 

# 1. Convert this while loop to a function that you can call, and replace 6 in the test  (i < 6) with a variable. 
# 2. Use this function to rewrite the script to try different numbers. 
# 3. Add another variable to the function arguments that you can pass in that lets you change the + 1 so you can change how much it 
# increments by.
# 4. Rewrite the script again to use this function to see what effect that has.
# 5. Write it to use for-loops and range. Do you need the incrementor in the middle anymore? What happens if you do not get rid of it? 

# The following is the output from study drill # 1-3:

def number_sequence(limit, increment):
    i = 0
    numbers = []

    while i < limit:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += increment
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")
    for num in numbers:
        print(num)

    print(numbers)

# Calling the function with different parameters
number_sequence(6, 1)
number_sequence(10, 2)
number_sequence(8, 3)

# The following is the output:

# At the top i is 0
# Numbers now:  [0]
# At the bottom i is 1
# At the top i is 1
# Numbers now:  [0, 1]
# At the bottom i is 2
# At the top i is 2
# Numbers now:  [0, 1, 2]
# At the bottom i is 3
# At the top i is 3
# Numbers now:  [0, 1, 2, 3]
# At the bottom i is 4
# At the top i is 4
# Numbers now:  [0, 1, 2, 3, 4]
# At the bottom i is 5
# At the top i is 5
# Numbers now:  [0, 1, 2, 3, 4, 5]
# At the bottom i is 6
# The numbers: 
# 0
# 1
# 2
# 3
# 4
# 5
# [0, 1, 2, 3, 4, 5]
# At the top i is 0
# Numbers now:  [0]
# At the bottom i is 2
# At the top i is 2
# Numbers now:  [0, 2]
# At the bottom i is 4
# At the top i is 4
# Numbers now:  [0, 2, 4]
# At the bottom i is 6
# At the top i is 6
# Numbers now:  [0, 2, 4, 6]
# At the bottom i is 8
# At the top i is 8
# Numbers now:  [0, 2, 4, 6, 8]
# At the bottom i is 10
# The numbers: 
# 0
# 2
# 4
# 6
# 8
# [0, 2, 4, 6, 8]
# At the top i is 0
# Numbers now:  [0]
# At the bottom i is 3
# At the top i is 3
# Numbers now:  [0, 3]
# At the bottom i is 6
# At the top i is 6
# Numbers now:  [0, 3, 6]
# At the bottom i is 9
# The numbers: 
# 0
# 3
# 6
# [0, 3, 6]

# In this script, number_sequence is a function that takes two arguments: limit and increment. It initializes i to 0 and numbers to
# an empty list. Then it enters a while loop that continues until i is not less than limit. In each iteration of the loop, it prints
# the current value of i, appends i to numbers, increments i by increment, and then prints the list of numbers and the new value of i.
# When the loop finishes, it prints all the numbers in numbers. Then we call number_sequence with different limit and increment values
# to see how it behaves with different inputs.

# The following is the output from study drill # 4 & 5:

# The function can be rewritten to use a for loop with the range() function, replacing the while loop. The range() function allows us
# to specify the start, stop, and step size (which is analogous to the increment in the original code). The function does not require
# an increment operation within the loop, as range() handles this automatically.

def number_sequence_for_loop(limit, increment):
    numbers = []

    for i in range(0, limit, increment):
        print(f"At the top i is {i}")
        numbers.append(i)
        
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")
    for num in numbers:
        print(num)

    print(numbers)

# Calling the function with different parameters
number_sequence_for_loop(6, 1)
number_sequence_for_loop(10, 2)
number_sequence_for_loop(8, 3)

# The following is the output:

# At the top i is 0
# Numbers now:  [0]
# At the bottom i is 0
# At the top i is 1
# Numbers now:  [0, 1]
# At the bottom i is 1
# At the top i is 2
# Numbers now:  [0, 1, 2]
# At the bottom i is 2
# At the top i is 3
# Numbers now:  [0, 1, 2, 3]
# At the bottom i is 3
# At the top i is 4
# Numbers now:  [0, 1, 2, 3, 4]
# At the bottom i is 4
# At the top i is 5
# Numbers now:  [0, 1, 2, 3, 4, 5]
# At the bottom i is 5
# The numbers: 
# 0
# 1
# 2
# 3
# 4
# 5
# [0, 1, 2, 3, 4, 5]
# At the top i is 0
# Numbers now:  [0]
# At the bottom i is 0
# At the top i is 2
# Numbers now:  [0, 2]
# At the bottom i is 2
# At the top i is 4
# Numbers now:  [0, 2, 4]
# At the bottom i is 4
# At the top i is 6
# Numbers now:  [0, 2, 4, 6]
# At the bottom i is 6
# At the top i is 8
# Numbers now:  [0, 2, 4, 6, 8]
# At the bottom i is 8
# The numbers: 
# 0
# 2
# 4
# 6
# 8
# [0, 2, 4, 6, 8]
# At the top i is 0
# Numbers now:  [0]
# At the bottom i is 0
# At the top i is 3
# Numbers now:  [0, 3]
# At the bottom i is 3
# At the top i is 6
# Numbers now:  [0, 3, 6]
# At the bottom i is 6
# The numbers: 
# 0
# 3
# 6
# [0, 3, 6]

# In In this function, we don't need an explicit increment operation (i += increment) within the loop because range() 
# automatically increments i by the step size after each iteration. If you keep the incrementor (i += increment) inside the
# loop while using range(), the counter i will increase twice as fast as intended per loop iteration. This is because range()
# will already increment i by the specified step size, and then the increment operation will increment i again. This may lead
# to skipping values or incorrect behavior based on the context of your program.