import os
import PIL
from PIL import ImageGrab
from PIL import Image
import turtle
import random
import math

this_dir = os.getcwd()
bounds = (366, 140, 1060, 800)

class Arc:
	def __init__(self, x0, y0, amplitude, frequency, phase):
		self.turt = turtle.Turtle()
		self.x = x0
		self.y = y0
		self.length = 20
		self.amp = amplitude
		self.freq = frequency
		self.phase = phase

	def setup(self):
		self.turt.penup()
		self.turt.width = 4
		x_0 = self._calc_x(self.x)
		y_0 = self._calc_y(self.x)
		self.turt.goto(x_0, y_0)

	def _calc_x(self, t):
		return t

	def _calc_y(self, t):
		return math.pow(t, 2) - (2 * t)

	def draw(self):
		for t in range(self.x, self.x*(-1)):
			x = self._calc_x(t)
			y = self._calc_y(t)
			self.turt.goto(x, y)

class Arc2:
	def __init__(self, x0, y0):
		self.turt = turtle.Turtle()
		self.x = x0
		self.y = self._calc_y(y0)
		self.radius = 20
		self.new_heading = 90

	def setup(self):
		self.turt.penup()
		self.turt.width = 4
		x_0 = self._calc_x(self.x)
		y_0 = self._calc_y(self.x)
		self.turt.goto(x_0, y_0)
		self.turt.pendown()

	def _calc_x(self, t):
		return t

	def _calc_y(self, t):
		return 90 - t

	def draw(self):
		for t in range(90):
			x = t
			y = self._calc_y(t)
			self.new_heading = t
			self.turt.setheading(self.new_heading)
			self.turt.forward(1)

def run():
	# arc1 = Arc(-20, 0, 10, 20, 5)
	# arc1.setup()
	# arc1.draw()	

	arc2 = Arc2(90, 0)
	arc2.setup()
	arc2.draw()

