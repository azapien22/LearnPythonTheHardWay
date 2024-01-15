# Exercise 35. Branches and Functions Study Drills

# 3. Write comments for the functions you do not understand.

# 4. Add more to the game. What can you do to both simplify and expand the game?

# 5. The gold_room has a weird way of getting you to type a number.
# What are all the bugs in this way of doing it? Can you make it better than what I've written?
# Look at how int() works for clues.

# The code represents a text-based adventure game where the player progresses through different rooms by making choices.

from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")
    
    choice = input("> ")
    if choice.isdigit(): # Check if the input is a valid number (consists of digits only)    # Study Drill #5
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")
    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard.")

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False
    
    while True:
        choice = input("> ")
        
        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            dragon_room()  
        else:
            print("I got no idea what that means.")

def dragon_room():  # New room (Study Drill 4)
    print("Here you see a giant dragon.")
    print("The dragon flies in front of another door.")
    print("Will you fight the dragon or run away?")
    
    choice = input("> ")
    
    if "fight" in choice:
        print("The Dragon exclaims, 'you shall not pass!' The user powers up the berserk sword and slays the dragon.")
        underground_chamber()
    elif "run" in choice:
        start()
    else:
        dragon_room()

def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")
    
    choice = input("> ")
    
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print(why, "Good Job!")
    exit(0)
    
def treasure_room():  # New room (Study drill 4)
    print("You've found the long-lost treasure of Cthulhu!")
    print("A voice echoes throughout the chamber, 'Touch nothing but the lamp!'")
    print('Steal the treasure or take the lamp?')
    
    choice = input("> ")
    if choice == "treasure":
        print("Suddenly, a horde of demons spawn into the room.")
        dead("They rip and tear you to pieces.")

    elif choice == "lamp":
        print("A genie manifests from the lamp to save you from the trap room and respawns you to a safe location.")
        start()
    else:
        treasure_room()
        
def underground_chamber(): # New room (Study Drill 4)
    print("You have made it passed the dragon and into the underground chamber.")
    print("You are faced with two final doors: Treasure room or Gold room.")
    print("Choose.")
    
    choice = input("> ")
    if choice == "treasure room":
        treasure_room()
    elif choice == "gold room":
        gold_room()
    else:
        underground_chamber()
        
def start():
    print("You are in a dark room.")
    print("The only light that shines are multiple doors with emanating light.")
    print("Door 1, door 2, or door 3.")
    print("Which one do you take?")
    
    choice = input("> ")
    if choice == "1" or choice == "door 1":
        bear_room()
    elif choice == "2" or choice == "door 2":
        cthulhu_room()
    else:
        dead("The floor beneath you crumbles and fall into a spike pit.")

start()

# 5. The gold_room has a weird way of getting you to type a number.
# What are all the bugs in this way of doing it? Can you make it better than what I've written?

#The gold_room function in your code aims to manage user input to determine if they win or lose based on their choice of how much gold to take. 
#However, there are several issues with the current implementation:

#1.Limited Number Recognition: The function only recognizes numbers containing "0" or "1". This means inputs like "25" or "3" are not recognized as numbers, 
#which is not intuitive. 
#2.String in Number Check: The method of checking if the input is a number by looking for "0" or "1" is not robust. For example,
#"a10" would pass as a number, which is incorrect. 
#3. No Input Validation: There's no check for negative numbers or non-numeric characters mixed with numeric ones (e.g., "30a"). 
#4. Lack of Flexibility: The function only allows for specific numbers, limiting the user's interaction.
#5. Exit Strategy: The use of exit(0) terminates the entire program, which might not be desirable in a larger application context.
#6. Error Handling: There is no handling for unexpected input types like a blank entry or special characters.
#To improve the function, we can implement more robust input validation and error handling. Here's a revised version:

"""def gold_room():
    print("This room is full of gold. How much do you take?")
    
    while True:
        choice = input("> ")
        try:
            how_much = int(choice)
            if how_much < 0:
                print("Please enter a positive number.")
                continue

            if how_much < 50:
                print("Nice, you're not greedy, you win!")
                break  # Replace exit(0) with break to just exit the loop, not the whole program
            else:
                dead("You greedy bastard.")
                break  # Assuming 'dead' ends the function or does something similar

        except ValueError:
            print("That's not a number. Please enter a number.")

gold_room()
"""




