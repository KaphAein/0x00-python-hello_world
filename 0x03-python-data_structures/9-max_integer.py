#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    for i in range(len(my_list)):
        if my_list[i] >= my_list[i + 1]:
            maxi = my_list[i]
        else:
            continue
    return maxi
