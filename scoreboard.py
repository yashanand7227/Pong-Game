from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.hideturtle()
        self.penup()
        self.color('white')
    def update_score(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"{self.score1}  |  {self.score2}", align='center', font=('Times New Roman', 20, 'normal'))
