#!/usr/bin/python3
"""
Module: json file
Provides 'json file'
"""
import json
""" import json"""


def save_to_json_file(my_obj, filename):
    """
    returns an object represented by a JSON string
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
