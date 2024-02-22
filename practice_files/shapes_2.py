from turtle import Turtle,Screen
timmy=Turtle()
timmy.shape("arrow")
colours=["burlywood1","brown","blueviolet","cyan1","darkgoldenrod1","red","blue","black"]
def draw(num_of_sides):
    angle=360/num_of_sides
    timmy.color(colours[num_of_sides-3])
    for sides in range(num_of_sides):
        
        timmy.forward(100)
        timmy.right(angle)
for sides in range(3,11):
    draw(sides)

my_screen=Screen()
my_screen.exitonclick()