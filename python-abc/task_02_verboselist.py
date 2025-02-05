#!/usr/bin/python3
"""
Module: verbose list
Provides a verbose list
"""
from abc import ABC, abstractmethod


class VerboseList(list):
    """
    Abstact class Verbose list.
    """
    pass

def __init__(self, *args):
    super().__init__(*args)

def append(self, item):
    print("Added {} to the list.".format(item))
    super().append(item)

def extend(self, x):
    print("Extended the list with {} items.".format(len(x)))
    super().extend(item)
    
def remove(self, item):
    print("Removed {} from the list.".format(item))
    super().remove(item)
  
def pop(self, index=-1):
    item = super().pop(index)
    print("Popped {} from the list.".format(item))
    return item
