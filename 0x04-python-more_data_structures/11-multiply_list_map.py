#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    def mul(x, number):
        return x * number
    return list(map(mul, my_list))
