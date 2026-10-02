#Graphics related operation in python for drawing simple shapes
import turtle as t
t.Turtle()

# draw the triangle using turtle
for i in range(3):
    t.forward(200)
    t.left(120)
t.forward(200)

#Draw a Five-Pointed Star ⭐

sides = 5
for i in range(sides):
    t.forward(100)
    t.right(144)
t.done()


