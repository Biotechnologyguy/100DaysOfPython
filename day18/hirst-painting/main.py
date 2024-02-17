import colorgram
import random
from turtle import Turtle, Screen, colormode

timmy = Turtle()
colormode(255)

# Extracting colors from image using colorgram.py package
colors = colorgram.extract('img.png', 110)

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
print(rgb_colors)
timmy.setheading(225)
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
timmy.forward(250)
timmy.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, random.choice(rgb_colors))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)




screen = Screen()
screen.exitonclick()
