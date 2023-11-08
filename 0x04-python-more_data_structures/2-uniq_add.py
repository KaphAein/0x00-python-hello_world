#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    for element in my_list:
        if my_list.count(element) > 1:
            continue
        else:
            result += element
    return result
