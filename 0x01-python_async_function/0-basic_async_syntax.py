#!/usr/bin/env python3
''' 0-basic_async_syntax.py module '''
import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> Union[int, float]:
    '''async coroutine that returns random delay'''
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return (random_delay)


if __name__ == '__main__':
    asyncio.run(wait_random())