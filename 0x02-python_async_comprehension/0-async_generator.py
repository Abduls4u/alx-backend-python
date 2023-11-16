#!/usr/bin/env python3
'''0-async_generator.py module'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''async generator funtion'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield (random.random() * 10)