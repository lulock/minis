# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 09:14:44 2020

@author: Lulock
"""

import turtle as timmy
import random


# Rough working out. If I were to hard code case n = 1 ... 
# timmy.forward(10)
# timmy.left(60)
# timmy.forward(10)
# timmy.right(120)
# timmy.forward(10)
# timmy.left(60)
# timmy.forward(10)


# recognise recursive property and implement as function below ...

COLOUR_PICKER = 20

def pen_color(turt,picker, a=5,b=1.5,c=0.5):
    turt.pencolor(min((a*picker)/255,1), min(((b*picker)/255),1), min(((c*picker)/255),1))

def koch_curve(turt, length, order, factor):
    global COLOUR_PICKER
    COLOUR_PICKER += 1
    if order == 0:
        turt.forward(length)
    else:
        
        pen_color(timmy,COLOUR_PICKER)
        koch_curve(turt,length*factor, order - 1,factor)
        turt.left(60)
        koch_curve(turt,length*factor, order - 1,factor)
        turt.right(120)
        koch_curve(turt,length*factor, order - 1,factor)
        turt.left(60)
        koch_curve(turt,length*factor, order - 1,factor)
        

# Multiple lines koch curves means multiple times moving timmy the turtle!
# Extract this behaviour and place into a function for repeated use:

def move_turtle(turt, x, y): 
    timmy.penup()
    timmy.goto(x,y)
    timmy.pendown()

def pen_color(turt,current, a=5,b=1.5,c=0.5):
    turt.pencolor(min(a*current/255,1), min(((b*current)/255),1), min(((c*current)/255),1))



# package all our little Timmy functions into a main function
def main():
    timmy.hideturtle()
    timmy.bgcolor('black')
    timmy.pencolor(1, 1, 1)

    WIDTH = 650
    HEIGHT = 650

    screen = timmy.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title("Welcome to Timmy's fractal park!!")

    n = 5
    x = -150
    y = 275
    pen_color(timmy,COLOUR_PICKER)
    
    for i in range(n):
        timmy.speed(10 + i*i)
        move_turtle(timmy, x, y)
        koch_curve(timmy,300,i,(1/3))
        y -= (HEIGHT/n)
        
    screen.exitonclick()

    timmy.done()
    try:
        timmy.bye()   
    except timmy.Terminator:
        pass


main()