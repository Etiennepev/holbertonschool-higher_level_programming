#!/usr/bin/python3
"""
Module: duck typing
Provides a duck tyîng
"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """
    Abstact class of the Shape.
    """
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius=0):
        self.radius = abs(radius)

    def area(self):
        return pi * (self.radius ** 2)
    
    def perimeter(self):
        return pi * self.radius * 2

class Rectangle(Shape):
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)
    
def shape_info(shape):
    """
    shape_info methode
    """
    if hasattr(shape,"area") and hasattr(shape, "perimeter"):
        print("Area : {}".format(shape.area()))
        print("Perimeter: {}".format(shape.perimeter()))
