# draw star with turtle

import turtle
s = turtle.Screen()
p = turtle.Pen()
p.pencolor('red')
p.pensize(4)
p.shape('turtle')
p.penup()
p.setpos(-90, 0)
p.pendown()
p.fd(150)
p.rt(144)
p.fd(150)
p.rt(144)
p.fd(150)
p.rt(144)
p.fd(150)
p.rt(144)
p.fd(150)
p.rt(144)
p.penup()
p.goto(-150, 200)
p.write("Our Nice Star pic with turtle", font=20)
p.ht()
s.exitonclick()