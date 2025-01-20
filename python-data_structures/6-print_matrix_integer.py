#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for idx in range(len(line)):
            if idx < len(line) - 1:
                print("{:d}".format(line[idx]), end=" ")
            else:
                print("{:d}".format(line[idx]), end="\n")
