from turtle import Turtle, Screen
import random

turtle_colors = ["red", "green", "blue", "yellow", "purple", "orange", "black", "pink", "cyan", "magenta", "grey",
                 "pink", "lime", "brown", "navy", "olive", "teal", "maroon", "violet", "gold", "coral", "aqua", "beige",
                 "chocolate", "crimson", "darkgreen", "darkblue", "fuchsia", "gold", "indigo", "ivory", "khaki",
                 "lavender", "lightblue", "lightgreen", "magenta", "orange", "plum", "salmon", "turquoise"]


timmy = Turtle()
timmy.shape("turtle")
directions = [0, 90, 180, 270]
timmy.pensize(11)
timmy.speed(30)


def do_random_walk():
    for _ in range(1000):
        timmy.forward(30)
        timmy.setheading(random.choice(directions))
        timmy.color(random.choice(turtle_colors))


do_random_walk()
screen = Screen()
screen.exitonclick()
