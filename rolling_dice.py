# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 18:11:17 2020

@author: Lulock
"""


# This is my first Mini. Today I will simulate rolling dice :)

# Dice Rolling Simulator

# Objective: write a program that simulates rolling dice. 
# When the program runs, it will ask to determine how many sides you would like your dice to have
# It will then prompt you to roll when you're 'ready' and depict that it is loading as the dice 'rolls'
# It should then ask you if you’d like to roll again. 

# Concepts to keep in mind:
# Random
# Integer
# Print
# While Loops
# Handling Exceptions
# Handling inputs
# Time

# Future considerations for this Mini project:
# package random roll into a function that limits the max number of sides
# function to handle multiple dice rolls and print the sum
# capture record of all rolls and return a plot of the distribution when asked

# generate random integer values
#from random import seed
from random import randint
import time
# seed random number generator
#seed(1)

playing = True

def repeat_game(play_again):
    if play_again.strip().lower() == 'n':
        print('\nThanks for playing! See you next time.')
        return False
    elif play_again.strip().lower() == 'y':
        print('\nSweet!')
        return True
    else:
        #handle exceptions
        return repeat_game(input("\n Sorry, I did not recognise your input. Please specify 'y' or 'n' to continue. \n"))

print("Welcome! So you've come here to role dice, huh? Waste no time and jump right in. \n")


while playing:

    sides = 0
    #handle exceptions, only accept type int
    while True:
        try:
            sides=int(input("How many sides would you like your dice to have? \n"))
            if sides == 0:
                print("\nSorry, your dice cannot have 0 sides. Please try again. \n")
                continue
            else:
                break
        except:
            print("\nThat's not a valid option! Please insert a number \n")
            
    if sides == 0:
        print("Sorry, your dice cannot have 0 sides. Please try again. \n")
    
    print("\nYou've selected a dice with ", sides, " sides! \n")
    
    input("Ready? Press ENTER to roll your " + str(sides) + " sided dice. \n")
    
    print("Rolling", end =" ")
    for i in range(8):
        print(".", end =" ")
        # wait 
        time.sleep(.5)
    	
    # generate random integer between 1 and 6
    value = randint(1, sides)
    
    print("Your dice rolled", value, "!\n") 
    
    time.sleep(1)
    
    playing=repeat_game(input("Would you like to roll again? (y/n) \n"))
    