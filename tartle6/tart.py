import turtle
import math
import random
from turtle import *
from shapes import Circular

def run():
	circles = []

	for s in range(10):
	    y = random.randint(-200, 200)
	    circles.append(Circular(10, 2, -200 + s*20, 10))

    for angle in range(0, 30):
        for circle in circles:
            circle.draw(angle)
