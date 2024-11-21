#!/usr/bin/python3
def best_score(a_dictionary):
    m = 0
    for i in a_dictionary:
        if a_dictionary[i] > m:
            m = a_dictionary[i]
    for i, j in a_dictionary.items():
        if j == m:
            s = i
            break
    return i, a_dictionary[i]
