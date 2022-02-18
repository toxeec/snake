from turtle import Turtle, Screen
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.pu()
        self.hideturtle()
        self.sety(250)
        self.color("cyan")
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 14, "bold"))

    def increase(self):
        self.score +=1
        self.clear()
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 14, "bold"))

    def save_score(self):
        score_input = Screen()
        player_name = score_input.textinput("Save results", "Enter your name")
        fscores = open("fscores","at")
        print(f"{player_name} --- {self.score}",file=fscores)
        fscores.close()

    def show_score(self):
        fscores = open("fscores", "rt")
        vert = 200
        for sign in fscores:
            self.goto(0, vert)
            self.write(f"{sign}", move=False, align="center", font=("Arial", 14, "bold"))
            vert -= 20
        fscores.close()