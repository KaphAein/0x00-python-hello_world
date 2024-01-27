#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    count = len(my_list) - 1
    new_list = my_list

    if idx < 0 or idx > count:
        return my_list
    else:
        del new_list[idx]
    return new_list
