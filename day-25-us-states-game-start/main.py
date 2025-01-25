import turtle
import pandas as pd
from name import Name

screen = turtle.Screen()
screen.title("U.S. States Game")
image = r'day-25-us-states-game-start\blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
name = Name()
count = 50
while count >0 :
    answer_state = screen.textinput(title=fr"{50-count}/50 states are completed",prompt="Enter a state name").lower()
    if answer_state == 'exit':
        name.exit()
        break
    if name.check_and_move(guess=answer_state):
        count-=1
        
        
screen.exitonclick()