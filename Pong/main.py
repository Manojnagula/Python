from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # Detect collision with ball
    if ball.ycor() > 280 or ball.ycor()<-280:
        # needs to bounce
        ball.bounce('y')

    # Detect collission with paddle
    if ball.distance(r_paddle)<50 and ball.xcor() > 320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce('x')
    
    # If ball is missed
    if ball.xcor()>380:
        scoreboard.update_scoreboard('left')
        ball.reset_position()
        
    elif ball.xcor()<-380:
        scoreboard.update_scoreboard('right')
        ball.reset_position()






screen.exitonclick()