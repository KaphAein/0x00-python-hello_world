#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    count = len(my_list) - 1
    if idx < 0 or idx > len(count):
        return my_list
    else:
        for i in range(count + 1):
            if i == idx:
                continue
            else:
                new_list[i] = my_list[i]
