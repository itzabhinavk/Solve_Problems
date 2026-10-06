# Write a Python program to draw a sun using Turtle.
import turtle as t

t.color("orange")
for _ in range(12):
    t.circle(50)
    t.left(30)
for _ in range(12):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.forward(100)
    t.backward(100)
    t.left(30)
t.done()