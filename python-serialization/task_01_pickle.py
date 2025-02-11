#!/usr/bin/env python3
"""
Module: basic serialization
Provides 'basic serialization'
"""
import pickle
""" import pickle"""


class CustomObject:
    """
    A class to represent a custom object with basic attributes.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
        is_student (bool): A flag indicating whether the person is a student.
    """
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        for attr, value in self.__dict__.items():
            print("{}: {}".format(attr, value))

    def serialize(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError, EOFError) as e:
            return None
