#!/usr/bin/python3
"""Module that finds a peak in a list of integers"""


def find_peak(list_of_integers):
    '''function body'''
    int_list = list_of_integers
    if int_list == []:
        return None
    list_len = len(int_list)
    start, end = 0, list_len - 1
    while start < end:
        mid = start + (end - start) // 2
        if (int_list[mid] > int_list[mid - 1]) and (int_list[mid] > int_list[mid + 1]):
            return int_list[mid]
        elif int_list[mid - 1] > int_list[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return int_list[start]
