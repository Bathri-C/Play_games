from turtle import Turtle,Screen
import random
num=random.randint(50,250)
tim=Turtle()
screen=Screen()
def move_forward():
    tim.forward(num)
def move_backward():
    tim.backward(num)
def turn_anticlockwise():
    tim.left(num)
def turn_clockwise():
    tim.right(num)
def erase():
    tim.clear()
    tim.reset()

screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="a",fun=turn_anticlockwise)
screen.onkey(key="d",fun=turn_clockwise)
screen.onkey(key="c",fun=erase)
screen.exitonclick()