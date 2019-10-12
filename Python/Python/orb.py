import random

from kivy.app import App
from kivy.graphics import Ellipse
from kivy.graphics import Color
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window

INCREMENT = -5 * 50000

class Orb(Ellipse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Display(Widget):
    def __init__(self):
        super().__init__()
        Window.size = (1000, 900)
        self.path_a = random.uniform(50, 500)
        self.path_b = random.uniform(50, 500)
        self.x = -self.path_a
        self.y = 400
        self.z = -400
        self.count = 1
        # self.planet = self.generate_planet()
        self.event = Clock.schedule_interval(self.follow_path, INCREMENT)
        # self.canvas.add(self.planet)

    def stop(self):
        Clock.unschedule(self.event)

    def start(self):
        self.event = Clock.schedule_interval(self.follow_path, INCREMENT)

    def variables(self):
        global INCREMENT
        self.path_a = random.uniform(50, 300)
        self.path_b = random.uniform(50, 300)
        self.x = -self.path_a
        self.y = 400
        self.z = -400
        self.count = 1
        self.event = Clock.schedule_interval(self.follow_path, INCREMENT)
        # self.planet = self.generate_planet()
        # self.canvas.add(self.planet)

    @staticmethod
    def orb_color():
        red = random.uniform(0.0, 1.0)
        blue = random.uniform(0.0, 1.0)
        green = random.uniform(0.0, 1.0)
        gamma = random.uniform(0.5, 1.0)
        return Color(red, blue, green, gamma)

    def follow_path(self, _):
        # self.planet.pos = (self.x + 500, self.y + 400)
        if self.count == 1:
            if self.x <= self.path_a:
                self.y = (((((self.path_a ** 2) * (self.path_b ** 2)) - ((self.path_b ** 2) *
                                                                         (self.x ** 2))) / (self.path_a ** 2)) ** 0.5)
                self.x += 1
                self.generate_orb()
            else:
                self.count += 1
                self.x = self.path_a
        else:
            if self.x >= -self.path_a:
                self.y = (((((self.path_a ** 2) * (self.path_b ** 2)) - ((self.path_b ** 2) *
                                                                         (self.x ** 2))) / (self.path_a ** 2)) ** 0.5)
                self.y = -self.y
                self.x -= 1
                self.generate_orb()
            else:
                self.count -= 1
                self.x = -self.path_a

    def generate_orb(self):
        size = random.uniform(10, 50)
        with self.canvas:
            self.orb_color()
            Orb(pos=(self.x+500, self.y+400), size=(size, size))

    # def generate_planet(self):
    #     return Planet(pos=(self.x, self.y), size=(self.planet_size, self.planet_size))


class OrbApp(App):
    def __init__(self):
        super().__init__()

    def build(self):
        self.root = Builder.load_file("orb.kv")
        return self.root


OrbApp().run()
