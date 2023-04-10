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

class Triangle:
    def __init__(self, x, y, width, height, color):
        self.turt = turtle.Turtle()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.hypotenuse = math.sqrt((width * width) + (height * height))

    def draw(self):
        self.turt.penup()
        self.turt.hideturtle()
        self.turt.color(self.color)
        self.turt.goto(self.x, self.y)
        self.turt.pendown()
        self.turt.begin_fill()
        self.turt.forward(self.width)
        self.turt.setheading(135)
        self.turt.forward(self.hypotenuse/2)
        self.turt.setheading(225)
        self.turt.forward(self.hypotenuse/2)
        self.turt.setheading(0)
        self.turt.forward(self.width)
        self.turt.end_fill()

def run():
    fuji = Triangle(-50, 0, 100, 100, blue)
    fuji.draw()

    peak = Triangle(-10, 35, 20, 20, white)
    peak.draw() 

    leo = turtle.Turtle()
    leo.hideturtle()
    leo.penup()
    leo.goto(0, -30)
    leo.write("富士山", True, align="center", font=('Arial', 20, 'normal'))

    img = ImageGrab.grab(bbox=bounds)
    img.save(this_dir + '/tartle19/tart.png', quality=95)
