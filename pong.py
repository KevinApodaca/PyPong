"""
    * Pong Game 
    @author Kevin Apodaca
    * Purpose: A personal project to experiment with the turtle module and create a simple game.
    * I followed the tutorial created by Christian Thompson which can be found on his website ->  http://christianthompson.com/node/51
"""
import turtle, os

wn = turtle.Screen() # creates the window
wn.title("Old School Pong by Kevin Apodaca")
wn.bgcolor("black")
wn.setup(width = 800, height = 600) # size of the window, can be changed
wn.tracer(0)

# ----------------------------------------------- BEGIN OBJECTS ----------------------
# Will initialize all the objects we need to play the game

score_a, score_b = 0, 0 # initialize scores for both players to zero

# Creates left-hand-side paddle
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Creates right-hand-side paddle
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Creates the ball object
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))
# ----------------------------------------------- END OBJECTS ----------------------

# ----------------------------------------------- BEGIN FUNCTIONS ----------------------
# Will move the paddle on the left upwards and downwards
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

# Will move the paddle on the left upwards and downwards
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
# ----------------------------------------------- END FUNCTIONS ----------------------

# Here we declare what keys will be used to play the game. Left paddle will use 'w' and 's', right paddle will use the 'up' and 'down' arrow keys.
wn.listen() # os module waiting for input 
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# ----------------------------------------------- GAME CONDITIONS ----------------------
while True: # keeps the game going
    wn.update()
    
    # Moves the ball around the screen window
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    """
    Border Checking around the window
    """
    # These conditions are for making sure the ball stays in the valid playing area by checking it's up and down position.
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.wav&") # simple sound effect
    
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    # These conditions are for making sure the ball stays in the valid playing area by checking it's left and right position.
    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Defining the collisions between a paddle and the ball object

    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1 
        os.system("afplay bounce.wav&")
    
    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
        os.system("afplay bounce.wav&")


    
