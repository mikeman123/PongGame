# *****************************************************************************
# Program: Pong.py
# Language: Python 3.10.6
#
# Description: This program is a classic pong game
#
# College: Husson University
# Course: IT 262 - Spring 2023
# Author: Michael Desjardins
#
# Change Log:
# Date          Description of Change
# -----------------------------------
# 03-1-2023    intitial Draft
# 03-2-2023    created the screen, paddles, ball, and pen
# 03-5-2023    Made it so you can move the paddles
# 03-10-2023   made the ball move and bounce of walls and paddles
# 03-14-2023   added the scoring logic
# 03-25-2023   made players paddle be able to move my using the mouse
# 03-28-2023   made different difficulty levels
# 04-10-2023   fixed the problem with the ball speeding up and slowing down
# *****************************************************************************

import turtle
import random
import time

# Set screen
wn = turtle.Screen()
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)
wn.title("Pong")

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.shapesize(5, 1)

# Ai player
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.shapesize(5, 1)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.dx = 0
ball.dy = 0

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.goto(0, 260)
pen.write("Player: 0  Computer: 0", align='center', font=('Courier', 24, 'bold'))
pen.hideturtle()

# quit
quit = turtle.Turtle()
quit.speed(0)
quit.color('red')
quit.penup()
quit.goto(0, 230)
quit.write("Press 'q' to quit game", align='center', font=('Courier', 24, 'bold'))
quit.hideturtle()

# Score
setScore = 0
score_a = 0
score_b = 0

# This function makes paddle_a move up
def paddle_a_up():
    y = paddle_a.ycor()
    y += 30
    if y + 50 > 300:  # Check if paddle is at the top border
        y = 250
    paddle_a.sety(y)

# This function makes paddle_a move down
def paddle_a_down():
    y = paddle_a.ycor()
    y += -30
    if y - 50 < -300:  # Check if paddle is at the bottom border
        y = -250
    paddle_a.sety(y)

# Function to move paddle_a smoothly up and down with mouse drag
def drag_paddle_a(x, y):
    paddle_a.ondrag(None)
    paddle_a.sety(y)
    paddle_a.ondrag(drag_paddle_a)
# Bind the mouse drag event to the paddle_a function
paddle_a.ondrag(drag_paddle_a)

# Choose difficulty level
difficulty = None
while difficulty not in ["easy", "medium", "hard"]:
    difficulty = wn.textinput("Choose difficulty level", "Enter 'easy', 'medium', or 'hard': \nGame Controls: 'w' up and 's' down or draging your mouse").lower()


# create different difficulty levels for the game
if difficulty == 'easy':
    paddle_b_speed = 40
    ball.goto(0, 0)
    ball.dx = random.choice([-7, 7])
    ball.dy = 0
    time.sleep(1)
    setScore = 8

elif difficulty == 'medium':
    paddle_b_speed = 65
    ball.goto(0, 0)
    ball.dx = random.choice([-9, 9])
    ball.dy = 0
    time.sleep(1)
    setScore = 8
else:
    paddle_b_speed = 64
    ball.goto(0, 0)
    ball.dx = random.choice([-12, 12])
    ball.dy = 0

    time.sleep(1)
    setScore = 8

# This function make the ai player move
def aiPlayer():
    global paddle_b_speed
    y = paddle_b.ycor()

    # Check if paddle is at the top or bottom of the border
    if y - 50 < -300:
        y = -250
    if y + 50 > 300:
        y = 250

    # controls the movement of the ai player
    if y < ball.ycor():
        y += paddle_b_speed * 0.025
    elif y > ball.ycor():
        y -= paddle_b_speed * 0.025
    paddle_b.sety(y)

def quit():
    global running
    running = False

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(quit, "q")

# Main game loop
running = True
while running:
    time.sleep(1 / 130)
    # closes the window and ends the game
    wn.onkeypress(quit, "q")

    wn.update()

    # Moving Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # moving ai player
    aiPlayer()

    # Border checking
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1

    # Check Score
    if ball.xcor() > 390:
        paddle_b.goto(350, 0)
        paddle_a.goto(-350, 0)
        ball.goto(0, 0)
        ball.dx *= -1
        ball.dy = 0

        score_a += 1
        pen.clear()
        pen.write("Player: {}  Computer: {}".format(score_a, score_b), align='center', font=('Courier', 24, 'bold'))

    if ball.xcor() < -390:
        paddle_b.goto(350, 0)
        paddle_a.goto(-350, 0)
        ball.goto(0, 0)
        ball.dx *= -1
        ball.dy = 0

        score_b += 1
        pen.clear()
        pen.write("Player: {}  Computer: {}".format(score_a, score_b), align='center', font=('Courier', 24, 'bold'))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (
            ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() - 60):
        ball.setx(340)
        ball.dx *= -1
        ball.dy = random.choice([-3.5, 3.5]) * random.uniform(0.3, 0.7)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (
            ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() - 60):
        ball.setx(-340)
        ball.dx *= -1
        ball.dy = random.choice([-3.5, 3.5]) * random.uniform(0.3, 0.7)


    # Win condition
    if score_a >= setScore or score_b >= setScore:
        pen.clear()
        pen.write("{}".format("YOU WIN!" if score_a >= setScore else "COMPUTER WINS!"), align='center', font=('Courier', 24, 'bold'))
        ball.dx = 0
        ball.dy = 0

if score_a == setScore:
    print("You Win!!!!!")
elif score_b == setScore:
    print("Computer Won!")

