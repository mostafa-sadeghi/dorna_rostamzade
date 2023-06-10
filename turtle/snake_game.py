# pip install pyinstaller

from turtle import Screen, Turtle
import sys
import os

if getattr(sys, 'frozen', False):
    wd = sys._MEIPASS
else:
    wd = ''   

icon_image_path = os.path.join(os.getcwd(),'images',"orange.ico")

display_surface = Screen()
display_surface.bgcolor('blue')
display_surface.title('Snake Game')
display_surface.setup(width=600, height=600)

root = display_surface._root
root.iconbitmap(icon_image_path)
root.resizable(False, False)


def make_turtle(object_shape, object_color):
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
    # سایر جهت ها 
    if snake_head.direction == "down":
        pass
    if snake_head.direction == "left":
        pass
    if snake_head.direction == "right":
        pass

snake_head = make_turtle("square", "black")
snake_head.goto(100, 100)
snake_head.direction = "up"

food = make_turtle("circle", "red")
# exercise : جای غذا تصادفی باشد





running = True
while running:
    display_surface.update()
    move_snake()