# coding:utf-8

# TODO-1 - Create a snake body
from turtle import Screen, Turtle
from snake import Snake
import time
from turtle import Screen
from food import Food
from snake import Snake
from Scoreboard import Scoreboard_table

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

# TODO-2 - Move the snake

tim = Snake()
food = Food()
score = Scoreboard_table()

screen.onkey(tim.up, "Up")
screen.onkey(tim.down, "Down")
screen.onkey(tim.right, "Right")
screen.onkey(tim.left, "Left")
screen.listen()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    tim.move_snake()

    if tim.head.distance(food) < 15:
        food.refresh()
        tim.extend()
        score.increase_score()

    if tim.head.xcor() > 280 or tim.head.xcor() < -280 or tim.head.ycor() > 280 or tim.head.ycor() < -280:
        score.my_reset()
        tim.my_reset()

    for segments in tim.segments[1:]:
        if tim.head.distance(segments) < 15:
            score.my_reset()
            tim.my_reset()

screen.exitonclick()

# TODO-3 - Crontrol the snake
