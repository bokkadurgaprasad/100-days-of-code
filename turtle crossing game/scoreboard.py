from turtle import Turtle

FONT =  ("courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-380,250)
        self.update_level()
    
    def update_level(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase(self):
        self.level += 1
        self.clear()
        self.update_level()

    