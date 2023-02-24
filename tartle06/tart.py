import os
import PIL
from PIL import ImageGrab
from PIL import Image
import turtle
import random
import math
from shapes import Circular

this_dir = os.getcwd()
bounds = (366, 140, 1060, 800)

def run():
	circles = []

	for s in range(10):
		y = random.randint(-200, 200)
		circles.append(Circular(10, 2, -200 + s*20, 10))

	for angle in range(0, 30):
		for circle in circles:
			circle.draw(angle)

	img = ImageGrab.grab(bbox=bounds)
	img.save(this_dir + '/tartle06/tart.png', quality=95)
