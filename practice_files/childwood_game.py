import turtle as t
import random
tommy=t.Turtle()
angle=0
tommy.speed(10)
t.colormode(255)
tommy.pensize(1)

def random_color():
    r=random.randint(0,200)
    g=random.randint(0,200)
    b=random.randint(0,200)
    my_color=(r,g,b)
    tommy.color(my_color)

def draw_spirograph(size):
    for _ in range(int(360/size)):
        random_color()
        tommy.circle(100)
        tommy.setheading(tommy.heading()+size)
    
draw_spirograph(5)












t.Screen().exitonclick()