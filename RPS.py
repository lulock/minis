# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 13:10:47 2020

@author: Lulock
"""

# Rock, Paper, Scissors
## Future considerations : extract more functions and modularise

input('ROCK, PAPER, SCISSORS || PRESS ENTER TO BEGIN')

from random import randint
import time

points={'player1': 0, 'player2': 0}
choice={0:'ROCK',1:'PAPER',2:'SCISSORS'}

# function to increment score and print new score
def increment_score(player):
    points[f'{player}']+=1
    
    if(player == 'player1'):
        print("I win this round.")
    else:
        print("You win this round.")
    
    print(f"\nScore is me: {points['player1']} and you: {points['player2']}")

# function to process player's input
def process_input(text):
    if(text.strip().lower()=='rock'):
        return 0
    elif(text.strip().lower()=='paper'):
        return 1
    elif (text.strip().lower()== 'scissors'):
        return 2
    else:
        return process_input(input(f'sorry, {text} is not an option, please choose Rock, Paper, or Scissors:\n'))

# function to compare
def compare(player1, player2):
    print('\n')
    if(player1 == player2):
        player1choice = choice[player1] 
        print(f"I chose {player1choice}.")
        print("It's a tie!")
        
    elif (player1 == 0):
        print("I chose ROCK.")
        if(player2 == 2):
            increment_score('player1')
        elif(player2 == 1):
            increment_score('player2')
    elif (player1 == 1):
        print("I chose PAPER.")
        if(player2 == 0):
            increment_score('player1')
        elif(player2 == 2):
            increment_score('player2')
    elif (player1 == 2):
        print("I chose SCISSORS.")
        if(player2 == 1):
            increment_score('player1')
        elif(player2 == 0):
            increment_score('player2')


def play():
    print(f"\nScore is me: {points['player1']} and you: {points['player2']}")
    
    while((points['player1']<3) and (points['player2']<3)):
        print('\nTake your pick : Rock, Paper, or Scissors? Input in', end= " ")
        for i in range(3):
            print(3-i,'.',end=' ')
            time.sleep(1)
        
        player1 = randint(0,2)
        player2 = process_input(input())
        compare(player1,player2)
        
    print("===========================================")
    print(f"\nEND GAME! Final Score is me: {points['player1']} and you: {points['player2']}")

play()
