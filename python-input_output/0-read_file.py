#!/usr/bin/python3
"""
Module: read file
Provides 'Read file'
"""


def read_file(filename=""):
    with open("my_file_0.txt", "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip(), end="")
