#!/usr/bin/env python3
''' 6-sum_mixed_list.py module '''
from typing import List, Union


def sum_mixed_list(input_list: List[Union[int, float]]) -> float:
    '''returns sum of list items'''
    sum = 0.0
    for i in input_list:
        sum += i
    return (sum)
