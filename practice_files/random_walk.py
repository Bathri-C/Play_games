import turtle as t
import random
jerry=t.Turtle()
jerry.shape("turtle")

jerry.speed(0)
t.colormode(255)
direction=[0,90,180,270]
def random_color():
    r=random.randint(0,200)
    g=random.randint(0,200)
    b=random.randint(0,200)
    my_color=(r,g,b)
    jerry.color(my_color)


for i in range(200):
    jerry.pensize(15)
    random_color()
    jerry.forward(35)
    jerry.setheading(random.choice(direction))
    
  


my_screen=t.Screen()
my_screen.exitonclick()