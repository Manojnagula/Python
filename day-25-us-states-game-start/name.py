from turtle import Turtle
import pandas as pd

states_info = pd.read_csv(r"day-25-us-states-game-start\50_states.csv")
states_info['state']=states_info['state'].apply(lambda x:str(x).lower())

class Name(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.correct_guesses=[]
    
    def check_and_move(self,guess):
        answer_state = guess
        if answer_state in states_info['state'].to_list() and answer_state not in self.correct_guesses:
            self.correct_guesses.append(answer_state)
            cors = states_info[states_info['state']==answer_state]
            self.penup()
            self.goto(cors['x'].item(),cors['y'].item())
            self.write(answer_state)
            self.hideturtle()
            return True
    
    def exit(self):
        states_info[~states_info['state'].isin(self.correct_guesses)].to_csv(r"day-25-us-states-game-start\states_not_guessed.csv")

