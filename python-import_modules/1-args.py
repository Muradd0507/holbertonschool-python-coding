#!/usr/bin/python3
argv=[]
for t, argument in enumerate(argv):
    if len(argv) == 0:
        print("0 arguments")
    elif len(argv) == 1:
        print("1 argument\n{}: {}".format(t + 1, argument))
    else:
        print("{} arguments".format(len(argv)))
        print("{}: {}".format(t + 1, argument))