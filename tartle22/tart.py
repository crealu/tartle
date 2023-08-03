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

# amplitude = 100
# frequency = math.pi/10
# phase = 2

class MillerFestLogo:
    def __init__(self, x, y):
        self.turt = turtle.Turtle()
        self.length = 10
        self.x0 = x
        self.y0 = y

    def setup(self):
        self.turt.penup()
        self.turt.hideturtle()
        self.turt.color(blue)
        self.turt.goto(self.x0, self.y0)

    def draw(self):
        self.turt.pendown()
        self.turt.begin_fill()

        # line 1
        self.turt.setheading(180)
        for i in range(180, 450, self.line_lengths[0]):
            self.turt.setheading(i)
            self.turt.forward(self.length)

        # line 2
        self.turt.setheading(90)
        self.turt.forward(self.line_lengths[1])

        # line 3
        self.turt.setheading(300)
        for j in range(270, 450, self.line_lengths):
            self.turt.setheading(j)
            self.turt.forward(4)

        # line 4 (start F)
        self.turt.setheading(270)
        self.turt.forward(100)

        self.turt.setheading(0)
        self.turt.forward(50)

        self.turt.setheading(90)
        self.turt.forward(80)

        self.turt.setheading(0)
        self.turt.forward(40)

        self.turt.setheading(90)
        self.turt.forward(40)

        self.turt.setheading(180)
        self.turt.forward(40)

        self.turt.setheading(90)
        self.turt.forward(30)

        self.turt.setheading(0)
        self.turt.forward(60)

        self.turt.setheading(90)
        self.turt.forward(60)

        # M
        self.turt.setheading(270)

        for z in range(240, 180, -5):
            self.turt.setheading(z)
            self.turt.forward(4)

        self.turt.setheading(180)
        self.turt.forward(60)

        self.turt.setheading(180)
        for u in range(180, 270, 10):
            self.turt.setheading(u)
            self.turt.forward(5)

        self.turt.setheading(90)
        for d in range(90, 180, 10):
            self.turt.setheading(d)
            self.turt.forward(5)

        self.turt.setheading(180)
        self.turt.forward(50)

        self.turt.setheading(270)
        self.turt.forward(120)

        self.turt.end_fill()

def run():
    mf_logo = MillerFestLogo(-100, 0)
    mf_logo.setup()
    mf_logo.draw()
    img = ImageGrab.grab(bbox=bounds)
    img.save(this_dir + '/tartle22/tart.png', quality=95)
