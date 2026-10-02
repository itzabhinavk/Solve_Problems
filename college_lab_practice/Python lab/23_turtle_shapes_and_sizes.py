# Write a Python program to draw different shapes with varying sizes using Turtle.
import turtle as t

shapes = ["turtle", "arrow", "circle", "square"]
for index, shape in enumerate(shapes):
    pen = t.Turtle()
    pen.shape(shape)
    pen.shapesize(index + 1)
    pen.penup()
    pen.goto(-150 + index * 100, 0)
t.done()
