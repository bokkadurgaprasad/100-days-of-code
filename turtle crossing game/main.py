from turtle import Screen
from player import Player
from carmanager import CarManager
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
level = Scoreboard()


screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_car()

    #detect collosion with cars
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            player.game_over()

    

    #detect the collosion with finish line
    if player.is_at_finish_line():
        player.go_to_start()
        cars.level_up()
        level.increase()



screen.exitonclick()