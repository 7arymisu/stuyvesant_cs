import turtle
import random

def sierpinski(turtle, length, depth):
    if depth == 0:
        return
    for i in range(3):
            random_color = (random.random(), random.random(), random.random())
            turtle.color(random_color)
            turtle.forward(length)
            sierpinski(turtle, length / 2, depth - 1)
            turtle.backward(length)
            turtle.left(120)

leo = turtle.Turtle()
leo.speed(0)
leo.left(90)
sierpinski(leo, 100, 5)

window = turtle.Screen()
window.exitonclick()