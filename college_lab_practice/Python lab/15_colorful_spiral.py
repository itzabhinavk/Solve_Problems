# Write a Python program to draw a colorful spiral using Turtle.
import turtle as t

colors = ["red", "orange", "blue", "green", "purple"]
t.bgcolor("black")
t.speed(0)
for step in range(100):
    t.color(colors[step % len(colors)])
    t.forward(step * 2)
    t.right(91)
t.done()