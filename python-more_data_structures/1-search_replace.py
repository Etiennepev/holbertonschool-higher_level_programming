#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for index in range(len(new_list)):
        if new_list[index] == 2:
            new_list[index] = 89
    return new_list
