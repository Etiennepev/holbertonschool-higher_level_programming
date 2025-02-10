#!/usr/bin/python3
"""
Module: json file
Provides 'json file'
"""
import json
""" import json"""


def from_json_string(my_str):
    """
    returns an object represented by a JSON string
    """
    return json.loads(my_str)
