import math as m
import random

class Circle:
    def __init__(self, radius, position=(0, 0)):
        self.radius = radius
        self.position = position

    def real_area(self):
        return m.pi * self.radius * self.radius  # m.pi is a constant in math module

    def is_inside(self, point):
        point_x, point_y = point
        center_x, center_y = self.position
        return (point_x - center_x) ** 2 + (point_y - center_y) ** 2 <= self.radius**2

class Square:
    def __init__(self,length,position=(0, 0),function_mode=False,):  
    # if function_mode is True, the left down corner is in the origin the center of the square is the position
        self.length = length
        self.position = position
        self.function_mode = function_mode

    def area(self):
        return self.length * self.length

    def random_point(self):
        if self.function_mode:
            x, y = 0, 0  # set origin as the bottom-left corner
        else:
            # adjust position so that (x, y) represents the center of the square
            x, y = (
                self.position[0] - self.length / 2,
                self.position[1] - self.length / 2,
            )

        x_rand = random.uniform(x, x + self.length)
        y_rand = random.uniform(y, y + self.length)
        return (x_rand, y_rand)

class exponential_function:  # a * exp(b * x)
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def value(self, x):
        return self.a * m.exp(self.b * x)

    def real_area(self, x0, x1):  # integral from x0 to x1 of a * exp(b * x) dx
        return (self.a / self.b) * (m.exp(self.b * x1) - m.exp(self.b * x0))

    def is_inside(self, point):
        x, y = point
        return y <= self.value(x)