#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    count = len(my_list) - 1
    for i in range(count + 1):
        if i < count:
            temp = my_list[i]
            my_list[i] = my_list[count - i]
            my_list[count - i] = temp
        print("{}".format(my_list[i]))
