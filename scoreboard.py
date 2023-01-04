from turtle import Turtle

FONT = ("Courier", 24, "bold")
ALIGN = ["left", "right"]
POS = [(-100, 250), (100, 250)]


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.create()

    def create(self):
        for i in range(0, 2):
            self.score = 0
            self.color("white")
            self.penup()
            self.hideturtle()
            self.goto(POS[i])
            self.update()

    def update(self):
        for i in range(0, 2):
            self.write(f"Score:{self.score}", align=ALIGN[i], font=FONT)
