import turtle
import random

tim = turtle.Turtle()
colors = ['red', 'blue', 'green', 'purple', 'yellow', 'orange', 'black']

#set colors for turtle
tim.color('red', 'blue')

#set pen width
tim.width(5)

#Fill in shape color
tim.begin_fill()
tim.circle(50)
tim.end_fill()

tim.penup()
tim.forward(200)
tim.pendown()

#Draw a square Take 1

tim.begin_fill()
tim.color('yellow', 'black')
tim.forward(100)
tim.right(90)
tim.forward(100)
tim.right(90)
tim.forward(100)
tim.right(90)
tim.forward(100)
tim.right(90)
tim.end_fill()

#Draw a square Take 2

tim.penup()
tim.backward(400)
tim.pendown()

tim.begin_fill()
for x in range(4):
    tim.forward(100)
    tim.right(90)
tim.end_fill()


tim.setpos(0,0)