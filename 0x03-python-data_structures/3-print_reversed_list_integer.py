#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        count = len(my_list) - 1
        for i in range(count + 1):
            if i < count - i:
                temp = my_list[i]
                my_list[i] = my_list[count - i]
                my_list[count - i] = temp
            print("{:d}".format(my_list[i]))
