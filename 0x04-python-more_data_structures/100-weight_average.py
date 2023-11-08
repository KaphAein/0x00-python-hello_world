#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    sum_score = 0
    agg = 0
    for pair in my_list:
        weight, score = pair
        sum_score += score
        agg += weight * score
    return  agg / sum_score
