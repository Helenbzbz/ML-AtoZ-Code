from turtle import Turtle
import random 

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-13, 13)
        random_y = random.randint(-13, 13)
        self.goto(random_x*20,random_y*20)



