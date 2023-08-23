import os
import turtle
import random
import math
import PIL
from PIL import ImageGrab
from PIL import Image

this_dir = os.getcwd()
bounds = (366, 140, 1060, 800)

yellows = ['#ffe108', '#f7e250' , '#fbf0a5', '#f7f1c8']
blues = ['#0953dc', '#1e60da', '#3d74da', '#6c91d6', '#0953dc']

class Scale:
	def __init__(self, x, y, size, color):
		self.turt = turtle.Turtle()
		self.x = x
		self.y = y
		self.size = size
		self.color = color

	def setup(self):
		self.turt.penup()
		self.turt.speed(10)
		self.turt.hideturtle()
		self.turt.color(self.color)
		self.turt.goto(self.x, self.y)
		self.turt.width(3)

	def draw(self):
		deg1 = 90
		deg2 = 270
		fwd = 10
		start = 8
		arc = 5

		for i in range(0, 4):
			self.turt.pendown()
			for i in range(deg1, deg2, arc):
				self.turt.setheading(i)
				self.turt.forward(fwd)
			self.turt.penup()
			self.turt.goto(self.turt.pos()[0] / start, self.y)		
			fwd -= 2.5
			start /= 2

class Scale2:
	def __init__(self, x, y, size, color):
		self.turt = turtle.Turtle()
		self.x = x
		self.y = y
		self.size = size
		self.color = color

	def setup(self):
		self.turt.penup()
		self.turt.hideturtle()
		self.turt.color(self.color)
		self.turt.goto(self.x, self.y)
		self.turt.width(3)

	def draw(self):
		self.turt.fillcolor(yellows[2])
		fwd = 10
		start = 8
		arc = 5
		y = 0
		for g in range(0, 3):
			self.turt.pendown()
			self.turt.begin_fill()
			for i in range(0, 360, 10):
				self.turt.setheading(i)
				self.turt.forward(fwd)
			self.turt.penup()
			self.turt.end_fill()

			fwd -= 2.5
			y += 15
			self.turt.goto(self.x, self.y + y)


def run():
	ys = [150, 75, 0, -75, -150]
	xs = [-150, -75, 0, 75, 150]
	i = 0
	for y in ys:			
		for x in xs:
			new_x = x
			if (i == 1 or i == 3):
				new_x += 50
			scale = Scale2(new_x, y, 10, blues[i])
			scale.setup()
			scale.draw()
		i += 1

	img = ImageGrab.grab(bbox=bounds)
	img.save(this_dir + '/tartle25/tart.png', quality=95)

