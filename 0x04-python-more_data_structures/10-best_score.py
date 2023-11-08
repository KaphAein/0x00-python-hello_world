#!/usr/bin/python3
def best_score(a_dictionary):
    max_value = 0
    if a_dictionary is None:
        return None
    for value in a_dictionary.values():
        if isinstance(value, int):
            if max_value == 0 or value > max_value:
                max_value = value
    return max_value
