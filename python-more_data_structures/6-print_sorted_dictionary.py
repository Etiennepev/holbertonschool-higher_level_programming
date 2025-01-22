#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    key = a_dictionary.keys()
    sort_keys = sorted(key)
    for key in sort_keys:
        print(f"{key}: {a_dictionary[key]}")
