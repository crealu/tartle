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
	def __init__(self, x0, step):
		self.turt = turtle.Turtle()
		self.x = x0
		self.y = 0
		self.amp = 40
		self.freq = math.pi/10
		self.phase = 3
		self.step = step

	def setup(self):
		self.turt.penup()
		self.turt.hideturtle()
		self.turt.width(3)
		self.turt.goto(self.x, self.y)
		self.turt.pendown()

	def _calc_x(self, angle):
		return self.amp * math.cos((angle * self.freq) + self.phase)

	def _calc_y(self, angle):
		return self.amp * math.sin((angle * self.freq) + self.phase)

	def draw(self):
		for t in range(90, -90, -1):
			self.turt.setheading(t)
			self.turt.forward(self.step)

def run():
	points = [-3, -2, -1]
	for p in points:
		arc = Arc(p * 100, abs(p));
		arc.setup();
		arc.draw();

	img = ImageGrab.grab(bbox=bounds)
	img.save(this_dir + '/tartle11/tart.png', quality=95)

