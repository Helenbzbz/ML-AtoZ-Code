from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.goto(-260, 260)
        self.hideturtle()
        self.color("black")
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", False, align = "left", font = FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", False, align = "center", font = FONT)