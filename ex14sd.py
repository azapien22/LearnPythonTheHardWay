# Ex. 14 Study Drill

# Study drill 2. Change the prompt variable:

 imports the argv module from the sys library.
from sys import argv
# unpacks the argv variable into two variables, script and user_name. The script variable will contain the name of the script, 
# while user_name will contain the value passed in as an argument to the script.
script, user_name = argv
# Sets the variable prompt to a string that will be used as a prompt when asking the user for input.
prompt = f'{script}> '
# prints a formatted string that greets the user and displays the name of the script.
print(f"Hi {user_name}, I'm the {script} script.")
# prints a message asking the user to answer a few questions.
print("I'd like to ask you a few questions.")
# prints a formatted string asking the user if they like the program.
print(f"Do you like me {user_name}?")
# prompts the user to enter a response to the previous question and stores their response in the likes variable.
likes = input(prompt)
# prints a formatted string asking the user where they live.
print(f"Where do you live {user_name}?")
# prompts the user to enter a response to the previous question and stores their response in the lives variable.
lives = input(prompt)
# prints a message asking the user what kind of computer they have.
print("What kind of computer do you have?")
# prompts the user to enter a response to the previous question and stores their response in the computer variable.
computer = input(prompt)
#  prints a formatted string that summarizes the user's responses.
print(f"""Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is. And you have a {computer} computer. Nice.""")

# Study Drill 3.
# Add another argument and use it in your script
from sys import argv
# Added title as another argument.
script, user_name, title = argv

prompt = f'{script}:user:{user_name}:title:{title}> '

print(f"Hi {user_name}, I'm the {script} script.")

print("I'd like to ask you a few questions.")

print(f"Do you like me, {user_name}?")

likes = input(prompt)

print(f"Where do you live {user_name}?")

lives = input(prompt)

print(f"How old are you {user_name}")
age = input(prompt)

print("What kind of computer do you have?")

computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives} and are {age} years old. Not sure where {lives} is. And you have a {computer} computer. Nice.""")