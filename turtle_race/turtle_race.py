from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(width=800,height=600)
is_race_on=False
user_bet=screen.textinput(title="user_bet",prompt="Which turtle will win the race.Enter the color :")
colour=["red","orange","blue","purple","yellow","green"]
all_turtle=[]
x=-390 
y=-170
for _ in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colour[_])
    new_turtle.penup()
    new_turtle.goto(x,y)
    y+=60
    all_turtle.append(new_turtle)
if user_bet:
    is_race_on=True
    while is_race_on:
        for turtle in all_turtle:
            if turtle.xcor()>380:
                is_race_on=False
                winning_color=turtle.pencolor()
                if user_bet==winning_color:
                    print(f"you win.{winning_color} is the winning color")
                else:
                    print(f"you lose.{winning_color} won the race.")

            rand_dist=random.randint(0,10)
            turtle.forward(rand_dist)


    
screen.exitonclick()

