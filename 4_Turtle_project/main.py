# coding:utf-8
import turtle
from turtle import Screen
import random

import turtle as t
t.colormode(255)

tim = t.Turtle()
tim.shape("turtle")
tim.color("red")
# tim.fd(100)
# tim.right(90)
# tim.fd(100)
# tim.right(90)
# tim.fd(100)
# tim.right(90)
# tim.fd(100)
#
"""
Draw different figure with different colors
"""
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
#            "SeaGreen"]
#
#
# def draw_shap(numbers_of_side):
#     angle = 360/numbers_of_side
#     for line in range(0,numbers_of_side):
#         tim.pen(pensize=3)
#         tim.speed(1)
#         tim.fd(100)
#         tim.rt(angle)
#     tim.color(random.choice(colours))
#
# draw_shap(3)
# draw_shap(4)
# draw_shap(5)
# draw_shap(6)
# draw_shap(7)
# draw_shap(8)
# draw_shap(9)
# draw_shap(10)
# # for line in range(10):
#     tim.pen(fillcolor="green", pencolor="red", pensize=5)
#     tim.speed(1)
#     tim.fd(10)
#     tim.pd()
#     tim.fd(10)
#     tim.pu()
#     tim.fd(10)
"""
Random color
"""


def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color_t = (r,g,b)
    return random_color_t
#
#
# movement = [0, 90, 180, 270]
# for x in range(80):
#     tim.heading()
#     tim.pen(pencolor="", pensize=5)
#     tim.color(random_color())
#     tim.speed(8)
#     tim.fd(20)
#     tim.setheading(random.choice(movement))
    #     tim.speed(1)
    #     tim.fd(100)
    #     tim.rt(90)
    # tim.color(random.choice(colours))


"""
Circle
"""


def drw_spirograph(size_of_circle):
    for _ in range(int(360/size_of_circle)):
        tim.color(random_color(), random_color())
        #tim.begin_fill()
        tim.speed(10)
        current_heading = tim.heading()
        tim.dot(10,"green")
        tim.circle(100)
        #tim.end_fill()
        tim.setheading(current_heading + 10)

drw_spirograph(50)









screen = Screen()
screen.exitonclick()
