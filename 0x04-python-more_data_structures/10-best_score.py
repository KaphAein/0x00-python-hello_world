#!/usr/bin/python3
def best_score(a_dictionary):
    max_value = 0
    if a_dictionary == None:
        return None
    for i in a_dictionary:
        if a_dictionary[i][1] > max_value:
            max_value = a_dictionary[i][1]
    return max_value
