from turtle import Turtle

FONT = ("Courier", 24, "normal")

#On which level we are currently on and the game over message

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.update_score(self.level)
        
    def update_score(self, level):
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(-230, 260)
        self.write("Level: " + str(level), align="center", font=("Courier", 13, "normal"))
        
    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 13, "normal"))
        
    def increase_level(self):
        self.level += 1
        self.update_score(self.level) 
