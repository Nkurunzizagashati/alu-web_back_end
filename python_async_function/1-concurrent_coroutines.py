#!/usr/bin/env python3

"""
    This module contains an async routine called wait_n,
    it takes in 2 int arguments n, and max_delay,
    it will spawn wait_random n times with the specified max_delay.
    wait_n should return the list of all the delays (float values).
    The list of the delays should be in ascending order without using sort() because of concurrency
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
        This async routine takes in two int arguments and
        returns a list of all the delays
    """

    return [i async for i in wait_random()]
