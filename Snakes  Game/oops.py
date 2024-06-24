from turtle import Turtle , Screen
import random
POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVEMENT=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake:
    def __init__(self):
        self.every_square = []
        self.create_snake()
    def create_snake(self):
        for i in POSITIONS:
            self.add_segment(i)

    def add_segment(self,i):
        timmy = Turtle(shape="square")
        timmy.color("white")
        timmy.penup()
        timmy.goto(i)
        self.every_square.append(timmy)

    def extent(self):
        self.add_segment(self.every_square[-1].position())


    def move(self):
        for i in range(len(self.every_square) - 1, 0, -1):
            x_cordinate = self.every_square[i - 1].xcor()
            y_cordinate = self.every_square[i - 1].ycor()
            self.every_square[i].goto((x_cordinate, y_cordinate))
        self.every_square[0].forward(MOVEMENT)

    def left(self):
        if self.every_square[0].heading!=0 or self.every_square[0].heading!=180:
            self.every_square[0].setheading(180)
    def right(self):
        if self.every_square[0].heading != 0 or 180:
            self.every_square[0].setheading(0)
    def up(self):
        if self.every_square[0].heading != 90 or 270:
            self.every_square[0].setheading(90)
    def down(self):
        if self.every_square[0].heading != 90 or 270:
            self.every_square[0].setheading(270)










