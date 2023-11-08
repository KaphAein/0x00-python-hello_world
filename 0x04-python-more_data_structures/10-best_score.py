#!/usr/bin/python3
def best_score(a_dictionary):
    max_value = 0
    if a_dictionary is None:
        return None
    for value in a_dictionary.values():
        if (value > max_value and isinstance(value, int)) or (max_value is None and isinstance(value, int)):
            max_value = value
    return max_value
