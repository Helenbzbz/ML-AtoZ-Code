###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
# import colorgram
# rgb_colors = []
# colors = colorgram.extract("/Users/jielanzheng/Desktop/Summer Plan/3. Machine Learning A-Z (Codes and Datasets)/ML-AtoZ-Code/100Day Python Bootcamp/Day 18 Turtle Class/image.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))

colors = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
import turtle
import random


t = turtle.Turtle()
t.hideturtle()
t.speed("fastest")
turtle.Screen().colormode(255)

def go_to_left_top():
    t.penup()
    t.right(180)
    t.forward(50*6)
    t.right(90)
    t.forward(50*6)
    t.right(90)
    t.pendown()

def line():
    for i in range(13):
        t.dot(20, random.choice((colors)))
        t.penup()
        t.forward(50)

def switch_line():
    t.back(50*13)
    t.right(90)
    t.forward(50)
    t.left(90)
    t.pendown()

go_to_left_top()
for i in range(12):
    line()
    switch_line()

turtle.Screen().exitonclick()