import random
from turtle import Screen, Turtle
from paddle import STARTING
import paddle
from paddle import Paddle, paddles
from ball import Ball
from scoreboard import Scoreboard

import time

s = Screen()
s.setup(width=800, height=600)
s.bgcolor("black")
s.title("PingPong")
# sc = Scoreboard()
p = Paddle()
left_paddle = paddles[0]
right_paddle = paddles[1]
s.tracer(0)


def move_up():
    if left_paddle.ycor() <= 200:
        y = left_paddle.ycor()
        left_paddle.goto(left_paddle.xcor(), y + 40)


def move_down():
    if left_paddle.ycor() >= -200:
        y = left_paddle.ycor()
        left_paddle.goto(left_paddle.xcor(), y - 40)


def move_upr():
    if right_paddle.ycor() <= 200:
        y = right_paddle.ycor()
        right_paddle.goto(right_paddle.xcor(), y + 40)


def move_downr():
    if right_paddle.ycor() >= -200:
        y = right_paddle.ycor()
        right_paddle.goto(right_paddle.xcor(), y - 40)


b = Ball()

game = True
s.listen()
s.onkey(fun=move_up, key="w")
s.onkey(fun=move_down, key="s")
s.onkey(fun=move_upr, key="Up")
s.onkey(fun=move_downr, key="Down")

while game:
    time.sleep(0.1)
    s.update()
    b.move()

    if b.ycor() >= 270 or b.ycor() <= -270:
        b.bounce_y()

    if b.distance(right_paddle) < 50 and b.xcor() < 320 or b.distance(left_paddle) < 50 and b.xcor() < -320:
        b.bounce_x()

    if b.xcor() >= 351:
        b.reset_pos()

    if b.xcor() <= -351:
        b.reset_pos()

s.exitonclick()
