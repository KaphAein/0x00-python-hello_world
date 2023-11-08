#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_dictionary = [[x * 2 for x in row] for row in a_dictionary]
    return a_dictionary
