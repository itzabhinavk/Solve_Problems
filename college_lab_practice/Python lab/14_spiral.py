# Write a Python program to draw a spiral using Turtle.
import turtle as t

for distance in range(5, 201, 5):
    t.forward(distance)
    t.right(30)
t.done()