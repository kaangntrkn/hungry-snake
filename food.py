from turtle import Turtle
from random import randint




class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.color('coral')
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed('fastest')
        self.refresh()


    def refresh(self):
        position_x = randint(-280, 280)
        position_y = randint(-280, 280)
        self.goto(position_y, position_y)
