from turtle import Turtle

class scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.pencolor("white")
        self.update()

    def update(self):
        self.write(f"Score = {self.score}", False, align = "center", font = ("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()
    
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER", False, align = "center", font = ("Arial", 24, "normal"))


    

