from turtle import Turtle, Screen, colormode
import random


timmy = Turtle()
timmy.speed(30)
colormode(255)


def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_colors())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spirograph(5)


screen = Screen()
screen.exitonclick()
