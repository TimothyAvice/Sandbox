import random

from kivy.app import App
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window


class Tree(Rectangle):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Point:
    def __init__(self, x=400, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)


class Display(Widget):
    def __init__(self):
        super().__init__()
        self.points = []
        self.height = 8
        self.current = []
        self.initialise()
        self.event = Clock.schedule_interval(self.generate, 0.1)
        self.event2 = Clock.schedule_interval(self.draw, 0.1)

    def initialise(self):
        y = 0
        for i in range(self.height+1):
            new_point = Point(400, 2 + y)
            self.points.append(new_point)
            self.current.append(new_point)
            y += 2

    def draw(self, _):
        self.canvas.clear()
        for item in self.points:
            tree = Tree(pos=(item.x, item.y), size=(2, 2))
            self.canvas.add(tree)
            self.current.append(item)

    def generate(self, _):
        # m = len(self.points)
        temp_list = []
        for item in self.points:
            if self.points.index(item) > (len(self.points) - 7):
                x = random.randrange(item.x - 4, item.x + 6, 2)
                y = item.y + 2
                x2 = random.randrange(item.x - 4, item.x + 6, 2)
                y2 = item.y + 2
                new_point = Point(x, y)
                new_point2 = Point(x2, y2)
                temp_list.append(new_point)
                temp_list.append(new_point2)
        self.points += temp_list


class Run(App):
    def build(self):
        return Display()


Run().run()