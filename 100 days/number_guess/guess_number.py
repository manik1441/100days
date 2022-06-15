import time
import turtle
from random import randint
from turtle import Screen

print('''
   _____                       _   _            _   _                 _               
  / ____|                     | | | |          | \ | |               | |              
 | |  __ _   _  ___  ___ ___  | |_| |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __| | __| '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \ | |_| | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/  \__|_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     
''')


scr = Screen()
scr.setup(500, 400)
title_txt = 'Please select your Number.'
style = ('Arial', 50, 'italic')
turtle.color('red')
colors = ['red', 'green', 'black', 'yellow', 'purple']

num = randint(1, 10)
for i in range(5):
    inp = scr.textinput(title="Guess the Number", prompt=title_txt)
    inp = int(inp)
    if inp == num:
        while True:
            for i in colors:
                turtle.color(i)
                turtle.write('You are Correct', font=style, align='center')
    elif inp > num:
        title_txt = 'You guessed too high, Select Again'
    elif inp < num:
        title_txt = 'You guessed too low, Select Again'
    if 4 - i != 0:
        title_txt += '''
            Only {} attempts left'''.format(4 - i)
    else:
        turtle.write('Sorry, No attempts left', font=style, align='center')

scr.exitonclick()
