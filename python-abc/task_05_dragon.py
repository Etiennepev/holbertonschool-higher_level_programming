#!/usr/bin/python3
"""
Module: flying fish
Provides 'FlyingFish'
"""
from abc import ABC


class SwimMixin:
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    def fly(self):
        print("The creature flies!")
    
class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")
