#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    cop = a_dictionary
    for key, val in cop.items():
        if val == value:
            del cop[key]
            break
    return cop
