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
	def __init__(self, x0, y0):
		self.turt = turtle.Turtle()
		self.x = x0
		self.y = y0
		self.radius = 20
		self.new_heading = 90 + x0
		self.amp = 10
		self.freq = 10
		self.phase = 8

	def setup(self):
		self.turt.penup()
		self.turt.hideturtle()
		self.turt.width = 10
		x_0 = self._calc_x(self.x)
		y_0 = self._calc_y(self.y)
		self.turt.goto(x_0, y_0)
		self.turt.pendown()

	def _calc_x(self, angle):
		return self.amp * math.cos((angle/10 * self.freq) + self.phase)


	def _calc_y(self, angle):
		return self.amp * math.sin((angle/10 * self.freq) + self.phase)

	def draw(self):
		for t in range(90, -90, -1):
			self.new_heading = t + self.x
			self.turt.setheading(self.new_heading)
			self.turt.forward(1)

def run():
	for a in range(0, 360, 10):
		arc2 = Arc(a, a*10)
		arc2.setup()
		arc2.draw()

	img = ImageGrab.grab(bbox=bounds)
	img.save(this_dir + '/tartle11/tart.png', quality=95)

