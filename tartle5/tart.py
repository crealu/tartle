import turtle
import math
from turtle import *

class Spiral:
    def __init__(self, diameter, stroke_width):
        self.turt = turtle.Turtle()
        self.stroke_width = stroke_width
        self.amplitude = 1
        self.frequency = math.pi/10
        self.phase = diameter

    def setup(self):
        self.turt.hideturtle()
        self.turt.penup()
        self.turt.width(self.stroke_width)
        x0 = self._calc_x(0, self.amplitude)
        y0 = self._calc_y(0, self.amplitude)
        self.turt.goto(x0, y0)

    def draw(self, angle):
        x = self._calc_x(angle, self.amplitude)
        y = self._calc_y(angle, self.amplitude)
        self.amplitude += 1
        self.turt.pendown()
        self.turt.goto(x, y)

    def _calc_x(self, angle, amplitude):
        return self.amplitude * math.sin((angle * self.frequency) + self.phase)

    def _calc_y(self, angle, amplitude):
        return self.amplitude * math.cos((angle * self.frequency) + self.phase)

spiral = Spiral(10, 2)
spiral.setup()

spiral_a = Spiral(30, 1)
spiral_a.setup()

spirals = [spiral, spiral_a]

def draw_all():
		for angle in range(0, 90):
				spiral.draw(angle)
				spiral_a.draw(angle)
	#for spiral in spirals:
	#	spiral.draw()

turtle.listen()
turtle.onkey(draw_all, 'r')
turtle.mainloop()
