#!/usr/bin/env python3
"""
Module: basic serialization
Provides 'basic serialization'
"""
import pickle
""" import pickle"""

def serialize_and_save_to_file(data, filename):
    with open(filename, "wb") as file:
        return pickle.dump(data, file)
    pass

def load_and_deserialize(filename):
    with open(filename, "rb") as file:
        return pickle.load(file)
    pass
