import turtle
import random

turtle.setup(500, 500)
turtle.bgcolor('black')
turtle.speed(0)

def draw_stars():
    for i in range(75):
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.fillcolor('white')
        turtle.begin_fill()
        turtle.circle(2)
        turtle.end_fill()
        

def draw_rectangle(x, y, width, height, color):
    turtle.penup()
    turtle.pencolor('gray')
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    
    
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

    turtle.end_fill()

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


draw_stars()
draw_rectangle(-250, -250, 100, 300, "gray")
draw_rectangle(-150, -250, 120, 150, "gray")
draw_rectangle(-50, -250, 100, 350, "gray")
draw_rectangle(50, -250, 150, 250, "gray")
draw_rectangle(150, -250, 200, 310, "gray")
draw_rectangle(250, -250, 100, 100, "gray")

draw_square(-200, -200, 30, 'yellow')
draw_square(100, -150, 20, 'yellow')
draw_square(250, -180, 40, 'yellow')
draw_square(0, -20, 30, 'yellow')
draw_square(150, -20, 30, 'yellow')
draw_square(150, -70, 30, 'yellow')
