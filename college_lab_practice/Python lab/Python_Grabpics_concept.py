#Graphics related operation in python for drawing simple shapes
import turtle as t
t.Turtle()

# draw the triangle using turtle
for i in range(3):
    t.forward(200)
    t.left(120)
t.forward(200)
# draw the square using turtle
for i in range (4):
    t.forward(150)
    t.left(90)

t.forward(150)

# draw the pentagon using turtle
sides= 5
for i in range (sides):
    t.forward(100)
    t.left(360/sides)

t.forward(100)


#Draw the ractungle using turtle
for i in range (2):
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.left(90)

# draw the haxagon using turtle
sides = 6
for i in range(sides):
    t.forward(100)
    t.left(360/sides)
    
t.done()