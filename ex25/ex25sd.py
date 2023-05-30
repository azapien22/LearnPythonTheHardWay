# Exercise 25. Even more practice
# The provided code snippet defines several functions related to manipulating and printing words in a sentence. Let's go through 
# each function and its purpose:
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words
# The break_words function takes a string (stuff) as input. It splits the string into a list of words using a space (' ') as the delimiter 
# and assigns the result to the words variable. The function then returns the list of words.
    
def sort_words(words):
    """Sorts the words."""
    return sorted(words)
# The sort_words function takes a list of words (words) as input. It uses the sorted() function to sort the words alphabetically and returns 
# the sorted list.

def print_first_word(words):
    """Prints the first word after popping it off"""
    word = words.pop(0)
    print(word)
    # The print_first_word function takes a list of words (words) as input. It removes the first word from the list using the pop() method
    # with an index of 0 and assigns it to the word variable. It then prints the value of word to the console.
    
def print_last_word(words):
    """Print the last word after popping it off."""
    word = words.pop(-1)
    print(word)
# The print_last_word function takes a list of words (words) as input. It removes the last word from the list using the pop() method with
# an index of -1 (which refers to the last element) and assigns it to the word variable. It then prints the value of word to the console.
    
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)
# The sort_sentence function takes a string (sentence) as input. It calls the break_words function to break the sentence into a list of
# words and assigns the result to the words variable. Then, it calls the sort_words function to sort the words alphabetically and
# returns the sorted list.

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
# The print_first_and_last function takes a string (sentence) as input. It calls the break_words function to break the sentence into
# a list of words and assigns the result to the words variable. Then, it calls the print_first_word function to print the first word
# of the words list and the print_last_word function to print the last word of the words list.
    
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
# The print_first_and_last_sorted function takes a string (sentence) as input. It calls the sort_sentence function to break the
# sentence into a list of words and sort them alphabetically, assigning the result to the words variable. Then, it calls the
# print_first_word function to print the first word of the words list and the print_last_word function to print the last word
# of the words list.