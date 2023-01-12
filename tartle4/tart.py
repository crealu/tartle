import turtle
import math
from turtle import *

don = turtle.Turtle()

don.speed(10)
don.pencolor(0.0, 0.0, 0.7)
don.width(6)
don.penup()
don.hideturtle()

mike = don.clone()
mike_offset = 10

raph = mike.clone()
raph_offset = 20

amplitude = 50
frequency = math.pi/50
phase = 2

x_0 = -amplitude * math.sin((0 * frequency) + phase)
y_0 =  amplitude * math.cos((0 * frequency) + phase)

mike_x = x_0 + mike_offset
mike_y = y_0 + mike_offset
raph_x = x_0 + raph_offset
raph_y = y_0 + raph_offset

don.goto(x_0, y_0)
don.pendown()

mike.goto(mike_x, mike_y)
mike.pencolor(1.0, 0.4, 0.2)
mike.pendown()

raph.penup()
raph.goto(raph_x +10, raph_y + 10)
raph.pencolor(0.4, 0.8, 0.2)
raph.pendown()

def run():
    amp = amplitude
    for t in range(0, 1080):
        x = -amp * math.sin((t * frequency) + phase)
        y = amp * math.cos((t * frequency) + phase)
        amp += 0.5
        don.goto(x, y)
        mike.goto(x+mike_offset, y+mike_offset)
        raph.goto(-x+raph_offset+10, y+raph_offset+10)
    print('done')

turtle.listen()
turtle.onkey(run, 'r')
turtle.mainloop()
