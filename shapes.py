import turtle
import math
import random

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

class Rhombus:
    def __init__(self, stroke_width, x0, y0):
        self.turt = turtle.Turtle()
        self.stroke_width = stroke_width
        self.side_length = 40
        self.angles = [45, 135, 225, 315]
        self.x = x0
        self.y = y0

    def setup(self):
        self.turt.hideturtle()
        self.turt.penup()
        self.turt.width(self.stroke_width)
        self.turt.goto(self.x, self.y)
        self.turt.setheading(self.angles[0])

    def draw(self):
        self.turt.pendown()
        for angle in self.angles:
            self.turt.setheading(angle)
            self.turt.forward(self.side_length)
