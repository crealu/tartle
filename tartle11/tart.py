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
	def __init__(self, angle):
		self.turt = turtle.Turtle()
		self.x = angle
		self.y = 10
		self.radius = 20
		self.new_heading = 90 + angle
		self.amp = 40
		self.freq = math.pi/10
		self.phase = 3

	def setup(self):
		self.turt.penup()
		self.turt.hideturtle()
		self.turt.width(3)
		x_0 = self.x * self._calc_x(self.x)
		y_0 = self._calc_y(self.x)
		print(x_0, y_0)
		self.turt.goto(x_0, y_0)
		self.turt.pendown()

	def _calc_x(self, angle):
		return self.amp * math.cos((angle * self.freq) + self.phase)

	def _calc_y(self, angle):
		return self.amp * math.sin((angle * self.freq) + self.phase)

	def draw(self):
		self.turt.setheading(self.new_heading)
		self.turt.forward(10)

		# for t in range(self.new_heading, -1 * self.new_heading, -1):
		# 	self.new_heading += t
		# 	self.turt.setheading(self.new_heading)
		# 	self.turt.forward(10)

def run():
	for a in range(0, 360, 10):
		arc2 = Arc(a)
		arc2.setup()
		arc2.draw()

	img = ImageGrab.grab(bbox=bounds)
	img.save(this_dir + '/tartle11/tart.png', quality=95)

