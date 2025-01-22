from turtle import Turtle
import random

COLORS = ['black','green','red','yellow','purple','cyan','pink','blue']
STARTING_MOVE_DISTANCE = 5
MOVE_DISTANCE = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
    
    def create_cars(self):
        chance = random.randint(1,6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)
    
    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)