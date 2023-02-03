import turtle
import math
import random
from turtle import *

class Circular:
    def __init__(self, diameter, stroke_width, x0, y0):
        self.turt = turtle.Turtle()
        self.stroke_width = stroke_width
        self.amplitude = 1
        self.frequency = math.pi/10
        self.phase = diameter
        self.x = x0
        self.y = y0
        self.setup()

    def setup(self):
        self.turt.hideturtle()
        self.turt.penup()
        self.turt.width(self.stroke_width)
        self.turt.goto(self.x, self.y)

    def draw(self, angle):
        x = self._calc_x(angle, self.amplitude)
        y = self._calc_y(angle, self.amplitude)
        self.turt.pendown()
        self.turt.goto(x, y)

    def _calc_x(self, angle, amplitude):
        return self.amplitude * math.sin((angle * self.frequency) + self.phase) + self.x

    def _calc_y(self, angle, amplitude):
        return self.amplitude * math.cos((angle * self.frequency) + self.phase) + self.y

class Spiral(Circular):
    def draw(self, angle):
        x = self._calc_x(angle, self.amplitude)
        y = self._calc_y(angle, self.amplitude)
        self.amplitude += 1
        self.turt.goto(x, y)
        self.turt.pendown()

spirals = []

for s in range(10):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    spirals.append(Spiral(10, 2, x, y))

def draw_all():
    for angle in range(0, 45):
        for spiral in spirals:
            spiral.draw(angle)

turtle.listen()
turtle.onkey(draw_all, 'r')
turtle.mainloop()
