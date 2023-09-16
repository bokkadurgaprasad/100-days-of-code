from turtle import Turtle,Screen
import random

is_race_on = False

s = Screen()
s.setup(width=500, height=400)
user_bet = s.textinput(title="Make your bet", prompt="Which turtle will win the race?"
                        "Enter a color:\n(red,blue,green,yellow,orange,purple) ")
colors = ["red","orange","yellow","green","blue","purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_tutles = []


for turtle_index in range(0,6):
    new_turtle= Turtle(shape = "turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x= -230, y= y_position[turtle_index])
    all_tutles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_tutles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! the {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

s.exitonclick()