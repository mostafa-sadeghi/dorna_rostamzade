# pip install pyinstaller

from turtle import Screen, Turtle
import sys
import os
from random import randint
from time import sleep


score = 0
if getattr(sys, 'frozen', False):
    wd = sys._MEIPASS
else:
    wd = ''

icon_image_path = os.path.join(os.getcwd(), 'images', "orange.ico")

display_surface = Screen()
display_surface.bgcolor('blue')
display_surface.title('Snake Game')
display_surface.setup(width=600, height=600)
display_surface.tracer(False)


root = display_surface._root
root.iconbitmap(icon_image_path)
root.resizable(False, False)


def make_turtle(object_shape="square", object_color="white"):
    turtle_object = Turtle()
    turtle_object.shape(object_shape)
    turtle_object.color(object_color)
    turtle_object.speed('fastest')
    turtle_object.penup()
    return turtle_object


def move_snake():
    if snake_head.direction == "up":
        yposition = snake_head.ycor()
        snake_head.sety(yposition + 20)

    if snake_head.direction == "down":
        yposition = snake_head.ycor()
        snake_head.sety(yposition - 20)

    if snake_head.direction == "left":
        xposition = snake_head.xcor()
        snake_head.setx(xposition - 20)

    if snake_head.direction == "right":
        xposition = snake_head.xcor()
        snake_head.setx(xposition + 20)


def change_food_position():
    xposition = randint(-270, 270)
    yposition = randint(-270, 270)
    food.goto(xposition, yposition)


def change_direction_to_up():
    if snake_head.direction != "down":
        snake_head.direction = "up"


def change_direction_to_left():
    if snake_head.direction != "right":
        snake_head.direction = "left"


def change_direction_to_down():
    if snake_head.direction != "up":
        snake_head.direction = "down"


def change_direction_to_right():
    if snake_head.direction != "left":
        snake_head.direction = "right"


def reset():
    global score
    score = 0
    snake_head.goto(0, 0)
    snake_head.direction = ""
    for body in snake_bodies:
        body.hideturtle()
    snake_bodies.clear()


snake_head = make_turtle("square", "black")
snake_head.direction = ""

food = make_turtle("circle", "red")
change_food_position()

score_board = make_turtle()
score_board.hideturtle()
score_board.goto(0, 260)


display_surface.listen()
display_surface.onkeypress(change_direction_to_up, "Up")
display_surface.onkeypress(change_direction_to_down, "Down")
display_surface.onkeypress(change_direction_to_left, "Left")
display_surface.onkeypress(change_direction_to_right, "Right")

snake_bodies = []
running = True
while running:
    score_board.clear()
    score_board.write(f"Score: {score}", align="center", font=("Terminal", 22))

    display_surface.update()

    if snake_head.distance(food) < 20:
        change_food_position()
        score += 1
        new_tail = make_turtle("square", "grey")
        snake_bodies.append(new_tail)

    for i in range(len(snake_bodies) - 1, 0, -1):
        prev_x = snake_bodies[i-1].xcor()
        prev_y = snake_bodies[i-1].ycor()
        snake_bodies[i].goto(prev_x, prev_y)

    if len(snake_bodies) > 0:
        head_x_position = snake_head.xcor()
        head_y_position = snake_head.ycor()
        snake_bodies[0].goto(head_x_position, head_y_position)

    if snake_head.xcor() > 290 or \
            snake_head.xcor() < -290 or\
            snake_head.ycor() > 290 or\
            snake_head.ycor() < -290:
        reset()

    move_snake()
    for body in snake_bodies:
        if body.distance(snake_head) < 20:
            reset()

    sleep(0.2)
