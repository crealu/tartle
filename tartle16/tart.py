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
blues = ['#0953dc', '#1e60da', '#3d74da', '#6c91d6']
yellows = ['#ffe108', '#f7e250' , '#fbf0a5', '#f7f1c8']
greens = ['#06f339', '#64ec81', '#a0e8b0', '#cbe8d2']
details = [
    {
        "rotation": 0,
        "color": reds
    },    
    {
        "rotation": 90,
        "color": yellows
    },    
    {
        "rotation": 180,
        "color": greens
    },    
    {
        "rotation": 270,
        "color": blues
    }
]

class StripedSpiral:
    def __init__(self, colors, rotation):
        self.turt = turtle.Turtle()
        self.colors = colors
        self.rotation = rotation

    def draw(self):
        t = self.turt
        t.hideturtle()
        for i in range(0, 360):
            if i % 10 == 0:
                t.color(random.choice(self.colors))
                t.width(40 - int(i/9))
                t.setheading(i + self.rotation)
                t.forward(15)

def run():
    for detail in details:
        spiral = StripedSpiral(detail["color"], detail["rotation"])
        spiral.draw()

    img = ImageGrab.grab(bbox=bounds)
    img.save(this_dir + '/tartle16/tart.png', quality=95)
