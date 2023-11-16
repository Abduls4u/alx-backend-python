#!/usr/bin/env python3
'''1-async_comprehension.py module '''
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''async comprehension'''
    return ([_ async for _ in async_generator()])
