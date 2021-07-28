###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##

# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     rgb_colors.append(color.rgb)
#
# print(rgb_colors)
# print(len(rgb_colors))

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors[0])
#
# print(rgb_colors)
# print(len(rgb_colors))
import random
from turtle import Screen
import turtle as t


color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
              (107, 127, 153), (176, 192, 208), (168, 99, 102)]






tim = t.Turtle()
t.colormode(255)
tim.shape("turtle")
tim.penup()
tim.hideturtle()
number_of_dots = 100

tim.setheading(225)
tim.fd(300)
tim.setheading(0)

def turn_right ():
    tim.setheading(90)
    tim.fd(50)
    tim.setheading(100)
    tim.fd(500)
    tim.setheading(0)


for dots in range(1,number_of_dots + 1):
    tim.speed(6)
    tim.dot(20, random.choice(color_list))
    tim.fd(50)
    tim.pen(pensize=5)

    if dots % 10 == 0:
        tim.setheading(90)
        tim.fd(50)
        tim.setheading(180)
        tim.fd(500)
        tim.setheading(0)









screen = Screen()
screen.exitonclick()
