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
        self.length = random.randrange(10, 40)
        self.anglex = 1
        self.angley = 0.5
        self.initialise()
        # self.event = Clock.schedule_interval(self.generate, 0.1)
        self.event2 = Clock.schedule_interval(self.draw, 1)

    def stop(self):
        Clock.unschedule(self.event2)
        
    def start(self):
        self.event2 = Clock.schedule_interval(self.draw, 1)

    def tree(self):
        self.points = []
        self.length = random.randrange(10, 40)
        self.anglex = 1
        self.angley = 1
        self.initialise()


    def initialise(self):
        i = 0
        x = random.randrange(100, 800, 100)
        temp_list = []
        while i <= self.length:
            y = i
            i += 2
            new_point = Point(x, y)
            temp_list.append(new_point)
            self.points.append(new_point)
        for item in temp_list:
            with self.canvas:
                branch = Tree(pos=(item.x, item.y), size=(2, 2))
                self.canvas.add(branch)

    def draw(self, _):
        max_y = 0
        i = 0
        xs = []
        for item in self.points:
            if item.y > max_y:
                max_y = item.y
        start_y = max_y
        for item in self.points:
            if item.y == start_y:
                x = item.x
                xs.append(x)
        temp_list = []
        while i <= self.length:
            for item in xs:
                x = item + (self.anglex * i)
                y = start_y + (i * self.angley)
                x2 = item - (self.anglex * i)
                y2 = start_y + (i * self.angley)
                new_point = Point(x, y)
                new_point2 = Point(x2, y2)
                temp_list.append(new_point)
                temp_list.append(new_point2)
                self.points.append(new_point)
                self.points.append(new_point2)
            i += 1
        for item in temp_list:
            with self.canvas:
                branch = Tree(pos=(item.x, item.y), size=(2, 2))
                self.canvas.add(branch)
        addx = random.uniform(0,1)
        addy = random.uniform(0,1)
        self.angley = random.choice([addy, -addy])
        self.anglex = random.choice([addx, -addx])



class Run(App):
    def build(self):
        return Display()


Run().run()