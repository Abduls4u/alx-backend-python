#!/usr/bin/env python3
''' 8-make_multiplier.py module '''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' create multiplier'''
    def mul(val: float):
        '''mul function'''
        return (val * multiplier)
    return (mul)
