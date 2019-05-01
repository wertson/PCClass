# import turtle graphics, random and math
import turtle, random, math



# func name: make_snake
# arguments: none
# return: 1 snake (turtle object)
# description: creates the snake in the game
def make_snake():
    # create a variable called snake and set it equal to turtle.Turtle()
    snake = turtle.Turtle()
    # set the shape of the snake to be a square
    snake.shape('square')
    # set the color of the snake to be green
    snake.fillcolor('green')
    # set turtle size to be smallest (1) stretch_line for the snake right now
    snake.turtlesize(stretch_len=1)

    # have the snake raise the penup
    snake.penup()

    # create a variable called x and set it equal to a random integer
    #        between -230 and 230
    x = 0
    # create a variable called y and set it equal to a random integer
    #        between 150 and 250
    y = 200
    # tell the snake to goto x and y
    snake.goto(x, y)

    # set the y trajectory of snake to be equal to 0
    snake.dy = 0
    # set the x trajectory of snake to be equal to 2
    snake.dx = 2

    # return snake
    return snake



# func name: make_apples
# arguments: none
# return: 1 apples (a list of turtle object)
# description: creates the snake in the game
def make_apples():
    # create an empty list called apples
    apples = []

    # for apple in range of 5
    for apples in range(5):
        # create a variable called apple and set it equal to turtle.Turtle()
        appple = turtle.Turtle()
        # set the shape of the apple to be a circle
        apple.shape('circle')
        # set the color of the apple to be red
        apple.fillcolor('red')

        # have the apple raise the penup
        apple.penup()

        # create a variable called x and set it equal to a random integer
        #        between -230 and 230
        x = 0

        # create a variable called y and set it equal to a random integer
        #        between 150 and 250
        y = 200
        # tell the apple to goto x and y
        apple.goto(x, y)

        # append the apple to the end of the list called appples
        apple.append('apples')

    # return the list called apples
    return apples       



# func name: isCollision
# arguments: 2 different turtle objects (one is the snake, one is an apple)
# return: True or False
# description: checks if the snake has collided (touched) an apple
def isCollision(t1, t2):
    # compute distance between snake and apple
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))

    # if the distance between the snake and apple is less than 15
    #    then the snake has collided with an apple
    if distance < 15:
        # return True
        return True

    # else
    #    the snake has not collided with an apple
    else:
        # return False
        return False


    
# func name: move
# arguments: 1 number representing the size of the snake
# return: none
# description: moves the snake and checks for collisions with apples
def move():
    # create a variable called points and set it equal to 0
    points = 0
    # create a variable called num_apples that is equal to the len of apples list
    num_apples = apples

    # loop while the variable num_apples is not equal to 0
    while num_apples != 0:
        # set turtle size to be equal to size stretch_line for the snake
        
        # make the snake move forward 5
        snake.forward(5)

        # check if the snake hit the right wall
        # if the snake's x coordinate is greater than 230
        if x > 230:
            # make the snake's heading be 180
            snake.setheading(180)
            # subtract 1 from points
            points = points - 1

        # check if the snake hit the left wall
        # if the snake's x coordinate is less than 230
        elif x < 230:
            # make the snake's heading be 0
            snake.setheading(0)
            # subtract 1 from points
            points = points - 1

        # check if the snake hit the top wall
        # if the snake's y coordinate is greater than 235
        elif y > 235:
            
      
            # make the snake's heading be 0
            snake.setheading(0)
            # subtract 1 from points
            points = points - 1
            
          

        # check if the snake hit the bottom wall
        # if the snake's y coordinate is less than -230
        else y < -230:
       
            # make the snake's heading be 90
            snake.setheading(90)
           
            # subtract 1 from points
            points = points - 1
      

        # loop for apple in apples
        
            # if you call the isCollision function and pass it snake and apple
            #    and it is true (so there is a collision)
           
                # add 1 to size
                
                # reset the apple
                apple.reset()
                # subtract 1 from num_apples
                
                # add 1 to points
                

        # output the points in the game



# func name: up
# arguments: none
# return: none
# description: makes the snake move up with the up arrow key
def up():
    # make the snake's heading be 90
    snake.setheading(90)



# func name: left
# arguments: none
# return: none
# description: makes the snake move left with the left arrow key
def left():
    # make the snake's heading be 180
    snake.setheading(180)



# func name: down
# arguments: none
# return: none
# description: makes the snake move down with the down arrow key
def down():
    # make the snake's heading be 270
    snake.setheading(270)



# func name: right
# arguments: none
# return: none
# description: makes the snake move right with the right arrow key
def right():
    # make the snake's heading be 0
    snake.setheading(0)
    
    

# set the screen to be 500 wide and 500 high  
snake.setup(500, 500)
# create screen variable called wn
wn = turtle.Screen()
# use wn instead of turtle to change the background color to black
wn = 'black'

# call the function to make the snake and store what it returns in
#      a variable called snake
make_snake()

# call the function to make the apples and store what it returns in
#      a variable called apples


# use wn variable to call functions responsible for moving the
#     snake with the arrow keys
wn.onkey(up, 'Up')
wn.onkey(left, 'Left')
wn.onkey(right, 'Right')
wn.onkey(down, 'Down')
wn.listen()

# create a variable called size and set it equal to 1
size = 1

# call the function responsible for moving the snake and pass it size
move()

# use wn variable to run mainloop (repeat drawing the moving snake on screen)
wn.mainloop()
