#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence != "":
        tup1 = (len(sentence),)
        tup2 = (sentence[0],)
    else:
        tup1 = (len(sentence),)
        tup2 = None
    tup = tup1 + tup2
    return tup
