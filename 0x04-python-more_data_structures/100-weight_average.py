#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    sum_score = 0
    agg = 0
    else:
        for key, value in my_list.items():
            sum_score += value
            agg += key * value
        return  agg / sum_score
