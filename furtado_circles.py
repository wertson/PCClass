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
#                   the turtle should go to (0,-200)
turtle.goto(0,-200)
#                   put the pen down
turtle.pendown()
#draw a circle with the radius of 100 pixels
turtle.circle(100)

#fill color
turtle.fillcolor('red')


turtle.begin_fill()
