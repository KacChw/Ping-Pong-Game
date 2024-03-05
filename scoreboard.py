from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.setposition(position)
        self.write(f"{self.l_score}", align="center", font=('Courier', 40, 'normal'))
        self.hideturtle()

    def clear_l_scoreboard(self):
        self.write(f"{self.l_score}", align="center", font=('Courier', 40, 'normal'))

    def clear_r_scoreboard(self):
        self.write(f"{self.r_score}", align="center", font=('Courier', 40, 'normal'))

    def update_l(self):
        self.l_score += 1
        self.clear()
        self.clear_l_scoreboard()

    def update_r(self):
        self.l_score += 1
        self.clear()
        self.clear_l_scoreboard()