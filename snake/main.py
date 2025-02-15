from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title("snake-game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,'Up') 
screen.onkey(snake.down,'Down') 
screen.onkey(snake.left,'Left') 
screen.onkey(snake.right,'Right') 

game_is_on = True
while game_is_on:
    screen = Screen()
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food)<15:
        snake.extend()
        food.refresh()
        scoreboard.update_score()

    # Detect collission with wall
    if snake.head.xcor() > 290 or snake.head.xcor () <-290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()
    
    # Detect collission with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.reset()
            snake.reset()




screen.exitonclick()