from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(500, 400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -60, -20, 20, 50, 100]

user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? Enter a color: "
)

if user_bet is not None:
    user_bet = user_bet.strip().lower()

all_turtles = []

for turtle_index in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

is_race_on = user_bet in colors

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner.")
            else:
                print(f"You lost. The {winning_color} turtle us the winner.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

 
screen.exitonclick()