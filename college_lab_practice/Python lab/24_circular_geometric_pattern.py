# Write a Python program to draw a circular geometric pattern using Turtle.
import turtle as t

t.speed(0)
for i in range(36):
    for i in range(4):
        t.forward(100)
        t.right(90)
    t.right(10)
t.done()