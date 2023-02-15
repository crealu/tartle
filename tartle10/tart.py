import os
import turtle
import random
import math
import PIL
from PIL import ImageGrab
from PIL import Image
from shapes import Rhombus

this_dir = os.getcwd()
bounds = (366, 140, 1060, 800)

class EyeKanji:
	def __init__(self, x0, y0):
		self.turt = turtle.Turtle()
		self.x = x0
		self.y = y0

	def setup(self):
		self.turt.hideturtle()
		self.turt.penup()
		self.turt.width(5)
		self.turt.goto(self.x, self.y)

	def draw(self):
		self.turt.pendown()
		self.turt.setheading(270)
		self.turt.forward(45)
		self.turt.penup()
		self.turt.goto(self.x, self.y)
		self.turt.setheading(0)
		self.turt.pendown()
		self.turt.forward(30)
		self.turt.setheading(270)
		self.turt.forward(45)
		self.turt.penup()
		self.turt.goto(self.x, self.y - 14)
		self.turt.setheading(0)
		self.turt.pendown()
		self.turt.forward(30)
		self.turt.penup()
		self.turt.goto(self.x, self.y - 28)
		self.turt.setheading(0)
		self.turt.pendown()
		self.turt.forward(30)
		self.turt.penup()
		self.turt.goto(self.x, self.y - 42)
		self.turt.setheading(0)
		self.turt.pendown()
		self.turt.forward(30)

def run():
	eye = EyeKanji(0, 0)
	eye.setup()
	eye.draw()
	img = ImageGrab.grab(bbox=bounds)
	img.save(this_dir + '/tartle10/tart.png', quality=95)
	readme = open('README.md', 'a')
	readme.write('\n')
	readme.write('![alt text](./tartle10/tart.png)')
	readme.write('tartle 10')
	readme.write('&nbsp;')

