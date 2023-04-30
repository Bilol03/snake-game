from turtle import Turtle, Screen
import time

positions = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
class Snake:
    def __init__(self):
        self.snake_parts = []
        self.create_snake()
        self.head = self.snake_parts[0]
    def create_snake(self):
        for i in positions:
            turtle = Turtle(shape='square')
            turtle.color('white')
            turtle.penup()
            turtle.goto(i)
            self.snake_parts.append(turtle)

    def move(self):
        for snake in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[snake - 1].xcor()
            new_y = self.snake_parts[snake - 1].ycor()

            self.snake_parts[snake].goto(new_x, new_y)
        self.snake_parts[0].forward(move_distance)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)
