# Exercise 36 Game
#I'll outline a simple text-based Python game featuring rooms, monsters, and traps in a Cthulhu-themed adventure. 
#The game will have a basic structure with a few rooms, each containing different challenges like monsters or traps. 
#The player navigates through these rooms by making choices.

# Game Concept:
# The Player is an explorer in a mysterious, ancient temple with Cthulu mythos elements.
# The goal is to find the hidden artifact and escape the temple.
# Each room presents a challenge: a puzzle, a monster, or a trap.
# The player has health points (HP) which are depleted by traps or monster attacks.
# Some rooms may contain health potions to restore HP.
# The game ends when the player either escapes with the artifact or loses all HP.

# Implementation Plan:
# 1. Game Setup: Define basic game elements like rooms, monsters, traps, player stats.
# 2. Room Navigation: Implement the logic for moving between rooms.
# 3. Challenges: Each room will present a unique challenge.
# 4. Player Interaction: The player makes choices to interact with each room.
# 5. Game Ending: Define win and lose conditions.

import random
# Import the 'random' module, which provides functions for generating random numbers.

class Game:
    # Define a class named 'Game'.

    def __init__(self):
        # Define the constructor (__init__) method for initializing new Game objects.

        self.rooms = ['Entrance Hall', 'Puzzle Room', 'Monster Room', 'Trap Room', 'Treasure Room']
        # Create an instance variable 'rooms' as a list of strings representing different rooms in the game.

        self.hp = 100
        # Initialize an instance variable 'hp' (health points) and set it to 100.

        self.has_artifact = False
        # Initialize an instance variable 'has_artifact' as a boolean, set to False indicating the player doesn't have the artifact initially.

    def start_game(self):
        # Define a method 'start_game' to start the game.

        print("Welcome to the Temple of Cthulhu!")
        # Print a welcome message to the player.

        for room in self.rooms:
            # Start a loop over each room in the 'rooms' list.

            if not self.enter_room(room):
                # Call the 'enter_room' method for the current room. If it returns False (player dies), execute the code block.

                print("You have died. Game over.")
                # Print a message indicating the player died.

                return
                # Exit the 'start_game' method.

            if room == 'Treasure Room':
                # Check if the current room is the 'Treasure Room'.

                self.has_artifact = True
                # Set the 'has_artifact' variable to True, indicating the player has found the artifact.

        if self.has_artifact:
            # Check if the player has the artifact.

            print("Congratulations! You have retrieved the artifact and escaped the temple!")
            # Print a congratulatory message.

        else:
            # If the player does not have the artifact.

            print("You escaped the temple, but without the artifact. Game over.")
            # Print a message indicating the player escaped without the artifact.

    def enter_room(self, room):
        # Define a method 'enter_room' that takes a 'room' as an argument.

        print(f"\nEntering {room}...")
        # Print a message indicating the player is entering the specified room.

        if room == 'Monster Room':
            # Check if the room is 'Monster Room'.

            return self.monster_encounter()
            # Call the 'monster_encounter' method and return its result.

        elif room == 'Trap Room':
            # Check if the room is 'Trap Room'.

            return self.trap_encounter()
            # Call the 'trap_encounter' method and return its result.

        elif room == 'Puzzle Room':
            # Check if the room is 'Puzzle Room'.

            return self.puzzle_encounter()
            # Call the 'puzzle_encounter' method and return its result.

        elif room == 'Treasure Room':
            # Check if the room is 'Treasure Room'.

            print("You found the hidden artifact!")
            # Print a message indicating the player found the artifact.

        return True
        # Return True by default, indicating the player survives the room.

    def monster_encounter(self):
        # Define a method 'monster_encounter' for the encounter with a monster.

        print("A wild monster appears!")
        # Print a message indicating a monster encounter.

        fight_or_flee = input("Do you fight (f) or flee (r)? ")
        # Ask the player to choose to fight or flee and store their choice.

        if fight_or_flee == 'f':
            # Check if the player chose to fight.

            return self.fight_monster()
            # Call the 'fight_monster' method and return its result.

        return self.flee_monster()
        # If the player chose to flee, call the 'flee_monster' method and return its result.

    def fight_monster(self):
        # Define a method 'fight_monster' for fighting the monster.

        self.hp -= random.randint(10, 30)
        # Reduce the player's hp by a random amount between 10 and 30.

        print(f"You defeated the monster but lost some HP. Current HP: {self.hp}")
        # Print a message indicating the outcome of the fight and the current hp.

        return self.hp > 0
        # Return True if hp is greater than 0, False otherwise (indicating the player's death).

    def flee_monster(self):
        # Define a method 'flee_monster' for fleeing from the monster.

        self.hp -= random.randint(5, 15)
        # Reduce the player's hp by a random amount between 5 and 15 for fleeing.

        print(f"You managed to flee. Current HP: {self.hp}")
        # Print a message indicating the player fled and show the current hp.

        return self.hp > 0
        # Return True if hp is greater than 0, False otherwise.

    def trap_encounter(self):
        # Define a method 'trap_encounter' for encountering a trap.

        self.hp -= random.randint(20, 40)
        # Reduce the player's hp by a random amount between 20 and 40 due to the trap.

        print(f"You encountered a trap! Current HP: {self.hp}")
        # Print a message indicating the trap encounter and the current hp.

        return self.hp > 0
        # Return True if hp is greater than 0, False otherwise.

    def puzzle_encounter(self):
        # Define a method 'puzzle_encounter' for encountering a puzzle.

        answer = input("Solve the puzzle: What has roots as nobody sees, Is taller than trees, Up, up it goes, And yet never grows? ")
        # Ask the player to solve a riddle and store their answer.

        if answer.lower() == "mountain":
            # Check if the player's answer (in lowercase) is 'mountain'.

            print("You solved the puzzle!")
            # Print a message indicating the puzzle was solved.

            return True
            # Return True, indicating the player survived the puzzle.

        print("Wrong answer. The trapdoor opens beneath you!")
        # Print a message indicating a wrong answer and a negative outcome.

        return False
        # Return False, indicating the player did not survive the puzzle.

# Start the game
game = Game()
# Instantiate a Game object and store it in the variable 'game'.

game.start_game()
# Call the 'start_game' method of the game object to begin the game.