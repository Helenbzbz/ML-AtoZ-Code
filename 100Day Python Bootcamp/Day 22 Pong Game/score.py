from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) :
        super().__init__()
        self.scoreleft = 0
        self.scoreright = 0
        self.penup()
        self.goto(0, 230)
        self.hideturtle()
        self.pencolor("white")
        self.update()

    def update(self):
        self.write(f"{self.scoreleft}   {self.scoreright}", False, align = "center", font = ("Arial", 60, "normal"))

    def increase_leftscore(self):
        self.scoreleft += 1
        self.clear()
        self.update()
    
    def increase_rightscore(self):
        self.scoreright += 1
        self.clear()
        self.update()
    
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER", False, align = "center", font = ("Arial", 24, "normal"))
