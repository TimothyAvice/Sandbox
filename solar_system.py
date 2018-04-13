import random


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
        self.generate_sun()
        self.generate_path()

    def generate_sun(self):
        with self.canvas:
            Color(1, 1, 0, 1)
            planet(pos=(265, 265), size=(70, 70))

    def generate_path(self):
        a = random.randint(50, 300)
        b = random.randint(50, 300)
        for x in range(-a, a):
            y = ((((a**2)*(b**2)) - ((b**2)*(x**2)))/(a**2))**0.5
            self.draw_path(x, y)
        x = random.randint(-a,a)
        y = ((((a ** 2) * (b ** 2)) - ((b ** 2) * (x ** 2))) / (a ** 2)) ** 0.5
        z = random.choice([y, -y])
        self.generate_planet(x, z)

    def draw_path(self, x, y):
        with self.canvas:
            Color(1, 0, 1, 1)
            planet(pos=(x + 300, y + 300), size=(1, 1))
            planet(pos=(x + 300, -y + 300), size=(1, 1))

    def generate_planet(self, x, z):
        size = self.planet_size()
        with self.canvas:
            self.planet_color()
            planet(pos=(x + (300 - (size/2)), z + (300-(size/2))), size=(size, size))

    @staticmethod
    def planet_color():
        red = random.uniform(0.0, 1.0)
        blue = random.uniform(0.0, 1.0)
        green = random.uniform(0.0, 1.0)
        return Color(red, green, blue)

    @staticmethod
    def planet_size():
        size = random.uniform(10, 50)
        return size


class Planet(App):
    # AU is placeholder for distance from the sun
    def __init__(self, au=1, radius=20, speed=1):
        super().__init__()
    #     self.au = au
    #     self.radius = radius
    #     # self.orbit = generate_ellipse()
    #     self.speed = speed
    #     Display().generate_ellipse()

    def build(self):
        self.root = Builder.load_file("solar_system.kv")
        return self.root


Planet().run()
