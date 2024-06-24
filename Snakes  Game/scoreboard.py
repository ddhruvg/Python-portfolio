from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.highest_score=0
        self.goto(y=260,x=0)
        self.score=0
        self.upadte_scoreboard()
    def  upadte_scoreboard(self):
        self.write(f"Score:{self.score}", align="center", font=("Arial", 24, "normal"))
    def incerse_score(self):
        self.score+=1
        self.clear()
        self.upadte_scoreboard()
    def game_over(self):
        self.clear()
        self.goto((0,0))
        self.write("Game Over!",align='center',font=("Arial", 24, "normal"))
