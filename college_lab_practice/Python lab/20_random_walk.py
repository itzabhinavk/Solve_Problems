# Write a Python program to draw a random walk using Turtle.
import random
import turtle as t

t.speed(0)
t.pensize(3)
colors = ["red", "blue", "green", "orange"]
for _ in range(100):
    t.color(random.choice(colors))
    t.forward(30)
    t.right(random.choice([0, 90, 180, 270]))
t.done()
