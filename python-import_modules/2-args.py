#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":

    if (len(argv) == 1):
        print("{:d} arguments.".format(len(argv) - 1))
    elif (len(argv) == 2):
        print("{:d} argument:".format(len(argv) - 1))
        print("{:d}: {}".format(len(argv) - 1, argv[1]))
    else:
        print("{:d} arguments:".format(len(argv) - 1))
        for i in range(1, len(argv)):
            print("{:d}: {}".format(i, argv[i]))
