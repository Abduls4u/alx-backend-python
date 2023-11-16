#!/usr/bin/env python3
'''2-measure_runtime.py modules'''
import asyncio
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''measure time function'''
    start = time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    stop = time()
    elapsed_time = stop - start
    return (elapsed_time)
