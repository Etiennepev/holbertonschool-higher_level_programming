#!/usr/bin/python3
"""
Module: json file
Provides 'json file'
"""
import json
""" import json"""


def to_json_string(my_obj):
    """
    use json for the representation of an object (string)
    """
    return json.dumps(my_obj)
