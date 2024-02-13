from turtle import Turtle, Screen, colormode
import random

my_tuple = (5, 11, 2)

# We can access elements same like list
print(my_tuple[2])

# We can not modify elements of the tuple(immutable)
# my_tuple[1] = 11 # Not allowed

# convert to list
my_tuple = list(my_tuple)
print(my_tuple)


def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


timmy = Turtle()
timmy.shape("turtle")
directions = [0, 90, 180, 270]
timmy.pensize(11)
timmy.speed(30)
colormode(255)


def do_random_walk():
    for _ in range(1000):
        timmy.forward(30)
        timmy.setheading(random.choice(directions))
        timmy.color(random_colors())


do_random_walk()
screen = Screen()
screen.exitonclick()


