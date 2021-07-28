import random
import turtle
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?Enter your color:\n")

y_position = [-70, -40, -10, 20, 50, 80]
color = ["red","yellow","green","blue","purple","orange"]
all_turtle = []

is_race = False

for turtle_index in range(0,6):
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.color(color[turtle_index])
    new_turtle.shape("turtle")
    new_turtle.goto(x=-200, y=y_position[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race = True

while is_race:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race = False
            if winning_color == user_bet:
                print(f"You've won and the {winning_color} turtle is the winner")
            else:
                print(f"You've lost and the {winning_color} turtle is the winner")

        rand_forward = random.randint(0, 10)
        turtle.fd(rand_forward)





"""
def move_forward():
    tim.fd(10)
def move_backward():
    tim.bk(10)
def turn_left():
    tim.lt(10)
def turn_right():
    tim.rt(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_forward,"d")
screen.onkey(turn_right, "r")
screen.onkey(turn_left,"l")
screen.onkey(move_backward,"b")
screen.onkey(clear,"c")
clear()
"""





screen.exitonclick()
