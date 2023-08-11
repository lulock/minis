import turtle
import random

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.left(90)

window = turtle.Screen()
distance = 10
angle = 25
stack = []

window.colormode(255)
window.bgcolor(252,252,249)
t.penup()
t.setpos(0,-window.canvheight)
t.pendown()

def change_color():
    R = random.randint(0,255)
    B = random.randint(0,255)
    G = random.randint(0,255)

    t.color(R, G, B)

rules = {
    "X": "F+[[X]-X]-F[-FX]+X",
    "F": "FF"
}

def t_forward():
    # print("forward")
    t.forward(distance)
    return
def t_pop():
    # print("pop")
    ang , pos = stack.pop()
    t.setheading(ang)
    t.penup()
    t.goto(pos[0], pos[1])
    t.pendown()
    return
def t_push():
    # print("push")
    stack.append([t.heading(), [t.xcor(), t.ycor()]])
    return
def t_right():
    # print("right")
    t.right(angle)
    return
def t_left():
    # print("left")
    t.left(angle)
    return

def noop():
    pass

drawRules = {
    "F": t_forward,
    "]": t_pop,
    "[": t_push,
    "+": t_right,
    "-": t_left,
    "X": noop
}

start = 'X'
print(rules[start])

def generate(word):
    next = ""

    # loop over all characters in current word
    for character in word:
        # check if character is in our rule set
        if character in rules:
            # print(f"{character} -> {rules[character]}")
            next += rules[character]
        else:
            next += character

    return next

num_iterations = 5
l_word = start
for i in range(num_iterations):
    l_word = generate(l_word)

for l in l_word:
    drawRules[l]()
    change_color()

window.exitonclick()
