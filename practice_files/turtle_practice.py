from turtle import Turtle,Screen
tom=Turtle()
tom.shape("turtle")
for _ in range(50):
    tom.forward(10)
    tom.penup()
    tom.forward(10)
    tom.pendown()
    tom.speed(0)
my_screen=Screen()
my_screen.exitonclick()
