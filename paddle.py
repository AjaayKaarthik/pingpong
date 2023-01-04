from turtle import Turtle

paddles = []
STARTING = [(-350, 0), (350, 0)]


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.create_paddle()

    def create_paddle(self):
        for pos in STARTING:
            new = Turtle("square")
            new.color("white")
            new.penup()
            new.shapesize(stretch_len=1, stretch_wid=5)
            new.goto(pos)
            paddles.append(new)
