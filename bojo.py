from turtle import Turtle

class Bojo(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(0, -280)
        for _ in range(28):
            new_x = self.xcor()
            new_y = self.ycor()
            self.goto(new_x, new_y +20)
            self.dot()
            self.hideturtle()
        self.goto(-400, 295)
        for _ in range(39):
            new_x = self.xcor()
            new_y = self.ycor()
            self.goto(new_x + 20, new_y)
            self.dot()
            self.hideturtle()
        self.goto(-400, -285)
        for _ in range(39):
            new_x = self.xcor()
            new_y = self.ycor()
            self.goto(new_x + 20, new_y)
            self.dot()
            self.hideturtle()




