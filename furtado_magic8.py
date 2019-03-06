# WERTSON FURTADO
# COMI-1150-399# ASSIGNMENT 
# MIDTERM PROJECT - PART II: MAGIC 8-BALL PROGRAM
# 03/06/19

# PROGRAM TITLE: MAGIC 8-BALL

# PROGRAM DESCRIPTION: A Python program that simulates the magic 8-ball game
#                      by having the user ask a question and then outputting
#                      random advice.


# PSEUDOCODE: 
#              import libraries to use in your program (turtle, time, random)
#
#              setup the graphics window to be 500 x 500 with a gray background
#              at the top of the graphics window, write the message:
#                 Welcome to the Magic 8-Ball game!
#
#              draw a black circle in the center of the graphics window
#              draw a white circle in the center of the black circle
#              draw a purple triangle in the center of the white circle 
#              write "Welcome!" inside the purple triangle
#
#              create a list of affirmative sayings from the magic 8-ball
#              create a list of non-committal sayings from the magic 8-ball
#              create a list of negative sayings from the magic 8-ball
#
#              ask the user to enter a question to ask the magic 8-ball 
#
#              at the top of the graphics window write user's question
#              redraw the purple triangle in the center of the circle
#              write "Shaking!" inside the center of the purple triangle
#              make the computer sleep for a random amount of time (between 1 and 3) using time library
#
#              compute a random number between 0 and 2 and store in variable
#              redraw the purple triangle in the center of the circle
#
#              if the random number equals 0 then:
#                 (1) choose the list of affirmative sayings
#                 (2) compute another random number between 0 and 9
#                 (3) use random number as index for affirmative sayings list
#                 (4) write sayings chosen in step 3 in purple triangle
#
#              if the random number equals 1 then:
#                 (1) choose the list of non-committal sayings
#                 (2) compute another random number between 0 and 4
#                 (3) use random number as index for non-committals sayings list
#                 (4) write sayings chosen in step 3 in purple triangle
#
#              if the random number equals 2 then:
#                 (1) choose the list of negative sayings
#                 (2) compute another random number between 0 and 4
#                 (3) use random number as index for negative sayings list
#                 (4) write sayings chosen in step 3 in purple triangle

import turtle, random, time

#setting the screen size, color and title.
turtle.setup(500, 500)
turtle.speed(0)
turtle.bgcolor('gray')
turtle.title(" Welcome to the Magic 8-Ball game!")

#Message format and location of the message
turtle.penup()
turtle.goto(-240,200)
turtle.pencolor('purple')
turtle.pendown()
turtle.write(" Welcome to the Magic 8-Ball game!", font=('Arial',20,'bold'))
turtle.penup()
turtle.goto(0,-200)
#put the pen down
turtle.pendown()
#set the fill color to yellow
turtle.fillcolor('black')
#start the fill
turtle.begin_fill()
#draw a circle with radius of 100 pixels
turtle.circle(200)
#end the fill
turtle.end_fill()

turtle.penup()

turtle.goto(0,-100)
#put the pen down
turtle.pendown()
#set the fill color to yellow
turtle.fillcolor('white')
#start the fill
turtle.begin_fill()
#draw a circle with radius of 100 pixels
turtle.circle(100)
#end the fill
turtle.end_fill()

turtle.penup()

turtle.goto(-76,-55)
# change the pen color
turtle.pencolor('purple')
# put the pen down
turtle.pendown()
turtle.fillcolor('purple')
turtle.begin_fill()
# draw a triangle

for i in range(3):
    turtle.forward(160)
    turtle.left(120)



turtle.end_fill()
turtle.penup()
#write the welcome inside of the triangle.
turtle.goto(-15, 0)
turtle.pendown()
turtle.pencolor("black")
turtle.write("Welcome!", font=('Arial',8))
turtle.penup()

#popup question to the user.
question = turtle.textinput('Magic 8-Ball Question. ', 'Enter a question for the magic 8-Ball:')


turtle.goto(-200, -230)
turtle.pencolor('black')
turtle.write(question, font=('Arial',16))

#list

affirmativeList= ['It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes - definitely.', 'You may rely on it.', 'As I see it, yes.', 'Most likely.', 'Outlook good.', 'Yes', 'Signs points to yes.']
nonCommittalList= ['Reply hazy. Try again.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.']
negativeSayingList= ["Don't count on it.", 'My reply is no.', 'My sources say no.', 'Outlook not so good', 'Very doubtful.']


turtle.penup()

turtle.goto(-76,-55)
# change the pen color
turtle.pencolor('purple')
# put the pen down
turtle.pendown()
turtle.fillcolor('purple')
turtle.begin_fill()
# draw a triangle

for i in range(3):
    turtle.forward(160)
    turtle.left(120)

turtle.end_fill()

turtle.penup()

#write the shaking inside of the triangle.

turtle.goto(-15, 0)
turtle.pendown()
turtle.pencolor("black")
turtle.write("Shaking!", font=('Arial',8))
turtle.penup()

#time it takes to show message
time.sleep(random.randint(1, 3))


#choose a random number between 0 and 2 which is the 3 different list options.
randomNumber = random.randint(0, 2)

turtle.penup()

turtle.goto(-76,-55)
# change the pen color
turtle.pencolor('purple')
# put the pen down
turtle.pendown()
turtle.fillcolor('purple')
turtle.begin_fill()
# draw a triangle

for i in range(3):
    turtle.forward(160)
    turtle.left(120)

turtle.end_fill()

turtle.goto(-35, 0)
turtle.pendown()
turtle.pencolor('black')

#random choice from the computer.
randomNumber = random.randint(0, 2)
computerGuess = ""

if randomNumber == 0:
    randomNumber = random.randint(0, 9)
    turtle.write(affirmativeList[randomNumber], font=('Arial',7))
    
elif randomNumber == 1:
    randomNumber = random.randint(0, 4)
    turtle.write(nonCommittalList[randomNumber], font=('Arial',7))
    
else:
    randomNumber = random.randint(0, 4)   
    turtle.write(negativeSayingList[randomNumber], font=('Arial',7))




