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
				self.turt.pencolor(abs(0.33 - red)/1.0, red, 1.0 - red)
				self.turt.width(15)
				self.turt.goto(self.x, self.y + 20)
				self.turt.pendown()
				self.turt.goto(self.x, self.y + 20)

def run():
		rhombi = []
		amplitude = 70
		frequency = math.pi/10
		phase = 20

		for r in range(270, -270, -1):
				if r % 10 == 0:
						x = amplitude * math.cos((r/10 * frequency) + phase)
						y = r
						w = 0.1
						rhombus = FilledRhombus(w, x, y)
						rhombus.setup()
						rhombi.append(rhombus)

		for r in rhombi:
				red = abs(r.y/270)
				r.draw(red)

		img = ImageGrab.grab(bbox=bounds)
		img.save(this_dir + '/tartle9/tart.png', quality=95)

	# readme = open('README.md', 'a')
	# readme.write('\n')
	# readme.write('![alt text](./tartle9/tart.png')
	# readme.write('tartle 9')
	# readme.write('&nbsp;')
