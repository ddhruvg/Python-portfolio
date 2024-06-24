from turtle import Turtle, Screen
import random
import time
from oops import Snake
from food import Food
from scoreboard import Scoreboard
screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to Snake Game!")
score=Scoreboard()
screen.tracer(0)

snake=Snake()
food=Food()
screen.listen()
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Left",fun=snake.left)
screen.onkey(key="Right",fun=snake.right)



game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.every_square[0].distance(food)<15:
        food.refresh()
        snake.extent()
        score.incerse_score()
    if snake.every_square[0].xcor()>280 or snake.every_square[0].xcor()<-280:
        print("Game Over!")
        score.game_over()
        break

    if snake.every_square[0].ycor() > 280 or snake.every_square[0].ycor() < -280:
        print("Game Over!")
        score.game_over()
        break
    for square in snake.every_square[1:]:
        if snake.every_square[0].distance(square)<10 :
            score.game_over()
            print("Game over!")
            game_is_on=False
            break



screen.exitonclick()

