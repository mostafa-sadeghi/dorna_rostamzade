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
    snake_head.direction = "up"


def change_direction_to_left():
    snake_head.direction = "left"


def change_direction_to_down():
    snake_head.direction = "down"


def change_direction_to_right():
    snake_head.direction = "right"


snake_head = make_turtle("square", "black")
snake_head.direction = ""

food = make_turtle("circle", "red")
change_food_position()

score_turtle = make_turtle()
score_turtle.hideturtle()
score_turtle.goto(0, 260)
score_turtle.write(f"Score: {score}", align="center", font=("Arial", 28))


display_surface.listen()
display_surface.onkeypress(change_direction_to_up, "Up")
display_surface.onkeypress(change_direction_to_down, "Down")
display_surface.onkeypress(change_direction_to_left, "Left")
display_surface.onkeypress(change_direction_to_right, "Right")


running = True
while running:
    display_surface.update()

    if snake_head.distance(food) < 20:
        change_food_position()
        score += 1

    move_snake()
    sleep(0.2)
