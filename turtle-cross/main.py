from player import Player
import time
from turtle import Screen
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


car_manager = CarManager()
player = Player()
score_board = Scoreboard()


screen.listen()
screen.onkey(player.go_up,'Up')
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()

    # detect collission with car
    for car in car_manager.all_cars:
        if car.distance(player)<20:
            game_is_on=False
            score_board.game_over()
        
    # Check whether the player reached finish line
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        score_board.increase_level()

    
    
screen.exitonclick()