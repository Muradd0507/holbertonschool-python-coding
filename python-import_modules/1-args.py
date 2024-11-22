#!/usr/bin/python3
import sys

if __name__ == "__main__":

    argv = sys.argv
    if len(argv) > 0:
        argv = argv[1:]
    for t, argument in enumerate(argv):
        if len(argv) == 0:
            print("0 arguments")
        elif len(argv) == 1:
            print("1 argument\n{}: {}\n".format(t + 1, argument))
        else:
            print("{} arguments".format(len(argv)))
            print("{}: {}\n".format(t + 1, argument))
