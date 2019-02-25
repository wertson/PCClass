# WERTSON FURTADO
# COMI-1150-399# ASSIGNMENT #4
# 02/25/2019
# PROGRAM TITLE: DRAWING A SMILEY FACE
# PROGRAM DESCRIPTION: Use turtle graphics and animations to draw a smiley
#                      face.
# PSEUDOCODE:
#              import the turtle library
import turtle
#              setup the screen to be 500 pixels wide and 500 pixels high
turtle.setup(500,500)
#              set the background color of the screen
turtle.bgcolor('black')
#              set the pen to be size 5
turtle.pensize(5)
#              set the animation speed to be 2
turtle.speed(2)
#              set the shape of the pen to be a turtle
turtle.shape('turtle')
#              set the pen color to yellow
turtle.pencolor('yellow')
#
#              draw the head:
#                   raise the pen up
turtle.penup()
#                   the turtle should go to (0,-100)
turtle.goto(0,-100)
#                   put the pen down
turtle.pendown()
#                   set the fill color to yellow
turtle.fillcolor('yellow')

#                   start the fill
turtle.begin_fill()
#                   draw a circle with radius of 100 pixels
turtle.circle(100)
#                   end the fill
turtle.end_fill()
#
#              draw the smile:
#                   raise the pen up
#                   the turtle should go to (-67,-40)
#                   set the heading to -60
#                   set the pen color to black
#                   put the pen down
#                   draw a circle with radius of (80,120) pixels to
#                        create an arch
#
#              draw the eyes:
#                   set the fill color to black
#                   the turtle should go to (-35, 10)
#                   put the pen down
#                   start the fill
#                   draw a circle with radius of 10 pixels
#                   end the fill
#
#                   set the fill color to black
#                   the turtle should go to (45, 10)
#                   put the pen down
#                   start the fill
#                   draw a circle with radius of 10 pixels
#                   end the fill
#                   hide the turtle
