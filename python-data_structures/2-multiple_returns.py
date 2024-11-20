#!/usr/bin/python3
def multiple_returns(sentence):
    tup1 = (len(sentence),)
    tup2 = (sentence[0],)
    tup = tup1 + tup2
    return tup
