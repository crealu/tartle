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
details = [
    {
        "rotation": 0,
        "color": reds
    },
    {
        "rotation": 60,
        "color": oranges
    },
    {
        "rotation": 120,
        "color": yellows
    },
    {
        "rotation": 180,
        "color": greens
    },
    {
        "rotation": 240,
        "color": blues
    },
    {
        "rotation": 300,
        "color": purples
    }
]

class WaveSpiral:
    def __init__(self, colors, rotation):
        self.turt = turtle.Turtle()
        self.colors = colors
        self.rotation = rotation

    def setup(self):
        self.turt.hideturtle()

    def draw(self, width, r, i):
        self.turt.color(self.colors[r])
        self.turt.width(width)
        self.turt.setheading(i + self.rotation)
        self.turt.forward(15)

def run():
    spirals = []

    for detail in details:
        spiral = WaveSpiral(detail["color"], detail["rotation"])
        spiral.setup()
        spirals.append(spiral)

    for i in range(0, 135):
        r = random.randint(0, 3)
        for spiral in spirals:
            if i % 5 == 0:
                width = 5 + int(i / 9)
                spiral.draw(width, r, i)

    img = ImageGrab.grab(bbox=bounds)
    img.save(this_dir + '/tartle17/tart.png', quality=95)
