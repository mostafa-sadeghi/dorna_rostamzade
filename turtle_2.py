import turtle
import time
s = turtle.Screen()
# s.register_shape("my_shape", ((5, 0), (5, 5), (0, 5), (0, 0)))
s.register_shape("strawberry.gif")
p = turtle.Pen()
# p.speed('fastest')
# p.speed('fast')
# p.speed('normal')
# p.speed('slow')
# p.speed('slowest')
# 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
# p.shape('my_shape')
# p.shape('strawberry.gif')
# p.shapesize(3)
# p.ht()

# p.fd(120)
# p.lt(90)

# time.sleep(1)

# p.fd(120)
# p.lt(90)
# time.sleep(1)

# p.fd(120)
# p.lt(90)
# time.sleep(1)

# p.fd(120)
# p.lt(90)


# draw a circle
# p.penup()
# p.goto(20, -50)
# p.setpos(20,-50)
# p.setposition(20,-50)
# p.pendown()
# p.circle(50)
p.pensize(4)
p.setheading(45)
p.fd(100)
p.pencolor('gray')
p.seth(180)
p.forward(100)
# p.seth(270)
p.pencolor('brown')
# p.fd(100)
p.goto(0, 0)
# p.home()

s.exitonclick()

# exercise draw a pentagon
