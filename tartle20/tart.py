import os
import turtle
import random
import math
import PIL
from PIL import ImageGrab
from PIL import Image

this_dir = os.getcwd()
bounds = (366, 140, 1060, 800)

c1 = []
c2 = []
colors = 0

reds = ['#ea0606', '#e24141', '#de6565', '#dc9393']
oranges = ['#ffc108', '#f7c450', '#fbd6a5', '#f7e3c8']
yellows = ['#ffe108', '#f7e250' , '#fbf0a5', '#f7f1c8']
greens = ['#06f339', '#64ec81', '#a0e8b0', '#cbe8d2']
blues = ['#0953dc', '#1e60da', '#3d74da', '#6c91d6']
purples = ['#db09dc', '#d51eda', '#a53dda', '#bb80ce']

yellows = ['#ffe108', '#f7e250' , '#fbf0a5', '#f7f1c8']
blue = '#0953dc'
purple = '#db09dc'
white = '#FFFFFF'

amplitude = 100
frequency = math.pi/10
phase = 2

class Poster:
    def __init__(self):
        self.turt = turtle.Turtle()

    def draw(self):
        self.turt.hideturtle()
        self.turt.penup()
        for y in range(-300, 300, 100):
            x = -200
            self.turt.goto(x, y)
            r = abs(y / 300)
            g = abs(y / 300)
            # r = random.randint(0, 100) / 00
            self.turt.color(r, 1.0, 1.0)
            self.write_date(abs(int(30 - (y / 10))))
            self.turt.goto(x, -y)
            self.turt.color(1.0, g, 1.0)
            self.write_place(abs(int(30 - (y / 10))))

    def write_date(self, size):
        self.turt.write(
            "May 5",
            True,
            align="center",
            font=('Arial', size, 'normal')
        )    

    def write_place(self, size):
        self.turt.write(
            "@ The Gutter",
            True,
            align="center",
            font=('Arial', size, 'normal')
        )

def run():
    poster = Poster()
    poster.draw()
    img = ImageGrab.grab(bbox=bounds)
    img.save(this_dir + '/tartle20/tart.png', quality=95)
