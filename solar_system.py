import random
import math

from kivy.app import App
from kivy.graphics import Ellipse
from kivy.graphics import Color
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window

class planet(Ellipse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Display(Widget):
    def __init__(self):
        super().__init__()
        Window.size = (600, 600)
        a = random.randint(0, 300)
        b = random.randint(0, 300)
        for x in range(-a, a):
            y = ((((a**2)*(b**2)) - ((b**2)*(x**2)))/(a**2))**0.5
            self.draw_path(x, y)
            # with self.canvas:
            #     Color(1, 0, 1, 1)
            #     planet(pos=(x+300, y+300), size=(2, 2))
            #     planet(pos=(x+300, z+300), size=(2, 2))

    def draw_path(self, x, y):
        with self.canvas:
            Color(1, 0, 1, 1)
            planet(pos=(x + 300, y + 300), size=(2, 2))
            planet(pos=(x + 300, -y + 300), size=(2, 2))

    # def orbit(self):
        # self.root.ids.orbit.pos = self.generate_ellipse()


class Planet(App):
    # AU is placeholder for distance from the sun
    # def __init__(self, au=1, radius=20, speed=1):
    #     super().__init__()
    #     self.au = au
    #     self.radius = radius
    #     # self.orbit = generate_ellipse()
    #     self.speed = speed
    #     Display().generate_ellipse()

    def build(self):
        self.root = Builder.load_file("solar_system.kv")
        return self.root

Planet().run()
