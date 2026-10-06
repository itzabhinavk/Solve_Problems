# Write a Python program to draw concentric circles using Turtle.
import turtle as t

for radius in range(20, 101, 20):
    t.penup()
    t.goto(0, -radius)
    t.pendown()
    t.circle(radius)
t.done()