#!/usr/bin/env python3

"""
    This module contains a coroutine that imports async_comprehension
    from the 1-async_comprehension.py. It will execute
    async_comprehension four times in parallel using asyncio.gather.

    The coroutine should measure the total runtime and return it
"""

import asyncio
from time import perf_counter
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
        This coroutine will execute async_comprehension
        four times in parallel using asyncio.gather.

        It should measure the total runtime and return it
    """

    start_time = perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = perf_counter()
    return end_time - start_time
