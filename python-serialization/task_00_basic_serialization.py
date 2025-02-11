#!/usr/bin/env python3
"""
Module: basic serialization
Provides 'basic serialization'
"""
import pickle
""" import pickle"""


def serialize_and_save_to_file(data, filename):
    with open(filename, "w") as file:
        return pickle.dump(data, file)
    pass


def load_and_deserialize(filename):
    with open(filename, "r") as file:
        return pickle.load(file)
    pass
