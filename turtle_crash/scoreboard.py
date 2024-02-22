from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.penup()
        self.goto(-200,250)
        self.write(f"Level : {self.level}",align="center",font=FONT)
        self.hideturtle()
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align="left",font=FONT)
        self.hideturtle()
    def level_increase(self):
        self.clear()
        self.level+=1
        self.write(f"Level : {self.level}",align="center",font=FONT)

    
