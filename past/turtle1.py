import turtle

s = turtle.Screen()
s.bgcolor('pink')
# s.bgpic('iran.png')
# s.setup(width=.3, height=.3)

p = turtle.Pen()
p.pencolor('red')
p.pensize(4)
p.fillcolor('orange')
p.begin_fill()
p.forward(100)
p.left(120)
p.forward(100)
p.left(120)
p.forward(100)
p.left(120)
p.end_fill()

# second triangle

p.fillcolor('green')
p.begin_fill()
p.fd(100)
p.right(120)
p.fd(100)
p.right(120)
p.fd(100)
p.right(120)
p.end_fill()
s.exitonclick()
print("terminate")


# exercise 1 draw 2 squares with different colors
# exercise 1 draw 2 rectangles with different colors
