# import turtle graphics
import turtle

# set window size to 500, pen size
turtle.setup(500,500)
turtle.pensize(3)

# set up squares
def draw_square(x, y, width, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()

    for i in range(4):
        turtle.forward(width)
        turtle.left(90)

    turtle.end_fill()

# draw squares in the different locations
draw_square(-200, 100, 50, "black")
draw_square(-150, 100, 50, "white")
draw_square(-100, 100, 50, "black")
draw_square(-50, 100, 50, "white")
draw_square(0, 100, 50, "black")
draw_square(-200, 50, 50, "white")
draw_square(-150, 50, 50, "black")
draw_square(-100, 50, 50, "white")
draw_square(-50, 50, 50, "black")
draw_square(0, 50, 50, "white")
draw_square(-200, 0, 50, "black")
draw_square(-150, 0, 50, "white")
draw_square(-100, 0, 50, "black")
draw_square(-50, 0, 50, "white")
draw_square(0, 0, 50, "black")
draw_square(-200, -50, 50, "white")
draw_square(-150, -50, 50, "black")
draw_square(-100, -50, 50, "white")
draw_square(-50, -50, 50, "black")
draw_square(0, -50, 50, "white")
draw_square(-200, -100, 50, "black")
draw_square(-150, -100, 50, "white")
draw_square(-100, -100, 50, "black")
draw_square(-50, -100, 50, "white")
draw_square(0, -100, 50, "black")

