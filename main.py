import turtle
from turtle import Turtle, Screen, colormode
import random


turtle.colormode(255)
t = Turtle()
t.hideturtle()
t.speed("fast")

# import colorgram
#
# colors = colorgram.extract('hirst.jpg', 40)
#
# rgb_list = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     my_tuple = (r, g, b)
#     rgb_list.append(my_tuple)
#
# print(rgb_list)

rgb_colors = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51), (6, 68, 42), (176, 176, 233), (239, 168, 161), (249, 8, 48), (5, 246, 222), (15, 76, 110), (243, 15, 14), (38, 43, 221)]

t.penup()
t.setheading(225)
t.forward(300)
t.setheading(0)
t.pendown()

for y in range(10):
    for x in range(10):
        t.dot(20, random.choice(rgb_colors))
        t.penup()
        t.forward(50)
        t.pendown()

    t.penup()
    t.setheading(90)
    t.forward(50)
    t.setheading(180)
    t.forward(500)
    t.setheading(0)
    t.pendown()











screen = Screen()
screen.exitonclick()
