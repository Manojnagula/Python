from turtle import Turtle
class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.display_score()
    
    def display_score(self):
        self.goto(-100,200)
        self.write(self.l_score,align="center",font=("Courier",80,"normal"))
        self.goto(100,200)
        self.write(self.r_score,align="center",font=("Courier",80,"normal"))

    
    def update_scoreboard(self,player):
        self.clear()
        if player == 'left':
            self.l_score+=1
            self.display_score()
        else:
            self.r_score+=1
            self.display_score()