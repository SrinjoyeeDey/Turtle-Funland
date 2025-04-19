from turtle import Turtle,Screen
import random


is_race_on=False
screen=Screen()
screen.setup(width=500,height=400)

user_choice=screen.textinput(title="Make your Bet,", prompt="Guess which Turtle will win the race? Enter a color: ")
colors=["red","orange","yellow","green","blue","purple"]
y_positions=[-70,-40,-10,20,50,80]
all_turtles=[]

for turtle_index in range(0,6):
    tim=Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230,y=y_positions[turtle_index])
    all_turtles.append(tim)


if user_choice:
    is_race_on=True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            win_color=turtle.pencolor()
            if win_color==user_choice:
                print(f"you've won! The {win_color} turtle is the winner!")
            else:
                print(f"you've lost! The {win_color} turtle is the winner!")
                break

        
        random_dist=random.randint(0,10)
        turtle.forward(random_dist)



screen.exitonclick()