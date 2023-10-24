#!/usr/bin/env python3
''' 7-to_kv.py module '''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''to_kv function'''
    v_squared: float = v ** 2
    return (k, v_squared)
