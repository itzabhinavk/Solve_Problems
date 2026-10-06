# Write a Python program to draw a filled triangle using Turtle.
import turtle as t

t.color("green")
t.begin_fill()
for _ in range(3):
    t.forward(120)
    t.left(120)
t.end_fill()
t.done()