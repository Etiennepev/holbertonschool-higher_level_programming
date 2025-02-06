#!/usr/bin/python3

"""
Module task_01_abc.py
Provides an ABC class Shape
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    ABC class Shape
    """

    @abstractmethod
    def area(self):
        """
        area ABC method
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        perimeter ABC method
        """
        pass


class Circle(Shape):
    """
    Circle class
    """

    def __init__(self, radius):
        """
        Initialize the Circle class
        """
        self.__radius = abs(radius)

    def area(self):
        """
        area method
        """
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        """
        perimeter method
        """
        return math.pi * self.__radius * 2


class Rectangle(Shape):
    """
    Rectangle class
    """

    def __init__(self, width, height):
        """
        Initialize the Rectangle class
        """
        self.__width = width
        self.__height = height

    def area(self):
        """
        area method
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        perimeter method
        """
        return 2 * (self.__height + self.__width)


def shape_info(shape):
    """
    shape_info methode
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


if __name__ == "__main__":

    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=7)

    shape_info(circle)
    shape_info(rectangle)
