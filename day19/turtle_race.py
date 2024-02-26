from turtle import Turtle, Screen


screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your Bet",prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


for turtle_index in range(6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=100 - turtle_index * 40)


screen.exitonclick()
