from snake import Snake
from turtle import Screen
import time
from food import Food
from score import  Score
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)


snake_game = Snake()

snake_food = Food()

score = Score()

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
#     If snake eats the food

    if snake_game.head.distance(snake_food) < 15:
        snake_food.refresh()
        score.add_score()
screen.exitonclick()
