from  turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.speed('fastest')
        self.color('blue')
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.refresh()
       
    def refresh(self):
        x_random = random.randint(-300,300)
        y_random = random.randint(-300,300)
        self.goto(x_random ,y_random)