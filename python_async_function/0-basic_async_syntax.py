#!/usr/bin/env python3

"""
    This module contains a coroutine that takes an int
    argument(max_delay) with a default value of 10. It waits for
    a random delay between 0 to max_delay seconds and eventually
    returns it.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
        This function takes in a max_delay, and int argument
        and wait for a random delay between 0 and max_delay
        and returns the max_delay.
    """

    await asyncio.sleep(random.uniform(0, max_delay))
    return max_delay