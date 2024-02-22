# import colorgram
# rgb_color=[]
# colors=colorgram.extract("image.jpg",12)
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     rgb_value=(r,g,b)
#     rgb_color.append(rgb_value)
# print(rgb_color)
import turtle as t
import random
t.colormode(255)
tim=t.Turtle()
color_list=[(235, 225, 209), (210, 156, 97), (187, 64, 25), (216, 218, 226), (141, 144, 156), (234, 215, 224), (97, 106, 136), (229, 211, 110), (190, 157, 30), (205, 151, 177), (223, 231, 225), (93, 114, 178)]
tim.penup()
tim.setheading(225)
tim.forward(270)
tim.setheading(360)

def map():
    for i in range(10):
        tim.dot(20,random.choice(color_list))
        tim.penup()
        tim.forward(50)
for _ in range(5):

    map()
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.penup()
    tim.forward(50)
    map()
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(360)
    tim.penup()
    tim.forward(50)









t.Screen().exitonclick()