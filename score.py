from turtle import Turtle
ALIGN = 'center'
FONT = ("Arial", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(arg=f"Score: {self.score}", align=ALIGN, font=FONT)


    def add_score(self):
        # self.clear()
        self.score += 1
        self.clear()
        self.update_score()

