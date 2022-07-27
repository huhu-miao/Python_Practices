# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# colors_list = []
# for i in range(30):
#     current_color = colors[i]
#     rgb = current_color.rgb
#     red = rgb.r
#     green = rgb.g
#     blue = rgb.b
#     color = (red, green, blue)
#     colors_list.append(color)
# print(colors_list)

from turtle import Turtle, colormode, dot, Screen
import random

my_screen = Screen()
my_screen.screensize(500, 500)

colormode(255)
colors_list = [(239, 247, 245), (2, 13, 31), (52, 25, 17), (217, 128, 107), (11, 104, 159), (241, 213, 69), (149, 83, 41), (215, 86, 64), (155, 7, 25), (164, 162, 32), (156, 62, 102), (11, 63, 33), (206, 74, 104), (12, 95, 57), (93, 7, 20), (176, 134, 162), (9, 173, 216), (2, 61, 144), (5, 212, 205), (157, 33, 24), (11, 138, 84), (146, 226, 217), (121, 193, 148), (221, 177, 216), (102, 218, 229), (117, 172, 194), (81, 134, 179)]

hirst = Turtle()
hirst.speed("fastest")
hirst.hideturtle()

x_position = -225
y_position = -225

hirst.penup()

for i in range(10):
    hirst.setpos(x_position, y_position)
    for j in range(10):
        color = random.choice(colors_list)
        hirst.dot(20, color)
        hirst.forward(50)
    y_position += 50


my_screen.exitonclick()
