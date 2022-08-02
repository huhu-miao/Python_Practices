from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("Black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.2)

    snake.move()

    # Detect eat the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.count()

    # Detect hit the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        is_game_on = False
        score.game_over()

    # Detect collision with the tail
    
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            score.game_over()

    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         is_game_on = False
    #         score.game_over()

screen.exitonclick()
