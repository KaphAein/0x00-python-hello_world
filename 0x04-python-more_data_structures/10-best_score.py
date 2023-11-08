#!/usr/bin/python3
def best_score(a_dictionary):
    max_value = 0
    if a_dictionary is None:
        return None
    for i in a_dictionary:
        if isinstance(a_dictionary[i], int):
            if max_value == 0 or a_dictionary[i] > max_value:
                max_value = a_dictionary[i]
                max_key = i
    return max_key
