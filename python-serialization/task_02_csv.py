#!/usr/bin/env python3
"""
Module: basic serialization
Provides 'basic serialization'
"""
import csv 
import json
""" import csv and json"""


def convert_csv_to_json(filename):
    try:
        with open(filename, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            rows = list(csv_reader)
        with open(filename, mode='w', encoding='utf-8') as json_file:
            json.dump(rows, json_file, indent=4)
        return True
    except:
        return False
