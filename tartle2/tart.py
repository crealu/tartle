import turtle, math
from turtle import *

don = turtle.Turtle()

x_0 = -300
y_0 = 300
width = 3

don.hideturtle()
don.speed(10)
don.pencolor(0.2, 0.8, 0.2)
don.width(width)
don.penup()
don.goto(x_0, 0)

leo = don.clone()
leo.goto(0, x_0)

mike = leo.clone()
mike.goto(-x_0, 0)

raph = mike.clone()
raph.goto(0, -x_0)
# f(x) = Asin(B(x-h))+k    amplitude A    frequency B    phase h

amplitude = 50
frequency = math.pi/50
phase = 2

turtles = [don, mike, leo, raph]
def run():
    crement = 1
    new_width = width
    for x in range(x_0, -1 * x_0):
        y =  amplitude * math.sin((x * frequency) + phase)
        don.goto(x, y)
        leo.goto(-y, x)
        mike.goto(x, -y)
        raph.goto(-y, -x)
        new_width += crement
        for t in turtles:
            t.pendown()
            t.width(new_width)
        if (new_width == 20):
            crement *= -1
        elif (new_width == 1):
            crement *= -1



turtle.listen()
turtle.onkey(run, 'r')
turtle.mainloop()
