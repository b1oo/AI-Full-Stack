import turtle

def draw_square(turtle):
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)

# create a turtle
t = turtle.Turtle()

# draw the square
draw_square(t)

# hide the turtle and exit turtle graphics
turtle.done()