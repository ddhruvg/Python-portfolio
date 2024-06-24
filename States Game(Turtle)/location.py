import turtle
class Goto(turtle.Turtle):
    def __init__(self,xx,yy):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x=xx,y=yy)
    def to_write(self,state):
        self.write(f"{state}",align="center",font=("Arial",8,"normal"))