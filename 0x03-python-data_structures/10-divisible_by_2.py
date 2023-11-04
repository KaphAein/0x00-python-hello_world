#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    boo = []
    for i in my_list:
        if i % 2 == 0:
            boo += "True"
        else:
            boo += "False"
    return boo
