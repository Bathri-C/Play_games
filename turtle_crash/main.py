import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
FINISH_LINE_Y=280
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()
screen.listen()
screen.onkey(player.move_forward,"Up")
car_manager=CarManager()
scoreboard=Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_car:
        if car.distance(player)<30:
            game_is_on=False
            scoreboard.game_over()
    if player.ycor()>FINISH_LINE_Y:
        player.refresh()
        car_manager.level_up()
        scoreboard.level_increase()


screen.exitonclick()
    
