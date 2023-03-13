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
	leo.width(2)

	radians = (random.randint(0, 10)/100.0) * math.pi * 2
	velocity = random.randint(1, 8)/100.0

	leo.hideturtle()
	leo.penup()
	for i in range(-300, 300, 10):
		radians += velocity		
		x = i + math.cos(radians) * 35
		y = (i/20) + math.sin(radians) * 55
		leo.setheading(i)
		leo.forward(60)
		leo.penup()
		leo.goto(x, y)
		leo.pendown()	

	leo.penup()
	x0 = (-300/20) + math.sin(radians) * 55
	y0 = -280 + math.cos(radians) * 35
	leo.goto(x0, y0)
	leo.pendown()

	for i in range(-280, 300, 10):
		radians += velocity		
		x = (i/20) + math.sin(radians) * 55
		y = i + math.cos(radians) * 35
		leo.setheading(i)
		leo.forward(60)
		leo.penup()
		leo.goto(x, y)
		leo.pendown()


	img = ImageGrab.grab(bbox=bounds)
	img.save(this_dir + '/tartle14/tart.png', quality=95)

