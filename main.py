from snake import Snake
from turtle import Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)


snake_game = Snake()
game_is_on = True


screen.listen()
screen.onkey(snake_game.up, "Up")
screen.onkey(snake_game.down, "Down")
screen.onkey(snake_game.left, "Left")
screen.onkey(snake_game.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake_game.move()
screen.exitonclick()
