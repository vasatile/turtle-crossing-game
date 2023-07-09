import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
car_manager = CarManager()


turtle = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(turtle.go_up, "Up")





game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    #detect car colision

    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            game_is_on = False
            scoreboard.game_over()

    #detect successful crosing

    if turtle.is_at_finish_line():
        turtle.goto_start()
        car_manager.level_up()
        scoreboard.increase_level()



screen.exitonclick()


