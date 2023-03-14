import os
import turtle
import random
import math
import PIL
from PIL import ImageGrab
from PIL import Image

this_dir = os.getcwd()
bounds = (366, 140, 1060, 800)

def run():
	leo = turtle.Turtle()
	leo.width(5)
	leo.speed(10)

	radians = (random.randint(0, 10)/100.0) * math.pi * 4
	velocity = random.randint(1, 8)/100.0

	leo.hideturtle()
	leo.penup()
	x0 = math.cos(radians) * 150
	y0 = math.sin(radians) * 150
	leo.goto(x0, y0)

	for r in range(0, 1080, 10):
		rm = random.randint(10, 20)
		radians += velocity
		x = math.cos(radians) * 150
		y = math.sin(radians) * 150
		leo.setheading(radians)
		leo.forward(10)
		leo.pendown()
		leo.goto(x, y)
		leo.penup()

	img = ImageGrab.grab(bbox=bounds)
	img.save(this_dir + '/tartle15/tart.png', quality=95)

