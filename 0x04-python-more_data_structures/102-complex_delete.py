#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    del_key = []

    if a_dictionary is not None and value is not None:
        for key, val in a_dictionary.items():
            if val == value:
                del_key.append(key)

        for key in del_key:
            del a_dictionary[key]
        return a_dictionary
