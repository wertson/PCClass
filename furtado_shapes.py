# WERTSON FURTADO
# COMI-1150-399
# ASSIGNMENT #4 - INTRODUCTION TO TURTLE GRAPHICS
# 02/25/2019

# PROGRAM TITLE: DRAWING OTHER SHAPES
# PROGRAM DESCRIPTION: Use turtle graphics and animations to draw a triangle,
#                      pentagon, hexagon, heptagon, and octagon.
#PSEUDOCODE:

# import the turtle library to use graphics and animations
import turtle

# SETUP THE SCREEN
# set up screen with width = 500 and height = 500
turtle.setup(500,500)


# set up screen to have a background color
turtle.bgcolor('green')

# change the pen size to 5
turtle.pensize(5)

# change the speed to be 1
turtle.speed(1)

# change the turtle to have a turtle shape
turtle.shape('turtle')

# DRAW YOUR NAME             
             
# raise the pen up
turtle.penup()

# have the turtle goto (-240, 200)
turtle.goto(-240,200)

# put the pen down
turtle.pendown()

# change the pen color
turtle.pencolor('yellow')

# use the turtle to write your name
#     include the font, size, and bold
turtle.write('Wertson Furtado', font=('Arial',20,'bold'))

# DRAW SHAPES
# raise the pen up
turtle.penup()                                      

# have the turtle goto(-100,-100)
turtle.goto(-100,-100)
                                      

# change the pen color
turtle.pencolor('red')
# put the pen down
turtle.pendown()
# draw a triangle
#      use a loop to draw the steps
#      there are 3 points in a triangle so the steps should repeat 3 times
#            move the turtle forward 100 pixels
#            turn the turtle left 120 degrees
for i in range(3):
    turtle.forward(100)
    turtle.left(120)

# erase all drawings on the screen
turtle.clear()

# draw a pentagon
#      use a loop to draw the steps
#      there are 5 points in a pentagon so the steps should repeat 5 times
#            move the turtle forward 100 pixels
#            turn the turtle left 72 degrees
for i in range(5):
    turtle.forward(100)
    turtle.left(72)


# erase all drawings on the screen
turtle.clear()

# draw a hexagon
#      use a loop to draw the steps
#      there are 6 points in a pentagon so the steps should repeat 6 times
#            move the turtle forward 100 pixels
#            turn the turtle left 60 degrees
for i in range(6):
    turtle.forward(100)
    turtle.left(60)

# erase all drawings on the screen
turtle.clear()

# draw a heptagon
#      use a loop to draw the steps
#      there are 7 points in a pentagon so the steps should repeat 7 times
#            move the turtle forward 100 pixels
#            turn the turtle left 51 degrees
for i in range(7):
    turtle.forward(100)
    turtle.left(51)

# erase all drawings on the screen
turtle.clear()

# draw a octagon
#      use a loop to draw the steps
#      there are 8 points in a pentagon so the steps should repeat 8 times
#            move the turtle forward 100 pixels
#            turn the turtle left 45 degrees
for i in range(8):
    turtle.forward(100)
    turtle.left(45)
