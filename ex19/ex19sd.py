# Ex 19 study drill 

# Write at least one more function of your own design, and run it 10 different ways.

# Here's an example of a custom function named 'calculate_total' that takes two parameters 'price' and 'quantity' and 
#calculates total cost"
def calculate_total(price, quantity):
    total = price * quantity
    return total

# Now, let's run the 'calculate_total' function in 10 different ways:

# 1. Provide numerical values directly:
result1 = calculate_total(10,5)
print(result1) # Output: 50

# 2. Use variables as arguments:
item_price = 8
item_quantity = 3
result2 = calculate_total(item_price, item_quantity)
print(result2)

#3. Use Mathematical expressions as arguments:
result3 = calculate_total(2.5 * 4, 3 + 2)
print(result3) # output 50

# 4. Combine Variables and Mathematical expressions:
item_price = 5
item_quantity = 2
result4 = calculate_total(item_price * 2, item_quantity + 3)
print(result4) # output 50

# 5. Assign the function call to a variable:
result5 = calculate_total(6,4)
print(result5) # output 24

# 6. Pass the function call as an argument to another function:
def display_result(result):
    print(f"The total cost is {result}")
    display_result(calculate_total(7,3)) # Output the total cost: 21

# 7. Use function call as part of a larger expression
total_cost = calculate_total(9,2) + calculate_total(5,4)
print(total_cost) # output: 38

# 8. Call the function inside a loop:
for i in range(1,6):
    print(f"Total cost for item {i}: {calculate_total(5,i)}")
    # Output:
    #Total cost for item 1: 5
    #Total cost for item 2: 10
    #Total cost for item 3: 15
    #Total cost for item 4: 20
    #Total cost for item 5: 25
    
# 9. Pass arguments as user input:
    
price_input = float(input("Enter the price: "))
quantity_input = int(input("Enter the quantity: "))
result9 = calculate_total(price_input, quantity_input)
print(result9)

# 10. Use default arguments:

def calculate_total(price=10, quantity=2):
    total = price * quantity
    return total

result10 = calculate_total()
print(result10) # output: 20