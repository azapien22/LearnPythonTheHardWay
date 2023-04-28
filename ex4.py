# Exercise 4. Variables and Names
# Initialize the number of cars available
cars = 100

# Initialize the number of seats in each car
space_in_a_car = 4.0

# Initialize the number of drivers available
drivers = 30 

# Initialize the number of passengers
passengers = 90

# Calculate the number of cars that will not be driven
cars_not_driven = cars - drivers

# Calculate the number of cars that will be driven
cars_driven = drivers

# Calculate the total number of people that can be transported
carpool_capacity = cars_driven * space_in_a_car

# Calculate the average number of passengers in each car
average_passengers_per_car = passengers / cars_driven

# Print the number of cars available
print("There are", cars, "cars available.")

# Print the number of drivers available
print("There are only", drivers, "drivers available.")

# Print the number of cars that will not be driven
print("There will be", cars_not_driven, "empty cars today.")

# Print the total number of people that can be transported
print("We can transport", carpool_capacity, "people today.")

# Print the number of passengers that need to be transported
print("We have", passengers, "to carpool today.")

# Print the average number of passengers in each car
print("We need to put about", average_passengers_per_car, "in each car.")