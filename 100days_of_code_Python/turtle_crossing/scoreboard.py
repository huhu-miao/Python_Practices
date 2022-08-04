from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-220, 250)
        self.level = 1
        self.write(f"Level {self.level}", align="center", font=FONT)

    def level_count(self):
        self.clear()
        self.level += 1
        self.write(f"Level {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
