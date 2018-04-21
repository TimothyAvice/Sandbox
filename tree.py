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
        self.length = 30
        self.angle = 1
        self.initialise()
        self.draw()
        # self.event = Clock.schedule_interval(self.generate, 0.1)
        # self.event2 = Clock.schedule_interval(self.draw, 0.1)

    def initialise(self):
        i = 0
        temp_list = []
        while i <= self.length:
            x = 400
            y = i
            i += 2
            new_point = Point(x, y)
            temp_list.append(new_point)
            self.points.append(new_point)
        for item in temp_list:
            with self.canvas:
                branch = Tree(pos=(item.x, item.y), size=(2, 2))
                self.canvas.add(branch)

    def draw(self):
        start_x = self.points[len(self.points)-1].x
        start_y = self.points[len(self.points)-1].y
        i = 0
        temp_list = []
        while i <= self.length:
            x = start_x + (self.angle + i)
            y = start_y + i
            x2 = start_x - (self.angle + i)
            y2 = start_y + i
            i += 1
            new_point = Point(x, y)
            new_point2 = Point(x2, y2)
            temp_list.append(new_point)
            temp_list.append(new_point2)
        for item in temp_list:
            with self.canvas:
                branch = Tree(pos=(item.x, item.y), size=(2, 2))
                self.canvas.add(branch)



class Run(App):
    def build(self):
        return Display()


Run().run()