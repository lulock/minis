# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 09:49:20 2020

@author: Lulock
"""


# Mad Libs is a phrasal template word game where one player prompts others for a list of words to substitute for blanks in a story before reading aloud. The game is frequently played as a party game or as a pastime.

# Objective: write a Mad Libs game. 
# When the program runs, it will prompt the user to type a word class like "noun" or "adjective"
# Once all words are collected and the "word list" is complete, the programme will print the text, filling in missing values with the user's suggested inputs.

# Concepts to keep in mind:
# String
# Dictionary
# Print
# Loops
# Handling inputs
# Time
import time

# future considerations:
# multiple Mad Lib texts to choose from (thematic)
# Mad Lib generator. Prompts input in particular format, extracts "blanks" as keys, builds dictionary and corresponding text to print, and stores in a mad lib library.
# More stringent requirements - handle exceptions!
 
# Personalisation to get started. Ask for the user's name
name = input("Please insert your name: \n");
print(f"\nWelcome {name}! Let's get this party started.")

#empty dictionary to store user inputs. Each blank is a key and has a corresponding value in the text.
dict_halloween = {
    'exclamation' : '',
    'noun': '',
    'plural noun': '',
    'verb': '',
    'second verb': '',
    'adverb': '',
    'adjective': ''
    }

def mad_lib_halloween():
    for key in dict_halloween.keys():
        dict_halloween[key] = (input(f"\nPlease insert a {key}\n"))
    
    print('\nAlright, I am scribbling down your inputs. Ready for the big reveal?')
    for i in range(8):
        print(".", end =" ")
        time.sleep(.5)
        
    print(f"\n\n{dict_halloween['exclamation']}! Today is Halloween! I haven't got a {dict_halloween['noun']}, but I have got some {dict_halloween['plural noun']} I usually {dict_halloween['verb']} on Halloween, but today I'm going to {dict_halloween['second verb']} {dict_halloween['adverb']}. Today I feel {dict_halloween['adjective']}!\n")
    
 
mad_lib_halloween()
time.sleep(1)
print("LOL! Makes no sense. So silly. Thanks for playing!")