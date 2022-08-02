from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.score_num = -1
        self.count()

    def count(self):
        self.clear()
        self.score_num += 1
        self.write(f"Score: {self.score_num}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)
