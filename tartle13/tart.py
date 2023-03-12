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

def grid(d):
	for y in range(-100, 0, 10):
		d.goto(-200, y)
		d.pendown()
		d.setheading(0)
		d.forward(100)
		d.penup()

	for x in range(-200, -100, 10):
		d.goto(x, 0)
		d.pendown()
		d.setheading(270)
		d.forward(100)
		d.penup()


def run():
	don = turtle.Turtle()
	don.hideturtle()
	don.speed(10)
	don.penup()
	don.goto(-200, -100)
	don.pendown()

	for h in range(0, 360, 90):
		don.setheading(h)
		don.forward(100)

	don.penup()
	don.goto(-100, -100)
	don.pendown()
	don.goto(100, 100)
	don.goto(100, 120)
	don.goto(80, 120)

	don.penup()
	don.goto(-100, 0)
	don.pendown()
	don.goto(100, 120)

	don.penup()
	don.goto(-200, 0)
	don.pendown()
	don.goto(80, 120)
	don.penup()

	grid(don)

	img = ImageGrab.grab(bbox=bounds)
	img.save(this_dir + '/tartle13/tart.png', quality=95)

