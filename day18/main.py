from turtle import Turtle, Screen

# importing all classes from module(UNUSUAL IN PYTHON COMMUNITY)
# from turtle import *

# Alisaing modules
import heroes as h
print(h.gen())

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("orange")


# Challenge-1 Draw the square
def draw_square():
    for _ in range(0, 4):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(90)


# Draw dotted line
for _ in range(15):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()



# draw_square()



screen = Screen()
screen.exitonclick()
