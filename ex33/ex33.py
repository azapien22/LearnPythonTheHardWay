# Exercise 33 while loops

i = 0

numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)
    
    i += 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")
    
    
print("The numbers: ")

for num in numbers:
    print(num)
    
    
print(numbers)
    
# the following is the output:
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