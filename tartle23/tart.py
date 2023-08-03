import os
import turtle
import random
import math
import PIL
from PIL import ImageGrab
from PIL import Image

this_dir = os.getcwd()
bounds = (366, 140, 1060, 800)

purple = '#db09dc'
reds = ['#ea0606', '#e24141', '#de6565', '#dc9393']

class MillerFestLogo:
    def __init__(self, x, y, scale, color):
        self.turt = turtle.Turtle()
        self.length = 10
        self.x0 = x
        self.y0 = y
        self.scale = scale
        self.color = color
        self.f_lines = [
    		[270, 100],	[0, 50],   [90, 60],
    		[0, 40],	[90, 40],  [180, 40],
    		[90, 25], 	[0, 60],   [90, 60]
        ]

        self.m_lines = [
        	10, 100, 10, -5, 60, 10, 10, 55, 120
        ]

        self.curves = [10, 4, 4, 5, 5]

    def setup(self):
        self.turt.penup()
        self.turt.hideturtle()
        self.turt.color(self.color)
        self.turt.goto(self.x0, self.y0)
        for line in self.f_lines:
        	line[1] *= self.scale

        for line in self.m_lines:
        	line *= self.scale
        	print(line)

    def draw(self):
        self.turt.pendown()
        self.turt.begin_fill()

        # line 1
        self.turt.setheading(180)
        for i in range(180, 450, self.m_lines[0]):
            self.turt.setheading(i)
            self.turt.forward(self.curves[0])

        # line 2
        self.turt.setheading(90)
        self.turt.forward(self.m_lines[1])

        # line 3
        self.turt.setheading(300)
        for j in range(270, 450, self.m_lines[2]):
            self.turt.setheading(j)
            self.turt.forward(self.curves[1])

        # start F
        self.draw_F()

        # M
        self.turt.setheading(270)
        for z in range(240, 180, self.m_lines[3]):
            self.turt.setheading(z)
            self.turt.forward(self.curves[2])

        self.turt.setheading(180)
        self.turt.forward(self.m_lines[4])

        self.turt.setheading(180)
        for u in range(180, 270, self.m_lines[5]):
            self.turt.setheading(u)
            self.turt.forward(self.curves[3])

        self.turt.setheading(90)
        for d in range(90, 180, self.m_lines[6]):
            self.turt.setheading(d)
            self.turt.forward(self.curves[4])

        self.turt.setheading(180)
        self.turt.forward(self.m_lines[7])

        self.turt.setheading(270)
        self.turt.forward(self.m_lines[8])

        self.turt.end_fill()

    def draw_F(self):
    	for line in self.f_lines:
    		self.turt.setheading(line[0])
    		self.turt.forward(line[1])

def run():
    x = -100
    y = 100
    for red in reds:
        mf_logo = MillerFestLogo(x, y, 1, red)
        mf_logo.setup()
        mf_logo.draw()
        x += 50
        y -= 50

    img = ImageGrab.grab(bbox=bounds)
    img.save(this_dir + '/tartle23/tart.png', quality=95)











