import turtle, math
from turtle import *

leo = turtle.Turtle()
leo.pencolor(1, 0, 0)
leo.hideturtle()
leo.speed(10)

leo_2 = leo.clone()
leo_2.pencolor(0, 0, 1)
leo_2.speed(10)

leo_3 = leo.clone()
leo_3.pencolor(0, 1, 1)
leo_3.speed(10)

leo_4 = leo.clone()
leo_4.pencolor(0.5, 0, 1)
leo_4.speed(10)

leo_5 = leo.clone()
leo_5.pencolor(1, 0.5, 0.2)
leo_5.speed(10)

leo_6 = leo.clone()
leo_6.pencolor(0.8, 0.5, 0.6)
leo_6.speed(10)

x_0 = -350
y_0 = 330

turtles = [leo, leo_2, leo_3, leo_4, leo_5, leo_6]

def run():
    for tu in turtles:
        tu.penup()
        tu.width(2)

    for c in range(0, y_0, 10):
        leo.goto(x_0, c)
        leo_2.goto(x_0 + 100, -c)
        leo_3.goto(x_0 + 200, c)
        leo_4.goto(x_0 + 300, -c)
        leo_5.goto(x_0 + 400, c)
        leo_6.goto(x_0 + 500, -c)
        # leo_4.goto(x_0 + 400, c)
        for t in turtles:
            t.pendown()
            t.setheading(0)
            t.forward(100)

turtle.listen()
turtle.onkey(run, 'r')
turtle.mainloop()
