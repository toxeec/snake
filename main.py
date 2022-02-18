from Snake import Snake
import time
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
#screen init
sc = Screen()
sc.setup(width=600, height=600)
sc.tracer(0)
sc.bgcolor("green")
sc.title("My snake return")
scr = Scoreboard()
suzi = Snake(5)
suzi.create_trunk()
food = Food()
game_is_on = True

def exit_game():
    print("QQQ")
    game_is_on = False

def keys_check():
    sc.onkey(suzi.right_move, "Right")
    sc.onkey(suzi.up_move, "Up")
    sc.onkey(suzi.left_move, "Left")
    sc.onkey(suzi.down_move, "Down")
    sc.onkey(suzi.snake_die, "q")

#suzi.food()
sc.listen()
keys_check()
while game_is_on and suzi.alive:
    sc.update()
    time.sleep(0.2)
    suzi.move()
    if suzi.trunk[0].distance(food) < 15:
        food.refresh()
        suzi.snake_grow(1)
        scr.increase()

scr.save_score()
scr.show_score()
sc.exitonclick()







