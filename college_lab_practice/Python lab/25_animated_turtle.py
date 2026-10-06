# Write a Python program to draw an animated turtle pattern using Turtle.
import turtle as t

t.speed(3)
for distance in range(10, 151, 10):  
    t.forward(distance)
    t.right(90)
t.done()