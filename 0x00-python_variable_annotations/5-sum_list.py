#!/usr/bin/env python3
''' 5-sum_list.py module '''
import typing


def sum_list(input_list: typing.List[float]) -> float:
    '''returns sum of list items'''
    sum = 0.0
    for i in input_list:
        sum += i
    return (sum)
