import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("DarkGrey")
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
player.reset_position()

screen.listen()
screen.onkey(player.move, "Up")

scoreboard = Scoreboard()
car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_new_car()
    car_manager.move()

    for car in car_manager.all_cars:
        if car.distance(player) <= 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect crossing the finish-line
    if player.ycor() > 280:
        player.reset_position()
        scoreboard.level_count()
        car_manager.speed_up()

screen.exitonclick()
