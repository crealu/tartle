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

class ConcentricCircles:
    def __init__(self, quantity, colors, x_0, y_0):
        self.turt = turtle.Turtle()
        self.frequency = math.pi/10
        self.phase = 2
        self.quantity = quantity
        self.colors = colors
        self.x = x_0
        self.y = y_0

    def setup(self):
        self.turt.hideturtle()
        self.turt.penup()
        self.turt.width(3)
        x = self._calc_x(0, 10)
        y = self._calc_y(0, 10)
        self.turt.goto(x, y)

    def draw(self):
        for c in range(1, self.quantity):
            diameter = c * 20
            self.turt.color(self.colors[c-1])
            for angle in range(30):
                x = self._calc_x(angle, diameter)
                y = self._calc_y(angle, diameter)
                self.turt.goto(x, y)
                self.turt.pendown()

            self.reset(diameter)

    def reset(self, diameter):
        self.turt.penup()
        x = self._calc_x(0, diameter)
        y = self._calc_y(0, diameter)
        self.turt.goto(x, y)
            
    def _calc_x(self, angle, amplitude):
        return amplitude * math.sin((angle * self.frequency) + self.phase) + self.x

    def _calc_y(self, angle, amplitude):
        return amplitude * math.cos((angle * self.frequency) + self.phase) + self.y


def run():
    for deats in details:
        circles = ConcentricCircles(5, deats['color'], deats['rotation'] - 150, deats['rotation'] - 150)
        circles.setup()
        circles.draw()

    img = ImageGrab.grab(bbox=bounds)
    img.save(this_dir + '/tartle18/tart.png', quality=95)
