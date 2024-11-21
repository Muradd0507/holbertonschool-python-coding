#!/usr/bin/python3
def best_score(a_dictionary):
    m = 0
    if len(a_dictionary) > 0 and a_dictionary != None:
        for i in a_dictionary:
            if a_dictionary[i] > m:
                m = a_dictionary[i]
        for i, j in a_dictionary.items():
            if j == m:
                return i
    else:
        return None
