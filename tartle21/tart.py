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

class Square:
    def __init__(self, turt, length, x, y):
        self.turt = turt
        self.length = length
        self.x0 = x
        self.y0 = y

    def setup(self):
        self.turt.penup()
        self.turt.hideturtle()
        self.turt.color('#ea0606')
        self.turt.goto(self.x0, self.y0)

    def draw(self):
        self.turt.pendown()
        self.turt.begin_fill()
        for i in range(0, 360, 90):
            self.turt.setheading(i)
            self.turt.forward(self.length)
        self.turt.end_fill()

class Plaid:
    def __init__(self, length):
        self.turt = turtle.Turtle()
        self.x = -300
        self.y = -300
        self.length = length

    def draw(self):
        self.turt.speed(10)
        step = self.length * 2
        base = True

        for x in range(-300, 300, self.length):
            for y in range(self.y, 300, step):
                square = Square(self.turt, self.length, x, y)
                square.setup()
                square.draw()
            if (base):
                self.y += self.length
            else:
                self.y = -300
            base = not base

def run():
    plaid = Plaid(50)
    plaid.draw()
    img = ImageGrab.grab(bbox=bounds)
    img.save(this_dir + '/tartle21/tart.png', quality=95)
