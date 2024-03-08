from turtle import Turtle, Screen

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# each turtle is of 20 * 20 px
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.goto(position)







screen.exitonclick()

