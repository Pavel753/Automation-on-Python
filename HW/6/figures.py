from math import pi


class Rectangle:
    def __init__(self, a, b):
        self.length = a
        self.width = b

    def get_area(self):
        return self.length * self.width


class Square:
    def __init__(self, a):
        self.side = a

    def get_area_square(self):
        return self.side ** 2


class Circle:
    def __init__(self, r):
        self.radius = r

    def get_area_circle(self):
        return pi * self.radius ** 2
