from turtle import Turtle, Screen
import time, random
class Snake:

    def __init__(self, lenght = 3):
        self.lenght = lenght
        self.trunk = []
        self.grid_step = 20
        self.direction = "right"
        self.alive = True

    def create_trunk(self):
        for i in range(self.lenght):
            tt = Turtle()
            tt.shape("square")
            tt.color("yellow")
            tt.pu()
            tt.setx(-(self.grid_step * i))
            self.trunk.append(tt)
        self.trunk[0].color("light yellow")

    def snake_die(self):
        self.alive = False
        game_over = Turtle()
        game_over.color("brown")
        game_over.write(f"GAME OVER", move=False, align="center", font=("Impact", 72, "bold"))

    def snake_grow(self, count):
        tt = Turtle()
        tt.shape("square")
        tt.color("yellow")
        tt.pu()
        tt.goto(self.trunk[-1].position())
        self.trunk.append(tt)

    def move(self):
        for piece in range(1, len(self.trunk)):

            if self.trunk[0].distance(self.trunk[piece]) < 10:
                self.snake_die()
                print(self.alive)


        for piece_num in range(len(self.trunk) - 1, 0, -1):
            new_x = self.trunk[piece_num - 1].xcor()
            new_y = self.trunk[piece_num - 1].ycor()
            self.trunk[piece_num].goto(new_x, new_y)

        self.trunk[0].forward(self.grid_step)
        if self.trunk[0].xcor() > 280 or self.trunk[0].xcor() < -280 or self.trunk[0].ycor() > 280 or self.trunk[0].ycor() < -280:
            self.snake_die()



    def right_move(self):
        if self.direction != "left":
            self.trunk[0].setheading(0)
            self.direction = "right"

    def up_move(self):
        if self.direction != "down":
            self.trunk[0].setheading(90)
            self.direction = "up"

    def left_move(self):
        if self.direction != "right":
            self.trunk[0].setheading(180)
            self.direction = "left"

    def down_move(self):
        if self.direction != "up":
            self.trunk[0].setheading(270)
            self.direction = "down"



