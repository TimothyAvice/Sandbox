import random
import math

from kivy.app import App
from kivy.graphics import Ellipse
from kivy.graphics import Color
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.clock import Clock

class planet(Ellipse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Display(Widget):
    def __init__(self):
        super().__init__()
        # y = random.randint(1, 40)
        a = random.randint(1, 40)
        b = random.randint(1, 40)
        for i in range(-5, 5):
            y = math.sqrt((((a**2)*(b**2)) - ((b**2)*(i**2)))/(a**2))
            for n in range(-5, 5):
                x = math.sqrt((((a**2)*(b**2)) - ((a**2)*(n**2))) / (b ^ 2))
        # for x in range(0, 10):
        #     y = 5
                with self.canvas:
                    Color(1, 1, 1, 1)
                    planet(pos=(x+400, y+400), size=(2,2))


        # x = math.sqrt((((a^2)*(b^2)) - ((a^2)*(y^2)))/(b^2))
        # return a, b

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
