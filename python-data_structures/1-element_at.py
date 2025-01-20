#!/usr/bin/python3

def element_at(my_list, idx):
    if idx > my_list:
        return None
    if idx < 0:
        return None
    print("Element at index {:d} is {:d}".format(idx, my_list))
