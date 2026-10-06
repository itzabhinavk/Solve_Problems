# Write a Python program to draw a filled square using Turtle.
import turtle as t

t.color("blue")
t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.right(90)
t.end_fill()
t.done()