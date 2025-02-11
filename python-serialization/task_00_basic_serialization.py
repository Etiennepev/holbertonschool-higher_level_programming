#!/usr/bin/env python3
"""
Module: basic serialization
Provides 'basic serialization'
"""
import json
""" import json"""


def serialize_and_save_to_file(data, filename):
    with open(filename, "w") as file:
        return json.dump(data, file)
    pass


def load_and_deserialize(filename):
    with open(filename, "r") as file:
        return json.load(file)
    pass
