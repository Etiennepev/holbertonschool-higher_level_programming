#!/usr/bin/python3
"""
Module: json file
Provides 'json file'
"""
import json
""" import json"""


def load_from_json_file(filename):
    """
    returns an object represented by a JSON string
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
