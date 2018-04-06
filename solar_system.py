import random
import math

from kivy.app import App
from kivy.graphics import Ellipse
from kivy.graphics import Color
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.clock import Clock


class Planet(Ellipse):
    # AU is placeholder for distance from the sun
    def __init__(self, au=1, radius=20, speed = 1):
        self.au = au
        self.radius = radius
        self.orbit = generate_ellipse()
        self.speed = speed

    @staticmethod
    def generate_ellipse():
        x = random.randint(1,40)
        y = random.randint(1,40)
        a = random.randint(1,40)
        b = random.randint(1,40)
        for x < 40
            y = math.sqrt((((a^2)(b^2)) - ((b^2)(x^2)))/(a^2))
        x = math.sqrt((((a^2)(b^2)) - ((a^2)(y^2)))/(b^2))

    def build(self):


    def orbit(self):
