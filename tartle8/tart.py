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

class FilledRhombus(Rhombus):
	def draw(self, red):
		super().draw()
		self.turt.penup()
		self.turt.pencolor(red, 0.0, 1.0 - red)
		self.turt.width(20)
		self.turt.goto(self.x, self.y + 30)
		self.turt.pendown()
		self.turt.goto(self.x, self.y + 30)

def run():
	rhombi = []
	amplitude = 20
	frequency = math.pi/10
	phase = 20

	for r in range(-180, 180):
		if r % 10 == 0:
			x = r
			y = amplitude * math.sin((r/10 * frequency) + phase)
			if r != 0:
				w = abs(180/r)
			else:
				w = 7
			if w > 6.0:
				w = 7
			print(w)
			rhombus = FilledRhombus(w, x, y)
			rhombus.setup()
			rhombi.append(rhombus)

	for r in rhombi:
		red = abs(r.x/180)
		r.draw(red)

	img = ImageGrab.grab(bbox=bounds)
	img.save(this_dir + '/tartle8/tart.png', quality=95)



