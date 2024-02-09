# Why we need OOP?
# splitting of tasks in modules
# Working simultaneously on modules
# reusable modules
# class = blueprint
# Object =


# Procedural programming vs OOP : PP = writing functions and using them. increasing complexity

# object ==> HAS = attributes
#            Does = methods

# How to create an object
#     obj = ClassName()

from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")

# https://docs.python.org/3/library/turtle.html
# Turtle docs
timmy.forward(100)
timmy.right(100)
timmy.forward(100)
my_screen = Screen()
print(my_screen.canvwidth)
print(my_screen.canvheight)

# Allows our program to run until we click
my_screen.exitonclick()





