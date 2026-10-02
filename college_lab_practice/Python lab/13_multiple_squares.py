# Write a Python program to draw multiple squares using Turtle.
import turtle as t

for size in range(40, 161, 30):
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.penup()
    t.goto(t.xcor() + 15, t.ycor() - 15)
    t.pendown()
t.done()