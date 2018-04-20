import random

from kivy.app import App
from kivy.graphics import Ellipse
from kivy.graphics import Color
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window

class LifeForm:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Grid:
    def __init__(self, rows=500, cols=500):
        self.num_rows = rows
        self.num_cols = cols
        self.grid = []

    # def build(self):
    #     for i in range(self.num_rows + 1):
    #         temp = []
    #         for n in range(self.num_cols + 1):
    #             value = "O"
    #             temp.append(value)
    #         self.grid.append(temp)
    #
    # def __repr__(self):
    #     for i in range(self.num_rows):
    #         print(self.grid[i-1])
    #
    # def __str__(self):
    #     for i in range(self.num_rows):
    #         print(self.grid[i-1])