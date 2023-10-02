from turtle import Screen
from snake import Snake
from food2 import Food
from Scoreboard import Scoreboard
import time
screen=Screen()
screen.setup(height=600,width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer()
snake=Snake()
food=Food()
score=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

is_moving=True
while is_moving:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #detect colision
    if snake.segment[0].distance(food) < 15:
        score.increase_score()
        snake.extend()
        food.move_food()
    elif snake.segment[0].xcor() > 280 or snake.segment[0].ycor() > 280:
        score.game_over()
        is_moving=False
    elif snake.segment[0].xcor() < -280 or snake.segment[0].ycor() < -280:
        score.game_over()
        is_moving=False
    #detect collision with tail
    for segment in snake.segment[1:]:
        if snake.segment[0].distance(segment) < 10:
            is_moving = False
            score.game_over()

screen.exitonclick()
