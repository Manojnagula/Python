from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Arial",24,'normal')

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.display_score()

    def display_score(self):
        self.write(f'Score : {self.score}',align=ALIGNMENT,font=FONT)

    def update_score(self):
        self.score+=1
        self.clear()
        self.write(f'Score : {self.score}',align=ALIGNMENT,font=FONT)
