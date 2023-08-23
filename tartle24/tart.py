import os
import turtle
import random
import math
import PIL
from PIL import ImageGrab
from PIL import Image

this_dir = os.getcwd()
bounds = (366, 140, 1060, 800)

reds = ['#ea0606', '#e24141', '#de6565', '#dc9393']
oranges = ['#ffc108', '#f7c450', '#fbd6a5', '#f7e3c8']
yellows = ['#ffe108', '#decf64' , '#fbf0a5', '#f7f1c8']

colors = [reds, oranges, yellows]

class Target:
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

	def draw(self):
		self.turt.pendown()
		self.turt.begin_fill()
		for i in range(0, 360, self.size):
			self.turt.setheading(i)
			self.turt.forward(10)
		self.turt.end_fill()


def run():
	x = -100
	y = 0
	size = 10
	for color in colors:
		for col in color:
			target = Target(x, y, size, col)
			target.setup()
			target.draw()
			size += 5
		size = 10
		x += 100


	img = ImageGrab.grab(bbox=bounds)
	img.save(this_dir + '/tartle24/tart.png', quality=95)


