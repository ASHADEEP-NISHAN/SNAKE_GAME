from turtle import Turtle
ALLIGNMENT="center"
FONT=('Arial', 22, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()
    def update_scoreboard(self):
        self.write(f"SCORE {self.score}",move=False,align=ALLIGNMENT,font=FONT)
    def increase_score(self):
        self.clear()
        self.score+=1
        self.update_scoreboard()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align=ALLIGNMENT, font=FONT)



# screen=Screen()
# sco=Scoreboard()
# sco.score(13)
# screen.exitonclick()