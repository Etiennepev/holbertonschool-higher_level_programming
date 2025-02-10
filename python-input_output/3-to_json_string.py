#!/usr/bin/python3
"""
Module: json file
Provides 'json file'
"""
import json


def to_json_string(my_obj):
    json_string = json.dumps(my_obj)
    return json_string
