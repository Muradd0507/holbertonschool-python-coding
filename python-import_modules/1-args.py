#!/usr/bin/python3
import sys

if __name__ == "__main__":

    argv = sys.argv
    if len(argv) > 0:
        argv = argv[1:]
    if len(argv) != 1:
        print("{} arguments:".format(len(argv)))
    if len(argv) == 0:
        print("0 arguments.")
    else:
        print("1 argument:")

    for t, argument in enumerate(argv):
        if len(argv) == 0:
            pass
        elif len(argv) == 1:
            print("{}: {}".format(t + 1, argument))
        else:
            print("{}: {}".format(t + 1, argument))
