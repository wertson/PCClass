#import the turtle library to use graphics animations

import turtle

#set up the graphics window
#   screen size: width = 500 and height = 500
#   screen color: black
turtle.setup(500,500)
turtle.bgcolor ('black')


#set up turtle characteristics
#pen color: red
turtle.pencolor('red')

#pen size: 5 pixels
turtle.pensize(5)

#speed: 1
turtle.speed(1)

#shape: turtle
turtle.shape('turtle')

#repeat move forward and right turn code 4 times
for i in range(4):
    turtle.forward(100)
    turtle.right(90)

#raise pen up
turtle.penup()

#hide the turtle
turtle.hideturtle()

# tell the turtle to go to the upper left corner
turtle.goto(-240,200)

#put pen down
turtle.pendown()

#change the pen color
turtle.pencolor('green')

#write yout name and set for to Arial, size to 20, and bold
turtle.write('Wertson Furtado', font=('Arial',20,'bold'))

#raise pen up
turtle.penup()
