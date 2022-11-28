
import turtle
import random

tim = turtle.Turtle()
colors = ['red', 'blue', 'green', 'purple', 'yellow', 'orange', 'black']

#set pen width
tim.width(5)

#Draw random circles

for x in range(5):
    randColor = random.randrange(0, len(colors))
    tim.color(colors[randColor], colors[random.randrange(0, len(colors))])
    rand1 = random.randrange(-300, 300)
    rand2 = random.randrange(-300, 300)
    tim.penup()
    tim.setpos(rand1, rand2)
    tim.pendown()
    tim.begin_fill()
    tim.circle(50)
    tim.end_fill()

