import random

from kivy.app import App
from kivy.graphics import Ellipse
from kivy.graphics import Color
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window


class Planet(Ellipse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Display(Widget):
    def __init__(self):
        super().__init__()
        Window.size = (1000, 800)
        self.path_a = random.uniform(50, 300)
        self.path_b = random.uniform(50, 300)
        self.x = -self.path_a
        self.y = 400
        self.z = -400
        self.count = 1
        self.planet = self.generate_planet()
        Clock.schedule_interval(self.follow_orbit, 0.001)
        self.canvas.add(self.planet)

    def variables(self):
        self.path_a = random.uniform(50, 300)
        self.path_b = random.uniform(50, 300)
        self.x = -self.path_a
        self.y = 400
        self.z = -400
        self.count = 1
        self.planet = self.generate_planet()
        self.canvas.add(self.planet)

    @staticmethod
    def planet_color():
        red = random.uniform(0.0, 1.0)
        blue = random.uniform(0.0, 1.0)
        green = random.uniform(0.0, 1.0)
        return Color(red, blue, green)

    def follow_orbit(self, _):
        self.planet.pos = (self.x + 500, self.y + 400)
        if self.count == 1:
            if self.x <= self.path_a:
                self.y = (((((self.path_a ** 2) * (self.path_b ** 2)) - ((self.path_b ** 2) *
                                                                         (self.x ** 2))) / (self.path_a ** 2)) ** 0.5)
                self.x += 1
            else:
                self.count += 1
                self.x = self.path_a
        else:
            if self.x >= -self.path_a:
                self.y = (((((self.path_a ** 2) * (self.path_b ** 2)) - ((self.path_b ** 2) *
                                                                         (self.x ** 2))) / (self.path_a ** 2)) ** 0.5)
                self.y = -self.y
                self.x -= 1
            else:
                self.count -= 1
                self.x = -self.path_a

    def generate_planet(self):
        size = random.uniform(10, 50)
        return Planet(pos=(self.x, self.y), size=(size, size))


class PlanetApp(App):
    def __init__(self):
        super().__init__()

    def build(self):
        self.root = Builder.load_file("planet.kv")
        return self.root


PlanetApp().run()
