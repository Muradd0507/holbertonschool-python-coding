#!/usr/bin/python3
def no_c(my_string):
    strin = ""
    for i in my_string:
        if i != "c" or i != "C":
            strin += i
    return strin
