#!/usr/bin/env python3

"""
    This module contains a coroutine that takes no
    argument. It loops 10 times, each time asynchronously wait
    1 second, then yield a random number between 0 and 10.
    I am using random module
"""

import asyncio
import random
"""
    Imported asyncio and random modules, the random will
    help us to generate random numbers, whereas asyncio will
    help us to run the code asynchronously
"""


async def async_generator():
    """
        This coroutine takes no argument, it will
        generate random numbers between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
