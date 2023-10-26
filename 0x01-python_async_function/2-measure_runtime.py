#!/usr/bin/env python3
''' 2-measure_runtime.py module '''
import asyncio
from time import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''measure runtime of wait_n '''
    start_time = time()
    asyncio.run(wait_n(n, max_delay))
    stop_time = time()
    elapsed_time = stop_time - start_time
    return (elapsed_time / n)
