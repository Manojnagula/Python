from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier",24,'normal')

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        with open("snake\data.txt") as data:
            self.high_score=int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f'Score : {self.score} High Score: {self.high_score}',align=ALIGNMENT,font=FONT)

    def update_score(self):
        self.score+=1
        self.display_score()

    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("snake\data.txt",mode='w') as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.display_score()        