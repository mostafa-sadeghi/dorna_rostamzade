# sample 1:

# import turtle

# # COLORS = ["red","green","blue"]*4
# COLORS = ["red","green","blue"]

# s = turtle.Screen()
# p = turtle.Pen()
# p.shape('turtle')


# for i in range(12):
#     p.pencolor(COLORS[i % 3])
#     for j in range(4):
#         p.fd(100)
#         p.lt(90)

#     p.lt(30)

# s.exitonclick()


# sample 2

import turtle

s = turtle.Screen()
s.setup(420, 320)
s.bgcolor('black')
p = turtle.Pen()
COLOR = ['red', 'green', 'blue', 'yellow', 'purple']
p.pensize(4)
p.penup()
p.setpos(-90, 0)
p.pendown()
for i in range(5):
    p.pencolor(COLOR[i])
    p.fd(200)
    p.rt(144)
p.penup()
p.setposition(80, -140)
p.pencolor('olive')
p.write('Our Nice Star', font=("Arial", 12, "bold"))
p.ht()
s.exitonclick()


# exercise  draw an animation clock
'''
Turtle
for
forward
right
setpos
goto
pendown
penup
write
circle
setheading  #  زاویه حرکت


'''
