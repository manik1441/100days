import random
import turtle
from turtle import Turtle, Screen

scr = Screen()
user_bet = scr.textinput(title="Make your bet", prompt="Please select your Turtle.").lower()
bet_color = True
scr.setup(500, 400)
colors = ['red', 'green', 'blue']
while bet_color:
    if user_bet in colors:
        bet_color = False
    else:
        user_bet = scr.textinput(title="Make your bet", prompt="Select the right color").lower()
y_pos = 10
all_turtles = []
for i in range(3):
    tim = Turtle(shape='turtle')
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230, y=y_pos)
    y_pos += 30
    all_turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            if turtle.pencolor() == user_bet:
                scr.textinput(title=f'you\'ve Won. {turtle.pencolor()} has won.')
                # print(f'you\'ve Won. {turtle.pencolor()} has won.')
            else:
                scr.textinput(title=f'you\'ve Lost. {turtle.pencolor()} has won.')
                # print(f'You\'ve Lost. {turtle.pencolor()} has won.')
        else:
            rand_dist = random.randint(0, 10)
            turtle.forward(rand_dist)


scr.exitonclick()
