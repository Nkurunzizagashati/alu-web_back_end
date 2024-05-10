#!/usr/bin/env python3

"""
    This module contains a with two arguments n and max_delay
    which are both integers. It measures the total execution
    time for wait_n(n, max_delay) and returns the total_time/n
    which should be a float.
"""

import asyncio
from time import time
wait_n = __import__('1-concurent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
        measures the total execution time for wait_n(n, max_delay),
        and returns total_time / n. Your function should return
        a float
    """

    start_time = time()
    await wait_n(n, max_delay)
    end_time = time()
    elapsed_time = end_time - start_time
    return elapsed_time/n
