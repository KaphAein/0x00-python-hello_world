#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary and value:
        for key, val in a_dictionary.items():
            if val == value:
                del val
        return a_dictionary
