from turtle import Turtle, Screen
import random

# importing all classes from module(UNUSUAL IN PYTHON COMMUNITY)
# from turtle import *

# Alisaing modules
import heroes as h
print(h.gen())

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("orange")
turtle_colors = ["red", "green", "blue", "yellow", "purple", "orange", "black", "pink", "cyan", "magenta", "grey",
                 "pink", "lime", "brown", "navy", "olive", "teal", "maroon", "violet", "gold"]


# Challenge-1 Draw the square
def draw_square():
    for _ in range(0, 4):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(90)


# Draw dotted line
def draw_dotted_line():
    for _ in range(15):
        timmy_the_turtle.forward(10)
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(10)
        timmy_the_turtle.pendown()


def draw_from_traingle_to_n_shapes(max_no_of_sides):
    timmy_the_turtle.left(90)
    timmy_the_turtle.forward(15)
    for num in range(3, max_no_of_sides + 1):
        for i in range(0, num):
            timmy_the_turtle.forward(100)
            timmy_the_turtle.right(360/num)
        timmy_the_turtle.color(random.choice(turtle_colors))


# draw_square()
# draw_dotted_line()
draw_from_traingle_to_n_shapes(50)


screen = Screen()
screen.exitonclick()
