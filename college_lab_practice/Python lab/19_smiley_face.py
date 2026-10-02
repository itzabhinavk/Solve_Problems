# Write a Python program to draw a smiley face using Turtle.
import turtle as t

t.pensize(3)
t.circle(100)
t.penup()
t.goto(-35, 120)
t.pendown()
t.dot(15, "black")
t.penup()
t.goto(35, 120)
t.pendown()
t.dot(15, "black")
t.penup()
t.goto(-40, 60)
t.setheading(-60)
t.pendown()
for _ in range(5):
    t.forward(20)
    t.left(30)
t.done()