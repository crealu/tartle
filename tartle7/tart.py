import os
import PIL
from PIL import ImageGrab
from PIL import Image
import turtle
import random

this_dir = os.getcwd()
bounds = (366, 140, 1060, 800)

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

def run():
	rhombi = []

	for r in range(10):
		x = random.randint(-300, 300)
		y = random.randint(-300, 300)
		rhombus = Rhombus(5, x, y)
		rhombus.setup()
		rhombi.append(rhombus)

	for r in rhombi:
		r.draw()

	img = ImageGrab.grab(bbox=bounds)
	img.save(this_dir + '/tartle7/tart.png', quality=95)



# .