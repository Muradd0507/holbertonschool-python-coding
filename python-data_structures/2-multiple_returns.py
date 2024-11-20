#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence != "":
        tup1 = (len(sentence),)
        tup2 = (sentence[0],)
        tup = tup1 + tup2
        return tup
    else:
        return (len(sentence), sentence[0] if sentence else None)

