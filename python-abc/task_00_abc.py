#!/usr/bin/python3
"""
Module: task abc
Provides an ABC class Animal with two subclasses
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstact class of the representation of animal.
    """
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    """
    Concrete class representing a dog.
    """
    def sound(self):
        return "Bark"

class Cat(Animal):
    """
    Concrete class representing a cat.
    """
    def sound(self):
        return "Meow"
