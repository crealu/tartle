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

def run():
	def trail(t):
		for i in range(0, 6):
			random_heading = random.randint(-90, 90)
			t.setheading(random_heading)
			t.forward(10)

	turtles = []
	for m in range(0, 20):
		t = turtle.Turtle()
		turtles.append(t)

	for n in range (0, 20):
		turtles[n].hideturtle()
		turtles[n].goto(-300, (n*32) - 300)
		turtles[n].pendown()
		turtles[n].width(5)
		turtles[n].setheading(0)
		turtles[n].forward(300)

		trail(turtles[n])

	for o in range(0, 20):
		turtles[o].width(10)
		turtles[o].goto(360, (o*32) - 310)
		turtles[o].setheading(0)
		turtles[o].forward(140)

	img = ImageGrab.grab(bbox=bounds)
	img.save(this_dir + '/tartle12/tart.png', quality=95)