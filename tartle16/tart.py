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

color1 = input("Color 1 RGB: ").replace(' ', '').split(',')
color2 = input("Color 2 RGB: ").replace(' ', '').split(',')

# Color 1 RGB: 123, 10, 100
# Color 2 RGB: 123, 3, 19

class ColorGradient:
    def __init__(self, rgbC1, rgbC2):
        self.gradient = [
            [int(rgbC1[0]), int(rgbC2[0])],
            [int(rgbC1[1]), int(rgbC2[0])],
            [int(rgbC1[2]), int(rgbC2[0])]
        ]

#g = [29, 228, 26]
b = [29, 150, 255]
p = [133, 49, 243]
w = [250, 250, 250]

gg = ColorGradient(color1, color2).gradient
bg = ColorGradient(b, w).gradient
pg = ColorGradient(p, w).gradient

class SpiralGradient:
    def __init__(self, ca, dec, path):
        self.kame = turtle.Turtle(),
        self.kameSpeed = 0,
        self.circles = 10,
        self.colorArray = ca,
        self.path = path,
        self.decrementer = dec

    def manageColor(self):
        colorChangeArray = []
        for cv in self.colorArray[0]:
            difference = abs(cv[1] - cv[0])
            colorChangeArray.append(difference)

        grad = int(360 / self.circles[0])

        r = self.colorArray[0][0][0]
        g = self.colorArray[0][1][0]
        b = self.colorArray[0][2][0]

        rgbBase = [r, g, b]

        self.kame[0].pencolor(r, g, b)

        rInc = int(colorChangeArray[0] / grad)
        gInc = int(colorChangeArray[1] / grad)
        bInc = int(colorChangeArray[2] / grad)

        rgbIncArray = [rInc, gInc, bInc]

        return([rgbBase, rgbIncArray])

    def draw(self):
        incValue = self.manageColor()

        r = incValue[0][0]
        g = incValue[0][1]
        b = incValue[0][2]

        for i in range(0, 720):
            if i % self.circles[0] is 0:
                self.kame[0].width(abs(int(i/9) - 1))
                self.kame[0].setheading(i + self.path[0])
                self.kame[0].forward(i/self.decrementer)
                r -= incValue[1][0]
                g += incValue[1][1]
                b += incValue[1][2]

                self.kame[0].pencolor(r, g, b)


s1 = SpiralGradient(gg, 10, 65)

def run():
    s1.draw()
    img = ImageGrab.grab(bbox=bounds)
    img.save(this_dir + '/tartle16/tart.png', quality=95)
