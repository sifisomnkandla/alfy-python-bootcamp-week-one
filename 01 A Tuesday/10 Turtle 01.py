#Turtle Grapics in Pygame

import turtle

tim = turtle.Turtle()
tim.color('red')
tim.pensize(5)
tim.shape('turtle')

#Move Turtle
#tim.backward(90)

tim.forward(100)
tim.left(90)
tim.penup()
tim.forward(100)
tim.left(90)
tim.pendown()
tim.color('green')
tim.forward(100)
tim.left(90)
tim.forward(100)

dave = turtle.Turtle()
dave.color('blue')
dave.pensize(20)

dave.backward(100)
dave.speed(0.1)