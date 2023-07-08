# Exercise 35. Branches and Functions

# This Python script is a basic text-based adventure game. Here's an explanation of the code:

# Imports the exit function from the sys module.
from sys import exit

# Defines the 'gold_room' function.
def gold_room():
    print("This room is full of gold. How much do you take?")
    
    choice = input("> ")  # Takes input from the user.
    
    # If the user's input contains "0" or "1", the input is converted to an integer. 
    # If not, the 'dead' function is called with a specific string as an argument.
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")
        
    # If the user takes less than 50 gold, they win and the program exits.
    # If they take 50 or more, the 'dead' function is called.
    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard.")
        
# Defines the 'bear_room' function.
def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey")
    print("The fat bar is in front of another door")
    print("How are you going to move the bear?")
    bear_moved = False  # Initial flag set to False.
    
    # A loop that continuously takes input from the user until a certain condition is met.
    while True:
        choice = input("> ")
        
        # Depending on the user's input, different outcomes occur.
        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True  # Sets the flag to True.
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()  # Calls the 'gold_room' function.
        else:
            print("I got no idea what that means.")
            
# Defines the 'cthulhu_room' function.
def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")
    
    choice = input("> ")  # Takes input from the user.
    
    # Depending on the user's input, different outcomes occur.
    if "flee" in choice:
        start()  # Calls the 'start' function.
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()  # Calls the 'cthulhu_room' function again.

# Defines the 'dead' function with a parameter called 'why'.
def dead(why):
    print(why, "Good Job!")  # Prints the argument given when the function is called.
    exit(0)  # Exits the program.
        
# Defines the 'start' function.
def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")
    
    choice = input("> ")  # Takes input from the user.
    
    # Depending on the user's input, different outcomes occur.
    if choice == "left":
        bear_room()  # Calls the 'bear_room' function.
    elif choice == "right":
        cthulhu_room()  # Calls the 'cthulhu_room' function.
    else:
        dead("You stumble around the room until you starve.")  # Calls the 'dead' function.

# Calls the 'start' function to begin the game.
start()

# In this game, the player is prompted to make a series of choices, with different outcomes based on their input. 
# The game ends either when the player "dies" (triggering the dead function), or when the player "wins" in the gold_room.